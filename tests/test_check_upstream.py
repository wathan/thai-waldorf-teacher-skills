"""Behaviour tests for the repo-only upstream change check (spec #1, issue #17).

Each test writes an upstream record and a recorded upstream state into a temp
dir and runs the check against them, never against live GitHub.
Run: python3 -m unittest discover tests
"""

import io
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".claude/skills/check-upstream/scripts"))

from check_upstream import main  # noqa: E402

K12 = "anthropics/k12-teacher-skills"
MATT = "mattpocock/skills"
OLD, MID, NEW = "a" * 40, "b" * 40, "c" * 40
M_OLD = "1" * 40

RECORD = f"""# Upstream record

## Upstream repositories

| Key | Repo | License | HEAD when first recorded |
|---|---|---|---|
| k12 | {K12} | Apache-2.0 | {OLD} |
| mattpocock | {MATT} | MIT | {M_OLD} |

## Plugin-wide

| Repo | Path | Commit last reviewed | Role | Status |
|---|---|---|---|---|
| k12 | plugin/skills/k12-lesson-plan-creation | {OLD} | structural | firm |

## setting-up-class-profiles

| Repo | Path | Commit last reviewed | Role | Status |
|---|---|---|---|---|
| mattpocock | skills/productivity/grilling | {M_OLD} | pattern | firm |

## guiding-the-workflow

No upstream sources: written fresh.

## planning-main-lesson-blocks

| Repo | Path | Commit last reviewed | Role | Status |
|---|---|---|---|---|
| k12 | plugin/skills/k12-lesson-plan-creation | {OLD} | content | firm |
| k12 | plugin/skills/k12-lesson-prep | {OLD} | content | proposed |

## Pending confirmation

Nothing here is a skill.
"""


def state(k12_commits, matt_commits=()):
    return {
        "recorded_at": "2026-11-01",
        "repos": {
            K12: {"branch": "main", "commits": list(k12_commits)},
            MATT: {"branch": "main", "commits": list(matt_commits) or [
                {"sha": M_OLD, "files": ["skills/productivity/grilling/SKILL.md"]}
            ]},
        },
    }


BASE = {"sha": OLD, "files": ["plugin/skills/k12-lesson-plan-creation/SKILL.md"]}


class CheckUpstreamTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.record = self.tmp / "UPSTREAM.md"
        self.record.write_text(RECORD, encoding="utf-8")
        self.state_path = self.tmp / "upstream-state.json"

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def run_check(self, upstream_state):
        self.state_path.write_text(json.dumps(upstream_state), encoding="utf-8")
        out = io.StringIO()
        code = main(["--record", str(self.record), "--state", str(self.state_path)], out=out)
        return code, out.getvalue()

    def section(self, report, title):
        """Text of the report's '## <title>' section."""
        parts = report.split(f"## {title}\n", 1)
        self.assertEqual(len(parts), 2, f"no '## {title}' section in:\n{report}")
        return parts[1].split("\n## ", 1)[0]

    def test_changed_path_lists_affected_skills_and_changed_files(self):
        code, report = self.run_check(state([
            {"sha": NEW, "files": [
                "plugin/skills/k12-lesson-plan-creation/references/science.md",
                "plugin/skills/k12-lesson-differentiation/SKILL.md",
            ]},
            {"sha": MID, "files": ["plugin/skills/k12-lesson-plan-creation/SKILL.md", "README.md"]},
            BASE,
        ]))
        self.assertEqual(code, 1)
        changes = self.section(report, "Changes worth reviewing")
        for skill in ("plugin-wide", "planning-main-lesson-blocks"):
            self.assertIn(f"### {skill}", changes)
        self.assertIn("plugin/skills/k12-lesson-plan-creation/references/science.md", changes)
        self.assertIn("plugin/skills/k12-lesson-plan-creation/SKILL.md", changes)
        self.assertNotIn("k12-lesson-differentiation", changes)
        self.assertNotIn("README.md", changes)
        self.assertNotIn("setting-up-class-profiles", changes)

    def test_unchanged_sources_are_reported_up_to_date(self):
        code, report = self.run_check(state([
            {"sha": NEW, "files": ["plugin/skills/k12-lesson-plan-creation-v2/SKILL.md"]},
            BASE,
        ]))
        self.assertEqual(code, 0)
        self.assertNotIn("## Changes worth reviewing", report)
        current = self.section(report, "Up to date")
        self.assertIn("setting-up-class-profiles", current)
        self.assertIn("skills/productivity/grilling", current)
        self.assertIn("plugin/skills/k12-lesson-prep", current)
        self.assertIn("planning-main-lesson-blocks", current)

    def test_skill_with_no_sources_and_non_skill_sections(self):
        _, report = self.run_check(state([BASE]))
        self.assertIn("guiding-the-workflow", self.section(report, "No upstream sources"))
        self.assertNotIn("Pending confirmation", report.replace("## Pending", ""))
        self.assertNotIn("Upstream repositories", report)

    def test_recorded_commit_missing_upstream_needs_review(self):
        code, report = self.run_check(state([{"sha": NEW, "files": ["x"]}]))
        self.assertEqual(code, 1)
        problems = self.section(report, "Could not compare")
        self.assertIn("plugin/skills/k12-lesson-plan-creation", problems)
        self.assertIn(OLD[:7], problems)

    def test_report_names_the_recorded_state_it_used(self):
        _, report = self.run_check(state([BASE]))
        self.assertIn("upstream-state.json", report)
        self.assertIn("2026-11-01", report)

    def test_check_never_modifies_the_record_or_other_files(self):
        self.state_path.write_text(
            json.dumps(state([{"sha": NEW, "files": [BASE["files"][0]]}, BASE])), encoding="utf-8"
        )
        before = {p.name: p.read_bytes() for p in self.tmp.iterdir()}
        code = main(["--record", str(self.record), "--state", str(self.state_path)], out=io.StringIO())
        self.assertEqual(code, 1)
        after = {p.name: p.read_bytes() for p in self.tmp.iterdir()}
        self.assertEqual(after, before)
        self.assertEqual(self.record.read_text(encoding="utf-8"), RECORD)

    def test_unknown_repo_key_is_an_error(self):
        self.record.write_text(RECORD.replace("| k12 | plugin/skills/k12-lesson-prep", "| zz | x"))
        code, report = self.run_check(state([BASE]))
        self.assertEqual(code, 2)
        self.assertIn("zz", report)


FAKE_GH = r'''#!{python}
"""Fake gh CLI answering the two read-only endpoints live mode uses."""
import json, sys
args = sys.argv[1:]
with open({log!r}, "a") as log:
    log.write(" ".join(args) + "\n")
assert args[0] == "api", args
endpoint = args[1]
if "/compare/" in endpoint:
    if endpoint.startswith("repos/mattpocock/"):
        print(json.dumps({{"status": "identical", "commits": [], "files": []}}))
    else:
        print(json.dumps({{"status": "ahead", "commits": [{{"sha": "{new}"}}],
                          "files": [{{"filename": "plugin/skills/k12-lesson-prep/SKILL.md"}}]}}))
else:
    print(json.dumps({{"default_branch": "main"}}))
'''


class LiveModeTest(unittest.TestCase):
    """Live mode, with a fake gh standing in for GitHub."""

    def test_live_mode_compares_each_recorded_commit_with_the_default_branch(self):
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp)
        record, log, gh = tmp / "UPSTREAM.md", tmp / "gh.log", tmp / "gh"
        record.write_text(RECORD, encoding="utf-8")
        gh.write_text(FAKE_GH.format(python=sys.executable, log=str(log), new=NEW))
        gh.chmod(0o755)
        out = io.StringIO()
        code = main(["--record", str(record), "--gh", str(gh)], out=out)
        report = out.getvalue()
        self.assertEqual(code, 1, report)
        self.assertIn("live GitHub", report)
        changes = report.split("## Changes worth reviewing", 1)[1].split("\n## ", 1)[0]
        self.assertIn("plugin/skills/k12-lesson-prep/SKILL.md", changes)
        self.assertIn("### planning-main-lesson-blocks", changes)
        self.assertNotIn("plugin-wide", changes)
        calls = log.read_text().splitlines()
        self.assertIn(f"api repos/{K12}/compare/{OLD}...main", calls)
        self.assertEqual(len(calls), len(set(calls)), "each comparison is fetched once")


class EvalFixturesTest(unittest.TestCase):
    """The recorded states behind evals/check-upstream give the outcomes its cases grade."""

    FIXTURES = ROOT / "evals/check-upstream/fixtures"

    def report(self, state_dir):
        out = io.StringIO()
        code = main(["--record", str(self.FIXTURES / "record/UPSTREAM.md"),
                     "--state", str(self.FIXTURES / state_dir / "upstream-state.json")], out=out)
        return code, out.getvalue()

    def test_changed_state(self):
        code, report = self.report("state-changed")
        self.assertEqual(code, 1)
        changes = report.split("## Changes worth reviewing")[1].split("\n## ")[0]
        for text in ("### planning-main-lesson-blocks", "### mapping-curriculum",
                     "k12-lesson-plan-creation/references/science.md",
                     "coverage-audit/references/worked-examples.md"):
            self.assertIn(text, changes)
        for text in ("README.md", "crosswalk-v2", "code-review", "writing-thai-core-plans"):
            self.assertNotIn(text, changes)

    def test_unchanged_state(self):
        code, report = self.report("state-unchanged")
        self.assertEqual(code, 0)
        self.assertNotIn("## Changes worth reviewing", report)

    def test_rewritten_state(self):
        code, report = self.report("state-rewritten")
        self.assertEqual(code, 1)
        self.assertIn("### writing-thai-core-plans", report)
        problems = report.split("## Could not compare")[1].split("\n## ")[0]
        self.assertIn("k12-lesson-plan-creation` at `31fd6db`", problems)


class RealRecordTest(unittest.TestCase):
    """The committed UPSTREAM.md must parse: every row has a known repo and a full SHA."""

    def test_committed_record_parses(self):
        from check_upstream import parse_record

        record = parse_record((ROOT / "UPSTREAM.md").read_text(encoding="utf-8"))
        self.assertIn("check-upstream", record.no_sources)
        self.assertTrue(record.rows)
        for row in record.rows:
            self.assertRegex(row.commit, r"^[0-9a-f]{40}$", row)


if __name__ == "__main__":
    unittest.main()
