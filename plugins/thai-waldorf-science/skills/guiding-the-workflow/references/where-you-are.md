# Where the teacher is: reading the course folder

How to tell the teacher where they are in the design and teaching process, and which skill comes next, from the files already in the course folder. Read-only: never write, rename or move anything, never record a layout, never ask before answering.

## Contents

- [Step 1: look (silently)](#step-1-look-silently)
- [Step 2: find each piece of work](#step-2-find-each-piece-of-work)
- [Step 3: choose the next step](#step-3-choose-the-next-step)
- [Step 4: reply](#step-4-reply)

## Step 1: look (silently)

1. List the course folder, three levels deep, skipping hidden entries. Never read meaning into the folder's own name or mention it.
2. **Nothing there** (empty, or only hidden files): stop here and give the fixed walkthrough (`walkthrough.md`). That is the fallback whenever there is no course to read.
3. Read the top-level README's `## Plugin layout` table if there is one (course-layout Step 1, read in Step 0). Its rows say where each concept lives; use them as written.
4. **No layout table:** recognise files by the name and content cues in course-layout's Step 2 and by the file names the skills write (Step 2 below). Do not propose or record a layout here; the skill that next writes a file does that.

## Step 2: find each piece of work

Check each concept at its mapped location (or by cues), opening a file's first lines only when its name does not settle what it is. A plan counts as done when the file exists with content; a file that is still only the blank template does not count.

| Piece of work | Concept (layout row) | Usual file names | Written by |
|---|---|---|---|
| Class profile | class profile | `class-profile.md` | `setting-up-class-profiles` |
| Year plan pointer | the profile's "Year plan" section | a path, or none | `setting-up-class-profiles` |
| Standards map | standards map | `standards-map.md` | `mapping-curriculum` |
| Block plan, week plans | block and week plans | `block-plan.md`, `week-1-plan.md`, … | `planning-main-lesson-blocks` |
| Day plans | session plans | `week-1-day-1.md`, … | `planning-main-lesson-blocks` |
| Unit plans, cycle plans (subject lessons) | unit plans, session plans | `unit-01-plan.md`, `unit-01-cycle-01.md`, … | `planning-subject-lessons` |
| Thai core plans | Thai core plans | `day-01-thai-core-plan.md`, `unit-01-cycle-01-thai-core-plan.md`, … | `writing-thai-core-plans` |
| Differentiation | differentiation | `differentiation-week-1.md`, … | `differentiating-for-learner-variability` |
| Formative assessment | assessments | `assessment-plan-week-1.md`, … | `planning-formative-assessment` |
| Epistemic agency audit | agency audit | `agency-audit-week-1.md`, `agency-audit-block.md`, … | `auditing-epistemic-agency` |
| Preparation notes | preparation notes | `week-1-day-1-prep.md`, `session-4-prep.md`, … | `preparing-to-teach` |

From the class profile read only: the kind of teaching sequence (main lesson block or subject lesson), its name, grade, length (weeks or term) and the year plan pointer. If the profile points to a year plan, you may check that file exists; read nothing else outside the course folder.

Work goes forward **week by week** (main lesson block) or **unit by unit** (subject lesson). For rows 5–10 below, the **current week** (or unit) is the earliest one that still has a session without a preparation note: that is where the teacher is, even when its plans are all written. A later week becomes current only once every session of the earlier week has a preparation note.

## Step 3: choose the next step

Take the **first** row whose condition holds; that skill is the next step. The row after it is "after that".

| # | Condition | Next step | What to ask for |
|---|---|---|---|
| 1 | No class profile | `setting-up-class-profiles` | describe the class (later skills can work without it, asking up to three questions) |
| 2 | No standards map, and no block plan or unit plan yet | `mapping-curriculum` | the Thai indicators this sequence claims (optional; planning can start straight away and choose indicators itself) |
| 3 | No block plan (main lesson block) or no unit plan (subject lesson) | `planning-main-lesson-blocks` or `planning-subject-lessons`, by the profile's kind | plan the block, or the subject lesson units |
| 4 | Main lesson block: a week in the block plan has no week plan | `planning-main-lesson-blocks` | the missing week plans |
| 5 | The current week has no day plans (main lesson block), or the current unit has no cycle plans (subject lesson) | `planning-main-lesson-blocks` (day plans for that week, on request) or `planning-subject-lessons` | day plans for that week; the Thai core plans are written from them |
| 6 | That week's days, or that unit's 5E cycles, have no Thai core plans | `writing-thai-core-plans` | Thai core plans for that week, or for that unit's cycles |
| 7 | No differentiation for that week or unit | `differentiating-for-learner-variability` | adapt that week's or unit's plans |
| 8 | No formative assessment for that week or unit | `planning-formative-assessment` | hinge questions and reflection for that week or unit |
| 9 | No saved epistemic agency audit for that week or unit | `auditing-epistemic-agency` | audit that week's or unit's plans |
| 10 | Everything above is there for the current week or unit | `preparing-to-teach` | prepare the current week's first session that has no preparation note, named by week and day (e.g. week 1, day 1, Monday) or by session; planning the next week or unit is "after that" |

Notes on the order:

- Rows 7–9 may be done in any order; name the first missing one as next and list the others as still open. The audit usually runs straight after planning; if none is saved, say you see no saved audit (it may have been given only in chat) and offer it.
- Row 2 is optional: say the teacher may skip straight to planning.
- **Anticipated route** (the block plan marks units interchangeable): weeks after the current unit are planned only once the driving question board has chosen the next unit; rows 4–9 apply to units already chosen.
- Do not jump ahead to planning the next week while the current week's sessions still need preparing: preparing comes first, the next week's day plans come after. When the last week is prepared, say the sequence is fully planned.
- If the profile points to a year plan, mention once that `mapping-curriculum` can check the whole year's coverage; never let it replace the next step.

## Step 4: reply

Keep it short, in the teacher's language. Name the work, never where it is kept: no file paths, file names or folder names (not even "the templates folder" or "the evaluation folder"), and no talk of the layout.

1. **Where you are:** two to four plain bullets of what is already done (e.g. "a class profile for your G12 meteorology block; the block plan and all three week plans; no day plans yet").
2. **Next:** the one skill from Step 3, in a sentence: what to ask it for and what the teacher will get.
3. **After that:** one or two following steps, by skill name.
4. Ask whether that matches where they are (they may have done work that is not saved in the course folder).

If the teacher asked "what now?" together with another question, answer the question too, from the skill map in SKILL.md.
