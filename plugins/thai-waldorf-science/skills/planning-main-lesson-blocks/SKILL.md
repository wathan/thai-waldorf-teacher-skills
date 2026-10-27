---
name: planning-main-lesson-blocks
description: >
  Plans a storyline-based main lesson block for a Thai Waldorf upper-school
  science class (G9–G12 / ม.3–ม.6): grade mode, learning intentions and Thai
  indicators from the curriculum crosswalk, candidate anchoring phenomena for
  the teacher to choose, a driving question with its authorship stated, target
  and prerequisite ideas, units in a fixed sequence (or, on request, an
  anticipated route of fixed and interchangeable units chosen through the
  driving question board), the two-day rhythm (after
  Zech) with storyline routines fitted to it, and light universal UDL options.
  Writes the Waldorf block plan and week plans into the course folder, and day
  plans on request. Use when the teacher asks to plan, design, draft or rework a
  main lesson block (e.g. a meteorology or ecology block), its units, its week
  plans or its day plans. Do not use for
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
   - **Anticipated route** (only when the teacher asks for it: interchangeable units arranged as the driving question board directs): read `${CLAUDE_SKILL_DIR}/references/anticipated-route.md` NOW. Steps 1–6 still apply; that reference replaces their fixed-order parts and says which week plans to write now. When the teacher reports the board's choice of the next unit, follow its rolling generation instead of planning the block again.
   - **Day plans** (one day, one week or the whole block), in the two-day rhythm or, when the teacher asks, Rawson's four-day cycle: read `${CLAUDE_SKILL_DIR}/references/day-plans.md` NOW and follow it, after Step 1 and the block and week plans it needs. A whole-block document set is the block plan, week plans and every day plan; Thai core plans then go to `writing-thai-core-plans`.
   - **Thai core plans:** belong to `writing-thai-core-plans`, after the block plan exists.
   - **A subject lesson:** belongs to `planning-subject-lessons`.

## Step 1 — Context, at most three questions

1. Read the class profile where the layout places it: grade, grade mode, schedule (session length, days per week, weeks), learner variability, languages, academic year.
2. Read what the course already holds for this block: an existing block plan or notes at the mapped locations (anchor, units, indicators the teacher has chosen). The teacher's decisions there stand unless they ask to change them.
3. **Without a class profile:** follow class-profile.md's "When there is no class profile" (at most three questions in one numbered round; every other value a stated assumption from its defaults). The questions you may ask: the grade; the session length and count (days per week, weeks); and, if no anchoring phenomenon is chosen yet, the choice of anchor from your candidates (Step 2). The kind of teaching sequence is already known: a main lesson block.

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
4. **Language.** Thai by default (English when the teacher asks), with Thai official terms (indicators, ปีการศึกษา, form labels) verbatim; student-facing wording (recall questions, prompts) in the class profile's language of student materials. Keep each form's bilingual labels.

Day plans and Thai core plans are not written in this step.

## Checklist before replying

Run this against the files you wrote, and fix any miss before replying:

- [ ] The anchoring phenomenon is the teacher's choice, and the plan says so.
- [ ] The driving question's authorship is stated.
- [ ] Target ideas and prerequisite ideas are listed separately.
- [ ] Units run in a fixed order, each marked fixed; the driving question board frames ideas, not order. (Anticipated route: that reference's checklist instead.)
- [ ] Thai indicator codes and wording are verbatim; frameworks are not merged.
- [ ] Day 1 links to the previous block in this subject; every later day opens with Recall of yesterday's experience flowing into concept formation.
- [ ] Recall is open questions, never a quiz or a test.
- [ ] Concept formation is an individual position integrated into the class's understanding, never a predetermined concept stated as the answer.
- [ ] No session discusses, analyses or explains that day's new experience; a reflection never follows New Content directly.
- [ ] No four-day cycle labels (E→R→C→A, concept formation two days later) unless the teacher asked for the four-day cycle.
- [ ] Every session carries light universal UDL options; one shared task every student can start; no ability tiers.
- [ ] No student names or identifying details.
- [ ] Files sit where the layout says; nothing renamed, moved or deleted.

Then the generation checklist in `${CLAUDE_PLUGIN_ROOT}/references/rawson2021-generative-principles-upper-school.md` §5, read through the two-day rhythm: item 3 asks for overnight recall and concept formation the next day, not overlapping four-day cycles, and item 10's three levels become UDL options within one shared task.

## Then the audit

After writing any plan files, run `auditing-epistemic-agency` on what you wrote, unless the teacher switched it off for this request ("no audit", "skip the audit", "quick draft").

## Reply

A few sentences: what was written and where in teacher terms, the anchor and the driving question with its authorship, any assumption made, the audit's short summary (unless switched off), and the next steps (day plans and Thai core plans on request).
