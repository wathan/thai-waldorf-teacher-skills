## Agent skills

### Issue tracker

Issues tracked in GitHub Issues (wathan/thai-waldorf-teacher-skills) via `gh` CLI. See `docs/agents/issue-tracker.md`.

### Triage labels

Default five-role vocabulary: needs-triage, needs-info, ready-for-agent, ready-for-human, wontfix. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: root `GLOSSARY.md` + `docs/adr/`. See `docs/agents/domain.md`.

## Repo layout

- Plugin `thai-waldorf-science` lives in `plugins/thai-waldorf-science/` (skills in `skills/<name>/`, shared corpus in `references/`); marketplace at `.claude-plugin/marketplace.json`. Only that folder ships.
- Repo-only: `sources/` (PDFs, school forms), `archive/`, `evals/`, `scripts/`, `tests/`, `docs/`, `UPSTREAM.md`. Keep repo-root `LICENSE`/`NOTICE` and the plugin copies identical.
- Every new skill needs a `## <skill-name>` entry in `UPSTREAM.md` and `evals/<skill>/evals.json` (see `evals/README.md`).

## Checks

- `uv run --no-project python -m unittest discover tests` and `uv run --no-project python scripts/validate.py` (offline; CI runs both plus `claude plugin validate --strict`).
- Behaviour evals: `uv run --no-project python scripts/run_evals.py <skill>` (needs Claude credentials; not in CI).
