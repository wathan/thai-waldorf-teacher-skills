# Evals: skill-creator format vs native `claude plugin eval`

Two incompatible formats exist ("neither tool reads the other's case files" — plugin-evals docs). Spec #1/#2 say "skill-creator's eval format"; native `claude plugin eval` (CLI ≥2.1.269; installed 2.1.304) is the practical headless runner. **Recommendation:** author cases in skill-creator `evals/evals.json` per skill (spec compliance), and generate/maintain native `claude plugin eval` cases from them (or a small runner script) to execute headlessly in CI. Flag this choice to the user/lead.

## 1. skill-creator format
Local source: `/Users/wathan/.claude/plugins/marketplaces/claude-plugins-official/plugins/skill-creator/skills/skill-creator/` (`references/schemas.md`, `agents/grader.md`, `scripts/quick_validate.py`, `scripts/aggregate_benchmark.py`, `eval-viewer/generate_review.py`). Upstream: anthropics/claude-plugins-official, also anthropics/skills.

`evals/evals.json` (inside the skill dir per skill-creator; for us keep repo-only, e.g. `evals/<skill>/evals.json`, since evals must not ship):
```json
{
  "skill_name": "example-skill",
  "evals": [
    {
      "id": 1,
      "prompt": "User's example prompt",
      "expected_output": "Description of expected result",
      "files": ["evals/files/sample1.pdf"],
      "expectations": [
        "The output includes X",
        "The skill used script Y"
      ]
    }
  ]
}
```
Fields: `skill_name` (= frontmatter name), `evals[].id` int, `prompt`, `expected_output` (human), `files` (optional input paths relative to skill root), `expectations` (verifiable statements; SKILL.md calls them "assertions").
Per-run `eval_metadata.json`: `{"eval_id":0,"eval_name":"descriptive-name","prompt":"...","assertions":[]}`.
Grader output `grading.json`: `{"expectations":[{"text","passed","evidence"}], "summary":{"passed","failed","total","pass_rate"}, ...}` — field names `text/passed/evidence` are mandatory for the viewer.
Workspace: `<skill>-workspace/iteration-N/eval-<name>/{with_skill,without_skill}/outputs/`; runs are subagents (with + baseline), graded by grader agent; `python -m scripts.aggregate_benchmark <workspace>/iteration-N --skill-name <name>`; viewer `generate_review.py ... --static out.html` for headless.
Fixture convention for us: `files` → a fixture course folder, e.g. `evals/<skill>/fixtures/<case>/` (class profile or none; empty/default/custom layout; optional year plan; optional course templates).

## 2. Native `claude plugin eval` (headless, CI-able)
Docs: https://code.claude.com/docs/en/plugin-evals.md
Layout (eval dir default `<plugin>/evals/`; override `--eval-dir` or plugin.json `"experimental":{"evals":"..."}` — must be a dir BELOW plugin root, no `..`):
```
evals/<case>/prompt.md            # frontmatter + prompt body
evals/<case>/case.yaml            # optional: context.*, graders
evals/<case>/graders/<name>.md    # one grader per file
evals/results/<timestamp>/        # output; gitignore
```
**Problem:** eval dir must be inside the plugin root → would ship with the plugin. Options: (a) put cases at `<plugin>/evals/` and accept/strip (k12 keeps rubrics at repo-root `evals/`, outside `plugin/`); (b) keep a repo-only "eval harness plugin" dir whose `plugins:` frontmatter points at the real plugin (`plugins: ["../../plugins/thai-waldorf-science"]` paths are relative to case dir — untested whether paths outside are accepted); (c) copy cases into a temp plugin copy in CI. Needs a quick spike.

Scaffold `claude plugin eval init --bare <name>` produced (tested):
```markdown
---
max_turns: 10
allowed_tools: [Read, Glob, Grep, Skill]
---

TODO: describe what the agent should do
```
grader:
```markdown
---
type: llm
weight: 1
---

TODO: describe what a successful response looks like
```
prompt.md fields: `name, description, tags, plugins (dirs under test, relative to case dir), runs (default 3, 1–50), expected_outcome, model, max_turns (10, ≤200), timeout_seconds (300, ≤3600), allowed_tools, append_system_prompt, env (EVAL_* keys only)`. Unknown key = error.
case.yaml: `schema_version: "1.1"`, `name`, top-level `description/tags/plugins/runs/expected_outcome`, `execution:{model,max_turns,timeout_seconds,allowed_tools,append_system_prompt,env,prompt}`, `context:{scaffold_script, history_file, add_dirs}`, `graders:[{name,type,...,criteria}]`.
Fixtures: each run starts in an EMPTY workspace. Seed via `context.scaffold_script: fixture.sh` (bash, runs in workspace, only with `--scaffold`, 120 s, minimal env) — e.g. `cp -R "$OLDPWD"/...`? (cwd is workspace; script lives in case dir — use a path relative to script: `cp -R "$(dirname "$0")/fixture/." .`; verify). `context.add_dirs: [fixture]` = read-only dirs. Note: `file_exists` and `target: files` only see files CREATED during run, not scaffold files.
Grader types: `regex` (`pattern, flags, match: not_contains|"count:N", target`), `tool_used` (`tool, input_match, min, max`), `tool_order` (`before, after`), `file_exists` (`path` glob, `exists`), `llm` (`criteria`/body, `focus`; 2 of 3 judge votes), `baseline` (`baseline_file`, `criteria`). No custom-code graders. Common keys: `type, weight, arm (with-only|both)`.
target/focus values: `last_message` (default), `trace`, `files`, `{ source: file, path: <path> }` (file contents — use this to grade produced plans), `mock_calls`.
Skill-fired grader:
```markdown
---
type: tool_used
tool: Skill
input_match: '"skill"\s*:\s*"(?:[\w-]+:)?guiding-the-workflow"'
---
```
Isolation: temp HOME + workspace; no user CLAUDE.md/settings/other plugins; Artifact tool off; run cannot read eval dir. Writing files needs `--allow-tools Write Edit` (Bash too if needed).
Run (CI):
```bash
claude plugin eval plugins/thai-waldorf-science --trust-plugin --scaffold --allow-tools Write Edit \
  --ablation none --runs 1 --threshold 0.8 --json results.json --no-publish --judge-model sonnet --max-cost-usd 5
```
Exit 0 pass / 1 below threshold or error / 2 partial (cost/credential). Default ablation runs a no-plugin baseline arm too (doubles cost); `--ablation none` to skip. Needs Claude credentials in CI (ANTHROPIC_API_KEY) — CI eval job likely manual/optional; static validator is the always-on CI job.

## 3. Manual headless fallback (`claude -p`)
```bash
tmp=$(mktemp -d); cp -R evals/<skill>/fixtures/<case>/. "$tmp"; cd "$tmp"
claude -p "<prompt>" --plugin-dir /abs/path/plugins/thai-waldorf-science \
  --output-format stream-json --verbose --allowedTools "Read,Glob,Grep,Write,Edit,Skill" --max-turns 30 > transcript.jsonl
```
then grade: a second `claude -p` with grader.md instructions + expectations + transcript + outputs dir → write grading.json (`text/passed/evidence`). skill-creator's `run_eval.py` uses `claude -p --output-format stream-json --verbose --include-partial-messages` and strips `CLAUDECODE` env var to allow nesting.

## 4. k12 rubric CSV format (prior art for criteria)
Repo-root `evals/<skill>/rubrics/*.csv` (outside `plugin/`), header:
`ID,Bucket,Criterion,What pass requires,Notes,Conditional` (lesson-prep adds `,Source` = artifacts|chat|both).
Buckets: `P — Pedagogy`, `R — Rigor`, `O — Output/Formatting`, `M — Model Scaffolding` (M judged on chat reply, others on documents). Conditional non-empty → skipped (not failed) when condition unmet. Binary pass/fail per criterion; LLM-judge prompt returns `[{"id","pass","explanation"}]`. Example row (shared.csv): `P1,P — Pedagogy,Standard named verbatim,"The target standard appears as the full standard text ... Pass = ... Fail = ...",,`.
Suggested for us: per-skill `rubric.csv` in same columns, criteria from spec #1 Testing Decisions; each case's `expectations` reference rubric IDs.
