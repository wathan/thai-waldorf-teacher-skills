---
name: writing-thai-core-plans
description: >
  Writes Thai core plans (แผนการจัดการเรียนรู้, Core Curriculum B.E. 2551
  layout) for external supervision of a Thai Waldorf upper-school science
  class (G9–G12 / ม.3–ม.6): one plan per main-lesson day, with ขั้นนำ /
  ขั้นสอน / ขั้นสรุป filled from the Waldorf day, or one plan per 5E cycle
  of a subject lesson, with the stages as its design maps them; Thai indicators verbatim,
  K-P-A objectives unpacked from them, rubrics, official Thai skill and
  attitude names, the Buddhist-era ปีการศึกษา and blank scoring tables, and
  reports where the plans it was written from and the Thai core plan
  disagree. Use when the teacher asks for a Thai core plan,
  แผนการจัดการเรียนรู้, lesson plan for the supervisors or the school's
  statutory plan for days of a planned main lesson block or cycles of a
  planned subject lesson unit. Do not use to plan the block, its week plans or
  day plans, or a subject lesson's design.
license: CC-BY-SA-4.0
---

# Writing Thai core plans

You write the Thai core plan (แผนการจัดการเรียนรู้) that external supervisors receive, from a teaching sequence the teacher has already planned. The Thai core plan describes the lesson truthfully; it never redesigns it. The Waldorf plans and the Thai core plan must agree.

## Keeping the teacher posted

Talk as a colleague in plain teacher language: "your Thai plans folder", "the school's lesson plan form", never file paths, tool names or plugin jargon. Use the glossary terms exactly: Thai core plan, Waldorf plan, day plan, week plan, main lesson block, two-day rhythm, sequencing difference, assessment as learning.

## Step 0 — Route (silent)

1. Read `${CLAUDE_PLUGIN_ROOT}/references/course-layout.md` and `${CLAUDE_PLUGIN_ROOT}/references/class-profile.md` NOW. Follow both for every file you read or write.
2. Decide what is asked:
   - **Main-lesson days** (one day, several days, a week or the whole block of a main lesson block): one Thai core plan per day. Read `${CLAUDE_SKILL_DIR}/references/main-lesson-days.md` NOW; it supplies the source of each plan, the stage mapping and the consistency check used in Steps 2 and 4.
   - **Subject lessons** (one Thai core plan per 5E cycle of a unit; never per session, and no Waldorf plans): read `${CLAUDE_SKILL_DIR}/references/5e-cycles.md` NOW; it replaces main-lesson-days.md's sources, stage mapping and consistency check in Steps 2 and 4, and where this file says Waldorf plans, read the unit plan and cycle plans.
   - **Planning the block, its week plans or day plans:** belongs to `planning-main-lesson-blocks`. **Designing a subject lesson:** belongs to `planning-subject-lessons`.
3. Whatever the route, read `${CLAUDE_SKILL_DIR}/references/filling-the-form.md` NOW: it holds the section-by-section rules shared by every Thai core plan.
4. Read these shared references NOW too; filling-the-form.md says what each section takes from them:
   - `${CLAUDE_PLUGIN_ROOT}/references/thai-core-plan-template.th.md`: the plugin's form (used when the course has no form of its own) and its Section 7 stage mapping.
   - `${CLAUDE_PLUGIN_ROOT}/references/thai-science-core-indicators-2560.md` (and, for a ม.4–6 elective, `${CLAUDE_PLUGIN_ROOT}/references/thai-science-supplementary-learning-outcomes-2560.md`): indicators, character for character.
   - `${CLAUDE_PLUGIN_ROOT}/references/thai-science-glossary-2560.md`: indicator verbs, for the K objectives.
   - `${CLAUDE_PLUGIN_ROOT}/references/thai-science-key-skills-2560.md` and `${CLAUDE_PLUGIN_ROOT}/references/thai-science-scientific-mind-2560.md`: official skill and attitude names, for the P and A objectives.
   - `${CLAUDE_PLUGIN_ROOT}/references/thai-science-indicator-analysis-examples-2560.md`: IPST's own unpacking, the style to match.

## Step 1 — Context, at most three questions

1. Read the class profile where the layout places it: grade and Thai grade (ม.), grade mode, session length, languages, academic year.
2. Read the plans the route reference names as sources, at their mapped locations. A Thai core plan is written only from a planned teaching sequence: if the plan it would describe does not exist, say so in one sentence, name the skill that writes it, and write nothing.
3. **Scope.** Write exactly the plans asked for. If the request leaves the scope open, ask once with a recommendation (e.g. "the days of this week, recommended").
4. **Without a class profile:** follow class-profile.md's "When there is no class profile" (at most three questions in one numbered round; every other value a stated assumption from its defaults). The questions you may ask, only where the plans leave them open: usually the grade and the session length. Work out the ปีการศึกษา from today's date.

Never read the course folder's name for meaning.

## Step 2 — Map the lesson onto the three stages

Follow the route reference's stage mapping. Section 7's three stages (ขั้นนำเข้าสู่บทเรียน, ขั้นสอน/ขั้นจัดกิจกรรม, ขั้นสรุป) list what the lesson actually does, in the order the source plan gives, with the source's times. Never move an activity to a stage where it does not happen to make the form look conventional, and never add activities the source plan does not have.

## Step 3 — Fill the form

1. **Where.** Use the layout's `Thai core plans` row. A folder location gets one file per plan, named as the route reference says; a file location holds one section per plan in order. If a plan already exists there, update it in place and keep the teacher's decisions; never create a second one. With no row, run course-layout Steps 2–4 for this concept only (usual area: planning) and write after the teacher confirms (or has said up front they accept your proposal).
2. **Which form.** Follow course-layout's "Plan templates: the course's own come first" for the Thai core plan: a course template in the templates location is used exactly (its sections, labels, order and language win); otherwise the plugin's `${CLAUDE_PLUGIN_ROOT}/references/thai-core-plan-template.th.md`. Say in one line which one you used. The content rules in `filling-the-form.md` hold in either form wherever the course form has a matching place.
3. **What goes in.** Fill every section as `filling-the-form.md` describes: header and ปีการศึกษา, indicators verbatim with any sequencing difference cited and justified, K-P-A objectives unpacked from the indicators, official skill and attitude names, the stages from Step 2, measurement with rubrics, blank scoring tables and blank sign-off and results.
4. **Language.** The form's language: Thai for the plugin's form (supervisors read it), with every heading and label kept exactly; the course form's language when it has its own. English only when the teacher asks for it, with Thai official terms (indicators, skill and attitude names, ปีการศึกษา) still verbatim.

## Step 4 — Check consistency with the Waldorf plans

Run the route reference's consistency check on every plan you wrote, against the plans it was written from. Never edit a Waldorf plan to make it agree, and never copy a problem into the Thai core plan: report each disagreement or rule break in the reply in plain words (which day, which part, what differs), say which way the Thai core plan follows, and offer to fix the Waldorf plan through `planning-main-lesson-blocks` (a subject lesson's unit or cycle plan through `planning-subject-lessons`).

## Checklist before replying

Run this against the files you wrote, and fix any miss before replying:

- [ ] Exactly the plans asked for, one per main-lesson day or one per 5E cycle, at the `Thai core plans` location; the course's own form if it has one, otherwise the plugin's, headings and labels kept.
- [ ] Each stage lists what the source plan does there, in its order and with its times; nothing invented, nothing moved.
- [ ] Main-lesson days: ขั้นสรุป never explains, discusses or analyses that day's new experience; it closes and says what tomorrow's recall picks up.
- [ ] Main-lesson days: recall in ขั้นนำ is open questions; a quiz or closed check in the day plan is reported, never scored.
- [ ] 5E cycles: stages follow the cycle plan's mapping, each step labelled with its phase and session; time is the sum of the cycle's sessions; retrieval practice and exit slips unscored.
- [ ] Indicator codes and Thai wording are verbatim; every sequencing difference is cited as written with a grade-mode reason.
- [ ] K, P and A objectives each come from the indicators and the day's work; P uses official skill names, A uses the 8 คุณลักษณะอันพึงประสงค์ or official scientific-attitude names; every objective has a measurement row and a rubric.
- [ ] Rubrics describe this lesson's tasks, not the form's maths example.
- [ ] Assessment as learning is named without a score; nothing at Recall is scored.
- [ ] ปีการศึกษา in the Buddhist era; ระดับชั้น as the Thai grade.
- [ ] Scoring tables blank (no names, no numbers); results after teaching and the administrator's comments blank; signature lines left to sign.
- [ ] No student names or identifying details anywhere.
- [ ] Every disagreement with the Waldorf plans is in the reply; no Waldorf plan was changed.
- [ ] Files sit where the layout says; nothing renamed, moved or deleted.

## Reply

A few sentences: which Thai core plans were written and where in teacher terms, which form was used, any assumption made, every disagreement with the Waldorf plans found in Step 4 with the offer to fix it, and what is left for the teacher (signing, filling in class lists and results after teaching).
