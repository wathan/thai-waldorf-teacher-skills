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
    Path("produced.md").write_text("FAKE-OUTPUT-MARKER\n")
    Path("seen-files.txt").write_text("\n".join(sorted(os.listdir("."))))
    events = [{{"type": "system", "subtype": "init"}}]
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
          and "FAKE-OUTPUT-MARKER" in prompt and "FAKE-REPLY-MARKER" in prompt)
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
        seen = next(self.out.rglob("eval-1/course/seen-files.txt")).read_text()
        self.assertIn("class-profile.md", seen.split("\n"))
        fixture = self.evals / "doing-things/fixtures/with-profile"
        self.assertEqual(sorted(p.name for p in fixture.iterdir()), ["class-profile.md"])

    def test_failed_expectation_exits_one(self):
        os.environ["FAKE_GRADE_FAIL"] = "1"
        self.assertEqual(self.run_runner(), 1)
        self.assertGreater(self.grading()["summary"]["failed"], 0)

    def test_skill_not_invoked_fails_the_case(self):
        os.environ["FAKE_NO_SKILL"] = "1"
        self.assertEqual(self.run_runner(), 1)
        failed = [e["text"] for e in self.grading()["expectations"] if not e["passed"]]
        self.assertTrue(any("doing-things" in t for t in failed), failed)

    def test_case_selection_by_id(self):
        cases = json.loads((self.evals / "doing-things/evals.json").read_text())["evals"]
        cases.append(dict(cases[0], id=2))
        self.write_cases(cases)
        self.assertEqual(self.run_runner("--case", "2"), 0)
        self.assertEqual(list(self.out.rglob("eval-1")), [])
        self.assertEqual(len(list(self.out.rglob("eval-2/grading.json"))), 1)

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
