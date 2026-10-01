# S3 triage notes

## Source-selection protocol

- Course scope comes from `course-map.json`; each lesson uses its exact S0 syllabus line, learning outcome, and declared prerequisites.
- Each S2 `index.json` entry is the atomic source unit. When S2 split a chapter at a section boundary, the indexed section ID is used; no row assigns an entire book.
- Lenza, *Direito Constitucional Esquematizado* (2022; `lenza-esquematizado-2022`) and Mendes & Branco, *Curso de Direito Constitucional* (2023; `mendes-branco-curso-2023`) are the priority base books. A book chapter is primary only when it directly covers the lesson scope; when neither priority book covers that scope sufficiently, one directly applicable chapter from an available supplementary book may be primary. Other chapters remain supporting.
- Newer shelf entries marked `missing` were not presumed or substituted. Source rationales cite the precise indexed chapter/section topic and course line.
- Dependency rows are the exact union of primary chapter rows belonging to the lesson’s S0 prerequisites.

## Lessons without a primary book chapter

None. Every lesson has at least one primary book chapter in the current triage.

## Slide-source gaps preserved from S1

These S1 rows remain marked `missing`; no substitute or invented deck was added:
- `slides-31` → `aula-31.html`
- `slides-32` → `aula-32.html`
- `slides-33` → `aula-33.html`
- `slides-34` → `aula-34.html`
- `slides-35` → `aula-35.html`
- `slides-36` → `aula-36.html`
