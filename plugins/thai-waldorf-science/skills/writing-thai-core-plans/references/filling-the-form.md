# Filling the Thai core plan form

Section-by-section rules for every Thai core plan, whatever the teaching sequence. Section numbers follow the plugin's form, `${CLAUDE_PLUGIN_ROOT}/references/thai-core-plan-template.th.md`; with a course's own form, apply each rule to the matching place in it and skip rules with no place.

## Contents

- [Header](#header)
- [1. Standards and indicators](#1-standards-and-indicators)
- [2. K-P-A objectives](#2-k-p-a-objectives)
- [3 to 6. Key concept, competencies, content, integration](#3-to-6-key-concept-competencies-content-integration)
- [7. Learning activities](#7-learning-activities)
- [8. Materials and sources](#8-materials-and-sources)
- [9. Measurement and rubrics](#9-measurement-and-rubrics)
- [Scoring tables, results and sign-off](#scoring-tables-results-and-sign-off)
- [Hour-by-hour detail](#hour-by-hour-detail)

## Header

- **ระดับชั้น:** the Thai grade from the class profile (G9 = ม.3, G10 = ม.4, G11 = ม.5, G12 = ม.6).
- **ปีการศึกษา:** the Buddhist-era academic year from the class profile; without one, work it out from today's date (the Thai academic year starts in May; ปีการศึกษา = the CE year it starts in + 543). Never copy the form's example year. Add ภาคเรียนที่ when the profile or the course form gives a term.
- **กลุ่มสาระการเรียนรู้:** วิทยาศาสตร์และเทคโนโลยี.
- **ชื่อผู้สอน:** the teacher's name only if the teacher or the course gives it; otherwise leave the dotted line for them. The school name stays as the form prints it.

## 1. Standards and indicators

- Copy สาระ, มาตรฐาน and each ตัวชี้วัด with its code (`ว x.x ม.n/k`) and Thai wording **character for character** from `${CLAUDE_PLUGIN_ROOT}/references/thai-science-core-indicators-2560.md` (ม.4–6 electives: `${CLAUDE_PLUGIN_ROOT}/references/thai-science-supplementary-learning-outcomes-2560.md`). Never paraphrase, shorten or translate an indicator.
- Use only indicators the teaching sequence claims (its block plan or standards map), and only those this plan's lesson actually works toward. A day that reaches part of an indicator still cites it whole; the objectives say which part.
- **Sequencing difference:** an indicator assigned to another ม. grade than the class's is cited as written, followed by a short Thai note giving the indicator's grade and the grade-mode reason, taken from the block plan when it gives one (e.g. "หมายเหตุ: ตัวชี้วัดนี้กำหนดไว้ในระดับชั้น ม.6 นำมาจัดการเรียนรู้ในชั้น ม.5 เพราะ…"). Never drop or rewrite the indicator to hide the difference.

## 2. K-P-A objectives

Unpack each indicator into what this lesson develops, then write the objectives from that (after competency-unpacker):

1. **Read the verb** through `${CLAUDE_PLUGIN_ROOT}/references/thai-science-glossary-2560.md` (อธิบาย, บรรยาย, วิเคราะห์ … each asks for a different performance). The K objective keeps the indicator's demand at the level this lesson reaches: on a day of observation, describing what was observed; on a day of concept formation, explaining in students' own words.
2. **K (ด้านความรู้):** the knowledge point(s) of the indicator this lesson works toward, as something students can say, draw or explain ("นักเรียนสามารถอธิบาย…"). Phrase it as a performance, never as the scripted concept.
3. **P (ด้านทักษะ/กระบวนการ):** the skills the lesson's activities actually exercise, by their official names from `${CLAUDE_PLUGIN_ROOT}/references/thai-science-key-skills-2560.md` (e.g. ทักษะการสังเกต, ทักษะการสร้างแบบจำลอง, ทักษะการตีความหมายข้อมูลและลงข้อสรุป; 21st-century skills by their listed names).
4. **A (ด้านคุณลักษณะ):** from the 8 คุณลักษณะอันพึงประสงค์ in the template's controlled vocabulary and the scientific attitudes in `${CLAUDE_PLUGIN_ROOT}/references/thai-science-scientific-mind-2560.md` (prefer its nine names, e.g. ความใจกว้าง, ความอยากรู้อยากเห็น, ความเชื่อมั่นต่อหลักฐาน), chosen for what the lesson's activities let students show.
5. Keep each list short (one to three objectives per domain). Every objective gets its own row in Section 9.

`${CLAUDE_PLUGIN_ROOT}/references/thai-science-indicator-analysis-examples-2560.md` shows IPST's own unpacking into knowledge, skills and scientific mind with evidence sources; match its style.

## 3 to 6. Key concept, competencies, content, integration

- **3. สาระสำคัญ:** the target idea(s) this lesson works toward, from the teaching sequence's design, in two to four Thai sentences; core content wording from the indicators file where it fits.
- **4. สมรรถนะสำคัญของผู้เรียน:** only those of the five that the activities exercise *and* Section 9 assesses, by their official names.
- **5. สาระการเรียนรู้:** the topics of this lesson's activities.
- **6. สาระการเรียนรู้สู่การบูรณาการ:** only real links in the lesson (e.g. คณิตศาสตร์ for data work, ภาษาไทย for main lesson book writing, ศิลปะ for drawing); otherwise `-`.

## 7. Learning activities

The three stages follow the route reference's stage mapping exactly. Write student-centred steps as the lesson runs them, with minutes. **ชิ้นงาน/ภาระงาน:** the products students make (main lesson book entries, sketch models, data tables).

## 8. Materials and sources

From the plans' Preparation cells and resources: equipment, media, printed sources, places. Never invent a source that is not in the plans or the course.

## 9. Measurement and rubrics

**Measurement table.** One row per K, P and A objective: วิธีการวัดผล (e.g. ตรวจบันทึกในสมุดบทเรียนหลัก, สังเกตการอภิปราย), เครื่องมือวัด (the rubric or checklist below), เกณฑ์การประเมินผล (the pass level). Evidence comes from work the lesson already produces; no added test. Nothing at recall is scored.

**Assessment as learning.** Reflections and self-assessment are named in the measurement section as การประเมินเพื่อการเรียนรู้ของตนเอง (assessment as learning), with "ไม่ให้คะแนน" (not scored), and get no column in the scoring tables. When the plan includes students checking their own work, give them a **single-point rubric** (after single-point-rubric-designer): one column of criteria written as the expected quality, with blank columns either side for "ยังต้องพัฒนา" and "ทำได้เกินเกณฑ์" for students' own notes; no levels and no points.

**4-level rubrics (9.1).** The form's rubrics are maths examples; rewrite every criterion for this lesson (after criterion-referenced-rubric-generator):

- One rubric row per objective assessed, named for the observable performance (e.g. "การสร้างแบบจำลองการเคลื่อนที่ของอากาศ").
- Descriptors describe the **quality of the work** at each level, in parallel wording that changes one dimension at a time (completeness, accuracy, use of evidence, own reasoning), so a teacher can place a piece of work from what is on the page. Avoid vague steps (ดีมาก/ดี/พอใช้ alone) and counting-only or percentage-only steps unless the task really is a count.
- Level 3 describes meeting the objective; level 4 goes beyond it; level 2 is partial; level 1 is beginning.
- For A objectives, describe observable behaviour in the lesson (listening to other positions, citing evidence), using the form's existing A rows where they fit.
- Keep the form's 4-level scale, its การแปลความหมาย lines and หมายเหตุ pass lines.

## Scoring tables, results and sign-off

- **Scoring tables** (แบบบันทึกคะแนน…, แบบบันทึกการประเมินผล…): set the column headings to this plan's instruments, skills and attributes, with their maximum points; leave every row **blank**: no student names, numbers, initials, sample rows or scores. The teacher fills in the class list.
- **บันทึกผลหลังการสอน** (results after teaching), **ปัญหาและอุปสรรค**, **ข้อเสนอแนะ**: leave blank unless the teacher supplies results; never invent counts or percentages.
- **Signature lines and ความคิดเห็นของผู้บริหาร:** keep the dotted lines; fill only the teacher's name and position if the teacher gave them.

## Hour-by-hour detail

The form ends with รายละเอียดของแผนการจัดการเรียนรู้ในแต่ละชั่วโมง. Fill it with the timed sequence of the lesson from its source plan (the day plan's rows, in order, with minutes, recall questions as asked and the UDL options), in the form's language. Never add content the source plan does not have.
