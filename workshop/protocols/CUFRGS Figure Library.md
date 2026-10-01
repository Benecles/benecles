# CUFRGS Figure Library

The reference for what a figure on the site can be and how good it has to be. It was curated on 01/10 from the 784 figures live on the site (contact sheet: VIS-2, `codex/vis-2` → `work/vis-catalog/`). Use it in three ways:
- **Before drawing:** pick the genre whose job matches the lesson's point.
- **When gating:** hold the figure against its genre's exemplar.
- **When you need something new:** add a genre here first, with its exemplar.

A figure doesn't have to look like its exemplar. It has to be *as good as* it.

## The test (every figure, every gate)

1. **What does it do?** Name the verb: locate, count, measure, compare, decide, trace, read. If the only verb is "illustrates", it fails.
2. **Is it a real object or real data?** A month, a map, a petition, a vote, a ruler, a page. Not sentences poured into shapes.
3. **Delete the paragraph next to it.** If the figure now says nothing new, it was restating the text. It fails.
4. **Does it fill its frame?** Every mark carries content. One box on a 600×600 canvas fails. A deliberate single-object facsimile (the glossed page) passes.
5. **Craft:**
   - Labels sit in gutters, never on a line.
   - Colour means one thing, with a key when it isn't obvious.
   - Mono labels, course tokens, light and dark mode.
   - `breakscan` 0/0/0.

Facts from VIS-1 (`work/vis-forensics/`): every exemplar below was **built with a kit** (`maps.py`, front generators: 140–830 elements) and got its own run. Most failures are hand-typed inline SVG at 8–26 elements, made in bulk while writing lessons. **505 of 784 live figures have fewer than 30 elements.** New figures are generated from the kit (`ordenacoes-filipinas/tools/figkit/`), one component per genre.

## Genres and their exemplars

| Genre | Job (the verb) | Exemplar | Why it works |
|---|---|---|---|
| **Map** | locate, trace movement | ![](figure-library/dla-a01-s1.png) `dla-a01-s1` · ![](figure-library/dla-a02-s7.png) `dla-a02-s7` · ![](figure-library/met-index-s1.png) `met-index-s1` | Real geography. Fill encodes a variable with a key; flows carry dates; labels sit in the sea. You can answer "where, and when" by looking. |
| **Calendar / time grid** | count | ![](figure-library/pci-a07-s2.png) `pci-a07-s2` · ![](figure-library/pci-a07-s4.png) `pci-a07-s4` | The deadline is counted on a real month: holidays shaded, day 1 and the last day marked. The student does the count by eye. Best figure in its course. |
| **Document anatomy** | read a real form | ![](figure-library/pci-a01-s2.png) `pci-a01-s2` · ![](figure-library/met-a01-s3.png) `met-a01-s3` | The petição as a numbered form; the glossed page as text, gloss and commentary. The object the law produces, opened up. |
| **Tally / real data** | count, compare | ![](figure-library/dla-a03-s5.png) `dla-a03-s5` | ADPF 153: one dot per minister, coloured by vote. The decision as data, not as a sentence. |
| **Route / transit** | trace a sequence with branches | ![](figure-library/ctl-index-s1.png) `ctl-index-s1` | Stations are lessons; lines are the concentrated and diffuse routes; dashes are dependence. Every mark is a thing you can click and read. |
| **Timeline** | order, compare durations | ![](figure-library/tgc-a08-s8.png) `tgc-a08-s8` · ![](figure-library/dla-a01-s5.png) `dla-a01-s5` | A time axis with real events or regimes. The Latam variant pairs a map with a date ladder. |
| **Decision path** | decide | ![](figure-library/tdl-index-s1.png) `tdl-index-s1` · ![](figure-library/pci-a06-citacao-s2.png) `pci-a06-citacao-s2` | Each question has a named exit, and the exits are the legal consequences. Passes because the branches are real legal tests, not topics. |
| **Scale / ruler** *(new, kit component)* | measure | `ordenacoes-filipinas/specimen/figkit-controle-a01.html` (branch `figkit-a01`) | The parameter is a graduated rule and the act is a strip laid against it; past the limit is hatched. Controle's whole method (parâmetro × objeto) as an instrument. |
| **Case file** *(acceptable, not exemplary)* | classify | ![](figure-library/tdl-u14-s3.png) `tdl-u14-s3` | A real working form (ficha de imputação) with the active row highlighted per step. Passes only when the form is the one the student fills in. |
| **Section / strata** *(acceptable)* | read layers | ![](figure-library/dla-a01-s12.png) `dla-a01-s12` | A geological cut for layered law. It works when each layer is dated and named. |

## Anti-patterns (what fails, and the ids to learn from)

| Pattern | Examples | Why it fails | Fix |
|---|---|---|---|
| **Sentences in boxes** | ![](figure-library/ctl-a15-s5.png) `ctl-a15-s5` · ![](figure-library/tgc-a09-s14.png) `tgc-a09-s14` · ![](figure-library/ctl-a10-s17.png) `ctl-a10-s17` | The boxes restate the paragraph. Delete the text and the figure adds nothing. | Find the object the sentence is about (the statute, the month, the form) and draw that. |
| **Shape without data** | ![](figure-library/ctl-a01-s1.png) `ctl-a01-s1` · ![](figure-library/ctl-a04-s5.png) `ctl-a04-s5` | A triangle or mountains standing for "hierarchy". Swap the labels and it means anything. | Use an instrument that holds the relation: the ruler, a tally, a section with named layers. |
| **One thing on an empty canvas** | ![](figure-library/tdl-s20-s3.png) `tdl-s20-s3` | A single box on 600×600. | Either merge it into the previous panel or give it the object it points at. |
| **Real data, weak form** | ![](figure-library/ctl-a27-s11.png) `ctl-a27-s11` | The right content (virtual vs in-person sessions, 2024–25) set as text in boxes. | Bars or dots on a shared axis: the data is already there. |

## Genres not built yet (to add as the kit grows)

- **Statute cut:** an article with its caput, incisos and §§ as a real layout, with the relevant clause marked.
- **Docket / procedural clock:** a case's path with dates through the court, like the calendar but spanning years.
- **Who-decides matrix:** organ × act, with competence marked: STF, TJ, juízo singular.
- **Vote and coalition map:** the tally, extended to plenary splits over time.
