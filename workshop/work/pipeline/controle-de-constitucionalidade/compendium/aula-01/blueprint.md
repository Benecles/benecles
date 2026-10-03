# Blueprint: Controle, Aula 01 (Conceito): THE REFERENCE BLUEPRINT

This is the blueprint behind the reference lesson (live `courses/controle-de-constitucionalidade/aula-01.html`, whose `REF ·` comments annotate the result). Every blueprint in every course copies this file's **shape**, and every **Method** note tells you how to make the same decision for a different topic. The empty template is `protocols/templates/Lesson Blueprint.md`.

Read it this way: the plain text is what we decided for Aula 01. The **Method** blocks are the reasoning you reuse. A blueprint that copies our decisions without the reasoning fails the panel; one that reasons the same way about different material passes.

> **Method: why the blueprint matters more than the writing.** A writer following a precise blueprint has few ways left to go wrong. Every fault the W2/W3 gate found (F-019..F-022) traces back to a blueprint decision that was missing or vague: no thread, so a fictional country got invented; a scope fence with no warning, so it got pasted onto the page; traps not chosen, so every trap got restated six times. Spend the effort here.

---

## A0. Inputs read, and what each one is for

| Input | Size | What I took from it |
|---|---|---|
| S0 line (`course-map.json`) | 1 line | The learning outcome: *explain what controle is; identify norma controlada, parâmetro, órgão controlador*. This is the lesson's contract: every section must serve one of the three verbs. |
| Slides (`10-slides.txt`) | 7 pp. | The professor's framing: "adequação vertical", the two planes, constitucionalidade vs inconstitucionalidade as positions on that plane, parâmetro = CF (+ CE), convencionalidade via art. 5º § 3º. Slides tell you **what the professor will ask**, not how to explain it. |
| Lenza § 6.1 | 4.1k | Supremacy + rigidity as requirements; José Afonso da Silva's compatibilidade vertical; the nulidade default and art. 27 (boundary only). |
| Mendes/Branco cap. 10 (4 files) | 3.9k | Constitucionalidade as a normative relation (Jorge Miranda); Rui/Dicey's three senses; Kelsen on sanction; Bittar's definition; the who/when/how classification; Brazil as misto. |
| Barroso cap. I | 0.9k | Every application of law embeds a constitutionality check; rigidity counterfactual; what can be an objeto; jurisdição × controle. |
| Exercises/exams | none assigned | No past question maps here, so the traps come from the slides' contrasts and the classic confusions in the sources. |
| Live page (before) | 940 words | Kept: the hero, the three kit figures (FIG-1). Cut: abstract prose, the promised-but-missing example, the "Fontes e limites" disclaimer. |

Total source: ~9k words for a ~3k page, a **3:1 ratio**.

> **Method: read everything before outlining, and check the ratio.** Under 2:1 you'll pad (or invent; F-022). Over 6:1 you must choose harder, and the cut list (A7) gets long. Note for each input what it is FOR: the S0 line is the contract, the slides predict the exam, the books supply depth and carriers. Never mine slides for prose.

## A1. Reader brief

- **Already knows:** nothing from this course. From Const I: what a Constitution is; art. 5º lists rights.
- **Can do after reading** (exam verbs, not topics):
  1. Given facts, name the objeto, the parâmetro and a possible controlador.
  2. Say why the comparison is vertical, and what changes if the Constitution were flexible.
  3. Tell constitucionalidade from convencionalidade, and place a treaty (§ 3º vs supralegal).
  4. Tell controle from direct application of the Constitution.
- **One sitting:** ~3k words, 20 min.

> **Method:** write "can do" items as tasks a question could ask ("given facts, name…"), never as topics ("parâmetro de controle"). Each one must be tested in the quiz or the worked case. If you can't imagine the question, the item is a topic: rewrite it.

## A2. Exam traps (they decide where the words go)

| # | Trap | Why students fall for it | Where the page defuses it | Tested in |
|---|---|---|---|---|
| T1 | "Inconstitucional" used as mere censure | Everyday usage; the word sounds like disapproval | §03 Dicey table + Kelsen | chave |
| T2 | A conflict between norms of equal rank called inconstitucionalidade | Missing the rigidity premise | §02 counterfactual | quiz 1 |
| T3 | A treaty under § 3º treated like a supralegal treaty, or vice versa | Two rites, one word "tratado" | §05 + Fig. 3 | quiz 3 |
| T4 | A judge applying a right directly is thought to be "controlling" | Both invoke the CF | §04 minimal pair | quiz 2 |
| T5 | ADI at the STF against a municipal law | Students know the ADI first | §06 worked case | quiz 4 |

> **Method: each trap is stated ONCE, where it bites, and tested ONCE.** Restating it in three sections is writing to the gate (F-021). If you have no exam questions, derive traps from (a) contrasts the slides draw, (b) distinctions the sources spend a paragraph defending, (c) pairs of terms that sound alike.

## A3. Scope fence (PLANNING ONLY, NEVER ON THE PAGE)

> ⚠ **This list tells you what to leave out, silently.** Do not write a paragraph telling the reader which lesson covers what (F-020). On the page, a neighbour topic gets at most one boundary sentence with a link, and only where the reader would otherwise ask.

Pressupostos in depth → Aula 02 · Kelsen × Schmitt → 03 · bloco and treaties in depth → 04–05 · formal/material, ação/omissão → 06 · recepção → 07 · nulidade × anulabilidade, modulação → 08 · momentos/órgãos in depth → 09–10 · modelos → 11.

## A4. Claim inventory (locators private; never on the page)

| # | Claim | Status | Locator | Carrier | § |
|---|---|---|---|---|---|
| 1 | Controle = verifying the compatibility of an infra act with the Constitution | settled | slides p. 2; Barroso p. 23; Lenza 6.1.1 | Leis A/B, art. 5º XVI | 01 |
| 2 | Every application of an infra norm embeds a constitutionality check | settled | Barroso p. 23 | judge applying Lei B | 01 |
| 3 | Objeto: leis, MPs, decretos, regimentos; broadly also atos administrativos and decisões | settled | Barroso p. 24 | none | 01 |
| 4 | Omissão can be unconstitutional; private violations traditionally outside | traditional view | Barroso p. 24; Mendes p. 1860 | none (boundary) | 01 |
| 5 | Escalonamento; compatibilidade vertical (José Afonso da Silva) | settled | Lenza 6.1.1; slides p. 2–3 | Lei B depends on art. 5º XVI | 02 |
| 6 | Without rigidity, conflict = revogação, not inconstitucionalidade | settled | Barroso p. 24; Lenza 6.1.1 | counterfactual | 02 |
| 7 | CF/88 is rigid (art. 60 § 2º; § 4º) | statute | CF | quorum numbers | 02 |
| 8 | Constitucionalidade is a normative and valorative relation (Jorge Miranda) | named position | Mendes p. 1855–56 | none | 03 |
| 9 | Dicey via Rui: three senses of "inconstitucional" | historical, settled | Mendes p. 1856–57 | table | 03 |
| 10 | Kelsen: no annulment mechanism means no binding force; sanção qualificada | named position | Mendes p. 1858–59 | three-fifths vs simple majority | 03 |
| 11 | Bittar: constitutional = act that incurs no sanction | named position | Mendes p. 1859–60 | none | 03 |
| 12 | Brazil: nulidade default; art. 27 Lei 9.868/99 (2/3) | settled | Lenza 6.1.2, 6.1.4.1 | none (boundary) | 03 |
| 13 | Who/when/how classification; political control (CCJ, veto art. 66 § 1º) | settled | Mendes p. 1860–62 | Lei B in a table column | 04 |
| 14 | Judicial preventive exception: MS by parlamentar vs PEC (art. 60 § 4º) | settled | Mendes p. 1862 | none | 04 |
| 15 | Brazil misto: difuso since the Republic + ADI/ADC/ADO/representação | settled | Mendes p. 1865 | Marbury (1803) | 04 |
| 16 | Jurisdição constitucional (genus) × controle (species) | settled | Barroso p. 25 | same passeata, two judges | 04 |
| 17 | Parâmetro: CF; CE via art. 125 § 2º | settled | slides p. 6; CF | lei municipal | 05 |
| 18 | Treaty under § 3º = emenda; otherwise convencionalidade | settled | slides p. 7; CF | Fig. 3 | 05 |
| 19 | RE 466.343: supralegal (Gilmar Mendes, majority); Celso de Mello lost | settled holding | Sarlet 2020 p. 1787–88 | depositário infiel, CC art. 652 vs Pacto 7.7 | 05 |
| 20 | ADI only against federal/state law (art. 102 I a) | statute | CF | worked case | 06 |

> **Method:** every sentence on the page must map to a row; a row with no locator is a claim you're inventing (E4). Record **status** honestly: "named position" means you name the author on the page (C6); "settled" means you don't need to. The **carrier** column is where vagueness dies: a claim without a carrier becomes abstract prose.

## A5. The thread (how it was chosen)

**Chosen:** art. 5º, XVI (reunião) with two hypothetical laws: Lei A (48 h notice: inside the limit) and Lei B (mayor's authorization: crosses "independentemente de autorização").

| Candidate | §01 pieces | §02 vertical | §03 sanção | §04 who | §05 parâmetro | §06 case | Verdict |
|---|---|---|---|---|---|---|---|
| Art. 5º XVI + Leis A/B | ✓ the text has an explicit limit | ✓ | ✓ two verdicts | ✓ every path barrable | ✗ needs a 2nd parameter | ✓ municipal twist | **chosen**; §05 borrows Fig. 3 |
| Depositário infiel (RE 466.343) | ~ | ✓ | ✓ | ✗ one historical path | ✓ | ✗ settled, no twist | §05 only |
| A real ADI (e.g. a famous one) | ✓ | ✓ | ✓ | ✗ only concentrated | ✗ | ✗ | rejected |
| Fictional constitution | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **banned** (F-022) |

> **Method: test each candidate against every section before writing.** The winner is the one that survives the most sections with REAL text; a section it can't carry borrows a local carrier (here §05 uses the depositário). Prefer a constitutional or statutory text with an explicit **limit word** ("independentemente de", "salvo", "vedado", "prazo de"): the limit is what the figure measures and what the worked case turns on. A fictional setting always "fits", which is exactly why it's banned: it fits because it carries no law.

## A6. Section plan

| § | h2 (informs) | The question it answers | Claims | Carrier | Form | Words | Hands to the next § |
|---|---|---|---|---|---|---|---|
| hero | A Constituição como régua | What does controlling DO? | 1 | ruler (hero) | figure | — | the instrument |
| 00 | O curso | What will this course train? | — | two everyday cases | prose + `<ol>` roteiro | 250 | the four pieces |
| 01 | Três peças: objeto, parâmetro, controlador | What are the pieces of any controle question? | 1–4 | Leis A/B | prose → Fig. 1 | 550 | "the measure has a limit; why does it bind?" |
| 02 | Por que a comparação é vertical | Why can the Constitution measure laws? | 5–7 | counterfactual | prose only | 400 | "a violation has a consequence" |
| 03 | Conformidade ou vício | What does "inconstitucional" claim? | 8–12 | Fig. 2, Dicey table | figure → prose → table → prose | 550 | "someone must apply the sanction" |
| 04 | Quem controla, quando e como | Who can stop Lei B, when, how? | 13–16 | Lei B column; minimal pair | prose + table + prose | 500 | "which ruler?" |
| 05 | Qual é o parâmetro? | Which norm measures? | 17–19 | depositário (Fig. 3) | prose → Fig. 3 → prose | 400 | "now all at once" |
| 06 | Um caso do começo ao fim | Can you run the whole roteiro? | 20 + all | municipal law | `p.caso` + run-in steps | 350 | recap |
| ↺ | Recapitulação | — | traps T1–T5 | — | chave + 4 quiz items | 150 | — |

> **Method:** write each h2 as the content and each section as the **question** it answers; if two sections answer the same question, merge them. Give every section a word budget (the total lands at 2.5–4.5k) and the idea it hands on: if you can't name the hand-off, the order is wrong. Alternate figure sections and prose-only sections, so two dense stretches never meet. Prose-only stretches render centred and wider (LAY-1), so plan them deliberately.

## A7. Figures

| Fig | Verb | Instrument (kit) | The card claims | Negative space |
|---|---|---|---|---|
| hero | measure | Ruler, two strips (`controle_a01.hero`) | none (the deck carries the claim) | 15/16 |
| 1 | measure | Ruler + one strip | "the ruler has a limit; treating the same right doesn't make a law suspect" | 14/16 (weak lower right: known) |
| 2 | compare | Ruler + two strips | "same ruler, opposite verdicts, because of content" | 15/16 |
| 3 | compare | two Rulers, one law | "the same CC art. 652 passes one measure and fails the other" | 15/16 |

> **Method:** name the figure's VERB first (Figure Library test 1); if it's "illustrate", drop the figure. Choose a kit instrument for that verb. Write the card's claim before drawing: the drawing must make THAT claim visible. Check the frame fits the drawing, the 4×4 grid, and breakscan before the PR.

## A8. Cut list (and why)

- Nulidade × anulabilidade, Linkletter, Spain, Portugal, Germany: owned by Aula 08; one boundary sentence in §03 instead.
- Bloco de constitucionalidade, superveniência, Hesse on rigidity and flexibility: depth for later lessons; nothing here needs them.
- The old page's "Fontes e limites" note and its promise of an example it never gave.

> **Method:** a cut list makes the blueprint honest: the panel checks that what you dropped belongs elsewhere. Cutting is never announced on the page.

## A9. Failure modes to avoid in THIS lesson, with countermeasures

| Risk | Countermeasure |
|---|---|
| Abstraction drift (the old page's fault) | Every section names Lei A/B or its carrier within two sentences (C5). |
| Course-overview creep in §00 | Cap 250 words; no list of lesson contents. |
| Doctrine as quotes | Paraphrase; quote statutes only (E2). |
| Backstage on the page (F-019) | `slop_lint` hard ban; never write "slides", "material", "nesta leitura". |
| Restating traps (F-021) | Trap table A2: one place, one test. |

## A10. Acceptance

`slop_lint` 0 hard hits · `check_all` PASS (anatomy: no LOOSE-PROSA, LATE-PANEL, SQUARE-KIT) · breakscan 0/0 · hero "Leitura" = front clock · read three random paragraphs aloud · look at 1512 px and 375 px · every A6 hand-off is the actual last idea of its section.

## For the panel (S5a): what to check in a blueprint like this

1. A0 exists, and the source ratio is between 2:1 and 6:1.
2. "Can do" items are tasks, and each is tested (A1 ↔ A2 ↔ quiz).
3. The thread table (A5) tests real candidates against every section; no fictional settings.
4. Every A6 section has a question, claims from A4, a carrier, a form, a budget and a hand-off.
5. The scope fence (A3) is marked planning-only, and no section plans meta-text about other lessons.
6. Every figure has a verb, an instrument and a card claim (A7).
