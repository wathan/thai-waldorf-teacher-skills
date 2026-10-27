---
name: mapping-curriculum
description: >
  Relates Thai core indicators (ม.3–ม.6), Waldorf grade modes and
  PISA-adapted competencies for a Thai Waldorf upper-school science teacher
  using the plugin's curriculum crosswalk, and writes a course's standards map:
  the Thai indicators a teaching sequence claims, codes and Thai wording
  verbatim, verbs read through the official glossary. Use when the teacher asks
  which indicators, competencies or grade mode fit a topic or grade, or asks to
  map, list or check the indicators a main lesson block or subject lesson
  covers. Do not use to plan sessions or write Thai core plans.
license: CC-BY-SA-4.0
---

# Mapping the curriculum

You relate three frameworks without merging them and record what one teaching sequence claims. You never plan sessions here.

## Keeping the teacher posted

Talk as a colleague in plain teacher language: no file paths, tool names or plugin jargon in replies. Say where the standards map now lives in the course in everyday words ("in your planning folder"). Use the glossary terms exactly: teaching sequence, main lesson block, subject lesson, grade mode, curriculum crosswalk, sequencing difference.

## Step 0 — Route (silent)

- **Crosswalk question** ("which indicators fit monsoon in ม.6?", "what does G10 ask of S2?"): answer from the crosswalk. Write no files.
- **Course-level coverage** ("write / update the standards map", "which indicators does this block cover?"): follow Steps 1–4 and write the standards map.
- **Year-level coverage** (a year plan across several teaching sequences): not available in this version. Say so in one sentence and offer the course-level standards map instead.

## Step 1 — Read the sources, never match by hand

Read `${CLAUDE_PLUGIN_ROOT}/references/curriculum-crosswalk.md` NOW. It is the only place to match indicators, grade modes and PISA-adapted competencies. Look up exact wording there or in `${CLAUDE_PLUGIN_ROOT}/references/thai-science-core-indicators-2560.md`; read verb meanings in `${CLAUDE_PLUGIN_ROOT}/references/thai-science-glossary-2560.md`. For a ม.4–6 science-track elective, the supplementary outcomes are in `${CLAUDE_PLUGIN_ROOT}/references/thai-science-supplementary-learning-outcomes-2560.md` (their codes are not official: cite subject, statement, grade and outcome number).

## Step 2 — Establish the teaching sequence

1. **Layout first.** If the course README has a "Plugin layout" section, read it: it says where the class profile, plans and standards map live. Never read meaning into, or change, the course folder's own name.
2. **Class profile.** Read it where the layout places it (or an obvious class profile file) for grade, grade mode and kind of teaching sequence.
3. **What the sequence claims.** Take the indicators from the teacher's request and from the course's existing plans (block plan, unit plans). If only a topic is given, offer candidates from the crosswalk for the class's ม. grade and list them as *proposed* in the map until the teacher confirms.
4. **Missing context.** Without a class profile and without the grade in the request, ask at most three questions (grade; main lesson block or subject lesson; the topic or indicators) and state everything else as an assumption.

## Step 3 — Decide where the standards map goes

1. The Plugin layout names a location for the course standards map → write exactly there, creating folders as needed.
2. No mapping, but the course follows the default course template (admin, planning, design, resources, delivery, assessment, evaluation, templates areas) or is empty → write `planning/standards-map.md`.
3. A different structure with no mapping → propose a fitting location in one sentence, write there, and tell the teacher that `setting-up-class-profiles` can record the course layout.

Never create a second standards map: update the existing one in place.

## Step 4 — Write the standards map

If the course's templates area has a standards map template, follow it. Otherwise read `${CLAUDE_SKILL_DIR}/references/standards-map.md` NOW and follow it. Then check every rule below before replying:

- [ ] Every indicator: official code (`ว x.x ม.n/k`) and Thai wording copied character for character from the crosswalk. A teacher's English gloss or paraphrase never replaces it; an English gloss, if useful, sits in a separate column marked as a gloss.
- [ ] A code not in the indicators file is reported as not found and left out of the claimed list; never guess its wording or a nearby code.
- [ ] Each indicator verb is read through the glossary: Thai verb, official meaning (ความหมาย) quoted verbatim, and what it therefore asks of students.
- [ ] Waldorf grade mode, PISA-adapted competencies and Thai indicators sit in their own sections in their own wording. No merged statements, no KUD (know/understand/do) charts, no developmental-band translation; the Thai ม. grade is the band.
- [ ] Gaps are explicit: a claimed indicator with no PISA-adapted link, a PISA-adapted headline the sequence does not reach, a crosswalk grade-mode note (a verb whose mode sits above the class's grade mode).
- [ ] An indicator from a different ม. grade than the class is marked as a sequencing difference, cited exactly as written, with one line on the grade-mode reason.
- [ ] No student names or other personal details.

Reply in two or three sentences: where the map is, how many indicators it lists, and any gap, not-found code or sequencing difference the teacher should look at.
