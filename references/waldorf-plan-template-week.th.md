# Waldorf Weekly Plan Template (แผนรายสัปดาห์)

> **Source:** `sources/waldorf-plan-template-week.th.docx` (school form, bilingual EN/TH labels). Labels below are verbatim.
>
> **What this is:** Middle level of the Waldorf planning chain: one week of a main-lesson block, planned day by day (Mon–Fri). Its parent is a row of `waldorf-plan-template-block.th.md`; each day row expands into `waldorf-plan-template-day.th.md`.
>
> **Agent use:**
> - Keep the bilingual labels. Write cell content in Thai unless the teacher asks for English.
> - **Weekly Objectives** and **Key Skills** copy or refine the matching week row of the block plan. Name science Key Skills with the official Thai terms in `thai-science-key-skills-2560.md`.
> - Plan the days as overlapping **experience → recall → concept → apply** cycles (Rawson §2.4): a new experience on day *n* is recalled on day *n*+1, conceptualised on *n*+2 and applied on *n*+3. Monday recalls the previous week (or the previous block in this subject on the block's first day).
> - Every daily **Objectives** entry needs an **Assessment** entry in the same row.
> - **Extra Main:** the form leaves this column undefined. Use it for main-lesson-book work, practice lessons or other extensions linked to the block. Leave it empty if there are none.
> - **Review** (last row): written after teaching. Leave it blank unless the teacher supplies reflections. Never invent observations.
>
> **Related files:** `waldorf-plan-template-block.th.md` · `waldorf-plan-template-day.th.md` · `rawson2021-generative-principles-upper-school.md` (rhythm, checklist §5).

---

## Template

```markdown
| Block: ชื่อวิชาที่สอน | Weekly Objectives: เป้าหมายการสอนหรือกิจกรรมของสัปดาห์ | Key Skills: ทักษะสำคัญที่อยากให้เด็กได้ |
|---|---|---|
| {{block_title}} — สัปดาห์ที่ {{week_no}} | 1. {{weekly_objective}} | 1. {{key_skill}} |

**Notes:** {{notes}}

| วัน: | Objectives: วัตถุประสงค์ของวัน | Assessment: การประเมิน | Preparation: การเตรียมตัว | Rhythmic Time: กิจกรรมวงกลม | Main Lesson: เนื้อหาวิชา | Differentiation: แผนสำหรับเด็กที่มีข้อจำกัด | Extra Main |
|---|---|---|---|---|---|---|---|
| Monday | {{objectives}} | {{assessment}} | {{preparation}} | {{rhythmic_time}} | {{main_lesson}} | {{differentiation}} | {{extra_main}} |
| Tuesday | {{objectives}} | {{assessment}} | {{preparation}} | {{rhythmic_time}} | {{main_lesson}} | {{differentiation}} | {{extra_main}} |
| Wednesday | {{objectives}} | {{assessment}} | {{preparation}} | {{rhythmic_time}} | {{main_lesson}} | {{differentiation}} | {{extra_main}} |
| Thursday | {{objectives}} | {{assessment}} | {{preparation}} | {{rhythmic_time}} | {{main_lesson}} | {{differentiation}} | {{extra_main}} |
| Friday | {{objectives}} | {{assessment}} | {{preparation}} | {{rhythmic_time}} | {{main_lesson}} | {{differentiation}} | {{extra_main}} |

**Review:** {{review}}
```

Use `<br>` for line breaks inside a cell. In **Main Lesson**, label each part by its cycle role, e.g. `Recall E2 · Concept E1 · New E3`.
