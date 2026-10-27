# Upstream record

The plugin's skills are written fresh, not forked (ADR-0001). This record lists, per skill, the upstream skills each one draws on and the upstream commit last reviewed for that path. The repo-only `check-upstream` skill (`.claude/skills/check-upstream/`, not shipped) compares these commits with upstream and reports changes; merging stays manual. After reviewing a path by hand, update its commit here.

## Contents

- [Format](#format)
- [Upstream repositories](#upstream-repositories)
- [Plugin-wide](#plugin-wide)
- Skills: [setting-up-class-profiles](#setting-up-class-profiles) · [guiding-the-workflow](#guiding-the-workflow) · [mapping-curriculum](#mapping-curriculum) · [planning-main-lesson-blocks](#planning-main-lesson-blocks) · [planning-subject-lessons](#planning-subject-lessons) · [writing-thai-core-plans](#writing-thai-core-plans) · [differentiating-for-learner-variability](#differentiating-for-learner-variability) · [planning-formative-assessment](#planning-formative-assessment) · [auditing-epistemic-agency](#auditing-epistemic-agency) · [preparing-to-teach](#preparing-to-teach)
- Repo-only: [check-upstream](#check-upstream)
- [Pending confirmation](#pending-confirmation)

## Format

One `## <skill-name>` section per plugin skill (the structure validator requires it). Each row: upstream repo, path in that repo, commit last reviewed (the last commit touching that path when reviewed), role, status.

- **Status `firm`:** named in ADR-0001, spec #1 or its tickets.
- **Status `proposed`:** a likely source not named in the repo docs; pending the maintainer's confirmation. Drop or promote it when the skill is built.
- **Role:** `content` (ideas taken), `structural` (shape only, content does not fit), `pattern` (interaction pattern embedded).

## Upstream repositories

| Key | Repo | License | HEAD when first recorded |
|---|---|---|---|
| k12 | anthropics/k12-teacher-skills | Apache-2.0 | 31fd6dbb0c07cb50bb3ce7f62a4135a393bd0e8c |
| gareth | GarethManning/education-agent-skills | CC BY-SA 4.0 | 135d6275e7db0657d70b147f46d3191c5430677d |
| mattpocock | mattpocock/skills | MIT | 59db609eb1e18aaf59b63284d0e52255aff0c63c |

## Plugin-wide

| Repo | Path | Commit last reviewed | Role | Status |
|---|---|---|---|---|
| k12 | plugin/skills/k12-lesson-plan-creation | 31fd6dbb0c07cb50bb3ce7f62a4135a393bd0e8c | structural (house template: silent routing step, then kind-specific references) | firm |

## setting-up-class-profiles

| Repo | Path | Commit last reviewed | Role | Status |
|---|---|---|---|---|
| mattpocock | skills/productivity/grilling | 95249b0b49782349740fd9b8c6ce32b4e59e497a | pattern (rounds, numbered questions with recommended answers) | firm |

## guiding-the-workflow

No upstream sources: written fresh from spec #1 and the plugin's own skill set. Shape follows the plugin-wide house template.

## mapping-curriculum

| Repo | Path | Commit last reviewed | Role | Status |
|---|---|---|---|---|
| gareth | skills/curriculum-alignment/curriculum-crosswalk | 952cc158791caae0e34ee42f2b5a0a72ce837558 | content | firm |
| gareth | skills/curriculum-alignment/coverage-audit | b4d93ab2f203c8b7d92488abc6917e01b049e148 | content | firm |

## planning-main-lesson-blocks

| Repo | Path | Commit last reviewed | Role | Status |
|---|---|---|---|---|
| k12 | plugin/skills/k12-lesson-plan-creation | 31fd6dbb0c07cb50bb3ce7f62a4135a393bd0e8c | content (science grade 9–12 build) | firm |
| gareth | skills/environmental-experiential-learning/ecological-inquiry-anchor-designer | b8efa77fe34cc0c7206086a6acc3303bd4045da4 | content (anchor) | firm |
| gareth | skills/global-cross-cultural-pedagogies/phenomenon-based-unit-anchor | b8efa77fe34cc0c7206086a6acc3303bd4045da4 | content (anchor) | proposed |
| gareth | skills/global-cross-cultural-pedagogies/place-based-inquiry-anchor | b8efa77fe34cc0c7206086a6acc3303bd4045da4 | content (anchor) | proposed |
| gareth | skills/wellbeing-motivation-agency/awe-wonder-experience-designer | 99984f00b6cdbb1c4fc64fcf0463d73896b1cd0a | content (anchor) | proposed |
| gareth | skills/environmental-experiential-learning/experiential-learning-cycle-designer | b8efa77fe34cc0c7206086a6acc3303bd4045da4 | content (rhythm) | proposed |
| gareth | skills/curriculum-assessment/learning-progression-builder | b8efa77fe34cc0c7206086a6acc3303bd4045da4 | content (progression) | proposed |
| gareth | skills/curriculum-assessment/backwards-design-unit-planner | b8efa77fe34cc0c7206086a6acc3303bd4045da4 | content | proposed |

## planning-subject-lessons

| Repo | Path | Commit last reviewed | Role | Status |
|---|---|---|---|---|
| k12 | plugin/skills/k12-lesson-plan-creation | 31fd6dbb0c07cb50bb3ce7f62a4135a393bd0e8c | structural | firm |
| gareth | skills/explicit-instruction/explicit-instruction-sequence-builder | b8efa77fe34cc0c7206086a6acc3303bd4045da4 | content (Explain, Elaborate) | proposed |
| gareth | skills/explicit-instruction/practice-problem-sequence-designer | b8efa77fe34cc0c7206086a6acc3303bd4045da4 | content (graded practice) | proposed |
| gareth | skills/memory-learning-science/retrieval-practice-generator | 99984f00b6cdbb1c4fc64fcf0463d73896b1cd0a | content (short sessions) | proposed |

Built in #11 (5E design, explicit instruction, graded practice, retrieval practice); the storyline option reuses this plugin's `planning-main-lesson-blocks` storyline design. The gareth paths were not re-read when building (no access from the build session), so they stay `proposed` at their recorded commits until the maintainer reviews them.

## writing-thai-core-plans

| Repo | Path | Commit last reviewed | Role | Status |
|---|---|---|---|---|
| gareth | skills/curriculum-assessment/competency-unpacker | b8efa77fe34cc0c7206086a6acc3303bd4045da4 | content (K-P-A unpacking) | firm |
| gareth | skills/curriculum-assessment/criterion-referenced-rubric-generator | 5edef15c5f905a09cef002a2608748c4a44c3f5b | content (4-level rubrics) | firm |
| gareth | skills/original-frameworks/single-point-rubric-designer | 99984f00b6cdbb1c4fc64fcf0463d73896b1cd0a | content (unscored self-check for assessment as learning) | firm |

## differentiating-for-learner-variability

| Repo | Path | Commit last reviewed | Role | Status |
|---|---|---|---|---|
| k12 | plugin/skills/k12-lesson-differentiation | 31fd6dbb0c07cb50bb3ce7f62a4135a393bd0e8c | structural (single plan, shared content written once; no tiering) | firm |
| gareth | skills/inclusive-design/udl-barrier-anticipator | 129d5842b2045e268e0abb6ba7acf7a0b93b0ba6 | content (barriers before supports; design versus specialist support) | proposed |
| gareth | skills/inclusive-design/udl-options-designer | 129d5842b2045e268e0abb6ba7acf7a0b93b0ba6 | content (specific options, goal integrity, few options) | proposed |
| gareth | skills/inclusive-design/udl-lesson-auditor | 129d5842b2045e268e0abb6ba7acf7a0b93b0ba6 | content (checklist) | proposed |
| gareth | skills/eal-language-development/language-demand-analyser | b8efa77fe34cc0c7206086a6acc3303bd4045da4 | content (language demands) | proposed |
| gareth | skills/eal-language-development/academic-language-sentence-frame-generator | b8efa77fe34cc0c7206086a6acc3303bd4045da4 | content (graded frames that carry the thinking) | proposed |
| gareth | skills/eal-language-development/vocabulary-tiering-tool | b8efa77fe34cc0c7206086a6acc3303bd4045da4 | content (vocabulary tiers) | proposed |
| gareth | skills/eal-language-development/scaffolded-task-modifier | b8efa77fe34cc0c7206086a6acc3303bd4045da4 | content (cognitive demand kept) | proposed |
| gareth | skills/original-frameworks/inclusive-design-orchestrator | 99984f00b6cdbb1c4fc64fcf0463d73896b1cd0a | content (alternate; not drawn on, candidate to drop) | proposed |
| gareth | skills/curriculum-assessment/differentiation-adapter | 99984f00b6cdbb1c4fc64fcf0463d73896b1cd0a | content (alternate; not drawn on, candidate to drop) | proposed |

## planning-formative-assessment

| Repo | Path | Commit last reviewed | Role | Status |
|---|---|---|---|---|
| k12 | plugin/skills/k12-check-for-understanding | 31fd6dbb0c07cb50bb3ce7f62a4135a393bd0e8c | structural (misconception-derived distractors, each response routed to a next step) | firm |
| gareth | skills/questioning-discussion/hinge-question-designer | b8efa77fe34cc0c7206086a6acc3303bd4045da4 | content | firm |
| gareth | skills/curriculum-assessment/formative-assessment-technique-selector | 99984f00b6cdbb1c4fc64fcf0463d73896b1cd0a | content | firm |
| gareth | skills/explicit-instruction/checking-for-understanding-protocol-designer | b8efa77fe34cc0c7206086a6acc3303bd4045da4 | content | firm |
| gareth | skills/self-regulated-learning/metacognitive-prompt-library | b8efa77fe34cc0c7206086a6acc3303bd4045da4 | content | firm |
| gareth | skills/memory-learning-science/retrieval-practice-generator | 99984f00b6cdbb1c4fc64fcf0463d73896b1cd0a | content | firm |
| gareth | skills/original-frameworks/single-point-rubric-designer | 99984f00b6cdbb1c4fc64fcf0463d73896b1cd0a | content (unscored single-point rubric for self-assessment) | firm |

Built in #14: hinge questions and misconception-based checks with routed responses (`references/assessment-for-learning.md`), metacognitive prompts, self- and peer assessment and single-point rubrics (`references/assessment-as-learning.md`), and the placement and channel rules (`references/placement-rules.md`). The gareth and k12 paths were not re-read when building (no access from the build session); their recorded commits stand until the maintainer reviews them.

## auditing-epistemic-agency

| Repo | Path | Commit last reviewed | Role | Status |
|---|---|---|---|---|
| gareth | skills/questioning-discussion/discussion-protocol-selector | b8efa77fe34cc0c7206086a6acc3303bd4045da4 | content (suggestions to open more) | proposed |
| gareth | skills/questioning-discussion/dialogic-teaching-move-generator | b8efa77fe34cc0c7206086a6acc3303bd4045da4 | content (suggestions to open more) | proposed |

## preparing-to-teach

| Repo | Path | Commit last reviewed | Role | Status |
|---|---|---|---|---|
| k12 | plugin/skills/k12-lesson-prep | 281eb8d41fe2837d911541c9bbb870b58add804c | content (short teacher-only note walking the session's own parts in teaching order; prepare from the actual plan, never a guess) | firm |
| gareth | skills/questioning-discussion/dialogic-teaching-move-generator | b8efa77fe34cc0c7206086a6acc3303bd4045da4 | content (talk-move types, matching the move to the response, no evaluating moves) | firm |

## check-upstream

Repo-only maintainer skill, not shipped. No upstream sources: written fresh from spec #1 and issue #17.

## Pending confirmation

ADR-0001 counts 29 education-agent-skills sources but names only 12. This record lists 12 firm and 18 proposed distinct paths (two of them alternates for differentiation), so at least one proposed path must be dropped when the count is confirmed. `awe-wonder-experience-designer` sits in the wellbeing-motivation-agency domain; ADR-0001 excludes wellbeing programmes, so confirm it is not one.
