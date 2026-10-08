from kit import *

hero = ('<path class="draw" d="M540 150V40M380 60H700" style="stroke:var(--ink);stroke-width:3;fill:none"/>'
        '<path d="M520 150h40" style="stroke:var(--ink);stroke-width:5"/>'
        '<g class="pop" style="--d:.8s"><path d="M380 60L340 120H420Z" style="fill:var(--conc-wash);stroke:var(--conc);stroke-width:2"/>'
        '<path d="M700 60L660 120H740Z" style="fill:var(--dif-wash);stroke:var(--dif);stroke-width:2"/>'
        '<text x="380" y="140" text-anchor="middle" style="font:12px var(--mono);fill:var(--conc)">DAR</text>'
        '<text x="700" y="140" text-anchor="middle" style="font:12px var(--mono);fill:var(--dif)">RECEBER</text></g>'
        '<g class="pop" style="--d:1.4s;font:12px var(--mono);letter-spacing:1px"><text x="0" y="60" style="fill:var(--ink)">FUNÇÃO SOCIAL</text>'
        '<text x="0" y="84" style="fill:var(--ink)">BOA-FÉ OBJETIVA</text><text x="0" y="108" style="fill:var(--ink)">EQUILÍBRIO ECONÔMICO</text>'
        '<text x="1070" y="96" text-anchor="end" style="fill:var(--muted)">A TROCA DEVE SER ÚTIL E LEAL</text></g>')

# ---- função social ----
fs1 = (C(300, 290, 230, 'w-conc ink', style='stroke-dasharray:8 6')
       + T(300, 100, 'INTERESSES METAINDIVIDUAIS', 't-small tc-conc', anchor='middle')
       + T(300, 118, 'DIGNIDADE DA PESSOA', 't-small tc-conc', anchor='middle')
       + G(C(300, 300, 120, 'w-dif ink') + T(300, 296, 'AUTONOMIA', 't-mid tc-dif', anchor='middle') + T(300, 322, 'CONTRATUAL', 't-small tc-dif', anchor='middle'), 'pop', d=.2)
       + P('M300 140V170', 'c-conc grow', m='p-fs1-c') + P('M300 470V430', 'c-conc grow', m='p-fs1-c')
       + P('M110 300H170', 'c-conc grow', m='p-fs1-c') + P('M490 300H430', 'c-conc grow', m='p-fs1-c')
       + G(R(150, 540, 300, 44, 'f-ink') + T(300, 568, 'ENUNCIADO 23 · ATENUA, NÃO ELIMINA', 't-small t-light', anchor='middle'), 'pop', d=.9))
fs2 = (doc(210, 110, 180, 220, None, lines=9)
       + G(P('M300 370L380 400V470C380 520 300 550 300 550C300 550 220 520 220 470V400Z', 'w-dif ink', extra=' stroke-width="2"') + T(300, 470, 'CONSERVAÇÃO', 't-small tc-dif', anchor='middle'), 'pop', d=.3)
       + G(T(300, 80, 'ENUNCIADO 22', 't-small', anchor='middle', style='letter-spacing:.14em'), 'fade')
       + T(80, 440, 'trocas', 't-hand') + T(80, 468, 'úteis', 't-hand') + T(470, 440, 'e', 't-hand') + T(470, 468, 'justas', 't-hand'))
fs3 = (T(40, 64, 'LEI DE LOCAÇÕES · ART. 4º', 't-small', style='letter-spacing:.1em')
       + P('M60 170H540', 'ink', style='stroke-width:3') + T(60, 150, 'INÍCIO', 't-small') + T(540, 150, 'FIM DO PRAZO', 't-small', anchor='end')
       + G(box(40, 200, 250, 110, 'LOCADOR', 'não pode retomar', 'conc', ctx='fs3', sub2='durante o prazo'), 'pop', d=.2)
       + G(box(310, 200, 250, 110, 'LOCATÁRIO', 'pode devolver', 'dif', ctx='fs3', sub2='pagando multa proporcional'), 'pop', d=.5)
       + G(box(310, 340, 250, 110, 'TRANSFERIDO', 'pelo empregador', 'ink', ctx='fs3', sub2='avisando 30 dias: sem multa'), 'pop', d=.9)
       + T(40, 400, 'a lei protege', 't-hand') + T(40, 428, 'quem usa o imóvel', 't-hand') + T(40, 456, 'para morar e trabalhar', 't-hand'))
fs4 = (T(40, 64, 'VENDA DA SAFRA FUTURA DE SOJA', 't-small', style='letter-spacing:.1em')
       + P('M60 470H550M60 470V110', 'ink', style='stroke-width:1.5') + T(60, 500, 'CONTRATO', 't-small') + T(550, 500, 'ENTREGA', 't-small', anchor='end')
       + P('M60 330H550', 'c-dif', style='stroke-width:4') + T(540, 318, 'PREÇO FIXO', 't-small tc-dif', anchor='end')
       + P('M60 330C200 330 260 300 330 250S480 170 550 150', 'c-conc grow', m='p-fs4-c')
       + T(540, 136, 'COTAÇÃO', 't-small tc-conc', anchor='end')
       + G(P('M330 250V330M440 190V330', 'thin dash'), 'fade', d=.9)
       + G(T(360, 290, 'risco assumido', 't-hand'), 'fade', d=1.1)
       + G(R(60, 530, 480, 44, 'f-ink') + T(300, 558, 'STJ: CONTRATO MANTIDO', 't-small t-light', anchor='middle'), 'pop', d=1.4))

# ---- boa-fé ----
bf0 = (T(150, 70, 'SUBJETIVA', 't-mid tc-muted', anchor='middle') + T(450, 70, 'OBJETIVA', 't-mid tc-dif', anchor='middle')
       + P('M300 90V520', 'thin dash')
       + person(150, 250, None)
       + G(C(210, 170, 34, 'f-paper ink') + C(182, 208, 7, 'f-paper ink') + T(210, 176, '?', 't-mid', anchor='middle'), 'pop', d=.2)
       + T(150, 420, 'estado de consciência', 't-hand', anchor='middle') + T(150, 448, 'o que a pessoa sabia', 't-hand', anchor='middle')
       + person(450, 250, None)
       + G(P('M390 390H510', 's-accent', extra=' stroke-width="6"') + P('M400 384v12M420 384v12M440 384v12M460 384v12M480 384v12M500 384v12', 'ink'), 'pop', d=.6)
       + T(450, 420, 'regra de conduta', 't-hand', anchor='middle') + T(450, 448, 'aferida de fora', 't-hand', anchor='middle')
       + G(R(60, 500, 480, 44, 'f-ink') + T(300, 528, 'O DIREITO CONTRATUAL USA A OBJETIVA', 't-small t-light', anchor='middle'), 'pop', d=1))
branches = [('ART. 422', 'FONTE DE DEVERES', ['informar', 'proteger', 'guardar sigilo', 'cooperar']),
            ('ART. 187', 'LIMITE A DIREITOS', ['exceder manifestamente', 'os limites da boa-fé', '= ato ilícito']),
            ('ART. 113', 'CÂNONE DE INTERPRETAÇÃO', ['o negócio se lê', 'conforme a boa-fé', 'e os usos do lugar'])]
def tri(k):
    o = G(R(170, 50, 260, 56, 'f-ink') + T(300, 85, 'BOA-FÉ OBJETIVA', 't-mid t-light', anchor='middle'))
    xs = [110, 300, 490]
    for i, (art, name, items) in enumerate(branches):
        on = i == k
        o += P(f'M300 106C300 140 {xs[i]} 130 {xs[i]} 164', ('c-dif grow' if on else 'thin'))
        g = R(xs[i] - 90, 170, 180, 80, 'w-dif ink' if on else 'w-grey ink') + T(xs[i], 202, art, 't-mid' + (' tc-dif' if on else ''), anchor='middle') + T(xs[i], 230, name, 't-small', anchor='middle', maxw=170, ctx='tri')
        o += G(g, 'pop' if on else '', d=.2, extra='' if on else ' opacity=".4"')
    if k == 0:
        for j, it in enumerate(['INFORMAR FATOS RELEVANTES', 'PROTEGER PESSOA E BENS', 'GUARDAR SIGILO', 'COOPERAR NO CUMPRIMENTO']):
            y = 300 + j * 58
            o += G(R(110, y, 30, 30, 'f-paper ink') + check(125, y + 16) + T(160, y + 21, it, 't-small', maxw=380, ctx='tri0'), 'pop', d=.4 + .2 * j)
        o += T(300, 560, 'deveres que acompanham a prestação', 't-hand', anchor='middle')
    elif k == 1:
        o += T(80, 300, 'EXERCÍCIO DE UM DIREITO', 't-small')
        o += R(80, 320, 440, 46, 'f-paper ink')
        o += G(R(80, 320, 300, 46, 'w-dif', extra=' stroke="none"'), 'pop', d=.3)
        o += G(R(380, 320, 110, 46, 'w-conc', extra=' stroke="none"'), 'pop', d=.9)
        o += P('M380 300V390', 'c-conc', style='stroke-width:3;stroke-dasharray:6 4')
        o += T(380, 410, 'LIMITE DA BOA-FÉ', 't-small tc-conc', anchor='middle')
        o += G(T(435, 460, 'excesso manifesto', 't-hand', anchor='middle') + T(435, 488, '= ato ilícito', 't-hand tc-conc', anchor='middle'), 'fade', d=1.1)
        o += G(T(190, 460, 'exercício regular', 't-hand', anchor='middle'), 'fade', d=.6)
    else:
        o += doc(200, 290, 160, 200, None, lines=10)
        o += G(lens(330, 400, 48), 'pop', d=.4)
        o += T(300, 560, 'conforme a boa-fé e os usos do lugar', 't-hand', anchor='middle')
    return o
bf = [(f'p-bf{k+1}', tri(k), branches[k][1]) for k in range(3)]
# fix positions of left branch text (anchor start at x=50 may overflow) -> use middle anchor for all
sup = (T(40, 64, 'CONSÓRCIO · 36 MESES', 't-small', style='letter-spacing:.1em')
       + ''.join(R(60 + i * 13.5, 150, 9, 40, 'w-dif ink') for i in range(36))
       + T(60, 130, 'PARCELAS CALCULADAS PELA ADMINISTRADORA', 't-small')
       + G(P('M555 150V110', 'c-conc') + T(555, 100, 'COBRA DIFERENÇA', 't-small tc-conc', anchor='end'), 'pop', d=.4)
       + G(box(40, 260, 250, 120, 'SUPRESSIO', 'a administradora perde', 'conc', ctx='sup', sub2='o direito de cobrar'), 'pop', d=.8)
       + G(box(310, 260, 250, 120, 'SURRECTIO', 'o consorciado ganha', 'dif', ctx='sup', sub2='quitação e liberação'), 'pop', d=1.1)
       + T(300, 450, 'a conduta prolongada criou confiança', 't-hand', anchor='middle')
       + T(300, 480, 'o tempo, sozinho, não basta', 't-hand', anchor='middle', style='fill:var(--muted)'))

# ---- equilíbrio ----
eq1 = (G(box(40, 180, 220, 110, 'PRESTAÇÃO', 'de A', 'conc', ctx='eq1'), 'pop') + G(box(340, 180, 220, 110, 'PRESTAÇÃO', 'de B', 'dif', ctx='eq1'), 'pop', d=.3)
       + P('M262 220H336', 'c-conc grow', m='p-eq1-c') + P('M338 250H264', 'c-dif grow', m='p-eq1-d', extra=' style="--d:.4s"')
       + T(300, 150, 'SINALAGMA', 't-mid', anchor='middle')
       + T(300, 350, 'uma é a razão de ser da outra', 't-hand', anchor='middle')
       + G(box(40, 420, 250, 100, 'GENÉTICO', 'na formação', 'grey', ctx='eq1', sub2='campo da lesão'), 'pop', d=.8)
       + G(box(310, 420, 250, 100, 'FUNCIONAL', 'na execução', 'grey', ctx='eq1', sub2='campo da revisão'), 'pop', d=1.1))
eq2 = (P('M40 150H560', 'ink', style='stroke-width:3') + C(170, 150, 8, 'f-ink') + T(170, 128, 'FORMAÇÃO', 't-small', anchor='middle')
       + T(450, 128, 'EXECUÇÃO', 't-small', anchor='middle') + P('M300 138V162', 'ink')
       + G(box(40, 200, 250, 110, 'LESÃO · 157', 'necessidade ou inexperiência', 'conc', ctx='eq2', sub2='+ desproporção manifesta'), 'pop', d=.2)
       + G(box(310, 200, 250, 110, 'ART. 317', 'motivo imprevisível', 'dif', ctx='eq2', sub2='juiz corrige o valor'), 'pop', d=.5)
       + G(box(310, 330, 250, 110, 'ART. 478', 'extraordinário e imprevisível', 'dif', ctx='eq2', sub2='resolução (contínuos/diferidos)'), 'pop', d=.8)
       + G(box(40, 330, 250, 110, 'VÍCIO · 441', 'defeito oculto na coisa', 'grey', ctx='eq2', sub2='já existente na entrega'), 'pop', d=1.1)
       + T(300, 500, 'cada remédio tem seu momento', 't-hand', anchor='middle'))

S = lambda panel, label, h3, body, lcls='': dict(panel=panel, label=label, lcls=lcls, h3=h3, body=body)
b = ''
b += chapter('01', 'c1', 'Função social', 'Aplicação da teoria funcionalista dos direitos: todo direito tem uma finalidade, e a liberdade contratual também.')
b += scrolly('Função social', [('p-fs1', fs1, 'Enunciado 23'), ('p-fs2', fs2, 'Enunciado 22'), ('p-fs3', fs3, 'Lei de Locações'), ('p-fs4', fs4, 'Caso da soja')], [
    S('p-fs1', 'Art. 421', 'A autonomia continua de pé', '<p>O art. 421 manda exercer a liberdade contratual nos limites da função social. A Jornada de Direito Civil (<strong>Enunciado 23</strong>) esclarece o alcance: a função social não elimina a autonomia contratual. Ela a atenua ou reduz quando estão em jogo interesses metaindividuais ou a dignidade da pessoa humana.</p>'),
    S('p-fs2', 'Conservação', 'Trocas úteis e justas', '<p>A função social também serve para conservar o contrato. O <strong>Enunciado 22</strong> diz que ela é cláusula geral que reforça o princípio da conservação, assegurando trocas úteis e justas. Não é licença para o juiz reescrever qualquer negócio que depois pareça ruim.</p>'),
    S('p-fs3', 'Na lei', 'Um exemplo concreto', '<p>A Lei de Locações traz um exemplo. Durante o prazo do contrato, o locador não pode retomar o imóvel; o locatário pode devolvê-lo pagando multa proporcional, e fica dispensado dela se for transferido pelo empregador para outra cidade, avisando com trinta dias de antecedência (art. 4º).</p>'),
    S('p-fs4', 'O limite', 'Intervenção mínima', '<p>O parágrafo único do art. 421 prestigia a intervenção mínima e a revisão excepcional, e o art. 421-A manda respeitar a alocação de riscos feita pelas partes.</p><p>Quando um produtor de soja vendeu a safra futura a preço fixo e depois pediu aumento porque a cotação subiu, o STJ recusou: o risco de preço tinha sido distribuído pelas partes, os fatores alegados eram previsíveis, e o lucro maior do comprador não violava a função social.</p>'),
])
b += chapter('02', 'c2', 'Boa-fé objetiva', 'O princípio central do direito contratual. A pergunta não é se a parte se sentia honesta, e sim se sua conduta, vista de fora, foi leal e cooperativa.')
b += scrolly('Boa-fé objetiva', [('p-bf0', bf0, 'Subjetiva e objetiva')] + bf + [('p-sup', sup, 'Supressio e surrectio')], [
    S('p-bf0', 'Distinção', 'Boa-fé subjetiva × objetiva', '<p>A boa-fé <strong>subjetiva</strong> é um estado de consciência: acreditar, sem saber do vício, que se age corretamente. A <strong class="dif">objetiva</strong> é uma regra de conduta, aferida de fora. Alguém pode não ter querido prejudicar ninguém e, ainda assim, ter frustrado a confiança que o próprio comportamento criou.</p>'),
    S('p-bf1', 'Função 1', 'Fonte de deveres de conduta', '<p>Pelo art. 422, as partes devem guardar probidade e boa-fé na conclusão e na execução do contrato. Daí nascem deveres que acompanham a prestação principal: informar fatos relevantes, proteger a pessoa e os bens do outro, guardar sigilo, colaborar para o cumprimento.</p><p>O peso desses deveres varia conforme o contrato e o que cada parte sabia. Não há obrigação de revelar toda vantagem negocial: cada parte também deve se informar.</p>', 'dif'),
    S('p-bf2', 'Função 2', 'Limite ao exercício de direitos', '<p>Pelo art. 187, comete ato ilícito quem exerce um direito excedendo manifestamente os limites impostos pela boa-fé. É por aqui que a boa-fé chega às negociações: romper tratativas de forma abusiva é abuso do direito de não contratar (Aula 04).</p>', 'dif'),
    S('p-bf3', 'Função 3', 'Cânone de interpretação', '<p>Pelo art. 113, os negócios jurídicos se interpretam conforme a boa-fé e os usos do lugar de sua celebração.</p><p>Como é cláusula geral, a boa-fé exige método: identificar o comportamento, a expectativa legítima, o dever violado e a consequência. Sem isso, \"boa-fé\" vira rótulo para qualquer resultado que pareça injusto.</p>', 'dif'),
    S('p-sup', 'Na prática', 'Supressio e surrectio', '<p>Uma administradora de consórcio calculou e cobrou as parcelas por 36 meses e, ao encerrar o grupo, quis cobrar uma diferença decorrente de erro próprio, recusando-se a liberar a garantia do veículo. A Turma Recursal do RS aplicou a <em>supressio</em> (a administradora perdeu o direito de cobrar a diferença) e a <em>surrectio</em> (o consorciado ganhou o direito à quitação e à liberação).</p>'),
])
b += wide(table(['Figura', 'Ideia', 'Requisitos'], [
    ['<i>Venire contra factum proprium</i>', 'Proibição de comportamento contraditório.', 'Conduta anterior que gerou confiança legítima e conduta posterior incompatível, com prejuízo para quem confiou.'],
    ['<i>Supressio</i> / <i>surrectio</i>', 'O não exercício prolongado de um direito o faz perder eficácia, e cria para a outra parte uma posição correspondente.', 'Inércia ou prática prolongada, confiança justificada e circunstâncias que tornem desleal a mudança abrupta.'],
    ['Adimplemento substancial', 'Se o devedor cumpriu quase tudo, o credor não pode resolver o contrato pelo pouco que falta. Pode cobrar o saldo.', 'Grau de cumprimento, importância do que falta e conduta das partes.'],
]))
b += chapter('03', 'c3', 'Equilíbrio econômico e sinalagma', 'Os contratos são, em regra, relações de troca, e deve haver equilíbrio entre dar e receber. Equilíbrio não é igualdade matemática: é respeito à relação pactuada.')
b += scrolly('Equilíbrio', [('p-eq1', eq1, 'Sinalagma'), ('p-eq2', eq2, 'Os remédios no tempo')], [
    S('p-eq1', 'Reciprocidade', 'Sinalagma', '<p>Nos contratos bilaterais e comutativos, cada prestação é a razão de ser da outra. Essa reciprocidade é o <strong>sinalagma</strong>, e a correspondência é relativa: preço e utilidade não precisam valer exatamente o mesmo.</p><p>O sinalagma <strong>genético</strong> é o da formação (campo da lesão); o <strong>funcional</strong> é o da execução (campo da revisão).</p>'),
    S('p-eq2', 'Onde o Código protege o equilíbrio', 'Cada desequilíbrio, um remédio', '<p><strong class="conc">Na formação:</strong> há lesão quando alguém, sob premente necessidade ou por inexperiência, se obriga a prestação manifestamente desproporcional (art. 157). O negócio pode ser salvo por suplemento ou redução do proveito (§ 2º).</p><p><strong class="dif">Na execução:</strong> o art. 317 permite ao juiz corrigir o valor da prestação diante de desproporção manifesta por motivo imprevisível; o art. 478 permite pedir a resolução dos contratos de execução continuada ou diferida quando um fato extraordinário e imprevisível torna a prestação excessivamente onerosa, com extrema vantagem para o outro.</p><p>Os vícios redibitórios (art. 441) também expressam o equilíbrio, mas exigem defeito oculto na coisa.</p>'),
])
b += chapter('04', 'c4', 'Teste')
b += quiz([
    ('A parte agiu sem intenção de prejudicar. Isso encerra a análise da boa-fé objetiva?', 'Não. A boa-fé objetiva avalia a conduta vista de fora e a confiança que ela gerou, não a intenção.'),
    ('O preço de mercado subiu e uma das partes lucrou muito mais. Há desequilíbrio que justifique revisão?', 'Não automaticamente. Compare a mudança com o risco que cada um assumiu e com os requisitos legais. No caso da soja, o STJ manteve o contrato.'),
    ('Quais são as três funções da boa-fé objetiva, com os artigos?', 'Fonte de deveres de conduta (422), limite ao exercício de direitos (187) e cânone de interpretação (113).'),
    ('Um contrato já era desproporcional quando foi assinado. Qual instituto examinar?', 'Se havia premente necessidade ou inexperiência, lesão (art. 157). Se a desproporção surgiu na execução, os arts. 317 e 478.'),
])
page('aula-03.html', '03', 'Função social, boa-fé e equilíbrio',
     'Princípios contratuais II: função social (Enunciados 22 e 23), boa-fé objetiva e sua tríplice função, equilíbrio e sinalagma.',
     ['Unidade 2 · Princípios', 'Teoria Geral dos Contratos', 'UFRGS · 2026/2'], 'Função social,', 'boa-fé e equilíbrio',
     'A <strong class="conc">função social</strong> limita a liberdade de contratar; a <strong class="dif">boa-fé objetiva</strong> exige lealdade e cooperação. O equilíbrio e o sinalagma mostram o que foi trocado e o que a lei faz quando a troca se desequilibra.',
     hero, [('Unidade', '2 · Princípios II'), ('Leitura', '≈ 18 min'), ('Antes', 'Aula 02 · Princípios I'), ('Depois', 'Aula 04 · Tratativas')], b,
     ('aula-02.html', '← Aula 02', 'Liberdade, força e relatividade'), ('aula-04.html', 'Aula 04 →', 'Tratativas'), unit='2')
