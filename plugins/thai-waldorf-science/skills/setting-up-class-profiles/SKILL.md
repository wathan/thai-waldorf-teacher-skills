---
name: setting-up-class-profiles
description: >
  Sets up or updates the class profile for one class of a Thai Waldorf
  upper-school science teacher (G9–G12 / ม.3–ม.6) through a round-by-round
  interview with recommended answers: grade and grade mode, main lesson block
  or subject lesson, schedule, learner variability as anonymised counts,
  languages, and the academic year in CE and ปีการศึกษา. Detects the course
  folder's existing layout, proposes where plugin files go and records the
  confirmed mapping in the course README. Use when the teacher wants to
  describe a class, set up or change a class profile, start a new course
  folder, or tell the plugin where things live. Do not use to plan lessons.
license: CC-BY-SA-4.0
---

# Setting up class profiles

You interview the teacher about one class, find out how their course folder is laid out, and write the class profile where that layout says. You never plan lessons here.

## Keeping the teacher posted

Talk as a colleague in plain teacher language: say "your admin folder" or "the course notes", not file paths, tool names or plugin jargon. Use the glossary terms exactly: class profile, main lesson block, subject lesson, teaching sequence, grade mode, learner variability.

## Privacy first (applies to everything below)

- Never write a student's name, nickname, initials, student number or any detail that singles out one student into the profile, the README or any other file, and never repeat one in a reply.
- When the teacher gives names (in the request or in files you see), turn them into counts per need, and tell the teacher once, briefly: names were left out and only counts were recorded.
- If the teacher asks you to record names or a class list, decline and offer counts instead.
- Leave the teacher's own files that contain names untouched; just do not copy from them.

## Step 0 — Route (silent)

1. Read the shared layout procedure `${CLAUDE_PLUGIN_ROOT}/references/course-layout.md` and the profile contract `${CLAUDE_PLUGIN_ROOT}/references/class-profile.md` NOW. Follow both.
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
5. Where things go: the layout proposal from course-layout Step 3, including where the class profile goes. Recommend the proposal. It depends on no other answer, so it belongs in this first round.

Every question carries a recommendation; never write "no recommendation". When nothing points either way, recommend the common case (e.g. a main lesson block) and say how to switch.

Below the Round 1 questions, list the values already pre-filled so the teacher sees them early and only corrects what differs: the grade mode, once the grade is known (G9 What, G10 How, G11 Why, G12 Who), and the schedule default for each kind (main lesson block: 100-minute sessions, Monday to Friday, 3 weeks; subject lesson: one long 100-minute and one short 50-minute session a week).

**Round 2 — rhythm and learners** (depends on Round 1)

6. Grade mode: confirm the one that follows from the grade.
7. Schedule. Main lesson block: recommend 100-minute sessions, Monday to Friday, 3 weeks. Subject lesson: recommend one long (100 min) and one short (50 min) session a week for the term, and ask which days.
8. Class size.
9. Learner variability, as counts: learning differences, the language of instruction as an additional language, extension, other access needs. Say up front that you only need numbers, not names.

**Final check.** Show a short summary of the profile and layout and ask "Shall I write this? Recommended: yes." Skip it when the teacher has already confirmed.

## Writing

1. Record the confirmed layout in the README's "Plugin layout" section (course-layout Step 4). Keep the rest of the README exactly as it was.
2. Write the class profile at the class profile location, in the contract's file format, with today's date as `Last updated`.
3. In an empty folder, create only the README and the class profile in the admin area; other mapped folders are created when something is first written there.
4. Reply in a few lines: what was recorded, where it lives in teacher terms, any defaults you assumed, the note about names if it applies, and the next step (usually `mapping-curriculum`, then planning the teaching sequence).

## Updating a profile

1. Read the existing profile. Show its current values as the recommended answers and ask only about what the teacher wants to change (one round; skip it if the teacher already said what changes and confirmed).
2. Edit the same file in place: change the affected lines, keep every other value, update `Last updated`. Never create a second profile; if two profiles exist already, ask which one to keep before writing.
3. Recompute anything that depends on a changed value (grade mode follows grade; the additional-language row follows the language of instruction).
4. If no layout is recorded yet, propose one (course-layout Steps 2–4) with the existing profile's location as the class profile row.
5. Reply with what changed, in a sentence or two.

## Checklist before replying

- [ ] One class only; one profile file, at the mapped location.
- [ ] No names or identifying details in any file written or in the reply.
- [ ] Grade, grade mode, kind, schedule, counts, both languages, CE and ปีการศึกษา all present.
- [ ] README's other content unchanged; exactly one "Plugin layout" section.
- [ ] Nothing renamed, moved or deleted; the folder name never used.
