---
name: exporting-documents
description: >
  Turns one markdown document in a Thai Waldorf upper-school science
  teacher's course folder (Waldorf plans, Thai core plans, unit and cycle
  plans, preparation notes, run sheets, supporting-teacher briefs) into a
  print-ready A4 copy beside it: a self-contained HTML page in Sarabun /
  TH Sarabun New marked as Thai, printed from the browser. Asks for the
  delivery format once per course and records it; copies are one-way and
  never edited by hand, and a copy edited since export is kept unless the
  teacher confirms. Use when the teacher asks to print, export, make a
  printable or shareable copy, or turn a plan or note into HTML, Word or a
  doc. Do not use to write or change a plan, note or brief, or to fill a
  school's own Word or PDF form.
license: CC-BY-SA-4.0
---

# Exporting documents

You turn a document the teacher already has into a copy they can print or share. The markdown in the course folder is the single source of truth: you never change it, and you never write the copy by hand; the bundled renderer writes it.

## Keeping the teacher posted

Talk as a colleague in plain teacher language: "a printable copy next to your week 2 plan", "open it in your browser and print to A4", never script names, commands or file paths. Use the glossary terms exactly: Waldorf plan, Thai core plan, preparation note, run sheet, supporting-teacher brief.

## Step 0 — Route (silent)

1. Read `${CLAUDE_PLUGIN_ROOT}/references/course-layout.md` NOW and follow its Rules (private folders off limits; never rename, move or delete).
2. Decide what is asked:
   - **Export one or more named documents:** Steps 1–4, once per document.
   - **Write or change a plan, note or brief first:** that belongs to the skill that writes it (`planning-main-lesson-blocks`, `planning-subject-lessons`, `writing-thai-core-plans`, `preparing-to-teach`, `differentiating-for-learner-variability`). Say so in one sentence; export follows once the document exists.
   - **Fill the school's own Word or PDF form:** not something this skill does. Say so and offer an HTML copy of the plan instead.

## Step 1 — Find the document

1. The teacher names it ("my session 1 prep note", "the Thai core plan for day 3"). Find it through the Plugin layout's rows; never guess from folder names alone, and never look inside a private folder.
2. It must be a markdown file inside the course folder. Two equally likely matches: ask one question with a recommended answer. None: say plainly which document you could not find and where you looked, in teacher terms. Never write a copy of something that does not exist.

## Step 2 — The delivery format

1. Read the `Delivery format:` line in the README's Plugin layout section.
2. **None recorded:** ask once, with a recommendation: "Which format do you want for printable copies? Recommended: HTML (opens in any browser, print to A4). Word (docx) and Claude Docs come in the next version." Record the answer as `Delivery format: HTML` below the layout table (course-layout Step 4), keeping the README otherwise unchanged. Skip the question when the teacher already named a format in the request; record that one.
3. **A format named in the request** overrides the recorded one for this request only; do not change the recorded line unless the teacher says to.
4. **docx or Claude Docs** (recorded or asked for): in this version export HTML instead and say in one line that Word and Claude Docs copies come in the next version.

## Step 3 — Render

Run the renderer on the document, with the course folder as the working directory:

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/render_html.py" "<path to the document>"
```

It writes the copy beside the source with the same name and `.html`, and prints a JSON report: `out`, `written`, `edited_copy`, `unsupported`. Never open or edit the copy afterwards; to change the copy, change the source (through the skill that writes it) and export again.

- **Exit 3, `edited_copy: true`:** the existing copy was changed after it was exported (for example edited in the browser or Word), and was left as it is. Tell the teacher those changes would be lost, and ask: "Overwrite it from your plan? Recommended: yes, if the plan has everything you want." On yes, run again with `--force`. On no, leave it.
- **Exit 1, or `python3` not found:** say plainly that no copy was made and why, in one line. Never paste the document into the chat as a stand-in.
- **`unsupported` not empty:** those parts (a quote, a link, a code block, a picture, a nested list…) were kept as plain text. Name them in the reply in plain words.

## Step 4 — Reply

A few lines: which document, where the copy is in teacher terms ("next to your session 1 prep note"), how to print it (open it in a browser, print, A4, margins as set), any parts kept as plain text, and the format recorded if you just asked. When several documents were exported, one line each.

## Checklist before replying

- [ ] The source document is unchanged; the copy was written by the renderer, never by hand.
- [ ] The copy sits beside its source, same name, `.html`.
- [ ] The delivery format was asked at most once and recorded in the Plugin layout; a per-request format did not change the record.
- [ ] A copy edited since export was overwritten only after the teacher said yes.
- [ ] Unsupported parts and any failure are said plainly; nothing was pasted into the chat instead of a copy.
- [ ] No private folder opened; no file paths, commands or script names in the reply.
