# Waldorf Block Plan Template (แผนรายบล็อก)

> **Source:** `sources/waldorf-plan-template-block.th.docx` (school form, bilingual EN/TH labels). Labels below are verbatim.
>
> **What this is:** Top level of the Waldorf planning chain: one main-lesson **block** (one subject, ~3–4 weeks, ~90–100 min daily; Rawson P7), planned week by week. It breaks down into `waldorf-plan-template-week.th.md` (one per week), which breaks down into `waldorf-plan-template-day.th.md` (one per day).
>
> **Agent use:**
> - Keep the bilingual labels. Write cell content in Thai unless the teacher asks for English.
> - **Block Aims:** trace to ≥1 domain and ≥1 potentiality in `waldorf-education-goals.md`, phrased in the grade mode from `waldorf-upper-school-macro-curriculum.md`.
> - **Block Objectives and Assessable outcomes:** for science, draw on the grade's Sx.n / Ex.n in `waldorf-pisa-competencies-g9-g12.md`. Add the matching Thai indicator codes (`thai-science-core-indicators-2560.md`) in brackets when a Thai plan (`thai-core-plan-template.th.md`) will be produced. Each outcome states *how* learning is evidenced.
> - **One row per week.** The form has 3 rows. Add a `สัปดาห์ที่ 4` row for a 4-week block.
> - Weekly **Objectives** must add up to the block objectives. Every weekly objective needs a matching **Assessment** entry in the same row.
> - **Rhythmic Time** = attunement or circle activity (movement, recitation, mental work). **Main Lesson** = the week's content arc. Week 1 opens by connecting to the previous block in this subject (Rawson §2.4).
> - **Differentiation:** plan for students with limitations *and* for stretch (Rawson's three levels of application tasks).
> - Before output, run the generation checklist in `rawson2021-generative-principles-upper-school.md` §5.
>
> **Related files:** `waldorf-plan-template-week.th.md` · `waldorf-plan-template-day.th.md` · `thai-core-plan-template.th.md`.

---

## Template

```markdown
| Block: ชื่อวิชาที่สอน | Block Aims: เป้าหมายของวิชานี้ | Block Objectives and Assessable outcomes: วัตถุประสงค์ และผลที่ประเมินได้ (เราประเมินอย่างไรว่าเด็กได้เรียนรู้ ตามที่ตั้งเป้าไว้) |
|---|---|---|
| {{block_title}} ({{grade}}, {{weeks}} สัปดาห์) | 1. {{aim}} | 1. {{objective}} → ประเมินโดย {{evidence}} |

| สัปดาห์: | Objectives: เป้าหมายหรือวัตถุประสงค์ในแต่ละสัปดาห์ต้องการให้เด็กเรียนรู้อะไร | Assessment: การประเมิน | Rhythmic Time: กิจกรรมวงกลม | Main Lesson: เนื้อหาวิชาแต่ละสัปดาห์ | Differentiation: แผนสำหรับเด็กที่มีข้อจำกัด | Preparation: ต้องเตรียมอะไรบ้าง |
|---|---|---|---|---|---|---|
| สัปดาห์ที่ 1 | {{objectives}} | {{assessment}} | {{rhythmic_time}} | {{main_lesson}} | {{differentiation}} | {{preparation}} |
| สัปดาห์ที่ 2 | {{objectives}} | {{assessment}} | {{rhythmic_time}} | {{main_lesson}} | {{differentiation}} | {{preparation}} |
| สัปดาห์ที่ 3 | {{objectives}} | {{assessment}} | {{rhythmic_time}} | {{main_lesson}} | {{differentiation}} | {{preparation}} |
```

Use `<br>` for line breaks inside a cell. Never split one week across rows.
