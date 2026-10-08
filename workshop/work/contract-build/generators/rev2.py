import re
OUT = "/Users/benecles/Documents/Codex/2026-09-05/okay-couple-things-so-first-of/work/study-lab-publish/courses/teoria-geral-dos-contratos/"
p1 = open(OUT + 'revisao-p1.html').read()
head = p1[:p1.index('<body>')]
head = head.replace('<title>Revisão para a P1 · Teoria Geral dos Contratos</title>', '<title>Revisão para a P2 · Teoria Geral dos Contratos</title>')
head = head.replace('content="Revisão de véspera da P1 de Teoria Geral dos Contratos: o essencial de cada unidade, com os artigos, e dez casos resolvidos."',
                    'content="Revisão da P2 de Teoria Geral dos Contratos: interpretação, revisão, cessão da posição contratual e extinção, com os artigos e doze casos resolvidos."')
head = head.replace('</style>', '.revisao .unit-map h3 span{display:block;font:500 10px var(--mono);letter-spacing:.1em;color:var(--dif);margin-bottom:4px}\n</style>')
assert 'P2' in head

hero = ('<svg class="hero-fork" viewBox="0 0 1080 170" aria-hidden="true">'
        '<g class="pop" style="--d:.2s"><rect x="30" y="62" width="250" height="46" style="fill:var(--ink)"/>'
        '<text x="155" y="91" text-anchor="middle" style="font:12px var(--mono);letter-spacing:1px;fill:var(--paper)">O CONTRATO TEM UM PROBLEMA</text></g>')
BR = [('QUAL O SENTIDO?', 'INTERPRETAÇÃO · 09–10', 'dif', 20), ('ESTÁ EQUILIBRADO?', 'REVISÃO · 11–13', 'conc', 62), ('QUEM É A PARTE?', 'CESSÃO · 14', 'dif', 104), ('COMO TERMINA?', 'EXTINÇÃO · 15–17', 'conc', 146)]
for i, (q, u, tone, y) in enumerate(BR):
    hero += (f'<path class="draw" style="--d:{.5+.15*i}s;stroke:var(--{tone});stroke-width:2;fill:none" d="M280 85C420 85 430 {y} 560 {y}"/>'
             f'<g class="pop" style="--d:{1+.15*i}s;font:12px var(--mono);letter-spacing:1px"><circle cx="566" cy="{y}" r="6" style="fill:var(--{tone})"/>'
             f'<text x="584" y="{y+4}" style="fill:var(--ink)">{q}</text><text x="1050" y="{y+4}" text-anchor="end" style="fill:var(--{tone})">{u}</text></g>')
hero += '</svg>'

def art(unit, title, items):
    return f'    <article><h3><span>{unit}</span>{title}</h3><ul>\n' + ''.join(f'      <li>{x}</li>\n' for x in items) + '    </ul></article>\n'
units = ''.join([
    art('Unidade 6 · Aula 09', 'Interpretação: a regra geral', [
        'CC <strong>112</strong>: atende-se mais à intenção <em>consubstanciada na declaração</em> do que ao sentido literal. Não é licença para buscar vontade secreta.',
        'Leia a cláusula com o <strong>contrato inteiro</strong> e as circunstâncias. Um rótulo errado (“avalista”) não vence o resto do instrumento (REsp 1.013.976/SP).',
        'CC <strong>113</strong>: boa-fé e usos do lugar da celebração. § 1º, cinco referências conjuntas, sem hierarquia: <strong>conduta posterior</strong>, <strong>usos do mercado</strong>, <strong>boa-fé</strong>, <strong>quem não redigiu</strong> (se identificável), <strong>negociação razoável</strong>.',
        '§ 2º: as partes podem pactuar regras próprias de interpretação, preenchimento de lacunas e integração.',
    ]),
    art('Unidade 6 · Aula 10', 'Interpretação: regras especiais', [
        'CC <strong>114</strong>: negócios benéficos e renúncia se interpretam <strong>estritamente</strong>. Doação “pura e simples” não ganha encargo por dedução (REsp 1.938.997/MS).',
        'CC <strong>423</strong>: na adesão, cláusula ambígua ou contraditória a favor do <strong>aderente</strong>. CDC <strong>47</strong>: no consumo, todas as cláusulas a favor do <strong>consumidor</strong>.',
        '<strong>Interpretar</strong> revela o que foi combinado e não escrito; <strong>integrar</strong> completa, com a lei supletiva, o que ninguém combinou.',
        'AR 7.296/DF: limite da <strong>rescisória</strong> (CPC 966, V), não regra de que o texto literal sempre vence.',
    ]),
    art('Unidade 7 · Aula 11', 'Revisão: defeito na origem', [
        'Primeiro a <strong>data</strong>: o problema estava na assinatura ou surgiu depois?',
        '<strong>Cláusula abusiva</strong>: ataca uma regra do contrato no seu contexto. No consumo, nula de pleno direito (CDC <strong>51</strong>); fora dele, retirada e integração pela boa-fé é construção doutrinária.',
        '<strong>Lesão</strong> (CC <strong>157</strong>): premente necessidade <em>ou</em> inexperiência + prestação manifestamente desproporcional, medida pelos valores da <strong>celebração</strong> (§ 1º). Anulável; evita-se a anulação com suplemento suficiente ou redução do proveito (§ 2º).',
        'Caso da artista (TJDFT): 35 shows e multa de 138 SM contra a transferência de um domínio de site; distrato anulado.',
    ]),
    art('Unidade 7 · Aula 12', 'Revisão: fato superveniente', [
        'Comece pela <strong>álea</strong>: o que o contrato já distribuiu (preço fixo, índice, risco cambial) fica onde foi posto.',
        'CC <strong>317</strong>: motivo imprevisível + desproporção manifesta entre o valor devido e o da execução → o juiz <strong>corrige o valor</strong>, a pedido da parte.',
        'CC <strong>478</strong>: execução continuada ou diferida + onerosidade excessiva + <strong>extrema vantagem</strong> + fato <strong>extraordinário e imprevisível</strong> → o devedor pede <strong>resolução</strong>; sentença retroage à citação. <strong>479</strong>: o réu evita oferecendo modificação equitativa. <strong>480</strong>: obrigações de uma só parte, redução ou outro modo de executar.',
        'CDC <strong>6º, V</strong>: revisão por fato superveniente que torna a prestação excessivamente onerosa, <strong>sem</strong> exigir imprevisibilidade nem extrema vantagem.',
        'Revisão pedida diretamente pelo devedor pelo 478: <strong>doutrina diverge</strong> (leituras restritiva, integrativa e intermediária).',
    ]),
    art('Unidade 7 · Aula 13', 'Revisão: base do negócio', [
        'Quebra da base: uma <strong>premissa comum e determinante</strong> desaparece, sem que a prestação fique impossível.',
        'Prove os elos: qual premissa, que era <strong>comum</strong>, que era <strong>determinante</strong>, que o fato posterior a <strong>atingiu</strong>. Motivo unilateral não comunicado não serve.',
        'Não há artigo geral no Código Civil com remédio próprio para a base; é preciso justificar a causa jurídica e a resposta.',
        'Cláusulas de adaptação: <strong>indexação</strong> muda o preço sozinha; <strong>renegociação</strong> só obriga a negociar.',
    ]),
    art('Unidade 8 · Aula 14', 'Cessão da posição contratual', [
        'Três pessoas: <strong>cedente</strong> (sai), <strong>cessionário</strong> (entra), <strong>cedido</strong> (fica e consente).',
        'Transfere-se a <strong>posição inteira</strong>: direitos, deveres, poderes e encargos. Não confundir com <strong>cessão de crédito</strong> (286–298; notificar o devedor, <strong>290</strong>) nem com <strong>assunção de dívida</strong> (299–303; consentimento expresso do credor, silêncio após prazo é recusa, <strong>299</strong>).',
        'Sem artigo geral no Código; o STJ exige a <strong>anuência do cedido</strong>. Silêncio não vale, em regra, como consentimento.',
        'Substituir ≠ <strong>liberar</strong> o cedente: o cedido pode exigir responsabilidade subsidiária. O alcance sobre o passado depende do instrumento (REsp 356.383/SP).',
    ]),
    art('Unidade 9 · Aulas 15 e 16', 'Extinção: impossibilidade e vontade', [
        'O <strong>cumprimento</strong> extingue a obrigação satisfeita; no contrato continuado, cada pagamento extingue aquela parcela.',
        'Impossibilidade superveniente atinge <strong>uma prestação</strong>: coisa certa perdida sem culpa antes da tradição, obrigação resolvida para ambos (<strong>234</strong>); gênero não perece (<strong>246</strong>); devedor em mora responde até pelo fortuito (<strong>399</strong>). Falta de caixa não é impossibilidade.',
        '<strong>Distrato</strong>: novo acordo, mesma forma do contrato (<strong>472</strong>). Quem impediu a assinatura não se vale da falta de forma (REsp 1.040.606/ES).',
        '<strong>Denúncia</strong> (<strong>473</strong>): saída unilateral só onde a lei (ou o contrato) permite, notificada. Investimentos consideráveis → efeito só após <strong>prazo compatível</strong> (parágrafo único). Caso AMBEV: maioria aplicou a cláusula de 60 dias; voto vencido falou em confiança.',
    ]),
    art('Unidade 9 · Aula 17', 'Extinção: inadimplemento', [
        '<strong>Mora</strong>: atraso imputável, prestação ainda possível e útil (394–396). <strong>Definitivo</strong>: a prestação ficou inútil; o credor pode enjeitá-la e pedir perdas e danos (<strong>395, p. ú.</strong>).',
        '<strong>474</strong>: cláusula resolutiva <strong>expressa</strong> opera de pleno direito (sem sentença prévia, mas com a escolha comunicada); a <strong>tácita</strong> depende de interpelação judicial.',
        '<strong>475</strong>: o lesado escolhe <strong>resolver</strong> ou <strong>exigir o cumprimento</strong>, com perdas e danos em qualquer caso.',
        'Efeitos: restituição recíproca onde for possível; o já usado em prestações contínuas não volta. Contratos personalíssimos acabam com a morte de quem devia prestar.',
    ]),
])

def case(tag, title, problem, answer, trap):
    return (f'    <details>\n      <summary><span class="tag">{tag}</span><br>{title}</summary>\n      <p class="problem">{problem}</p>\n'
            f'      <div class="solution"><h3>Resposta</h3>{"".join(f"<p>{a}</p>" for a in answer)}<p><strong>Armadilha:</strong> {trap}</p></div>\n    </details>\n')
cases = ''.join([
    case('Interpretação', 'O sócio “avalista” do mútuo',
         'Num contrato de mútuo bancário, um sócio assina como “avalista-interveniente”. Outra cláusula o descreve como coobrigado pelo pagamento. Executado, ele alega que aval só existe em título de crédito e que, portanto, não responde.',
         ['Ele responde. Lido como um todo (arts. 112 e 113), o contrato mostra que ele assumiu a obrigação; o rótulo impreciso não apaga a cláusula de coobrigação. Foi o que o STJ fez no REsp 1.013.976/SP.'],
         'transformar o caso em regra de que “todo sócio responde pela dívida da empresa”. O tribunal interpretou aquele instrumento, que ele assinou.'),
    case('Interpretação', 'A doação com finalidade num papel antigo',
         'Uma empresa doa um terreno. Um instrumento particular anterior falava em construir ali um centro cultural; a escritura pública diz “doação pura e simples”, e um aditivo afasta encargo. O centro não sai, e a doadora pede a revogação por descumprimento de encargo.',
         ['Improcedente. A doação é negócio benéfico e se interpreta estritamente (art. 114): não se deduz um encargo que a escritura não impôs. Os arts. 112 e 113 apontam no mesmo sentido (REsp 1.938.997/MS).'],
         'usar a boa-fé ou a “finalidade” para criar, por interpretação, uma obrigação que o doador não assumiu.'),
    case('Interpretação', 'Dois prazos no mesmo formulário',
         'Uma distribuidora assina o formulário padrão de uma fabricante. Uma cláusula dá 30 dias para reclamar de defeitos; outra, 60. A distribuidora reclamou no 45º dia. As duas são empresas, e a distribuidora revende os produtos.',
         ['Vale o prazo de 60 dias. É contrato de adesão com cláusulas contraditórias, e o art. 423 manda interpretar a favor do aderente. O art. 113, § 1º, IV, reforça: a fabricante redigiu.'],
         'fundamentar no art. 47 do CDC. A distribuidora revende, e o enunciado não indica vulnerabilidade: a relação, em princípio, não é de consumo. Adesão e consumo são perguntas separadas.'),
    case('Revisão', 'O carro herdado vendido às pressas',
         'Um estudante de 19 anos herda um carro. Pressionado por uma dívida que vencia no dia seguinte, vende-o a um conhecido por 30% do preço de tabela da época. Dois anos depois, quer desfazer a venda.',
         ['Há sinais de lesão (art. 157): premente necessidade, talvez inexperiência, e prestação manifestamente desproporcional medida pelos valores da celebração (§ 1º). O negócio é anulável, dentro do prazo decadencial de quatro anos contado da celebração (art. 178, II).',
          'O comprador pode evitar a anulação oferecendo suplemento suficiente, ou concordando em reduzir o proveito (§ 2º).'],
         'medir a desproporção pelo preço de hoje, ou tratar o caso como onerosidade excessiva: o problema estava na assinatura.'),
    case('Revisão', 'O insumo que subiu dentro do normal',
         'Um restaurante corporativo se obrigou a fornecer refeições por preço fixo durante um ano. No sexto mês, o preço do principal insumo sobe 15%, dentro da variação histórica do setor. O restaurante pede a resolução pelo art. 478.',
         ['Não cabe. A variação está dentro da álea normal do contrato, e o preço fixo alocou esse risco ao restaurante. Falta o fato extraordinário e imprevisível; faltaria, provavelmente, também a extrema vantagem da outra parte.'],
         'tratar a queda de margem como prova dos requisitos. Dificuldade financeira não demonstra nenhum deles.'),
    case('Revisão', 'A prestação do consumidor que disparou',
         'Um consumidor tem um financiamento com parcelas atreladas a um indexador. Um fato posterior faz a parcela disparar a ponto de se tornar excessivamente onerosa. O banco responde que o fato não era imprevisível nem extraordinário.',
         ['O argumento do banco não encerra a questão. No consumo, o art. 6º, V, do CDC admite revisão por fato superveniente que torne a prestação excessivamente onerosa, sem exigir imprevisibilidade, extraordinariedade ou extrema vantagem.',
          'O consumidor ainda precisa provar a relação de consumo, o fato posterior e a onerosidade excessiva.'],
         'aplicar ao consumidor os requisitos do art. 478 do Código Civil.'),
    case('Revisão', 'O festival cancelado',
         'Um espaço é locado por cinco dias. O contrato descreve o festival que seria realizado, com as datas, e a negociação girou em torno dele. Uma proibição pública cancela o festival. O espaço continua disponível, e o locador cobra o aluguel inteiro.',
         ['Há base para discutir a <strong>quebra da base do negócio</strong>: a premissa era comum (está no contrato), determinante e foi atingida pela proibição. A resposta ainda precisa de causa jurídica e remédio justificados; não é automática.',
          'Se o festival fosse só um plano do locatário, nunca comunicado, seria motivo unilateral, e o argumento cairia.'],
         'confundir com impossibilidade (o espaço existe e pode ser usado) ou tratar qualquer frustração de expectativa como quebra da base.'),
    case('Cessão', 'O locador que não respondeu',
         'Ana, locatária comercial, e Bruno assinam a cessão da posição de Ana no contrato. Avisam o locador, Caio, por e-mail. Caio não responde. Três meses depois, o aluguel atrasa, e Caio cobra Ana.',
         ['Caio pode cobrar Ana. A cessão da posição exige o consentimento do cedido, e o silêncio, em regra, não vale como consentimento. Sem anuência, Ana continua locatária.',
          'Mesmo que Caio tivesse aceitado Bruno, seria preciso ver se liberou Ana ou manteve sua responsabilidade.'],
         'aplicar a regra da cessão de crédito (basta notificar, art. 290). Ali só se transfere um crédito; aqui, a posição inteira.'),
    case('Extinção', 'Shopping fechado, aluguel cobrado',
         'Por ordem pública, um shopping fica fechado por 40 dias. Um lojista pede que o contrato seja declarado extinto por impossibilidade e se recusa a pagar qualquer aluguel dali em diante.',
         ['O pedido vai longe demais. O fechamento pode tornar temporariamente impossível parte da prestação do shopping (acesso, funcionamento), e isso repercute nas parcelas daquele período. Pagar dinheiro, porém, continua possível.',
          'A queda de faturamento pode sustentar outra discussão, sobre onerosidade (arts. 317 e 478), com os requisitos próprios. Nada disso extingue automaticamente o contrato inteiro.'],
         'chamar de impossibilidade a falta de caixa, ou tratar um impedimento temporário e parcial como fim do contrato.'),
    case('Extinção', 'O distrato que a locadora não assinou',
         'Locadora e locatária combinam o fim da locação e a devolução de parte dos valores pagos. A minuta é preparada, mas a locadora se recusa a assiná-la e passa a sustentar que o contrato continua, porque o distrato exigiria forma escrita.',
         ['A locadora não pode se valer disso. Provado o acordo, quem frustrou a assinatura não pode usar a falta do documento para negar o distrato e fugir da devolução (REsp 1.040.606/ES).'],
         'concluir que o art. 472 deixou de valer. O resultado depende da prova do acordo e da conduta contraditória.'),
    case('Extinção', 'A distribuidora que acabou de investir',
         'Um contrato de distribuição por prazo indeterminado admite denúncia com 30 dias de aviso. A distribuidora acabou de fazer investimentos consideráveis, exigidos pela fornecedora, para atender a uma nova linha. Um mês depois, recebe a denúncia.',
         ['A denúncia é possível (art. 473), mas o parágrafo único adia o seu efeito: com investimentos consideráveis feitos por causa da natureza do contrato, ela só produz efeito depois de prazo compatível com a natureza e o vulto desses investimentos.'],
         'citar o caso AMBEV como regra de que “o aviso contratual sempre basta”. Aquela decisão é anterior ao Código de 2002 e aplicou a cláusula daquele contrato.'),
    case('Extinção', 'Os convites que chegaram depois da festa',
         'Uma gráfica deveria entregar convites de casamento 30 dias antes da festa. Entrega dois dias depois do casamento. O contrato não tem cláusula resolutiva.',
         ['É inadimplemento definitivo: a prestação ficou inútil para o credor (art. 395, parágrafo único). Sem cláusula expressa, a resolução depende de interpelação judicial (art. 474). O casal pode resolver ou, se quisesse, exigir o cumprimento, com perdas e danos em qualquer caso (art. 475).'],
         'tratar como simples mora. Se a entrega atrasasse dois dias mas ainda antes da festa, aí sim seria mora, e caberia exigir a entrega e os danos do atraso.'),
])

body = f'''<body>
<nav class="topbar"><a href="index.html">← Teoria Geral dos Contratos</a><span>Revisão · P2</span><button class="theme-toggle" type="button" aria-pressed="false" title="Alternar modo noite"><span class="tt-track" aria-hidden="true"><span class="tt-knob"></span></span><span class="tt-label">Modo noite</span></button></nav>
<header class="hero">
  <div class="kicker label"><span>Unidades 6 a 9</span><span>Da interpretação à extinção</span><span>Prova em 27.11</span></div>
  <h1><span class="split">Revisão</span><span class="split">para a P2</span></h1>
  <p class="deck">Diante de um problema, a primeira pergunta decide a unidade: é de <strong class="dif">sentido</strong>, de <strong class="conc">equilíbrio</strong>, de <strong class="dif">quem é parte</strong> ou de <strong class="conc">como termina</strong>? Depois vêm os artigos e doze casos para resolver.</p>
  {hero}
  <div class="titleblock label" role="list">
    <div role="listitem">Parte 1<b>O que saber</b></div>
    <div role="listitem">Parte 2<b>Doze casos</b></div>
    <div role="listitem">Parte 3<b>Como responder</b></div>
  </div>
</header>

<section class="chapter" aria-labelledby="saber">
  <span class="num" aria-hidden="true">01</span>
  <h2 id="saber">O que saber, unidade por unidade</h2>
  <p class="lede">Cada bloco traz os conceitos e artigos que a prova cobra, na ordem das aulas.</p>
</section>
<div class="revisao">
  <div class="unit-map">
{units}  </div>
</div>

<section class="chapter" aria-labelledby="casos">
  <span class="num" aria-hidden="true">02</span>
  <h2 id="casos">Doze casos</h2>
  <p class="lede">Resolva antes de abrir. Cada resposta traz o raciocínio e a armadilha mais comum.</p>
</section>
<div class="revisao">
  <div class="quiz">
{cases}  </div>
</div>

<section class="chapter" aria-labelledby="responder">
  <span class="num" aria-hidden="true">03</span>
  <h2 id="responder">Como responder</h2>
</section>
<div class="revisao">
  <p class="exam-note">Comece pela pergunta certa: sentido, equilíbrio, parte ou fim. Na revisão, date o problema (assinatura ou execução) e leia a alocação de riscos antes da lei. Na cessão, diga o que exatamente foi transferido e quem consentiu. Na extinção, identifique o evento, a prestação atingida e o efeito no tempo. Cite a regra, aponte o fato que a aciona e pare no efeito que ela produz.</p>
  <nav class="lesson-links" aria-label="Aulas da P2">
    <a href="aula-09.html">09 · Sentido do acordo</a><a href="aula-10.html">10 · Regras especiais</a><a href="aula-11.html">11 · Desequilíbrio na origem</a><a href="aula-12.html">12 · Fato superveniente</a><a href="aula-13.html">13 · Base do negócio</a><a href="aula-14.html">14 · Cessão</a><a href="aula-15.html">15 · Impossibilidade</a><a href="aula-16.html">16 · Saída por vontade</a><a href="aula-17.html">17 · Inadimplemento</a>
  </nav>
  <p style="margin:14px 0 0;font-size:15px"><a href="artigos.html">Índice de artigos do curso →</a></p>
</div>
<footer class="endnav"><a href="index.html"><span>Curso</span>Voltar ao índice</a><a href="aula-09.html"><span>Começar pelas aulas</span>Aula 09 · Interpretação</a></footer>
<script src="assets/curso.js?v=20260925d"></script>
</body>
</html>
'''
open(OUT + 'revisao-p2.html', 'w').write(head + body)
print('ok', len(head + body))
