#!/usr/bin/env python3
"""Run a skill's behaviour evals headlessly (spec #1, seam 1).

Usage:
  uv run --no-project python scripts/run_evals.py <skill> [--case ID ...]
      [--model M] [--grader-model M] [--max-turns N] [--out DIR]

Cases live in evals/<skill>/evals.json in skill-creator's format:

  {"skill_name": "<skill>",
   "evals": [{"id": 1, "prompt": "...", "expected_output": "...",
              "files": ["fixtures/<folder-or-file>"], "expectations": ["..."]}]}

`files` are relative to evals/<skill>/; each is copied into an empty course
folder (a directory's contents, or a single file) that becomes the working
directory of a `claude -p` run with the plugin loaded via --plugin-dir. A
skill not in the plugin is looked up in --repo-skills-dir (.claude/skills,
repo-only) and loaded through a throwaway wrapper plugin. An optional
top-level "allowed_tools" list adds executor tools (e.g. "Bash") for that
skill's cases. The course folder sits in a teacher folder that the run may
also write to (a year plan lives outside the course); a case's optional
"teacher_files" are copied into that teacher folder, beside the course. A
second `claude -p` call grades the reply and the files left in both folders
against the expectations. The runner adds one deterministic
expectation: the skill under test was invoked.

Per case it writes <out>/<skill>/<timestamp>/eval-<id>/ with teacher/course/,
transcript.jsonl, final_message.md and grading.json (skill-creator grader
schema: expectations[{text, passed, evidence}] and summary). Exit status:
0 all expectations passed, 1 some failed, 2 invalid case file or run error.

Needs Claude credentials; not run in CI. Standard library only.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DEFAULT_PLUGIN = REPO / "plugins/thai-waldorf-science"
DEFAULT_REPO_SKILLS = REPO / ".claude/skills"
EXECUTOR_TOOLS = "Read,Glob,Grep,Write,Edit,Skill"
MAX_FILE_CHARS = 20000


class CaseError(ValueError):
    pass


def load_cases(skill_evals_dir: Path) -> list:
    """Load and check evals.json; raise CaseError on any schema problem."""
    return load_suite(skill_evals_dir)[0]


def load_suite(skill_evals_dir: Path) -> tuple:
    """Return (cases, extra executor tools) from evals.json, checked."""
    path = skill_evals_dir / "evals.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CaseError(f"{path}: {exc}")
    if data.get("skill_name") != skill_evals_dir.name:
        raise CaseError(f"{path}: skill_name must be {skill_evals_dir.name!r}")
    cases = data.get("evals")
    if not isinstance(cases, list) or not cases:
        raise CaseError(f"{path}: 'evals' must be a non-empty list")
    seen = set()
    for case in cases:
        cid = case.get("id")
        if not isinstance(cid, int) or isinstance(cid, bool) or cid in seen:
            raise CaseError(f"{path}: each case needs a unique integer id (got {cid!r})")
        seen.add(cid)
        if not isinstance(case.get("prompt"), str) or not case["prompt"].strip():
            raise CaseError(f"{path}: case {cid} needs a prompt")
        exp = case.get("expectations")
        if not isinstance(exp, list) or not exp or not all(isinstance(e, str) for e in exp):
            raise CaseError(f"{path}: case {cid} needs a non-empty list of expectations")
        for rel in [*case.get("files", []), *case.get("teacher_files", [])]:
            if not (skill_evals_dir / rel).exists():
                raise CaseError(f"{path}: case {cid} file {rel} does not exist")
    tools = data.get("allowed_tools", [])
    if not isinstance(tools, list) or not all(isinstance(t, str) and t for t in tools):
        raise CaseError(f"{path}: allowed_tools must be a list of tool names")
    return cases, tools


def copy_in(skill_evals_dir: Path, rels: list, dest: Path) -> None:
    for rel in rels:
        src = skill_evals_dir / rel
        if src.is_dir():
            shutil.copytree(src, dest, dirs_exist_ok=True)
        else:
            shutil.copy2(src, dest / src.name)


def prepare_course(skill_evals_dir: Path, case: dict, course: Path) -> None:
    """Fill the course from `files` and the teacher folder around it from `teacher_files`."""
    course.mkdir(parents=True)
    copy_in(skill_evals_dir, case.get("files", []), course)
    copy_in(skill_evals_dir, case.get("teacher_files", []), course.parent)
    for keep in course.parent.rglob(".gitkeep"):
        keep.unlink()


def child_env() -> dict:
    env = dict(os.environ)
    env.pop("CLAUDECODE", None)  # allow a nested claude -p
    return env


def run_executor(args, case: dict, course: Path, run_dir: Path) -> list:
    cmd = [
        args.claude, "-p", case["prompt"],
        "--plugin-dir", str(Path(args.skill_plugin_dir).resolve()),
        "--add-dir", str(course.parent.resolve()),
        "--output-format", "stream-json", "--verbose",
        "--max-turns", str(args.max_turns),
        "--allowedTools", ",".join([EXECUTOR_TOOLS, *args.extra_tools]),
        "--setting-sources", "project",
        "--strict-mcp-config",
    ]
    if args.model:
        cmd += ["--model", args.model]
    proc = subprocess.run(
        cmd, cwd=course, env=child_env(), capture_output=True, text=True,
        timeout=args.timeout,
    )
    (run_dir / "transcript.jsonl").write_text(proc.stdout, encoding="utf-8")
    if proc.stderr:
        (run_dir / "stderr.txt").write_text(proc.stderr, encoding="utf-8")
    events = []
    for line in proc.stdout.splitlines():
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return events


def final_message(events: list) -> str:
    for event in reversed(events):
        if event.get("type") == "result":
            return event.get("result") or ""
    return ""


def skills_invoked(events: list) -> list:
    names = []
    for event in events:
        message = event.get("message")
        content = message.get("content") if isinstance(message, dict) else None
        for block in content if isinstance(content, list) else []:
            if isinstance(block, dict) and block.get("type") == "tool_use" and block.get("name") == "Skill":
                names.append(str((block.get("input") or {}).get("skill", "")))
    return names


def course_snapshot(course: Path, skip: Path = None) -> str:
    parts = []
    for path in sorted(p for p in course.rglob("*") if p.is_file()):
        if skip is not None and skip in path.parents:
            continue
        rel = path.relative_to(course)
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            parts.append(f"=== {rel} (binary, {path.stat().st_size} bytes)")
            continue
        if len(text) > MAX_FILE_CHARS:
            text = text[:MAX_FILE_CHARS] + "\n[... truncated ...]"
        parts.append(f"=== {rel}\n{text}")
    return "\n\n".join(parts) or "(the course folder is empty)"


GRADER_PROMPT = """You are grading one run of a Claude Code skill against expectations.
Judge only what the evidence shows; an expectation passes only with clear evidence.
Quote or point to the evidence for every verdict.

## Teacher request
{prompt}

## Expected output (human description)
{expected}

## Expectations
{expectations}

## Final reply to the teacher
{reply}

## Files in the course folder after the run
{files}

## Files outside the course folder after the run (paths relative to the folder holding the course, which is `course/`)
{outside}

Respond with only a JSON object, no prose:
{{"expectations": [{{"text": "<expectation, verbatim>", "passed": true, "evidence": "..."}}]}}
"""


def extract_json(text: str) -> dict:
    fenced = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.S)
    candidate = fenced.group(1) if fenced else text[text.find("{"): text.rfind("}") + 1]
    return json.loads(candidate)


def run_grader(args, case: dict, reply: str, course: Path, run_dir: Path) -> list:
    prompt = GRADER_PROMPT.format(
        prompt=case["prompt"],
        expected=case.get("expected_output", "(none)"),
        expectations="\n".join(f"- {e}" for e in case["expectations"]),
        reply=reply or "(no reply)",
        files=course_snapshot(course),
        outside=course_snapshot(course.parent, skip=course).replace(
            "(the course folder is empty)", "(none)"),
    )
    cmd = [
        args.claude, "-p", prompt, "--output-format", "json", "--max-turns", "1",
        "--tools", "", "--setting-sources", "project", "--strict-mcp-config",
    ]
    if args.grader_model:
        cmd += ["--model", args.grader_model]
    proc = subprocess.run(
        cmd, cwd=run_dir, env=child_env(), capture_output=True, text=True,
        timeout=args.timeout,
    )
    (run_dir / "grader_output.json").write_text(proc.stdout, encoding="utf-8")
    try:
        verdicts = extract_json(json.loads(proc.stdout).get("result", ""))["expectations"]
    except (ValueError, KeyError, TypeError, AttributeError):
        verdicts = []
    by_text = {v.get("text"): v for v in verdicts if isinstance(v, dict)}
    graded = []
    for i, text in enumerate(case["expectations"]):
        verdict = by_text.get(text)
        if verdict is None and i < len(verdicts) and isinstance(verdicts[i], dict):
            verdict = verdicts[i] if verdicts[i].get("text") not in case["expectations"] else None
        if verdict is None:
            graded.append({"text": text, "passed": False, "evidence": "not graded"})
        else:
            graded.append(
                {"text": text, "passed": verdict.get("passed") is True,
                 "evidence": str(verdict.get("evidence", ""))}
            )
    return graded


def skill_expectation(skill: str, events: list) -> dict:
    invoked = skills_invoked(events)
    passed = any(name.split(":")[-1] == skill for name in invoked)
    return {
        "text": f"The {skill} skill was invoked",
        "passed": passed,
        "evidence": f"Skill tool calls: {invoked or 'none'}",
    }


def run_case(args, skill_evals_dir: Path, case: dict, batch_dir: Path) -> dict:
    run_dir = batch_dir / f"eval-{case['id']}"
    course = run_dir / "teacher" / "course"
    prepare_course(skill_evals_dir, case, course)
    events = run_executor(args, case, course, run_dir)
    reply = final_message(events)
    (run_dir / "final_message.md").write_text(reply, encoding="utf-8")
    expectations = [skill_expectation(args.skill, events)]
    expectations += run_grader(args, case, reply, course, run_dir)
    passed = sum(e["passed"] for e in expectations)
    grading = {
        "eval_id": case["id"],
        "prompt": case["prompt"],
        "expectations": expectations,
        "summary": {
            "passed": passed,
            "failed": len(expectations) - passed,
            "total": len(expectations),
            "pass_rate": round(passed / len(expectations), 3),
        },
    }
    (run_dir / "grading.json").write_text(
        json.dumps(grading, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return grading


def resolve_plugin(args, batch_dir: Path) -> Path:
    """The plugin to load: --plugin-dir if it has the skill, else a wrapper
    plugin around a repo-only skill from --repo-skills-dir (never shipped)."""
    plugin = Path(args.plugin_dir)
    if (plugin / "skills" / args.skill).is_dir():
        return plugin
    repo_skill = Path(args.repo_skills_dir) / args.skill
    if not (repo_skill / "SKILL.md").is_file():
        raise CaseError(f"skill {args.skill!r} not found in {plugin}/skills or {args.repo_skills_dir}")
    wrapper = batch_dir / "plugin"
    manifest = {"name": "repo-only-skills", "version": "0.0.0",
                "description": "Wrapper for evaluating a repo-only skill"}
    (wrapper / ".claude-plugin").mkdir(parents=True)
    (wrapper / ".claude-plugin/plugin.json").write_text(json.dumps(manifest), encoding="utf-8")
    shutil.copytree(repo_skill, wrapper / "skills" / args.skill,
                    ignore=shutil.ignore_patterns("__pycache__"))
    return wrapper


def parse_args(argv):
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("skill")
    parser.add_argument("--case", type=int, action="append", help="run only these ids")
    parser.add_argument("--evals-dir", default=str(REPO / "evals"))
    parser.add_argument("--plugin-dir", default=str(DEFAULT_PLUGIN))
    parser.add_argument("--repo-skills-dir", default=str(DEFAULT_REPO_SKILLS),
                        help="repo-only skills, used when the plugin lacks the skill")
    parser.add_argument("--out", default=str(REPO / "evals-workspace"))
    parser.add_argument("--claude", default="claude", help="claude executable")
    parser.add_argument("--model", help="model for the run under test")
    parser.add_argument("--grader-model", help="model for the grader")
    parser.add_argument("--max-turns", type=int, default=30)
    parser.add_argument("--timeout", type=int, default=900, help="seconds per call")
    return parser.parse_args(argv)


def main(argv) -> int:
    args = parse_args(argv)
    skill_evals_dir = Path(args.evals_dir) / args.skill
    try:
        cases, args.extra_tools = load_suite(skill_evals_dir)
    except CaseError as exc:
        print(f"ERROR {exc}", file=sys.stderr)
        return 2
    if args.case:
        cases = [c for c in cases if c["id"] in args.case]
        if not cases:
            print(f"ERROR no case with id in {args.case}", file=sys.stderr)
            return 2
    batch_dir = Path(args.out) / args.skill / time.strftime("%Y%m%d-%H%M%S")
    try:
        args.skill_plugin_dir = resolve_plugin(args, batch_dir)
    except (CaseError, OSError) as exc:
        print(f"ERROR {exc}", file=sys.stderr)
        return 2
    all_passed = True
    for case in cases:
        try:
            grading = run_case(args, skill_evals_dir, case, batch_dir)
        except (OSError, subprocess.SubprocessError) as exc:
            print(f"eval-{case['id']}: ERROR {exc}", file=sys.stderr)
            return 2
        s = grading["summary"]
        all_passed &= s["failed"] == 0
        print(f"eval-{case['id']}: {s['passed']}/{s['total']} passed")
        for e in grading["expectations"]:
            if not e["passed"]:
                print(f"  FAIL {e['text']}: {e['evidence']}")
    print(f"results: {batch_dir}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
