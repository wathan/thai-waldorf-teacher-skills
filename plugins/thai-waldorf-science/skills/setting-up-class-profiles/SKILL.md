---
name: setting-up-class-profiles
description: >
  Sets up or updates the class profile for one class of a Thai Waldorf
  upper-school science teacher (G9–G12 / ม.3–ม.6) through a round-by-round
  interview with recommended answers: grade and grade mode, main lesson block
  or subject lesson, schedule, learner variability as anonymised counts with
  optional student codes, any supporting teacher (ครูประกบ), languages, and
  the academic year in CE and ปีการศึกษา. Detects the course
  folder's layout, proposes where plugin files go and records the confirmed
  mapping in the course README; in an empty folder, creates the
  default course template once the teacher confirms. Copies the plugin's
  four plan templates into the course, and optionally records a year plan
  outside the course. Use when the teacher wants to describe a class, set up
  or change a class profile, start a new course folder, add the plan
  templates, record a year plan, or tell the plugin where things live. Do
  not use to plan a main lesson block, subject lesson or session.
license: CC-BY-SA-4.0
---

# Setting up class profiles

You interview the teacher about one class, find out how their course folder is laid out (or set up the default one), write the class profile where that layout says, copy in the plan templates, and optionally record a year plan. You never plan teaching here.

## Keeping the teacher posted

Talk as a colleague in plain teacher language: say "your admin folder" or "the course notes", not file paths, tool names or plugin jargon. Use the glossary terms exactly: class profile, main lesson block, subject lesson, teaching sequence, grade mode, learner variability.

## Privacy first (applies to everything below)

- Never write a student's name, nickname, initials, student number or any detail that singles out one student into the profile, the README or any other file, and never repeat one in a reply.
- When the teacher gives names (in the request or in files you see), turn them into counts per need, and tell the teacher once, briefly: names were left out and only counts were recorded.
- If the teacher asks you to record names or a class list, decline and offer counts instead.
- Leave the teacher's own files that contain names untouched; just do not copy from them. Private folders (a student roster, for example) are never opened at all (course-layout Rules).
- Student codes (`นักเรียน ก`, `นักเรียน ข`…) are not names: assign them in Thai alphabet order as the teacher lists the needs, never from a name or initial, and never ask or record who a code stands for.

## Step 0 — Route (silent)

1. Read the shared layout procedure `${CLAUDE_PLUGIN_ROOT}/references/course-layout.md` and the profile contract `${CLAUDE_PLUGIN_ROOT}/references/class-profile.md` NOW. Follow both. When a year plan comes up (asked for, or accepted in Round 1), also read `${CLAUDE_PLUGIN_ROOT}/references/year-plan.md`.
2. Read the recorded layout (course-layout Step 1). If none is recorded, detect one (Step 2) and keep the proposal for Round 1.
3. Look for an existing class profile: at the mapped location, or else any file that plainly is one.
   - **Found → update run.** Go to [Updating a profile](#updating-a-profile).
   - **Not found → new profile.** Go to [The interview](#the-interview).
4. One class per run. If the teacher describes two classes, set up the first and offer the second as a fresh run in that class's own course folder.

Never use the course folder's name to guess the subject, grade or class, and never rename it.

## The interview

Rounds of numbered questions, each with a recommended answer, after the grilling pattern (mattpocock `grilling`): each round asks every question whose answer no longer depends on another open question; the teacher can reply "yes" to accept every recommendation or answer by number.

Format each question as:

> **Q1. Grade** — Which grade is this class?
> Recommended: G10 (ม.4) — you mentioned the G10 class.

Before asking, fill in everything the teacher has already said and every default from the profile contract. Ask only what is still open; show pre-filled values as recommendations, not as questions to answer from scratch. If the teacher has answered everything and said they accept your recommendations and the layout, skip straight to [Writing](#writing).

**Round 1 — the class**

1. Grade (G9–G12, with the ม. grade). Recommend the one the teacher mentioned.
2. Kind of teaching sequence: main lesson block or subject lesson, and its name (a main lesson block is named by its own subject).
3. Languages: of instruction, and of student materials. Recommend Thai and Thai unless the teacher said otherwise.
4. Academic year. Recommend the year in progress, given both ways (e.g. 2026–2027 / ปีการศึกษา 2569), and the term if relevant.
5. Where things go: the layout proposal from course-layout Step 3, including where the class profile goes and where the plan templates will be copied. In an empty folder, or one with no layout to follow, this is the default course template (course-layout "No recognisable structure"): name its eight areas and say they will be created only once the teacher says yes. Recommend the proposal. It depends on no other answer, so it belongs in this first round.
6. Year plan: record one now (the year's teaching sequences per grade and term, with the Thai indicators each claims), kept outside this course? Recommend "not now, you can add it any time" unless the teacher mentioned a year plan; then recommend yes.

Every question carries a recommendation; never write "no recommendation". When nothing points either way, recommend the common case (e.g. a main lesson block) and say how to switch.

Below the Round 1 questions, list the values already pre-filled so the teacher sees them early and only corrects what differs: the grade mode, once the grade is known (G9 What, G10 How, G11 Why, G12 Who), and the schedule default for each kind (main lesson block: 100-minute sessions, Monday to Friday, 3 weeks; subject lesson: one long 100-minute and one short 50-minute session a week).

**Round 2 — rhythm and learners** (depends on Round 1)

7. Grade mode: confirm the one that follows from the grade.
8. Schedule. Main lesson block: recommend 100-minute sessions, Monday to Friday, 3 weeks. Subject lesson: recommend one long (100 min) and one short (50 min) session a week for the term, and ask which days.
9. Class size.
10. Learner variability, as counts: learning differences, the language of instruction as an additional language, extension, other access needs. Say up front that you only need numbers, not names.
   - When the count of learning differences is above zero, offer codes: "Give each of these students a code (นักเรียน ก, ข…) with their need, so a brief for a supporting teacher can say who gets which support? Recommended: yes if a supporting teacher works with them, otherwise not now." On yes, ask for one short need per student, in plain words.
11. Supporting teacher (ครูประกบ): is one in the room for this class, when (the whole session or part of it, e.g. 13:00–15:00), and what do they do? Is there a pre-teaching slot (day, time, purpose)? Recommend "none" unless the teacher mentioned one.

**Round 3 — year plan** (only if the teacher wants one; it depends only on question 6, so ask it alongside Round 2; follow `year-plan.md`)

12. Where to keep it. Recommend the folder that holds this course, as `../year-plan-<ปีการศึกษา>.md`; if a year plan is already there, say you will add to it.
13. Teaching sequences per grade and term. Recommend this course's teaching sequence as the first row (its grade, its kind, the current term) and ask for the rest.
14. Indicators each sequence claims, as Thai codes (`ว 2.3 ม.3/1`). Recommend, for each sequence, the codes from `${CLAUDE_PLUGIN_ROOT}/references/thai-science-core-indicators-2560.md` whose content matches its subject for that ม. grade, marked as suggestions; or "none yet, to come from mapping-curriculum".

**Final check.** Show a short summary of the profile and layout and ask "Shall I write this? Recommended: yes." Skip it when the teacher has already confirmed.

## Writing

1. Record the confirmed layout in the README's "Plugin layout" section (course-layout Step 4). Keep the rest of the README exactly as it was.
2. Write the class profile at the class profile location, in the contract's file format, with today's date as `Last updated`.
3. **Default course template confirmed** (empty folder): create every area folder of the template, as course-layout "No recognisable structure" says. Otherwise create nothing beyond what this run writes; other mapped folders are created when something is first written there.
4. **Plan templates:** copy the plugin's four templates into the mapped templates location, following course-layout "Plan templates" (read each from `${CLAUDE_PLUGIN_ROOT}/references/` and write it unchanged under the same filename): `thai-core-plan-template.th.md`, `waldorf-plan-template-block.th.md`, `waldorf-plan-template-week.th.md`, `waldorf-plan-template-day.th.md`. Never overwrite a file, and skip any plan kind the course already has its own form for. No templates area in a found layout: copy nothing and offer.
5. **Year plan** (if wanted): write or extend it at the confirmed path in the `year-plan.md` format, then put its path in the profile's Year plan section. Otherwise the section says `- None recorded.`
6. Reply in a few lines: what was recorded, where it lives in teacher terms, any defaults you assumed, which plan templates were copied and any of the teacher's own forms that will be used instead, the note about names if it applies, and the next step (usually `mapping-curriculum`, then planning the teaching sequence).

## Updating a profile

1. Read the existing profile. Show its current values as the recommended answers and ask only about what the teacher wants to change (one round; skip it if the teacher already said what changes and confirmed).
2. Edit the same file in place: change the affected lines, keep every other value, update `Last updated`. Never create a second profile; if two profiles exist already, ask which one to keep before writing.
3. Recompute anything that depends on a changed value (grade mode follows grade; the additional-language row follows the language of instruction).
4. If no layout is recorded yet, propose one (course-layout Steps 2–4) with the existing profile's location as the class profile row.
5. Year plan or templates asked for: run Round 3 (ask only what the teacher has not said) and write as in [Writing](#writing) steps 4–5; set the profile's Year plan line to the path.
6. Reply with what changed, in a sentence or two.

## Checklist before replying

- [ ] One class only; one profile file, at the mapped location.
- [ ] No names or identifying details in any file written or in the reply; no private folder opened.
- [ ] Student codes, if any, in Thai alphabet order, one per learning-differences count, each with a need and nothing that identifies the student.
- [ ] Grade, grade mode, kind, schedule, counts, both languages, CE and ปีการศึกษา all present.
- [ ] README's other content unchanged; exactly one "Plugin layout" section.
- [ ] Nothing renamed, moved or deleted; the folder name never used.
- [ ] Default template folders created only after the teacher confirmed it.
- [ ] Plan templates copied unchanged; none of the teacher's own templates overwritten.
- [ ] Year plan, if any, outside the course, indicator codes exactly as given, and its path in the profile; nothing else written outside the course.
