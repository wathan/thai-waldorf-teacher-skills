# Claude Code plugin + marketplace format (verified 2026-10-27, CLI 2.1.304)

Sources: https://code.claude.com/docs/en/plugin-marketplaces · https://code.claude.com/docs/en/plugins/marketplace-reference.md · https://code.claude.com/docs/en/plugins-reference (manifest reference)

## Target layout for this repo (proposed, mirrors anthropics/k12-teacher-skills which uses `./plugin`)
```
.claude-plugin/marketplace.json        # repo root = marketplace root
plugins/thai-waldorf-science/          # plugin root (or ./plugin like k12)
  .claude-plugin/plugin.json           # ONLY plugin.json lives here
  skills/<skill-name>/SKILL.md         # one dir per skill; references/ inside skill dir
  references/ (shared corpus)          # any non-component dir OK at plugin root
```
- Everything except plugin.json sits at plugin root, NOT inside `.claude-plugin/`.
- A `CLAUDE.md` at plugin root is NOT loaded and `validate` warns → don't put one there.
- Installed plugins are copied to cache; paths must not escape plugin root (`..` = validate error "Path contains \"..\""). So shared references MUST live inside the plugin dir. In skill Markdown reference them via `${CLAUDE_PLUGIN_ROOT}/references/...` (substituted inline in skill content) or `${CLAUDE_SKILL_DIR}` (skill's own dir). Env vars are NOT available in Bash tool.
- Skills namespaced `/<plugin-name>:<skill-name>` (e.g. `/thai-waldorf-science:guiding-the-workflow`).

## marketplace.json (repo-root `.claude-plugin/marketplace.json`)
Required: `name`, `owner{name}`, `plugins[]`. Entry required: `name`, `source`.
```json
{
  "name": "thai-waldorf-teacher-skills",
  "description": "...",            // validate warns if missing
  "owner": { "name": "wathan" },
  "plugins": [
    { "name": "thai-waldorf-science",
      "source": "./plugins/thai-waldorf-science",   // must start with ./ ; relative to repo root, not .claude-plugin/
      "description": "...", "category": "education" }
  ]
}
```
- Entry `name` MUST equal plugin.json `name` (else install-by-manifest-name fails).
- Don't set `version` in both entry and plugin.json (validate warns; plugin.json wins). k12 sets both equal (0.10.0).
- Optional: `metadata.pluginRoot` ("./plugins" → bare `"source": "thai-waldorf-science"`), `category`, `tags`, `displayName`, `strict` (default true).
- Marketplace name rules: `[A-Za-z0-9._-]`, start alnum; reserved names incl. anything impersonating claude/anthropic.

## plugin.json
Only `name` required (kebab-case; must not start with `claude-`/`anthropic-`). Fields: `displayName, version, description, author{name,email,url}, homepage, repository, license (SPDX e.g. "CC-BY-SA-4.0"), keywords, skills (adds to default skills/ scan), experimental.evals (eval dir if not evals/)`. Unknown top-level keys stripped + warning. Missing version/description/author → warning (fails `--strict`).
k12 example (`plugin/.claude-plugin/plugin.json` @31fd6dbb):
```json
{ "name": "k12-education", "version": "0.10.0", "description": "...", "author": { "name": "Anthropic" } }
```

## Validation (exists, use in CI)
- `claude plugin validate <plugin-dir>` and `claude plugin validate <repo-root>` (marketplace; also validates each relative-path plugin's plugin.json as `plugins[N] plugin.json → ...`).
- `--strict` = warnings are errors (CI). `--json` = machine report. Exit 1 on failure.
- Tested in scratchpad: minimal plugin without `author` → warning "No author information provided"; `--strict` fails. So set `author`.
- Validate does NOT check: missing relative source dir (fails only at install), SKILL.md line limits, TOC, UPSTREAM, NOTICE → own validator needed (issue #2).
- `claude plugin details <name>` = component inventory + token cost. `claude plugin tag` creates `{name}--v{version}` tag after checking plugin.json/marketplace agree.

## Install / test commands
- Local dev without marketplace: `claude --plugin-dir ./plugins/thai-waldorf-science` (marketplace name `inline`).
- Local marketplace: `claude plugin marketplace add ./` (or path) → `claude plugin install thai-waldorf-science@thai-waldorf-teacher-skills` → `claude plugin list` / `claude plugin details thai-waldorf-science`.
- From GitHub: `claude plugin marketplace add wathan/thai-waldorf-teacher-skills` then install as above. In-session: `/plugin marketplace add wathan/thai-waldorf-teacher-skills`, `/plugin install thai-waldorf-science@thai-waldorf-teacher-skills`, `/reload-plugins`.
- Local-path marketplace loads plugin files in place (edits apply on next session or `/reload-plugins`).
- Remove: `claude plugin marketplace remove <name>`.
