# Year coverage: reading a year plan and the report template

Year-level coverage across every teaching sequence in the teacher's year plan. A course-local year coverage template overrides the report layout below. Write in Thai by default (it is shared with supervisors), English when the teacher asks; Thai official terms verbatim either way.

## Reading the year plan

The year plan follows the plugin's year plan format (one section per grade, one subsection per term, a table of teaching sequences with the indicators each claims). A teacher may have edited it by hand: read tables, lists or prose as written, and never rewrite the file.

- **Per teaching sequence, take:** grade (G9–G12, with ม.3–ม.6), term, the sequence's name, its kind (main lesson block or subject lesson, if given) and each indicator it claims.
- **Codes.** Normalise spacing only (`ว3.2 ม.6/8` → `ว 3.2 ม.6/8`). Expand a range within one standard and grade (`ว 3.2 ม.6/7–ม.6/12`, `` `ว 3.2 ม.6/7`–`ม.6/12` ``, `ว 3.2 ม.6/7-12`) into each code. `none yet` claims nothing. A range across standards or grades, or a code you cannot read, is listed under "Could not read" and asked about; never guess.
- **Wording.** Take every indicator's Thai wording from the crosswalk, never from the year plan. An English gloss or paraphrase in the year plan stays a gloss.
- **Not found.** A code that is not in the indicators file goes under "Not found" and counts toward nothing.
- **Gaps in the plan.** A sequence without a grade or term is listed with "grade not given" / "term not given"; ask about it in the reply rather than assigning one.

## Working it out

1. **Grades in scope** are the grades the year plan lists. Each one's indicator list is its ม. grade section in the crosswalk.
2. **Covered:** every indicator claimed by at least one sequence, listed by the grade and term of the sequence that claims it.
3. **Missing:** for each grade in scope, the indicators of that ม. grade no sequence in the year claims. An indicator claimed in another grade (a sequencing difference) counts as covered there; say where. List ว 4.1 and ว 4.2 (technology and computing) as their own group, noting that schools often teach them in a technology subject.
4. **Duplicated:** an indicator claimed by two or more sequences, in any grade or term. Name every sequence. A duplicate is a fact to show, not an error: the teacher may revisit an indicator on purpose.
5. **Sequencing differences:** an indicator whose ม. grade differs from the grade of the class that teaches it. For each, write a justification line from the crosswalk's grade bands (§1): the class's grade mode (question, capacity or motif) and why the indicator fits it, against the indicator's own grade and mode. If the year plan already gives a reason, keep the teacher's reason and add the grade modes. Mark drafted lines "draft: confirm or edit".

## Report template

```markdown
# Year coverage: <school year CE> / ปีการศึกษา <BE>

- **Year plan:** <the teacher's name for it, not a file path> · read <date>
- **Grades in scope:** <e.g. G9 (ม.3), G10 (ม.4)>
- **Source:** curriculum crosswalk (plugin references)

## Covered, by grade and term

### G<n> (ม.<n>) · <grade mode>

| Term | Teaching sequence | Kind | Code | ตัวชี้วัด (verbatim) | Note |
|---|---|---|---|---|---|
| <term> | <name> | <main lesson block / subject lesson> | `ว x.x ม.n/k` | <Thai wording copied exactly> | <sequencing difference / duplicated / —> |

## Missing, by grade

### ม.<n> (G<n>): <count> of <total> core indicators not claimed

| Code | ตัวชี้วัด (verbatim) |
|---|---|

Technology and computing (ว 4.1, ว 4.2), often taught in a technology subject: <codes, or "none missing">

## Duplicated

| Code | ตัวชี้วัด (verbatim) | Claimed by (grade · term · teaching sequence) |
|---|---|---|

## Sequencing differences

For Thai core plans: cite the code and wording as below, then the justification.

### `ว x.x ม.n/k`: taught in ม.<m> (G<m>), belongs to ม.<n> (G<n>)

- **ตัวชี้วัด (verbatim):** <Thai wording copied exactly>
- **Taught in:** <teaching sequence> · <term>
- **Grade-mode justification:** <one line: G<m> <mode> … ; the indicator sits at ม.<n> / G<n> <mode> …> (<draft: confirm or edit | the teacher's reason>)

## Not found and could not read

- **Not found:** <codes in the year plan that are not in the indicators file; or "none">
- **Could not read:** <entries and what is unclear; or "none">
```

## Notes

- One row per indicator per sequence; never merge indicators into one row.
- If a year coverage report for the same school year already exists, update it in place.
- No student names or other personal details, even if the year plan holds any.
