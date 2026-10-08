# Span-level prose critic

## Role
You are an editorial critic for Portuguese legal teaching prose. Review a frozen draft against `protocols/STYLE.md` and Part D of `protocols/Writing Standard.md`. This is not an AI detector and must not judge authorship.

## Modes
- **Conform** (default): bring site prose toward STYLE.md.
- **Preserve**: when the chairman's own prose or a source quotation is being edited, protect its voice and wording; flag only concrete defects within the requested scope.

## Review method
Read the whole page for its legal thread and teaching purpose. Return only spans whose exact words create a specific reader-facing problem. A pattern-list match is not a reason by itself. Preserve legal terms of art, statutory language, quotations, accurate repetition, genuine legal contrasts, necessary caveats, and enumerated requirements. Do not invent doctrine, sources, facts, examples, or uncertainty.

Two quick tests for any suspect sentence (MariusAure): **meaning** — restate it in its boring version; if that is "things matter" or "this is complex", it carries no proposition; **fungibility** — if it could be pasted into an unrelated lesson unnoticed, it is filler.

Review these dimensions separately: information density; restatement; fake contrast; fake nuance; causal depth (circular explanation); forced symmetry; metadiscourse; significance inflation; conclusion pressure; formatting pressure; D10 fake disagreement; circular causal explanation; unnecessary restatement; excessive sectioning; reflexive qualification.

For every span, give:
1. exact quoted span (smallest phrase/sentence that carries the issue);
2. dimension;
3. why it impedes this page's legal teaching purpose, naming the missing or duplicated proposition;
4. smallest replacement, or `delete` if no proposition is lost.

Do not rewrite paragraphs, whole sections, or unflagged text. If a dimension has no supported issue, return an empty list for it. Do not require changes to satisfy a quota.

## Output JSON
Return valid JSON only:
```json
{
  "page": "...",
  "mode": "Conform",
  "scores": {
    "information_density": {"score": 0, "evidence": "short exact quotation or none"},
    "restatement": {"score": 0, "evidence": "..."},
    "fake_contrast": {"score": 0, "evidence": "..."},
    "fake_nuance": {"score": 0, "evidence": "..."},
    "causal_depth": {"score": 0, "evidence": "..."},
    "forced_symmetry": {"score": 0, "evidence": "..."},
    "metadiscourse": {"score": 0, "evidence": "..."},
    "significance_inflation": {"score": 0, "evidence": "..."},
    "conclusion_pressure": {"score": 0, "evidence": "..."},
    "formatting_pressure": {"score": 0, "evidence": "..."},
    "fake_disagreement": {"score": 0, "evidence": "..."},
    "circular_causal_explanation": {"score": 0, "evidence": "..."},
    "unnecessary_restatement": {"score": 0, "evidence": "..."},
    "excessive_sectioning": {"score": 0, "evidence": "..."},
    "reflexive_qualification": {"score": 0, "evidence": "..."}
  },
  "spans": [
    {"quote":"...", "dimension":"...", "reason":"...", "replacement":"..."}
  ]
}
```
Scores run 0 (no observed issue) to 100 (pervasive, evidenced issue), with the quoted evidence explaining any nonzero score. A score is not a grade of the author.


Mode: **conform**

---
# STYLE.md
# STYLE.md — target for Portuguese legal teaching

This is a positive target for the site, not a voice imitation or authorship test. The reference set is Portuguese legal scholarship and the reviewed house lessons. The current discovery report measured 9 legal-text reference candidates (622,934 word tokens) and 20 staged lesson-page proxies (21,611 word tokens); the page writers are unlabeled and these are not confirmed model samples. See `work/slop-bench/report.md`. No numeric style threshold is calibrated from those proxies, and no frequency is treated as a quality score.

## Attributes

| Dimension | Target | Reader-facing check |
|---|---|---|
| Information density | High: each sentence adds a rule, reason, application, or consequence. | Can the sentence be removed without losing a proposition? |
| Paragraph length | Highly variable, following the paragraph's job. | Does each paragraph establish one point, apply one rule, or present one named position? |
| Sentence length | Variable; moderate default, with longer sentences where legal conditions depend on each other. | Is the actor and operative verb easy to find? |
| Argument | Causal and evidentiary. State who acted, under which rule, and with what effect. | Does each explanation add a fact, rule, or actor instead of renaming the result? |
| Transitions | Mostly implicit; explicit connectors only when they clarify a real relation. | Is the relation actually causal, contrasting, or dependent? |
| Headings | Sparse navigation at real changes in the question. | Does the section answer a different question? |
| Lists | Only for enumerable, genuinely parallel items. | Is this a list of legal requirements/categories, or reasoning that belongs in prose? |
| Conclusions | Optional; no recap-only ending. | Does the final sentence add a consequence or answer, rather than restate? |
| Restatement | Very low, except where a legal term or comparison needs stable repetition. | Does the repeated phrase preserve precision, or only echo? |
| Metacommentary | None in reader-facing exposition. | Is the sentence about the lesson/text instead of the law? |
| Qualification | Only where the source or doctrine leaves genuine doubt; name its reason once. | Can the hedge be tied to an authority, split, or open issue? |
| Examples | Concrete and legally grounded: article, case, parties, vote, date, procedural act. | Can the student apply the rule to a real carrier? |
| Rhetorical symmetry | Low; position lengths follow their arguments, not a balanced template. | Is a contrast or triad doctrinally necessary? |
| Rhetorical questions | Rare; use as headings or when the case itself poses the question. | Does the question orient a real decision? |
| Legal vocabulary | Stable and exact. Repeat terms of art instead of varying them for elegance. | Would a synonym change the legal category? |

Numeric corpus distributions are descriptive in the current pilot, not targets. Once the discovery report has enough correctly labeled Portuguese data, it may add ranges for paragraph and sentence distributions; it must not optimize vocabulary diversity or a single aggregate score.

## Short reference passages

These are brief excerpts from local Brazilian constitutional-law treatise extracts. They illustrate legal exposition, not mandatory wording. Preserve quoted source language and terminology when teaching from these works.

> “O controle de constitucionalidade é um desses mecanismos”
>
> — Luís Roberto Barroso, local extract `work/controle-depth/extracts/barroso-pdf-20-362.txt`.

> “As Constituições escritas são apanágio do Estado Moderno.”
>
> — Gilmar Ferreira Mendes, local extract `work/controle-depth/extracts/mendes-branco-pdf-1853-2610.txt`.

> “O controle de constitucionalidade se define como ‘juízo relacional que procura estabelecer uma comparação valorativamente relevante’”
>
> — Dimitri Dimoulis and Soraya Lunardi, local extract `work/controle-depth/extracts/dimoulis-lunardi-pdf-82-185.txt`.

## Editing modes

- **Conform:** default for site prose. Apply these attributes and the Writing Standard Part D.
- **Preserve:** when editing the chairman's own prose or a quoted/source passage. Correct only the requested issue; retain meaningful voice, quotation, and legal terms.

A style flag is not evidence that a person used AI. Patch only the flagged span and preserve every unaffected proposition.


---
# Writing Standard, Part D
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



---
# Deterministic findings (review prompts, not verdicts)
- line 33 `negative-parallelism`: “não é”
- line 44 `negative-parallelism`: “não foi”
- line 44 `negative-parallelism`: “não é”
- line 45 `negative-parallelism`: “não era”
- line 66 `negative-parallelism`: “não é”
- line 68 `negative-parallelism`: “não é”
- line 69 `negative-parallelism`: “não é”
- line 70 `negative-parallelism`: “não é”
- line 70 `negative-parallelism`: “não é”
- line 88 `negative-parallelism`: “não é”
- line 104 `negative-parallelism`: “não foi”
- line 145 `negative-parallelism`: “não é”
- line 67 `negated-inference`: “não basta”
- line 70 `negated-inference`: “não decide”
- line 81 `negated-inference`: “não decide”
- line 109 `negated-inference`: “não garante”
- line 117 `negated-inference`: “não decide”
- line 148 `negated-inference`: “não torna”
- line 151 `negated-inference`: “Não decide”
- line 29 `colon-reveal`: “256 é a chave da estratégia: se a Convenção fosse “mais favorável” aos direitos políticos do que a Constituição, prevaleceria sobre ela.”
- line 33 `colon-reveal`: “Antes de ler: como decidir?”
- line 35 `colon-reveal`: “A OC-28/21 foi consultiva: orienta a interpretação da Convenção, mas não anulou a decisão boliviana no processo em que foi proferida.”
- line 44 `colon-reveal`: “A Constituição não foi riscada nem reformada: suas frases deixaram de ser aplicadas porque o Tribunal considerou mais favorável a norma convencional.”
- line 45 `colon-reveal`: “Mas a decisão tratou de elegibilidade, não de vitória: quem vence continua sendo decidido nas urnas.”
- line 53 `colon-reveal`: “23 da Convenção como mais generoso que a Constituição: o art.”
- line 62 `colon-reveal`: “Em 21 de outubro de 2019, a Colômbia pediu à Corte Interamericana uma opinião consultiva: a reeleição presidencial indefinida é um direito humano protegido pela Convenção, e proibi-la é compatível com ela?”
- line 66 `colon-reveal`: “ou inabilitação de um eleito por autoridade administrativa, o “exclusivamente” vale à letra: só uma condenação penal por juiz competente pode fazê-lo (casos López Mendoza e Petro Urrego, § 107).”
- line 67 `colon-reveal`: “Não estar na lista não basta para ser válida: a restrição precisa estar prevista em lei, perseguir fim legítimo e ser idônea, necessária e proporcional (§ 114).”
- line 67 `colon-reveal`: “32 da Convenção: evitar que uma pessoa se perpetue no poder e assegurar pluralismo, alternância e freios entre os poderes (§ 119).”
- line 69 `colon-reveal`: “Limitar a reeleição presidencial, nessa leitura, não é uma imposição externa contra o povo: é o cumprimento de um compromisso que o próprio Estado assumiu.”
- line 70 `colon-reveal`: “Para a maioria, haver petições pendentes sobre tema próximo não impedia responder: interpretar em abstrato não é prejulgar aqueles casos.”
- line 78 `colon-reveal`: “No mérito, separa mandato indefinido de reeleição indefinida : no primeiro, o governante não precisa submeter sua permanência a eleições periódicas; no segundo, ele ainda disputa votos em eleições sucessivas.”
- line 81 `colon-reveal`: “, portanto, não decide sozinho a validade de cada limite para prefeitos, vereadores ou assembleístas: para cada cargo, é preciso identificar a norma doméstica e o precedente pertinente.”
- line 104 `colon-reveal`: “O referendo de 2016 não foi anulado, mas perdeu efeito prático: a candidatura que ele recusara ficou liberada.”
- line 117 `colon-reveal`: “Gelman e a OC-28 convergem num ponto que a SCP contrariou: há matérias que a maioria não decide sozinha.”
- line 126 `colon-reveal`: “Corte IDH, Gelman (2011): o voto popular não legitima a impunidade de graves violações.”
- line 127 `colon-reveal`: “TCP, SCP 0084/2017: aplicação preferente do art.”
- line 129 `colon-reveal`: “Pazmiño: admissibilidade, reformulação da consulta, igualdade eleitoral e pluralismo de modelos.”
- line 129 `colon-reveal`: “Zaffaroni: competência para prescrever engenharia institucional e mandato sem eleição × candidatura reiterada.”
- line 139 `colon-reveal`: “256: tratados de direitos humanos que declarem direitos mais favoráveis aplicam-se de maneira preferente sobre a Constituição.”
- line 143 `colon-reveal`: “O Tribunal não anulou o referendo: afastou as regras que limitavam a reeleição, com o mesmo efeito prático que o “sim” teria tido.”
- line 145 `colon-reveal`: “Votação: 5 × 2 (vencidos Pazmiño Freire e Zaffaroni).”
- line 152 `colon-reveal`: “Eixo: um tribunal invoca o direito de ser eleito para afastar um limite de mandatos que o eleitorado se recusou a mudar.”
- line 68 `denial-restatement`: “não é a ruptura abrupta, mas a erosão gradual das salvaguardas, “incluso si este es electo mediante elecciones populares” (§ 145)”
- line 68 `denial-restatement`: “não restringe a reeleição presidencial em geral, mas a ausência de limitação razoável e os mecanismos que permitam a perpetuação de uma mesma pessoa na P”
- line 104 `denial-restatement`: “não foi anulado, mas perdeu efeito prático”
- line 25 `triad-density`: “e aplica a mesma regra a governadores, assembleístas e autoridades municipais (arts”
- line 26 `triad-density`: “Em setembro de 2017, uma senadora e onze deputados da Assembleia Legislativa Plurinacional propu”
- line 26 `triad-density`: “23, 24 e 29 da Convenção Americana”
- line 44 `triad-density`: “assembleístas departamentais, prefeitos e vereadores”
- line 52 `triad-density`: “amplamente o direito de participar do poder político, nas vertentes de votar e de ser votado, seriam normas-princípio”
- line 54 `triad-density`: “frente a quem aspira a ele, sem justificativa objetiva e razoável”
- line 67 `triad-density`: “para ser válida: a restrição precisa estar prevista em lei, perseguir fim legítimo e ser idônea, necessária e proporcional (§ 114)”
- line 67 `triad-density`: “que uma pessoa se perpetue no poder e assegurar pluralismo, alternância e freios entre os poderes (§ 119)”
- line 67 `triad-density`: “pesou dois direitos: o de quem ocupa o cargo, que não tem direito autônomo à reeleição e só perde a chance de concorrer de novo, e o dos demais cidad”
- line 68 `triad-density`: “: a opinião não restringe a reeleição presidencial em geral, mas a ausência de limitação razoável e os mecanismos que permitam a perpetuação de uma mesma pessoa”
- line 69 `triad-density`: “o poder tende a concentrar-se no presidente, enquanto o Legislativo e o Judiciário são relativamente mais fracos (§ 121)”
- line 70 `triad-density`: “a Corte não recebeu recurso contra o tribunal boliviano, não julgou a Bolívia em caso contencioso e não anulou a SCP 0084/2017 nem o resultado do referendo”
- line 70 `triad-density`: “com autoridade de intérprete final da Convenção, que juízes e autoridades podem usar em controle de convencionalidade, mas”
- line 77 `triad-density`: “questão como um direito individual de reeleger-se sem limite, propõe examinar em conjunto o direito de votar e ser eleito em condições de igualdade e a relação entre democ”
- line 79 `triad-density`: “reformulação da consulta, igualdade eleitoral e pluralismo de modelos”
- line 81 `triad-density`: “A SCP 0084/2017 afastou limites para quatro grupos de cargos, inclusive legislativos e subnacionais”
- line 81 `triad-density`: “vereadores ou assembleístas: para cada cargo, é preciso identificar a norma doméstica e o precedente pertinente”
- line 88 `triad-density`: “Em cada uma, pergunte de quem é o direito invocado e contra quem ele é usado”
- line 99 `triad-density`: “afirmar que uma decisão majoritária (a Lei de Caducidade, confirmada em referendo e plebiscito) não pode impedir a investigação de graves violaç”
- line 122 `triad-density`: “casos, divergência e posição”
- line 129 `triad-density`: “reformulação da consulta, igualdade eleitoral e pluralismo de modelos”
- line 145 `triad-density`: “sua proibição é compatível com a Convenção, a Declaração Americana e a Carta Democrática”
- line 149 `triad-density`: “individual (só por condenação penal de juiz competente, como em López Mendoza e Petro), não às regras gerais que todo sistema eleitoral prec”
- line 149 `triad-density`: “idoneidade, necessidade e proporcionalidade”
- line 151 `triad-density`: “não transporta automaticamente a conclusão a cargos locais, e uma regra que permite uma reeleição e veda a seguinte é o tipo de limitação razoável que considera”
- line 55 `uniform-paragraphs`: “Aí está o paradoxo que o caso expõe. O vocabulário dos direitos políticos, invoc”

---
# Frozen draft: aula-06.html

Direito Latino-americano DIR03057 UFRGS · 2026/2 

 Reeleição e direitos políticos 

 Em Gelman, a Convenção limitou a maioria para proteger vítimas. Na Bolívia, um tribunal a usou para liberar a candidatura que o referendo recusou . Em 2021, a Corte Interamericana leu o mesmo artigo ao contrário .

 
 Aula 31/08 · Soberania popular 
 Leitura ≈ 20 min 
 Antes Aula 05 · Gelman 
 Depois Aula 07 · Estado de coisas 


 
 
 01 A regra que o eleitor recusou mudar
 A Constituição de 2009 permitia uma única reeleição consecutiva. Em 2016, o eleitorado recusou mudar isso.
 
 A Constituição boliviana de 2009 fixa o mandato do presidente e do vice-presidente em cinco anos, com possibilidade de reeleição “por una sola vez de manera continua” (arts. 156 e 168), e aplica a mesma regra a governadores, assembleístas e autoridades municipais (arts. 285.II e 288). Em 21 de fevereiro de 2016, um referendo sobre a reforma que permitiria uma nova candidatura de Evo Morales terminou com a vitória do “não”.
 Em setembro de 2017, uma senadora e onze deputados da Assembleia Legislativa Plurinacional propuseram uma ação de inconstitucionalidade abstrata com dois pedidos. Primeiro, a inconstitucionalidade dos dispositivos da Lei do Regime Eleitoral (Lei 026/2010) que reproduziam o limite. Segundo, e mais ousado, a inaplicabilidade dos próprios artigos da Constituição que o estabelecem, por “contradição intraconstitucional” com os arts. 26 e 28 (direitos políticos) e por contrariarem os arts. 1.1, 23, 24 e 29 da Convenção Americana.
 Constituição da Bolívia art. 256.I Los tratados e instrumentos internacionales en materia de derechos humanos que hayan sido firmados, ratificados o a los que se hubiera adherido el Estado, que declaren derechos más favorables a los contenidos en la Constitución, se aplicarán de manera preferente sobre ésta.
 Tradução nossa Os tratados e instrumentos internacionais em matéria de direitos humanos que tenham sido firmados, ratificados ou aos quais o Estado tenha aderido, que declarem direitos mais favoráveis aos contidos na Constituição, aplicar-se-ão de maneira preferencial sobre esta.
 ver tradução O art. 256 é a chave da estratégia: se a Convenção fosse “mais favorável” aos direitos políticos do que a Constituição, prevaleceria sobre ela. A pergunta, portanto, era a mesma de Gelman vista do avesso. Lá, uma decisão majoritária foi barrada pelos direitos das vítimas ( Aula 05 ); aqui, um direito seria usado contra o resultado de uma votação.



 Antes de ler: como decidir? Na Bolívia, a Constituição de 2009 permite uma única reeleição presidencial consecutiva. Em 2017, o Tribunal Constitucional Plurinacional afastou esse limite com base no direito de ser eleito previsto no art. 23 da Convenção Americana. Em 2021, ao responder consulta da Colômbia, a Corte Interamericana concluiu que reeleição presidencial indefinida não é um direito humano protegido pela Convenção. Qual leitura corresponde à posição da Corte Interamericana?
 O art. 23 garante reeleições sem limite, pois enumera de forma fechada todas as restrições possíveis ao direito de ser eleito. A Convenção não reconhece um direito à reeleição presidencial indefinida; um limite que preserve a alternância pode ser compatível com direitos políticos. Corte IDH, OC-28/21 A opinião consultiva anulou diretamente a decisão do tribunal boliviano e restabeleceu a regra constitucional. A Convenção proíbe qualquer reeleição presidencial consecutiva. 
 A Corte Interamericana entendeu que a reeleição presidencial indefinida não constitui um direito humano autônomo. A OC-28/21 foi consultiva: orienta a interpretação da Convenção, mas não anulou a decisão boliviana no processo em que foi proferida.




 02 O que a SCP 0084/2017 afastou
 Duas operações no dispositivo, e nenhuma delas é anular o referendo.
 
 Em 28 de novembro de 2017, a Sala Plena do Tribunal Constitucional Plurinacional (presidente e relator Macario Lahor Cortez Chávez) decidiu duas coisas diferentes. Primeiro, com base no art. 256, declarou a aplicação preferente do art. 23 da Convenção Americana, “por ser la norma más favorable en relación a los Derechos Políticos”, sobre as frases “por una sola vez de manera continua” dos arts. 156 e 168 e “de manera continua por una sola vez” dos arts. 285.II e 288 da Constituição. Segundo, declarou a inconstitucionalidade das mesmas expressões na Lei do Regime Eleitoral (Lei 026/2010).
 Os quatro artigos cobriam presidente e vice-presidente, governadores, assembleístas departamentais, prefeitos e vereadores. A Constituição não foi riscada nem reformada: suas frases deixaram de ser aplicadas porque o Tribunal considerou mais favorável a norma convencional. A lei, essa sim, teve as expressões declaradas inconstitucionais. Seis magistrados assinaram; um sétimo não assinou por não ter participado da sessão, o que não é voto vencido.
 O referendo de 21 de fevereiro de 2016 não era objeto da ação, e a sentença não o anulou nem disse que o “não” valia como “sim”. O que ela fez foi remover a barreira jurídica que o “não” havia mantido. O efeito prático foi o mesmo que a reforma rejeitada teria produzido, e o mais visível foi liberar uma nova candidatura de Evo Morales. Mas a decisão tratou de elegibilidade, não de vitória: quem vence continua sendo decidido nas urnas.



 03 A leitura boliviana do direito de ser eleito
 Princípio contra regra, tratado contra Constituição, candidato contra candidato.
 
 O Tribunal chegou ao dispositivo por três passos. O primeiro foi dentro da própria Constituição. Os arts. 156, 168, 285.II e 288 seriam normas-regra ; os arts. 26 e 28, que reconhecem amplamente o direito de participar do poder político, nas vertentes de votar e de ser votado, seriam normas-princípio . Havendo “antinomia” entre elas, a regra que limita a reeleição cederia ao princípio que amplia a participação.
 O segundo passo trouxe o tratado. O art. 410.II da Constituição boliviana integra os tratados de direitos humanos ao bloco de constitucionalidade, e o art. 256 manda aplicar com preferência os que forem mais favoráveis. Somando a isso os princípios pro homine e de favorabilidade, o Tribunal leu o art. 23 da Convenção como mais generoso que a Constituição: o art. 23.1 garante votar e ser eleito, e o art. 23.2 diz que a lei pode regular esses direitos “exclusivamente” por idade, nacionalidade, residência, idioma, instrução, capacidade civil ou mental, ou condenação penal. Como o limite de mandatos não está na lista, seria uma restrição sem base.
 O terceiro passo foi a igualdade. Os autores da ação haviam sustentado que os limites eram discriminatórios e que não se pode restringir a participação “mientras el soberano así lo desee”, pois quem elege é o povo pelo voto. O Tribunal acolheu o núcleo do argumento: a frase “por una sola vez de manera continua” seria uma medida de exclusão de quem já exerceu o cargo após uma reeleição, frente a quem aspira a ele, sem justificativa objetiva e razoável.
 Aí está o paradoxo que o caso expõe. O vocabulário dos direitos políticos, invocado em nome do soberano, serviu para neutralizar o que o próprio soberano havia decidido no referendo. E a Convenção Americana, que em Gelman limitou a maioria para proteger vítimas, aqui foi usada para ampliar a posição de quem já governava.



 04 A resposta consultiva de 2021
 Consultada pela Colômbia, a Corte leu o mesmo art. 23 em sentido oposto.
 
 Em 21 de outubro de 2019, a Colômbia pediu à Corte Interamericana uma opinião consultiva: a reeleição presidencial indefinida é um direito humano protegido pela Convenção, e proibi-la é compatível com ela? A Corte respondeu em 7 de junho de 2021, por cinco votos a dois.
 Corte IDH · OC-28/21 parte dispositiva 2. La reelección presidencial indefinida no constituye un derecho autónomo protegido por la Convención Americana [...]. 3. La prohibición de la reelección indefinida es compatible con la Convención Americana [...] y la Carta Democrática Interamericana. 4. La habilitación de la reelección presidencial indefinida es contraria a los principios de una democracia representativa.
 Tradução nossa 2. A reeleição presidencial indefinida não constitui um direito autônomo protegido pela Convenção Americana [...]. 3. A proibição da reeleição indefinida é compatível com a Convenção Americana [...] e com a Carta Democrática Interamericana. 4. A habilitação da reeleição presidencial indefinida é contrária aos princípios de uma democracia representativa.
 ver tradução Primeiro, não há direito autônomo. O que a Convenção garante é ser eleito em eleições periódicas e autênticas; nenhum tratado reconhece um direito a ser reeleito para a Presidência. Os Estados escolhem seu sistema político e regulam a reeleição conforme sua história (§ 86), desde que dentro da Convenção.
 Segundo, a palavra “exclusivamente”. É aqui que a leitura boliviana se desfaz. A Corte distinguiu dois regimes. Quando o direito político é restringido por sanção a uma pessoa, como a destituição ou inabilitação de um eleito por autoridade administrativa, o “exclusivamente” vale à letra: só uma condenação penal por juiz competente pode fazê-lo (casos López Mendoza e Petro Urrego, § 107). Mas um sistema eleitoral precisa de regras gerais que vão muito além da lista do art. 23.2, e o parágrafo 2 não pode ser lido isolado do parágrafo 1. Por isso, “por el solo hecho de no estar incluida explícitamente en el artículo 23.2”, a limitação da reeleição não é contrária à Convenção (§ 112).
 Terceiro, o teste da restrição. Não estar na lista não basta para ser válida: a restrição precisa estar prevista em lei, perseguir fim legítimo e ser idônea, necessária e proporcional (§ 114). O fim é legítimo pelo art. 32 da Convenção: evitar que uma pessoa se perpetue no poder e assegurar pluralismo, alternância e freios entre os poderes (§ 119). É idônea, dada a concentração de poder na Presidência (§ 120), e a Corte não encontrou medida menos gravosa igualmente eficaz (§ 121). Na proporcionalidade, pesou dois direitos: o de quem ocupa o cargo, que não tem direito autônomo à reeleição e só perde a chance de concorrer de novo, e o dos demais cidadãos, cujo direito de votar não inclui opções ilimitadas de candidatos (§§ 123–125).
 Quarto, a maioria também tem limite aqui. A Corte afirmou que a eliminação dos limites “no debería ser susceptible de ser decidida por mayorías ni sus representantes para su propio beneficio” (§ 144), e que o maior perigo atual para as democracias da região não é a ruptura abrupta, mas a erosão gradual das salvaguardas, “incluso si este es electo mediante elecciones populares” (§ 145). A Corte também precisou o alcance: a opinião não restringe a reeleição presidencial em geral, mas a ausência de limitação razoável e os mecanismos que permitam a perpetuação de uma mesma pessoa na Presidência (§ 148).
 Esse quarto ponto responde à objeção da soberania. A Corte lembra que os Estados americanos consentiram, soberanamente, que o exercício efetivo da democracia é uma obrigação jurídica internacional (§ 147). Limitar a reeleição presidencial, nessa leitura, não é uma imposição externa contra o povo: é o cumprimento de um compromisso que o próprio Estado assumiu. E a razão de o limite recair sobre a Presidência é institucional: em sistemas presidenciais, como registrou a Comissão de Veneza citada pela Corte, o poder tende a concentrar-se no presidente, enquanto o Legislativo e o Judiciário são relativamente mais fracos (§ 121).
 Falta dizer o que a opinião não é. A Colômbia pediu uma interpretação em abstrato; a Corte não recebeu recurso contra o tribunal boliviano, não julgou a Bolívia em caso contencioso e não anulou a SCP 0084/2017 nem o resultado do referendo. A função consultiva fixa interpretação com autoridade de intérprete final da Convenção, que juízes e autoridades podem usar em controle de convencionalidade, mas não decide fatos, partes ou remédios de um litígio. Para a maioria, haver petições pendentes sobre tema próximo não impedia responder: interpretar em abstrato não é prejulgar aqueles casos.



 05 O alcance dos votos e dos cargos
 Dois dissensos que não dizem a mesma coisa, e dois dispositivos que não cobrem os mesmos cargos.
 
 L. Patricio Pazmiño Freire não se limita a discordar do resultado sobre reeleição. Sua crítica principal é sobre o caminho consultivo. Ele questiona se a consulta colombiana era admissível quando havia petições relacionadas pendentes e critica a maioria por reformular a pergunta e ampliar seu objeto, inclusive interpretando diretamente a Carta Democrática. No mérito, desloca a análise: em vez de tratar a questão como um direito individual de reeleger-se sem limite, propõe examinar em conjunto o direito de votar e ser eleito em condições de igualdade e a relação entre democracia representativa e participativa. Sua objeção alerta para o risco de uma interpretação regional padronizar arranjos políticos nacionais sem demonstrar por que o instrumento confere essa competência.
 Eugenio Raúl Zaffaroni também vê uma consulta ligada a uma controvérsia boliviana concreta e potencialmente contenciosa, mas desenvolve uma crítica própria à competência da Corte para prescrever detalhes de engenharia institucional. No mérito, separa mandato indefinido de reeleição indefinida : no primeiro, o governante não precisa submeter sua permanência a eleições periódicas; no segundo, ele ainda disputa votos em eleições sucessivas. Para Zaffaroni, os tratados não proíbem expressamente a reeleição indefinida, e deduzir essa proibição por analogia adicionaria ao texto um limite à soberania popular que os Estados não pactuaram.
 A divergência entre os juízes, então, tem dois níveis. Pazmiño enfatiza admissibilidade, reformulação da consulta, igualdade eleitoral e pluralismo de modelos; Zaffaroni enfatiza competência para definir detalhes institucionais e a diferença textual entre mandato sem eleição e candidatura reiterada a eleições. Ambos criticam a extensão da atuação consultiva, mas não apresentam uma única tese conjunta. Trate seus votos como dissensos individuais, não como uma posição alternativa unificada.
 Até onde vai cada decisão
 A OC-28 responde sobre a reeleição presidencial indefinida. A SCP 0084/2017 afastou limites para quatro grupos de cargos, inclusive legislativos e subnacionais. Comparar os dois textos, portanto, não decide sozinho a validade de cada limite para prefeitos, vereadores ou assembleístas: para cada cargo, é preciso identificar a norma doméstica e o precedente pertinente. Do mesmo modo, a opinião não condena toda reeleição. Uma regra que permite uma reeleição consecutiva e proíbe a seguinte é exatamente o tipo de limitação razoável que ela considera compatível; quem disputa a única reeleição permitida não está no caso de quem busca um terceiro mandato seguido.



 06 Três usos da Convenção
 O mesmo vocabulário, três direções.
 
 Postas lado a lado, as três decisões mostram que “direitos humanos” não é um argumento que aponta sempre para o mesmo lado. Em cada uma, pergunte de quem é o direito invocado e contra quem ele é usado.



 
 
 Fig. 1 · Três usos da Convenção 1 / 3 
 

 
 Gelman A Convenção contra a maioria, a favor das vítimas
 Em Gelman, a Corte IDH usou a Convenção para afirmar que uma decisão majoritária (a Lei de Caducidade, confirmada em referendo e plebiscito) não pode impedir a investigação de graves violações. O limite protege as vítimas.



 Bolívia A Convenção contra a Constituição
 O TCP declarou a aplicação preferente do art. 23 da Convenção sobre as frases “por una sola vez de manera continua” da Constituição e declarou inconstitucionais as mesmas frases da Lei do Regime Eleitoral. O referendo de 2016 não foi anulado, mas perdeu efeito prático: a candidatura que ele recusara ficou liberada. O “direito” protegido era o de quem ocupava o poder de concorrer outra vez.



 OC-28 A Convenção a favor dos limites
 Em 2021, respondendo a uma consulta da Colômbia, a Corte IDH disse que a Convenção não garante reeleição presidencial indefinida, e que proibi-la é compatível com ela. A opinião consultiva não revisa nem anula a sentença boliviana; mas, lidas lado a lado, as duas decisões interpretam o mesmo art. 23 em sentidos opostos. Aqui a Convenção protege a alternância e, com ela, os direitos políticos de todos os demais.



 



 Gelman e a OC-28 convergem num ponto que a SCP contrariou: há matérias que a maioria não decide sozinha. Em Gelman, a impunidade de graves violações (§ 239); na OC-28, a remoção dos limites à permanência no poder em benefício de quem o exerce (§ 144). O Tribunal boliviano fez o movimento inverso, usando um direito individual para desfazer, na prática, uma decisão majoritária que protegia a alternância.



 07 Responder ao eixo com os casos
 Tese, casos, divergência e posição.
 
 Eixo de discussão da aula Pode uma decisão majoritária afastar direitos protegidos constitucional e internacionalmente? Quais são os limites da soberania popular?
 Tese. A maioria tem limites, mas os limites não apontam todos para o mesmo lado.
 Contraste. Corte IDH, Gelman (2011): o voto popular não legitima a impunidade de graves violações.
 O caso boliviano. TCP, SCP 0084/2017: aplicação preferente do art. 23 sobre os limites constitucionais e inconstitucionalidade dos legais, por princípio contra regra, art. 256 e igualdade; sem anular o referendo.
 A leitura interamericana. Corte IDH, OC-28/21 (5 × 2): não há direito autônomo à reeleição presidencial indefinida; o “exclusivamente” vale para sanções, não para regras gerais; a proibição passa no teste; e a remoção dos limites não deveria ser decidida por maiorias em benefício próprio. Opinião consultiva, não recurso.
 Divergência. Pazmiño: admissibilidade, reformulação da consulta, igualdade eleitoral e pluralismo de modelos. Zaffaroni: competência para prescrever engenharia institucional e mandato sem eleição × candidatura reiterada.
 Posição. Diga qual leitura do art. 23 você sustenta e por quê, separando o plano doméstico do interamericano.
 


 08 Teste
 Responda antes de abrir.
 
 
 Qual dispositivo da Constituição boliviana permitiu ao TCP aplicar a Convenção por cima dela?
 O art. 256: tratados de direitos humanos que declarem direitos mais favoráveis aplicam-se de maneira preferente sobre a Constituição.
 O que a SCP 0084/2017 decidiu, exatamente?
 Declarou a aplicação preferente do art. 23 da Convenção sobre as expressões “por una sola vez de manera continua” dos arts. 156, 168, 285.II e 288 da Constituição, e a inconstitucionalidade das expressões equivalentes da Lei 026/2010 (regime eleitoral).
 Por que a decisão boliviana é um “paradoxo” da soberania popular?
 Porque invocou direitos políticos para liberar a candidatura que a maioria havia recusado no referendo de 2016. O Tribunal não anulou o referendo: afastou as regras que limitavam a reeleição, com o mesmo efeito prático que o “sim” teria tido.
 Quais são as três respostas da OC-28/21?
 A reeleição presidencial indefinida não é direito autônomo; sua proibição é compatível com a Convenção, a Declaração Americana e a Carta Democrática; e habilitá-la é contrário aos princípios da democracia representativa. Votação: 5 × 2 (vencidos Pazmiño Freire e Zaffaroni).
 Como Gelman e a SCP 0084/2017 usam a Convenção em direções opostas?
 Em Gelman, a Convenção limita a maioria para proteger as vítimas. Na Bolívia, é aplicada com preferência sobre a Constituição para ampliar o direito de quem governa de concorrer outra vez, apesar do resultado do referendo.
 Por que a ausência da reeleição na lista do art. 23.2 não torna o limite inválido, segundo a OC-28?
 Porque o “exclusivamente” se aplica às restrições por sanção individual (só por condenação penal de juiz competente, como em López Mendoza e Petro), não às regras gerais que todo sistema eleitoral precisa. O art. 23.2 não pode ser lido isolado do 23.1 (§§ 107–112). A restrição ainda precisa passar no teste de legalidade, fim legítimo, idoneidade, necessidade e proporcionalidade.
 A OC-28 proíbe que um prefeito boliviano dispute a reeleição, ou que um presidente dispute a única reeleição permitida?
 Não decide nenhum dos dois. Ela responde sobre a reeleição presidencial indefinida; não transporta automaticamente a conclusão a cargos locais, e uma regra que permite uma reeleição e veda a seguinte é o tipo de limitação razoável que considera compatível.
 Eixo: um tribunal invoca o direito de ser eleito para afastar um limite de mandatos que o eleitorado se recusou a mudar. Responda com os casos.
 Comece pelo contraste com Gelman (a maioria não legitima a impunidade). Descreva a SCP 0084/2017 com precisão (aplicação preferente e inconstitucionalidade; referendo não anulado; princípio × regra, art. 256, igualdade). Oponha a OC-28/21: não há direito autônomo, o limite passa no teste, e a remoção dos limites não deveria ser decidida por maiorias em benefício próprio (§ 144), lembrando que é consultiva. Registre Pazmiño e Zaffaroni separadamente. Conclua com sua leitura do art. 23.
