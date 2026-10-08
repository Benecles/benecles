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
- line 76 `negative-parallelism`: “não é”
- line 116 `negative-parallelism`: “não é”
- line 139 `negative-parallelism`: “não é”
- line 11 `colon-reveal`: “Todo contrato tem dois lados: uma operação econômica , que faz a riqueza circular, e uma forma jurídica , que torna essa operação obrigatória.”
- line 25 `colon-reveal`: “A qualificação depende dos fatos da operação: uma empresa pode ser consumidora em uma relação e não em outra, e a doação aceita também é contrato.”
- line 37 `colon-reveal`: “Fato da natureza, que produz efeitos jurídicos sem depender de ação humana: o nascimento, a morte, o decurso do tempo.”
- line 42 `colon-reveal`: “Exemplos: a caça, a tomada de posse.”
- line 61 `colon-reveal`: “O mesmo contrato pode ser lido de três jeitos: como acordo de vontades, como operação econômica e como relação que o Direito reconhece.”
- line 69 `colon-reveal`: “Estruturalmente, o contrato é um acordo: duas declarações unilaterais, a proposta e a aceitação, que se encontram.”
- line 74 `colon-reveal`: “Por trás do acordo há uma operação que faz a riqueza circular: bens, serviços, crédito, uso de coisas, riscos.”
- line 82 `colon-reveal`: “O italiano define: é o acordo entre duas ou mais partes para constituir, regular ou extinguir entre elas uma relação jurídica patrimonial (art.”
- line 102 `colon-reveal`: “O poder público também, quando atua como agente econômico: deve serviços adequados, eficientes, seguros e, se essenciais, contínuos (art.”
- line 123 `colon-reveal`: “A razão do cuidado: se todos fossem consumidores, ninguém teria tratamento diferenciado, e a proteção especial do CDC viraria direito comum.”
- line 128 `colon-reveal`: “O STJ aplicou o CDC: o avião atendia a uma necessidade própria e não fazia parte do serviço que a empresa vendia.”
- line 129 `colon-reveal`: “O STJ afastou o CDC: o serviço integrava a atividade, e não houve prova de vulnerabilidade.”
- line 138 `colon-reveal`: “6º: informação clara, proteção contra práticas e cláusulas abusivas, revisão de prestações desproporcionais ou excessivamente onerosas.”
- line 148 `colon-reveal`: “A máquina entra diretamente na produção: é consumo intermediário.”
- line 152 `colon-reveal`: “Ato jurídico em sentido estrito: há vontade de mudar de endereço, mas os efeitos jurídicos vêm prontos da lei.”
- line 21 `triad-density`: “O percurso parte do conceito e dos princípios, acompanha a formação e a classificação e chega à interpretação e ao fim do vínculo”
- line 22 `triad-density`: “O contrato reúne declarações de vontade, organiza uma operação econômica e cria um vínculo sujeito a regras jurídicas”
- line 23 `triad-density`: “O estudo começa pelo conceito, pelos princípios e pelas perguntas que definem uma relação de consumo”
- line 23 `triad-density`: “riscos, garantias e modos de execução”
- line 24 `triad-density`: “das mudanças no equilíbrio, da circulação da posição contratual e das formas de extinção”
- line 25 `triad-density`: “os riscos distribuídos, as obrigações assumidas e o regime jurídico aplicável”
- line 61 `triad-density`: “pode ser lido de três jeitos: como acordo de vontades, como operação econômica e como relação que o Direito reconhece”
- line 69 `triad-density`: “o contrato é um acordo: duas declarações unilaterais, a proposta e a aceitação, que se encontram”
- line 81 `triad-density`: “e é o ordenamento que diz como interpretá-la, executá-la e limitá-la”
- line 91 `triad-density`: “O CDC se aplica conforme quem contrata, o que é fornecido e para onde vai o produto ou serviço”
- line 104 `triad-density`: “é atividade fornecida no mercado mediante remuneração, inclusive bancária e securitária”
- line 122 `triad-density`: “Para os finalistas, só quem retira o bem do mercado de fato e economicamente”
- line 138 `triad-density`: “4º, I) e se apoia em transparência, boa-fé, equilíbrio e confiança”
- line 138 `triad-density`: “6º: informação clara, proteção contra práticas e cláusulas abusivas, revisão de prestações desproporcionais o”
- line 156 `triad-density`: “consumo depende dos sujeitos, do objeto e da destinação”

---
# Frozen draft: aula-01.html

Unidade 1 · Conceito Teoria Geral dos Contratos UFRGS · 2026/2 

 Conceito de contrato 

 Todo contrato tem dois lados: uma operação econômica , que faz a riqueza circular, e uma forma jurídica , que torna essa operação obrigatória.

 
 Unidade 1 · Conceito 
 Leitura ≈ 15 min 
 Depois Aula 02 · Princípios I 


 
 00 O curso
 O percurso parte do conceito e dos princípios, acompanha a formação e a classificação e chega à interpretação e ao fim do vínculo.
 Comprar uma bicicleta, contratar um serviço ou aceitar uma doação são situações distintas que podem envolver um acordo reconhecido pelo Direito. O contrato reúne declarações de vontade, organiza uma operação econômica e cria um vínculo sujeito a regras jurídicas.
 O estudo começa pelo conceito, pelos princípios e pelas perguntas que definem uma relação de consumo. Seguem as tratativas e a formação do vínculo; depois, as classificações ajudam a identificar obrigações, riscos, garantias e modos de execução.
 Na sequência, o curso trata da interpretação, das mudanças no equilíbrio, da circulação da posição contratual e das formas de extinção. Esses temas acompanham o vínculo desde as negociações até seu encerramento.
 A análise de cada caso considera quem declarou o quê, a finalidade econômica do acordo, os riscos distribuídos, as obrigações assumidas e o regime jurídico aplicável. A qualificação depende dos fatos da operação: uma empresa pode ser consumidora em uma relação e não em outra, e a doação aceita também é contrato.

 
 01 Onde o contrato se encaixa
 Os fatos jurídicos vão do que acontece sem ninguém querer até aquilo que as pessoas regulam por vontade própria. O contrato está no último degrau.
 
 
 Fig. 1 · Os fatos jurídicos 1 / 4 
 

 
 Degrau 1 Fato jurídico em sentido estrito
 Fato da natureza, que produz efeitos jurídicos sem depender de ação humana: o nascimento, a morte, o decurso do tempo.



 Degrau 2 Ato-fato
 Exige uma ação humana, mas a vontade não importa para o Direito, só o resultado. Exemplos: a caça, a tomada de posse.



 Degrau 3 Ato jurídico em sentido estrito
 Há ação voluntária e consciente, mas os efeitos já vêm prontos da lei. Quem fixa domicílio quer mudar de endereço; as consequências jurídicas, a lei é que define.



 Degrau 4 Negócio jurídico
 A vontade escolhe o conteúdo e os efeitos da relação, dentro dos limites que a lei deixa. O contrato é a principal espécie de negócio jurídico. Por isso as regras gerais do direito contratual estão, em boa parte, na Parte Geral do Código Civil.



 



 02 Os três elementos do contrato
 O mesmo contrato pode ser lido de três jeitos: como acordo de vontades, como operação econômica e como relação que o Direito reconhece.
 
 
 Fig. 2 · Três leituras do contrato 1 / 3 
 

 
 Elemento estrutural O acordo de vontades
 Estruturalmente, o contrato é um acordo: duas declarações unilaterais, a proposta e a aceitação, que se encontram. É o que faz dele um negócio jurídico bilateral quanto à formação, mesmo quando só uma parte se obriga.



 Elemento substancial A operação econômica
 Na linguagem comum, contrato é “o negócio”. Por trás do acordo há uma operação que faz a riqueza circular: bens, serviços, crédito, uso de coisas, riscos. Por isso a função do contrato é a circulação de riqueza.
 Como diz Orlando Gomes, ninguém sobrevive no meio social sem praticar diariamente uma série de contratos.
 Operação econômica não é especulação. Comprar algo para uso próprio, fazer seguro de um bem ou contratar um serviço para tocar uma atividade são operações econômicas, mesmo sem nenhuma aposta ou busca de lucro. Há contratos especulativos, como os derivativos, mas eles são uma parte pequena do todo.



 Elemento normativo O contrato no Direito
 A palavra “contrato” serve tanto para a operação quanto para sua roupagem jurídica. É a forma jurídica que dá força obrigatória à operação, e é o ordenamento que diz como interpretá-la, executá-la e limitá-la.
 O Código Civil brasileiro não define contrato. O italiano define: é o acordo entre duas ou mais partes para constituir, regular ou extinguir entre elas uma relação jurídica patrimonial (art. 1.321). Onde não há norma cogente, as partes decidem como compor seus interesses (Enzo Roppo). Mas o art. 421 submete a liberdade à função social, e o art. 421-A presume paritários os contratos civis e empresariais, ressalvados os regimes especiais, como o do consumidor.



 



 03 Quando se aplica o CDC
 Nem todo contrato é de consumo. O CDC se aplica conforme quem contrata, o que é fornecido e para onde vai o produto ou serviço.
 
 
 Elemento
 Quem é
 Detalhe
 Consumidor
 Pessoa física ou jurídica que adquire ou utiliza produto ou serviço como destinatária final (CDC, art. 2º).
 Equipara-se a consumidor a coletividade que intervém na relação de consumo (art. 2º, parágrafo único).
 Fornecedor
 Pessoa física ou jurídica, pública ou privada, nacional ou estrangeira, ou ente despersonalizado, que atua no mercado produzindo, distribuindo ou comercializando produtos ou prestando serviços (art. 3º).
 O poder público também, quando atua como agente econômico: deve serviços adequados, eficientes, seguros e, se essenciais, contínuos (art. 22).
 Objeto
 Produto é qualquer bem, material ou imaterial. Serviço é atividade fornecida no mercado mediante remuneração, inclusive bancária e securitária.
 Ficam de fora as relações de caráter trabalhista.
 



 
 Fig. 3 · Destinação final 1 / 3 
 

 
 A questão O bem termina no uso ou volta para o mercado?
 O que decide é o que o adquirente faz com o bem ou serviço. Se atende a uma necessidade própria e não é revendido nem usado para produzir o que ele oferece a terceiros, ele é destinatário final , e há relação de consumo.
 Se o bem entra na atividade como insumo, ferramenta, peça ou mercadoria para revenda, o consumo é intermediário . Conta a função econômica real, e não o fato de o bem se desgastar com o uso.



 Pessoa jurídica consumidora Três correntes
 O art. 2º menciona a pessoa jurídica, mas quando ela é destinatária final? Para os finalistas, só quem retira o bem do mercado de fato e economicamente. Para os maximalistas, basta ser destinatário de fato. O finalismo aprofundado , adotado pelo STJ, parte do critério finalista mas o flexibiliza quando a empresa prova vulnerabilidade técnica, jurídica, fática ou econômica diante do fornecedor.
 A razão do cuidado: se todos fossem consumidores, ninguém teria tratamento diferenciado, e a proteção especial do CDC viraria direito comum.



 Na jurisprudência Mesmo critério, resultados opostos
 Uma administradora de imóveis comprou uma aeronave. O STJ aplicou o CDC: o avião atendia a uma necessidade própria e não fazia parte do serviço que a empresa vendia.
 Já uma vendedora de ingressos contratou intermediação de pagamentos para operar o negócio. O STJ afastou o CDC: o serviço integrava a atividade, e não houve prova de vulnerabilidade.



 



 
 Vulnerabilidade O CDC existe porque reconhece a vulnerabilidade do consumidor no mercado (art. 4º, I) e se apoia em transparência, boa-fé, equilíbrio e confiança. Daí os direitos básicos do art. 6º: informação clara, proteção contra práticas e cláusulas abusivas, revisão de prestações desproporcionais ou excessivamente onerosas.
 Adesão ≠ consumo Contrato de adesão não é o mesmo que contrato de consumo. Há adesão fora do CDC e relação de consumo em contrato negociado. O Código Civil tem regras próprias para a adesão (arts. 423 e 424).




 04 Teste
 
 
 Uma empresa compra uma máquina para a linha de produção. É destinatária final?
 Em regra, não. A máquina entra diretamente na produção: é consumo intermediário. Só mudaria se a empresa provasse vulnerabilidade diante do fornecedor (finalismo aprofundado).
 Uma empresa contrata seguro para o próprio imóvel. Pode ser relação de consumo?
 Sim. O seguro protege patrimônio próprio e não integra o que a empresa oferece ao mercado.
 Em que degrau está a fixação de domicílio, e por quê?
 Ato jurídico em sentido estrito: há vontade de mudar de endereço, mas os efeitos jurídicos vêm prontos da lei.
 Qual é a diferença entre o elemento estrutural e o substancial do contrato?
 O estrutural é o acordo de vontades (proposta + aceitação); o substancial é a operação econômica que esse acordo realiza, a circulação de riqueza.
 Contrato de adesão é sempre contrato de consumo?
 Não. Adesão é um modo de contratar; consumo depende dos sujeitos, do objeto e da destinação.
