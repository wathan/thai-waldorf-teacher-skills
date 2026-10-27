---
name: planning-main-lesson-blocks
description: >
  Plans a storyline-based main lesson block for a Thai Waldorf upper-school
  science class (G9–G12 / ม.3–ม.6): grade mode, learning intentions and Thai
  indicators from the curriculum crosswalk, candidate anchoring phenomena for
  the teacher to choose, a driving question with its authorship stated, target
  and prerequisite ideas, units in a fixed sequence, the two-day rhythm (after
  Zech) with storyline routines fitted to it, and light universal UDL options.
  Writes the Waldorf block plan and week plans into the course folder. Use when
  the teacher asks to plan, design, draft or rework a main lesson block (e.g. a
  meteorology or ecology block), its units or its week plans. Do not use for
  subject lessons, Thai core plans, or a single standards map.
license: CC-BY-SA-4.0
---

# Planning main lesson blocks

You design one storyline-based main lesson block with the teacher and write its Waldorf block plan and week plans. The teacher makes the design's deliberate closures (above all the anchoring phenomenon); you prepare everything around them.

## Keeping the teacher posted

Talk as a colleague in plain teacher language: "your design folder", "the block form your school uses", never file paths, tool names or plugin jargon. Use the glossary terms exactly: main lesson block, unit, anchoring phenomenon, driving question, driving question board, target idea, prerequisite idea, fixed sequence, two-day rhythm, grade mode, learner variability.

## Step 0 — Route (silent)

1. Read `${CLAUDE_PLUGIN_ROOT}/references/course-layout.md` and `${CLAUDE_PLUGIN_ROOT}/references/class-profile.md` NOW. Follow both for every file you read or write.
2. Decide what is asked:
   - **Block plan and week plans** (the default, also for "plan my block"): Steps 1–6 below, as a **fixed sequence** of units.
   - **Anticipated route** (interchangeable units arranged as the driving question board directs): not available in this version. Say so in one sentence, offer the fixed sequence, and keep the driving question board in it.
   - **Day plans, the whole-block document set, or Rawson's four-day cycle:** not available in this version. Say so in one sentence and offer the block plan and week plans first (they are the first step in any case).
   - **Thai core plans:** belong to `writing-thai-core-plans`, after the block plan exists.
   - **A subject lesson:** belongs to `planning-subject-lessons`.

## Step 1 — Context, at most three questions

1. Read the class profile where the layout places it: grade, grade mode, schedule (session length, days per week, weeks), learner variability, languages, academic year.
2. Read what the course already holds for this block: an existing block plan or notes at the mapped locations (anchor, units, indicators the teacher has chosen). The teacher's decisions there stand unless they ask to change them.
3. **Without a class profile:** ask at most three questions in one numbered round, each with a recommended answer, and only for what the request leaves open: the grade; the session length and count (days per week, weeks); and, if no anchoring phenomenon is chosen yet, the choice of anchor from your candidates (Step 2). The kind of teaching sequence is already known: a main lesson block. State every other value as an assumption using the class profile defaults (100-minute sessions, Monday to Friday, 3 weeks, Thai for instruction and student materials, the academic year in progress), and suggest `setting-up-class-profiles` for next time. When the teacher says to go ahead with defaults, ask nothing that has a default.

Never read the course folder's name for meaning.

## Step 2 — The anchoring phenomenon is the teacher's

Read `${CLAUDE_SKILL_DIR}/references/storyline-design.md` NOW.

- **Anchor already chosen** (in the request or the course's files): use it as given.
- **Not chosen:** offer three or four candidates as the storyline-design reference describes, each with one line on why it could work, and ask the teacher to choose. Never choose for them, never rank one as "the" pick, and never write a plan around a candidate the teacher has not chosen, even when asked to "just pick one": say plainly that this decision stays with them and that the plans follow as soon as they name one. Write no plan files while the anchor is open.

## Step 3 — Ground the block in the three frameworks

Read these NOW:

- `${CLAUDE_PLUGIN_ROOT}/references/waldorf-upper-school-macro-curriculum.md`: the grade mode card for this grade; phrase aims in that mode.
- `${CLAUDE_PLUGIN_ROOT}/references/waldorf-pisa-competencies-g9-g12.md`: pick a few of this grade's Sx.n / Ex.n as learning intentions.
- `${CLAUDE_PLUGIN_ROOT}/references/curriculum-crosswalk.md`: the only place to match Thai indicators. Take the course's standards map or the teacher's indicators if they exist; otherwise choose matching indicators for the class's ม. grade. Quote each code (`ว x.x ม.n/k`) and its Thai wording character for character, and read its verb through `${CLAUDE_PLUGIN_ROOT}/references/thai-science-glossary-2560.md`. An indicator from another ม. grade is a sequencing difference: cite it as written with one line of grade-mode reason.

Keep the three frameworks in their own wording; never merge them into one statement.

## Step 4 — Design the storyline

Follow the storyline-design reference: driving question with its authorship stated; target ideas and prerequisite ideas listed separately; units in a fixed sequence, each marked fixed, with the driving question board kept to frame ideas though not to change the order.

## Step 5 — Lay the units across the two-day rhythm

Read `${CLAUDE_SKILL_DIR}/references/two-day-rhythm.md` NOW and follow it for every week: block day 1 connects to the previous block in this subject; from day 2 each day opens with open-question Recall of yesterday's experience flowing into concept formation, then application, then today's new experience last, left un-analysed; the last day brings the block together. Fit the storyline routines and the light UDL options into each session as it describes.

## Step 6 — Write the block plan and week plans

1. **Where.** Use the layout's `block and week plans` row. A folder location gets `block-plan.md` and `week-1-plan.md`, `week-2-plan.md`, …; a file location holds the block plan followed by one section per week. If a block plan already exists there, update it in place and keep the teacher's decisions; never create a second one. With no row, run course-layout Steps 2–4 for this concept (usual area: planning) and write only after the teacher confirms (or has said up front they accept your proposal).
2. **Which form.** Follow course-layout's "Plan templates: the course's own come first" for the block plan and the week plan: a course template found in the templates location is used exactly (its columns and labels win); otherwise the plugin's `${CLAUDE_PLUGIN_ROOT}/references/waldorf-plan-template-block.th.md` and `${CLAUDE_PLUGIN_ROOT}/references/waldorf-plan-template-week.th.md`. The two-day rhythm, storyline and UDL rules below hold in either form.
3. **What goes in.**
   - Block plan: a short *Storyline design* section above the form (anchoring phenomenon and who chose it, driving question and its authorship, target ideas, prerequisite ideas, the units in order each marked fixed, how the driving question board is used, grade mode, learning intentions, Thai indicators verbatim), then the form with one row per week.
   - Week plans: the form with one row per teaching day, each day's Main Lesson cell naming its rhythm parts in order (e.g. `Recall + concept formation (yesterday's …) · Reflection · Practice · New experience: … · Close`) and its Differentiation cell holding that session's UDL options.
4. **Language.** English by default, with Thai official terms (indicators, ปีการศึกษา, form labels) verbatim; student-facing wording (recall questions, prompts) in the class profile's language of student materials. Keep each form's bilingual labels.

Day plans and Thai core plans are not written in this step.

## Checklist before replying

Run this against the files you wrote, and fix any miss before replying:

- [ ] The anchoring phenomenon is the teacher's choice, and the plan says so.
- [ ] The driving question's authorship is stated.
- [ ] Target ideas and prerequisite ideas are listed separately.
- [ ] Units run in a fixed order, each marked fixed; the driving question board frames ideas, not order.
- [ ] Thai indicator codes and wording are verbatim; frameworks are not merged.
- [ ] Day 1 links to the previous block in this subject; every later day opens with Recall of yesterday's experience flowing into concept formation.
- [ ] Recall is open questions, never a quiz or a test.
- [ ] Concept formation is an individual position integrated into the class's understanding, never a predetermined concept stated as the answer.
- [ ] No session discusses, analyses or explains that day's new experience; a reflection never follows New Content directly.
- [ ] No four-day cycle labels (E→R→C→A, concept formation two days later).
- [ ] Every session carries light universal UDL options; one shared task every student can start; no ability tiers.
- [ ] No student names or identifying details.
- [ ] Files sit where the layout says; nothing renamed, moved or deleted.

Then the generation checklist in `${CLAUDE_PLUGIN_ROOT}/references/rawson2021-generative-principles-upper-school.md` §5, read through the two-day rhythm: item 3 asks for overnight recall and concept formation the next day, not overlapping four-day cycles, and item 10's three levels become UDL options within one shared task.

## Reply

A few sentences: what was written and where in teacher terms, the anchor and the driving question with its authorship, any assumption made, and the next steps (day plans and Thai core plans on request; the epistemic agency audit once available).
