# Standards map template

The default layout of a course standards map. A course-local template overrides it. Fill every `<…>`; keep section order. Write in Thai by default (it is shared with supervisors), English when the teacher asks; Thai official terms verbatim either way.

```markdown
# Standards map: <teaching sequence, e.g. Meteorology main lesson block>

- **Class:** <grade> (ม.<n> / G<n>) · <main lesson block | subject lesson> · <academic year CE / ปีการศึกษา BE, if known>
- **Source:** curriculum crosswalk (plugin references) · updated <date>
- **Status:** <confirmed | includes proposed indicators awaiting the teacher's confirmation>

## Thai indicators claimed

| Code | ตัวชี้วัด (verbatim) | Where in the teaching sequence | Status |
|---|---|---|---|
| `ว x.x ม.n/k` | <Thai wording copied exactly> | <unit or week, if known> | claimed / proposed |

## Indicator verbs (official glossary)

| Verb | ความหมาย (glossary, verbatim) | What it asks of students |
|---|---|---|
| <Thai verb> | <official meaning> | <one plain-language line> |

## Waldorf grade mode

- **G<n> *<What? | How? | Why? | Who?>*:** <question and capacity, as worded in the crosswalk>
- **Grade-mode notes:** <crosswalk notes for the claimed indicators, e.g. "สร้างแบบจำลอง → G11, above G9"; or "none">

## PISA-adapted competencies (candidate links)

| Headline | Linked indicators (crosswalk link rules) |
|---|---|
| S1 Explain phenomena scientifically | `ว …` / Gap |

Links are candidates from the crosswalk's rules, not alignment claims. Sub-abilities for this grade: <codes and titles from the crosswalk grade section, only those the teacher selects>.

## Gaps and differences

- **Gaps:** <claimed indicators with no PISA-adapted link; headlines the sequence does not reach; standards the sequence does not touch at this grade, if the teacher asked>
- **Sequencing differences:** <indicator from another ม. grade: code and wording verbatim, one line of grade-mode reason; or "none">
- **Not found:** <codes the teacher gave that are not in the indicators file; or "none">
```

## Notes

- One table row per indicator; never merge two indicators into one row.
- If the course already has a standards map, keep its rows and add, mark or remove only what changed.
- Leave the PISA-adapted sub-abilities empty rather than choosing them for the teacher, unless the request asks for a selection.
