# Skill authoring rules (Anthropic best practices + Claude Code skills)

Sources: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices · https://code.claude.com/docs/en/skills · skill-creator `scripts/quick_validate.py`

## Frontmatter (validator-enforceable)
- `name`: required for portability; ≤64 chars; `^[a-z0-9-]+$`; no leading/trailing `-`, no `--`; no XML tags; must not contain reserved words `anthropic`, `claude`. Should equal skill dir name (Claude Code defaults name to dir name). Spec #1: gerund form, no plugin prefix (e.g. `planning-main-lesson-blocks`).
- `description`: non-empty; ≤1024 chars; no XML tags / no `<` `>` (quick_validate rejects angle brackets); third person ("Plans…", never "I can"/"You can"); states WHAT + WHEN ("Use when…"). Claude Code truncates description+`when_to_use` at 1536 chars in listing.
- Portable key set (claude.ai / API / package_skill.py hard-error on others): `name, description, license, allowed-tools, metadata, compatibility` (compatibility ≤500 chars). Claude Code also accepts `when_to_use, argument-hint, arguments, disable-model-invocation, user-invocable, model, effort, context, agent, hooks, paths, shell`. Recommend: stick to portable keys (+ `license: CC-BY-SA-4.0`).
- k12 style: `license: "Copyright … SPDX-License-Identifier: Apache-2.0. Complete terms in LICENSE and NOTICE."`, description uses YAML `>` folded scalar and includes "Load BEFORE asking clarifying questions", "Do NOT load for …", disambiguation vs sibling skills. Good pattern for our routing between sibling skills.

## Body
- SKILL.md body < 500 lines (hard rule in spec; Gareth validator counts whole file incl. frontmatter: `content.count("\n")+1 > 500` → warning).
- Concise: assume Claude is smart; only add non-obvious context.
- Progressive disclosure: SKILL.md = overview + routing; details in files referenced DIRECTLY from SKILL.md (one level deep; no ref→ref chains — Claude may `head -100` nested files).
- Any reference file >100 lines needs a table of contents at top (e.g. `## Contents` list).
- Forward slashes only; descriptive filenames; consistent terminology (use GLOSSARY.md terms); no time-sensitive statements.
- Workflows: numbered steps / copyable checklist; feedback loop (draft → check against rules → fix). Conditional workflow pattern for routing (house template: k12 lesson-plan-creation "Step 0 — Route (silent)" → read matching reference NOW).
- Template pattern for output formats; examples pattern for style.
- Default with escape hatch; avoid offering many options.
- Paths in plugin skills: `${CLAUDE_SKILL_DIR}/references/x.md` for skill-local, `${CLAUDE_PLUGIN_ROOT}/references/x.md` for shared corpus (substituted inline when skill loads).
- Evaluation-driven: ≥3 evals per skill; test across Haiku/Sonnet/Opus.

## Checklist (from best-practices page)
Description specific + key terms + what & when · body <500 lines · details split out · no time-sensitive info · consistent terms · concrete examples · refs one level deep · workflows have clear steps · ≥3 evaluations.

## Validator checks to implement (issue #2 seam 2)
frontmatter parses; name regex/len/reserved words/dir match; description present ≤1024 no `<>`; only allowed keys; SKILL.md ≤500 lines; every `.md` under skill dir or shared references >100 lines has a `Contents`/TOC heading in first ~40 lines; every skill has UPSTREAM.md entry; LICENSE + NOTICE exist; no repo-only material (archive/, sources/, *.pdf, *.docx, check-upstream, evals/) inside plugin dir; `claude plugin validate --strict` on plugin and repo root.
