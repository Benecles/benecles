# Blueprint: Processo Civil I-a, Aula 10 (Julgamento conforme o estado do processo)

## A0. Inputs read, and what each one is for

| Input | Size | What I took from it |
|---|---:|---|
| S0 line — course-map.json, aula-10.html | 1 record | The contract is: “Escolher a saída compatível com o estado do processo e justificar se a instrução ainda é necessária.” The page keeps the aula-10.html address, centers that task, and targets about 3,300 words. |
| Slides — 10-slides.txt | 10 words | The file says that no slide source is mapped to this lesson. It adds no professor-specific framing, examples, or claims. |
| Barbosa Moreira, Parte I — 20-primary-001-barbosa-moreira-temas-serie4-1989-10-saneamento-do-processo-e-aud-9d888dac.txt | 1.3k | PDF pp. 115–118 give the test of utility and necessity for continuing through the standard procedure and the reason to leave only necessary proof for instruction. This is the conceptual opening, not a taxonomy of foreign procedure. |
| Barbosa Moreira, Parte II — 20-primary-002-barbosa-moreira-temas-serie4-1989-10-saneamento-do-processo-e-aud-afaee2c0.txt | 1.2k | PDF pp. 119–121 distinguish concentrated and diffuse ways of organizing procedural work. The comparison is context, not a claim needed for this page; its international models stay out. |
| Didier Jr., chapter 21 — 20-primary-003-didier-curso-vol1-2017-ch21.txt | 10.0k | PDF pp. 767–775 supply the transition after preliminary measures, the five statutory exits, and the limits of judgment under art. 355. The remainder treats organization and stabilization in depth; only the residual role of art. 357 is needed here. |
| Lucon, arts. 354–357 — 20-primary-004-lucon-cpc-355-357-assigned-reading.txt | 6.8k | PDF pp. 3–6 (book pp. 586–589) distinguish the routes in arts. 354 and 355 and analyze proof sufficiency, revelia, and surprise decisions. PDF pp. 7–13 (book pp. 590–596) supply a short art. 356 boundary and the art. 357 fallback. |
| CPC extracts — 30-supporting-001 through 009 | 746 | Arts. 10, 344, 345, 348, 349, 353, 355, 357, and 370 provide the exact statutory conditions used in the page. |
| Decision on “julgamento conforme a sinceridade do processo” — 30-supporting-012-moodle-model-julgamento-sinceridade-moodle-model-julgamento-sinceridade.txt | 257 | The actual decision records a purchase in Nov. 2012, filing on 18 Aug. 2015, and a 15 Jan. 2016 recognition of decadence. It is one concrete record to read, not a general rule or a model of judicial style. |
| Exercises and exams — 50-exercises-and-exams.txt; exam-bank.json | 12 in the compendium file | S3 assigns no exercise or past-exam chapter to aula-10.html, and the exam bank has no question assigned to that lesson ID. The overlapping prompt “Dê um exemplo de julgamento parcial de mérito?” (2015/1, q. 10) is assigned to aula-11-merito.html; it gets one bounded test because partial merits remain on this syllabus line. |
| Live page before | 3.9k HTML words; about 2.7k visible words | It already has the right procedural moment and covers arts. 353, 355, and 357. Its fictional Oficina Rocha case, broad preliminaries list, long partial-judgment section, and detailed sanitation material do not fit this lesson's present S0 boundary. Keep the page identity and navigation; rebuild the explanation around the real court record. |
| Reference blueprint and live page with REF notes | Blueprint plus 3.1k-word page | The reference Method notes supply the decisions used here: function before outline, traps before section order, a tested real thread, claims with private locators, questions as section heads, and a reader-facing page free of source and scope-fence commentary. The live comments define which structures copy, vary, or stay backstage. |
| Design Direction, Visual Genres, Visual Casting, BUGS.md | House rules and issue index | Use a real paper object from Processo Civil I’s world (petição, autos, calendar, clerk’s stamp, order of acts); two accent inks at most; no decoration; the figure must make its claim visible and pass the textless-mark test. BUGS.md has no S5a-specific blueprint symptom. Its relevant figure findings are frame/crop, late panel, label collision, and breakscan failures (#21–26); this plan uses one scaled docket and must preserve actual date precision. |

Source ratio: about 20.3k words of primary text, selected CPC extracts, and the real decision : 3.5k target words = **5.8:1**.

## A1. Reader brief

- **Already knows:** the basic order of pleadings; contestation and revelia; that preliminary measures may be needed after the response; and how a decision organizing proof identifies disputed facts and evidence.
- **Can do after reading** (tasks a question could ask):
  1. Given a record after the preliminary measures, classify the available route under arts. 354, 355, 356, or 357 and explain which condition selects it.
  2. Apply both branches of art. 355, including the separate checks for the effect of revelia and a timely request for evidence.
  3. Explain what changes when a parcel of the merits is ready before the rest, then state what the court must organize if no immediate route applies.
  4. Read the real Florianópolis decision's dates and dispositive, identify the route it used, and distinguish that route from art. 355.
- **One sitting:** about 3.5k words, 20 minutes.

## A2. Exam traps

| # | Trap | Why students fall for it | Where the page defuses it (one place) | Tested in (one item) |
|---|---|---|---|---|
| T1 | Every decision made after the pleadings is called judgment under art. 355. | The decisions share a procedural moment, but they have different statutory triggers. | §02, the comparison of the five outcomes. | Quiz 1: classify the real decadence disposition. |
| T2 | Revelia alone authorizes art. 355, II. | Students remember the presumed truth of pleaded facts and skip the other statutory conditions. | §03, where the three conditions and art. 345 exceptions are read together. | Quiz 2: test whether revelia alone completes art. 355, II. |
| T3 | A judge may declare that no more proof is needed and then reject the claim because the plaintiff failed to prove it. | “No further proof” can sound like a conclusion about the claimant's evidence rather than a commitment about the record. | §03, in the paragraph on the decision's internal consistency. | Quiz 3: identify the contradiction in that disposition. |
| T4 | A partial merits judgment is the same as a final judgment that grants only part of a claim. | “Partial” can describe either the content of the result or the portion of the process decided at that moment. | §04, limited to the distinction required to locate art. 356. | Quiz 4 uses the 2015/1 q. 10 prompt once: give a statutory example of a partial merits judgment. |

The exam bank contains no question assigned directly to aula-10.html. Question 2015/1, q. 10, is the sole entry on the overlapping syllabus point and is assigned to aula-11-merito.html. It is tested once in Quiz 4; the rest of that topic remains outside this page.

### Syllabus coverage

| Syllabus point | Where it is honored |
|---|---|
| Estabilização do processo | A3 scope fence only. The target compendium has no lesson-specific source pages for stabilization as its own topic; the course map assigns it to the separate aula-10-estabilizacao.html compendium. |
| Saneamento do processo | §05 covers art. 357 as the residual decision that organizes continued proof. Detailed organization and stabilization remain outside. |
| Julgamento conforme o estado do processo | §02 names and distinguishes the outcomes after the preliminary measures. |
| Julgamentos parciais de mérito | §04 states the art. 356 threshold briefly and tests the assigned q. 10 prompt once. |
| Decidir se instrui ou julga; julgamento antecipado do mérito | §03 applies art. 355's two branches; §05 identifies the instruction route when no immediate judgment fits. |

## A3. Scope fence (PLANNING ONLY, NEVER ON THE PAGE)

- Stabilization of the organization, the hearing in cooperation, agreement on issues, calendar, and effects of stabilization → aula-10-estabilizacao.html.
- Full treatment of partial judgment, its appeal, liquidation, enforcement, and effects → aula-11-merito.html.
- General theory of proof, admissibility, and valuation → aulas 14–16.

The page itself can make at most two natural hand-offs: one sentence from art. 357 to the detailed organization page, and one sentence from the short art. 356 boundary to the full partial-judgment treatment. Do not print this list or announce what the page omits.

## A4. Claim inventory (locators private)

| # | Claim (full sentence) | Status | Locator | Carrier | § |
|---|---|---|---|---|---|
| 1 | After the preliminary measures are completed or are unnecessary, the judge selects a decision according to the state of the process. | statute | 30-supporting-006, CPC art. 353; 20-primary-003, PDF pp. 771–772 | The real post-response court record | 01–02 |
| 2 | Continuing through the full procedure is justified only when it is useful and necessary; the remaining instruction should include all and only necessary proof. | named position | 20-primary-001, PDF pp. 115–116 | Barbosa Moreira's utility/necessity test, applied to the real record | 01 |
| 3 | The five routes are extinction without merits, extinction with merits on the grounds in art. 487, II or III, judgment under art. 355, partial judgment under art. 356, and organization under art. 357. | statute | 20-primary-003, PDF p. 771; 20-primary-004, PDF pp. 3–13; 30-supporting-006–008, CPC arts. 353, 355, 357 | The statutory comparison; actual decadence disposition | 02 |
| 4 | CPC art. 354 calls for sentence in the cases under arts. 485 and 487, II or III. | statute | 20-primary-004, PDF p. 3 (book p. 586) | The real decision recognizing decadence | 02, 06 |
| 5 | The real decision's recognition of decadence follows the art. 354 route, not art. 355. | statute applied to record | 20-primary-004, PDF p. 3; 30-supporting-012, whole document | Florianópolis decision | 02, 06 |
| 6 | Art. 355, I, permits judgment on the merits when no additional evidence is needed. | statute | 20-primary-003, PDF pp. 772–774; 20-primary-004, PDF pp. 4–6; 30-supporting-007, CPC art. 355 | The art. 355 text beside the real record | 03 |
| 7 | Art. 355, II, requires revelia, the effect in art. 344, and no evidence request under art. 349. | statute | 20-primary-003, PDF pp. 773–774; 20-primary-004, PDF pp. 5–6; 30-supporting-002, 005, 007 | The art. 355 text | 03 |
| 8 | The exceptions in art. 345 prevent the art. 344 effect; in that case art. 348 directs the court to specify evidence. | statute | 20-primary-004, PDF p. 6; 30-supporting-003–004, CPC arts. 345, 348 | The statutory extract | 03 |
| 9 | A defendant in revelia may still produce counterproof if represented in time to perform the necessary acts. | statute | 30-supporting-005, CPC art. 349; 20-primary-004, PDF p. 6 | The real case as contrast: its defendant answered | 03 |
| 10 | Before deciding on a ground not yet addressed by the parties, the judge must give them an opportunity to speak, even when the issue is cognizable ex officio. | statute | 30-supporting-001, CPC art. 10; 20-primary-004, PDF p. 3 (book p. 586) | The real decision's reference to the response to contestation | 03 |
| 11 | Didier treats a judgment under art. 355 as inconsistent with later rejection for lack of proof after the judge has declared further proof unnecessary. | named position | 20-primary-003, PDF pp. 773–774 | The art. 355, I, text and the real record | 03 |
| 12 | If none of the preceding routes applies, art. 357 orders the judge to organize the process and delimit the evidence still required. | statute | 20-primary-003, PDF p. 774; 20-primary-004, PDF pp. 9–13; 30-supporting-008, CPC art. 357 | The real record's terminating disposition as a limit | 05 |
| 13 | Art. 356 allows a partial merits decision when one or more claims or a parcel of them is undisputed or ready for immediate judgment under art. 355. | statute | 20-primary-003, PDF p. 774; 20-primary-004, PDF pp. 7–9 (book pp. 590–592) | The actual q. 10 exam prompt | 04 |
| 14 | The real court record states a purchase in Nov. 2012, an action filed on 18 Aug. 2015, and a 15 Jan. 2016 disposition recognizing decadence. | settled fact | 30-supporting-012, whole document | The same real court record throughout | Hero, 01–06 |
| 15 | The judge may determine necessary evidence and must give reasons when refusing useless or dilatory measures. | statute | 30-supporting-009, CPC art. 370 | The real record, with the legal rule kept distinct from its facts | 03, 05 |

## A5. The thread

**Chosen:** the actual decision from the 2º Juizado Especial Cível in Florianópolis in the case of Bruno dos Santos Vieira against Lilla Imports and another defendant. The file reports the phone purchase as November 2012, the action filing as 18 August 2015, and the decision as 15 January 2016; the judge states that decadence ends the action. Use only the facts and ground the decision itself records. It is a local record to classify, not a precedent establishing a general rule.

| Candidate | Hero | §01 | §02 | §03 | §04 | §05 | §06 / recap | Verdict |
|---|---|---|---|---|---|---|---|---|
| Real Florianópolis decision | ✓ dated entries are the figure's data | ✓ opens after the answer and reply | ✓ its stated decadence ground identifies art. 354 | ✓ a contestation makes art. 355, II unavailable; the dates remain a proof-sufficiency example, not a 355 holding | △ it does not illustrate art. 356; the statute supplies that brief boundary | ✓ the disposition ends the case rather than ordering art. 357 organization | ✓ run the whole classification on the same record | **Chosen**; it carries the lesson by both what it shows and which routes it does not show. |
| CPC art. 355 | — no chronology | △ only one procedural condition | △ one of five outcomes | ✓ the statute's core | — no partial decision | — no residual organization | △ can test a rule but cannot carry a case | Rejected as the whole thread; keep as a local legal carrier in §03. |
| CPC art. 357 | — no chronology | △ after the response | △ one outcome | △ only if the art. 355 tests fail | — no partial judgment | ✓ the fallback | △ gives no record to classify | Rejected as the whole thread; keep as the legal source for §05. |
| Exam 2015/1, q. 10 | — prompt only | — no case | — no routes | — no proof question | ✓ exact partial-merits prompt | — no organization | ✓ one recap item | Rejected as the thread; it carries only the bounded art. 356 test. |

The single case stays present even when a section gives the statutory boundary. In §04, the case is not presented as a partial judgment example; in §03 it is not mislabeled as an art. 355 judgment. No invented parties or alternative facts are added.

## A6. Section plan

| § | h2 (names the content) | The question it answers | Claims (A4 #) | Carrier | Form | Words | Compendium locator | Hands to the next § |
|---|---|---|---|---|---|---:|---|---|
| hero | Pronto para julgar? | What does the state of the process let the judge do? | 14 | The three dated entries and disposition in the real Florianópolis record | Measured docket figure | — | 30-supporting-012, whole document | The docket's final entry is a decision; identify the statutory route before naming the kind of judgment. |
| 01 | A decisão começa pelo que já está nos autos | Why does the court pause after preliminary measures? | 1–2, 14 | The actual record, read through the utility/necessity distinction | Prose-only | 500 | 20-primary-001, PDF pp. 115–116; 20-primary-003, PDF pp. 767–771; 30-supporting-006, art. 353; 30-supporting-012, whole document | Once the record is ready for a decision, the next question is which legal exit its state permits. |
| 02 | As saídas do art. 353 | Which decisions count as judgment according to the state of the process? | 1, 3–5 | The five outcomes; the actual decadence disposition is placed under art. 354 and art. 487, II | Prose plus a compact HTML comparison table, not a figure | 520 | 20-primary-003, PDF p. 771; 20-primary-004, PDF pp. 3–4; 30-supporting-006–008, arts. 353, 355, 357; 30-supporting-012, whole document | The real disposition is under art. 354; now isolate the different art. 355 threshold. |
| 03 | Quando o art. 355 dispensa a instrução | When may the judge resolve the merits without further proof? | 6–11, 15 | Art. 355, I and II, with the actual contestation setting a limit on the revelia branch | Prose, lex excerpt, then the docket instrument's art. 355 setting; no arrow diagram | 900 | 20-primary-003, PDF pp. 772–775; 20-primary-004, PDF pp. 4–6; 30-supporting-001–005, 007, 009, arts. 10, 344, 345, 348, 349, 355, 370; 30-supporting-012, whole document | Full-process readiness raises a separate question: can a ready parcel be decided while another continues? |
| 04 | A parcela pronta | What makes a partial merits judgment different from a partial result? | 13 | Re-open the same Florianópolis docket at its decadence disposition and classify it as art. 354/487, II; hold that actual single disposition beside art. 356's threshold, explicitly noting that this record does not show a partial merits decision. Then answer the bank's q. 10 statutory prompt without attaching it to the docket. | Prose-only, with one short law extract | 320 | 20-primary-003, PDF p. 774; 20-primary-004, PDF pp. 7–9; 30-supporting-012, dispositive; exam-bank.json, exam-2015-1-avaliacao-2-q10; 50-exercises-and-exams.txt records that no item is assigned to this lesson | If neither a full nor partial merits route is ready, the process still needs an organized path for proof. |
| 05 | A instrução que ainda falta | What does the court do when none of the immediate routes applies? | 12, 15 | Return to the same docket's final line and trace its actual art. 354 choice; mark art. 357 as unselected in this record, then pivot to the statute for the residual operation: organize the process and delimit necessary proof. Do not supply unrecorded facts or proof needs for this case. | Prose-only | 400 | 20-primary-003, PDF p. 774; 20-primary-004, PDF pp. 9–13; 30-supporting-008–009, arts. 357, 370; 30-supporting-012, dispositive | Return to the same real record and classify its actual outcome. |
| 06 | A decisão de Florianópolis, do registro ao dispositivo | Can the reader use the classification on the real record? | 4–10, 14 | The same date entries and disposition, worked in order: record, ground, route, consequence | Case folder in prose, with four bold run-ins | 400 | 30-supporting-012, whole document; 20-primary-004, PDF p. 3; 30-supporting-001, art. 10 | The worked answer becomes the one-breath key before the quiz. |
| recap | Escolha a saída | Can the reader name and justify the route? | T1–T4; A1 tasks 1–4 | The actual Florianópolis record plus one statutory art. 356 prompt; the exit task asks whether the record supports judgment without further proof or calls for organized instruction, without treating the recorded decadence disposition as an art. 355 holding | Key, four quiz items, and one record-based exit exercise | 300 | No assigned exercises or exam pages: 50-exercises-and-exams.txt says none; exam-bank.json maps q. 10 to aula-11-merito.html. Quiz items are authored from A4 claims already traced above; the exit task asks the reader to assess material facts, any missing evidence, and the record's limits. | — |

**Total:** about 3.5k words. The sequence alternates the case instrument with explanatory prose and a decision table; the table stays HTML because its content is rows of legal outcomes, not a figure.

**Closing exercise, after Quiz 4:** use the Florianópolis record, not a new hypothetical. Prompt: “O registro informa a compra em novembro de 2012 e o ajuizamento da ação em 18 de agosto de 2015. O juiz também registra a alegação de tentativas repetidas de solução amigável e questiona a prova e a menção na petição inicial. Identifique quais fatos são materiais para a decadência adotada, avalie se o trecho esclarece esses fatos e, se não, indique que prova poderia alterar a decisão. Justifique se o registro permite dispensar outras provas pelo art. 355, I, ou se a instrução precisa ser organizada pelo art. 357, e limite sua conclusão ao que o trecho permite afirmar.” The prompt asks the learner to assess necessity from the record; it does not state which facts are material, whether more proof is needed, or what conclusion to reach. Preserve the actual classification of the decadence disposition under art. 354/487, II; do not treat the case as an art. 355 holding or a general rule.

## A7. Figures: the cast

| Fig | Move | Cast (chosen) | Rejected casts and why | The sheet, described | Card claims |
|---|---|---|---|---|---|
| Hero · measured docket | Trace the dated record to the actual disposition and then name what that disposition does—and does not—teach about art. 355. | **Docket / calendar family:** dated records arranged on one month scale. **Dossier family:** actual case file opened at facts, issue, reasons, and disposition. **Decision-form family:** the reader checks conditions and receives the art. 354/355/356/357 route. **Ledger family:** record entries balanced against proof still needed. | Dossier: strong for one matter, but its tabs alone do not show the time between purchase, filing, and decision; Aula 08 already uses a document dossier. Decision form: would be a useful later instrument, but the table of five legal outcomes belongs in HTML and its boxes would make a figure out of words. Ledger: there is no monetary or numerical balance to close. | **Choose the docket** as one composed, measured strip, with an intentional temporal callback to Aula 07's real calendar: that page counts a deadline; this one reads dates already in a case record. Top to bottom: a small heading “Autos · Juizado Especial Cível · Florianópolis”; one linear month axis from Nov. 2012 through Jan. 2016; a blue record mark at “Compra · nov. 2012” shown as a month band because the source gives no day; a second blue mark at “Ação · 18 ago. 2015”; a third mark at “Decisão · 15 jan. 2016”; and one orange disposition stamp “Decadência reconhecida · ação extinta.” The span is measured in months; no 90-day scale or missing purchase date is invented. The paper uses no boxes or arrows. | “As datas já registradas conduzem a uma decisão de decadência neste caso; a conclusão concreta é art. 354/487, II, e não uma definição geral de quando art. 355 se aplica.” |

**Uniqueness tests.** **Swap:** replacing these three events with another docket changes both the intervals and outcome, so the sheet cannot illustrate a generic “processo pronto.” **Ledger:** no earlier Processo Civil figure is a docket; the one deliberate family callback is Aula 07's calendar, whose operation is counting a deadline, while this one traces the record of a real decision. **Object:** each mark is a date or disposition present in the actual judicial record. **Verb:** the reader traces chronology and reads the stamp; afterward they can distinguish “the judge decided on recorded dates” from “the statute's art. 355 route.” The date grid and positions still carry sequence and elapsed time without a caption; no row of words is being redrawn as a figure.

## A8. Cut list (and why)

- The fictional Oficina Rocha / Transportes Lima scenario: replace it with the actual Florianópolis decision, following F-022.
- The full list of preliminary acts after contestation: keep only the art. 353 threshold because the page's task begins when those measures have been completed or dispensed with.
- The international concentrated/diffuse comparison in Barbosa Moreira, Parte II: it does not help classify the Brazilian CPC routes taught here.
- The full treatment of partial judgment, appeal, liquidation, and enforcement: reduce to the art. 356 threshold and the one q. 10 test.
- Detailed hearing, joint organization, calendar, stabilizing effects, later burden-of-proof disputes, and new facts after stabilization: move out of this page's scope.
- The current partial-merits routing SVG: replace it; the course casting ledger marks pci-a10-s2 for redo, and its branch diagram belongs to the bounded art. 356 topic, not the central decision rule here.
- Any course overview, visible source list, invented “practice” rubric, or announcement of what a later lesson covers: none belongs on this page.

## A9. Failure modes for THIS lesson, with countermeasures

| Risk | Countermeasure |
|---|---|
| Treating the real judge's decadence disposition as a general rule or as an art. 355 holding | Label the case as a local record; classify its stated decadence under arts. 354 and 487, II; do not infer a broader holding. |
| The art. 355 section becomes a paragraph about speed instead of proof sufficiency | Use the statutory conditions as the section's spine; keep the two revelia conditions conjunctive. |
| Repeating a trap in multiple paragraphs and again in several quiz items (F-021) | A2 gives each trap one defusing location and exactly one quiz item. |
| Scope fence appears as page prose or creates a long list of lesson links (F-020) | Keep A3 planning-only; at most two short, concept-triggered hand-offs in the page. |
| A decision table is redrawn as labeled SVG boxes and arrows | Keep the outcome taxonomy as an HTML table. The only figure is a measured docket of real dates, not a flowchart. |
| The figure implies a precise day for the Nov. 2012 purchase or introduces an unsupported deadline | Display only the month band stated in the source; do not draw the CDC 90-day rule from this packet. |
| The hero becomes a set of empty corners, tiny labels, or a late scrolly panel | Compose around the three actual date marks; crop to the time strip; preserve clear label bands and the sole panel's “on” state. |
| The q. 10 boundary grows into a duplicate chapter on art. 356 | Keep §04 to the statutory threshold and the item the bank actually asks. |

## A10. Acceptance

For the later S5 page: slop_lint has 0 hard hits; check_all passes; breakscan reports 0 CROSS / 0 CLASH; the hero's “Leitura” matches the regenerated course-front clock; three random paragraphs are read aloud; the page and figure are checked at desktop and 375 px; every A6 hand-off is the real last idea of its section. The figure's labels carry no source citation, all legal claims map to A4, and no REF comments or scope-fence text leak onto the reader page.
