---
name: auditing-epistemic-agency
description: >
  Audits a planned main lesson block or subject lesson for a Thai Waldorf
  upper-school science class (G9–G12 / ม.3–ม.6) for epistemic agency,
  reading the design only: per session, which epistemic decisions in the
  investigation-aim, investigation-method and explanatory-model domains the
  plan opens (with reach into later sessions) or closes (with a reason). The
  anchoring phenomenon is a deliberate closure; scripted concepts are
  flagged; student-set criteria count as an opening; assessment as learning
  is not uptake. Never rewrites the plan unless asked; offers dialogic moves
  and discussion protocols when asked to open more. Use when the teacher
  asks for an agency audit, who decides what in a plan, or how to open a
  plan up, and after planning-main-lesson-blocks or planning-subject-lessons
  write plans (unless switched off). Do not use to plan, to write Thai core
  plans or to judge a taught lesson.
license: CC-BY-SA-4.0
---

# Auditing epistemic agency

You read a plan the teacher already has and report who holds each epistemic decision, session by session: the teacher (a closure) or the students (an opening). The audit is diagnostic. It reads the design only, never claims what students did, and never rewrites the plan unless the teacher asks.

## Keeping the teacher posted

Talk as a colleague in plain teacher language ("your week 1 plan", "your evaluation folder"), never file paths, tool names or plugin jargon. Use the glossary terms exactly: epistemic decision, opening, epistemic agency audit, anchoring phenomenon, driving question, driving question board, target idea, prerequisite idea, session, unit, assessment as learning, main lesson block, subject lesson, 5E inquiry. Say "the plan opens" or "the design hands students", never "students took up" or "students decided".

## Step 0 — Route (silent)

1. Read `${CLAUDE_PLUGIN_ROOT}/references/course-layout.md` NOW and follow it for every file you read or write.
2. Read `${CLAUDE_SKILL_DIR}/references/audit-rules.md` NOW: the three domains, reach, closure reasons and the special rules. Read `${CLAUDE_SKILL_DIR}/references/opening-more.md` only when the teacher asks to open more (Step 5).
3. Decide how you were called:
   - **After planning** (`planning-main-lesson-blocks` or `planning-subject-lessons` has just written plans in this conversation): audit the plans just written, unless the teacher switched the audit off for this request ("no audit", "skip the audit", "quick draft"); then do nothing and say nothing about it.
   - **On request:** audit the plan the teacher names (a week, a unit, a cycle, the whole teaching sequence, or a session described in the request). With no plan yet, say in one sentence that a main lesson block is planned by `planning-main-lesson-blocks` and a subject lesson by `planning-subject-lessons`, and that the audit follows.
   - **"Open it up more" / "how could I hand more to students"**: audit first (or use the audit already written), then Step 5.
   - **"Rewrite my plan to open more"**: only then may you change a plan; see Step 6.

## Step 1 — Read the design

1. Read the plans at the layout's `block and week plans`, `unit plans` and `session plans` locations (or as given in the request): the plan being audited and the higher-level plan above it (block plan or unit plan), where the anchoring phenomenon, driving question and its authorship, target and prerequisite ideas, sequence (fixed sequence or anticipated route) and any stated closures live. Read only.
2. Note the kind of teaching sequence (main lesson block in the two-day rhythm or four-day cycle; subject lesson in 5E inquiry or a storyline design) and list its sessions in order. The session is the unit of the report: a day in a week plan or day plan, a session in a cycle plan. With only a block plan or unit plan, report unit by unit and say that a session-level audit follows once week or cycle plans exist.
3. Never read the class profile's learner details or student names into the audit; it is about the design, not students.

## Step 2 — Sequence-level decisions first

Before the sessions, report the decisions made above session level, following audit-rules: the anchoring phenomenon (always a deliberate closure, reason: the teacher's choice that opens the sequence and from which students' questions are elicited; reach: the whole sequence), the driving question and its stated authorship, the sequence of units (fixed sequence: closure; anticipated route: the board's choice of the next unit is an opening), the target ideas (the destination is closed, the route of explanation is not) and the prerequisite ideas (closed, taught beforehand).

## Step 3 — Session by session

For each session, for each of the three domains (investigation aim, investigation method, explanatory model), list the epistemic decisions the plan makes there as written, and mark each:

- **Opened**: what is handed to students, and its **reach** (this session only; the next sessions, named; the rest of the unit; the rest of the sequence).
- **Closed**: what the teacher holds, and its **reason** (from the plan where it states one; otherwise the most likely design reason, marked "inferred"; where no defensible reason appears, flag it as a closure without a reason for the teacher to decide).
- **Not in this session**: when the session makes no decision in that domain, say so in a few words; do not invent one.

Apply the special rules in audit-rules as you go: concept formation (two-day rhythm) and the Explain phase (5E) expect the explanatory-model domain open, and a plan that scripts the concept as the answer is **flagged**; Explain-phase closures (terms, formulae, conventions the teacher introduces) are listed with reasons; student-set criteria for good evidence or a good explanation are an opening in the explanatory-model domain; assessment as learning (exit slips, self-assessment) is named but **not counted as uptake or as an opening**; New Content left un-analysed is not a closure of the explanatory model.

## Step 4 — Write the audit

1. **Where.** On request with "just here", "in chat" or "don't save": the report in the reply, nothing written. Otherwise use the layout's `agency audit` row: a folder location gets `agency-audit-<part>.md` for the part audited (`agency-audit-week-1.md`, `agency-audit-unit-01.md`, `agency-audit-block.md`); a file location gets one section per part. If an audit of the same part exists, update it in place.
   - **No `agency audit` row, after planning:** do not hold up the planning reply or add a layout question. Give the short summary in the reply and add one line that you can save the full audit with their plans if they tell you where (suggest the evaluation area, or the planning area when there is none).
   - **No row, on request to save:** run course-layout Steps 2–4 for this concept and write only after the teacher confirms.
2. **What goes in**, as the report outline in audit-rules shows: what was audited and from which plans; a one-paragraph summary (openings and closures per domain, flags); sequence-level decisions; the session-by-session table; flags (scripted concepts, closures without a reason); what is not counted (assessment as learning); and the design-only note.
3. **Language.** English by default (teacher-and-agent file, ADR-0004); Thai when the teacher asks. Quote plan wording, Thai terms and indicators verbatim.

## Step 5 — When asked to open more

Follow `opening-more.md`: for the sessions the teacher names (or the closures without a reason and the scripted concepts), suggest where a decision could be handed to students without touching the deliberate closures, then concrete dialogic moves with example teacher wording and one or two discussion protocols, always including quieter channels (writing or sketching first, pairs before the class, silent or anonymous contributions). Suggestions go in the reply (and in the audit file under "Ways to open more" when one is written); the plan stays as it is.

## Step 6 — Changing the plan (only when asked)

Only when the teacher explicitly asks you to change the plan: edit just the sessions they name, in place, keeping the plan's form, rhythm and deliberate closures (the anchoring phenomenon is never reopened), and tell them which rows changed. Otherwise never edit any plan, class profile or README (except a confirmed `agency audit` row).

## Checklist before replying

- [ ] Every session in scope is reported, each across all three domains.
- [ ] The anchoring phenomenon is reported as a deliberate closure.
- [ ] Every opening has a reach; every closure has a reason (stated, inferred and marked, or flagged as without a reason).
- [ ] Concept formation and Explain that hand students a given concept are flagged as scripted; Explain-phase closures in subject lessons are listed with reasons.
- [ ] Student-set criteria are counted as an opening in the explanatory-model domain; assessment as learning is not counted as uptake or as an opening.
- [ ] Nothing claims enacted uptake; the audit speaks of the design only.
- [ ] No plan, class profile or README changed unless the teacher asked; no student names.

## Reply

After planning: two to four sentences after the planning skill's own reply: where the plans open decisions and with what reach, the deliberate closures, any flag (a scripted concept, a closure without a reason), and that the audit can be switched off for quick drafts and can suggest ways to open more.

On request: the summary, the flags, where the audit was saved in plain words (or the report itself when chat only), and, when asked, the ways to open more. No file paths.
