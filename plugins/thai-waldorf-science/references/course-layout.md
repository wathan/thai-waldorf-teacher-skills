# Course layout: detection and the "Plugin layout" mapping

Shared by every skill that reads or writes files in a course folder (ADR-0002). A course folder holds one teaching sequence. The plugin follows the layout the teacher already has; it never imposes one. The confirmed mapping lives in the course README's "Plugin layout" section, and every skill reads it before reading or writing course files.

## Contents

- [Rules](#rules)
- [Concepts](#concepts)
- [Step 1: read the recorded layout](#step-1-read-the-recorded-layout)
- [Step 2: detect a layout](#step-2-detect-a-layout)
- [Step 3: propose and confirm](#step-3-propose-and-confirm)
- [Step 4: record the mapping](#step-4-record-the-mapping)
- [No recognisable structure](#no-recognisable-structure)
- [Plan templates: the course's own come first](#plan-templates-the-courses-own-come-first)

## Rules

- **The folder name is off limits.** Never read the course folder's own name for meaning (it is not the subject, grade or class), never mention it, never rename or move the folder. Work with paths relative to the folder.
- **Stay inside the course folder.** The only file outside it a skill may touch is the year plan, at the path the class profile gives (see `year-plan.md`); only `setting-up-class-profiles` writes it. Plugin reference files are not course files and may always be read.
- **Private folders are off limits.** A folder inside the course named `private` (any case, at any depth), or one the course's ignore rules (`.gitignore`) mark as private, holds things such as a student roster. Never read, list, search or mention it or anything in it, never copy from it, and leave it out of detection and of the mapping.
- **Never rename, move or delete the teacher's files or folders.** New files go where the mapping says; existing files are only edited when they are the mapped file for a concept.
- **Map only after confirmation.** Detection proposes; the teacher confirms or corrects; only then is the mapping recorded. A teacher who says up front that they accept the proposed layout has confirmed it.
- **Read, don't guess again.** Once a mapping is recorded, skills use it as written, even where they would have chosen differently.
- **Create on first write.** A mapped location that does not exist yet is created when a skill first writes there, not before. The one exception is the default course template, which `setting-up-class-profiles` creates whole once the teacher confirms it.

## Concepts

Each concept has a fixed name, used verbatim in the mapping table. Locations may be a file or a folder (a trailing `/` marks a folder).

| Concept | What it holds | Usual area |
|---|---|---|
| class profile | The one class this teaching sequence is for (format: `class-profile.md` in this folder) | admin |
| year plan | Not mapped: the year plan lives outside the course, and its path is in the class profile's "Year plan" section | outside the course |
| standards map | Thai indicators this teaching sequence claims; coverage | planning |
| block and week plans | Waldorf block plan and week plans (main lesson blocks) | planning |
| unit plans | Per unit: anchoring phenomenon, driving question and its authorship, target and prerequisite ideas, fixed or interchangeable | design |
| session plans | Waldorf day plans, or 5E sessions for subject lessons | design |
| Thai core plans | แผนการจัดการเรียนรู้ documents | planning |
| differentiation | UDL options and targeted supports | design |
| assessments | Assessment for learning and assessment as learning | assessment |
| agency audit | Epistemic agency audit reports | evaluation |
| driving question board | Record of the class's driving question board | delivery |
| preparation notes | Day-before preparation, equipment and setup, risk notes | delivery |
| resources | Equipment lists, sources, handouts, student materials | resources |
| templates | Course-local plan templates, used before the plugin's (see [Plan templates](#plan-templates-the-courses-own-come-first)) | templates |

## Step 1: read the recorded layout

1. Look for a README at the course folder's top level (`README.md`, any case; also `readme.md`, `README.th.md`).
2. If it has a `## Plugin layout` section, use its table. Do not detect again.
3. If a concept the skill needs is missing from the table, run Steps 2–4 for that concept only and add one row.
4. If a mapped location has been renamed or removed by the teacher, say so plainly and ask where that concept now lives; update the row once confirmed.

## Step 2: detect a layout

Only when no mapping is recorded.

1. List the course folder's folders and files, three levels deep, skipping hidden entries and private folders. Folders count even when empty. Read a file's first lines only when its name is ambiguous.
2. Match each entry against the cues below, in English or Thai, ignoring case, numbering prefixes (`00 `, `01_`, `1.`) and separators.

| Concept or area | Name cues | Content cues |
|---|---|---|
| admin | admin, administration, ธุรการ, general, info, class | timetable, class list, profile |
| planning | planning, plans, แผน, overview, outline, block plan, scheme | week-by-week outline, indicators |
| design / session plans | lessons, sessions, days, week 1, day 1, unit, หน่วย, activities, กิจกรรม | day notes, lesson steps |
| Thai core plans | แผนการจัดการเรียนรู้, lesson plan, core plan, แผนการสอน | ขั้นนำ / ขั้นสอน / ขั้นสรุป |
| assessment | assessment, การประเมิน, การวัดผล, rubrics, tests | rubrics, checks, scoring |
| evaluation | evaluation, reflection, review, audit | teacher reflection |
| delivery | delivery, teaching, in class, board, DQB | driving question board |
| resources | resources, materials, สื่อ, equipment, handouts, sources | lists of equipment or readings |
| templates | templates, forms, แบบฟอร์ม, blank | blank plan forms |
| class profile | class-profile, profile, class info, ข้อมูลนักเรียน | grade, schedule, counts |

3. The structure is **recognisable** when at least two entries match different areas, or one existing file plainly is a concept (e.g. a class profile). Otherwise see [No recognisable structure](#no-recognisable-structure).
4. For each concept, choose a location inside the matching existing area. When a concept has no matching area, place it in the closest existing area (e.g. agency audit in the planning area) rather than adding a new top-level folder, and mark it "new".

## Step 3: propose and confirm

Show the teacher the proposed mapping as a short table in plain words: concept, where it would go, and why (the folder or file that suggested it). Mark rows that create something new. Ask one numbered question with a recommended answer: "Use this layout? Recommended: yes." Accept corrections row by row. Skip the question when the teacher has already said they accept the proposed layout.

Propose the concepts the current skill needs plus a row for every area the folder already shows (e.g. an assessment folder → assessments); other skills add the remaining rows when they need them.

## Step 4: record the mapping

Write or update the `## Plugin layout` section of the top-level README, creating `README.md` if there is none. Keep every other line of the README exactly as it was; append the section at the end if it is new; if it exists, edit rows in place and never add a second section.

```markdown
## Plugin layout

Recorded by the thai-waldorf-science plugin after the teacher confirmed it. Skills read this table instead of guessing again; edit it freely.

| Concept | Location |
|---|---|
| class profile | `00 Admin/class-profile.md` |
| block and week plans | `01 Planning/` |
| session plans | `02 Lessons/` |
| assessments | `03 Assessment/` |
| templates | `Forms/` |
```

Locations are relative to the course folder, in backticks, without the course folder's name.

## No recognisable structure

When the folder is empty or nothing matches, offer the teacher's **default course template**: eight areas, each a top-level folder.

| Area | Holds (concepts) |
|---|---|
| `admin/` | class profile (`admin/class-profile.md`) |
| `planning/` | standards map, block and week plans, Thai core plans |
| `design/` | unit plans, session plans, differentiation |
| `resources/` | resources |
| `delivery/` | driving question board, preparation notes |
| `assessment/` | assessments |
| `evaluation/` | agency audit |
| `templates/` | templates (the four plan templates, copied in) |

Filenames are suggestive, not binding. Propose it as in Step 3: say in plain words that the folder is empty (or has no layout to follow) and list the eight areas with what each holds; ask "Use this layout? Recommended: yes." Record the mapping as in Step 4, one row per concept in the table above. Only `setting-up-class-profiles` creates the template, and only after the teacher confirms: every area folder at once (an area with nothing else to hold yet gets a one-line `README.md` saying what goes there), the class profile in admin, and the plan templates copied into `templates/`.

## Plan templates: the course's own come first

The plugin's four plan templates are its defaults:

| Plan kind | Plugin template (in the plugin's `references/`) | Cues that a course file is this kind |
|---|---|---|
| Thai core plan | `thai-core-plan-template.th.md` | core plan, lesson plan, แผนการจัดการเรียนรู้, แผนการสอน |
| block plan | `waldorf-plan-template-block.th.md` | block plan, แผนรายบล็อก, block |
| week plan | `waldorf-plan-template-week.th.md` | week plan, แผนรายสัปดาห์, weekly |
| day plan | `waldorf-plan-template-day.th.md` | day plan, แผนรายวัน, daily |

Every skill that fills a plan does this first:

1. Look in the location mapped to `templates` (Step 1; if none is mapped, there are no course templates). A file there is the course's template for a plan kind when its name or title carries that kind's cues.
2. **Course template found → use it**, even when it differs from the plugin's: its headings, labels, order, language and placeholders exactly. Keep the plugin's content rules for that kind (e.g. indicators verbatim, never inventing student data) wherever the course template does not say otherwise; where they differ, the course template wins.
3. **None found → use the plugin's template** for that kind.
4. Say in one line which one you used ("your course's own block plan form" or "the plugin's block plan template").

**Copying the templates in** (`setting-up-class-profiles` only): copy each plugin template into the templates location unchanged, under its plugin filename. Never overwrite or edit a file already there, and skip a plan kind the course already has its own template for; tell the teacher their own form is kept and will be used. When a found layout has no templates area, do not create one: tell the teacher the plugin's templates will be used and offer to copy them wherever they name.
