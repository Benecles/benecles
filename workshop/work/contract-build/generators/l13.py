from kit import *

# hero: a deck resting on two pillars; the shared-premise pillar gives way
hero = ('<path class="draw" d="M200 60H880" style="stroke:var(--ink);stroke-width:5;fill:none"/>'
        '<g class="pop" style="--d:.5s"><rect x="250" y="64" width="40" height="90" style="fill:var(--dif-wash);stroke:var(--dif);stroke-width:2"/></g>'
        '<g class="pop" style="--d:.8s"><path d="M790 64h40v36l-12 8l14 10l-12 10v26h-30z" style="fill:var(--conc-wash);stroke:var(--conc);stroke-width:2"/></g>'
        '<g class="pop" style="--d:1.2s;font:12px var(--mono);letter-spacing:1px"><text x="270" y="30" text-anchor="middle" style="fill:var(--dif)">PRESTAÇÕES</text>'
        '<text x="810" y="30" text-anchor="middle" style="fill:var(--conc)">PREMISSA COMUM</text>'
        '<text x="540" y="100" text-anchor="middle" style="fill:var(--ink)">O CONTRATO</text></g>')

# ---- Fig 1: shared premise vs private motive
def bubbles(shared):
    o = person(160, 260, None, 'ink') + person(440, 260, None, 'ink')
    if shared:
        o += G(R(180, 80, 240, 90, 'w-dif ink', rx=40) + T(300, 120, 'FESTIVAL', 't-mid tc-dif', anchor='middle') + T(300, 144, 'datas certas, no contrato', 't-small', anchor='middle'), 'pop', d=.2)
        o += P('M190 160L170 238M410 160L430 238', 'c-dif grow', style='--d:.5s')
        o += G(box(40, 430, 520, 100, 'PREMISSA COMUM', 'as duas partes contrataram sobre ela', 'dif', ctx='bub'), 'pop', d=.9)
    else:
        o += G(R(40, 80, 220, 90, 'w-grey ink', rx=40) + T(150, 120, 'O ARTISTA X', 't-mid', anchor='middle') + T(150, 144, 'nunca foi dito', 't-small', anchor='middle'), 'pop', d=.2)
        o += P('M150 170L158 238', 'thin grow', style='--d:.5s')
        o += G(T(440, 150, '?', 't-big', anchor='middle'), 'pop', d=.6)
        o += G(box(40, 430, 520, 100, 'MOTIVO UNILATERAL', 'não entra no contrato por presunção', 'grey', ctx='bub'), 'pop', d=.9)
    o += T(160, 400, 'LOCATÁRIO', 't-small', anchor='middle') + T(440, 400, 'LOCADOR', 't-small', anchor='middle')
    return o
LINKS = [('PREMISSA', 'qual circunstância?'), ('COMUM', 'as duas partes'), ('DETERMINANTE', 'sem ela, não haveria'), ('RUPTURA', 'o fato posterior a atingiu')]
def chain(k):
    o = T(40, 64, 'PROVE OS ELOS', 't-small', style='letter-spacing:.1em')
    for i, (a, s) in enumerate(LINKS):
        y = 100 + i * 110
        on = i <= k
        tone = 'conc' if i == 3 else 'dif'
        o += G(R(150, y, 300, 80, f'w-{tone} ink' if on else 'f-paper ink', rx=40, style='' if on else 'opacity:.35')
               + T(300, y + 36, a, 't-mid' + (f' tc-{tone}' if on else ''), anchor='middle', style='' if on else 'opacity:.4')
               + (T(300, y + 58, s, 't-small', anchor='middle') if on else ''), 'pop' if i == k else '', d=.1)
        if i < 3: o += P(f'M300 {y+80}V{y+110}', 'ink' if i < k else 'thin', style='stroke-width:4' if i < k else '')
    return o

# ---- Fig 2: routes (four scenarios)
ROUTES = [('NASCEU DESEQUILIBRADO', 'cláusula abusiva ou lesão', 'Aula 11', 'grey'),
          ('VALOR DA PRESTAÇÃO MUDOU', 'art. 317', 'Aula 12', 'dif'),
          ('FATO EXTRAORDINÁRIO, ONEROSIDADE', 'arts. 478–480', 'Aula 12', 'conc'),
          ('PREMISSA COMUM RUIU', 'base do negócio', 'esta aula', 'mix')]
def routes(k):
    o = G(R(200, 50, 200, 60, 'f-ink') + T(300, 86, 'O QUE ACONTECEU?', 't-small t-light', anchor='middle'), 'pop', d=0)
    for i, (q, r, where, tone) in enumerate(ROUTES):
        y = 150 + i * 105
        on = i == k
        o += P(f'M60 {y+35}H80', 'thin')
        o += G(R(80, y, 480, 70, (f'w-{tone} ink' if on else 'f-paper ink'), style='' if on else 'opacity:.45')
               + T(96, y + 30, q, 't-small' + (f' tc-{tone}' if on and tone != 'grey' else ''), style='' if on else 'opacity:.5')
               + T(96, y + 52, f'{r} · {where}', 't-small', style='' if on else 'opacity:.5'), 'pop' if on else '', d=.2)
    o += P('M300 110V128H60V500', 'thin')
    return o

# ---- Fig 3: adaptation clauses
idx = (T(40, 64, 'INDEXAÇÃO · AJUSTE AUTOMÁTICO', 't-small', style='letter-spacing:.1em')
       + G(R(60, 110, 200, 120, 'w-grey ink') + T(160, 160, 'ÍNDICE', 't-mid', anchor='middle') + T(160, 186, 'sobe 8%', 't-small', anchor='middle'), 'pop', d=.1)
       + P('M260 170H340', 'c-dif grow', m='p-idx-d', style='--d:.4s') + T(300, 156, 'fórmula', 't-small tc-dif', anchor='middle')
       + G(R(340, 110, 200, 120, 'w-dif ink') + T(440, 160, 'PREÇO', 't-mid tc-dif', anchor='middle') + T(440, 186, 'sobe 8%', 't-small', anchor='middle'), 'pop', d=.7)
       + G(T(300, 290, 'ninguém precisa concordar de novo', 't-hand', anchor='middle'), 'fade', d=1)
       + G(box(40, 340, 520, 130, 'ESCREVA', 'índice, periodicidade, base de cálculo,', 'grey', ctx='idx', sub2='teto e piso, e o risco que fica com cada um'), 'pop', d=1.2))
reneg = (T(40, 64, 'CLÁUSULA DE RENEGOCIAÇÃO', 't-small', style='letter-spacing:.1em')
         + G(R(40, 110, 150, 80, 'w-conc ink') + T(115, 146, 'GATILHO', 't-small tc-conc', anchor='middle') + T(115, 166, 'proibição do uso', 't-small', anchor='middle'), 'pop', d=.1)
         + P('M190 150H236', 'c-conc grow', m='p-reneg-c', style='--d:.3s')
         + G(R(240, 90, 150, 120, 'f-paper ink', rx=60) + person(290, 125, None, 'ink', s=.45) + person(340, 125, None, 'ink', s=.45) + T(315, 196, '10 dias', 't-small', anchor='middle'), 'pop', d=.5)
         + P('M390 130C420 130 430 110 450 110', 'c-dif grow', m='p-reneg-d', style='--d:.8s') + P('M390 170C420 170 430 200 450 200', 'thin grow', style='--d:.8s')
         + G(T(458, 114, 'acordo', 't-small tc-dif') + T(458, 204, 'sem acordo:', 't-small') + T(458, 220, 'saída prevista', 't-small'), 'fade', d=1)
         + G(box(40, 290, 520, 110, 'NÃO MUDA O PREÇO SOZINHA', 'obriga a negociar de boa-fé; não garante um novo', 'conc', ctx='reneg', sub2='preço nem deixa uma parte fixá-lo sozinha'), 'pop', d=1.2)
         + G(T(300, 470, 'gatilho objetivo · aviso · prazo · informação', 't-hand', anchor='middle'), 'fade', d=1.4))

S = lambda panel, label, h3, body, lcls='': dict(panel=panel, label=label, lcls=lcls, h3=h3, body=body)
b = ''
b += chapter('01', 'c1', 'O plano era comum ou só de uma parte?', 'Um fato posterior pode frustrar a razão de ser do contrato sem tornar nenhuma prestação impossível. A pergunta é se essa razão era das duas partes.', 'dif')
b += scrolly('Premissa comum × motivo', [('p-bub1', bubbles(True), 'Comum'), ('p-bub0', bubbles(False), 'Unilateral')] + [(f'p-ch{k}', chain(k), LINKS[k][0]) for k in range(4)], [
    S('p-bub1', 'Premissa comum', 'O festival que as duas partes conheciam', '<p>Duas partes alugam um espaço para sediar, em datas certas, um festival que ambas discutiram como razão do negócio. Uma proibição pública cancela o evento. O espaço continua lá, e o aluguel continua pagável, mas a função combinada talvez tenha desaparecido.</p>', 'dif'),
    S('p-bub0', 'Motivo unilateral', 'O plano que ninguém contou', '<p>Agora o locatário alugou pensando em trazer um artista específico e nunca disse isso ao locador. O artista cancela. Esse motivo pessoal não vira pressuposto do contrato só porque era importante para uma das partes.</p><p>Queda de lucro, aposta comercial frustrada ou expectativa de um lado só não mostram que a base comum mudou.</p>'),
    S('p-ch0', 'Elo 1', 'Qual era a premissa?', '<p>Identifique a circunstância concreta que sustentava a contratação: um evento, uma finalidade, uma situação de fato.</p>'),
    S('p-ch1', 'Elo 2', 'Era comum?', '<p>Mostre que as duas partes contrataram sobre ela. Indícios úteis: o texto do contrato, as mensagens da negociação, a forma de execução. O que ficou só na cabeça de uma parte não serve.</p>', 'dif'),
    S('p-ch2', 'Elo 3', 'Era determinante?', '<p>Sem aquela circunstância, o contrato não teria sido feito, ou não naqueles termos.</p>', 'dif'),
    S('p-ch3', 'Elo 4', 'O fato posterior a atingiu?', '<p>Por fim, ligue o evento à ruptura da premissa e mostre o efeito sobre as prestações que ainda restam. Só então se discute a causa jurídica e o remédio; a quebra da base não produz revisão ou extinção automática.</p>', 'conc'),
])
b += chapter('02', 'c2', 'Não confunda as teorias', 'Onerosidade excessiva e quebra da base respondem a perguntas vizinhas, mas diferentes.')
b += wide(table(['', 'Arts. 478 e 479', 'Quebra da base comum'], [
    ['O que mudou', 'Uma prestação ficou excessivamente onerosa por fato extraordinário e imprevisível.', 'Uma circunstância comum e determinante, que sustentava o negócio, desapareceu ou mudou.'],
    ['O que provar', 'Execução continuada ou diferida, evento, onerosidade, extrema vantagem, imprevisibilidade.', 'Que a premissa era comum, determinante e foi atingida; e que não era mero motivo de uma parte.'],
    ['Remédio', 'O devedor pede resolução; o réu pode oferecer modificação equitativa.', 'Não há artigo geral no Código Civil com remédio próprio. É preciso justificar a causa jurídica e a resposta.'],
], hcls=['', 'conc', 'dif']) + '<p class="note">Parte da doutrina distingue o fato imprevisível que perturba a economia do contrato da alteração de um pressuposto comum, que pode ser previsível em abstrato e ainda assim ter consequências incalculáveis. A tese exige provar o que as duas partes tinham em comum. “Base do negócio” não é um atalho para fugir dos requisitos do art. 478.</p>')
b += chapter('03', 'c3', 'Planeje a adaptação antes da crise', 'Cláusulas de revisão distribuem o risco e desenham a resposta antes do conflito. São soluções privadas, diferentes da revisão judicial.', 'dif')
b += scrolly('Duas cláusulas de adaptação', [('p-idx', idx, 'Indexação'), ('p-reneg', reneg, 'Renegociação')], [
    S('p-idx', 'Ajuste automático', 'A fórmula faz o trabalho', '<p>Uma cláusula de indexação muda o preço quando o índice ou o marco definido se move. Ninguém precisa concordar de novo. Uma cláusula clara também mostra que a parte aceitou o risco que ficou fora da fórmula.</p>', 'dif'),
    S('p-reneg', 'Renegociação', 'O gatilho obriga a conversar', '<p>A cláusula de renegociação não muda o preço: quando o gatilho ocorre, obriga as partes a negociar a adaptação. Não garante que chegarão a um novo preço, nem autoriza uma delas a fixá-lo sozinha.</p><p>Escreva o gatilho de modo objetivo, o aviso, o prazo, as informações a trocar, se a execução continua durante a conversa e o que acontece sem acordo.</p>', 'conc'),
])
b += chapter('04', 'c4', 'Quatro cenários, quatro rotas', 'Não comece pelo remédio. Comece pelo que aconteceu e pelo que as partes tinham combinado.')
b += scrolly('Mapa da revisão', [(f'p-rt{k}', routes(k), ROUTES[k][0]) for k in range(4)], [
    S('p-rt0', 'Aula 11', 'O contrato já nasceu desequilibrado', '<p>Investigue cláusula abusiva ou lesão. A data que importa é a da assinatura.</p>'),
    S('p-rt1', 'Aula 12', 'O valor da prestação perdeu a proporção', '<p>Motivo imprevisível e desproporção manifesta entre o valor devido e o valor na execução: teste o art. 317.</p>', 'dif'),
    S('p-rt2', 'Aula 12', 'Fato extraordinário tornou a prestação excessivamente onerosa', '<p>Teste os arts. 478 a 480, a álea do contrato e quem pode pedir cada resposta.</p>', 'conc'),
    S('p-rt3', 'Esta aula', 'Uma premissa comum desapareceu', '<p>Prove que ela era comum e determinante e que foi atingida; depois justifique a causa e o remédio. Se o motivo era privado, ou o risco foi aceito, não há revisão automática.</p><p>Volte ao festival: se o contrato descrevia o evento e as datas, há indício textual de premissa comum. Se o organizador guardou o plano para si, há só motivo próprio. E se o espaço ainda serve para outra finalidade, isso pesa no remédio, mas não apaga a prova.</p>'),
])
b += chapter('05', 'c5', 'Teste', 'Classifique a mudança e escolha a próxima pergunta.')
b += quiz([
    ('O locador sabia que o espaço era alugado só para um festival identificado no contrato. Uma proibição impede o festival, mas o espaço continua disponível. O que deve ser provado?', 'Que o festival era premissa comum e determinante, que a proibição a atingiu e qual o efeito nas prestações que restam. Depois vêm a causa jurídica e o remédio; nada é automático.'),
    ('O locatário alugou o espaço pensando num artista específico, mas nunca contou isso ao locador. O show é cancelado. Houve quebra da base?', 'Não. O motivo não comunicado é unilateral. Seria preciso outro indício de que a circunstância era comum e determinante para as duas partes.'),
    ('O contrato prevê reajuste anual por índice e, se uma proibição impedir o uso principal, renegociação por dez dias. O preço muda sozinho durante a proibição?', 'Não. A indexação anual é automática; a proibição só aciona o dever de negociar.'),
    ('Uma compra para revenda ficou menos lucrativa porque a procura caiu normalmente. Nenhuma cláusula ou fato comum mudou a finalidade do contrato. Cabe revisão?', 'Não. Lucro menor é resultado comercial; não prova base rompida nem os requisitos dos arts. 317 ou 478. Revisão não é seguro contra mau negócio.'),
])
page('aula-13.html', '13', 'Revisão: a base comum do negócio',
     'Revisão dos contratos III: quebra da base do negócio, premissa comum × motivo unilateral, cláusulas de indexação e renegociação.',
     ['Unidade 7 · Revisão', 'Teoria Geral dos Contratos', 'UFRGS · 2026/2'], 'A base comum', 'do negócio',
     'Uma mudança pode tirar o sentido do contrato sem tornar nada impossível. A pergunta é se a <strong class="conc">premissa</strong> que caiu era <strong class="dif">das duas partes</strong> ou só de uma.',
     hero, [('Unidade', '7 · Revisão III'), ('Leitura', '≈ 12 min'), ('Antes', 'Aula 12 · Fato superveniente'), ('Depois', 'Aula 14 · Cessão da posição')], b,
     ('aula-12.html', '← Aula 12', 'O que mudou na execução'), ('aula-14.html', 'Aula 14 →', 'Cessão da posição contratual'), unit='7')
