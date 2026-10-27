# Waldorf Block Plan Template (แผนรายบล็อก)

> **Source:** `sources/waldorf-plan-template-block.th.docx` (school form, bilingual EN/TH labels). Labels below are verbatim.
>
> **What this is:** Top level of the Waldorf planning chain: one main-lesson **block** (one subject, ~3–4 weeks, ~90–100 min daily; Rawson P7), planned week by week. It breaks down into `waldorf-plan-template-week.th.md` (one per week), which breaks down into `waldorf-plan-template-day.th.md` (one per day).
>
> **Agent use:**
> - Keep the bilingual labels. Write cell content in Thai by default, with Thai official terms (indicator codes and wording, skill and attitude names) verbatim; in English when the teacher asks. Student-facing wording follows the class profile's language of student materials.
> - **Block Aims:** trace to ≥1 domain and ≥1 potentiality in `waldorf-education-goals.md`, phrased in the grade mode from `waldorf-upper-school-macro-curriculum.md`.
> - **Block Objectives and Assessable outcomes:** for science, draw on the grade's Sx.n / Ex.n in `waldorf-pisa-competencies-g9-g12.md`. Add the matching Thai indicator codes (`thai-science-core-indicators-2560.md`) in brackets when a Thai plan (`thai-core-plan-template.th.md`) will be produced. Each outcome states *how* learning is evidenced.
> - **One row per week.** The form has 3 rows. Add a `สัปดาห์ที่ 4` row for a 4-week block.
> - Weekly **Objectives** must add up to the block objectives. Every weekly objective needs a matching **Assessment** entry in the same row.
> - **Rhythmic Time** = attunement or circle activity (movement, recitation, mental work). **Main Lesson** = the week's content arc in the two-day rhythm (ADR-0003): each experience left un-analysed on its day, recalled the next day straight into concept formation, then applied. Week 1 opens by connecting to the previous block in this subject (Rawson §2.4).
> - **Differentiation:** UDL first: light universal options for the whole class around one shared task every student can start, with room to extend and several ways in; targeted supports for anonymised needs after that. Tiers or Rawson's three levels of application tasks only as one option within UDL, never as the default.
> - Before output, run the generation checklist in `rawson2021-generative-principles-upper-school.md` §5, reading its rhythm item as the two-day rhythm and its three levels as UDL options.
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
