# Skill behaviour evals

Repo-only (never shipped). One folder per plugin skill: `evals/<skill>/evals.json` in skill-creator's format, plus `evals/<skill>/fixtures/<name>/`, each a fixture course folder (class profile or none; empty, default-template or custom layout; optional year plan; optional course-local templates). Paths in a case's `files` are relative to `evals/<skill>/`; a directory's contents (or a single file) are copied into an empty course folder before the run, and `.gitkeep` files are dropped (a folder holding only `.gitkeep` arrives empty, so give a folder that should look in use a real file). The course folder sits inside a teacher folder that the run may also write to, so a file a skill keeps outside the course (a year plan at `../<name>.md`) is graded too. An optional `"teacher_files": ["fixtures/<name>"]` per case copies files into that teacher folder beside the course, for a year plan the teacher already has.

```json
{"skill_name": "<skill>",
 "evals": [{"id": 1, "prompt": "...", "expected_output": "...",
            "files": ["fixtures/empty"], "expectations": ["..."]}]}
```

Repo-only skills (in `.claude/skills/`, such as `check-upstream`) are evaluated the same way: when the plugin has no skill of that name, the runner loads it from `.claude/skills/<skill>` through a throwaway wrapper plugin. An optional top-level `"allowed_tools": ["Bash"]` adds executor tools for a skill whose cases need them (by default the executor gets Read, Glob, Grep, Write, Edit and Skill only). `check-upstream` cases run against a recorded upstream state (`upstream-state.json` in the fixture), never live GitHub.

Write expectations about external behaviour only: what the reply says, which files are written where, and whether the agreed rules hold in them (spec #1, Testing Decisions). The runner adds one expectation itself: the skill under test was invoked.

## Run

```bash
uv run --no-project python scripts/run_evals.py <skill>            # all cases
uv run --no-project python scripts/run_evals.py <skill> --case 2   # one case
```

Options: `--model`, `--grader-model`, `--max-turns` (default 30), `--out` (default `thai-waldorf-evals/` in the system temp dir, e.g. `/tmp/thai-waldorf-evals/`; keep it outside the repo, or the run under test picks up the repo's `CLAUDE.md`). Results per case land in `<out>/<skill>/<timestamp>/eval-<id>/`: `teacher/course/` (the course folder after the run; anything written beside it stays in `teacher/`), `transcript.jsonl`, `final_message.md`, `grading.json`. Exit 0 = all passed, 1 = some failed, 2 = invalid case file or run error. If the grader's reply is not valid JSON the runner asks it once more; if it fails again, that case's graded expectations are reported `NOT GRADED` (`"passed": null`, counted in `summary.not_graded`), never as failed, and the run exits 2.

Needs Claude credentials and costs tokens, so it is not part of CI. `tests/test_run_evals.py` checks every committed `evals.json` loads, offline.
