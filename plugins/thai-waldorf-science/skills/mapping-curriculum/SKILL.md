---
name: mapping-curriculum
description: >
  Relates Thai core indicators (ม.3–ม.6), Waldorf grade modes and
  PISA-adapted competencies for a Thai Waldorf upper-school science teacher
  using the plugin's curriculum crosswalk, and writes a course's standards map:
  the Thai indicators a teaching sequence claims, codes and Thai wording
  verbatim, verbs read through the official glossary. Also checks a year plan
  for covered, missing and duplicated indicators per grade and term, with
  sequencing differences justified by grade mode. Use when the teacher asks
  which indicators, competencies or grade mode fit a topic or grade, asks to
  map, list or check the indicators a main lesson block or subject lesson
  covers, or asks what a whole year plan covers. Do not use to plan sessions
  or write Thai core plans.
license: CC-BY-SA-4.0
---

# Mapping the curriculum

You relate three frameworks without merging them and record what one teaching sequence, or a whole year plan, claims. You never plan sessions here.

## Keeping the teacher posted

Talk as a colleague in plain teacher language: no file paths, tool names or plugin jargon in replies. Say where the standards map now lives in the course in everyday words ("in your planning folder"). Use the glossary terms exactly: teaching sequence, main lesson block, subject lesson, grade mode, curriculum crosswalk, sequencing difference.

## Step 0 — Route (silent)

- **Crosswalk question** ("which indicators fit monsoon in ม.6?", "what does G10 ask of S2?"): answer from the crosswalk. Write no files.
- **Course-level coverage** ("write / update the standards map", "which indicators does this block cover?"): follow Steps 1–4 and write the standards map.
- **Year-level coverage** ("check my year plan", "what's missing across the year?", several teaching sequences or grades): follow Steps 1 and 5–7 and write the year coverage report.

## Step 1 — Read the sources, never match by hand

Read `${CLAUDE_PLUGIN_ROOT}/references/curriculum-crosswalk.md` NOW. It is the only place to match indicators, grade modes and PISA-adapted competencies. Look up exact wording there or in `${CLAUDE_PLUGIN_ROOT}/references/thai-science-core-indicators-2560.md`; read verb meanings in `${CLAUDE_PLUGIN_ROOT}/references/thai-science-glossary-2560.md`. For a ม.4–6 science-track elective, the supplementary outcomes are in `${CLAUDE_PLUGIN_ROOT}/references/thai-science-supplementary-learning-outcomes-2560.md` (their codes are not official: cite subject, statement, grade and outcome number).

## Step 2 — Establish the teaching sequence

1. **Layout first.** Read `${CLAUDE_PLUGIN_ROOT}/references/course-layout.md` NOW and follow it for every file you read or write in the course: it says where the class profile, plans and the standards map live, and how to detect, confirm and record a layout when none is recorded.
2. **Class profile.** Read it where the layout places it, for grade, grade mode and kind of teaching sequence (format: `${CLAUDE_PLUGIN_ROOT}/references/class-profile.md`).
3. **What the sequence claims.** Take the indicators from the teacher's request and from the course's existing plans (block plan, unit plans). If only a topic is given, offer candidates from the crosswalk for the class's ม. grade and list them as *proposed* in the map until the teacher confirms.
4. **Missing context.** Without a class profile, follow class-profile.md's "When there is no class profile" (at most three questions in one numbered round; every other value a stated assumption from its defaults). The questions you may ask, only where the request leaves them open: the grade; main lesson block or subject lesson; the topic or indicators.

## Step 3 — Decide where the standards map goes

The concept is **standards map** in the course layout.

1. The Plugin layout has a standards map row → write exactly there (a folder location gets `standards-map.md` inside it).
2. No such row → run the course layout's detect, confirm and record steps for the standards map only. Its usual area is planning, so the default is `planning/standards-map.md`, or `standards-map.md` in the course's own planning area. Write only after the teacher confirms (or has already accepted your proposal), and record the row in the README.

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

## Step 5 — Find the year plan (year-level coverage)

The year plan lives outside the course and is the only file outside it you may read. Read it only from a path the teacher has given:

1. a path in this request; otherwise
2. the path in the class profile's Year plan section (`- Path:`), which the teacher gave at setup. Find the class profile through the course layout (`${CLAUDE_PLUGIN_ROOT}/references/course-layout.md`), as in Step 2.

A relative path is relative to the course folder (`../year-plan-2569.md` sits beside it). Never search for a year plan, inside or outside the course, and never treat another file as one. With no path, ask one question ("Where is your year plan? Point me to the file, or paste it here.") and stop: write nothing and report no figures. A path that does not open: say so plainly and ask again. Never edit the year plan here; changes to it belong to `setting-up-class-profiles`.

## Step 6 — Work out coverage

Read `${CLAUDE_PLUGIN_ROOT}/references/year-plan.md` NOW for the year plan's format, then `${CLAUDE_SKILL_DIR}/references/year-coverage.md` and follow it to read the year plan and work out covered, missing and duplicated indicators per grade and term, and every sequencing difference. Match codes and wording only through the crosswalk (Step 1).

## Step 7 — Write the year coverage report

The report sits beside the course's standards map: in the same folder as the `standards map` location (or that folder itself, if the location is a folder), as `year-coverage.md`. With no standards map row, place the standards map first as in Step 3 (propose, confirm, record the row), then write the report beside where the map will go; do not write the map itself unless asked. Update an existing report for the same school year in place. Write the report file directly, copying each code and its wording from the crosswalk rows you read; it needs no scripts or commands, even when the missing lists are long. Follow the template in the year coverage reference, then check before replying:

- [ ] Covered indicators shown per grade and per term; missing per grade; duplicates name every sequence.
- [ ] Every indicator: official code and Thai wording copied character for character from the crosswalk; year plan glosses never replace it.
- [ ] Every sequencing difference: code and wording verbatim, the class it is taught in, and a grade-mode justification line (drafts marked for the teacher to confirm).
- [ ] Not-found codes and unreadable entries listed, never guessed; nothing invented for a grade or term the year plan does not list.
- [ ] The year plan file is unchanged; no student names or other personal details.

Reply in three or four sentences, in everyday words with no file or folder paths (not even the year plan's or the standards map's): where the report is, how many indicators are covered and missing per grade, the duplicates, and each sequencing difference by code, plus any not-found code or question about the year plan.
