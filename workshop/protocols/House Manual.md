# House Manual

**For lesson writers.** Version 1, 2026-10-07. Read this instead of the Writing Standard, STYLE.md, Design Direction, Visual Genres, Visual Casting, the Figure Library, the PROC-R2 rulings and the FLIGHT-LOG. Those stay as references for the long reasoning; every rule a writer acts on is here, in the order you need it. Tags give provenance: [F-0NN] FLIGHT-LOG row, [WS B3] Writing Standard section, [R14] PROC-R2 ruling, [DD] Design Direction, [VG] Visual Genres, [VC] Visual Casting, [FL] Figure Library.

**Precedence.** A FLIGHT-LOG row dated after this manual outranks it; otherwise this manual wins over the older documents. Settled conflicts: Appendix B.

**The reader.** A UFRGS law student mid-semester, often the week before an exam, who wants the right answer and the reason for it, so they can handle a variation. Every sentence gives law, a reason, or the law working on facts. [WS 0]

---

## 1. What a lesson is

### 1.1 Purpose and size
- **One question, one sitting: 2,500–4,500 words** (15–25 minutes). Past 4,500, split into two (at most three) full topic pages at the seam where the question changes, chained by the "Nesta aula" strip and the endnav. No hub pages, no page under ~1,500 words, never cut content to hit a number. *Why:* a page answering two questions gets read for neither; stubs waste a click. [WS A0, VG "Course architecture", R10]
- **Why before what.** Show the mechanism (who acted, under which rule, with what effect) before the label. *Why:* only the reason transfers to the exam's variation. [WS D preamble, STYLE.md]

### 1.2 Plan first
- **Write `compendium/<lesson>/blueprint.md` from `protocols/templates/Lesson Blueprint.md`,** modelling each field on the reference blueprint (Controle `compendium/aula-01/blueprint.md`, its Method notes) and the live Controle Aula 01 page with its `REF ·` comments. Copy the reasoning, not the accidents. *Why:* models write fluent paragraphs and incoherent documents, and agents who copied without knowing why copied the mistakes too. [WS A, F-012, F-024]
- **Add a two-line addendum naming the source blocks (passage + page) and the thread.** *Why:* both are planned, not found mid-draft. [R11]
- **The scope fence is planning only:** it tells you what to leave out, silently. [F-020]
- **Re-plan instead of drifting;** the plan must describe the text that exists. [WS A7]

### 1.3 The thread
- **One real fact pattern carries the lesson,** from the exam bank where possible. It opens the lesson, returns in every chapter with each concept shown working on it, and the closing exercises turn on it. Cut "por exemplo, a parte afirma…" stand-ins. *Why:* abstract exposition gives the exam nothing to grip. [F-030a, WS A5]
- **Carriers are real** (an article, a case, a statute, an exam's facts). A hypothetical only as a variation on real text, like Controle Aula 01's Lei A/B on art. 5º, XVI. *Why:* "Comunidade C" was rejected while real material existed. [F-022]

### 1.4 Anatomy, top to bottom
1. **Hero:** kicker (course · code · UFRGS · 2026/2); h1 in at most two lines; a one- or two-sentence deck saying what the lesson lets the reader do; optional hero figure; title block whose **Leitura ≈ N min equals the front's clock**. *Why:* a hero that disagrees with the front looks careless. [F-013, DD D1]
2. **Bet** ("Antes de ler") in the first chapter: a real case, the rule at stake, options, the court's answer revealed. *Why:* committing first makes the explanation land.
3. **Chapters:** `section.chapter`, numbered h2 naming the content, and a `p.lede` that **states the chapter's question, not its answer**. *Why:* an answer in the lede is restatement. [WS D10.3, C8; B9]
4. **Prose** inside `.longform` or `.wide`, never a loose `.prosa`. *Why:* it renders off the grid. [F-014]
5. **Source blocks** where the argument rests on a source (Section 3).
6. **At least two SVG figures,** alternating figure sections with prose-only ones. [F-028a, Blueprint A6]
7. **Closing exercises** (`.quiz`, "Responda antes de abrir") from the lesson's own exam-bank questions first. Each prompt is self-contained; each blueprint trap is tested once; each item names its exam (year, and the setter when it isn't the course professor). *Why:* the exercises prove the lesson worked. [R12, R5, F-021]
8. **Endnav** to the next lesson's first page.

**End on substance:** the last chapter ends on its most exam-relevant application, then the exercises. No recap, no "Para a prova" list. [WS D10.3; B10]

### 1.5 Pacing
- **Concrete, rule, near miss:** a situation (parties, object, date, money), the rule with its article, then one fact changed and the result flipped, at least once per major rule. *Why:* exam questions are near misses. [WS B3]
- **Alternate density** (after a three-condition rule, a case; after two cases, the principle); put the hardest idea after its prerequisites and beside its figure; spend words where the exam does. [WS B7]
- **Long prose (3–6 paragraphs between figures) for arguments only:** a controversy, a leading case's reasoning, a history that explains the rule. Paragraphs under ~220 words. [WS C13]
- **Worked cases:** facts → question → rule → application in full sentences → result. *Why:* the step where facts meet the rule is what exams test. [WS C14]
- **At most ~5 cross-lesson links,** plain, where the text hands off a concept. [F-020, WS C15]

---

## 2. Prose

### 2.1 Craft
- **Talk about the law, not the discourse;** don't announce, do it. "O contrato entre ausentes se forma quando a aceitação é expedida (art. 434)." [WS B1]
- **Define each term of art in the sentence where it first appears,** and write the step that seems obvious. *Why:* the writer who just read three treatises forgets what the student lacks. [WS B2]
- **Actors as subjects, actions as verbs; old before new; the article, exception or result at the end.** Keep subject and verb together. *Why:* the stress position is what gets remembered. [WS B4, C1, C2]
- **One job per paragraph, one method** (definition, example, cause, contrast, enumeration, application), **lengths that follow the job.** *Why:* equal-length, equal-shape paragraphs are the surest machine tell. [WS B6, C4]
- **Specific within two sentences:** an article, a named case with court and year, numbers, parties, a date. [WS C5]
- **Contested points get names, reasons and the prevailing view.** *Why:* "parte da doutrina" hides what the reader needs. [WS C6]
- **Hedge once, where the doubt is, with its cause;** state settled law flatly. [WS C7]
- **Stable exact terms** ("resolução" never drifts into "extinção"); plain words otherwise ("usar", not "utilizar"; no "realizar / efetuar / proceder à"); no juridiquês ("outrossim", "insta salientar", "in casu"); exam Latin kept and explained. *Why:* in law a synonym is a different category. [WS B5, B9, C11]
- **Tone:** a good professor after class: exact, economical, occasionally dry. Evaluation belongs to named sources. [WS B8]
- **Lists only for parallel items** (requisitos, hipóteses); reasoning stays in prose. *Why:* bullets delete the "porque… salvo se". [WS C9]
- **Headings inform;** no puns or taglines. [WS C8]
- **No em dashes, no exclamation marks; colons only before a list, definition or quotation;** rhetorical questions only as headings or a case's literal question. [WS C10]
- **Beside a figure, say what it proves, never what it shows.** *Why:* "A imagem é dura…" is slide narration. [WS C12, F-012]

### 2.2 No backstage
- **The page never talks about its making:** no "os slides", "o professor disse", "materiais da disciplina", "nesta leitura", "relatada por Lenza", locator tables, section codes, "blueprint". slop_lint hard-bans these. *Why:* provenance lives in the ledger and the `.fonte` header. [F-019, WS E3]
- **If the source doesn't support a claim, leave it out without saying so.** *Why:* on-page caution is writing to the gate. [F-021, WS E4]
- **State each trap once, where it bites.** *Why:* Aula 08 restated one trap six times. [F-021]

### 2.3 Hard bans [WS D1–D8]
- **Negative parallelism** ("não é X, é Y", "não se trata de X, mas de Y", "mais do que X, Y"), unless both halves carry law. Test: delete the "não" half; if no law is lost, it goes.
- **Puffery:** "papel crucial", "pedra angular", "marco", "revela-se essencial", gerund tails ("…, evidenciando a importância de").
- **Meta-text:** "vale ressaltar", "é importante notar", "como vimos", "nesta aula veremos", "em conclusão". One per lesson each: "em suma", "ou seja", "dessa forma", "nesse sentido", "além disso", "ademais".
- **Slogans, moral closers, staged reveals.** House tics, one per lesson: "A pergunta é se…", "Tudo depende…".
- **Vague attribution** ("há quem diga") when the source names who; "por um lado… por outro" without resolution.
- **Reader address** ("Perceba que", "Repare:"), except instructions in exercises.
- **Intensifiers:** three per lesson in total; terms of art don't count.
- **Emoji, decorative rules, headings holding only headings, plain bold.**

*Why for all:* each is machinery standing in for information. Editing order: maximize propositions per sentence; impose no structure the content didn't ask for; never manufacture nuance; allow asymmetry; explain by mechanism; judge tells by density; never "humanize" with fragments or fake opinions. [WS D preamble]

### 2.4 Density limits, per 1,000 words [WS D9, BACKTEST.md]
| Pattern | Limit | Why |
|---|---|---|
| Negated inference ("não basta / substitui / resolve / prova…") | ≤ 0.5 | Our worst tic: 18× human doctrine on live pages, ~25× in Luna drafts. Say what the decision did. |
| "Não é X" frames | ≤ 2.0 | Each still passes the delete-the-"não" test. |
| Colon reveals | ≤ 5.6 | Human ~3; 40% of Luna drafts over. |
| Triads ("X, Y e Z") | ≤ 12.3 | 60% of Luna drafts over. |
| "em vez de / ao invés de" | ≤ 1 | 13–15× the human rate. |
| AI vocabulary basket | ≤ 5.2 | |
| Stance adverbs / "não X, mas Y" | ≤ 1.2 / ≤ 1.6 | Humans break these too. |
| Stacked questions, same-opener runs, five uniform paragraphs | any run | Model-only patterns. |

**Luna's measured habits are triads, colon reveals and negated inference;** it produces almost no generic AI vocabulary, so English word lists miss it.

### 2.5 The five pathologies (hard bans) [WS D10]
1. **Fake disagreement:** a view nobody in the sources holds, staged to be refuted.
2. **Circular cause:** the "porque" restates the effect. Test: does the reason add a fact, rule or actor?
3. **Unnecessary restatement:** if deleting it loses no proposition, delete it.
4. **Excessive sectioning:** a section exists when the question changes.
5. **Reflexive qualification:** a caveat that changes nothing is cut.

**Patch spans, never rewrite whole drafts.** *Why:* full rewrites flatten variation and break what was right. [WS D preamble]

---

## 3. Sources

### 3.1 The source block
- **When a book, decision, statute or treaty says it better than we can, the prose stops and a `.fonte` opens there,** as long as the passage earns (a paragraph, or several hundred words of a key stretch). Prose resumes without "como vimos". *Why:* the lesson should read as a collage of the assigned reading's own words set into our explanation. [WS E2, Processo R2 brief]
- **`.fonte` is the only source component** (it replaced `.lex`, `blockquote.law`, `.julgado`, `.source-block`). Markup: `specimen/casa.html`.
- **The bar colour says what the source is to the argument:** `.fonte.dec` **blue** = a statute's or decision's operative words; `.fonte.lim` **orange** = a limit; plain `.fonte` **ink** = a book or doctrine. *Why:* the same legend as the marks and figures. [WS C10b, casa.css]
- **At least 4 blocks per lesson, at least 1 doctrine block** from the assigned reading or treatise, whose decisive passages the argument walks through. *Why:* 11 Processo lessons passed every lint with 6 blocks among them. [F-028a, F-029a, R10]
- **`.key` inside a block** marks the few words the prose leans on. [WS E2]
- **`.fonte.resumo` for our summary of a decision:** no blockquote, no quotation marks; `.corpo` for the body, `.tese` for the result. *Why:* our words must never look like the court's. [casa.css, CEO.md 06/10]

### 3.2 Quote once, verbatim, by script
- **The governing article appears once, verbatim, in a `.fonte.dec` where the lesson first needs it;** afterwards the prose applies it without renaming it. house_check's warning at >5 mentions of one article is a fail. *Why:* art. 356 was named 32 times in one lesson. [F-029a, R10]
- **A script pastes every quote from the source file by locator** (source id + page or article); you pick the passage and the cut. Never type a quote or quote from memory. *Why:* models drop words silently, and the content filter refuses to retype statutes (which aren't protected: Lei 9.610/98, art. 8º, IV). [R14, WS E2]
- **Mark every cut "[...]".** [R14]
- **Statutes by article, never whole codes;** pull missing ones with `tools/pull_source.py`. [F-002, R6]

### 3.3 Attribution, translation, paraphrase
- **Attribution only in the block header:** author, *work*, chapter/page; or court, case, date. No "segundo X" lead-ins, no pages or footnotes in our prose. [WS E2, E3]
- **Prose may name who holds a contested position;** that is content, not credit for a quote. [WS C6; B11]
- **Non-Portuguese passages stay in the original** with a hidden `.tr` ("Tradução nossa") and a `data-tr` toggle. *Why:* the source's words are the evidence; the translation is our help. [WS E2]
- **Quotes are Preserve mode:** never edit one to pass a lint. [STYLE.md]
- **Paraphrase from understanding:** read, close, write your own claim in your own order, then check it. Depth comes from the compendium, never the model. [WS E1, E4]

---

## 4. Inline marks

One vocabulary at the "proposto" intensity. Specimen `specimen/casa.html`; load `assets/casa.css` and `assets/casa.js` on every lesson. [WS C10b, R10]

| Mark | Use | Cap | Why |
|---|---|---|---|
| `.held` blue bold | What the court or law decided | ≤ 1 per paragraph, ~6 words (lint fails > 8) | Blue = decided, site-wide |
| `.limit` orange bold | The limit or trap; what the decision did not do | same | Orange = limit, site-wide |
| `.mark` highlighter | The one sentence per chapter worth memorising | ≤ 1 per chapter | Scarcity carries the meaning |
| `.term` + `data-def` | A term of art, defined from the lesson's own sentence | as needed | The answer appears in place |
| `.org` small caps | A court or organ, first mention | first mention | Structure without bold |
| `.tab` | Dates, votes, sums | as needed | Figures align |
| `.runin` | A ≤ 3-word run-in head in a parallel run ("Peru, 1823.") | | Structure, not emphasis |

- **At least 3 `.held` / `.limit` / `.term` per lesson,** each on a real holding, limit or term. [F-028a]
- **No plain bold** in running text; run-ins use `.runin`. *Why:* the two coloured bolds carry meaning; generic bold dilutes it. [WS D8, marks_lint; B4]
- **Never colour ordinary prose or set colour inline;** never mark for decoration. [C10b]
- **No `.art` chips;** write "art. 5º, XVI" plainly. *Why:* dense chips read as noise. [B5]
- **Italic** for foreign terms, case names and works.
- **Refused:** party colours in comparisons (they collide with blue = decided); sidenotes and glosas (no margin in the column, and source talk outside the block). [C10b, WS C15]

---

## 5. Figures

### 5.1 Instruments, not diagrams
- **Labelled boxes joined by arrows fail.** Ask first: what does the reader do with it, and what do they know afterwards that the text didn't give them? "Look at it" is not an answer. [VG v2]
- **Pass one of three ways:** **the real object** (a statute's layout, a petição, a dispositivo, eleven plenary seats, a docket); **an instrument** (the reader sets an input and the law answers: pick the legitimado, count to a quorum); **a measured picture** (position, length, count and time carry meaning: a 15-day prazo on the real month). [VG v2, F-031b]
- **Name the verb:** locate, count, measure, compare, decide, trace, read. "Illustrates" fails. [FL test 1]
- **Study `specimen/instrumentos.html` before drawing:** the deadline counted on the real April 2015 calendar, and the litisconsórcio seating chart with the exam's parties seated and the trap dashed in orange. Each is the real object plus the rule as the question the object answers. [R18]

### 5.2 Casting
- **Cast each figure in the blueprint (A7)** from the claim it carries: the move; at least three candidates from different form families in the course's world; the four tests; the choice and the sentence that sells it; the sheet described with real labels and numbers. [VC]
- **The four tests.** *Swap:* would relabelling fit another lesson? Reject. *Ledger:* has this course used the form for another idea (`work/figure-qc/casting-ledger.md`)? Only one argued callback. *Object:* is this lesson's article, case or number on the sheet? *Verb:* what does the reader do? [VC]
- **Borrow the paper form people perfected for the problem** ("this is basically a ___"): calendar for deadlines, hemicycle for a split court, ledger for balances, genealogy for lines of cases, palimpsest for amendments, map for place. Uniqueness lives in what is depicted, consistency in how it's drawn. [VG table, VC]
- **The writer draws the lesson's figures, in the same context.** [Source Pipeline S5]
- **A redo keeps its predecessor's claim.** Write the claim in one line and check the drawing shows it unaided. [F-025]
- **Legibility beats cleverness:** draw the literal structure and write meaning on the mark ("não → fato atípico"); no decoding metaphor, no legend where a label would do. *Why:* the sluice-gate canal was unreadable. [DD §3]

### 5.3 What fails
- **A statute as figure.** A quoted article is a `.fonte.dec`. [F-031b]
- **Text in ruled cells.** The delete-every-word test: remove every text node; if a month, a seat plan or a stack of pages is left, it's an instrument; if an empty grid is left, it's a table and belongs in HTML. Put the result and the crop in the PR. [F-026, R17]
- **Restating the text:** delete the adjacent paragraph; if the figure adds nothing, it fails. If a table beside it says the same, one goes. [FL test 3, F-025]
- **Shape without data, one thing on an empty canvas, ornament, relief shading, arrows across text.** [FL, DD §3]
- **Invented precision:** draw only the precision the text has; check every sum before charting. [F-007, F-008]

### 5.4 The frame
- **Content fills the frame.** Crop the viewBox to the drawing + ~16 units; a one-panel scrolly takes the drawing's proportions. At least 10 of 16 cells of a 4×4 grid hold a mark; fill the empty arms of T and L shapes with the verdict, the facts or a second object. *Why:* Aula 01 shipped half blank, and its type shrank. [F-016, F-017, FL test 4]
- **Labels at reading size, in clear space:** no SVG text under 11 px at the 600 px panel; mono leading ≥ 14 px, serif ≥ 18 px; lines skip text; leaders run into empty space. [DD §2, F-006]
- **Two accents at most,** meaning what they mean in the text: blue = answer/decided, orange = trap/tested term, grey = out of focus. [VC, C10b; B8]
- **≤ ~7 labels per panel, ≤ 3–4 panels per figure.** [DD §3]
- **A plate (full-bleed) once or twice per page at most,** between chapters, only for what needs the whole screen; static except one reveal. [DD D2]

### 5.5 Building
- **Prefer a generated figure:** dates, counts and positions computed by script (`tools/figkit/` or a generator like `work/figure-sheet/instrumentos_processo.py`). No hand-typed SVG. *Why:* every exemplar was kit-built; most failures were hand-typed at 8–26 elements. [R18, F-004; B14]
- **HTML and CSS are first-class** (real text, range inputs, radio groups, `<details>`, CSS grid); SVG for geometry. Instruments work without JS in their default state. [VG v2]
- **Kit SVGs carry `.figkit`; no blanket label CSS. Patch SVG attributes in place;** text outside SVGs stays byte-identical. [F-005, F-003]
- **A one-step scrolly's only panel carries `on`.** [F-015]
- **For one page, call its own `inject()` contract,** so another page's contract can't abort the run. [F-031a]
- **New kit components get a `specimen/figuras.html` entry.** [F-025]
- **Look at the whole sheet, not one crop:** a clean probe is not a look. [F-031b, F-027]

---

## 6. The page

- **The feel:** a scholar's drafting desk: paper, ink, a grid underneath, two accent inks; drawn, never decorated; calm, precise, generous. The home page is the elegance benchmark. [DD §1]
- **Tokens only** (`--paper`, `--paper-2`, `--ink`, `--ink-2`, `--muted`, `--grid`, `--grid-major`, `--dif`, `--conc`, their washes; `--mix` rarely). No hex. *Why:* dark mode works for free; check it anyway. [DD §2]
- **Paper objects:** square corners, 1.5 px ink border, shadow `6px 6px 0 var(--grid-major)`. No gradients, blur, rounded pills, glass, icons. [DD §2]
- **Type:** Archivo (sans 600–750, the main noun); Spectral (serif reading prose at 19 px/1.62, and italic `t-hand` for one-line notes); IBM Plex Mono (uppercase, ~.08–.1em tracking, 10–13 px, for labels, kickers, axes, figure headers). [DD §2]
- **Column:** `min(1,083 px, viewport − 96 px)`, centred, headings aligned. *Why:* 1,444 px was too wide, 76ch too narrow. [CEO.md WIDE-4]
- **Motion:** `pop` / `draw` / `fade` on reveal and scrolly changes, only when the movement is the content. No idle motion, no easter eggs, no scrolljacking; respect `prefers-reduced-motion`. [VG, WS C15; B3]
- **Desktop first:** check at 1280 px; no phone work or phone variants of figures; phone findings are logged debt. [Chairman 05/10, F-009; B2]
- **No PDF or print export.** *Why:* flattening kills the live medium. [VG]
- **Workshop artifacts stay in the workshop repo;** the site gets what readers load, plus `tools/`. [F-010]

---

## 7. Checks before hand-in

The checks pass on absence, so read the page too. PAGE is the site path (e.g. `~/Developer/ordenacoes-filipinas/courses/processo-civil-i/aula-14.html`).

**Text (workshop repo)**
1. `python3 work/slop-bench/slop_gate.py PAGE` → PASS. It runs slop_lint and marks_lint and writes `critic_input.md` for a separate reviewer; apply span patches only, re-run. Then read each paragraph's last sentence for moral closers. [WS G]
2. `python3 protocols/tools/marks_lint.py PAGE` → 0 findings.
3. `python3 work/house-style/house_check.py PAGE` → PASS with **no article warning** (casa.css + casa.js, ≥ 4 `.fonte`, ≥ 1 doctrine, ≥ 2 SVG figures, ≥ 3 marks, `.term` with `data-def`). [F-028a, F-029a, R13]
4. `python3 work/house-style/quote_check.py PAGE [--corpus DIR]` → no FAIL: every quoted segment of 6+ words is found in the course's `work/pipeline/<course>/chapters` after normalizing. Treat its "cut without [...]" WARN as a fail. [R14]

**Site (site repo)**
5. After adding a lesson or touching a front: `python3 tools/offline_build.py`, then `git checkout -- assets/front.css specimen/register.html`, and commit every generated output. *Why:* CI rejects a stale offline manifest. [F-029b]
6. `git add`, then `sh tools/check_all.sh` → `check_all: PASS` (fronts reproducible, dead links, anatomy). It compares against the index, so stage first. Keep unwritten lessons as non-links; never make placeholder pages. If a regenerated front differs, fix the front data. [F-014, F-028b, F-030b]
7. Hero Leitura = regenerated front clock. [F-013]

**Figures (serve your checkout on its own port)**
8. `node work/checks/breakscan.mjs ~/Developer/ordenacoes-filipinas /tmp/breakscan.csv --width 1280 --base-url http://127.0.0.1:PORT` → 0 new findings. Confirm the port serves your build (`curl …/PAGE | grep "≈"`).
9. `node work/figure-sheet/figsheet.mjs --base-url http://127.0.0.1:PORT --out sheet.png courses/<course>/<page>.html`, and look at every tile. [F-031b, R18]

**Read**
10. Three random paragraphs aloud; split any sentence that takes more than one breath. Fact pass: every article, date, vote and case name against its locator. [WS G, A8]

**PR body:** words before and after, the figsheet, each figure's crop and delete-every-word result, check outputs, `requests.md` summary, doubts. Search `BUGS.md` by symptom before debugging; a new fix adds a row in the same commit. [Source Pipeline S5, R17, F-018]

**Flow:** one approved lesson first as the prototype; log its faults as FLIGHT-LOG rows; then waves of ≤ 6, each applying the log first. The CEO reads the staging build before the swap. [F-023b]

---

## Appendix A. Flight-log rows not folded in

- **Superseded:** **F-011** (tables at 375 px) by desktop first (05/10). **F-023** (writing pause) by F-023b (07/10). **F-027**'s per-panel 1512 px crop by the figsheet plus per-figure crops (F-031b, R17); its "a clean probe is not a look" stands.
- **Valid, not writer-facing** (Source Pipeline S0–S4): **F-001**; the budget half of **F-002**.
- **Numbering collision:** F-028 to F-031 each appear twice. Cited here in file order, **a** first, **b** second: F-028a house_check / F-028b front non-links; F-029a quote once / F-029b offline_build; F-030a the thread / F-030b front data; F-031a single-page inject / F-031b contact sheet. Renumber the b rows when convenient.

## Appendix B. Conflicts resolved (CEO to confirm)

1. **Page size.** WS A0 (25/09) 2.5–4k, "not a cap"; VG and Source Pipeline (27–30/09) 2.5–4.5k; R10 (07/10) "the 4.5k ceiling". **Chosen:** 2.5–4.5k, split past 4.5k, no page under ~1.5k.
2. **Phone.** DD (29/09), VG and Blueprint A10 require 390/375 px and phone versions of wide figures; F-009 (01/10) bars phone variants; chairman 05/10: desktop first. **Chosen:** desktop first, 1280 only.
3. **Idle motion.** DD (29/09) allows one slow ambient loop ("the owner liked a slow idle flag"); WS C15 (25/09) rejects the hero pennant; VG v2 (30/09) bans idle motion. **Chosen:** none (newest). Confirm whether the flag is a standing exception.
4. **Run-in bold.** WS D8 lets run-ins stay bold; marks_lint and casa.css (06/10) ban plain `<strong>` and add `.runin`. **Chosen:** `.runin`.
5. **`.art` chips.** C10b (06/10) allows them rarely; the 06/10 evening handoff records them judged noisy and unused. **Chosen:** don't use.
6. **Mark length.** C10b ~6 words; marks_lint fails above 8. **Chosen:** aim for 6; 8 is the hard limit.
7. **Statute rendering.** VG's ontology puts primary sources in the `lex` block or a facsimile sheet; C10b and F-031b (07/10) make them `.fonte.dec`, never a figure. **Chosen:** `.fonte.dec`; a statute-cut figure only if it measures what a block can't.
8. **Colour.** DD: orange = emphasis, exits, the tested thing; blue = the contrasting term, the answer. VG calls `conc` "red". C10b (06/10): blue = decided, orange = limit, figures agree. **Chosen:** blue = decided/answer, orange = limit/trap/tested term; neutral contrasts in ink and grey.
9. **Ledes.** D10.3 (05/10): ledes state the question. The Latam Aula 05 density reference previews answers. **Chosen:** the rule; Latam's ledes are legacy.
10. **Closing list.** WS B7 gives long lessons a "Para a prova" list; D10.3 (05/10) bans restatement; the Processo brief and F-030a close on exam-bank exercises. **Chosen:** exercises only.
11. **Authors in prose.** WS C6 (chairman-confirmed): naming a position's holder is content. E2 (05/10): no lead-in attribution. **Chosen:** name holders of positions; never introduce or credit a quote in prose; never pages.
12. **Plan review.** WS A9: Claude reviews every plan. Source Pipeline S5a and R3: a panel approves; no mid-run CEO gate. **Chosen:** blueprint plus panel.
13. **Lint command.** WS G names slop_lint; slop_gate (06/10) wraps it with marks_lint. **Chosen:** slop_gate, plus house_check.
14. **Figure source.** F-004: figkit only. R18: any generated figure. **Chosen:** generated by script; hand-typed SVG banned.
15. **Crop width.** Blueprint A10 and F-027: 1512 px; desktop first: 1280; figsheet defaults to 1,440. **Chosen:** breakscan at 1280, figsheet at its default.
