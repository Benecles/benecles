# CUFRGS Visual Genres (v1, 2026-09-25)

Owner: Claude (design authority, per Benecles). Codex builds to this; Claude refines.
Companion to `CUFRGS Writing Standard.md`. Code: `~/Documents/Codex/2026-09-23/you-h/work/latam-build/maps.py`, `contract-build/generators/kit.py`.

## The rule

**Pick the paper form that people already perfected for this information problem.** Don't pick it because it looks good. Before drawing any figure, finish this sentence: *"This is basically a ___."* Then borrow that object's grammar.

The site is one imaginary scholar's desk: every subject becomes the sheet humanity would have invented to understand that structure physically. It stays *paper* throughout, but each figure may think like a different object.

## Three levels, and when to stop

1. **Surface**: it looks like the object (graph paper, a folder). Cheap; use it freely.
2. **Structure**: the information is laid out the way the object lays it out (strata, a genealogy, a ledger). This is the default target for every figure.
3. **Function**: it *behaves* like the object. A blueprint drafts itself as you scroll; a dossier opens by its tabs; a palimpsest shows the old text under the new. Use this where the behaviour itself teaches the concept, and nowhere else.

Sometimes the right answer is good text on a good sheet. If the reader ends up studying the interface instead of the law, cut it.

## Question → genre

| The reader needs to know… | Genre | Grammar we inherit |
|---|---|---|
| **where**; how things vary across space | map, atlas plate, inset | borders, graticule, legend, routes, insets, scale (no relief) |
| **when**; periods | timeline, year strip on a map | chronology, periods, milestones |
| **what lies under what**; long-duration continuity | stratigraphic section | layers, unconformities, fossils (a continuity that survives the layers) |
| **what descended from what** | genealogy, stemma | branches; adopt / distinguish / narrow / overrule marks |
| **how parts make a whole** | blueprint, exploded patent drawing | numbered parts, leaders, sections, dimensions |
| **what is inside what** | anatomical plate, cutaway | systems isolated one at a time |
| **what happens if** | flowchart, decision table, form | nodes; conditions × consequences; boxes to tick |
| **what balances against what** | ledger | two columns, running balance, a total that does or doesn't close |
| **what must happen by when** | calendar, docket | dated boxes, deadlines, entries, disposition |
| **many actors at once over time** | score (musical, orchestral) | parallel staves, synchronised bars |
| **a network moving through time** | railway timetable, transit map | lines, stations, interchanges |
| **how a collegiate court split** | hemicycle, bench plan | one seat per judge, placed by vote |
| **everything that belongs to one matter** | dossier, case folder | tabs: Fatos / Questão / Decisão / Razões / Divergência / Depois |
| **what changed, while the old stays visible** | palimpsest, amended text | strike-through, new hand, old text faint underneath |
| **layers of norms over one object** | tracing-paper overlays | translucent sheets you can toggle |
| **navigating uncertainty** | nautical chart | safe channel, shoals (open questions), lighthouse (leading case), soundings |
| **how variables decide an outcome** | nomogram | aligned scales; a ruler across them gives the answer |
| **an atomic concept to recall** | index card | the Cartões deck; cards file and sort themselves |

## Physical ontology (keep it consistent across the site)

- **Primary source:** set in an official-document style (the `lex` block now; later a facsimile sheet).
- **A later change:** a different ink or hand, with the old text struck through and still legible.
- **One case:** a folder. **A line of cases:** a genealogy. **A course:** the desk (the index).
- **Geography:** always a real map, with current borders labelled "para orientação" whenever the story is historical.
- **Numbers:** a ledger or statistical sheet, never decorative.

## Settled constraints (Benecles, still in force)

- No glosas, margin comments or sticky-note commentary on the lesson text. Marginalia were tried and rejected.
- No decorative or idle motion, and no click easter eggs. Motion only where it *is* the behaviour (drafting, opening, growing), triggered by scroll or click, and it respects reduced-motion.
- No arrows crossing text. Leaders run from labels to places or parts, out into empty space.
- No scrolljacking. The scrolly steps drive the figures; the page scrolls normally.
- Every visual element must explain something (Writing Standard C15).
- Everything must work in light and dark mode and at 390 px, and survive print.

## Kit

- **Maps:** `maps.py`.
  - `map_defs()` (once per page), then `latam_map(fills, labels, pins, key, note, ...)` for a 600×600 Latin America panel.
  - Built in: graticule, sea names, waterlines and a scale bar. **No relief** (Benecles, 2026-09-25: shaded bands and hachures were both rejected; maps stay flat).
  - `flow(a, b, text)` draws a route; `inset(...)` draws a zoom box.
  - `Frame(name)` handles any other region: build it with `geo/build_frame.py NAME lon0 lon1 lat0 lat1 width tol`. The Aula 01 hero uses `Frame('atlantic')`.
  - Data: Natural Earth 1:50m (public domain). The relief pipeline (`geo/relief.py`) is retired; don't use it.
- **Tones:** `dif` (blue), `conc` (red), `mix` (violet), `grey`, `hatch`. Washes for fills, full colour for strokes and labels.
- **Figures:** `kit.py`, the 600×600 scrolly panels via `scrolly()`. Heroes can take a custom `hero_vb` (Aula 01 uses a 1080×787 map).



## Course architecture: one rule for every course (2026-09-27)

**Course → units → lesson pages.**
- **Unit** = a block of the syllabus, as the professor numbers it (Controle's blocos I–IX, Contratos' unidades 1–9, Delito's weeks). Units are what the course-front drawing shows.
- **Lesson** = one class or one syllabus topic, and one reading. Its label follows the syllabus: **"Aula NN"** where the syllabus is dated by class (Latam, Contratos, Controle), **"Unidade NN"** where it is organised by topic (Delito).
- **Pages per lesson:** one page when the lesson's content fits in about 4.5k words. Beyond that, split it into **two (at most three) full topic pages**, chained by the "Nesta aula/unidade" strip and the endnav (Delito unit 01: "I · A arquitetura" / "II · Os filtros sob carga"). **Never a hub page, and never a page under ~1.5k words.**
- **Course pages every course has:** the front (drawing first), a review page per exam, cartões with spaced repetition, and a reference page where the course has a statute (Contratos: artigos).
- **Naming:** `aula-NN.html` / `unidade-NN.html` for the first page, `…-NN-<topic>.html` for the second. The endnav always chains to the next lesson's first page.

## Course fronts (Benecles, 2026-09-27)

Every course index has the same macro-order:
1. **Compact title block:** kicker, title on at most two lines, a one-sentence deck.
2. **The course as one drawing, immediately, with no scrolling to reach it.** Pick its genre per the table above:
   - Controle: the blueprint ("planta");
   - Latam: the atlas;
   - Delito: the analysis flowchart itself (question per filter, "não" exits right to its result, "sim" goes down, units on the left of the question they answer; `work/delito-build/index_gen.py`). A canal-with-sluice-gates version was rejected as unreadable;
   - Contratos: the life of one contract (the parties are two lines that bind at the signature, one is swapped at the cessão, and they part at the torn edge; `work/contract-build/generators/front_life.py`).
   Every piece of the drawing links to its lesson. Mark the next exam's lessons with a thin colored bar, not a bracket.
   The drawing should encode the course's central mechanism, not list its units. Test: would the drawing still teach something with the labels removed?
   **Legibility beats cleverness (owner, 2026-09-27):** a first-time reader must get the drawing in about five seconds. Prefer the literal structure (flowchart, map, timeline) over a metaphor laid on top of it, and write what each mark means directly on the drawing ("assinam: o contrato nasce"). If it needs a legend to decode, it has failed.
3. The exam or review card and the jump links, beside or just below the drawing.
4. Units in syllabus order as the lesson-card grid.

Home page: no personal exam timeline, because the page must be shareable (`work/home-build/semestre.py` is kept but unused). Each course card on the shelf carries a miniature of that course's front drawing.

**Lesson sizing across courses:** a lesson is a full reading of one syllabus topic, roughly 2.5–4k words at book depth. A syllabus unit splits into lessons only where the content warrants it. No stubs, no hub pages. A course's units should look proportionate in its blueprint (Controle's 7–1–2 lopsidedness is a content problem to fix, not a layout one).

**Rejected:** print or PDF export of lessons (2026-09-27): flattening the live medium kills it.

## Build queue (next "level-3" pieces, by fit)

1. ~~**Stratigraphic section**~~ (done, Latam A01): constitutional strata (Haiti → Cádiz → the liberal-conservative pact → social constitutionalism → redemocratisation), with "fossils" for what persists (strong executive, broad rights). *Latam A01.*
2. **Genealogy:** the ECI line SU-559 → T-068 → T-153 → T-025 → ADPF 347, with a branch to Tema 1234; the amnesty line Barrios Altos → Almonacid → Gomes Lund → Gelman. *Latam A07–A09 and A03/A05.*
3. **Hemicycle:** ADPF 153 (7×2, named), OC-28 (5×2), Tema 1234 (unanimous). *Latam A03, A06, A09.*
4. **Palimpsest:**
   - CC art. 421 as amended by Lei 13.874/2019 (*Contratos A13*);
   - Bolivia's "por una sola vez" set aside by the TCP (*Latam A06*).
5. **Ledger:** Auto 176's money trail (*Latam A08*); the broken exchange balance in quebra da base (*Contratos A13*).
6. **Dossier with tabs:** one folder per leading case, as the case card on each lesson.
7. **Calendar / docket:** the T-025 orders (*Latam A08*); procedural deadlines in Controle.
8. **Transit map:** the course index as a network, with doctrine lines, case stations and interchanges.
9. **Form / checklist:** the six cumulative requirements of Tema 6 as a form the reader fills in against a case (*Latam A09*).
10. **Nautical chart:** open questions in a course (Tema 1234 embargos, the Gomes Lund × STF impasse).
