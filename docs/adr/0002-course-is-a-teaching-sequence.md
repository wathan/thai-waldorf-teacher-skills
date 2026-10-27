# A course folder holds one teaching sequence, laid out as found

Skills work in the folder they are run in and treat it as one teaching sequence: a main lesson block named by its own subject (meteorology, not science) or a subject lesson, built from units of one topic each. They detect the existing structure and, once the teacher confirms, record the mapping of plugin concepts to files in a "Plugin layout" section of the course README, which later skills read instead of guessing again. Only when no recognisable structure exists do they offer the teacher's default course template, whose filenames are suggestive, not binding. Each course keeps its own copy of the class profile; the year plan is the one file outside the course, read only by year-level coverage checks from a path the teacher gives.

## Considered Options

- **Course = one class's subject for a school year, units = teaching sequences:** rejected. A main lesson block is a subject in its own right, and an anticipated route needs units to be the interchangeable topic pieces inside a block.
- **One fixed folder structure imposed on every course:** rejected. Teachers and schools already have layouts; the plugin must follow them.
- **A parent folder holding shared class profiles and year plans:** rejected. Skills would reach outside the folder they were run in, and courses would stop being self-contained.

## Consequences

- Skills never act on the folder name.
- A class profile change must be repeated in each course that class takes.
- Course-local templates override the plugin's, so another school's forms need no plugin change.
