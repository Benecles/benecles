# S3 triage notes

## Source-selection protocol

- Course scope comes from `course-map.json`; every lesson assignment matches its S0 syllabus line and learning outcome.
- Each S2 indexed section or legal article is an atomic source unit. CF/88 and the indexed statutes are assigned only by a specific article; no row assigns a whole legal instrument or book.
- The basic essential sources are Lenza, *Direito Constitucional Esquematizado* (`lenza-esquematizado-2022`) and Mendes & Branco, *Curso de Direito Constitucional* (`mendes-branco-curso-2023`). Each lesson has at least 5,000 body words of topic-matched primary material from these sources. If a future lesson falls short, its course-map entry must state a specific `thin_primary_reason`.
- Supporting material is capped at 10,000 words per item and 30,000 words per lesson. Oversized supporting atoms require a concrete `Specific need:` explanation in `why`.
- Newer shelf entries marked `missing` were not presumed or substituted. Supporting and primary rationales name the indexed unit and its connection to the S0 lesson topic.
- Dependency rows are the exact union of primary atoms belonging to each lesson’s direct S0 prerequisites.

## Aula 01 source boundary

Aula 01 uses Lenza §6.1 for the concept of constitutional review and constitutional supremacy, plus focused Mendes & Branco atoms 10-01, 10-02, 10-04, and 10-05. Mendes atoms 10-03 and 10-07 contain only heading text and were not treated as lesson content; 10-06 covers international law and is outside Aula 01’s syllabus scope.

## Lessons without a primary book chapter

None. Every lesson has at least 5,000 words from the two basic essential sources; no `thin_primary_reason` exceptions are used.

## Slide-source gaps preserved from S1

These S1 rows remain marked `missing`; the S3 checker reports them as warnings rather than failures:

- `slides-31` → `aula-31.html`
- `slides-32` → `aula-32.html`
- `slides-33` → `aula-33.html`
- `slides-34` → `aula-34.html`
- `slides-35` → `aula-35.html`
- `slides-36` → `aula-36.html`

The exact PIPE-4 failure demonstration is recorded in `policy-baseline-pipe4.txt`.
