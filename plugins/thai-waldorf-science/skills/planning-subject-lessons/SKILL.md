---
name: planning-subject-lessons
description: >
  Plans a subject lesson for a Thai Waldorf upper-school science class
  (G9–G12 / ม.3–ม.6), such as Science Practice, as 5E inquiry by default
  (storyline design on request): units of one topic made of one or more 5E
  cycles, phases placed across the class's weekly pattern of long and short
  sessions as the design needs, explicit instruction and graded practice
  inside Explain and Elaborate, retrieval practice for short consolidation
  sessions, Thai indicators verbatim and light universal UDL options. Writes
  the unit plan and one cycle plan per 5E cycle, each saying how its phases
  fall on the Thai core plan stages. Use when the teacher asks to plan,
  design or rework a subject lesson, a unit of one, a 5E cycle or 5E
  sessions. Do not use for main lesson blocks, Thai core plans or a single
  standards map.
license: CC-BY-SA-4.0
---

# Planning subject lessons

You design one unit of a subject lesson with the teacher and write its unit plan and its cycle plans. A subject lesson recurs in the weekly timetable across a term; its units are one topic each, built from one or more 5E cycles. Subject lessons have no Waldorf plans: the unit plan and cycle plans are the design, and the Thai core plan (one per 5E cycle) is written from them by `writing-thai-core-plans`.

## Keeping the teacher posted

Talk as a colleague in plain teacher language: "your design folder", "your unit 1 plan", never file paths, tool names or plugin jargon. Use the glossary terms exactly: subject lesson, unit, session, 5E inquiry, Thai core plan, target idea, prerequisite idea, grade mode, learner variability, assessment as learning; with a storyline design also anchoring phenomenon, driving question, driving question board.

## Step 0 — Route (silent)

1. Read `${CLAUDE_PLUGIN_ROOT}/references/course-layout.md` and `${CLAUDE_PLUGIN_ROOT}/references/class-profile.md` NOW. Follow both for every file you read or write.
2. Read `${CLAUDE_SKILL_DIR}/references/5e-design.md` NOW: cycles, phase placement, explicit instruction, graded practice, retrieval practice and the two plan formats. It applies to every route below.
3. Decide what is asked:
   - **A unit as 5E inquiry** (the default, also for "plan my next unit" or "a 5E lesson on …"): Steps 1–5.
   - **A unit as a storyline design** (only when the teacher asks for a storyline, an anchoring phenomenon or a driving question board): also read `${CLAUDE_PLUGIN_ROOT}/skills/planning-main-lesson-blocks/references/storyline-design.md` (anchor, driving question, ideas, board) and `${CLAUDE_SKILL_DIR}/references/storyline-units.md` (how they fit a subject lesson's cycles and weekly pattern) NOW. Steps 1–5 still apply.
   - **One more cycle or a reworked cycle** in a unit already planned: Steps 1, 4 and 5 for that cycle; keep the unit plan's decisions.
   - **Thai core plans:** belong to `writing-thai-core-plans`, after the cycle plans exist. **A main lesson block:** belongs to `planning-main-lesson-blocks`.

## Step 1 — Context, at most three questions

1. Read the class profile where the layout places it: grade, grade mode, schedule (sessions per week, each session's length and day, length of the sequence), learner variability, languages, academic year.
2. Read what the course already holds: the standards map (the indicators each unit claims), earlier unit plans (what students met before), and any plan or notes for this unit. The teacher's decisions there stand unless they ask to change them.
3. **Scope.** Plan exactly the unit asked for, over the weeks the request or the course gives; otherwise propose a length from the indicators (usually two to four weeks) and state it.
4. **Without a class profile:** ask at most three questions in one numbered round, each with a recommended answer, and only for what the request leaves open: the grade; the sessions per week with their lengths and days; and, with a storyline design, the anchor if none is chosen. The kind of teaching sequence is already known: a subject lesson. State every other value as an assumption using the class profile defaults (one long 100-minute and one short 50-minute session a week, for one term; Thai for instruction and student materials; the academic year in progress), and suggest `setting-up-class-profiles` for next time. When the teacher says to go ahead with defaults, ask nothing that has a default.

Never read the course folder's name for meaning.

## Step 2 — Ground the unit in the three frameworks

Read these NOW:

- `${CLAUDE_PLUGIN_ROOT}/references/waldorf-upper-school-macro-curriculum.md`: the grade mode card for this grade; phrase the unit's aims in that mode.
- `${CLAUDE_PLUGIN_ROOT}/references/waldorf-pisa-competencies-g9-g12.md`: pick a few of this grade's Sx.n / Ex.n as learning intentions.
- `${CLAUDE_PLUGIN_ROOT}/references/curriculum-crosswalk.md`: the only place to match Thai indicators. Take the indicators the standards map gives this unit, or the teacher's; otherwise choose matching indicators for the class's ม. grade. Quote each code (`ว x.x ม.n/k`) and its Thai wording character for character, and read its verb through `${CLAUDE_PLUGIN_ROOT}/references/thai-science-glossary-2560.md`. An indicator from another ม. grade is a sequencing difference: cite it as written with one line of grade-mode reason.

Keep the three frameworks in their own wording; never merge them into one statement.

## Step 3 — Design the unit

Follow `5e-design.md`: one topic; target ideas and prerequisite ideas listed separately; one or more 5E cycles, each with its own question in students' terms, its indicators and its target ideas. With a storyline design, follow `storyline-units.md` too: the anchoring phenomenon is the teacher's (offer candidates if none is chosen, never choose, write no plan files while it is open), the driving question's authorship is stated, and the driving question board frames the cycles.

## Step 4 — Place each cycle's phases on the weekly pattern

Follow `5e-design.md`. Lay the cycles over the actual sessions of the class profile's weekly pattern in calendar order, whatever the pattern is. Place each phase where its work fits (a phase may span sessions; a session may hold several phases) and give each placement a short reason from the design. Put explicit instruction and graded practice inside Explain and Elaborate where the unit needs a skill, procedure or calculation; give short consolidation sessions retrieval practice; let sessions close with an exit-slip reflection where it helps. Every session carries light universal UDL options. Then record, per cycle, how its phases fall on the Thai core plan stages (ขั้นนำ / ขั้นสอน / ขั้นสรุป) as this design runs them.

## Step 5 — Write the unit plan and the cycle plans

1. **Where.** The unit plan goes to the layout's `unit plans` row; the cycle plans to the `session plans` row. A folder location gets `unit-01-plan.md` and `unit-01-cycle-01.md`, `unit-01-cycle-02.md`, … (two-digit unit and cycle numbers; continue the course's own naming if its files already use another); a file location holds the unit plan followed by one section per cycle. If a plan already exists there, update it in place and keep the teacher's decisions; never create a second one. With no row, run course-layout Steps 2–4 for these concepts (usual area: design) and write only after the teacher confirms (or has said up front they accept your proposal).
2. **Which form.** If the templates location holds the course's own unit plan or session plan form (cues: unit plan, แผนหน่วย, 5E, session, lesson plan form), use it exactly: its headings, labels and order win, and the rules here still hold wherever it has a matching place. Otherwise use the formats in `5e-design.md`. Say in one line which one you used. Never write a Waldorf block, week or day plan for a subject lesson.
3. **Language.** Thai by default (English when the teacher asks), with Thai official terms (indicators, ปีการศึกษา, IPST's Thai phase names) verbatim; student-facing wording (prompts, retrieval questions, exit slips) in the class profile's language of student materials.

Thai core plans are not written in this step.

## Checklist before replying

Run this against the files you wrote, and fix any miss before replying:

- [ ] The unit is one topic made of one or more 5E cycles; each cycle runs Engage, Explore, Explain, Elaborate and Evaluate in that order.
- [ ] Sessions follow the class profile's weekly pattern in calendar order; each session's minutes add up to its length.
- [ ] Phase placement follows the design, with a reason per placement; no split repeated by habit, no Explain before Explore.
- [ ] Engage raises the question without telling the answer; in Explain students explain from their own evidence before terms or formulae are introduced.
- [ ] Explicit instruction and graded practice sit inside Explain or Elaborate, where the unit needs a skill, procedure or calculation.
- [ ] Short consolidation sessions carry retrieval practice: from memory, low-stakes, never scored.
- [ ] Exit slips and self-assessment are named as assessment as learning, never scored.
- [ ] Each cycle plan states its Thai core plan stage mapping, matching what its sessions actually do.
- [ ] Thai indicator codes and wording are verbatim; frameworks are not merged; target and prerequisite ideas listed separately.
- [ ] Storyline design only: the anchor is the teacher's choice and the plan says so; the driving question's authorship is stated; students' questions on the board are never invented.
- [ ] Every session carries light universal UDL options; one shared task every student can start; no ability tiers.
- [ ] No Waldorf plans and no Thai core plans written; no student names or identifying details.
- [ ] Files sit where the layout says; nothing renamed, moved or deleted.

## Reply

A few sentences: what was written and where in teacher terms, which form was used, the cycles and how they fall across the week, any assumption made, and the next steps (Thai core plans per cycle through `writing-thai-core-plans`; targeted supports through `differentiating-for-learner-variability`; the epistemic agency audit once available).
