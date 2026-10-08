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
- line 42 `negative-parallelism`: “não é”
- line 45 `negative-parallelism`: “não era”
- line 76 `negative-parallelism`: “não é”
- line 134 `negative-parallelism`: “não é”
- line 167 `negative-parallelism`: “não era”
- line 168 `negative-parallelism`: “Não foi”
- line 11 `negated-inference`: “não basta”
- line 33 `negated-inference`: “não tornam”
- line 47 `negated-inference`: “não garante”
- line 52 `negated-inference`: “não cria”
- line 117 `negated-inference`: “não resolve”
- line 26 `colon-reveal`: “848, de Caducidade da Pretensão Punitiva do Estado: o Estado renunciava a punir os crimes cometidos até 1º de março de 1985 por militares e policiais, por motivos políticos ou em cumprimento de ordens.”
- line 31 `colon-reveal`: “Antes de ler: como decidir?”
- line 42 `colon-reveal`: “O primeiro está no § 229: a incompatibilidade não se restringe às autoanistias .”
- line 45 `colon-reveal`: “ver tradução O segundo passo responde exatamente ao que distinguia o caso uruguaio: a lei não era uma autoanistia de ditadura, e o povo a confirmou duas vezes.”
- line 45 `colon-reveal`: “E no § 239 formula o princípio: Corte IDH · Gelman vs.”
- line 48 `colon-reveal`: “Por isso a condenação não se limita ao caso: o Uruguai descumpriu o dever de adequar seu direito interno à Convenção (art.”
- line 51 `colon-reveal`: “mas o juiz Eduardo Vio Grossi juntou um voto concorrente que explica o passo mais ousado da sentença: imputar ao Estado o resultado de uma votação popular.”
- line 52 `colon-reveal`: “Vio Grossi apoia a frase do § 239 na Carta Democrática Interamericana: ela faz do respeito aos direitos humanos §§§§§§§§§§§§§§§§§§ da democracia (art.”
- line 52 `colon-reveal`: “O mesmo voto traz uma advertência que reaparecerá em Montevidéu: a jurisprudência da Corte é fonte auxiliar do direito internacional.”
- line 59 `colon-reveal`: “A lei restabeleceu a pretensão punitiva do Estado, e seus três artigos fazem coisas diferentes: o art.”
- line 60 `colon-reveal`: “20/2013 , de 22 de fevereiro de 2013, a Suprema Corte de Justiça acolheu a exceção só em parte: declarou inconstitucionais e inaplicáveis aos excepcionantes os arts.”
- line 60 `colon-reveal`: “10 e 72): suspender retroativamente a prescrição e requalificar retroativamente os crimes agravava a situação de quem já havia adquirido o direito à prescrição.”
- line 61 `colon-reveal`: “ou descumprir a Corte IDH, mas de exercer o controle de constitucionalidade, que é irrenunciável: se a Corte IDH é a intérprete última da Convenção, a Suprema Corte é a intérprete última da Constituição uruguaia.”
- line 61 `colon-reveal`: “Cita ainda a crítica de Néstor Sagüés ao controle de convencionalidade: Estados passam a ficar vinculados por jurisprudência formada em processos dos quais não foram parte.”
- line 63 `colon-reveal`: “3º admite interpretação conforme à Constituição: nem todo delito coberto pela Lei de Caducidade é de lesa-humanidade, e cabe ao juiz do mérito qualificar cada conduta.”
- line 64 `colon-reveal`: “A Sentencia 65/2014 da mesma Suprema Corte, de 17 de março de 2014, julga outra matéria: uma exceção contra o art.”
- line 71 `colon-reveal`: “A pergunta era outra: depois da sentença de 2011, o Estado tinha tomado as medidas necessárias para que a Lei de Caducidade e obstáculos semelhantes não bloqueassem a investigação?”
- line 75 `colon-reveal`: “tese uruguaia de que a decisão só produzia efeito no processo concreto, e respondeu com o raciocínio: a fundamentação podia ser reiterada em casos análogos.”
- line 76 `colon-reveal`: “O desaparecimento forçado é uma violação continuada: enquanto não se conhece o destino da pessoa, o delito continua.”
- line 77 `colon-reveal`: “O conflito real está no efeito prático: se o raciocínio da Sentencia 20/2013 se repete, a ordem do ponto 11 deixa de ser cumprida.”
- line 82 `colon-reveal`: “Nem toda anistia é igual: a legitimidade democrática tem graus.”
- line 91 `colon-reveal`: “a favor dos próprios militares, antes de deixar o poder, no pior momento de popularidade do regime: um caso-limite de falta de legitimidade.”
- line 106 `colon-reveal`: “a ditadura, os uruguaios já tinham rejeitado por mais de 57% um plebiscito convocado pelos militares: o eleitorado sabia dizer não.”
- line 114 `colon-reveal`: “A Corte confunde reproche, sanção e castigo: trata a prisão como a única forma de expressar a máxima reprovação social.”
- line 114 `colon-reveal`: “Seu ponto é mais estreito: antes de concluir que a Convenção exige o castigo penal como única resposta, a Corte precisava justificar essa leitura.”
- line 116 `colon-reveal`: “que o Uruguai também aderiu democraticamente ao sistema interamericano e ratificou a Convenção: há pedigree democrático na autoridade regional.”
- line 116 `colon-reveal`: “E lembra que juízes também discordam sobre o conteúdo dos direitos e resolvem o desacordo votando: a regra majoritária não desaparece quando a decisão é judicial, muda de foro e de composição.”
- line 117 `colon-reveal`: “Uma ressalva do próprio Gargarella evita a leitura caricata: há boas razões de igualdade para não dar tratamento especial justamente aos autores dos piores crimes da história da região.”
- line 117 `colon-reveal`: “Na prática, a diferença é verificável: memorial, reparação e pedido de perdão, sem investigar o desaparecimento, não satisfazem a ordem concreta de Gelman.”
- line 127 `colon-reveal`: “Delas sai o ponto 11: a lei não pode obstruir a investigação.”
- line 131 `colon-reveal`: “Ataca o § 229 e os §§ 238–239: tratar da mesma forma uma autoanistia de ditadura e uma lei confirmada por plebiscito ignora diferenças de legitimidade que importam.”
- line 135 `colon-reveal`: “A segunda crítica mira a premissa por trás do ponto 9: que responder a graves violações exige, sempre, investigação e sanção penal.”
- line 151 `colon-reveal`: “Para a Corte IDH (2011, unânime), não pode: a proteção dos direitos humanos é limite intransponível à regra da maioria, e o voto popular, por ser ato do Estado, gera responsabilidade como qualquer lei.”
- line 154 `colon-reveal`: “Para cada um: tribunal, ano, o que decidiu, por quê.”
- line 155 `colon-reveal`: “Quem discordou e como: Pérez Manrique contra a maioria uruguaia; Gargarella contra a Corte IDH; Vio Grossi concorda, mas por um fundamento próprio.”
- line 158 `colon-reveal`: “E se alguém disser que a Sentencia 20/2013 anulou Gelman, a resposta é não: são decisões de planos diferentes, e a sentença internacional continua vinculando o Uruguai.”
- line 159 `colon-reveal`: “O caso inverso vem na Aula 06: na Bolívia, um tribunal usou a Convenção Americana para ampliar o que a maioria havia recusado no voto.”
- line 172 `colon-reveal`: “10 e 72 da Constituição uruguaia): suspender retroativamente a prescrição e requalificar retroativamente os delitos como lesa-humanidade prejudicava os acusados.”
- line 176 `colon-reveal`: “de que anistias diferem em legitimidade democrática, conforme a inclusão e o debate que as cercaram: da autoanistia de Bignone à lei de Fujimori, às leis de perdão de Alfonsín e, no topo, à lei uruguaia confirmada por duas consultas populares.”
- line 178 `colon-reveal`: “Ninguém: os pontos resolutivos foram votados por unanimidade.”
- line 183 `colon-reveal`: “Eixo: um país aprova em referendo uma lei que extingue a punibilidade de desaparecimentos forçados cometidos sob a ditadura.”
- line 42 `denial-restatement`: “não é o processo de adoção nem a autoridade que editou a lei, mas a sua ratio legis , isto é, deixar impunes graves violações”
- line 61 `denial-restatement`: “não trata de cumprir ou descumprir a Corte IDH, mas de exercer o controle de constitucionalidade, que é irrenunciável”
- line 170 `denial-restatement`: “não depende do processo de adoção nem da autoridade que as editou, mas da ratio legis de deixar impunes graves violações”
- line 25 `triad-density`: “argentina de 19 anos, estudante de Filosofia e Letras, foi detida em Buenos Aires em 24 de agosto de 1976,”
- line 25 `triad-density`: “filho do poeta Juan Gelman, por comandos militares uruguaios e argentinos”
- line 41 `triad-density`: “Peru (2001): são inadmissíveis anistias, prescrições e excludentes de responsabilidade que impeçam a investigação e”
- line 41 `triad-density`: “como tortura, execuções e desaparecimentos forçados (§ 225)”
- line 48 `triad-density`: “Mesmo assim, o principal obstáculo às investigações tinha sido a vigência e a aplicação da própria lei (§ 241)”
- line 48 `triad-density`: “2º), pela interpretação e aplicação que deu à Lei de Caducidade em graves violações”
- line 49 `triad-density`: “responsável pelo desaparecimento forçado de María Claudia, pela supressão e substituição da identidade de Macarena, tratada como forma d”
- line 49 `triad-density`: “Mandou conduzir a investigação, determinar responsabilidades e aplicar as sanções cabíveis (ponto 9), continuar a busca por”
- line 49 `triad-density`: “por carecer de efeitos, não volte a obstruir a investigação deste e de outros casos de graves violações (ponto 11)”
- line 51 `triad-density`: “Logo, a cidadania inteira pode violar uma norma internacional e comprometer a responsabilidade do Estado”
- line 60 `triad-density`: “O fundamento foi a irretroatividade da lei penal mais grave, que decorre dos princípios de liberdade e legalidade da Constituição uruguaia (arts”
- line 62 `triad-density`: “O problema está no raciocínio, que pode ser repetido em cada caso análogo e conduzir à prescrição de todos eles”
- line 75 `triad-density`: “a Corte reconheceu os passos concretos do Uruguai, o Decreto 323 e a Lei 18”
- line 75 `triad-density`: “expostas constituíam um obstáculo ao pleno cumprimento , que poderia quebrar o acesso das vítimas à justiça e perpetuar a impunidade”
- line 75 `triad-density`: “vinculante em sua integralidade, nas partes considerativas e dispositivas, para todos os órgãos uruguaios”
- line 76 `triad-density`: “remover obstáculos, formar agentes e garantir acesso a arquivos”
- line 96 `triad-density`: “em 1995 pelo Congresso que se seguiu ao autogolpe de 1992, num contexto de fortes restrições às liberdades civis e políticas”
- line 101 `triad-density`: “com amplas liberdades, mobilização nas ruas e debate público, e depois mantidas pela Corte Suprema argenti”
- line 106 `triad-density`: “No topo está a lei uruguaia: aprovada em plena democracia, afetada por medos e por pressões militares, mas reforçada por duas consultas pop”
- line 114 `triad-density`: “A Corte confunde reproche, sanção e castigo: trata a prisão como a única forma de expressar a má”
- line 115 `triad-density`: “investigar, sancionar e reparar”
- line 116 `triad-density`: “regra majoritária não desaparece quando a decisão é judicial, muda de foro e de composição”
- line 117 `triad-density`: “a diferença é verificável: memorial, reparação e pedido de perdão, sem investigar o desaparecimento, não sati”
- line 135 `triad-density`: “sempre, investigação e sanção penal”
- line 135 `triad-density`: “Verdade, reparação e memória também são formas de reprovação”
- line 176 `triad-density`: “A ideia de que anistias diferem em legitimidade democrática, conforme a inclusão e o debate que as cercaram: da autoanistia de Bignone à lei de”
- line 148 `stacked-questions`: “Pode uma decisão majoritária afastar direitos protegidos constitucional e internacionalmente? Eixo de discussão da aula Pode uma decisão majoritária afastar direitos protegidos constitucional e internacionalmente?”
- line 181 `stacked-questions`: “A Sentencia 20/2013 anulou Gelman? O que a Corte IDH disse dela?”

---
# Frozen draft: aula-05.html

Direito Latino-americano DIR03057 UFRGS · 2026/2 

 A maioria e os direitos 

 O Uruguai confirmou duas vezes, pelo voto, uma lei que impedia punir os crimes da ditadura. A Corte Interamericana disse que o voto não basta . Gargarella perguntou se todo voto vale o mesmo .

 
 Aula 31/08 · Soberania popular 
 Leitura ≈ 20 min 
 Antes Aula 04 · Colômbia 
 Depois Aula 06 · Bolívia e OC-28 


 
 
 01 Os fatos do caso Gelman
 Um desaparecimento da Operação Condor e uma lei aprovada, e duas vezes confirmada, pela democracia uruguaia.
 
 María Claudia García Iruretagoyena, argentina de 19 anos, estudante de Filosofia e Letras, foi detida em Buenos Aires em 24 de agosto de 1976, grávida de cerca de sete meses, com o marido Marcelo Gelman, filho do poeta Juan Gelman, por comandos militares uruguaios e argentinos. Foi levada ao Uruguai, onde deu à luz uma menina, entregue a uma família uruguaia. María Claudia continua desaparecida. A filha, María Macarena Gelman, só recuperou sua identidade anos depois. Os fatos se inserem na Operação Condor, a aliança secreta de repressão entre as ditaduras do Cone Sul.
 O obstáculo à investigação foi uma lei da democracia. Em 1986, o governo eleito do Uruguai promulgou a Lei 15.848, de Caducidade da Pretensão Punitiva do Estado: o Estado renunciava a punir os crimes cometidos até 1º de março de 1985 por militares e policiais, por motivos políticos ou em cumprimento de ordens. A lei foi submetida duas vezes ao voto popular. Em 1989, um referendo a manteve. Em 25 de outubro de 2009, um plebiscito sobre uma reforma constitucional que declararia nulos os arts. 1 a 4 não obteve os votos necessários.
 A Comissão Interamericana levou o caso à Corte em janeiro de 2010. A Corte julgou em 24 de fevereiro de 2011 .



 Antes de ler: como decidir? No caso Gelman vs. Uruguai (2011), a Corte Interamericana examinou a Lei de Caducidade, que impedia investigar graves violações cometidas durante a ditadura e havia sido mantida em duas consultas populares. A Convenção Americana obriga o Estado a investigar violações graves e a garantir proteção judicial. A aprovação democrática da lei, por si só, impede a Corte de considerá-la sem efeitos?
 Sim. Uma lei confirmada pelo voto popular prevalece sobre a obrigação internacional de investigar. Não. A maioria não pode autorizar a impunidade por graves violações, mesmo quando a lei foi aprovada democraticamente. Corte IDH, Gelman vs. Uruguai (2011) Sim, exceto quando a lei tiver sido aprovada por uma ditadura. Não, mas apenas porque a Lei de Caducidade era uma autoanistia militar. 
 A Corte entendeu que a origem democrática e a ratificação popular não tornam legítima, por si sós, uma lei que impeça a investigação de graves violações. Direitos humanos impõem limites à regra da maioria.




 02 O que a Corte Interamericana decidiu
 As anistias para graves violações não têm efeito jurídico, venham de onde vierem.
 
 A Corte reafirmou a linha que vinha desde Barrios Altos vs. Peru (2001): são inadmissíveis anistias, prescrições e excludentes de responsabilidade que impeçam a investigação e a punição de graves violações, como tortura, execuções e desaparecimentos forçados (§ 225). Essas leis violam os arts. 1.1 e 2 da Convenção, porque impedem que as vítimas sejam ouvidas por um juiz (art. 8.1) e recebam proteção judicial (art. 25), e por isso “ carecem de efeitos jurídicos ” (§ 226).
 Dois passos da sentença vão além dessa linha. O primeiro está no § 229: a incompatibilidade não se restringe às autoanistias . O que importa não é o processo de adoção nem a autoridade que editou a lei, mas a sua ratio legis , isto é, deixar impunes graves violações. A incompatibilidade é material, não formal. 
 Corte IDH · Gelman vs. Uruguai (2011) § 238 El hecho de que la Ley de Caducidad haya sido aprobada en un régimen democrático y aún ratificada o respaldada por la ciudadanía en dos ocasiones no le concede, automáticamente ni por sí sola, legitimidad ante el Derecho Internacional .
 Tradução nossa O fato de a Lei de Caducidade ter sido aprovada num regime democrático e ainda ratificada ou respaldada pela cidadania em duas ocasiões não lhe concede, automaticamente nem por si só, legitimidade perante o Direito Internacional.
 ver tradução O segundo passo responde exatamente ao que distinguia o caso uruguaio: a lei não era uma autoanistia de ditadura, e o povo a confirmou duas vezes. Para a Corte, o referendo de 1989 (art. 79 da Constituição uruguaia) e o plebiscito de 2009 (art. 331) são atos atribuíveis ao Estado e, portanto, também geram responsabilidade internacional (§ 238). E no § 239 formula o princípio:
 Corte IDH · Gelman vs. Uruguai (2011) § 239 La sola existencia de un régimen democrático no garantiza, per se, el permanente respeto del Derecho Internacional [...]. La legitimación democrática de determinados hechos o actos en una sociedad está limitada por las normas y obligaciones internacionales de protección de los derechos humanos [...], la protección de los derechos humanos constituye un límite infranqueable a la regla de mayorías , es decir, a la esfera de lo “susceptible de ser decidido” por parte de las mayorías.
 Tradução nossa A mera existência de um regime democrático não garante, por si só, o respeito permanente ao Direito Internacional [...]. A legitimação democrática de determinados fatos ou atos numa sociedade está limitada pelas normas e obrigações internacionais de proteção dos direitos humanos [...], a proteção dos direitos humanos constitui um limite intransponível à regra das maiorias, isto é, à esfera do “suscetível de ser decidido” pelas maiorias.
 ver tradução O caso tinha uma particularidade que a Corte registrou sem se deixar desviar por ela. Desde 23 de junho de 2005, o Executivo uruguaio entendia que o caso Gelman estava fora do alcance da Lei de Caducidade, e a investigação havia sido reaberta. Mesmo assim, o principal obstáculo às investigações tinha sido a vigência e a aplicação da própria lei (§ 241). Por isso a condenação não se limita ao caso: o Uruguai descumpriu o dever de adequar seu direito interno à Convenção (art. 2º), pela interpretação e aplicação que deu à Lei de Caducidade em graves violações.
 Nos pontos resolutivos, todos votados por unanimidade, a Corte declarou o Uruguai responsável pelo desaparecimento forçado de María Claudia, pela supressão e substituição da identidade de Macarena, tratada como forma de desaparecimento forçado, e pela falta de investigação. Mandou conduzir a investigação, determinar responsabilidades e aplicar as sanções cabíveis (ponto 9), continuar a busca por María Claudia (ponto 10) e garantir que a Lei de Caducidade, por carecer de efeitos, não volte a obstruir a investigação deste e de outros casos de graves violações (ponto 11).
 O voto de Vio Grossi: por que o eleitorado responde pelo Estado
 Ninguém divergiu, mas o juiz Eduardo Vio Grossi juntou um voto concorrente que explica o passo mais ousado da sentença: imputar ao Estado o resultado de uma votação popular. Pelas regras de responsabilidade internacional codificadas pela Comissão de Direito Internacional da ONU, é ato do Estado o comportamento de qualquer de seus órgãos, exerça ele funções legislativas, executivas, judiciais ou “de outra índole”. Quando o eleitorado aprova ou ratifica uma lei, exerce função legislativa, ou ao menos uma função de outra índole, a da democracia direta. Logo, a cidadania inteira pode violar uma norma internacional e comprometer a responsabilidade do Estado. A qualificação de um ato como ilícito pelo direito internacional não depende do que diz o direito interno.
 Vio Grossi apoia a frase do § 239 na Carta Democrática Interamericana: ela faz do respeito aos direitos humanos elemento essencial da democracia (art. 3º) e, no art. 8º, garante a quem se considere violado o acesso ao sistema interamericano de petições, e não aos órgãos políticos da OEA. O mesmo voto traz uma advertência que reaparecerá em Montevidéu: a jurisprudência da Corte é fonte auxiliar do direito internacional. Ela interpreta o tratado, o costume ou o princípio vigente para o Estado; não cria direito novo .



 03 A reação uruguaia
 O Legislativo cumpriu a sentença; a Suprema Corte derrubou parte do cumprimento.
 
 O Uruguai começou a cumprir. O Decreto 323, de 30 de junho de 2011, e a Lei 18.831, de 27 de outubro de 2011, foram passos que a própria Corte IDH depois reconheceria como concretos. A lei restabeleceu a pretensão punitiva do Estado, e seus três artigos fazem coisas diferentes: o art. 1º restaura a possibilidade de processar os crimes cobertos pela Lei de Caducidade; o art. 2º manda não computar prazo algum de prescrição ou caducidade entre 22 de dezembro de 1986 e a vigência da nova lei; o art. 3º declara esses delitos crimes de lesa-humanidade, conforme os tratados de que o Uruguai é parte.
 Investigados opuseram exceção de inconstitucionalidade contra os três artigos. Na Sentencia 20/2013 , de 22 de fevereiro de 2013, a Suprema Corte de Justiça acolheu a exceção só em parte: declarou inconstitucionais e inaplicáveis aos excepcionantes os arts. 2º e 3º e rejeitou o resto, de modo que o art. 1º ficou de pé. O fundamento foi a irretroatividade da lei penal mais grave, que decorre dos princípios de liberdade e legalidade da Constituição uruguaia (arts. 10 e 72): suspender retroativamente a prescrição e requalificar retroativamente os crimes agravava a situação de quem já havia adquirido o direito à prescrição.
 O acórdão enfrenta Gelman sem negá-lo de frente. A maioria afirma que o caso não trata de cumprir ou descumprir a Corte IDH, mas de exercer o controle de constitucionalidade, que é irrenunciável: se a Corte IDH é a intérprete última da Convenção, a Suprema Corte é a intérprete última da Constituição uruguaia. Cita ainda a crítica de Néstor Sagüés ao controle de convencionalidade: Estados passam a ficar vinculados por jurisprudência formada em processos dos quais não foram parte. A objeção tem parentesco com a advertência de Vio Grossi sobre a jurisprudência como fonte auxiliar, levada a uma conclusão que ele não tirou.
 Formalmente, a decisão vale só para os excepcionantes daquele processo. O problema está no raciocínio, que pode ser repetido em cada caso análogo e conduzir à prescrição de todos eles.
 Ricardo Pérez Manrique ficou vencido, por três razões. Os arts. 2º e 3º nem se aplicavam ao caso concreto. Também não inovavam: os tratados de direitos humanos têm raiz constitucional no Uruguai, e os crimes contra a humanidade são imprescritíveis por integrarem o jus cogens desde Nuremberg; a convenção sobre imprescritibilidade apenas declara obrigações preexistentes. Por fim, o art. 3º admite interpretação conforme à Constituição: nem todo delito coberto pela Lei de Caducidade é de lesa-humanidade, e cabe ao juiz do mérito qualificar cada conduta. Onde a maioria dá peso à data em que o regime legal foi positivado, Pérez Manrique dá peso ao caráter inderrogável da proibição internacional.
 A Sentencia 65/2014 da mesma Suprema Corte, de 17 de março de 2014, julga outra matéria: uma exceção contra o art. 365 do Código Penal, na redação da Lei 19.120, que trata de faltas como a falta de respeito à autoridade. Não trata de Gelman nem da Lei 18.831.



 04 A resposta da Corte em 2013
 A supervisão não anula a decisão uruguaia; chama-a de obstáculo.
 
 Um mês depois, em 20 de março de 2013, a Corte IDH emitiu resolução de supervisão de cumprimento. Não funcionou como recurso contra a Sentencia 20/2013 nem declarou seus efeitos anulados. A pergunta era outra: depois da sentença de 2011, o Estado tinha tomado as medidas necessárias para que a Lei de Caducidade e obstáculos semelhantes não bloqueassem a investigação?
 Corte IDH · supervisão Gelman (2013) considerando 102 La obligación del Estado de dar pronto cumplimiento a las decisiones de la Corte […] vincula a todos sus poderes y órganos, incluidos sus jueces […], por lo cual no puede invocar disposiciones del derecho constitucional u otros aspectos del derecho interno para justificar una falta de cumplimiento de la Sentencia.
 Tradução nossa A obrigação do Estado de dar pronto cumprimento às decisões da Corte […] vincula todos os seus poderes e órgãos, incluídos seus juízes […], pelo que não pode invocar disposições do direito constitucional ou outros aspectos do direito interno para justificar um descumprimento da Sentença.
 ver tradução Em português: a obrigação de cumprir vincula todos os poderes e órgãos, inclusive os juízes, e o Estado não pode invocar a própria Constituição para justificar o descumprimento. A Corte acrescentou que seria contraditório usar o controle de convencionalidade, um instrumento para aplicar o direito internacional, como justificativa para deixar de cumprir a sentença.
 No considerando 103, a Corte reconheceu os passos concretos do Uruguai, o Decreto 323 e a Lei 18.831, e disse que a decisão de 22 de fevereiro de 2013 não estava em consonância com a evolução do direito interamericano e universal dos direitos humanos. Mesmo contendo reflexões dirigidas a cumprir a sentença, pela maneira como estavam expostas constituíam um obstáculo ao pleno cumprimento , que poderia quebrar o acesso das vítimas à justiça e perpetuar a impunidade. A resolução registrou a tese uruguaia de que a decisão só produzia efeito no processo concreto, e respondeu com o raciocínio: a fundamentação podia ser reiterada em casos análogos. No considerando 104, afirmou que a sentença de 2011 é coisa julgada internacional, vinculante em sua integralidade, nas partes considerativas e dispositivas, para todos os órgãos uruguaios.
 A Corte enfrentou também a objeção de irretroatividade. O desaparecimento forçado é uma violação continuada: enquanto não se conhece o destino da pessoa, o delito continua. Aplicar a tipificação uruguaia de desaparecimento forçado, em vigor desde 2006, a um desaparecimento ainda em curso não é aplicar retroativamente uma lei nova a um fato encerrado. A supervisão manteve abertas as obrigações de investigar, buscar María Claudia, remover obstáculos, formar agentes e garantir acesso a arquivos.
 As duas cortes, portanto, não se contradizem no mesmo plano. A Suprema Corte decidiu o dever doméstico de cada juiz naquele processo, à luz da Constituição. A Corte IDH decidiu o dever internacional do Uruguai, como Estado, de cumprir uma sentença em caso do qual foi parte. O conflito real está no efeito prático: se o raciocínio da Sentencia 20/2013 se repete, a ordem do ponto 11 deixa de ser cumprida.



 05 A crítica de Gargarella
 Nem toda anistia é igual: a legitimidade democrática tem graus.
 
 
 
 Fig. 1 · A gradação democrática 1 / 4 
 

 
 Grau 1 A autoanistia da ditadura argentina
 Roberto Gargarella aceita que as anistias da região foram muitas e diversas, e critica a Corte por tratá-las todas do mesmo modo. No extremo inferior está a anistia editada pelo general Bignone a favor dos próprios militares, antes de deixar o poder, no pior momento de popularidade do regime: um caso-limite de falta de legitimidade.



 Grau 2 A lei de Fujimori
 Em seguida, a anistia peruana aprovada em 1995 pelo Congresso que se seguiu ao autogolpe de 1992, num contexto de fortes restrições às liberdades civis e políticas. A presunção de validade é muito baixa.



 Grau 3 As leis de perdão de Alfonsín
 As leis de perdão do governo Alfonsín foram aprovadas por um Congresso democrático, com amplas liberdades, mobilização nas ruas e debate público, e depois mantidas pela Corte Suprema argentina. Mas surgiram sob pressão militar ilegítima, que culminou no levante da Semana Santa. São, em princípio, legítimas, mas golpeadas em sua legitimidade.



 Grau 4 A Lei de Caducidade uruguaia
 No topo está a lei uruguaia: aprovada em plena democracia, afetada por medos e por pressões militares, mas reforçada por duas consultas populares, que Gargarella considera a expressão máxima da soberania popular. Ele lembra que, em 1980, sob a ditadura, os uruguaios já tinham rejeitado por mais de 57% um plebiscito convocado pelos militares: o eleitorado sabia dizer não. Para ele, a Corte IDH deveria ter feito um esforço argumentativo especial para distinguir esta lei da autoanistia de Bignone, e desautorizou a decisão democrática “em menos de dez linhas”.



 



 Gargarella acrescenta uma segunda crítica. A Corte confunde reproche, sanção e castigo: trata a prisão como a única forma de expressar a máxima reprovação social. Uma comunidade democrática pode escolher outras formas de responder a crimes massivos: comissões de verdade (Chile, El Salvador, a Comissão para a Paz uruguaia, a Comissão Nacional da Verdade brasileira), reparações, pedidos públicos de perdão, memoriais, arquivos, “juízos pela verdade”. Ele não sustenta que essas alternativas sejam superiores nem pede impunidade. Seu ponto é mais estreito: antes de concluir que a Convenção exige o castigo penal como única resposta, a Corte precisava justificar essa leitura.
 A disputa aparece no art. 1.1 da Convenção. A Corte lê o dever de respeitar e garantir direitos como fundamento para prevenir, investigar, sancionar e reparar; Gargarella observa que a redação do artigo não enumera essa sequência e questiona a passagem que converte o dever de garantia em obrigação de sancionar penalmente. A crítica não demonstra que a Corte esteja errada. Identifica o passo que ela precisa justificar.
 Víctor Abramovich, ex-vice-presidente da Comissão Interamericana, objeta que o Uruguai também aderiu democraticamente ao sistema interamericano e ratificou a Convenção: há pedigree democrático na autoridade regional. Gargarella responde que aceitar um tribunal abre, em vez de encerrar, a discussão sobre o alcance de sua autoridade. E lembra que juízes também discordam sobre o conteúdo dos direitos e resolvem o desacordo votando: a regra majoritária não desaparece quando a decisão é judicial, muda de foro e de composição.
 Uma ressalva do próprio Gargarella evita a leitura caricata: há boas razões de igualdade para não dar tratamento especial justamente aos autores dos piores crimes da história da região. O que ele recusa é que isso justifique, sem discussão, o modelo punitivo como única resposta possível. Na prática, a diferença é verificável: memorial, reparação e pedido de perdão, sem investigar o desaparecimento, não satisfazem a ordem concreta de Gelman. Mas reconhecer o dever de investigar não resolve sozinho qual sanção é devida em cada processo.



 
 Fig. 2 · A sentença e suas objeções 1 / 4 
 

 
 A sentença Três razões, uma ordem
 A conclusão da Corte se apoia em três razões que se reforçam: a anistia impede que as vítimas sejam ouvidas e protegidas (§ 226); o que conta é o efeito da lei, não sua origem (§ 229); e o voto popular não dá à lei legitimidade perante o direito internacional (§§ 238–239). Delas sai o ponto 11: a lei não pode obstruir a investigação.


 Primeira objeção A gradação ataca duas razões
 Gargarella não nega o § 226. Ataca o § 229 e os §§ 238–239: tratar da mesma forma uma autoanistia de ditadura e uma lei confirmada por plebiscito ignora diferenças de legitimidade que importam.


 Segunda objeção Reproche não é só castigo
 A segunda crítica mira a premissa por trás do ponto 9: que responder a graves violações exige, sempre, investigação e sanção penal. Verdade, reparação e memória também são formas de reprovação.


 A objeção de Montevidéu A sentença fica; a execução cai
 A Sentencia 20/2013 não toca nenhuma razão da Corte. Derruba os arts. 2º e 3º da lei que cumpria a sentença, e mantém o art. 1º. É por isso que a supervisão de 2013 a chama de obstáculo, e não de afronta.



 



 06 O eixo da aula
 Pode uma decisão majoritária afastar direitos protegidos constitucional e internacionalmente?
 
 Eixo de discussão da aula Pode uma decisão majoritária afastar direitos protegidos constitucional e internacionalmente? Quais são os limites da soberania popular?
 O caso Gelman oferece três respostas para comparar. Para a Corte IDH (2011, unânime), não pode: a proteção dos direitos humanos é limite intransponível à regra da maioria, e o voto popular, por ser ato do Estado, gera responsabilidade como qualquer lei. Para a Suprema Corte uruguaia (2013, com o voto vencido de Pérez Manrique), a pergunta se desloca: mesmo quando o Estado decide cumprir a obrigação internacional, garantias constitucionais do acusado, como a irretroatividade penal, também limitam o que as maiorias podem fazer. Para Gargarella, a resposta depende do grau de legitimidade democrática da decisão e do tipo de resposta que ela dá aos crimes; tratar um plebiscito livre como uma autoanistia empobrece a própria ideia de democracia.
 Como montar a resposta
 Tese. Diga se a maioria pode, e com qual limite.
 Casos. Para cada um: tribunal, ano, o que decidiu, por quê. Gelman (§§ 229, 238–239, ponto 11); Sentencia 20/2013 (arts. 2º e 3º caem, art. 1º fica); supervisão de 2013 (considerandos 102–104).
 Divergência. Quem discordou e como: Pérez Manrique contra a maioria uruguaia; Gargarella contra a Corte IDH; Vio Grossi concorda, mas por um fundamento próprio.
 Posição. Separe o plano internacional (o dever do Estado) do doméstico (o dever de cada juiz) antes de concluir.
 Três situações para testar
 Se uma lei nova apenas reabre a pretensão punitiva e mexe em prazos para fatos passados, a objeção de legalidade da Sentencia 20/2013 está diretamente em jogo. Se a investigação apura um desaparecimento que continuou depois de o tipo penal entrar em vigor, a razão da Corte IDH sobre crime continuado precisa ser enfrentada. E se alguém disser que a Sentencia 20/2013 anulou Gelman, a resposta é não: são decisões de planos diferentes, e a sentença internacional continua vinculando o Uruguai.
 O caso inverso vem na Aula 06: na Bolívia, um tribunal usou a Convenção Americana para ampliar o que a maioria havia recusado no voto.



 07 Teste
 Responda antes de abrir.
 
 
 Por que a Lei de Caducidade não era uma “autoanistia”?
 Porque foi promulgada por um governo democrático em 1986 e depois mantida pelo voto popular duas vezes (referendo de 1989 e plebiscito de 2009). Não foi editada pelo regime em favor de si próprio.
 O que diz o § 229 de Gelman e por que ele importa?
 Que a incompatibilidade das anistias com a Convenção não depende do processo de adoção nem da autoridade que as editou, mas da ratio legis de deixar impunes graves violações. Por isso vale também para leis democráticas, e não só para autoanistias.
 Qual o fundamento da Sentencia 20/2013 para derrubar os arts. 2 e 3 da Lei 18.831?
 A irretroatividade da lei penal mais grave (arts. 10 e 72 da Constituição uruguaia): suspender retroativamente a prescrição e requalificar retroativamente os delitos como lesa-humanidade prejudicava os acusados.
 Qual o argumento do voto vencido de Pérez Manrique?
 Os tratados de direitos humanos integram o bloco de constitucionalidade e a imprescritibilidade dos crimes de lesa-humanidade já era jus cogens na época dos fatos; a lei apenas a reconheceu, então não haveria retroatividade.
 O que é a “gradação democrática” de Gargarella?
 A ideia de que anistias diferem em legitimidade democrática, conforme a inclusão e o debate que as cercaram: da autoanistia de Bignone à lei de Fujimori, às leis de perdão de Alfonsín e, no topo, à lei uruguaia confirmada por duas consultas populares. A Corte IDH deveria tê-las distinguido.
 Quem divergiu em Gelman vs. Uruguai?
 Ninguém: os pontos resolutivos foram votados por unanimidade. O juiz Vio Grossi juntou voto concorrente, não divergente, explicando por que um voto popular é ato do Estado.
 Por que um plebiscito pode gerar responsabilidade internacional do Estado?
 Porque o comportamento de qualquer órgão do Estado, em função legislativa ou de outra índole, é ato do Estado; o eleitorado que aprova ou ratifica uma lei exerce essa função (§ 238; voto de Vio Grossi). A legitimação democrática é limitada pelas obrigações de direitos humanos (§ 239).
 A Sentencia 20/2013 anulou Gelman? O que a Corte IDH disse dela?
 Não. Ela declarou inaplicáveis aos excepcionantes os arts. 2º e 3º da Lei 18.831. Na supervisão de 20/03/2013, a Corte IDH chamou a decisão de obstáculo ao pleno cumprimento, porque seu raciocínio podia ser reiterado em casos análogos, e reafirmou que a sentença vincula todos os órgãos uruguaios, inclusive os juízes (considerandos 102–104).
 Eixo: um país aprova em referendo uma lei que extingue a punibilidade de desaparecimentos forçados cometidos sob a ditadura. A maioria pode fazer isso?
 Pela Corte IDH, não: Gelman (2011) diz que a origem democrática não dá à lei legitimidade internacional (§ 238) e que os direitos humanos limitam as maiorias (§ 239); o efeito, não a origem, decide (§ 229). Divergências a registrar: Gargarella pediria distinguir o grau de legitimidade do referendo e discutir se a resposta tem de ser penal; e, se o Estado depois reabrir os casos, a Sentencia 20/2013 mostra que a irretroatividade penal limita como fazê-lo, enquanto a Corte IDH responde com o crime continuado.
