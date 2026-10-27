# Current repo state (HEAD ce05ebef751452bd7aad1a2d3285114a0f77d563, main, clean)

Repo: wathan/thai-waldorf-teacher-skills · local `/Users/wathan/Documents/misc/thai-waldorf-teacher-skills`
Issues: #1 spec (parent), #2–#17 tickets, all OPEN, label `ready-for-agent`. Build order (#1): (1) skeleton+UPSTREAM+NOTICE/LICENSE+validator [#2] (2) mapping-curriculum+crosswalk [#3,#4] (3) setting-up-class-profiles [#5,#6] (4) main lesson blocks [#7,#8,#9] + subject lessons [#11] (5) Thai core plans [#10] (6) audit [#12] + differentiation [#13] (7) formative assessment [#14] + preparing-to-teach [#15] (8) guiding-the-workflow context-aware [#16] (9) check-upstream [#17].
Memory rule: NO Claude co-author trailer in commits (hook forbids; never bypass hooks).

## Layout
```
CLAUDE.md  GLOSSARY.md  .gitignore(.DS_Store only)
docs/adr/0001-inspired-by-with-upstream-tracking.md
docs/adr/0002-course-is-a-teaching-sequence.md
docs/adr/0003-zech-two-day-rhythm-default.md
docs/agents/{issue-tracker,triage-labels,domain}.md
references/README.md (index, 35 lines) + 16 .md files
references/sources/  (82 MB: 2 IPST PDFs, rawson2021steiner.pdf, 4 *.th.docx school forms)  → repo-only
archive/references-original-2026-10-27/ (1.3 MB, 12 pre-rewrite .md) → repo-only
```
No plugin, LICENSE, NOTICE, UPSTREAM.md, CI, evals yet. `.DS_Store` is committed at root.

## references/ (to ship, moved inside plugin) — lines / TOC?
| File | Lines | Role (from index) |
|---|---|---|
| waldorf-education-goals.md | 108 | Meta aims |
| rawson2021-generative-principles-upper-school.md | 403 | Meta pedagogy; §5 15-item checklist |
| waldorf-upper-school-macro-curriculum.md | 182 | Macro: grade modes G9 What/G10 How/G11 Why/G12 Who |
| waldorf-pisa-competencies-g9-g12.md | 755 | Meso Sx.n/Ex.n (generated snapshot) |
| waldorf-pisa-vertical-progression-g9-g12.md | 165 | Meso ramps (generated snapshot) |
| pisa-science-2025.md | 144 | Meso source, never plan from directly |
| thai-science-core-indicators-2560.md | 1799 | Statutory indicators `ว x.x ม.n/k` |
| thai-science-supplementary-learning-outcomes-2560.md | 1204 | ม.4–6 electives |
| thai-science-glossary-2560.md | 64 | Indicator verbs |
| thai-science-key-skills-2560.md | 225 | Official skill names |
| thai-science-scientific-mind-2560.md | 63 | Official attitude names |
| thai-science-indicator-analysis-examples-2560.md | 159 | IPST three-column format |
| waldorf-plan-template-block.th.md | 35 | Template |
| waldorf-plan-template-week.th.md | 39 | Template |
| waldorf-plan-template-day.th.md | 49 | Template |
| thai-core-plan-template.th.md | 227 | Template (K-P-A, สมรรถนะ, rubrics, sign-off) |
**None of the 11 files >100 lines has a TOC** → validator (TOC rule) will fail until TOCs are added (or the rule is scoped to skill-owned references only). Decide in #2.
Index (`references/README.md`) lists all 16 files + a "Default chain" (grade mode → intentions → Thai anchors → justification → Rawson design + §5 checklist → IPST format → block→week→day templates + Thai core plan). It also points to `sources/*.pdf`, `sources/*.th.docx` and `../archive/references-original-2026-10-27/` — these links break / must be reworded after the move (#2 AC: "index still resolves every file it lists").
Each reference file header cites `sources/...` paths (e.g. thai-science-core-indicators: `File: sources/สสวท2017….pdf`) — provenance notes; harmless but point outside plugin.

## Templates and Waldorf-day → Thai-stage mapping
- Plan templates: `references/thai-core-plan-template.th.md`, `references/waldorf-plan-template-{block,week,day}.th.md` (originals `references/sources/*.th.docx`). These are the plugin's four default templates (spec #1; #6 copies them into a course's templates area).
- Mapping location: `references/thai-core-plan-template.th.md` lines 219–227, section "## Mapping a Waldorf main-lesson day onto Section 7":
  - ขั้นนำเข้าสู่บทเรียน = Rhythmic Time (กิจกรรมวงกลม) + Recall of the previous day's experience (open questions, not a quiz)
  - ขั้นสอน/ขั้นจัดกิจกรรม = Concept formation from earlier experience → New Content (left un-analysed) → Practice
  - ขั้นสรุป = close; do NOT analyse today's new experience; state what tomorrow's recall picks up.
  Section 7 stage headings at lines 87/90/93.
- Day template rows (line 38 etc.): Rhythmic Time → Maths/Literacy → Recall (การทบทวนสิ่งที่เรียนไป) → Practice → New Content; rows may be reordered, labels kept.

## Inconsistencies to fix (flag)
- `waldorf-plan-template-day.th.md` l.14: "Recall … flows into concept formation for the experience *before that*" = Rawson four-day cycle; ADR-0003 says recall of yesterday's experience flows into concept formation for *that same* experience. Mapping table in thai-core-plan-template ("Concept formation from earlier experience") is ambiguous but compatible.
- `references/README.md` l.20 and week template: "E→R→C→A cycles" — four-day vocabulary (glossary _Avoid_ term).
- Day template l.15 and block template l.14: "differentiated at three levels" (Rawson) vs spec UDL-first, one shared task default (ADR-0001, #13); rawson file l.223/368 keeps Rawson's three levels as source content (fine).

## ADR key decisions
**0001 Inspired-by with tracked upstream, CC BY-SA 4.0**
- Skills written fresh in one shape (Anthropic best practices; k12 lesson-plan-creation as house template); not forked/vendored.
- Root `UPSTREAM.md`: per skill, upstream sources + commit last reviewed; repo-only `check-upstream` reports changes; merging manual.
- License CC BY-SA 4.0 with `NOTICE` (attribution Gareth Manning CC BY-SA; also satisfies k12 Apache-2.0 notice; mattpocock MIT).
- v1 skill list (10 + repo-only check-upstream); sources 4 k12 + 29 Gareth + mattpocock grilling; k12 CFU and differentiation structural only; explicit rejections and v2 list (see upstream.md).
**0002 Course folder = one teaching sequence, laid out as found**
- Skill's cwd = one teaching sequence (main lesson block named by subject, or subject lesson) of units (one topic each).
- Detect existing structure → confirm → record concept→file mapping in course README "Plugin layout" section; later skills read it.
- Default course template only when no recognisable structure; filenames suggestive. Folder name never read/changed.
- Class profile copied per course; year plan is the only file outside course, read from teacher-given path for year coverage. Course-local templates override plugin's.
**0003 Two-day rhythm (Zech) default**
- Day N experience un-analysed; day N+1 recall flows into discussion + concept formation (~40–50 min), then application, new experience last.
- Assessment-as-learning reflection right after recall+concept formation, never directly after New Content.
- Concept formation = individual position integrated into class understanding → audit expects explanatory-model domain open, flags scripted concepts.
- Day-plan Recall row covers recall + concept formation; Thai stage mapping unchanged; four-day cycle on request.

## Repo-only vs ship (spec #1 Implementation Decisions)
Ship (inside plugin dir): `.claude-plugin/plugin.json`, `skills/` (10), shared `references/` (16 .md, incl. generated crosswalk later).
Repo-only (outside plugin dir): `archive/`, `references/sources/` (PDFs, docx), `check-upstream` skill, `evals/`, validator script, `docs/`, `GLOSSARY.md`, `CLAUDE.md`, `UPSTREAM.md`?, `NOTICE`/`LICENSE` at repo root (consider also copying NOTICE/LICENSE into plugin dir since installs copy only the plugin dir — k12 has both root and per-skill LICENSE/NOTICE).
Moving 82 MB `sources/` out of `references/` matters: whole `references/` dir moves into plugin, sources must stay outside (e.g. `sources/` at repo root).
