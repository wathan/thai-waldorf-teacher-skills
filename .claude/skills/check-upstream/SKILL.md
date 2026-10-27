---
name: check-upstream
description: >
  Reports which of the thai-waldorf-science plugin's skills have upstream
  changes worth reviewing, by comparing the commits recorded in UPSTREAM.md
  with the current state of k12-teacher-skills, education-agent-skills and
  mattpocock/skills, and lists the upstream files changed since each recorded
  commit. Repo-only maintainer tool, not shipped in the plugin. Use when the
  maintainer asks whether upstream skills have changed, what to review
  upstream, or to check UPSTREAM.md against upstream. Reports only; never
  merges changes or edits skills or the upstream record.
license: CC-BY-SA-4.0
---

# Checking upstream

You report; the maintainer decides. Merging upstream changes stays manual (ADR-0001).

## Hard rule

Never write or edit any file during this skill: not the plugin's skills, not `UPSTREAM.md`, not the state file. Even when changes are found, do not "bring the record up to date" or adapt a skill. If the maintainer asks you to, say that is a separate, explicit edit after they have reviewed the changes, and name the rows they would update.

## Step 1 — Find the inputs (silent)

- **Upstream record:** `UPSTREAM.md` in the working directory (the repo root). If it is missing, ask where it is; do not search the plugin.
- **Upstream state:**
  - If the maintainer names a recorded upstream state file (JSON, for tests and evals), use it and nothing else. Do not contact GitHub in that case, even to double-check.
  - Otherwise use live GitHub through the script's default mode (it calls `gh api`, read-only).

## Step 2 — Run the check

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/check_upstream.py" --record UPSTREAM.md [--state <recorded-state.json>]
```

Run it from the directory that holds `UPSTREAM.md`. The script prints a Markdown report. Exit 0: everything up to date. Exit 1: changes or commits it could not compare. Exit 2: the record or state file is invalid; show the error line and stop.

Do not recompute the comparison yourself or by other means; the script's report is the result.

## Step 3 — Report to the maintainer

Give the report in this order, keeping every skill, path, commit and file name exactly as the script printed it:

1. **Changes worth reviewing:** each affected skill (and `plugin-wide`, which covers all skills), each changed upstream path with the recorded and current commit, and the changed upstream files under it. Add the row's role and status from `UPSTREAM.md` (for example `structural`, `proposed`) when it helps the maintainer judge the change.
2. **Could not compare:** any path whose recorded commit is missing upstream or could not be fetched, with the reason.
3. **Up to date:** every skill and source with no change since its recorded commit.
4. **No upstream sources:** the skills that draw on none.

Close by saying plainly that no skill and not `UPSTREAM.md` were changed, that merging is left to the maintainer, and that after reviewing a path by hand they update its commit in `UPSTREAM.md`.
