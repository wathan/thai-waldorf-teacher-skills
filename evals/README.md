# Skill behaviour evals

Repo-only (never shipped). One folder per plugin skill: `evals/<skill>/evals.json` in skill-creator's format, plus `evals/<skill>/fixtures/<name>/`, each a fixture course folder (class profile or none; empty, default-template or custom layout; optional year plan; optional course-local templates). Paths in a case's `files` are relative to `evals/<skill>/`; a directory's contents (or a single file) are copied into an empty course folder before the run, and `.gitkeep` files are dropped (a folder holding only `.gitkeep` arrives empty, so give a folder that should look in use a real file). The course folder sits inside an otherwise empty teacher folder that the run may also write to, so a file a skill keeps outside the course (a year plan at `../<name>.md`) is graded too.

```json
{"skill_name": "<skill>",
 "evals": [{"id": 1, "prompt": "...", "expected_output": "...",
            "files": ["fixtures/empty"], "expectations": ["..."]}]}
```

Write expectations about external behaviour only: what the reply says, which files are written where, and whether the agreed rules hold in them (spec #1, Testing Decisions). The runner adds one expectation itself: the skill under test was invoked.

## Run

```bash
uv run --no-project python scripts/run_evals.py <skill>            # all cases
uv run --no-project python scripts/run_evals.py <skill> --case 2   # one case
```

Options: `--model`, `--grader-model`, `--max-turns` (default 30), `--out` (default `evals-workspace/`, gitignored). Results per case land in `evals-workspace/<skill>/<timestamp>/eval-<id>/`: `teacher/course/` (the course folder after the run; anything written beside it stays in `teacher/`), `transcript.jsonl`, `final_message.md`, `grading.json`. Exit 0 = all passed, 1 = some failed, 2 = invalid case file or run error.

Needs Claude credentials and costs tokens, so it is not part of CI. `tests/test_run_evals.py` checks every committed `evals.json` loads, offline.
