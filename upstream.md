# Upstream sources (fetched 2026-10-27 via gh api)

| Repo | Branch | HEAD SHA | Date | License |
|---|---|---|---|---|
| anthropics/k12-teacher-skills | main | 31fd6dbb0c07cb50bb3ce7f62a4135a393bd0e8c | 2026-10-14 | Apache-2.0 (+NOTICE: Anthropic, Learning Commons) |
| GarethManning/education-agent-skills | main | 135d6275e7db0657d70b147f46d3191c5430677d | 2026-10-22 | CC BY-SA 4.0 (© 2026 Gareth Manning; GitHub reports NOASSERTION) |
| mattpocock/skills | main | 59db609eb1e18aaf59b63284d0e52255aff0c63c | 2026-10-27 | MIT |

Per-path last commit (`gh api "repos/<r>/commits?path=<p>&per_page=1" --jq '.[0].sha'`) — use for UPSTREAM.md "commit last reviewed" and for check-upstream (compare `repos/<r>/commits?path=<p>&sha=<branch>` since recorded SHA, or `repos/<r>/compare/<recorded>...<head>` and filter `.files[].filename` by path prefix):
- k12 `plugin/skills/k12-lesson-plan-creation` → 31fd6dbb0c07cb50bb3ce7f62a4135a393bd0e8c
- k12 `plugin/skills/k12-lesson-differentiation` → 31fd6dbb0c07cb50bb3ce7f62a4135a393bd0e8c
- k12 `plugin/skills/k12-check-for-understanding` → 31fd6dbb0c07cb50bb3ce7f62a4135a393bd0e8c
- k12 `plugin/skills/k12-lesson-prep` → 281eb8d41fe2837d911541c9bbb870b58add804c
- mattpocock `skills/productivity/grilling` → 95249b0b49782349740fd9b8c6ce32b4e59e497a
- Gareth: not fetched per path (29 calls); record repo HEAD 135d627… unless implementer fetches per path.

## k12-teacher-skills structure (@31fd6dbb)
- Marketplace at repo root `.claude-plugin/marketplace.json`, plugin at `./plugin` (`plugin/.claude-plugin/plugin.json`, name `k12-education`, v0.10.0), `plugin/.mcp.json` (US edtech connectors — drop). Evals OUTSIDE plugin: `evals/<skill>/rubrics/*.csv` + `evals/README.md`. Root `NOTICE`, `LICENSE`; each skill also has `LICENSE`/`NOTICE`.
- Skills (4): `plugin/skills/k12-lesson-plan-creation`, `k12-lesson-differentiation`, `k12-lesson-prep` (SKILL.md + LICENSE only), `k12-check-for-understanding`.
- **lesson-plan-creation SKILL.md (230 lines)** headings: Keeping the teacher posted (teacher language only, no tool/file jargon) → **Step 0 — Route (silent, before anything else)**: determine subject → "read the matching reference file NOW" (`references/math.md|ela.md|science.md|social_studies.md`; "Loading the matching reference file is mandatory"), curriculum branch, connector check → Step 1 Clarify (≤2 questions, defaults silently; one structured round incl. draft offer) → Step 2 Ground in standards → Step 3 Build → Copyright guardrail → Step 4 Draft offer → Step 5 Output (5a common JSON `references/lesson-json.md`, 5b every document same turn, 5c satisfaction ask + iteration options, 5d revisions keep docs in sync). Refs: `references/{science.md(186 lines: Clarify, Standards grounding, Build: curriculum branching, grade band (9–12 section), section structure; Exit ticket; Writing lesson.json), output.md, lesson-json.md, example_lesson.json, learning-commons-kg.md, NOTICE}`, `rendering/{claude-artifact.md,docx.md}`, `scripts/*.py` (renderers — dropped in v1).
  → Our house template: Step 0 silent route main lesson block vs subject lesson → read `references/main-lesson-block.md` or `references/subject-lesson.md`.
- Rubric CSVs: `evals/k12-lesson-plan-creation/rubrics/{shared,science,math,ela,social_studies}.csv`, `evals/k12-lesson-differentiation/rubrics/{differentiation,clarifying_question}.csv`, `evals/k12-lesson-prep/rubrics/internalization.csv`, `evals/k12-check-for-understanding/rubrics/math.csv`. Columns `ID,Bucket,Criterion,What pass requires,Notes,Conditional` (+`Source` in lesson-prep). See evals.md.

## education-agent-skills structure (@135d627)
- Root plugin (`source: "./"`), `.claude-plugin/{marketplace.json,plugin.json}` (plugin.json `skills: ["./skills/<domain>", ...]`), 165 skills at `skills/<domain>/<name>/SKILL.md`; some have `references/worked-examples.md`, `agents/openai.yaml`.
- Frontmatter extended schema: `name, description (project policy ≤250 chars), disable-model-invocation (required bool), user-invocable, effort, skill_id (<domain>/<name>), skill_name, domain, version, evidence_strength (strong|moderate|low-moderate|medium|emerging|original|practitioner), evidence_sources[], input_schema{required[],optional[]}{field,type,description}`.
- **Validation scripts** (CI `.github/workflows/validate.yml`): `scripts/validate-skills.py` (frontmatter YAML; name regex `^[a-z0-9-]+$` ≤64 and == parent dir; description ≤250; >500 lines warning; domain == grandparent dir; input_schema types), `scripts/export-standard-skills.py` + `scripts/validate-standard-skills.py` (exports portable profile to `dist/agent-skills`, validates with pinned official `skills_ref` package: `from skills_ref import validate, to_prompt`; deps in `requirements/standard-validation.txt`), `scripts/validate-registry.py`, `scripts/generate-registry.py` (registry.json sync, skill count check). Pattern worth copying: count check + `skills_ref.validate(path)` per skill.

## mattpocock/skills (@59db609)
- `skills/productivity/grilling/SKILL.md` (MIT): design tree, rounds; frontier = decisions whose prerequisites are settled; ask the whole frontier per round, numbered `❓ **Q1** - **title**: body` then `➡️ recommended answer`; word so "yes" accepts recommendation; look up facts yourself, decisions are the user's; done when frontier empty, confirm before acting. Related: `skills/productivity/grill-me`, `skills/engineering/grill-with-docs`.

## Mapping to our ten skills
Explicitly named in ADR-0001 / issues = **[N]**; everything else **PROPOSED** (the 29 are not enumerated anywhere; 12 are named). Gareth paths are `skills/<domain>/<name>`.

| Our skill | k12 | Gareth (29 total) | Other |
|---|---|---|---|
| setting-up-class-profiles | — | — | mattpocock `grilling` [N #5] |
| guiding-the-workflow | — | — (none) | — |
| mapping-curriculum | — | curriculum-alignment/curriculum-crosswalk [N], curriculum-alignment/coverage-audit [N] | |
| planning-main-lesson-blocks | k12-lesson-plan-creation [N #7] | environmental-experiential-learning/ecological-inquiry-anchor-designer [N]; PROPOSED: global-cross-cultural-pedagogies/phenomenon-based-unit-anchor, global-cross-cultural-pedagogies/place-based-inquiry-anchor, wellbeing-motivation-agency/awe-wonder-experience-designer (anchor); environmental-experiential-learning/experiential-learning-cycle-designer (rhythm); curriculum-assessment/learning-progression-builder (progression); curriculum-assessment/backwards-design-unit-planner | #7 says "Gareth anchor, rhythm and progression skills" |
| planning-subject-lessons | k12-lesson-plan-creation (shape) | PROPOSED: explicit-instruction/explicit-instruction-sequence-builder, explicit-instruction/practice-problem-sequence-designer (+ retrieval-practice-generator shared) | |
| writing-thai-core-plans | — | curriculum-assessment/competency-unpacker [N #10], curriculum-assessment/criterion-referenced-rubric-generator [N #10], original-frameworks/single-point-rubric-designer [N #10] | |
| differentiating-for-learner-variability | k12-lesson-differentiation (structural only) [N] | PROPOSED (#13 "UDL, inclusive-design and EAL sources"): inclusive-design/udl-barrier-anticipator, inclusive-design/udl-options-designer, inclusive-design/udl-lesson-auditor, eal-language-development/language-demand-analyser, eal-language-development/academic-language-sentence-frame-generator, eal-language-development/vocabulary-tiering-tool, eal-language-development/scaffolded-task-modifier | alt: original-frameworks/inclusive-design-orchestrator, curriculum-assessment/differentiation-adapter |
| planning-formative-assessment | k12-check-for-understanding (structural only) [N] | questioning-discussion/hinge-question-designer [N], curriculum-assessment/formative-assessment-technique-selector [N], explicit-instruction/checking-for-understanding-protocol-designer [N], self-regulated-learning/metacognitive-prompt-library [N], memory-learning-science/retrieval-practice-generator [N] | single-point-rubric also relevant |
| auditing-epistemic-agency | — | PROPOSED: questioning-discussion/discussion-protocol-selector (+ dialogic-teaching-move-generator shared) | |
| preparing-to-teach | k12-lesson-prep [N #15] | questioning-discussion/dialogic-teaching-move-generator [N #15] | |

Count: named Gareth = 12 distinct; proposed = 16 (anchor 3, rhythm 1, progression 1, backwards-design 1, subject 2, UDL 3, EAL 4, audit 1) → 28; add one alternate (inclusive-design-orchestrator or differentiation-adapter) to reach 29. **Flag to user for confirmation.**
Explicitly excluded (ADR-0001): socratic-questioning-sequence-generator, agency-scaffold-generator, dispositional-knowledge-assessment-designer, mixed-age-learning-task-designer, argument-structure-scaffold-generator (CER, deferred), kud-chart-author, developmental-band-translator, goal-setting-protocol-designer, study-strategy-selector, error-analysis-protocol, self-regulation-scaffold-generator; whole domains ai-learning-science, ai-literacy, student-learning, historical-thinking, montessori-alternative-approaches, wellbeing programmes. v2: disciplinary-writing-scaffold, scope-and-sequence-designer, lesson-study-cycle-designer, teacher-inquiry-cycle-designer, lesson-observation-protocol-designer, reflective-practice-prompt-generator, systems-thinking/*.
Note: awe-wonder-experience-designer is in wellbeing-motivation-agency domain (ADR excludes "wellbeing programmes", not necessarily this) — confirm.
