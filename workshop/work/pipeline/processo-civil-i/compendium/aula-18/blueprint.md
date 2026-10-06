# Blueprint: Processo Civil I, Aula 18 (Máximas de experiência e poderes instrutórios do juiz)

## A0. Inputs read, and what each one is for

| Input | Size | What I took from it |
|---|---:|---|
| S0 line (`course-map.json`) | 1 entry | **Learning outcome, verbatim:** “Identificar o papel das máximas de experiência e justificar o alcance da iniciativa probatória judicial.” Contract for the page. The syllabus line is “Ônus da Prova. Máximas da Experiência. Poderes Instrutórios do Juiz.” |
| Slides (`10-slides.txt`) | 10 words | No slide source is mapped to this lesson; do not invent a professor-specific framing. |
| Primary (`20-primary-001-marinoni-novo-curso-vol2-14.02.txt`) | 13,891 words; PDF 252–278 | Full assigned compendium chapter. §9.4.3 supplies the short carry-forward on unresolved doubt; §§9.5.1–9.5.2 separate facts not requiring proof from experience rules; §9.6 addresses the judge’s power to take evidence. |
| Selected support (`30-supporting-002-barbosa-moreira-temas-serie4-1989-05-os-poderes-do-juiz-na-direca-ed113342.txt`) | 3,019 words; PDF 55–62 | A bounded account of the judge’s active role and why taking evidence on the judge’s own initiative is not, by itself, incompatible with impartiality. Use its reasoning in §05, not as a second course overview. |
| CPC extracts | 8 article files; 335 words | Arts. 2, 9, 10, 369–371, 374 and 375 give the exact statutory controls for process initiative, hearing, proof rights, evaluation, notoriety and experience rules. Read and cite at article level. |
| Matching exam/exercise material | 1 relevant prompt | No exam-bank appearance is tagged to `aula-18.html`. The compendium includes 2015/1 Avaliação 2, Q11; the bank maps it to Aula 15 but records its overlap with valuation and experience rules. Include Q11 once as the final application and identify it honestly as a cross-topic question. |
| Compendium index (`00-index.md`) | 26 rows | Confirms each source’s role and locator; the primary chapter is the direct source, while background chapters mostly carry material from prior lessons. |
| Live page before | 0 words | S0 sets `page_state: planned`, `route_status: new-planned-lesson`, and `live_href: null`; no Processo Civil I `aula-18.html` exists to preserve, replace or cut. Add a full new lesson page. |
| Reference blueprint and live reference page | 153-line blueprint; 1 page | Read the Aula 01 Method notes and the reference page at `work/staging/courses/controle-de-constitucionalidade/aula-01.html`. The HTML in this checkout has no `REF ·` comments; use the Method notes and visible page structure, and do not claim a comment-specific instruction. |

Selected writing set: about **17,311 source words : 3,200 target words = 5.4:1**. This counts the full direct primary chapter, the selected supporting chapter, the eight short CPC extracts, and the Q11 prompt/answer. It excludes unneeded peer notes and background chapters rather than treating the entire 96k-word compendium as required reading.

## A1. Reader brief

- **Already knows:** Aula 14’s principles and models of proof; Aula 16’s valuation and standards of proof; Aula 17’s allocation of the burden and its role when factual doubt remains.
- **Can do after reading** (tasks a question could ask):
  1. Distinguish a fact that is notorious from a rule of experience and say what each does in the proof process.
  2. Explain how a common or technical experience rule may support an inference without turning a generalization into proof of a particular fact.
  3. Separate the party’s initiative to begin the process from the judge’s authority to order evidence within it, and explain what the burden still does if doubt remains.
  4. Justify an evidentiary order by reference to necessity and explain how hearing and impartiality constrain its use.
  5. Answer 2015/1 Avaliação 2, Q11: whether proof may be produced about implausible facts, distinguishing production from valuation.
- **One sitting:** about 3,200 words, 16–25 minutes. The closing five-item set tests each task once; Q11 is the one sourced exam item.

## A2. Exam traps

| # | Trap | Why students fall for it | Where the page defuses it (one place) | Tested in (one item) |
|---|---|---|---|---|
| T1 | Treating a fact notorious to the relevant public as the same thing as a rule of experience | Both sound like ordinary knowledge, and Arts. 374 and 375 sit next to each other | §02, where the page contrasts the case-level fact with the general rule used to reason about facts | Closing item 1 |
| T2 | Treating a familiar or technical generalization as proof of the particular fact | A familiar pattern can feel self-evident even when the record does not establish it | §03, where the page traces the inference and keeps the reason attached to the evidence in the record | Closing item 2 |
| T3 | Reading “impulso oficial” as permission for the judge to start a case | “Official initiative” is used for two different procedural moments | §04, by reading Arts. 2 and 370 together | Closing item 3 |
| T4 | Assuming that the judge’s own evidentiary initiative necessarily makes the judge partial | One side may benefit from the new evidence, while the unresolved uncertainty had already benefited the other | §05, with Barbosa Moreira’s bounded argument and the hearing rules | Closing item 4 |
| T5 | Treating implausibility alone as an automatic bar to producing evidence | Students collapse admissibility, necessity and evidentiary weight | §06, through the exact question in Q11 | Closing item 5 (Q11) |

Each trap is handled at its listed point and tested once. The rest of the page uses the distinctions without re-announcing them.

## A3. Scope fence (PLANNING ONLY, NEVER ON THE PAGE)

This fence is a private cut instruction. Do not print it, paraphrase it as a course map, or add section prose about which class owns a topic. On the page, use no boundary sentence unless a reader would otherwise mistake the present discussion for full treatment of a neighboring topic.

- General principles and models of proof → Aula 14. Carry only what is needed to place the judge’s evidentiary initiative.
- Admission, legality and types of evidence → Aula 15. Use Q11 only to separate the possibility of producing proof from its later valuation.
- Valuation and standards of proof → Aula 16. Explain only how experience rules enter the reasoning and the need to give reasons.
- Allocation and dynamic distribution of the burden → Aula 17. Recall only the consequence of factual doubt that remains after the evidence is evaluated.
- Collaboration duties of parties and third parties under CPC Arts. 378–380 are outside this lesson’s stated scope; do not expand the page into a catalogue of duties.

## A4. Claim inventory (locators private; never on the page)

| # | Claim (full sentence) | Status | Locator | Carrier | § |
|---|---|---|---|---|---|
| 1 | CPC Art. 375 directs the judge to apply common experience rules drawn from what ordinarily happens and technical experience rules, subject to the statutory reservation concerning expert examination. | statute | `30-supporting-012-cpc-lei-13105-capture-2026-09-28-Art.-375.txt`, Art. 375 | CPC Art. 375 | 02–03 |
| 2 | CPC Art. 374(I) exempts notorious facts from proof; the exemption concerns a fact in the case, not the generalization used to reason about facts. | statute / settled distinction | `30-supporting-011-cpc-lei-13105-capture-2026-09-28-Art.-374.txt`, Art. 374(I); primary §9.5.1–9.5.2, pp. 276–278 (PDF 269–271) | CPC Arts. 374–375 | 02 |
| 3 | Marinoni describes rules of experience as generalizations, notions and criteria from worldly experience that help the judge reason about proof and facts; unlike the fact itself, the rule need not be alleged by a party. | named position | `20-primary-001-marinoni-novo-curso-vol2-14.02.txt`, §9.5.2, pp. 276–278 (PDF 269–271) | Art. 375 | 02–03 |
| 4 | CPC Art. 371 requires the judge to evaluate the evidence in the record regardless of who produced it and to state the reasons for the resulting conviction. | statute | `30-supporting-010-cpc-lei-13105-capture-2026-09-28-Art.-371.txt`, Art. 371 | CPC Art. 371 | 03, 05–06 |
| 5 | The burden rule serves as a way to decide when factual doubt remains after the evidentiary activity; it does not itself establish what evidence is necessary. | settled | `20-primary-001-marinoni-novo-curso-vol2-14.02.txt`, §9.4.3, p. 263 (PDF 256); §9.6, p. 285 (PDF 278) | CPC Art. 370 | 01, 04 |
| 6 | CPC Art. 2 says the process begins on a party’s initiative and proceeds by official impetus, subject to legal exceptions. | statute | `30-supporting-005-cpc-lei-13105-capture-2026-09-28-Art.-2.txt`, Art. 2 | CPC Arts. 2 and 370 | 04 |
| 7 | CPC Art. 370 authorizes the judge, on the judge’s own initiative or at a party’s request, to determine evidence necessary to decide the merits; Marinoni’s §9.6 notes the bar on useless or dilatory diligence. | statute | `30-supporting-009-cpc-lei-13105-capture-2026-09-28-Art.-370.txt`, Art. 370; primary §9.6, p. 285 (PDF 278) | CPC Art. 370 and sole paragraph | 01, 02, 04–06 |
| 8 | CPC Art. 369 gives the parties the right to employ legal and morally legitimate means of proof, including means not specified in the Code. | statute | `30-supporting-008-cpc-lei-13105-capture-2026-09-28-Art.-369.txt`, Art. 369 | CPC Arts. 369–370 | 04, 06 |
| 9 | CPC Arts. 9 and 10 require prior hearing before an adverse decision and an opportunity to address a ground used by the judge, including a matter to be decided ex officio. | statute | `30-supporting-006-cpc-lei-13105-capture-2026-09-28-Art.-9.txt`, Art. 9; `30-supporting-007-cpc-lei-13105-capture-2026-09-28-Art.-10.txt`, Art. 10 | CPC Arts. 9–10 | 05 |
| 10 | Barbosa Moreira argues that the use of statutory evidentiary powers is not, by itself, incompatible with impartiality; his discussion keeps the inquiry within the dispute submitted to the court. | named position | `30-supporting-002-barbosa-moreira-temas-serie4-1989-05-os-poderes-do-juiz-na-direca-ed113342.txt`, §3, pp. 46–47 (PDF 56–57) | CPC Art. 370 | 05 |
| 11 | The answer recorded for Q11 is yes: implausibility may affect valuation but does not by itself exclude production; the means must still be pertinent and lawful, and the court may reject useless or dilatory diligence. | settled exam answer | `exam-bank.json`, `exam-2015-1-avaliacao-2-q11`, verified answer; `50-exercises-and-exams.txt`, p. 2 (PDF 2); CPC Arts. 369–371 and 375 | Actual Q11 | 06 |

## A5. The thread

**Chosen:** CPC Art. 370 and its sole paragraph, carried through the exact statutory terms “provas necessárias” and “diligências inúteis ou protelatórias”; the real Q11 supplies the final variation without adding a fact pattern. Art. 375 is the local companion that shows how a judge reasons about the record while deciding what evidence is needed.

| Candidate | §01 | §02 | §03 | §04 | §05 | §06 | Verdict |
|---|---|---|---|---|---|---|---|
| CPC Art. 370 + its sole paragraph | ✓ burden resolves residual doubt after evaluation | ✓ experience affects what the record may establish | ✓ Art. 371 gives reasons for valuation | ✓ direct source of authority and limit | ✓ exercised with hearing safeguards | ✓ applied to the real exam prompt | **Chosen**; one real rule carries the plan from residual doubt to the final proof question |
| CPC Art. 375 | ~ no burden rule | ✓ common/technical rules | ✓ inference and evaluation | ~ not the source of evidentiary initiative | ~ no direct impartiality rule | ✓ useful to the answer | Local source, but too narrow to carry the lesson’s full syllabus line |
| CPC Art. 2 | ~ | ~ | ~ | ✓ distinguishes starting the process from its official development | ~ | ~ | Local contrast in §04; cannot carry maxims, valuation or Q11 |
| Exam 2015/1 Q11 | ~ | ~ | ~ | ~ | ~ | ✓ exact final question | Capstone only; it is a real exam prompt, not a through-line for the whole lesson |

Tested candidates against every section; no hypothetical law, jurisdiction, litigant or fact pattern. Art. 370’s statutory verbs and limits are the recurring object, not a fictional case.

## A6. Section plan

| § | h2 (names the content) | The question it answers | Claims (A4 #) | Carrier | Compendium locator | Form | Words | Hands to the next § |
|---|---|---|---|---|---|---|---:|---|
| 01 | **A dúvida que resta** | What does the burden rule do after the evidence has been evaluated? | 5, 7 | Art. 370 is the thread: it concerns evidence needed before the merits are decided; the burden rule addresses the remaining doubt after evaluation. | `20-primary-001-marinoni-novo-curso-vol2-14.02.txt`, §9.4.3, p. 263 (PDF 256), and §9.6, p. 285 (PDF 278) | Prose-only; one short recall line | 400 | Once the burden is placed after evaluation, the next question is what counts as a fact to prove and what is a rule for reasoning. |
| 02 | **Fato notório e regra de experiência** | Is this a case-level fact that need not be proved, or a general rule used to reason about facts? | 1–3, 7 | Art. 370’s necessity question depends on what must be established; Arts. 374 and 375 separate the fact from the inferential rule. | `20-primary-001-marinoni-novo-curso-vol2-14.02.txt`, §§9.5.1–9.5.2, pp. 276–278 (PDF 269–271); `30-supporting-011-cpc-lei-13105-capture-2026-09-28-Art.-374.txt`, Art. 374(I); `30-supporting-012-cpc-lei-13105-capture-2026-09-28-Art.-375.txt`, Art. 375 | Short HTML contrast table + lex excerpt; no figure | 550 | The distinction identifies the kind of proposition; next show how an experience rule supports evaluation without becoming the case fact itself. |
| 03 | **A máxima como razão de avaliação** | How does experience enter the judge’s reasoning about evidence? | 1, 3, 4 | Art. 375’s common/technical distinction; Art. 371’s duty to state the reasons connecting the record to the conclusion. | `20-primary-001-marinoni-novo-curso-vol2-14.02.txt`, §9.5.2, pp. 276–278 (PDF 269–271); `30-supporting-012-cpc-lei-13105-capture-2026-09-28-Art.-375.txt`, Art. 375; `30-supporting-010-cpc-lei-13105-capture-2026-09-28-Art.-371.txt`, Art. 371 | Prose-only | 500 | If the record still needs support, ask what the judge may do while the merits remain undecided. |
| 04 | **O que o art. 370 permite** | Who may trigger the production of evidence, and what is the power for? | 6–8, 5, 7 | The real statutory contrast is process initiative under Art. 2 versus evidentiary initiative under Art. 370; Art. 369 preserves the parties’ proof rights. | `20-primary-001-marinoni-novo-curso-vol2-14.02.txt`, §9.6, p. 285 (PDF 278); `30-supporting-005-cpc-lei-13105-capture-2026-09-28-Art.-2.txt`, Art. 2; `30-supporting-008-cpc-lei-13105-capture-2026-09-28-Art.-369.txt`, Art. 369; `30-supporting-009-cpc-lei-13105-capture-2026-09-28-Art.-370.txt`, Art. 370 | Figure 1, followed by prose | 600 | The authority is tied to deciding the merits; the next section states how its use remains answerable to the parties. |
| 05 | **Contraditório e imparcialidade** | How can the judge order evidence while preserving participation and impartiality? | 4, 7, 9, 10 | Arts. 9–10 require opportunity to be heard; Barbosa Moreira’s argument explains why initiative alone does not establish partiality. | `30-supporting-006-cpc-lei-13105-capture-2026-09-28-Art.-9.txt`, Art. 9; `30-supporting-007-cpc-lei-13105-capture-2026-09-28-Art.-10.txt`, Art. 10; `30-supporting-002-barbosa-moreira-temas-serie4-1989-05-os-poderes-do-juiz-na-direca-ed113342.txt`, §3, pp. 46–47 (PDF 56–57); `30-supporting-010-cpc-lei-13105-capture-2026-09-28-Art.-371.txt`, Art. 371 | Prose-only + lex block | 500 | A valid initiative still needs a fact-specific reason; put that distinction to the sourced exam question. |
| 06 | **A questão 11: fatos inverossímeis** | Is proof about an implausible fact possible, and what can the question establish? | 1, 4, 7, 8, 11 | The exact prompt asks a general question, not for a case-specific necessity ruling. It is the fifth and final exercise: answer the possibility once, then separate admissibility, need and later weight. | `50-exercises-and-exams.txt`, Q11, p. 2 (PDF 2); `exam-bank.json`, `exam-2015-1-avaliacao-2-q11`, verified answer; `30-supporting-008-cpc-lei-13105-capture-2026-09-28-Art.-369.txt`, Art. 369; `30-supporting-009-cpc-lei-13105-capture-2026-09-28-Art.-370.txt`, Art. 370; `30-supporting-010-cpc-lei-13105-capture-2026-09-28-Art.-371.txt`, Art. 371; `30-supporting-012-cpc-lei-13105-capture-2026-09-28-Art.-375.txt`, Art. 375 | Actual case-folder question, as closing item 5; no earlier worked answer | 650 | The answer ends with the boundary between possibility of proof, case-specific necessity and valuation. |
| | | | | | **Total** | | **3,200** | |

### Callouts and devices

- **Lex block, Art. 375 (§02–03):** its exact words set out common and technical experience and the expert-examination reservation; earns space because those words define the lesson’s first distinction.
- **Contrast table (§02):** one row for the case fact under Art. 374(I), one for the general rule under Art. 375. This is text comparison, so it stays an HTML table rather than a drawn figure.
- **Recall line (§01):** one sentence places burden at the remaining-doubt stage; do not reopen allocation or dynamic distribution.
- **Lex block, Art. 370 (§04):** the real procedural rule names who may act and the purpose of the act; the companion figure makes the reader operate on its threshold.
- **Case folder (§06):** preserve Q11’s exact wording and answer it with the statutory distinctions. It is the closing exercise because it is the only exam-bank item selected into this compendium.

## A7. Figures: the cast

| Fig | Move | Cast list and uniqueness tests | Choice and the sentence that sells it | The sheet, described top to bottom | Card claims |
|---|---|---|---|---|---|
| 1 · Art. 370 | Locate the statutory terms that authorize an evidentiary order and distinguish them from the terms that limit it. | **Candidate A · official-document specimen (chosen):** exact Art. 370 text with a native selector that highlights “necessárias” or the sole-paragraph boundary described in §9.6. **Swap:** the tested wording is specific to evidentiary powers, not a relabelable generic process chart. **Ledger:** no earlier Processo figure uses this legal object; it differs from Aula 01’s petition form and Aula 07’s calendar. **Object:** the real Art. 370 text. **Verb:** select each statutory condition and see the distinct legal role it plays. <br><br> **Candidate B · case folder:** the real Q11 prompt and response line. **Swap:** Q11 is unique, but the folder form could be reused for any case. **Ledger:** case/document forms already appear in Aulas 01 and 08. **Object:** real prompt, but no request or factual record is stated. **Verb:** answer, but it cannot show the judge’s necessity boundary by itself. Use as the textual case folder in §06, not as the figure. <br><br> **Candidate C · procedural calendar/docket:** dated entries leading to a decision on evidence. **Swap:** generic across procedural topics. **Ledger:** repeats Aula 07’s calendar cast. **Object:** Q11 has no dates or sequence of acts. **Verb:** asks the reader to trace chronology where the statute gives a conditional threshold; reject. | **Choose A:** only the actual statutory instrument lets the reader inspect the real condition without invented parties, facts or case outcomes. | Header `CPC · ART. 370`; the actual caput, retaining `de ofício ou a requerimento da parte`; below it the phrase `provas necessárias ao julgamento do mérito`, with `necessárias` in the tested orange ink. A distinct line names the sole-paragraph boundary as `diligências inúteis ou protelatórias` (paraphrase anchored to primary §9.6, not a verbatim statute quotation). A native selector changes which phrase is highlighted; the full text remains visible in both states. No arrows, nodes or ruled sentence boxes. | “O art. 370 liga a iniciativa probatória à necessidade de decidir o mérito e exclui a diligência inútil ou protelatória.” |

## A8. Cut list (and why)

- **Live-page action:** keep none; replace none; add the full new `aula-18.html`; cut none from a legacy page because none exists.
- No second lesson on burden allocation or dynamic distribution; one brief carry-forward is enough for the syllabus line.
- No full models of proof, valuation standards, admissibility, typified evidence or proof rights; use only the bridges needed to place maxims and initiative.
- No catalogue of every Art. 374 category; notoriety alone is needed for the Art. 375 distinction.
- No extended debate over principle dispositif, third-party cooperation or Arts. 378–380; those materials exceed the stated lesson task.
- No invented lawsuit, parties, evidence request or result. The real statute and Q11 carry the thread.
- There is no legacy Aula 18 text to retain or cut; the route is new-planned.

## A9. Failure modes for THIS lesson, with countermeasures

| Risk | Countermeasure |
|---|---|
| The short burden recall becomes a second Aula 17 | Cap §01 at 400 words; state only the residual-doubt function and move on. |
| “Experience” becomes the judge’s personal intuition | Keep the generalization distinct from the particular fact; connect it to the record and Art. 371’s reasons. |
| The technical-experience clause is described as a substitute for expert examination | Quote Art. 375’s reservation accurately and keep it at the point where technical experience is introduced. |
| Art. 370 is presented as authority to start a case or search beyond the dispute | Read Arts. 2 and 370 side by side; keep the purpose tied to the merits and evidence necessary to decide them. |
| Initiative is treated as automatic bias or automatic neutrality | Present Barbosa Moreira as a named argument, pair it with Arts. 9–10, and make no claim that an improper use is harmless. |
| Q11 receives a fact-specific order despite containing no fact pattern | Answer only what Q11 asks; leave necessity of a particular evidentiary measure to an actual record. |
| The figure turns the statute into boxes connected by arrows | Use the actual statutory text and a native highlight selector; the operation is reading the terms, not following a diagram. |
| Scope-fence text leaks onto the reader’s page | Keep A3 private; `slop_lint` catches planning/backstage phrases. |
| A trap is repeated across the body and the quiz | A2 assigns one defusing section and one closing item to each trap; follow that mapping literally. |

## A10. Acceptance

For the later page build: `slop_lint` 0 hard findings · `check_all` PASS · breakscan 0/0 · title/deck and front-clock reading time consistent · three paragraphs read aloud · inspect the figure at 1512 px and 375 px, in both themes · every hand-off is the actual last idea of its section. Keep A3 off-page and include no `REF ·` annotations outside the reference page.
