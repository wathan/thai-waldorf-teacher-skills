# The supporting-teacher brief

How to write บันทึกสำหรับครูประกบ: a note for the supporting teacher (ครูประกบ) about one whole session, built from the session's differentiation plan. Thai by default (ADR-0005); English only when the teacher asks.

## Contents

- [Before writing](#before-writing)
- [Finding the demanding parts](#finding-the-demanding-parts)
- [Shape](#shape)
- [Pre-teaching section](#pre-teaching-section)
- [Where and how long](#where-and-how-long)
- [Reply](#reply)

## Before writing

1. **Differentiation plan.** Find the one covering this session at the layout's `differentiation` location. None: say plainly that the brief rests on the differentiation plan's barriers and supports, offer to write that plan first, and write no brief. A plan for the whole teaching sequence or week counts if it covers this session.
2. **Session plan.** Read it at the `session plans` location for the parts, their order and times. Read only.
3. **Run sheet.** If one exists for this session at the `preparation notes` location, take the times from it; else from the session plan.
4. **Class profile.** Read the Schedule's `Supporting teacher` and `Pre-teaching slot` lines and the learner variability codes.
   - **No supporting teacher recorded and none in the request:** ask one question: when are they in the room, and what do they do? Recommend "the whole session, supporting the students with learning differences".
   - **No codes:** write the brief by need ("นักเรียนที่มีความต้องการด้านการอ่าน") and end the reply with one line suggesting codes be added to the class profile (`setting-up-class-profiles`) so the brief can say who gets which support.
5. **Never** open a private folder, use a name, nickname or initial, or write who a code stands for. When the teacher's request names a student, leave the name out and say so in one line (Step 2).

## Finding the demanding parts

A part is **demanding** for a coded student when one of its tasks collides with that student's recorded need: the differentiation plan's barrier table marks the part high severity for learning differences, or answers it with targeted support, and the barrier matches the need written beside the code in the class profile. Check each flagged part against the profile; drop a flag the profile's needs do not support, and add one where a task plainly meets a recorded need the plan missed (say so in the reply as a gap in the differentiation plan).

Flag every demanding part, whether or not the supporting teacher is present. A demanding part **after the supporting teacher leaves** (or before they arrive) gets ⚠ in the brief and a follow-up suggestion: what to practise or revisit with the student next time they meet (the pre-teaching slot when there is one), never re-teaching the session's target idea in advance.

## Shape

Walk the whole session in teaching order, one row per part. Cells are short: at most two lines each; supports name the code and the concrete action.

```markdown
# บันทึกสำหรับครูประกบ: คาบที่ 1 (พฤหัสบดี 29 ต.ค.) ผ้าเปียกกับน้ำร้อน

จากแผนการปรับการสอนของคาบที่ 1 · ครูประกบอยู่ 13:00–15:00 · ดูแลนักเรียน ก และนักเรียน ข (ไม่ช่วยงานอุปกรณ์ทดลอง)

**บทบาท:** ช่วยให้นักเรียนเริ่มคิดเองได้ ไม่คิดแทน ไม่บอกคำตอบ

| เวลา | ช่วง | ครูประกบ | เกิดอะไรขึ้น | ช่วยอย่างไร | สังเกตอะไร / เมื่อไรถอย |
|---|---|---|---|---|---|
| 13:00–13:10 | นำเข้าสู่บทเรียน | อยู่ | มือเปียกกับมือแห้ง เป่าลมแล้วเทียบ | ชี้คำถามแบบตรงตัวบนกระดานให้ ก และ ข | ถ้าเริ่มพูดถึงสิ่งที่รู้สึกเอง ถอยออก |
| 13:35–13:50 ⚑ | เขียนนิยามและตัวแปร | อยู่ | เขียนว่า "เย็นเร็วกว่า" วัดอย่างไร ก่อนครูสอนคำศัพท์ | ไล่บันไดคำถามบนบัตรขั้นตอนกับ ก และ ข ทีละข้อ | ไม่เขียนแทน · ถ้าค้างเกิน 3 นาที ให้เลือกจากสองตัวเลือก |
| … | … | … | … | … | … |
| 15:00–15:25 ⚠ | อธิบาย (สรุปทั้งห้อง) | ไม่อยู่ | ศัพท์ ตัวแปรต้น ตัวแปรตาม ตัวแปรควบคุม · อภิปรายเร็ว | — | ⚠ ส่วนที่ยากที่สุดของคาบ เกิดหลังครูประกบออก |

**ส่วนที่ยากหลังครูประกบออก**
- ⚠ 15:00–15:25 อธิบาย: นามธรรมสูงและพูดเร็ว (ก: ภาษาไม่ตรงตัว · ข: ความคิดเชิงนามธรรม). ครั้งหน้า: ทบทวนสามคำกับตารางสามแถวจากกรณีอื่น
```

- Title: `บันทึกสำหรับครูประกบ:` then the session as the preparation note names it.
- Under the title: the source, the supporting teacher's window and role from the profile, the codes they support.
- **ครูประกบ** column: `อยู่` or `ไม่อยู่` for every row; a part they are present for only partly says when they leave (`อยู่ถึง 15:00`).
- ⚑ marks a demanding part while the supporting teacher is present; ⚠ one when they are not.
- Rows where they are absent keep เกิดอะไรขึ้น but leave ช่วยอย่างไร as `—`.
- Supports come from the differentiation plan's targeted supports and the shared task's UDL options, said as actions for the supporting teacher; never a new support, never one that lowers the core learning intention.
- After the table, **ส่วนที่ยากหลังครูประกบออก**: one bullet per ⚠ part with the colliding need per code and a follow-up suggestion. Omit the heading when there is none.

Use plain, literal Thai: one action per sentence, verb first, no idioms. Keep the session's own part names.

## Pre-teaching section

Only when the class profile records a pre-teaching slot. Heading `ช่วงเตรียมล่วงหน้า (<day and time from the profile>)`, then at most five bullets:

- the routine to rehearse (the session's parts and room changes, from the picture timetable or the plan);
- the words to practise (from the differentiation plan's language supports, the Tier 2 and Tier 3 words students meet in the session);
- the different case to practise them on: one everyday case that uses the same routine and words but is **not** the session's phenomenon, so the session's experience stays new;
- any card or frame to try out beforehand;
- follow-up from the ⚠ parts of the previous session, if its brief flagged any.

## Where and how long

- **Where.** The layout's `preparation notes` location, one file per session, named like the session's preparation note with `-brief` (`session-1-brief.md`, `week-2-day-6-brief.md`). An existing brief for the session is updated in place, keeping the teacher's own additions. With no `preparation notes` row, run course-layout Steps 2–4 for that concept only (usual area: delivery) and write after the teacher confirms.
- **How long.** At most two A4 pages: about 600 Thai words, table included. Cut supporting detail before cutting a row; never drop a ⚠ part.
- **Read-only elsewhere.** Never edit the session plan, the differentiation plan, the run sheet or the class profile.

## Reply

A few sentences to the lead teacher in plain teacher language: where the brief is, the supporting teacher's window, and **the demanding parts after the supporting teacher leaves**, each with the code and need it affects, so the teacher can plan their own support for those students. Add any gap found in the differentiation plan, any assumption, and the no-codes line when it applies.
