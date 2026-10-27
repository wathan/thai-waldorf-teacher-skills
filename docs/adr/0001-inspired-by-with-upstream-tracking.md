# Inspired-by skills with tracked upstream sources, licensed CC BY-SA 4.0

The plugin's skills are written fresh in one uniform shape (Anthropic's skill-authoring best practices, with k12-teacher-skills' lesson-plan-creation as the house template) rather than forked from anthropics/k12-teacher-skills or GarethManning/education-agent-skills, whose structures differ from each other and from that guideline. Each skill still records the upstream skills it draws on, with the commit last reviewed, in a root `UPSTREAM.md`; a repo-only `check-upstream` skill (not shipped in the plugin) reports which of our skills have upstream changes worth reviewing, and merging stays manual. Because the skills are derived from Gareth Manning's CC BY-SA 4.0 work, the plugin is licensed CC BY-SA 4.0 with attribution in `NOTICE`, which also satisfies k12-teacher-skills' Apache-2.0 notice terms.

## Considered Options

- **Fork and rewrite upstream skills:** rejected. Two incompatible structures, and US-specific content (NGSS, CCSS, Learning Commons, US edtech connectors) throughout.
- **Overlay (own context skills plus vendored upstream skills):** rejected. Mixed shapes inside one plugin, and vendored copies drift silently.
- **Inspired-by with no record of sources:** rejected. Loses the ability to pick up upstream improvements and obscures attribution.

## Skills in v1

Plugin: `setting-up-class-profiles`, `guiding-the-workflow`, `mapping-curriculum`, `planning-main-lesson-blocks`, `planning-subject-lessons`, `writing-thai-core-plans`, `differentiating-for-learner-variability`, `planning-formative-assessment`, `auditing-epistemic-agency`, `preparing-to-teach`. Repo only: `check-upstream`. Upstream sources: 4 k12-teacher-skills skills, 29 education-agent-skills skills (including `curriculum-crosswalk`, `coverage-audit`, `ecological-inquiry-anchor-designer` and `metacognitive-prompt-library`), and mattpocock/skills `grilling` (MIT).

k12's skills are structural sources only where their content does not fit: `k12-check-for-understanding` is maths-only, so only its shape (misconception-derived distractors, each likely response routed to a next step) is kept; `k12-lesson-differentiation` lends its single-plan output with shared content written once, not its below/at/above tiering. `differentiating-for-learner-variability` defaults to one shared task every student can start, with room to extend and several ways in.

`planning-formative-assessment` covers both assessment for learning and assessment as learning. From self-regulated-learning only `metacognitive-prompt-library` is taken; goal-setting, study strategies, error analysis and self-regulation scaffolds serve study habits and individual coaching, beyond lesson planning.

Gareth domains left out on purpose: AI-tutoring and student-facing (ai-learning-science, ai-literacy, student-learning), other disciplines or traditions (historical-thinking, montessori), wellbeing programmes, and Manning's own KUD/band methodology (`kud-chart-author`, `developmental-band-translator`: Thai plans use K-P-A and Thai indicators are already per grade). Specific rejections:

- Socratic questioning sequences: converge on the teacher's answer, closing the explanatory-model domain.
- `agency-scaffold-generator`: rests on "choice, voice, ownership", which the thesis treats as too broad.
- `dispositional-knowledge-assessment-designer`: treats agency as an individual disposition, whereas the thesis defines epistemic agency as enacted and community-level; scoring students on it would also contradict the plan-only audit.
- `mixed-age-learning-task-designer`: addresses mixed age, not the single-grade mixed-ability upper-school class.
- CER and argument scaffolds (deferred): fix the form of the class's model.

v2 candidates: main lesson book writing (`disciplinary-writing-scaffold`), scope and sequence, thesis tooling (uptake coding, stimulated recall; `lesson-study-cycle-designer`, `teacher-inquiry-cycle-designer`, `lesson-observation-protocol-designer`, `reflective-practice-prompt-generator`), systems-thinking epistemic tools for G11/G12.

## Consequences

- Upstream changes never arrive automatically; someone runs `check-upstream` and decides.
- Publishing later needs no relicensing: attribution and share-alike are in place from the first commit.
