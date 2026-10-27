# Waldorf Daily Main-Lesson Plan Template (แผนรายวัน)

> **Source:** `sources/waldorf-plan-template-day.th.docx` (school form, bilingual EN/TH labels). Labels below are verbatim. Thai labels for Differentiation, Homework and Review are missing in the original; the agent-facing equivalents here are added in brackets.
>
> **What this is:** Bottom level of the Waldorf planning chain: one main-lesson day, timed segment by segment. Its parent is a day row of `waldorf-plan-template-week.th.md`.
>
> **Agent use:**
> - Keep the bilingual labels. Write cell content in Thai unless the teacher asks for English.
> - **Weekly Objectives** and **Key Skills** copy the parent weekly plan. Each segment's **Objective** must serve one of them.
> - **Time:** clock times or minutes per segment. The total is ~90–100 min (Rawson P7).
> - **Aspect of ML** rows are the form's default sequence. Meaning, from `rawson2021-generative-principles-upper-school.md` §2.4–2.5:
>   - **Rhythmic Time:** attunement (verse, movement, recitation, mental arithmetic).
>   - **Maths/Literacy:** a short skills strand. For upper-school science, use it for quantitative or scientific-writing practice tied to the block. Mark it `—` if unused.
>   - **Recall:** open-question reconstruction of *yesterday's* experience (not a quiz). It flows into concept formation for the experience before that.
>   - **Practice:** application of earlier concepts and individual or group work, differentiated at three levels.
>   - **New Content:** today's new experience. Leave it **un-analysed** until tomorrow's recall.
> - Rows may be reordered or repeated when the lesson design needs it (e.g. New Content before Practice). Keep the row labels.
> - **Homework** and **Review** are single cells covering the whole day. Write **Review** only from teacher-supplied reflections.
> - **To do:** follow-ups (materials to prepare, students to check in with, items to carry to the next day).
>
> **Related files:** `waldorf-plan-template-week.th.md` · `waldorf-plan-template-block.th.md` · `thai-core-plan-template.th.md` (Section 7 mapping of this rhythm).

---

## Template

```markdown
| Date: วันที่ | Block: วิชา | Weekly Objectives: เป้าหมายการสอนหรือกิจกรรมของสัปดาห์ | Key Skills: ทักษะสำคัญที่อยากให้เด็กได้ |
|---|---|---|---|
| {{date}} | {{block_title}} — สัปดาห์ที่ {{week_no}} วันที่ {{day_no}} | 1. {{weekly_objective}} | 1. {{key_skill}} |

**Notes:** {{notes}}

| Time: | Aspect of ML: ช่วงต่างๆ ของวิชาหลัก | Activity: กิจกรรม/ทำอะไรบ้าง | Objective: จุดประสงค์ | Differentiation: [แผนสำหรับเด็กที่มีข้อจำกัด] | Assessment: การประเมิน | Preparation: การเตรียม |
|---|---|---|---|---|---|---|
| {{time}} | Rhythmic Time: กิจกรรมวงกลม | {{activity}} | {{objective}} | {{differentiation}} | {{assessment}} | {{preparation}} |
| {{time}} | Maths/Literacy | {{activity}} | {{objective}} | {{differentiation}} | {{assessment}} | {{preparation}} |
| {{time}} | Recall: การทบทวนสิ่งที่เรียนไป | {{activity}} | {{objective}} | {{differentiation}} | {{assessment}} | {{preparation}} |
| {{time}} | Practice: ช่วงทำงาน | {{activity}} | {{objective}} | {{differentiation}} | {{assessment}} | {{preparation}} |
| {{time}} | New Content: เรื่องใหม่ | {{activity}} | {{objective}} | {{differentiation}} | {{assessment}} | {{preparation}} |

**Homework: [การบ้าน]** {{homework}}

**Review: [ทบทวนหลังสอน]** {{review}}

**To do:** {{todo}}
```

Use `<br>` for line breaks inside a cell. In the original form, Homework and Review are columns merged down all segment rows. Here they are lifted out as day-level fields with the same meaning.
