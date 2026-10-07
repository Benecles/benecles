# Benecles

Benecles turns law-course source material (slides, textbooks, case law, syllabi) into structured study guides that a student can read in one sitting, search, and use offline. It started as one student's study site for the UFRGS law course and has grown into a publishing pipeline plus the guides it produces.

**Live:** https://benecles.github.io/ordenacoes-filipinas/ (published as *Ordenações Filipinas · guias de estudo*; the content is in Portuguese)

|  |  |
|---|---|
| ![Course shelf on the home page](docs/img/home.png) | ![A lesson page: headline, thesis, timeline](docs/img/lesson.png) |

## What it is

Not a folder of notes: every course is built from named sources, split into lessons of about 15–25 minutes, drawn with figures made for that lesson, and checked before it ships.

- **Who it is for:** law students working through a university syllabus.
- **The problem:** course material arrives as slide decks and long books, and the student has to rebuild the argument alone. Summaries rarely say which source a claim comes from.
- **What a guide gives you:** one syllabus topic per lesson, the question each decision answers, redrawn diagrams, review questions, and the source behind each claim.

## What is published

| Course | Pages |
|---|--:|
| Controle de Constitucionalidade | 37 |
| Teoria do Delito | 42 |
| Direito Constitucional I | 40 |
| Teoria Geral dos Contratos | 22 |
| Processo Civil I-a | 20 |
| Metodologia Jurídica | 13 |
| Direito Latino-americano | 12 |

187 pages and about 1.15 million words in seven courses, with 919 inline SVG figures. Pages include lesson texts, course fronts, review pages and cards. Processo Civil is being rebuilt from scratch as the reference course; the others are being brought up to the same standard one lesson at a time. Counts are taken from the files in this repository.

## How it is built

- **Static build.** `tools/build_course.py` reads Markdown sources and writes standalone HTML plus `catalogue.json`, `search-index.json` and `provenance.json`. Provenance records source names, input hashes, counts and every logged transformation; the build fails on unresolved links, diagram markers or a miscounted correction. See [tools/README.md](tools/README.md).
- **Source discipline.** Source PDFs and books are not distributed here. Where a slide or author takes a debated position, the guide labels it as that source's position. The public editorial page explains source and version decisions and where review stopped.
- **Search and catalogue.** Per-course search indexes and a catalogue, generated at build time. Search is an enhancement; reading and links work without JavaScript.
- **Offline.** A service worker and a generated manifest of 280 files let a visited course be read without a connection. CI checks that the committed tree equals what `tools/offline_build.py` produces.
- **Figures.** Diagrams are drawn per lesson as instruments (a deadline on the real calendar, a seating chart, a balance), not as stock flowcharts. Mermaid diagrams are compiled to SVG at build time and ship with a collapsed text list of the same relationships.
- **Accessibility.** `lang="pt-BR"`, ARIA state on controls, a light and a dark theme, and graceful degradation without JavaScript.
- **Quality checks.** `tools/check_all.sh` runs on every push and PR: front pages must regenerate byte-identical, lesson links and register data must resolve, and a page-anatomy check flags loose prose and late panels. The private workshop adds a house-style check, a quotation check (every quotation must be found in the sources), a prose linter for padded writing, and a layout scan at desktop and phone widths.

## History and process

386 commits since 2026-09-05, 131 merged pull requests, one issue per change. [ISSUES.md](ISSUES.md) lists each merged change; `changelog.json` feeds the patch notes on the home page. Development is assisted by AI coding agents; the agent instructions are in [AGENTS.md](AGENTS.md). AI is part of how the guides are built, not a feature the reader uses.

Design process and earlier directions are kept, not hidden:

- `specimen/` shows each house component in every state.
- `experiments/` holds earlier material studies; `prototype-folio.html`, `index-alt-*.html` and the standalone pages at the root are the original prototypes, kept at their original URLs.
- `VISUAL_CRAFT_NOTES.md` records the design process.

## Status

Early stage: a student-built project, not an incorporated company, with no paying users. No usage figures are published here. There is no license; all rights are reserved, and nothing here grants reuse of the content.

## Running it

Open `index.html`, or serve the folder (`python3 -m http.server`). Rebuilding a course needs the private source files, so `tools/build_course.py` will not run without them.
