"""Behaviour tests for the eval runner (spec #1, seam 1 harness).

A fake `claude` executable stands in for the CLI so the runner's contract
(fixture course folder in, grading.json and exit code out) is tested offline.
"""

import json
import os
import shutil
import stat
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from run_evals import main  # noqa: E402

FAKE_CLAUDE = r'''#!{python}
"""Fake claude CLI. Executor when --plugin-dir is given, grader otherwise."""
import json, os, sys
from pathlib import Path

args = sys.argv[1:]
prompt = args[args.index("-p") + 1]
if "--plugin-dir" in args:
    Path("../executor-args.json").write_text(json.dumps(args))
    Path("produced.md").write_text("FAKE-OUTPUT-MARKER\n")
    Path("seen-files.txt").write_text("\n".join(sorted(os.listdir("."))))
    if os.environ.get("FAKE_WRITE_OUTSIDE"):
        # Like the real CLI: writing outside the working directory needs --add-dir.
        added = [args[i + 1] for i, a in enumerate(args) if a == "--add-dir"]
        if any(Path(d).resolve() == Path("..").resolve() for d in added):
            Path("../year-plan.md").write_text("OUTSIDE-MARKER\n")
    events = [{{"type": "system", "subtype": "init"}}]
    if os.environ.get("FAKE_STRING_MESSAGE"):
        events.append({{"type": "system", "subtype": "notice",
                        "message": "a plain-text notice, not a message object"}})
    if not os.environ.get("FAKE_NO_SKILL"):
        events.append({{"type": "assistant", "message": {{"content": [
            {{"type": "tool_use", "name": "Skill",
              "input": {{"skill": "demo-plugin:doing-things"}}}}]}}}})
    events.append({{"type": "result", "subtype": "success",
                    "result": "Here is the walkthrough. FAKE-REPLY-MARKER"}})
    for e in events:
        print(json.dumps(e))
else:
    ok = (not os.environ.get("FAKE_GRADE_FAIL")
          and "FAKE-OUTPUT-MARKER" in prompt and "FAKE-REPLY-MARKER" in prompt
          and (not os.environ.get("FAKE_WRITE_OUTSIDE") or "OUTSIDE-MARKER" in prompt))
    texts = [line[2:] for line in prompt.splitlines() if line.startswith("- ")]
    grading = {{"expectations": [
        {{"text": t, "passed": ok, "evidence": "fake"}} for t in texts
        if t.startswith("The reply")]}}
    print(json.dumps({{"type": "result", "result": "```json\n" + json.dumps(grading) + "\n```"}}))
'''


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


class RunEvalsTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.evals = self.tmp / "evals"
        self.out = self.tmp / "out"
        self.plugin = self.tmp / "plugin"
        (self.plugin / "skills/doing-things").mkdir(parents=True)
        fake = self.tmp / "fake-claude"
        fake.write_text(FAKE_CLAUDE.format(python=sys.executable))
        fake.chmod(fake.stat().st_mode | stat.S_IEXEC)
        self.fake = fake
        write(self.evals / "doing-things/fixtures/with-profile/class-profile.md", "G10\n")
        self.write_cases(
            [
                {
                    "id": 1,
                    "prompt": "How does the process work?",
                    "expected_output": "A walkthrough.",
                    "files": ["fixtures/with-profile"],
                    "expectations": ["The reply gives the walkthrough"],
                }
            ]
        )
        self._env = dict(os.environ)

    def tearDown(self):
        os.environ.clear()
        os.environ.update(self._env)
        shutil.rmtree(self.tmp)

    def write_cases(self, cases, skill_name="doing-things"):
        write(
            self.evals / "doing-things/evals.json",
            json.dumps({"skill_name": skill_name, "evals": cases}),
        )

    def run_runner(self, *extra):
        return main(
            [
                "doing-things",
                "--evals-dir", str(self.evals),
                "--plugin-dir", str(self.plugin),
                "--out", str(self.out),
                "--claude", str(self.fake),
                *extra,
            ]
        )

    def grading(self) -> dict:
        found = list(self.out.rglob("eval-1/grading.json"))
        self.assertEqual(len(found), 1, f"grading.json files: {found}")
        return json.loads(found[0].read_text())

    def test_passing_case_exits_zero_and_writes_grading(self):
        self.assertEqual(self.run_runner(), 0)
        grading = self.grading()
        self.assertEqual(grading["summary"]["failed"], 0)
        self.assertEqual(grading["summary"]["pass_rate"], 1.0)
        texts = [e["text"] for e in grading["expectations"]]
        self.assertIn("The reply gives the walkthrough", texts)
        for e in grading["expectations"]:
            self.assertEqual(set(e), {"text", "passed", "evidence"})

    def test_case_runs_inside_a_copy_of_its_fixture_folder(self):
        self.run_runner()
        seen = next(self.out.rglob("eval-1/teacher/course/seen-files.txt")).read_text()
        self.assertIn("class-profile.md", seen.split("\n"))
        fixture = self.evals / "doing-things/fixtures/with-profile"
        self.assertEqual(sorted(p.name for p in fixture.iterdir()), ["class-profile.md"])

    def test_teacher_files_are_placed_beside_the_course(self):
        # A year plan the teacher already keeps outside the course folder.
        write(self.evals / "doing-things/fixtures/teacher/year-plan-2569.md", "Year plan\n")
        self.write_cases([{
            "id": 1, "prompt": "Check my year.", "files": ["fixtures/with-profile"],
            "teacher_files": ["fixtures/teacher"],
            "expectations": ["The reply gives the walkthrough"]}])
        self.assertEqual(self.run_runner(), 0)
        teacher = next(self.out.rglob("eval-1/teacher"))
        self.assertEqual((teacher / "year-plan-2569.md").read_text(), "Year plan\n")
        seen = (teacher / "course/seen-files.txt").read_text().split("\n")
        self.assertNotIn("year-plan-2569.md", seen)

    def test_missing_teacher_file_is_rejected(self):
        self.write_cases([{
            "id": 1, "prompt": "Check my year.", "teacher_files": ["fixtures/nope"],
            "expectations": ["The reply gives the walkthrough"]}])
        self.assertEqual(self.run_runner(), 2)

    def test_files_written_just_outside_the_course_are_graded(self):
        # A year plan lives outside the course folder, at a path the teacher gives.
        os.environ["FAKE_WRITE_OUTSIDE"] = "1"
        self.assertEqual(self.run_runner(), 0)
        self.assertEqual(self.grading()["summary"]["failed"], 0)
        self.assertEqual(len(list(self.out.rglob("eval-1/*/year-plan.md"))), 1)

    def test_failed_expectation_exits_one(self):
        os.environ["FAKE_GRADE_FAIL"] = "1"
        self.assertEqual(self.run_runner(), 1)
        self.assertGreater(self.grading()["summary"]["failed"], 0)

    def test_skill_not_invoked_fails_the_case(self):
        os.environ["FAKE_NO_SKILL"] = "1"
        self.assertEqual(self.run_runner(), 1)
        failed = [e["text"] for e in self.grading()["expectations"] if not e["passed"]]
        self.assertTrue(any("doing-things" in t for t in failed), failed)

    def test_events_with_plain_text_message_are_tolerated(self):
        os.environ["FAKE_STRING_MESSAGE"] = "1"
        self.assertEqual(self.run_runner(), 0)
        self.assertEqual(self.grading()["summary"]["failed"], 0)

    def test_case_selection_by_id(self):
        cases = json.loads((self.evals / "doing-things/evals.json").read_text())["evals"]
        cases.append(dict(cases[0], id=2))
        self.write_cases(cases)
        self.assertEqual(self.run_runner("--case", "2"), 0)
        self.assertEqual(list(self.out.rglob("eval-1")), [])
        self.assertEqual(len(list(self.out.rglob("eval-2/grading.json"))), 1)

    def executor_args(self) -> list:
        return json.loads(next(self.out.rglob("eval-1/teacher/executor-args.json")).read_text())

    def test_repo_only_skill_is_loaded_through_a_wrapper_plugin(self):
        shutil.rmtree(self.plugin / "skills/doing-things")
        repo_skills = self.tmp / "repo-skills"
        write(repo_skills / "doing-things/SKILL.md", "---\nname: doing-things\n---\n")
        write(repo_skills / "doing-things/scripts/tool.py", "print(1)\n")
        self.assertEqual(self.run_runner("--repo-skills-dir", str(repo_skills)), 0)
        args = self.executor_args()
        plugin = Path(args[args.index("--plugin-dir") + 1])
        self.assertTrue((plugin / "skills/doing-things/SKILL.md").is_file())
        self.assertTrue((plugin / "skills/doing-things/scripts/tool.py").is_file())
        manifest = json.loads((plugin / ".claude-plugin/plugin.json").read_text())
        self.assertTrue(manifest["name"])
        seen = next(self.out.rglob("eval-1/teacher/course/seen-files.txt")).read_text().split("\n")
        self.assertNotIn("skills", seen)

    def test_unknown_skill_is_a_run_error(self):
        shutil.rmtree(self.plugin / "skills/doing-things")
        self.assertEqual(self.run_runner("--repo-skills-dir", str(self.tmp / "none")), 2)

    def test_case_file_can_allow_extra_executor_tools(self):
        data = json.loads((self.evals / "doing-things/evals.json").read_text())
        data["allowed_tools"] = ["Bash"]
        write(self.evals / "doing-things/evals.json", json.dumps(data))
        self.run_runner()
        args = self.executor_args()
        tools = args[args.index("--allowedTools") + 1].split(",")
        self.assertIn("Bash", tools)
        self.assertIn("Read", tools)

    def test_executor_tools_default_to_no_bash(self):
        self.run_runner()
        args = self.executor_args()
        self.assertNotIn("Bash", args[args.index("--allowedTools") + 1].split(","))

    def test_invalid_case_file_is_rejected_before_running(self):
        for bad in (
            [{"id": 1, "prompt": "x", "files": []}],  # no expectations
            [{"id": 1, "prompt": "x", "expectations": ["e"], "files": ["fixtures/nope"]}],
            [{"id": "one", "prompt": "x", "expectations": ["e"]}],
        ):
            self.write_cases(bad)
            self.assertEqual(self.run_runner(), 2)
        self.write_cases([{"id": 1, "prompt": "x", "expectations": ["e"]}], skill_name="other")
        self.assertEqual(self.run_runner(), 2)
        self.assertFalse(self.out.exists() and any(self.out.rglob("transcript.jsonl")))


class RepoEvalFilesTest(unittest.TestCase):
    """Every committed evals.json must load (no LLM calls)."""

    def test_committed_case_files_are_valid(self):
        from run_evals import load_cases

        files = sorted((ROOT / "evals").glob("*/evals.json"))
        self.assertTrue(files, "no evals/<skill>/evals.json found")
        for path in files:
            cases = load_cases(path.parent)
            self.assertGreaterEqual(len(cases), 1, path)


if __name__ == "__main__":
    unittest.main()
