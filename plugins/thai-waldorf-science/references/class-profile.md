# Class profile: contract and file format

The class profile describes one class for one teaching sequence. `setting-up-class-profiles` writes it; every other skill reads it from the location the course README's "Plugin layout" section gives for the concept `class profile` (see `course-layout.md`). Each course keeps its own copy.

## Fields

| Field | Values | Default |
|---|---|---|
| Grade | G9–G12, with the Thai grade: G9 = ม.3, G10 = ม.4, G11 = ม.5, G12 = ม.6 | none: always ask |
| Grade mode | G9 What, G10 How, G11 Why, G12 Who (from the macro curriculum) | from grade |
| Class size | a number | ask; may be left blank |
| Kind of teaching sequence | main lesson block, or subject lesson (one per course folder) | none: always ask |
| Name | the teaching sequence's own subject (a main lesson block is named by its subject, e.g. meteorology) | ask; never taken from the folder name |
| Schedule | main lesson block: session length, days per week, number of weeks; subject lesson: sessions per week, each session's length and day, length of the sequence | main lesson block: 100 minutes, Monday–Friday, 3 weeks (2–4); subject lesson: one long (100 min) and one short (50 min) session a week, for one term |
| Learner variability | anonymised counts per need (see below) | ask |
| Language of instruction | e.g. Thai, English | Thai |
| Language of student materials | e.g. Thai, English, bilingual | same as instruction |
| Academic year | CE years and the Buddhist-era ปีการศึกษา; optionally the term (ภาคเรียน) | the academic year in progress (below) |
| Year plan | the path to the teacher's year plan, which lives outside the course (format: `year-plan.md` in this folder), or none | none |

**Academic year.** A Thai academic year starts in May. The ปีการศึกษา is the CE year in which it starts plus 543. From May 2026 to April 2027 the academic year is 2026–2027 = ปีการศึกษา 2569. Work it out from today's date; never hard-code it.

**Learner variability.** Counts only, by need: learning differences (e.g. dyslexia, attention), the language of instruction as an additional language, extension, other access needs (physical, sensory, health), each with an optional short note about the kind of need. Never names, nicknames, initials, student numbers, photos, or details that single out one student (e.g. "the boy from Myanmar who arrived in June").

## File format

Markdown, written in English with Thai grade and year terms verbatim. Keep these headings and labels so other skills can read the file; values in plain words.

```markdown
# Class profile

Recorded by setting-up-class-profiles. Anonymised: no student names or identifying details.

Last updated: 2026-10-27

## Class

- Grade: G10 (ม.4)
- Grade mode: How
- Class size: 24

## Teaching sequence

- Kind: main lesson block
- Name: meteorology

## Schedule

- Session length: 100 minutes
- Weekly pattern: every day, Monday to Friday
- Length of the sequence: 3 weeks

## Learner variability (anonymised counts)

| Need | Count | Notes |
|---|---|---|
| Learning differences | 2 | reading-related |
| Thai as an additional language | 1 | |
| Extension | 0 | |
| Other access needs | 0 | |

## Language

- Language of instruction: Thai
- Language of student materials: Thai

## Academic year

- CE: 2026–2027
- ปีการศึกษา: 2569

## Year plan

- None recorded.
```

With a year plan, the Year plan section reads `- Path:` followed by the path in backticks as the teacher gave it (e.g. `../year-plan-2569.md`), instead of `- None recorded.`

For a subject lesson, the Schedule section lists `Sessions per week`, `Session lengths` (each one) and `Weekly pattern` (which day each falls on), then `Length of the sequence`. Name the additional-language row after the actual language of instruction (e.g. "English as an additional language").

## When there is no class profile

Every skill that reads the class profile follows this rule when there is none; the skill names which values it may ask about.

1. **At most three questions, in one numbered round**, each with a recommended answer, and only for what the request (and any plan the skill reads) leaves open. The usual ones: the grade, the kind of teaching sequence, the session length and count. Never ask what the request already answers; with enough in the request, ask nothing. When the teacher says to go ahead with defaults, ask nothing that has a default.
2. **State every other value as an assumption**, using the defaults in the table above: in particular Thai for both the language of instruction and the language of student materials, and the academic year in progress worked out from today's date.
3. **End that same reply**, whether it asks or proceeds, with one line suggesting `setting-up-class-profiles` for next time (e.g. "Setting up a class profile for this class with `setting-up-class-profiles` saves these questions next time.").
