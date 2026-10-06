# CUFRGS Writing Standard

**Owner: Claude.** Codex and Luna apply this standard. They do not change it; they propose changes in the Relay Baton and Claude decides. Version 1.5, 2026-09-25 (A0 page-size guide; C15: no glosas, no decorative motion).
**Applies to:** everything that reaches a CUFRGS page (lessons, reviews, deep pages, cards) and every draft on the way there.
**Companion tool:** `protocols/tools/slop_lint.py` (Part G).

The standard has four jobs:
1. Make long pieces coherent by forcing a plan before any prose (Part A).
2. Say what good writing does (Part B, craft).
3. Set the rules that keep sentences clean (Part C).
4. Make the known AI tics impossible to ship (Parts D and G).

Parts A and B matter most. A banned-phrase list alone produces text that avoids the list and is still empty. Most slop comes from writing without knowing what each paragraph is for; the vocabulary is only the symptom. Clean is the floor; Part B is the target.

---

## 0. The reader

A UFRGS law student in the middle of the semester, reading on a phone or a laptop, often the week before an exam. They know basic legal vocabulary and the earlier lessons of the course. They want two things:
- to answer the exam question correctly;
- to understand why the answer is right, so they can handle a variation of it.

They do not want to be entertained, motivated or told that something is important. Every sentence either gives them law, gives them a reason, or shows the law working on facts.

---

## Part A. Plan before you write

**When:** mandatory for any piece over about 1,200 words, any lesson, and any deep page. For shorter pieces, do A1, A2 and A5 in your head and skip the file.

**Why:** models write fluent paragraphs and incoherent documents. The research on long-form generation agrees on two things (LongWriter/AgentWrite, STORM, recursive-planning work):
- a written plan with per-section content and length beats writing straight through;
- writing sections one after another, with the plan and the earlier sections in view, beats writing them in parallel.

A plan also lets Claude fix the structure while it's still cheap to fix, before 5,000 words exist.

### A0. Page size: one page answers one question
- A page teaches **one question**, aiming at about **2,500–4,000 words** (15–25 minutes of reading). This is a guide, not a cap: never cut content to hit it, and never create a tiny page to avoid going over. A 4,300-word page is fine; a 9,000-word page should split.
- A real class or syllabus unit that needs more becomes **several subpages, organised by the syllabus and Moodle topics**, not by how the in-person sessions were split. Example, Contratos unit 7 (revisão): vícios originários → fato superveniente (arts. 317 and 478–480) → quebra da base → cláusulas de adaptação.
- Total depth per unit can reach 8–15k words across its pages.
- Decide the split in the plan, before drafting, at a natural seam where the question changes.

### A1. Reader brief (3–5 lines)
- **Already known:** which earlier lessons or concepts this piece relies on.
- **Can do after reading:** concrete exam tasks, not topics.
  - Good: "decidir se uma proposta sem prazo, feita por telefone e aceita duas horas depois, ainda vincula".
  - Bad: "entender a proposta".
- **The likely exam traps** for this topic. Check the professor's lists, gabaritos and past questions.

### A2. Claim inventory
The 5–15 propositions the piece must establish. For each one, give:
- **the claim**, as a full sentence;
- **its status:** settled / majority view / contested. If contested, record who holds each position and the reason each gives;
- **the private source locator** (book + page, judgment + item). This never appears on the page;
- **the carrier:** the article, case or worked example that will make it concrete.

A claim with no carrier is not ready to be written.

### A3. Order and why
- Put the claims in an order where each one depends only on claims already made.
- Write one line saying why this order and not another, for example: "requisitos antes de prazos, porque o prazo só importa para uma proposta que já é proposta".
- If two orders seem equally good, pick the one closest to the order the professor taught.

### A4. Section plan
One row per section:

| Section | Question it answers | Claims (from A2) | Carrier | Figure (what it shows that prose can't) | Target words | What the reader carries into the next section |
|---|---|---|---|---|---|---|

A section whose question you can't state isn't a section. The last column is what makes transitions real: the next section starts from that sentence, not from a connector.

### A5. The thread
One sentence: the question the whole piece answers, which every section moves forward.
- Example: "Quando uma declaração de vontade já obriga quem a fez, e até quando?"
- This is for the plan only. It never appears on the page as a slogan.

### A6. Cut list
What the sources contain that you will **not** use, and why ("digressão histórica sobre o direito romano: não cai, não ajuda a resolver casos"). This stops source-dumping. It also gives Claude an easy way to spot something important you dropped.

### A7. Writing loop
1. Write section 1 with the plan in view.
2. Before section 2, check section 1 against its plan row: did it answer its question and establish its claims? Did it end on the "carries into" sentence?
3. Write each later section with the plan and all earlier sections in view.
4. **Re-plan instead of drifting.** If the writing shows the plan was wrong (a claim needs another first, a section splits in two), edit the plan file, note the change in one line, then continue. The plan must always describe the text that exists.

### A8. Revision passes, in order
1. **Reverse outline.** Write the one-line point of every paragraph in the margin of the plan.
   - If you can't state a paragraph's point, rewrite it.
   - If two paragraphs have the same point, merge them.
   - If a paragraph's point isn't in A2, cut it or add it to A2 on purpose.
2. **Craft pass:** Part B. Read each section for rhythm, term definitions, paragraph method and the concrete-before-abstract order. This is the pass that turns correct text into good text.
3. **Prose pass:** Part C.
4. **Lint pass:** run `slop_lint.py`. Resolve hard findings unless the match is a documented legal false positive; review density findings in context and apply only an explicit task budget (Part G).
5. **Fact pass:** check every article number, date, vote count, case name and quantity against the source locator.

### A9. Hand-in
- Deliver the plan file with the text. Claude reviews plans for lessons and deep pages **before** drafting starts, and reviews the text after.
- Plan files live in the private build folders, never in the site repo.

---

## Part B. Craft: what good writing does here

Removing tics leaves text that is merely inoffensive. This part describes the positive target: expository legal prose that a strong student reads quickly, understands the first time, and remembers.

### B1. Stance: show the reader the thing
- Write as someone pointing at something real (a contract, a court, a rule doing its work) for an intelligent reader who hasn't seen it yet. Pinker calls this "classic style".
- Talk about the law, not about the discourse. Not "a doutrina discute o momento da formação do contrato", but "O contrato entre ausentes se forma quando a aceitação é expedida (art. 434), com três exceções".
- Don't announce what you're about to do; do it.

### B2. Beat the curse of knowledge
The writer, and the model that has just read three treatises, forgets what the student doesn't know. Pinker calls this the main cause of bad expository prose.
- **Define every technical term in the sentence where it first appears,** in plain words, without breaking the flow: "a proposta é receptícia, isto é, só produz efeito quando chega ao destinatário".
- **Write the step that seems obvious.** If the reasoning goes rule → facts → result, the sentence where the facts meet the rule must exist.
- **Read the draft as the A1 reader:** someone who has only the earlier lessons. Every unexplained term or skipped step is a hole.

### B3. Concrete, then abstract, then the boundary
The order that teaches:
1. A situation the reader can picture: parties, an object, a date, money.
2. The rule it illustrates, stated generally with its article.
3. **The near miss:** change one fact and show the result flip. "Se a proposta tivesse fixado prazo de três dias, a aceitação de ontem formaria o contrato."

The near miss is what builds exam judgment, because exam questions are near misses. Use it at least once per major rule. The order can be reversed (rule first) when the rule is short and the case is long, but never leave a rule without a case or a case without its rule.

### B4. Sentence craft
- **Topic position and stress position** (Gopen and Swan): the start of the sentence links back to what the reader knows; the end carries the new information you want remembered. Put the article number, the exception or the result at the end.
- **Keep subject and verb together.** Portuguese legal prose loves to wedge a 30-word clause between them ("O contrato, que, conforme dispõe o art. 427 e ressalvadas as hipóteses…, é…"). Move the clause after the verb, or make it its own sentence.
- **One main idea per sentence.** Conditions and exceptions go in their own sentences, or in a list when they're genuinely parallel.
- **Rhythm is deliberate.** Mix lengths on purpose: a longer sentence lays out conditions and reasons, then a short one lands the rule. Three sentences of the same length and shape in a row is monotony; fix it by restructuring, not by padding. Short sentences are for what the reader must remember.
- **Parallel form for parallel content** (the hipóteses of a single article). Different form for different content. Don't force symmetry on material that isn't symmetrical.

### B5. Word choice
- **The exact term when one exists; the plain word when none does.**
  - Use "resilição", "resolução", "rescisão" in their technical senses, never loosely.
  - Outside terms of art, prefer "usar" to "utilizar", "começar" to "dar início", "por isso" to "destarte", "antes" to "previamente", "hoje" to "hodiernamente".
- **Strong, specific verbs:** "o STJ afastou a revisão", "a lei presume", "o credor perde a garantia". Avoid empty verbs that need a noun to mean anything: "realizar", "efetuar", "proceder à", "promover", "operar-se", "dar-se".
- **Cut juridiquês.** "Outrossim", "destarte", "mister se faz", "insta salientar", "cumpre salientar", "data venia", "in casu", "hodiernamente" belong to petitions from 1980. Brazilian courts themselves now push plain language (CNJ, Pacto Nacional do Judiciário pela Linguagem Simples, 2023). Latin terms of art that the exam uses (exceptio non adimpleti contractus, pacta sunt servanda) stay, italicised and explained at first use.
- **Concrete nouns** (o locatário, o camarote, R$ 50 mil) beat abstract ones (a parte, o bem, o valor) whenever the example allows.

### B6. Paragraph craft
- Each paragraph has a controlling idea, what Othon M. Garcia calls the *tópico frasal*. It's usually stated early and developed by **one** method:
  - definição;
  - exemplo;
  - causa e consequência;
  - contraste;
  - enumeração;
  - aplicação a fatos.
- Choose the method on purpose. A paragraph that defines, contrasts and applies all at once is usually three paragraphs.
- The topic sentence doesn't always come first. A case paragraph can open with the facts and close with the rule, which then sits in the stress position. Vary this across the lesson; don't vary it within a paragraph.
- Links between paragraphs come from content: the new paragraph picks up the idea the last one ended on (A4, last column).

### B7. Pacing across a lesson
- **Alternate density.** After a dense passage (a rule with three conditions), give a case; after two cases, step back to the principle.
- **Put the hardest idea where support is greatest:** after its prerequisites and next to its figure.
- **Spend words where the exam does.** Topics the professor tests get the near misses and worked cases. Background gets one tight paragraph.
- **Endings:** a section ends on the idea the next one needs. A lesson ends on its last substantive content, ideally the most exam-relevant application. Only lessons over about 3,000 words get a closing "Para a prova" list, and it holds rules, not a prose recap.

### B8. Tone
- A good professor explaining to a strong student after class: confident, exact, economical, occasionally dry. Never cheerful, never solemn, never selling.
- Evaluation belongs to named sources: courts, authors, the professor. The text's own voice explains and compares. It may say which view the courts follow and why that matters for the exam; it doesn't invent opinions.

### B9. Variation that comes from content
- Vary what the reader meets: a case, a hypothetical, a statute's exact words, a timeline, a table, a figure, a near miss. Vary the paragraph methods (B6) and sentence shapes (B4).
- **Never vary terminology for elegance.** Swapping synonyms is an AI tell, and in law it's dangerous: the reader will assume "resolução" and "extinção" mean different things, because they do.

### B10. Imitate models, not phrases
- Before a batch, read the exemplar pages Claude designates. Until the first depth-pass exemplar exists, use Benecles's Notas Polidas (listed in `LUNA_BRIEF - Rewrite for Voice and Formatting.md`).
- Copy the exemplar's moves: how it opens a section, where it puts the case, how it states an exception. Never copy its sentences.

---

## Part C. Prose rules

Each rule has its reason, because a rule whose purpose you know is harder to obey mechanically.

### C1. Characters as subjects, actions as verbs
The subject of a sentence should be the actor (a party, a court, the law). The verb should be what they do.
- ✗ "A ocorrência da vinculação do proponente se dá com a expedição."
- ✓ "O proponente fica vinculado assim que a proposta chega ao destinatário."

Watch for "a realização de", "a efetivação de", "a ocorrência de", "se dá", "opera-se". A sentence whose real verb is buried in a noun is harder to read and easier to leave vague.

### C2. Old before new
- Begin a sentence with what the reader already has. End it with the new information: the end of the sentence is where emphasis naturally falls.
- This builds the link between sentences, which is why good prose needs few connectors.
- ✓ "A proposta obriga o proponente (art. 427). Essa força obrigatória tem três exceções, e todas dependem do tempo."

### C3. Connectors only where the logic isn't visible
- Use "porque", "portanto", "mas", "ainda assim" when the relation is real and the reader might miss it.
- Don't open paragraphs with a connector by reflex. Open with the subject.
- "Além disso", "Nesse sentido", "Dessa forma" and "Ademais" as paragraph openers are almost always filler (limits in D3).

### C4. One job per paragraph, and lengths that follow the content
- A paragraph establishes one claim, applies one rule to one set of facts, or presents one side of a controversy.
- Lengths should vary: a definition can take two sentences, a case analysis two hundred words. A run of paragraphs of equal length and equal shape (topic sentence, elaboration, example, wrap-up) is the most reliable structural sign of machine prose.
- **End on the substance.** No closing sentence that restates the paragraph, and no moral.

### C5. Specific within two sentences
Every general statement is followed, within two sentences, by something the reader can check or picture: an article, a named case with its court and year, numbers, parties, a date.
- ✗ "Os tribunais têm sido cautelosos na aplicação da teoria."
- ✓ "O STJ recusou a revisão no REsp 1.321.614/SP (2014): a alta do dólar em 1999 era risco que as partes podiam prever."

### C6. Contested points get names and reasons
- Say who holds each position, the argument each gives, and which one prevails (STF/STJ, majority, the professor's position if she took one).
- "Parte da doutrina entende" is allowed only if the sources don't name anyone. They almost always do.
- Naming the author of a position is content, not citation (confirmed by Benecles, 2026-09-25). No page numbers or footnotes on the page (see E3).

### C7. Hedge once, where the doubt is, with its reason
- State settled law flatly: "A aceitação fora do prazo vale como nova proposta (art. 431)."
- Real uncertainty (a split, an open question, a recent change) gets one clause at the exact point, with the cause: "O STF ainda não julgou o mérito do Tema X; até lá, prevalece …".
- Never stack hedges ("pode, em certa medida, eventualmente").

### C8. Headings inform
- A heading is a noun phrase or the question a student would actually ask: "Prazo da proposta entre ausentes", "Quando o silêncio vale aceitação?".
- No puns, taglines or aphorisms. The page title names the topic.

### C9. Lists for enumerations, prose for reasoning
- Lists are for things that really are parallel and separate: requisitos, hipóteses do art. 428, legitimados do art. 103.
- A chain of reasoning ("porque… logo… salvo se…") never goes into bullets; the bullets cut out exactly the words that carry the logic.
- Don't default to three items. Enumerate as many as the law has.

### C10. Punctuation
- **No em dashes.** Use a comma, parentheses, a colon, or a new sentence.
- Colons introduce a list, a definition or a quotation. Not a punchline ("Não há contrato: faltou firmeza.").
- No exclamation marks.
- Rhetorical questions are allowed only as a heading, or as the literal question a case poses.

### C10b. Marks in running text (CASA-1, chairman picked "proposto", 06/10)
One vocabulary, learned once, read at a glance. Specimen: `specimen/casa.html`; CSS: `assets/casa.css`.
- `.held` (blue bold): what the court or law decided, the operative rule. At most one per paragraph, only on a holding, at most ~6 words.
- `.limit` (orange bold): the limit, the trap, what the decision did not do. Same caps.
- `.mark` (highlighter): the one sentence per chapter worth memorising. At most one per chapter.
- `.term` (dotted underline, `data-def` card): a term of art defined on the spot; the definition must come from the lesson itself.
- `.org` (small caps): court or organ name on first mention. `.tab`: tabular figures for dates, votes and sums. `.art` (mono chip): an article the reader may want to open, used rarely (dense runs of chips look like noise). Foreign terms, case names and works are italic.
- Colour is a legend: never colour a sentence of ordinary prose, never mark for decoration, and the colours agree with the source-block bars and figure legends (blue = decided, orange = limit).
- Refused: party colours in comparisons (collide with blue = decided); sidenotes (no margin in the 1,083 px column, and they put source talk outside the source block).

### C11. Portuguese register
- Norma culta, direct, active voice by default, plain words.
- Avoid calques of AI English: "desempenhar um papel crucial", "no cenário atual", "navegar por", "robusto", "abordagem holística", "jornada", "mergulhar".
- Use legal terms of art exactly and consistently. Don't vary a term for elegance: "resolução" stays "resolução", and doesn't become "extinção" three sentences later unless you mean extinção.

### C12. Prose next to figures says what the figure proves; it doesn't describe it
- The figure carries the structure. The adjacent paragraph states the claim the figure makes visible, or the application.
- Never describe the picture ("A imagem é dura: mãos entre as grades…", "É a mesma imagem de fundo da Aula 11…"). These are slide-narration leftovers.
- If the step text only makes sense with the figure, the figure needs to change, not the text.

### C13. Long-prose sections
Use a stretch of continuous prose (3–6 paragraphs between figures) where the subject is an argument rather than a structure:
- a doctrinal controversy;
- the reasoning of a leading case;
- a historical development that explains the current rule.

Shape: the question, then the positions with their reasons, then the resolution and its consequence for exam problems. Keep individual paragraphs under about 220 words. Don't use long prose for things a table or diagram shows better (classifications, procedural steps, comparisons).

### C14. Worked cases
Facts (only the ones that matter) → the legal question → the rule → application → result.
- Write the application in full sentences and show the step where the facts meet the rule. That step is what exams test.
- "Houve contrato? Não." is a card, not a worked case.

### C15. Linking and motion (kit helpers `lk`, `go`)
Benecles's rule of thumb (2026-09-25): **every visual element must explain something. Nothing is added as polish.**
- **No margin notes (glosas), no annotation arrows, no glints.** They were tried on Aula 13 and rejected. If a remark is worth making, it goes in the prose.
- **Linked terms** (`lk` in prose, `data-lk` on figure groups or inside table cells; dotted underline): only where the reader must hold the text and a figure or table together (comparisons, competing frames).
- **Jump-to-step** (`extra=go(panel_id, label)` on figure groups): standard for scrolly figures whose later panels still show earlier elements.
- **Motion:** entrance and step animations that show a mechanism stay. **No idle or decorative motion**, no easter eggs. A moving element is justified only when the movement itself is the content, like a figure that shows a flow. The rejected hero pennant is the counter-example.
- **Cross-lesson links:** a plain link where the text already names another lesson ("a Aula 12…"). No wiki-style linking.

---

## Part D. Banned and limited patterns

Hard bans get zero tolerance. Limits are per lesson. Terms of art are always allowed (see D6).

**What slop is.** Slop is rhetorical machinery standing in for information: a contrast, triad, concession, reveal, or moral produced where the content asked for none. These are ordinary Portuguese structures; frequency and function matter more than isolated occurrence. Research also cautions against a single objective slop label: judgments vary across people and domains, so this standard treats findings as dimensions for editorial review, not authorship evidence ([Shaib et al.](https://arxiv.org/html/2509.19163)).

Three findings shape this policy:
- **Vocabulary variety is not a target.** In SlopBench's 18-model, English benchmark, models were more lexically diverse than human references; its composite rankings changed with metric weights and did not track crowd Elo reliably ([SlopBench](https://arxiv.org/html/2609.33905)). Repeat the precise legal term rather than thesaurus it. This result is not a Portuguese legal-writing measurement.
- **No punctuation mark proves slop.** Pew's 490,000-page English Common Crawl study used an AI detector and cautions that a page can be misclassified; punctuation alone is not proof ([Pew report](https://www.pewresearch.org/data-labs/2026/08/20/how-much-of-the-internet-is-written-with-ai/)). Em dashes are limited here by C10 as house style, not as evidence of AI.
- **Full rewrites can flatten variation.** Across seven datasets and more than 880,000 texts, one study reports that LLM polishing/rewriting reduced writing-complexity variance by 21–50% ([Sourati et al.](https://www.nature.com/articles/s41562-026-02550-0)). Human post-editing also did not erase all measured LLM-style traces in one personal-writing study ([Baumler et al.](https://aclanthology.org/2026.acl-long.2030/)). These results do not predict effects on our pages; they support local, span-level edits over automatic full-draft rewrites.

The order of priority when editing: (1) maximize propositions per sentence and delete machinery that carries none; (2) impose no structure the content did not ask for (no automatic contrast, triad, summary, section, concession, reveal or closing moral); (3) never manufacture nuance: if the obvious reading is right, state it; a distinction exists because the law has it; (4) allow asymmetry: a point gets the sentences it needs, lists the items they have, paragraphs the length their job takes; (5) explain by mechanism (who did what, under which rule, with which effect), not by relabelling; (6) judge known tells by density; (7) never "humanize": no fragments, slang, fake opinions, invented anecdotes or planted errors.

### D1. Negative parallelism (hard ban)
- "não é X, é Y" / "não é X, e sim Y" / "não se trata de X, mas de Y" / "mais do que X, Y" / "X, não Y" used as a flourish.
- **Legal exception:** a genuine legal distinction may use "não… mas" when both halves carry law: "A resposta tardia não forma contrato, mas vale como nova proposta." The test: if you delete the "não" half, is law lost? If not, delete it.
- "não apenas/só X, mas também Y": banned unless both halves are necessary information. Even then, prefer "X e Y".

### D2. Puffery and significance claims (hard ban)
- "papel crucial/fundamental/central", "pedra angular", "marco", "divisor de águas", "ganha destaque", "reflete a importância", "evidencia a relevância", "revela-se essencial", "merece atenção especial".
- Trailing gerunds that add significance ("…, evidenciando / reforçando / consolidando / demonstrando a importância de …").
- If something matters for the exam, show that it does: a trap, a vote count, a consequence.

### D3. Formulaic connectors and meta-text
- **Hard ban:** "vale ressaltar/destacar/notar/lembrar", "cabe destacar", "é importante notar/ressaltar/destacar", "é interessante observar", "nesta aula veremos", "como vimos", "como veremos", "vamos entender", "em conclusão", "por fim, mas não menos importante", "à luz do exposto".
- **Limit 1 per lesson each:** "em suma", "em síntese", "em resumo", "ou seja", "dessa forma", "nesse sentido", "além disso", "ademais".

### D4. Slogans, aphorisms and dramatic closers (hard ban)
- Short quotable sentences that compress a rule into a maxim: "Interpretar revela o que foi combinado e não escreve outro contrato."
- Paragraph endings that deliver a moral.
- Staged reveals with a colon.
- House tics found on our own site (2026-09-25 audit), limit 1 per lesson: "A pergunta é se…", "A pergunta decisiva…", "Tudo começa…", "Tudo depende…".

### D5. Vague attribution and fake balance (hard ban)
- "especialistas apontam", "muitos autores", "a doutrina moderna", "há quem diga", "alguns críticos": ban all of these when the source names who.
- "Por um lado… por outro…" with no resolution.

### D6. Intensifiers (limit 3 per lesson, total)
- "crucial", "fundamental", "essencial", "central", "decisivo", "significativo", "extremamente", "bastante", "realmente", "de fato", "claramente", "evidentemente".
- **Terms of art don't count:** "direitos fundamentais", "elementos essenciais do contrato", "erro essencial", "questão central" when it's a technical usage.
- If you remove the intensifier and the sentence loses nothing, remove it.

### D7. Reader address (hard ban)
- Cheerleading and faux-dialogue: "Você já deve ter percebido", "Não se preocupe", "Pense nisso", "Perceba que", "Repare:".
- Direct instructions in exam-practice contexts are fine ("Responda antes de abrir a solução").

### D8. Formatting tics
- Plain bold is retired (CASA-1, 06/10): the only bold in running text is `.held` and `.limit` (see C10b). Run-in labels inside a structured block (Tese., Casos.) may stay bold. Never bold whole sentences.
- No emoji.
- No headings that contain only other headings.
- No horizontal rules as decoration.

---

### D9. Density limits (structural tells; set from the 06/10 backtest, `work/slop-bench/BACKTEST.md`)
Counted by `slop_lint` (⚙). Each limit is the smallest rate at which ≤ 10% of human Portuguese doctrine would alarm; a hit over the limit is a reason to look, not an automatic edit. Findings carry a band: **tell** (model habit) or **style** (house rule humans also break).
- ⚙ **Negated inference** ("não basta / substitui / resolve / autoriza / prova / transforma / significa…"): ≤ 0.5 per 1,000 words. Our pages ran 2.43 vs human doctrine 0.14 (~18×): our strongest house tic. State what the decision did; keep a limit sentence only where the reader would otherwise assume the opposite.
- ⚙ **"Não é X" frames** (D1): ≤ 2.0 per 1,000 words, legal test still applies to each.
- ⚙ **Colon reveals** (claim, colon, expansion in one sentence): ≤ 5.6 per 1,000 words (human ~3, our pages 7–8).
- ⚙ **Triads** ("X, Y e Z"): ≤ 12.3 per 1,000 words; two triads in one paragraph is still worth a look.
- ⚙ **"em vez de / ao invés de / em lugar de"**: ≤ 1 per 1,000 words (13–15× the human rate).
- ⚙ **Stacked rhetorical questions**, **same-opener runs**, **uniform paragraphs** (five consecutive within ±15%), **no parentheses on a long page**: model-only patterns; any run is a finding.
- ⚙ **AI vocabulary basket** ("crucial, fundamental, essencial, robusto, abrangente, panorama, nuance…"): ≤ 5.2 per 1,000 words.
- ⚙ **Style band** (applies to everyone): stance adverbs ≤ 1.2/1k, "não X, mas Y" ≤ 1.6/1k, no "Em suma," wrap-ups, no "vale destacar".
- Read, not counted: nominalization pile-ups (C1), participial and "o que demonstra…" tails (⚙ hard), sentences that restate an earlier one (D10.3).

### D10. The five pathologies generic guides miss (chairman, 05/10; hard bans)
1. **Fake disagreement.** Staging an opposing view nobody in the sources holds, so the text can refute it. Only named positions with reasons (C6) are disputed.
2. **Circular causal explanation.** The "because" clause restates the effect ("a Corte interveio porque havia necessidade de intervenção"). Test: does the reason name a fact, a rule or an actor not already in the claim? If not, find the cause in the sources or cut the "because".
3. **Unnecessary restatement.** A sentence, paragraph or section summary that repeats what the reader just read. Delete-test: if removing it loses no proposition, remove it. Chapter ledes state the question, not a preview of the answer.
4. **Excessive sectioning.** A heading for every two paragraphs, a list where three sentences reason. One page answers one question (A0); a section exists when the question changes.
5. **Reflexive qualification.** A hedge, caveat or "em certa medida" attached by habit. C7 governs: hedge once, where the doubt is, with its reason. A concession that changes nothing is cut.

## Part E. Sources and copyright

### E1. Paraphrase from understanding
- Read the passage, close it, write the claim in your own sentence and your own order, then check it against the source for accuracy.
- Paraphrasing sentence by sentence while the source is open produces close paraphrase. Close paraphrase is still copying (the structure is also protected), and it reads badly.

### E2. Source blocks: the books and decisions speak for themselves (chairman, 05/10; replaces "no doctrine quotations")
- When a book, decision, statute or treaty says the thing better than our paraphrase, the prose **stops** at that point and a **source block** opens right there: the passage itself, as long as it earns (a paragraph, or several hundred words of a key stretch). The prose resumes below without "como vimos" or a recap.
- **One component, `.fonte`** (replaces `.lex`, `blockquote.law`, `.julgado` and the Codex `.source-block`): mono header (source, locator), the passage in the reading serif, a left bar that says what the source is to the argument: blue = a decision or statute's operative words, orange = a limit, ink = a book or doctrine. Key words the prose leans on get a marker highlight inside the block. Non-Portuguese passages carry a `tradução nossa` toggle. Markup and examples: `specimen/casa.html`; `.src` is taken by the hidden-sourcing class.
- **No lead-in attribution in the prose** ("segundo X", "como afirma Y"). The block carries its own header: author, *work*, chapter/page; or court, case, date.
- Choose stretches that do something paraphrase can't: the author's argument in their own order, a definition the professor uses, the court's actual reasoning, the operative words of an article. Don't quote what a sentence of ours says as well.
- Decisions stay in their original language (Spanish, Portuguese); a translation toggle sits under non-Portuguese blocks.
- Quote exactly from the source file on disk (book extract, decision text). Never quote from model memory; a block whose text can't be matched to the source file doesn't ship.

### E3. Our own prose still never talks about sources
- Outside source blocks: no page numbers, footnotes, "segundo o slide", or provenance talk in the prose.
- The private ledger keeps every locator (A2); source blocks show theirs in the header.

### E4. Depth comes from the sources, not from the model
If the sources don't support a claim, it doesn't go in. Don't fill gaps with plausible general knowledge. If a gap matters, flag it in the plan for Claude.

---

## Part F. Before and after

**1. Slide narration (Controle, Aula 13)**
- ✗ "A imagem é dura: mãos entre as grades de uma cela superlotada, o retrato do próprio caso de origem, o sistema prisional da ADPF 347. Em suma: nomear um estado de coisas inconstitucional não resolve a superlotação; só reformas institucionais, fora do que uma decisão judicial pode sozinha entregar, resolvem."
- ✓ "Na ADPF 347 (2015), o STF declarou o estado de coisas inconstitucional do sistema prisional. A declaração não abriu uma única vaga: as medidas que reduzem a superlotação (orçamento, construção, política de encarceramento) dependem do Executivo e do Legislativo. Por isso, em 2023, o Tribunal voltou ao caso e determinou que a União e os estados apresentassem um plano, com metas e prazo, sob sua supervisão."
- **What changed:** the reader gets the case, the year, the limit of the declaration and the court's response, instead of a picture description and a moral. *(The 2023 detail illustrates the shape of the fix. Verify it against the source ledger before reusing it.)*

**2. The house template (Contratos, Aula 13)**
- ✗ "Uma mudança pode tirar o sentido do contrato sem tornar nada impossível. A pergunta é se a premissa que caiu era das duas partes ou só de uma."
- ✓ "Um fato novo pode esvaziar a finalidade do contrato sem impedir nenhuma prestação: o camarote alugado para ver um desfile que foi cancelado ainda pode ser entregue e pago. A revisão ou resolução só cabe quando o desfile era premissa comum, conhecida e aceita pelas duas partes; se era motivo só do locatário, o risco é dele."
- **What changed:** a carrier (the coronation-cases pattern) instead of the template, and the rule stated as a condition the student can apply.

**3. Negative parallelism (Controle, Aula 12)**
- ✗ "…a soma das duas heranças não é apresentada como uma solução, e sim como uma confusão a ser explicada."
- ✓ "O Brasil juntou o controle difuso de origem americana e o concentrado de origem austríaca sem definir qual prevalece; boa parte da aula trata dos atritos que isso produz (art. 52, X, e a chamada abstrativização)."

**4. Generic AI paragraph (typical Luna draft)**
- ✗ "A boa-fé objetiva desempenha um papel crucial no direito contratual brasileiro, refletindo a evolução do ordenamento jurídico. Além disso, é importante destacar que ela possui três funções fundamentais, evidenciando sua relevância prática."
- ✓ "O Código Civil usa a boa-fé objetiva de três maneiras. Ela orienta a interpretação do contrato (art. 113), limita o exercício de direitos (art. 187) e cria deveres que as partes não escreveram (art. 422), como informar e cooperar. As três funções aparecem juntas nos casos de venda de imóvel com vício oculto conhecido pelo vendedor."

---

## Part G. Acceptance checklist and lint

Before hand-in:

1. The plan file exists and matches the text (Part A).
2. The reverse outline passes: every paragraph has a stateable point that appears in A2.
3. `python3 protocols/tools/slop_lint.py <files>` reports line, rule, matched span, suggested fix, and a per-page density summary. Findings prompt review; they do not fail by themselves. Use `--json` for agent output and `--max-per-1000 N` only when a task sets an explicit finding-density budget. The linter does not treat em dashes as slop; C10 remains a house-style rule.
4. The fact pass is complete, with every locator in the ledger.
5. **Read-aloud test on three random paragraphs.** Any sentence you can't say in one breath gets split. Any sentence that sounds like an advert gets rewritten.
6. Figures: each adjacent paragraph states a claim, never a description (C12).

The linter is a floor, not a judge. Passing it proves the absence of listed tics, not quality. Claude's read is the judge.

---

## Sources for this standard

- Shaib et al., “Measuring AI ‘Slop’ in Text” (2026): dimensions vary by task and human binary judgments have low agreement; see `work/slop-bench/RESOURCES.md`.
- SlopBench (2026): English benchmark dimensions and model rankings vary with weights; the study does not validate Portuguese legal-writing thresholds; see `work/slop-bench/RESOURCES.md`.
- Paech et al., “Antislop” (ICLR 2026): English creative-writing suppression/training experiments; see `work/slop-bench/RESOURCES.md` for scope and transfer limits.
- NousResearch autonovel, ANTI-SLOP.md: structural tells (uniform sentences and paragraphs, transition openers, list abuse).
- Bai et al., "LongWriter / AgentWrite" (ICLR 2025): plan with per-section content and length, then write serially.
- Shao et al., STORM (2024), and recursive-planning follow-ups (arXiv 2503.08275): research-grounded outlines; re-plan when writing reveals new structure.
- Joseph Williams, *Style: Lessons in Clarity and Grace*: characters as subjects, actions as verbs; old before new; stress position.
- George Gopen and Judith Swan, "The Science of Scientific Writing" (American Scientist, 1990): topic and stress positions, subject–verb proximity, reader expectations.
- Steven Pinker, *The Sense of Style* (2014): classic style, the curse of knowledge.
- Othon M. Garcia, *Comunicação em Prosa Moderna* (FGV): tópico frasal and the methods of developing a paragraph.
- CNJ, Pacto Nacional do Judiciário pela Linguagem Simples (2023): plain language in Brazilian legal writing.
