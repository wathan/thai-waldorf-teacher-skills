# The run sheet

How to write ใบลำดับการสอน: one A4 page for one session, kept at hand while teaching. It is the running order only: when, what, what to say, what to pick up. The reasoning, anticipated responses and risk explanations stay in the preparation note. Thai by default (ADR-0005).

## Contents

- [Sources](#sources)
- [Shape](#shape)
- [Rules](#rules)

## Sources

1. **The session plan** (day plan or 5E session): parts, order, timings, materials. Read only.
2. **The session's preparation note**, if one exists at the `delivery documents` location: the key cue line per part (the opening Recall question, the hold-don't-correct line, the hard stop) and the setup checklist. With no preparation note, build from the plan alone and say so in the reply; never write a preparation note the teacher did not ask for.
3. **The class profile:** the session length, and the `Supporting teacher` line for the presence marker.

## Shape

```markdown
# ใบลำดับการสอน: คาบที่ 1 (พฤหัสบดี 29 ต.ค.) ผ้าเปียกกับน้ำร้อน

160 นาที · 13:00–15:40 · 👥 = ครูประกบอยู่ (13:00–15:00)

| เวลา | ช่วง | สัญญาณ/คำพูดหลัก | สื่อและอุปกรณ์ |
|---|---|---|---|
| 13:00–13:10 👥 | นำเข้าสู่บทเรียน | "เป่ามือทั้งสองข้าง ข้างไหนเย็นกว่า" | ถ้วยน้ำอุณหภูมิห้อง |
| 13:45 | — | ⏱ เปิดกาต้มน้ำ 85 °C ทั้งสองใบ | กาต้มน้ำ 2 |
| 14:45–14:50 👥 | อภิปรายความยุติธรรม | **หยุดตรง 14:50** · "ดูอุณหภูมิที่ลดลง" | ตารางรวมบนกระดาน |
| 15:00–15:25 | อธิบาย | ให้กลุ่มเทียบตารางก่อน · ย่อตัวอย่างที่ 15:07 ไม่ใช่ 15:00 | ใบตัวอย่าง |
| 15:40 | ปิดคาบ | เก็บสมุดทุกเล่ม บัตรท้ายคาบแยกกอง | กล่องสมุด |

**ก่อนคาบ:** ☐ ชุดอุปกรณ์กลุ่ม ×5 ☐ พิมพ์บัตรบทบาท ☐ กระดาน: ตารางเวลาภาพ, แกนกราฟเปล่า
```

- **Title:** `ใบลำดับการสอน:` then the session as the preparation note names it (week and day, or session number, date, topic).
- **Header line:** the session length and clock span; the presence key when the profile records a supporting teacher.
- **เวลา:** clock times when the plan has them (or the class profile's session start time); otherwise running minutes from the start (`0–10`, `10–55`). Mark 👥 on every row the supporting teacher is present for, and nothing when no supporting teacher is recorded.
- **ช่วง:** the plan's own part names, in Thai.
- **สัญญาณ/คำพูดหลัก:** at most two short items per row: the one line to say, a hard stop in bold, a ⏱ timing cue, or a watch-the-clock reminder. Lines said to students in the class profile's language of student materials.
- **สื่อและอุปกรณ์:** what to pick up for that part, short nouns.
- **Timed setup rows** (kettle on, fill jugs, hand out cards) get their own row with `—` as ช่วง.
- **ก่อนคาบ:** one line of tick boxes for what must be ready before the session starts, from the preparation note's setup list.

## Rules

- One page: at most about 15 rows and no prose paragraphs. Cut cue lines before cutting a row.
- Same read-only plan check as the preparation note: when the parts do not add up to the session length, show the plan's times and report the mismatch in the reply.
- No reasoning, no anticipated responses, no risk explanations; a safety-critical action (teacher pours only, gloves on) may appear as a cue line.
- No student names or identifying details.
- **Where:** the layout's `delivery documents` location, named like the preparation note with `-run-sheet` (`session-1-run-sheet.md`, `week-2-day-6-run-sheet.md`); a file location gets a section after that session's note. Update an existing run sheet in place, keeping the teacher's own additions.
