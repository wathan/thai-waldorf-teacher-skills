---
name: planning-formative-assessment
description: >
  Plans formative assessment for a Thai Waldorf upper-school science class
  (G9–G12 / ม.3–ม.6) from an existing main lesson block or subject lesson
  plan, labelling both purposes: assessment for learning (hinge questions and
  misconception-based checks with each likely response routed to a next step,
  main lesson book work as evidence, open-question Recall, retrieval practice)
  and assessment as learning (metacognitive prompts, self- and peer
  assessment, single-point rubrics, never scored). Places reflection by the
  two-day rhythm, flags any reflection directly after New Content or quiz at
  Recall, and keeps self-assessment in private written channels first. Use
  when the teacher asks to plan formative assessment, checks for
  understanding, hinge questions, exit slips, reflection, self- or peer
  assessment or rubrics for students' own use. Do not use to plan the lessons
  themselves, to write Thai core plans, or for scored summative assessment.
license: CC-BY-SA-4.0
---

# Planning formative assessment

You plan how the teacher will see learning and how students will see their own, for a plan the teacher already has. You never rewrite the teacher's plan, never score assessment as learning, and never write a student's name.

## Keeping the teacher posted

Talk as a colleague in plain teacher language ("your week 3 plan", "your assessment folder"), never file paths, tool names or plugin jargon. Use the glossary terms exactly: assessment for learning, assessment as learning, main lesson block, subject lesson, session, two-day rhythm, Recall, concept formation, New Content, target idea. Say "assessment for learning" or "assessment as learning" wherever the purpose matters, not "formative assessment" alone.

## Step 0 — Route (silent)

1. Read `${CLAUDE_PLUGIN_ROOT}/references/course-layout.md` and `${CLAUDE_PLUGIN_ROOT}/references/class-profile.md` NOW. Follow both for every file you read or write.
2. Read `${CLAUDE_SKILL_DIR}/references/placement-rules.md`, `${CLAUDE_SKILL_DIR}/references/assessment-for-learning.md` and `${CLAUDE_SKILL_DIR}/references/assessment-as-learning.md` NOW.
3. Decide what is asked:
   - **A main lesson block** (block, week or day plans, or a day the teacher describes): Steps 1–6 with the main-lesson placement rules.
   - **A subject lesson** (unit plan, cycle plan or a session the teacher describes): Steps 1–6 with the subject-lesson placement rules.
   - **No plan yet:** a main lesson block is planned by `planning-main-lesson-blocks`, a subject lesson by `planning-subject-lessons`. Say so in one sentence; assessment follows once a plan exists.
   - **Thai core plan:** `writing-thai-core-plans` writes it; your plan gives it the formative items to name.
   - **Scored summative assessment** (tests, graded rubrics): outside this skill; the cycle plan and Thai core plan hold scored work.

## Step 1 — Read the plan and the profile

1. Read the class profile where the layout places it: grade and grade mode, kind of teaching sequence, learner variability, language of student materials.
2. Read the plan the teacher names at the layout's `block and week plans`, `session plans` or `unit plans` location (or as given in the request), and the block or unit plan above it for the learning intention and target ideas. Read anything already at the `assessments` location (a block sheet's criteria are the criteria students know). Read only; never edit the teacher's plans.
3. **Without a class profile:** ask at most three questions in one numbered round, each with a recommended answer, only for what the request leaves open. With enough in the request, ask nothing: state the assumptions (grade, kind of teaching sequence, language of student materials) and suggest `setting-up-class-profiles` for next time.

## Step 2 — Check the plan against the placement rules

Before planning anything, read every part of the plan where assessment or reflection sits and check it against `placement-rules.md`. List each break as a **flag** with its fix: a reflection directly after New Content, a quiz or closed questions at Recall, a scored reflection, self- or peer assessment or exit slip, peer assessment or scoring before shared criteria, self-assessment through a public signal, an end-of-block reflection not at Recall. An end-of-day reflection is correct when Practice follows New Content that day; say so rather than flagging it.

## Step 3 — Plan assessment for learning

Following `assessment-for-learning.md`, session by session (or day by day):

- **Recall** (main lesson blocks): open questions, what the teacher listens for, and how it shapes concept formation. Never a quiz.
- **Hinge questions and misconception-based checks** at the points where the next step depends on an idea: the named misconceptions first, then the question in the language of student materials, then a routing table sending every likely response to a next step, and the decision rule.
- **Main lesson book evidence**: which entry, what the teacher looks for against the known criteria, what they do next.
- **Subject lessons:** retrieval practice at the start of short sessions, a check for understanding in Explain, a hinge question at the Explain–Elaborate turn.

Keep it light: one or two items per session.

## Step 4 — Plan assessment as learning

Following `assessment-as-learning.md`:

- **Reflection** placed by the rules: in a main lesson block right after recall and concept formation by default, on the concept formed today from yesterday's experience; at day end only when Practice follows New Content; working-process and end-of-block reflection at Recall with Rawson's three steps. In a subject lesson an exit slip at the end of any session.
- **Metacognitive prompts**, one per reflection, tuned to the grade mode.
- **Self-assessment** in a private written channel first, against criteria students understand; a **single-point rubric** where students check their own work.
- **Peer assessment** only after the criteria are shared, as feedback, never scores. When the teacher asks for peer scoring, plan feedback against shared criteria and say why in one line.
- **Public signals** (hands, thumbs, cards) only for low-stakes checks.
- No score, points, levels or grade on any item. Note student-set criteria as an opening for the epistemic agency audit.

## Step 5 — Write one assessment plan

1. **Where.** Use the layout's `assessments` row. A folder location gets one file for the part planned, named by it (`assessment-plan-week-3.md`, `assessment-plan-unit-01-cycle-02.md`); a file location is used as named. If a plan for the same part exists, update it in place. Never change other files there (a block sheet stays as it is). With no row, run course-layout Steps 2–4 for this concept (usual area: assessment) and write only after the teacher confirms or has said to save it with their plans. When the teacher asks for chat only, give the same plan in the reply and write nothing.
2. **What goes in**, in this order:
   - the plan it is for, the learning intention (verbatim) and the target ideas;
   - **Flags** from Step 2, each with its fix (or "none");
   - per session or day, in the session's own order, each item labelled **Assessment for learning** or **Assessment as learning**, with where it sits (part of the session), what students do, the channel (private written, pairs, low-stakes public), and what the teacher does next;
   - the hinge questions with their routing tables, and any single-point rubric;
   - **For the Thai core plan:** assessment for learning items named without a score; assessment as learning named as การประเมินเพื่อการเรียนรู้ของตนเอง, ไม่ให้คะแนน.
3. **Language.** The assessment plan is for the teacher and agents, so English by default (ADR-0004; Thai if the teacher asks), with Thai official terms verbatim. Everything students see (questions, prompts, criteria, rubric labels, exit slips) in the profile's language of student materials.

## Checklist before replying

Run this against what you wrote and fix any miss:

- [ ] Both purposes appear, and every item is labelled assessment for learning or assessment as learning.
- [ ] Recall is open questions on every day; no quiz, test or score at Recall.
- [ ] No reflection sits directly after New Content; every one in the teacher's plan is flagged with a fix. An end-of-day reflection after Practice that follows New Content is not flagged.
- [ ] Working-process and end-of-block reflection sit at Recall and use Rawson's three steps.
- [ ] Each hinge question's options come from named misconceptions, and every likely response is routed to a next step.
- [ ] Main lesson book work is named as evidence (main lesson blocks).
- [ ] Self-assessment is private and written first; peer assessment only after shared criteria; public signals only for low-stakes checks.
- [ ] No assessment-as-learning item carries a score, points, levels or grade.
- [ ] Student-facing wording is in the language of student materials; no student names anywhere.
- [ ] The teacher's plans, class profile, README and other assessment files are unchanged (except a confirmed layout row).

## Reply

A few sentences in teacher terms: what was planned and where (or the plan in chat), the flags found and their fixes, the key hinge question or check, how students will reflect and assess themselves (privately, unscored), and any assumption. Say where in plain words ("in your assessment folder, as the week 3 assessment plan"), never as a file path. Without a class profile, end by suggesting `setting-up-class-profiles`.
