# References Index (Agent Entry Point)

Load only what the task needs. The files are arranged by curriculum layer (Bransby & Rawson): **meta** (aims, principles) → **macro** (grade developmental themes) → **meso** (local or statutory content and competencies) → **micro** (generated lessons).

| Layer | File | Load when |
|---|---|---|
| Meta: aims | `waldorf-education-goals.md` | Justifying *why* content belongs: domains, 12 potentialities, diagnostic question |
| Meta: pedagogy | `rawson2021-generative-principles-upper-school.md` | Designing or checking *how* to teach: learning phases, block rhythm, 15-item generation checklist, anti-patterns |
| Macro | `waldorf-upper-school-macro-curriculum.md` | Fixing the **grade mode** (G9 What / G10 How / G11 Why / G12 Who), potentiality-mode matrix, placement diagnostic |
| Meso: competencies | `waldorf-pisa-competencies-g9-g12.md` | Writing learning intentions for science (Sx.n / Ex.n by grade); bilingual EN/TH; *generated snapshot* |
| Meso: competencies | `waldorf-pisa-vertical-progression-g9-g12.md` | Checking ramps between grades and the ethical ladder; *generated snapshot* |
| Meso: source | `pisa-science-2025.md` | Age-15 PISA wording (OECD EN + IPST official TH) and lineage; never plan from this directly |
| Meso: statutory (TH) | `thai-science-core-indicators-2560.md` | Official indicators and core content, P.1–M.6 (`ว x.x ชั้น/ข้อ`) |
| Meso: statutory (TH) | `thai-science-supplementary-learning-outcomes-2560.md` | ม.4–6 science-track electives (biology, chemistry, physics, earth–astronomy–space) |
| Meso: crosswalk | `curriculum-crosswalk.md` | Relating Thai indicators (ม.3–ม.6), Waldorf grade modes and PISA-adapted competencies side by side, with gaps explicit; *generated* from the indicators, glossary, macro and competency files |
| Meso: vocabulary (TH) | `thai-science-glossary-2560.md` | Official meaning of indicator verbs (อธิบาย vs บรรยาย…) |
| Meso: vocabulary (TH) | `thai-science-key-skills-2560.md` | Official Thai skill names: process skills, engineering design, computational thinking, 21st-century |
| Meso: vocabulary (TH) | `thai-science-scientific-mind-2560.md` | Official Thai scientific-attitude names (9 + attitudes towards science) |
| Output format (TH) | `thai-science-indicator-analysis-examples-2560.md` | Producing IPST-style three-column analyses (analysis → learning → assessment) |
| Output template: Waldorf | `waldorf-plan-template-block.th.md` | Planning a whole block week by week (aims, assessable outcomes, weekly rows) |
| Output template: Waldorf | `waldorf-plan-template-week.th.md` | Planning one block week day by day (Mon–Fri, E→R→C→A cycles) |
| Output template: Waldorf | `waldorf-plan-template-day.th.md` | Planning one main-lesson day segment by segment (Rhythmic Time → Recall → Practice → New Content) |
| Output template: Thai | `thai-core-plan-template.th.md` | Writing the school's statutory แผนการจัดการเรียนรู้ (K–P–A, สมรรถนะ, rubrics, sign-off) |

**Default chain for generating a G9–G12 science block:**
1. **Grade mode:** read the macro file.
2. **Intentions:** pick a subset of the grade's PISA-adapted Sx.n.
3. **Statutory anchors:** find the matching Thai indicators in the crosswalk. Interpret their verbs via the glossary.
4. **Justification:** state the domain(s) and potentialities they serve (goals file, §5 template).
5. **Design:** apply the Rawson principles and run the §5 checklist.
6. **Document:** when a Thai-facing write-up is needed, use the IPST three-column format with official skill and attitude names.
7. **Plan output:** fill block → week → day templates. Produce the Thai core plan when the school requires a statutory write-up.

**Sources:** each file's header cites the document it was drawn from (the IPST PDFs, Rawson 2021, the school's original plan forms). Those source documents, and the originals of these files before the agent-facing rewrite (2026-10-27), are kept for verification in the source repository (github.com/wathan/thai-waldorf-teacher-skills, folders sources and archive) and do not ship with the plugin. A "sources/…" path in a file header refers to that repository.
