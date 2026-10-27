# Year plan: contract and file format

The year plan lists one school year's teaching sequences per grade and term, with the Thai indicators each one claims. It is the basis for year-level coverage (covered, missing and duplicated indicators). `setting-up-class-profiles` writes it; year-level coverage reads it. It is the one file that lives outside any course folder (ADR-0002): one year plan serves every course of that year, and each class profile's "Year plan" section gives its path.

## Where it lives

- At a path the teacher chooses, outside the course folder. Recommend the folder that holds the course, named after the ปีการศึกษา: `../year-plan-2569.md`.
- Record the path in the class profile's "Year plan" section exactly as the teacher gave it (relative to the course folder, or absolute).
- If a year plan already exists at that path, it belongs to other courses too: read it, add or change only the rows the teacher gives, keep every other line, and update `Last updated`. Never write a second year plan for the same year.
- Never read or write any other file outside the course folder.

## Fields

| Field | Values |
|---|---|
| Academic year | CE years and ปีการศึกษา, worked out as in `class-profile.md` |
| Grade | G9–G12 with the ม. grade; one section per grade the teacher plans |
| Term | Term 1 (ภาคเรียนที่ 1) or Term 2 (ภาคเรียนที่ 2); one subsection per term with sequences |
| Teaching sequence | its own subject (a main lesson block is named by its subject, e.g. meteorology), never a folder name |
| Kind | main lesson block or subject lesson |
| Indicators claimed | Thai indicator codes in the official format `ว <มาตรฐาน> <ชั้น>/<ข้อ>`, each in backticks, comma-separated; or `none yet` |
| Notes | optional, e.g. weeks, or why an indicator from another ม. grade is claimed |

**Indicators.** Copy codes exactly as the teacher gives them, in the official format (`ว 2.3 ม.3/1`). Check each code exists in `thai-science-core-indicators-2560.md` (ม.4–6 electives: `thai-science-supplementary-learning-outcomes-2560.md`); ask about any code that does not, and never invent or renumber one. An indicator from a different ม. grade than the one taught is allowed (a sequencing difference): keep the code as written and note it.

## File format

Markdown. Keep these headings and the table columns so year-level coverage can read the file.

```markdown
# Year plan

Recorded by setting-up-class-profiles. Teaching sequences per grade and term, with the Thai indicators each claims.

Last updated: 2026-10-27

## Academic year

- CE: 2026–2027
- ปีการศึกษา: 2569

## G9 (ม.3)

### Term 1 (ภาคเรียนที่ 1)

| Teaching sequence | Kind | Indicators claimed | Notes |
|---|---|---|---|
| Science Practice | subject lesson | `ว 2.3 ม.3/1`, `ว 2.3 ม.3/2` | |

### Term 2 (ภาคเรียนที่ 2)

| Teaching sequence | Kind | Indicators claimed | Notes |
|---|---|---|---|
| astronomy | main lesson block | `ว 3.1 ม.3/1` | 3 weeks |

## G10 (ม.4)

### Term 1 (ภาคเรียนที่ 1)

| Teaching sequence | Kind | Indicators claimed | Notes |
|---|---|---|---|
| meteorology | main lesson block | none yet | indicators to come from mapping-curriculum |
```

Omit a term with no teaching sequences; omit a grade the teacher does not plan. No student names or details ever appear here.
