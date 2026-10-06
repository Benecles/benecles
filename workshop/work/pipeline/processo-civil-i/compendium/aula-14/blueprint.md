# Blueprint: Processo Civil I, Aula 14 (Teoria da prova: princípios e modelos)

<!-- PLANEJAMENTO S5a. Este arquivo define arquitetura, claims, fontes privadas e dispositivos; não contém prosa final para a página. -->

## A0. Inputs read, and what each one is for

| Input | Size | What I took from it |
|---|---:|---|
| S0 line (`course-map.json`, `aula-14.html`) | 1 lesson record | Contract: “Comparar os modelos de prova e usar os princípios para formular o problema probatório de um caso.” The full syllabus line also includes “Objeto da prova”; I include it in §02 although the shorter S0 `scope` array omits that phrase. Prerequisites are the two Aula 10 pages. |
| Slides (`10-slides.txt`) | 10 words; no content | S1 records: “[No slide source is mapped to this lesson in S1.]” There are no slide claims or slide pages to use. |
| K · assigned primary: `20-primary-001-knijnik-prova-caps1-2-assigned-reading.txt` | 19,311 words; PDF 1–24 | The selected opening pages set out the theoretical rationale, the demonstrative and persuasive/argumentative poles, their non-exclusive relation, and the distinction between a past event and an assertion about it (selected: PDF 1–8; printed pp. 3–17). Later pages develop standards of proof and examples beyond this lesson’s limits. |
| M · primary: `20-primary-002-marinoni-novo-curso-vol2-14.01.txt` | 9,514 words; PDF 234–251 | Selected PDF 234–246 (printed pp. 241–253) for function, object, and the right to prove; the article’s 9.4 onward material is not imported as a topic. |
| BM · supporting: `30-supporting-001-barbosa-moreira-temas-serie4-1989-11-alguns-problemas-atuais-da-p-9dbeb3ae.txt` | 7,100 words; PDF 155–172 | Selected PDF 155–159 for the right to proof, non-exhaustive means, and the balance between party participation and judicial activity; later debates on particular means and valuation remain outside the page. |
| D · supporting: `30-supporting-005-didier-curso-vol1-2017-ch11.txt` | 8,410 words; PDF 487–506 | Selected PDF 488–489 for cognition as considering, analyzing, and valuing allegations and evidence within a contradictory, cooperative procedure. |
| CPC extracts: `30-supporting-002-cpc-lei-13105-capture-2026-09-28-Art.-369.txt`; `30-supporting-003-cpc-lei-13105-capture-2026-09-28-Art.-370.txt`; `30-supporting-004-cpc-lei-13105-capture-2026-09-28-Art.-371.txt` | 50 + 38 + 32 words | The real statutory thread: means of proof; necessity and judicial initiative; reasoned evaluation. The operative words of arts. 369–371 are the legal anchor, not a hypothetical scenario. |
| Exam extract: `50-exercises-and-exams.txt` | 1,194 words; PDF 1–2 | This lesson’s index names P2 2015/1 questions 7 and 11 as retrieval practice: the open system of proof and the production of evidence concerning implausible facts. |
| Matching `exam-bank.json` entries | Q7 and Q11 | `exam-2015-1-avaliacao-2-q7` and `...-q11` are currently tagged `aula-15.html`, not Aula 14. The A14 compendium separately lists both in its exercise file as relevant; include them here, with Q7 limited to the principle in art. 369 and Q11 limited to the distinction needed to answer its prompt. |
| Live Aula 14 page | None; `page_state: planned`, `live_href: null` | `/Users/benecles/Developer/ordenacoes-filipinas/courses/processo-civil-i/aula-14.html` does not exist. This is a new page, not an edit of existing Aula 14 prose. |
| Reference blueprint and live reference page | `work/pipeline/controle-de-constitucionalidade/compendium/aula-01/blueprint.md`; live `courses/controle-de-constitucionalidade/aula-01.html` | Read the full reference and its Method notes plus all `REF ·` comments. Carry forward the reasoned choices: task-based reader brief; traps chosen before outlining; private claim locators; one tested thread; h2 plus lede skeleton; varied section rhythm; a worked application; hidden sourcing; planning-only scope fence; quiz items matched to traps. Do not copy Aula 01’s course overview, ruler, hypothetical laws, or page wording. |
| Protocols | `protocols/Source Pipeline.md` S5/S5a; `protocols/templates/Lesson Blueprint.md`; `protocols/Design Direction.md`; `protocols/Visual Genres.md`; `protocols/Visual Casting.md` | Use all template fields; plan one sitting; use a real, functional instrument and the Processo Civil world (petição, autos, docket, acts); no boxes joined by arrows, decorative marks, or arbitrary positions. |
| `BUGS.md` symptom search (`blueprint`, `panel`) | Read | No blueprint-specific A14 symptom. Existing panel findings concern late/hidden panels, oversized viewBoxes, and false-clean visual probes; these are build-stage checks, not reasons to add content here. |

The selected excerpts total about **17,000 words** for a **3,700-word** page: approximately **4.6:1**. The much larger carry-forward/background packet is not treated as page evidence. No factual claim below relies on the unmapped slide placeholder or on the old live page.

## A1. Reader brief

- **Already knows:** The earlier Aula 10 material on judgment on the merits and stabilization of the procedural organization. The S0 dependencies say evidence answers questions delimited by organization of instruction, and that the need for evidence affects whether to instruct or decide.
- **Can do after reading** (tasks, not topics):
  1. Given a proof question, distinguish a factual assertion about the past from the past event, the item or means offered to support it, and the judge’s conclusion.
  2. Compare the demonstrative and argumentative/persuasive models by stating what each contributes to a factual decision and why neither is an exclusive account of civil proof.
  3. Use arts. 369–371 to frame the problem: what factual assertion matters, what proof is proposed, why it is relevant to the merits, and what the judge must explain when deciding.
  4. Given the real P2 prompt about evidence concerning implausible facts, formulate the evidentiary problem without inventing a factual record, compare how each model reasons about it, and answer under arts. 369–371 without treating appearance as proof or proof as a guaranteed finding.
- **One sitting:** about 3,700 words, about 20 minutes. One lesson; no split.

## A2. Exam traps

| # | Trap | Why students fall for it | Where the page defuses it (one place) | Tested in (one item) |
|---|---|---|---|---|
| T1 | Treat the statutory catalogue as closed, or treat an unlisted means as automatically inferior. | A named procedural method can feel exhaustive; permission to use a means gets confused with its eventual weight. | §03, where art. 369 is read as an open rule bounded by legality and moral legitimacy. Do not expand into a survey of particular means. | Recap item 1: P2 2015/1 Q7. |
| T2 | Treat apparent implausibility as enough, by itself, to bar the production of evidence. | A first impression about likelihood collapses the factual assertion, the means offered, and the later evaluation into one judgment. | §06, in the worked reading of the exact Q11 prompt. State the distinction once, without promising admission of every requested measure. | Recap item 2: P2 2015/1 Q11. |

## A3. Scope fence (PLANNING ONLY, NEVER ON THE PAGE)

This fence determines what to leave out silently. It is not a paragraph, list, or roadmap for the reader.

- **Aula 15 — objeto da prova e admissibilidade:** detailed delimitation of factual propositions, admissibility criteria, and specific proof means. Aula 14 gives only the foundational definition and the art. 369 principle needed for the P2 question.
- **Aula 16 — valoração e modelos de constatação:** burdens or standards of proof and their thresholds. Aula 14 compares the broader argumentative and demonstrative models; it does not teach a standard-of-proof scale.
- **Aula 17 — ônus da prova:** allocation, dynamic distribution, and consequences of uncertainty.
- **Aula 18 — máximas da experiência e poderes instrutórios:** detailed use of experience and the court’s evidence powers. Aula 14 mentions art. 370 only as one orienting principle.
- **On-page boundary:** at most one short handoff after §06, with a link to Aula 15 if the answer raises the detailed admissibility of a particular means. No course overview, no list of adjacent lessons, and no announcement of what this page excludes.

## A4. Claim inventory (locators private; never on the page)

Aliases are defined in A0; each locator below is a PDF marker in that exact compendium file or an article marker in the CPC extract.

| # | Claim (full sentence) | Status | Locator | Carrier | § |
|---|---|---|---|---|---|
| 1 | Proof is part of the procedural activity by which the court can decide factual disputes, rather than a topic detached from judgment. | settled | K · PDF 3–4; M · PDF 234–236; D · PDF 488 | CPC art. 370 | 01 |
| 2 | Proof serves a truth-oriented inquiry, but judicial knowledge of past events is mediated by available information and fallible reasoning. | named position (Knijnik’s synthesis of Taruffo and related accounts) | K · PDF 4–8; M · PDF 234–239 | CPC arts. 370–371 | 01, 05 |
| 3 | The demonstrative model treats proof as an empirical basis for reconstructing the past event and drawing a factual conclusion. | named position | K · PDF 5–7 | CPC arts. 370–371 | 05 |
| 4 | The argumentative/persuasive model treats factual proof as justification developed through parties’ dialogue, with awareness of limits and possible error. | named position | K · PDF 5–8; D · PDF 488–489 | CPC arts. 369–371 | 05 |
| 5 | These models are poles that may coexist asymmetrically in different procedural institutions; the page must not present them as mutually exclusive systems. | named position (Knijnik) | K · PDF 5–8 | CPC arts. 369–371 | 05 |
| 6 | The object of judicial proof is not the past event itself but the factual assertion or account whose truth is at issue. | named position (Carrata via Knijnik; also Marinoni) | K · PDF 7; M · PDF 244–245 | Actual Q11 prompt | 02, 06 |
| 7 | Proof concerns factual assertions relevant to the merits; it does not turn every fact or legal proposition into an issue requiring evidence. | settled | M · PDF 244–245; D · PDF 489; CPC art. 370 | CPC art. 370 | 02, 04 |
| 8 | The right to prove is connected to access to justice, contradictory participation, and an adequate procedure. | settled | K · PDF 3; M · PDF 245–246; BM · PDF 155–156; D · PDF 488 | CPC art. 369 | 03 |
| 9 | Article 369 permits legal and morally legitimate means even when the Code does not specify them. | statute | `30-supporting-002-cpc-lei-13105-capture-2026-09-28-Art.-369.txt`, `===== Art. 369 =====`; BM · PDF 155–156 | Actual text of art. 369 | 03 |
| 10 | Article 370 allows the judge to determine necessary evidence on request or on the judge’s own initiative, and requires reasons to refuse useless or merely dilatory measures. | statute | `30-supporting-003-cpc-lei-13105-capture-2026-09-28-Art.-370.txt`, `===== Art. 370 =====`; BM · PDF 157–159 | Actual text of art. 370 | 04 |
| 11 | Article 371 requires the judge to evaluate evidence irrespective of who produced it and to state the reasons for the resulting conviction. | statute | `30-supporting-004-cpc-lei-13105-capture-2026-09-28-Art.-371.txt`, `===== Art. 371 =====`; K · PDF 8 | Actual text of art. 371 | 04–05 |
| 12 | P2 2015/1 Q7’s correct alternative is that, as a general rule, the Brazilian civil process permits means not expressly regulated in the CPC; that statement does not make every means admissible or automatically weight-equivalent in a particular case. | exam answer / statute | `50-exercises-and-exams.txt`, `===== p. 2 (PDF 2) =====`, Q7; `exam-bank.json`, `exam-2015-1-avaliacao-2-q7`; CPC art. 369 | The exact exam question | 03; recap 1 |
| 13 | P2 2015/1 Q11 asks whether evidence may be produced about implausible facts; the answer distinguishes the opportunity to prove from the later evaluation of the evidence. | exam answer / settled for this limited answer | `50-exercises-and-exams.txt`, `===== p. 2 (PDF 2) =====`, Q11; `exam-bank.json`, `exam-2015-1-avaliacao-2-q11`; CPC arts. 369–371 | The exact exam prompt | 06; recap 2 |

## A5. The thread (how it was chosen)

**Chosen:** CPC art. 370, read in its real statutory setting beside arts. 369 and 371. The operative terms are “provas necessárias”, “de ofício ou a requerimento”, and refusal of measures “inúteis ou meramente protelatórias” only in a reasoned decision. No facts or litigants are invented. The article’s real limits recur as the lesson asks what is being proved, why it matters, how the parties and judge participate, and how the decision is justified.

| Candidate | §01 function | §02 object | §03 principles | §04 initiative | §05 models | §06 application | Verdict |
|---|---|---|---|---|---|---|---|
| CPC art. 370, with arts. 369/371 as adjacent provisions | ✓ evidence is tied to deciding the merits | ✓ “necessary” anchors factual relevance | ✓ party request and lawful means | ✓ own motion, necessity, reasoned refusal | ✓ evidence and reasons appear together in actual law | ✓ applied to the actual Q11 prompt without adding facts | **Chosen**; one real statutory thread survives every section. |
| CPC art. 369 | ~ provides a right to use legitimate means | ~ concerns proof of factual assertions | ✓ strongest for open means | ✗ does not state the court’s necessity/refusal test | ~ gives a party-facing evidentiary premise | ~ useful to the short answer | Rejected as sole thread; narrower than the whole lesson. |
| CPC art. 371 | ~ connects evidence with judicial decision | ~ can be linked to what is evaluated | ~ supports reasoned assessment | ~ controls evaluation, not initiation | ✓ strongest for rational evaluation | ~ supports the answer’s later-evaluation distinction | Rejected as sole thread; begins after the question of what proof is needed. |

The variations are statutory rather than fictional: request versus own initiative; necessary versus useless or merely dilatory; support for a factual assertion versus reasons stated in the decision. The exam prompt is the single authentic application. It supplies no underlying fact pattern, so the plan will not manufacture one.

## A6. Section plan

| § | h2 (names content) | The question it answers | Claims (A4 #) | Carrier | Form (figure / prose-only / table / case) | Words | Hands to the next § |
|---|---|---|---|---|---|---:|---|
| hero | **Prova como decisão** | What makes evidence part of a civil judgment? | 1, 10 | CPC art. 370, with a short exact statutory excerpt | Hero deck function + real statutory text; no course overview | 100 | “Necessary to judgment” raises what, exactly, has to be established. |
| 01 | **Para que serve a prova?** | How does proof help a court decide a factual dispute without claiming direct access to the past? | 1–2 | Art. 370 as the thread; K · PDF 3–8; M · PDF 234–239 | Prose-only; concrete legal question first, then function and epistemic limit | 500 | If the inquiry is about a past event, separate that event from what a party says happened. |
| 02 | **O que é objeto da prova?** | What is the thing a court can assess through evidence? | 6–7, 13 | Art. 370 “necessárias”; K · PDF 7; M · PDF 244–245; D · PDF 489 | Prose plus a compact HTML comparison table: event / factual assertion / evidentiary item / judicial conclusion; not a drawn flow | 500 | The object is a factual assertion; the next question is what rights and constraints govern its proof. |
| 03 | **Direito à prova e meios legítimos** | What room do the parties have to support factual assertions? | 8–9, 12 | Art. 369; BM · PDF 155–156; M · PDF 245–246; actual P2 Q7 | Prose + one genuine parallel table only if needed to distinguish “means permitted” from “weight later assigned” | 525 | The right to propose evidence does not itself decide whether the measure is necessary or how the court must handle it. |
| 04 | **Iniciativa, necessidade e razões** | Who may trigger evidence, and what must a decision say? | 10–11 | Art. 370, with art. 371; BM · PDF 157–159; K · PDF 8 | Prose-only; quote only the operative statutory words | 500 | The rules constrain the court’s inquiry; models explain what kind of knowledge that inquiry seeks and how it is justified. |
| 05 | **Reconstruir e justificar** | What does each model add to a decision about facts? | 2–5, 11 | K · PDF 5–8; D · PDF 488–489; arts. 369–371 | Comparison table in HTML prose structure plus the single score instrument in A7; no boxes-and-arrows figure | 550 | Both models can be used together; the reader can now frame a concrete proof question without turning either model into a guarantee. |
| 06 | **Uma pergunta probatória em exame** | How can the principles and models be used to answer the actual question about implausible facts? | 6, 8–13 | Actual P2 2015/1 Q11; K · PDF 7–8; M · PDF 244–246; CPC arts. 369–371 | Worked reading of the original prompt, not an invented fact pattern; run-in steps: assertion, model, principle, reasoned response | 550 | The answer’s distinctions become the reader’s short checklist for the recap. |
| ↺ | **Recapitulação** | Can the reader use the proof principles to formulate a problem and compare the two models in a reasoned answer? | 2–5, 8–13 | Actual P2 2015/1 Q7 and Q11; arts. 369–371 | One-breath chave + two quiz items. Item 1 is Q7. Item 2 uses Q11 as a composite task: state what the prompt supplies and which factual details it omits; formulate the proof question under arts. 369–371 without adding facts; compare what the demonstrative model asks about evidence and inference with what the argumentative/persuasive model asks about dialogue and reasons; then answer the exam question in a short reasoned conclusion. | 350 | — |

**Total:** about 3,575 words including hero and recap; revise the estimate to **3,600–3,700 words** during writing, within one sitting. The six content sections stay near the reference’s 250–550-word rhythm; no second long stretch without a change in form. The single comparison table is real parallel content, not a figure. Q7 tests T1. The single composite Q11 item tests T2 and requires, in the answer itself, both problem formulation and a reasoned comparison of the two syllabus models using the mapped principles; these are mandatory parts of the closing task, not optional extensions.

## A7. Figures: the cast

One figure only: the hero establishes it and §05 returns to the same composition. The figure is a working **score**, a Visual Genres form for multiple actors and operations over the course of a real procedural sequence. It is neither an SVG list of words nor text in boxes joined by arrows.

| Fig | Move | Cast (chosen) | Rejected casts and why | Uniqueness tests | The sheet, described | Card claims |
|---|---|---|---|---|---|---|
| Hero + Fig. 1 · “A decisão sobre a prova” | For each real statutory measure, select a model lens and identify the question that lens makes visible; compare both lenses on the same measure. | **Score** from Processo Civil’s actual materials: arts. 369–371 as three ordered measures, with the two models as staves. The instrument takes the reader from a statutory term to the distinct inquiry each model frames. | **Dossier:** a folder around Q11 could hold prompt and answer, but Processo Civil’s casting ledger already uses `pci-a08-s2+2` for a contestation dossier; it would repeat a passive folder and would not show the two models at work. **Annotated form:** plausible for art. 370, but `pci-a01-s2+2` already uses a form for the initial petition; a second form would repeat a family and show a checklist rather than the models’ relation. **Text facsimile alone:** it is a real object, but the reader would only look at it; retain the operative text in the hero, not as the figure. | **Swap:** pass only with these exact statutory measures and the two models; changing labels to another topic would remove the article-specific sequence. **Ledger:** no score form is listed for Processo Civil I; existing forms, docket, case folder, and calendar serve other moves. **Object:** arts. 369, 370, and 371 are the actual legal text; Q11 is the authentic prompt, with no invented litigants. **Verb:** select, answer, compare. The result is a reader-generated pairing of one statutory operation with each model’s question, making their distinct but complementary work inspectable. | On a 600-pixel sheet, two horizontal staves, not panels of boxes. The upper staff is **demonstrativo**; the lower is **argumentativo/persuasivo**. Four shared measures carry the actual legal anchors: **369** · “meios legais / moralmente legítimos”; **370** · “a requerimento / de ofício”; **370** · “necessárias / inúteis ou meramente protelatórias”; **371** · “independentemente de quem produziu / razões na decisão”. At measure **369**, selecting the upper staff asks which factual assertion a legitimate means could support; selecting the lower asks who may put that support into the process and contest it. At the first **370** measure, the upper asks what proof could matter to deciding the merits; the lower asks who may trigger the measure. At the second **370** measure, the upper asks what inferential gap a necessary measure could address; the lower asks what reason supports ordering or refusing it. At **371**, the upper asks what conclusion the record supports; the lower asks which reasons for that conclusion must be stated. The reader activates a measure, selects either staff, and then switches to the other without changing the legal text. The visible prompt changes; the answer remains the reader’s work. The result is a completed comparison of the two models over the same statute, not an automatic legal verdict. The orange ink marks necessity and the refusal limit; blue marks the contrast between party request and own initiative; other marks show statutory order only. No mark purports to measure weight, certainty, or elapsed time. Both staves remain visible by default and in print; the controls enhance rather than gate the information. At 390 px the score reflows as two stacked staves in the same order. No boxes-and-arrows, no decorative marks, no invented evidence fact. | “A mesma regra pode ser lida como pergunta sobre reconstrução e como exigência de justificação contraditória; comparar as duas leituras mostra por que os modelos são complementares.” The figure carries this claim through the same measures aligned across both staves. |

**Instrument test:** after removing every text node, the remaining measures still encode the statutory order 369 → 370 → 370 → 371 and the aligned operations. If the geometry no longer communicates sequence and comparison, the figure is cut or recast; it is not rescued by calling it a score. The interaction must work without JavaScript (both staves default visible), at 390 px, in both themes, and in print.

## A8. Cut list (and why)

- No Aula 01-style course overview: Aula 14 opens on art. 370’s actual problem.
- No claim that the court reaches an absolute or “real” truth. The sources support truth-oriented inquiry, mediated reconstruction, and fallibility.
- No complete list of facts that do not need proof, secondary/indiciary facts, or detailed boundaries of the object of proof; the syllabus needs the foundational object, not a taxonomy.
- No catalogue or treatment of documentary, oral, expert, digital, or other specific means. Q7 earns only the general art. 369 principle.
- No burden allocation, dynamic burden, models-of-constatação thresholds, standards of proof, experience maxims, or detailed powers of the judge.
- No historical tour of ordeals or comparative civil/penal/tributary systems. These would consume the sitting and distract from the two syllabus models.
- No invented parties, facts, countries, or evidence request. The actual Q11 prompt contains no fact pattern; its limits are kept visible to the writer.
- No visible source list, file names, page numbers, slide references, or narration about the reading packet. Locators remain in the private blueprint and source ledger.

## A9. Failure modes for THIS lesson, with countermeasures

| Risk | Countermeasure |
|---|---|
| The S0 `scope` array omits “Objeto da prova,” although the syllabus line includes it. | Keep §02 and claim rows 6–7; the full syllabus line governs coverage. |
| “Argumentativo” is treated as a separate model from the source’s “persuasivo,” or as mere rhetorical victory. | Name it “argumentativo/persuasivo” on first use; preserve Knijnik’s caution, fallibility, and dialogue. Do not present a strict either/or. |
| The two models are confused with standards/models of constatação. | Compare the models’ accounts of how evidence supports factual decisions; leave threshold levels to their own later syllabus line. |
| Q7’s general rule is expanded into a promise that every unlisted or unusual means must be admitted. | Keep the exact legal/moral boundary of art. 369; explain the exam trap once in §03 and test it once in recap item 1. |
| Q11 becomes “implausible facts always must be admitted,” or is repeated as a hedge in several sections. | State only that implausibility alone does not settle the evidence question; retain art. 370’s necessity and reasoned-refusal limits. Explain once in §06; test once in recap item 2. |
| A made-up lawsuit is inserted to make the theory feel concrete. | Use arts. 369–371 and the real Q11 prompt. The prompt supplies no factual record, so the worked answer must not invent one. |
| The figure becomes a labelled flowchart or a table disguised as art. | Keep parallel score staves and statutory measures; no boxes, arrows, arbitrary strengths, or text-only cells. The position and alignment must carry the claim. |
| Missing slide material encourages invented teacher emphasis. | The deck is explicitly unmapped; the syllabus line, selected book passages, statute, and exam questions govern. |
| Page reveals its sourcing or planning process. | Keep source locators hidden; no “slides,” “materiais,” “nesta leitura,” or scope-fence paragraph in page prose. |

## A10. Acceptance

For the later page-writing stage: `slop_lint` has 0 hard hits; `check_all` passes; breakscan has 0 CROSS / 0 CLASH; the reading clock matches the course front after regeneration; three random paragraphs are read aloud; the page is inspected at 1512 px and 375/390 px, light and dark; the score remains legible and its default state works without JavaScript; every section handoff is the actual final idea of the section. These are planned acceptance checks, not checks performed on this planning-only file.
