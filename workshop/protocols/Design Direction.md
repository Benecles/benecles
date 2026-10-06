# Design Direction (v1, 2026-09-29)

Owner: Claude (design authority). Companion to `Visual Genres.md` (which paper form to pick) and `Writing Standard.md` (prose).
This document says **how things should look and feel**, so builders (Sol, Luna) can design with real freedom and land close to done. It is taste plus hard constraints. Where it says *should*, use judgment; where it says *must*, don't deviate without asking Claude.

---

## 1. The feel, in one paragraph

A scholar's drafting desk. Paper, ink, a grid underneath, two accent inks. Everything is *drawn*, never decorated: every line on a figure means something, and the page feels made by one careful hand. It's calm (motion only when something is being drawn or revealed), precise (aligned, measured, consistent), and generous (big type, air around things). The home page is the benchmark for elegance: if a page looks busier or clunkier than the home page, it isn't done.

## 2. The system (must)

- **Tokens only.** Colours come from CSS variables: `--paper`, `--paper-2`, `--ink`, `--ink-2`, `--muted`, `--grid`, `--grid-major`, `--conc`/`--conc-wash`, `--dif`/`--dif-wash`, `--mix`/`--mix-wash`. Never a hex or a named colour in a page or figure. Dark mode then works for free; check it anyway.
- **Colour means something.**
  - `conc` (orange) is emphasis, exits, the thing being tested, the exam.
  - `dif` (blue) is the contrasting or second term, and the answer.
  - `mix` (violet) is a third category, used sparingly.
  - Grey (`--paper-2` fill, `--ink-2` or `--muted` stroke) is inactive or out of focus.
  - A figure uses at most **two accents**. If you want a third, the figure is doing too much.
- **Type roles.**
  - **Mono**, uppercase, letter-spaced ~.08–.1em, 10–13px, for structure: labels, kickers, axis names, figure headers.
  - **Sans**, weight 600–750, for the main noun of a box or node.
  - **Serif** for reading prose and italic geographic labels (seas, regions).
  - **Hand** (`t-hand`, serif italic) for one-line annotations.
  - In SVG, no text is smaller than **11px at the 600px panel size** (it shrinks on phones).
- **Paper objects.** Square corners, a 1.5px ink border, and the house offset shadow `6px 6px 0 var(--grid-major)` on sheets and cards. Nothing else: no gradients, no blur shadows, no rounded pills, no glassmorphism, no icons or clip art.
- **Motion.** Only `pop`/`draw`/`fade` on reveal, and the scrolly panel changes. One slow ambient loop is allowed at most, and rarely (the owner liked a slow idle flag). Everything respects `prefers-reduced-motion`. No arrows animating across text.
- **Phone.** 390px wide with no horizontal page scroll, ever. A figure that is wide by nature (a timeline, a canal) needs a **vertical phone version** (see Delito's front flowchart), not a sideways scroll, unless it's a map, where pan and zoom-by-width is fine.

## 3. What Claude keeps fixing (read this as a checklist before every gate)

1. **Labels overflowing their box or clipped at the edge.** Measure: at 600px, mono 11px is ~7px per character. Use `maxw` in `kit.T` and fix every WARN. Long labels get shortened, not squeezed.
2. **Labels colliding** with each other, with lines, or with pins. Map labels sit *above* the land with a paper halo (`maps.HALO`). Move labels into open space; add a leader line if it's far.
3. **Figure captions and info strips that don't wrap** on phones: they widen the page. Everything textual inside flex rows needs `min-width:0` and wrapping.
4. **Boxes-and-lines by default.** Before drawing labels in boxes joined by lines, ask the genre question again. A flowchart is right only when the content *is* a decision sequence.
5. **Metaphor over structure.** A canal with sluice gates for the theory of crime was rejected: the reader has to decode it. Draw the literal structure and write the meaning on it ("não → fato atípico").
6. **Ornament.** Sea monsters and dragons were rejected; so was relief shading, twice. No decorative flourishes.
7. **Legends people must decode.** If a mark needs a legend, label the mark itself instead.
8. **Visible sourcing** in figures or cards: page numbers, "segundo o material", author-page parentheticals. Sources go in hidden `src()` / `data-src` only.
9. **Density.** More than ~7 labels in one panel, or more than 3–4 panels in one figure. Split it, or cut it.
10. **Things that look different for no reason.** The same component must look the same everywhere: exam cards, lesson cards, bets, figure frames, chapter heads.

## 4. D1: the course front (the frame is standard; the drawing is each course's own)

Every course front renders through **one** template, in this order:

1. **Top bar:** `← Ordenações` · code · UFRGS · 2026/2 · ⓘ · Modo noite. (Exists; keep it.)
2. **Title block:** kicker line in mono (`Guia de estudo · <área> · N aulas · <Prof.>`); the course name as h1 (≤2 lines, the existing clamp size); **one-sentence deck** (≤62ch), which says what the course *is about*, not what the page is.
3. **The course drawing,** the course's own figure on a paper sheet at the content width (max 1180px), with the house shadow. It must be clickable to lessons, readable in five seconds, and have a phone version. Courses that don't have one yet (Const I, Processo, Metodologia) get a proposal at the gate; Claude may redraw.
4. **Exam row:** the exam card (≤520px) plus the review link if a review exists, and "Continuar: <aula>" when there's a saved place. Past exams show nothing, or the next exam.
5. **Lessons:** a section head ("Aulas"), then a grid of **unit cards** (`auto-fill, minmax(320px, 1fr)`). Each card holds a mono unit label, a sans unit title, one line of description, and its lesson links as rows (`Aula 03 · <title>`). Titles must match the lesson pages' own titles. Supplements are marked as complementary, in the same card style.
6. **Bibliografia** (`id="bibliografia"`), at the bottom: the syllabus bibliography verbatim in ABNT style, split into *Básica* and *Complementar*, in serif, small, plain. Nothing else.
7. **Endnote.**

The **ⓘ card** stays a short list (the syllabus books, Moodle materials, key decisions) and ends with a link, `ver bibliografia completa →`, to `#bibliografia`.

Style: the rhythm and spacing of the Latam and Delito fronts, which are the best current ones. The home page is the elegance benchmark.

## 5. D2: the plate (a full-bleed set piece)

**What it's for:** once or twice per lesson page at most, the text-and-figure rhythm breaks for one big thing that *needs* the whole screen to be understood: a map of a journey, a timeline across centuries, a whole-course panorama. If it would work at half size, it's not a plate; use a normal figure.

**Contract (must):**
- A `kit.plate(title, svg_inner, caption, viewbox='0 0 1600 900', phone_svg=None, aria=...)` component. It renders a `<figure class="plate">` that breaks out of the text column to the full viewport width (`width:100vw; margin-left:calc(50% - 50vw)`). On desktop its height is ~70–85vh (never taller than the viewport). The paper sheet has top and bottom rules and no side border, so it reads as a spread.
- A mono title row at the top-left and a one-line serif caption at the bottom. Both are short.
- **Static by default.** At most one reveal animation, e.g. a route drawing itself in order once when the plate scrolls into view. No scrolly inside a plate.
- **Phone:** use `phone_svg` (a portrait-proportioned version, simplified) when the desktop drawing would get too small. Maps may instead keep their proportions at full width.
- **Placement:** only between chapters, never inside prose. Precede it with a chapter whose text sets it up, and let the next chapter build on it. Aim for the rhythm scrolly-and-text → plain text → **plate** → text → scrolly.

**Maps as plates** reuse `latam-build/maps.py`: `Frame(name)` for other bounding boxes (`geo/build_frame.py NAME lon0 lon1 lat0 lat1 width tol`). Rules:
- **No relief.** Graticule and water lines only.
- Place names above the land with the halo. Sea names go in open water.
- Journeys are drawn as **dated flows** (`Frame.flow`), stops as pins labelled `City · century or year · what happened` in ≤4 words.
- Colour only the places that matter to the lesson.
- **Content only from the lessons.** If a stop or date isn't in the lesson text, it isn't on the map.

**First plate: Metodologia's journey of the ius commune.** It probably runs Bologna (the glosadores) → the Iberian peninsula (the reception, humanism) → Salamanca → the Indies (Lima, the colonial courts, casuísmo) → Coimbra → Brazil (the 1827 law schools), but the lessons decide the actual stops. Spread it across the lessons where each stop is taught, possibly as one plate per lesson showing "you are here" on the same route.

## 6. D3: the figure inventory

For every figure on the site, give one line: course · page · current form · **boxy? (yes/no)** · proposed genre from Visual Genres · why (≤12 words). Group by course and mark the exam-scope lessons. Don't rebuild anything until Claude picks.

## 7. D4: Modo avião phrases

While saving, rotate calm Portuguese lines every ~2.5s instead of "N de M páginas", in the site voice, short, with no emoji and no jokes that age. For example: "Guardando as aulas para ler sem internet…", "Copiando os desenhos…", "Quase lá…". Keep an `aria-live` status that reports completion. Success and failure messages stay factual.

## 8. Gates (what to hand Claude)

For each D item: a staging URL (`work/staging/...`, served at `python3 -m http.server 8767`), a list of pages changed, and **your own screenshots** at 1280 and 390, light and dark, of each new or changed figure or front, plus an overflow check (no page wider than the viewport, no SVG text past its box or viewBox). Say what you're unsure about. Claude polishes and ships; don't push.
