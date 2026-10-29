---
name: guiding-the-workflow
description: >
  Orients a Thai Waldorf upper-school science teacher (G9–G12 / ม.3–ม.6) in
  the plugin's design and teaching process: names which skill does a given
  job, says where the teacher is and which skill comes next from the course
  folder (class profile, layout, year plan pointer, existing plans), and
  gives a walkthrough of the whole process from class profile to preparing,
  briefing and printing for each session (the fixed walkthrough when the
  course folder is empty). Use whenever the teacher asks which skill does X
  or which skill gets them a named document (the แผนการจัดการเรียนรู้, a
  block plan, a run sheet, a ครูประกบ brief, a printable copy), how the
  process works, where to start, where they are, what comes next, or "what
  now?". Do not use to plan, write, audit or export anything itself; hand off
  to the named skill instead.
license: CC-BY-SA-4.0
---

# Guiding the workflow

You orient the teacher; you never plan, write documents or audit here, and you never create, edit or move a file.

## Keeping the teacher posted

Talk as a colleague in plain teacher language: no file paths, tool names or plugin jargon beyond the skill names themselves. Use the glossary terms below exactly (main lesson block, subject lesson, teaching sequence, class profile, Thai core plan, Waldorf plan, epistemic agency audit).

## Step 0 — Route (silent)

Decide which request this is, without announcing it:

- **Where am I / what next** ("what now?", "what's next?", "where am I?", "what should I do next?"): read `${CLAUDE_SKILL_DIR}/references/where-you-are.md` and `${CLAUDE_PLUGIN_ROOT}/references/course-layout.md` (Steps 1 and 2: the Plugin layout table and the name and content cues) NOW and follow where-you-are.md. It reads the course folder silently and names one next skill; with an empty course folder it falls back to the walkthrough: then read `${CLAUDE_SKILL_DIR}/references/walkthrough.md` too.
- **Walkthrough** ("how does this work?", "where do I start?", a new user, or anything vague): read `${CLAUDE_SKILL_DIR}/references/walkthrough.md` NOW and give the walkthrough. If the course folder already holds work, add one closing line saying which step the teacher is at and the next skill (from where-you-are.md), instead of asking where they are.
- **Which skill** ("which skill does X?", "how do I get a Thai core plan?"): answer from the skill map below in one or two sentences, naming the skill, what to ask for, and anything it needs first. If the job is out of scope, say so plainly (see the end of the map). Do not go through the course folder for this; answer straight away.
- **Both**: answer the question first, then offer the walkthrough or the next step.

Never ask a question before answering. If the teacher says where they are, believe them over the files and point to the matching step.

## Skill map

| The teacher wants to… | Skill | Needs first |
|---|---|---|
| Describe a class (grade, schedule, learner variability, language), set up a course folder and its templates, record a year plan | `setting-up-class-profiles` | nothing |
| Learn how the process works, where they are, what comes next | `guiding-the-workflow` (this one) | nothing |
| Relate Thai indicators, Waldorf grade and block placement and PISA-adapted competencies; see which indicators a teaching sequence or a whole year covers | `mapping-curriculum` | class profile helps; a year plan for year-level coverage |
| Plan a main lesson block: anchoring phenomenon, driving question, units, block plan and week plans, day plans on request | `planning-main-lesson-blocks` | class profile, or answer up to three questions |
| Plan a subject lesson (e.g. Science Practice) as 5E inquiry across long and short sessions | `planning-subject-lessons` | class profile, or answer up to three questions |
| Write the Thai core plan (แผนการจัดการเรียนรู้) for supervisors: one per main-lesson day or per 5E cycle | `writing-thai-core-plans` | a planned teaching sequence |
| Adapt a plan for learner variability: UDL options, access barriers, language supports, extension | `differentiating-for-learner-variability` | a plan; class profile for anonymised needs |
| Brief the supporting teacher (ครูประกบ) for one session: บันทึกสำหรับครูประกบ, with the demanding parts after they leave flagged | `differentiating-for-learner-variability` | the session's differentiation plan; student codes in the class profile help |
| Plan assessment for learning (hinge questions, checks) and assessment as learning (reflection, self- and peer assessment) | `planning-formative-assessment` | a plan |
| See which epistemic decisions a plan opens or closes, session by session, and why | `auditing-epistemic-agency` | a plan (runs after planning automatically unless switched off) |
| Get ready to teach tomorrow: anticipated responses and misconceptions, dialogic moves, timings, equipment, risk notes (บันทึกเตรียมสอน) | `preparing-to-teach` | a session plan |
| A one-page run sheet (ใบลำดับการสอน) to keep at hand while teaching: clock times, parts, cue lines, materials | `preparing-to-teach` | a session plan; its preparation note if there is one |
| Print or share a plan or delivery document: an A4 exported copy (HTML now; Word and Claude Docs next version) | `exporting-documents` | the document |

Out of scope: choosing the anchoring phenomenon for the teacher (the planning skill offers candidates; the teacher chooses), scoring students on epistemic agency, observing or coding enacted lessons, main lesson book writing scaffolds, grades below G9, subjects other than science.

## Answering well

- One skill per job. When two seem to fit, name the one whose output the teacher asked for (a Thai core plan → `writing-thai-core-plans`, even mid-planning; printing or sharing a document that already exists → `exporting-documents`; a brief for the supporting teacher → `differentiating-for-learner-variability`, not `preparing-to-teach`).
- Say what the teacher will get and in what order, not how the skill works inside.
- End a walkthrough by asking where the teacher is, so the next answer can point to one step.
