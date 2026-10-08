from kit import *

# hero: three switches, sliding into place
def hsw(x, lab, a, b, pos, d):
    return (f'<text x="{x}" y="36" style="font:12px var(--mono);letter-spacing:1px;fill:var(--muted)">{lab}</text>'
            f'<rect x="{x}" y="52" width="260" height="44" rx="22" style="fill:var(--paper-2);stroke:var(--ink);stroke-width:1.5"/>'
            f'<text x="{x+20}" y="128" style="font:12px var(--mono);fill:var(--ink)">{a}</text><text x="{x+240}" y="128" text-anchor="end" style="font:12px var(--mono);fill:var(--ink)">{b}</text>'
            f'<g class="pop" style="--d:{d}s"><circle cx="{x+(238 if pos else 22)}" cy="74" r="17" style="fill:var(--{"dif" if pos else "conc"})"/></g>')
hero = (hsw(40, 'QUEM SE OBRIGA?', 'UNILATERAL', 'BILATERAL', 1, .4) + hsw(410, 'QUEM TEM VANTAGEM?', 'GRATUITO', 'ONEROSO', 1, .8)
        + hsw(780, 'HÁ RISCO ASSUMIDO?', 'COMUTATIVO', 'ALEATÓRIO', 0, 1.2)
        + '<path class="draw" d="M40 156H1040" style="stroke:var(--ink);stroke-width:1.5;fill:none"/>')

def sw(y, q, a, b, pos, note, d):
    o = T(40, y, q, 't-small', style='letter-spacing:.1em')
    o += R(40, y + 14, 520, 56, 'w-grey ink', rx=28)
    o += T(474, y + 49, b, 't-small', anchor='middle', style='opacity:.45') if pos == 0 else T(126, y + 49, a, 't-small', anchor='middle', style='opacity:.45')
    kx = 46 if pos == 0 else 394
    o += G(R(kx, y + 20, 160, 44, 'f-ink', rx=22, style=f'fill:var(--{"dif" if pos else "conc"})') + T(kx + 80, y + 48, a if pos == 0 else b, 't-small t-light', anchor='middle'), 'pop', d=d)
    o += G(T(300, y + 98, note, 't-hand', anchor='middle'), 'fade', d=d + .3)
    return o
def grid(title, v, notes):
    o = T(300, 50, title, 't-mid', anchor='middle')
    o += sw(100, 'QUEM SE OBRIGA?', 'UNILATERAL', 'BILATERAL', v[0], notes[0], .2)
    o += sw(260, 'QUEM TEM VANTAGEM?', 'GRATUITO', 'ONEROSO', v[1], notes[1], .5)
    o += sw(420, 'HÁ RISCO ASSUMIDO?', 'COMUTATIVO', 'ALEATÓRIO', v[2], notes[2], .8)
    return o
g1 = grid('COMPRA E VENDA', (1, 1, 0), ('entregar e pagar', 'bem e preço', 'prestações certas'))
g2 = grid('DOAÇÃO PURA', (0, 0, 0), ('só o doador', 'recebe sem dar nada', 'gratuito não é aleatório'))
g3 = grid('SWAP CAMBIAL', (1, 1, 1), ('as duas partes', 'as duas partes', 'depende do dólar'))

# ---- exceções
def node(cx, cy, l, tone='conc', label=None, r=30):
    o = C(cx, cy, r, f'w-{tone} c-{tone}', extra=' stroke-width="2"') + T(cx, cy + 8, l, f't-mid tc-{tone}', anchor='middle')
    if label: o += T(cx, cy + r + 22, label, 't-small', anchor='middle')
    return o
e476 = (node(120, 150, 'A', 'conc', 'VENDEDOR') + node(480, 150, 'B', 'dif', 'COMPRADORA')
        + P('M160 132H440', 'thin dash') + T(300, 118, 'ENTREGA · NÃO FEITA', 't-small', anchor='middle')
        + G(check(300, 142, False), 'pop', d=.3)
        + P('M440 172H160', 'c-conc grow', m='p-476-c', extra=' style="--d:.5s"') + T(300, 196, '"PAGUE!"', 't-small tc-conc', anchor='middle')
        + G(R(360, 250, 200, 110, 'w-dif ink', rx=8) + coin(400, 290) + coin(424, 306) + T(452, 296, 'RETÉM', 't-small tc-dif') + T(380, 340, 'até receber a entrega', 't-small'), 'pop', d=1.0)
        + G(box(40, 420, 520, 110, 'ART. 476', 'quem não cumpriu não pode exigir', 'ink', ctx='e476', sub2='a prestação correlata do outro'), 'pop', d=1.3))
rite = (T(40, 64, 'CUMPRIR MAL', 't-small', style='letter-spacing:.1em')
        + R(70, 100, 150, 300, 'f-paper ink') + P('M70 180H220M70 260H220M70 340H220', 'thin')
        + G(R(96, 280, 98, 110, 'w-conc ink') + P('M110 300l30 30l-12 14l40 30', 'c-conc'), 'pop', d=.3)
        + T(145, 430, 'ELEVADOR', 't-small', anchor='middle') + T(145, 450, 'cabine com falhas', 't-small', anchor='middle')
        + G(R(290, 110, 270, 50, 'w-dif ink') + T(304, 141, 'PARCELA 1 · PAGA', 't-small tc-dif'), 'pop', d=.5)
        + G(R(290, 180, 270, 50, 'w-dif ink') + T(304, 211, 'PARCELA 2 · PAGA', 't-small tc-dif'), 'pop', d=.7)
        + G(R(290, 250, 270, 50, 'f-paper ink', style='stroke-dasharray:6 4') + T(304, 281, 'PARCELA FINAL · RETIDA', 't-small tc-conc'), 'pop', d=.9)
        + G(box(290, 340, 270, 110, 'NON RITE', 'falha relevante', 'conc', ctx='rite', sub2='equivale a não cumprir'), 'pop', d=1.2)
        + T(300, 530, 'defeito pequeno: abatimento, não retenção', 't-hand', anchor='middle'))
ins = (T(40, 64, 'PATRIMÔNIO DE A', 't-small', style='letter-spacing:.1em')
       + P('M60 380H560M60 100V380', 'ink')
       + P('M60 150H240C300 150 320 300 400 320H540', 'c-conc grow', extra=' style="--d:.2s"')
       + P('M240 90V390', 'thin dash') + T(240, 410, 'CONTRATO', 't-small', anchor='middle')
       + G(T(420, 300, 'queda posterior', 't-hand'), 'fade', d=1)
       + G(box(40, 440, 520, 110, 'ART. 477', 'B suspende até receber', 'dif', ctx='ins', sub2='a prestação ou garantia suficiente'), 'pop', d=1.3))

# ---- evicção
ev1 = (T(40, 64, 'EVICÇÃO · ARTS. 447 A 457', 't-small', style='letter-spacing:.1em')
       + P('M60 300H540', 'ink', style='stroke-width:2')
       + G(C(140, 300, 9, 'f-ink', style='fill:var(--mix)') + T(140, 336, 'DIREITO DE C', 't-small', anchor='middle') + T(140, 354, '(anterior)', 't-small', anchor='middle'), 'pop', d=.1)
       + G(C(300, 300, 9, 'f-ink') + T(300, 336, 'VENDA A → B', 't-small', anchor='middle'), 'pop', d=.4)
       + G(C(460, 300, 9, 'f-ink', style='fill:var(--conc)') + T(460, 336, 'B PERDE', 't-small tc-conc', anchor='middle') + T(460, 354, 'o bem', 't-small', anchor='middle'), 'pop', d=.7)
       + P('M140 290C200 170 400 170 452 288', 'c-mix grow', m='p-ev1-m', extra=' style="--d:1s"')
       + T(300, 180, 'defeito no direito, não na coisa', 't-hand', anchor='middle')
       + G(box(40, 410, 160, 110, 'A', 'alienante', 'grey', ctx='ev1', sub2='responde'), 'pop', d=1.3)
       + G(box(220, 410, 160, 110, 'B', 'evicto', 'conc', ctx='ev1', sub2='perde'), 'pop', d=1.4)
       + G(box(400, 410, 160, 110, 'C', 'evictor', 'mix', ctx='ev1', sub2='tinha o direito'), 'pop', d=1.5))
recov = ['o preço, pelo valor na evicção', 'frutos que teve de restituir', 'despesas do contrato', 'prejuízos diretos', 'custas e honorários']
ev2 = T(40, 64, 'O QUE O EVICTO RECEBE · ART. 450', 't-small', style='letter-spacing:.1em')
for i, t in enumerate(recov):
    ev2 += G(R(40, 84 + i * 50, 30, 30, 'f-paper ink') + check(55, 99 + i * 50) + T(86, 105 + i * 50, t, 't-serif'), 'pop', d=.1 + .15 * i)
ev2 += (T(40, 368, 'EVICÇÃO PARCIAL · ART. 455', 't-small', style='letter-spacing:.1em')
        + G(box(40, 386, 250, 100, 'CONSIDERÁVEL', 'desfazer ou receber', 'conc', ctx='ev2', sub2='a parte do preço'), 'pop', d=1.0)
        + G(box(310, 386, 250, 100, 'NÃO CONSIDERÁVEL', 'só indenização', 'grey', ctx='ev2'), 'pop', d=1.2)
        + T(300, 540, 'comprou sabendo? não reclama (457)', 't-hand', anchor='middle'))
lau = (G(doc(60, 90, 140, 170, 'IMÓVEL', lines=5), 'pop', d=.1)
       + G(R(400, 90, 140, 170, 'w-dif ink') + T(470, 150, 'QUOTAS', 't-mid tc-dif', anchor='middle') + T(470, 176, 'ou ações', 't-small', anchor='middle') + T(470, 280, 'SOCIEDADE', 't-small', anchor='middle'), 'pop', d=.3)
       + P('M210 150H390', 'ink grow', m='p-lau-i', extra=' style="--d:.5s"') + P('M390 210H210', 'c-dif grow', m='p-lau-d', extra=' style="--d:.8s"')
       + T(300, 136, 'INTEGRALIZA', 't-small', anchor='middle') + T(300, 236, 'RECEBE EM TROCA', 't-small tc-dif', anchor='middle')
       + G(box(40, 340, 520, 100, 'ONEROSO', 'há troca, mesmo sem dinheiro', 'dif', ctx='lau', sub2='→ o laudêmio incide'), 'pop', d=1.1)
       + T(300, 510, 'sem preço em dinheiro ≠ doação', 't-hand', anchor='middle'))

# ---- aleatórios
def tree(x, y, fruits, ghost=False):
    o = P(f'M{x} {y}v-88', 'ink', style='stroke-width:5')
    o += P(f'M{x} {y-40}l-26 -34M{x} {y-50}l22 -30', 'ink', style='stroke-width:3')
    cl = 'w-dif ink' if not ghost else 'f-paper ink'
    st = 'stroke-dasharray:5 4' if ghost else ''
    o += P(f'M{x-70} {y-86}a34 34 0 0 1 20-52a40 40 0 0 1 74-18a38 38 0 0 1 60 30a30 30 0 0 1 -8 50z', cl, style=st)
    for i, (fx, fy) in enumerate(fruits):
        o += G(C(x + fx, y - 100 + fy, 8, 'accent', extra=' stroke="var(--ink)" stroke-width="1.2"'), 'pop', d=.6 + .1 * i)
    return o
F = [(-34, -14), (8, -46), (-4, -8), (36, -18), (-20, -40), (22, 6)]
def alea(kind):
    o = T(40, 64, ['ART. 458 · RISCO DE NÃO EXISTIR', 'ART. 459 · RISCO DE QUANTIDADE', 'ART. 460 · COISA EXPOSTA A RISCO'][kind], 't-small', style='letter-spacing:.1em')
    if kind == 0:
        o += G(tree(150, 330, F), '', d=0) + T(150, 360, 'SAFRA CHEIA', 't-small', anchor='middle')
        o += G(tree(450, 330, [], True), 'pop', d=.4) + T(450, 360, 'NADA', 't-small', anchor='middle')
        o += G(box(40, 400, 520, 110, 'PREÇO INTEGRAL NOS DOIS', 'o comprador assumiu o risco', 'dif', ctx='a0', sub2='de nada existir (salvo dolo ou culpa)'), 'pop', d=1.0)
    elif kind == 1:
        o += G(tree(150, 330, [F[1], F[3]]), '', d=0) + T(150, 360, 'VEIO POUCO', 't-small', anchor='middle')
        o += G(tree(450, 330, [], True), 'pop', d=.4) + T(450, 360, 'NADA', 't-small', anchor='middle')
        o += G(box(40, 400, 250, 110, 'PREÇO INTEGRAL', 'o risco era', 'dif', ctx='a1', sub2='de quantidade'), 'pop', d=1.0)
        o += G(box(310, 400, 250, 110, 'SEM VENDA', 'nada veio:', 'conc', ctx='a1', sub2='devolve o preço'), 'pop', d=1.2)
    else:
        o += P('M40 300C120 280 200 320 280 300S440 280 560 300', 'c-dif', style='stroke-width:2') + P('M40 330C120 310 200 350 280 330S440 310 560 330', 'c-dif', style='stroke-width:1.2;opacity:.5')
        o += G(P('M220 250h160l-24 40h-112z', 'f-paper ink') + P('M300 250v-80M300 180l50 50H300', 'ink'), 'pop', d=.2)
        o += T(300, 140, 'CARGA NO MAR', 't-small', anchor='middle')
        o += G(box(40, 380, 250, 130, 'PREÇO DEVIDO', 'mesmo que a coisa', 'dif', ctx='a2', sub2='já não existisse'), 'pop', d=.8)
        o += G(box(310, 380, 250, 130, 'ART. 461', 'o outro sabia que', 'conc', ctx='a2', sub2='já tinha afundado?') + T(324, 490, 'anulável por dolo', 't-small'), 'pop', d=1.1)
    return o

# ---- vícios redibitórios
vr = (T(40, 64, 'DEFEITO OCULTO · ART. 441', 't-small', style='letter-spacing:.1em')
      + R(120, 100, 360, 170, 'f-paper ink', rx=10) + P('M150 140H450M150 180H390M150 220H420', 'thin')
      + G(lens(360, 190, 34) + P('M340 170l14 12l-8 10l18 14', 'c-conc'), 'pop', d=.3)
      + T(300, 300, 'já existia na entrega', 't-hand', anchor='middle')
      + P('M300 316V346', 'ink') + P('M150 346H450M150 346V376M450 346V376', 'ink', m='p-vr-i')
      + G(box(40, 380, 250, 100, 'REDIBIR', 'devolve a coisa,', 'conc', ctx='vr', sub2='desfaz o contrato'), 'pop', d=.7)
      + G(box(310, 380, 250, 100, 'ABATER', 'fica com a coisa,', 'dif', ctx='vr', sub2='paga menos (442)'), 'pop', d=.9)
      + T(300, 530, 'sabia do vício? + perdas e danos (443)', 't-hand', anchor='middle'))
def bar(y, x0, days, maxd, cls, label, sub, d):
    w = 440 * days / maxd
    return G(R(120, y, w, 34, cls) + T(110, y + 22, label, 't-small', anchor='end') + T(128 + w, y + 22, sub, 't-small'), 'pop', d=d)
prz = (T(40, 64, 'PRAZOS · ART. 445', 't-small', style='letter-spacing:.1em')
       + T(40, 110, 'MÓVEL', 't-mid tc-conc')
       + bar(126, 0, 30, 365, 'w-conc ink', 'ENTREGA', '30 dias', .2)
       + bar(170, 0, 15, 365, 'w-conc ink', 'JÁ NA POSSE', '15 dias', .4)
       + bar(214, 0, 180, 365, 'w-conc ink', 'CIÊNCIA', 'até 180 dias', .6)
       + T(40, 300, 'IMÓVEL', 't-mid tc-dif')
       + bar(316, 0, 365, 365, 'w-dif ink', 'ENTREGA', '', .8) + T(540, 338, '1 ano', 't-small', anchor='end')
       + bar(360, 0, 182, 365, 'w-dif ink', 'JÁ NA POSSE', '6 meses', 1.0)
       + bar(404, 0, 365, 365, 'w-dif ink', 'CIÊNCIA', '', 1.2) + T(540, 426, 'até 1 ano', 't-small', anchor='end')
       + G(R(40, 470, 520, 80, 'f-ink') + T(300, 502, 'GARANTIA CONTRATUAL (446)', 't-small t-light', anchor='middle')
           + T(300, 526, 'prazo legal suspenso; avisar em 30 dias', 't-small t-light', anchor='middle'), 'pop', d=1.5))

def jul(tone, b, span, corpo, tese):
    return f'<article class="julgado {tone}"><header><b>{b}</b><span>{span}</span></header><div class="corpo"><p>{corpo}</p></div><div class="tese">{tese}</div></article>'

S = lambda panel, label, h3, body, lcls='': dict(panel=panel, label=label, lcls=lcls, h3=h3, body=body)
b = ''
b += chapter('01', 'c1', 'Três perguntas independentes', 'Uma compra e venda comum é, ao mesmo tempo, bilateral, onerosa e comutativa. Cada termo responde a uma pergunta diferente.')
b += scrolly('A grade de classificação', [('p-g1', g1, 'Compra e venda'), ('p-g2', g2, 'Doação'), ('p-g3', g3, 'Swap')], [
    S('p-g1', 'Exemplo 1', 'Compra e venda comum', '<p><strong>Bilateral</strong>: as duas partes se obrigam, uma a entregar, outra a pagar. <strong>Onerosa</strong>: bem e preço são vantagens recíprocas. <strong>Comutativa</strong>: as prestações são certas, ainda que o valor de mercado varie depois.</p><p>\"Bilateral\" não quer dizer que duas pessoas assinaram. Quer dizer que as duas assumiram obrigações.</p>'),
    S('p-g2', 'Exemplo 2', 'Doação pura', '<p>Unilateral, porque só o doador se obriga. Gratuita, porque o donatário recebe sem dar nada. E comutativa: o que se promete é certo. Gratuidade e aleatoriedade são perguntas diferentes.</p><p>A classificação tem efeito prático: negócios benéficos se interpretam estritamente (art. 114), e nos contratos benéficos quem é favorecido responde por culpa, e o outro só por dolo (art. 392).</p>', 'conc'),
    S('p-g3', 'Exemplo 3', 'Derivativo', '<p>Um swap cambial obriga as duas partes e é oneroso para ambas. O que muda é o terceiro interruptor: o resultado depende da variação do índice escolhido. É aleatório.</p>', 'dif'),
])
b += chapter('02', 'c2', 'Bilaterais × unilaterais', 'Nos contratos bilaterais, as obrigações são ligadas entre si. Por isso, quem ainda não cumpriu a sua parte não pode exigir a do outro.', 'conc')
b += wide(table(['Tipo', 'Quem se obriga', 'Exemplo'], [
    ['Unilateral', 'Só uma parte.', 'Doação pura.'],
    ['Bilateral (sinalagmático)', 'As duas, e uma obrigação é a razão da outra.', 'Compra e venda.'],
    ['Plurilateral', 'Várias partes, em busca de um fim comum.', 'Sociedade.'],
    ['Bilateral imperfeito', 'Nasce unilateral; na execução, surge obrigação para quem não tinha se comprometido.', 'Depositante que reembolsa as despesas do depositário.'],
]))
b += scrolly('As defesas do contrato bilateral', [('p-476', e476, 'Art. 476'), ('p-rite', rite, 'Non rite'), ('p-477', ins, 'Art. 477')], [
    S('p-476', 'Art. 476', 'Exceção do contrato não cumprido', '<p>Em contrato bilateral, quem ainda não cumpriu a própria obrigação não pode exigir a do outro. Cobrada sem ter recebido, a outra parte pode suspender a contraprestação e alegar a <em>exceptio non adimpleti contractus</em>.</p><p>A defesa segue a ligação entre as prestações: não autoriza reter qualquer valor por qualquer falha. Identifique qual prestação corresponde à que está sendo cobrada.</p>', 'conc'),
    S('p-rite', 'Cumprimento defeituoso', '<em>Exceptio non rite adimpleti contractus</em>', '<p>Cumprir mal, fora da qualidade, do tempo ou do modo combinados, também pode justificar a retenção. A falha precisa ser relevante para a finalidade do contrato. Defeito pequeno gera abatimento ou reparação, não a suspensão de toda a contraprestação.</p>'),
    S('p-477', 'Art. 477', 'Exceção de inseguridade', '<p>Depois de concluído o contrato, o patrimônio de uma parte diminui a ponto de pôr em dúvida o cumprimento. A outra pode suspender a sua prestação até receber a prestação devida ou garantia suficiente.</p><p>Aqui ainda pode não haver inadimplemento: o gatilho é a perda de segurança, que precisa ser posterior ao contrato e concreta. A suspensão não vira, sozinha, rescisão ou indenização.</p>', 'dif'),
])
b += wide('<div class="julgados">'
          + jul('conc', 'Exclusividade', 'art. 476', 'Num contrato de loja em shopping, a exclusividade de venda fazia parte do negócio. Quando a administração deixou uma loja-âncora vender o mesmo produto, a lojista se recusou a pagar o saldo.', 'A recusa foi legítima: o inadimplemento parcial atingia a prestação central do contrato.')
          + jul('', 'Elevador', 'non rite', 'Num contrato de instalação de elevador, parte do serviço foi feita, mas a perícia apontou falhas graves na cabine e no material.', 'O STJ manteve a inexigibilidade da parcela final. Serviço feito com falha grave continua inadimplido.')
          + jul('dif', 'Costura', 'art. 477', 'Numa prestação continuada de serviços de costura, a contratante suspendeu os pagamentos alegando obrigações essenciais pendentes e a piora patrimonial da prestadora.', 'O art. 477 exige risco concreto e posterior ao contrato. Preocupação genérica não basta.')
          + '</div>')
b += chapter('03', 'c3', 'Onerosos × gratuitos', 'A pergunta é quem tem vantagem econômica. Nos contratos onerosos, quem adquire tem garantia contra a evicção.', 'dif')
b += scrolly('Onerosidade e evicção', [('p-lau', lau, 'Integralização'), ('p-ev1', ev1, 'Evicção'), ('p-ev2', ev2, 'O que se recupera')], [
    S('p-lau', 'Caso', 'O imóvel usado para integralizar capital', '<p>No contrato <strong>gratuito</strong>, só uma parte tem vantagem. No <strong>oneroso</strong>, as duas têm, e a contraprestação não precisa ser em dinheiro.</p><p>Uma sociedade transferiu um imóvel em terreno de marinha para integralizar o capital de outra empresa. O laudêmio só é devido nas transferências onerosas. A Corte Especial do STJ decidiu que a transferência é onerosa, porque quem integraliza capital entrega o bem e recebe quotas ou ações em troca; o Tema Repetitivo 332 confirmou. Um acórdão de 2009 em sentido contrário foi superado.</p><p>A onerosidade também muda regras de garantia fora da evicção: na cessão de crédito a título oneroso, o cedente responde pela existência do crédito (art. 295).</p>', 'dif'),
    S('p-ev1', 'Arts. 447 a 449', 'Evicção', '<p>O adquirente (<strong>evicto</strong>) perde o bem, total ou parcialmente, porque um terceiro (<strong>evictor</strong>) tinha direito anterior sobre ele. O problema está no direito transmitido, não na coisa.</p><p>O alienante responde nos contratos onerosos, inclusive em hasta pública (art. 447). As partes podem reforçar, diminuir ou excluir a garantia (art. 448), mas, mesmo excluída, o evicto recupera o preço se não sabia do risco ou não o assumiu (art. 449).</p>', 'conc'),
    S('p-ev2', 'Arts. 450 a 457', 'O que se recupera', '<p>Salvo acordo diferente, o evicto recebe o preço, pelo valor da coisa na época da evicção, os frutos que teve de restituir, as despesas do contrato, os prejuízos diretos e as custas e honorários (art. 450). Os arts. 451 a 454 tratam de deteriorações e benfeitorias.</p><p>Na evicção parcial considerável, o evicto escolhe entre desfazer o contrato ou receber a parte do preço do que perdeu; se não for considerável, só cabe indenização (art. 455). Quem comprou sabendo que a coisa era alheia ou litigiosa não pode reclamar (art. 457). O art. 456 foi revogado pelo CPC de 2015.</p><p>Num caso de lotes atingidos por decisão que declarou ineficaz a venda, por fraude à execução fiscal, o STJ reconheceu a evicção antes do trânsito em julgado, porque a perda já era efetiva ou iminente.</p>'),
])
b += chapter('04', 'c4', 'Comutativos × aleatórios', 'A pergunta é se as prestações são certas ou se uma delas depende de um risco que alguém assumiu. Comparar o preço com o valor de mercado depois não responde isso.', 'dif')
b += scrolly('As três figuras do contrato aleatório', [('p-a0', alea(0), 'Art. 458'), ('p-a1', alea(1), 'Art. 459'), ('p-a2', alea(2), 'Art. 460')], [
    S('p-a0', 'Art. 458', 'Risco de a coisa não existir', '<p>No contrato <strong>comutativo</strong>, as partes conseguem estimar as prestações desde a formação, sem exigir igualdade matemática. No <strong>aleatório</strong>, uma parte aceita que a existência, a quantidade ou a conservação da prestação dependa de fato incerto.</p><p>Na primeira figura, compra-se a coisa futura com o risco de ela não existir: o alienante recebe o preço inteiro mesmo que nada venha, desde que não tenha agido com dolo ou culpa.</p>', 'dif'),
    S('p-a1', 'Art. 459', 'Risco quanto à quantidade', '<p>O comprador assume o risco de vir menos do que o esperado. O preço é integral mesmo que venha pouco. Mas, se nada vier, não há venda, e o preço é devolvido.</p>'),
    S('p-a2', 'Arts. 460 e 461', 'Coisa existente exposta a risco', '<p>A coisa existe, mas está exposta a um risco que o adquirente assume, como uma carga em viagem. O preço é devido mesmo que ela já não existisse no dia do contrato. Se o alienante sabia que o risco já tinha se realizado, a venda é anulável por dolo (art. 461).</p>', 'conc'),
])
b += wide('<div class="julgados">'
          + jul('dif', 'Swap', 'álea conhecida', 'Uma fabricante contratou um swap cambial para se proteger da variação do dólar. O real desvalorizou, ela perdeu dinheiro e pediu revisão.', 'O STJ manteve o contrato: a variação cambial era o próprio risco do negócio, conhecido pelas duas partes. Fraude ou falha de informação continuam controláveis.')
          + jul('', 'Loteria', 'risco assumido', 'Quem cedeu direitos sobre uma nova loteria aceitou receber só se a arrecadação superasse certo patamar em relação a outra loteria. O patamar não foi atingido.', 'Nada é devido e não há ilícito: ninguém prometeu manter a proporção. Risco na remuneração não torna o contrato gratuito.')
          + '</div>')
b += chapter('05', 'c5', 'Vícios redibitórios', 'Defeito oculto numa coisa recebida por contrato comutativo, que já existia na entrega.', 'conc')
b += scrolly('O defeito oculto', [('p-vr', vr, 'Redibir ou abater'), ('p-prz', prz, 'Prazos')], [
    S('p-vr', 'Arts. 441 a 444', 'Redibir ou abater', '<p>Vício redibitório é o defeito oculto em coisa recebida por contrato comutativo, ou por doação onerosa, que a torna imprópria ao uso ou diminui seu valor (art. 441). O adquirente escolhe: rejeita a coisa e desfaz o contrato, ou fica com ela e pede abatimento no preço (art. 442).</p><p>Se o alienante conhecia o vício, devolve o que recebeu e paga perdas e danos; se não conhecia, devolve o valor e as despesas do contrato (art. 443). Se a coisa perecer depois da entrega por vício que já existia, ele continua responsável (art. 444). A doutrina explica o instituto pelas teorias do erro, do inadimplemento e da garantia.</p>', 'conc'),
    S('p-prz', 'Arts. 445 e 446', 'Prazos', '<p>Trinta dias para móvel e um ano para imóvel, contados da entrega. Se o adquirente já estava na posse, contam da alienação e caem pela metade. Se o vício só puder ser conhecido mais tarde, o prazo conta da ciência, até o máximo de 180 dias para móvel e um ano para imóvel.</p><p>Enquanto vigora uma garantia contratual, os prazos legais não correm, mas o adquirente deve avisar o defeito em 30 dias da descoberta (art. 446).</p>'),
])
b += wide('<div class="julgados">' + jul('conc', 'Carro novo', 'sem vício', 'Um veículo novo tinha potência e capacidade um pouco abaixo das anunciadas.', 'O STJ entendeu que as diferenças não o tornavam impróprio ao uso nem reduziam seu valor. Não havia vício redibitório nem dano moral.') + '</div>')
b += chapter('06', 'c6', 'Roteiro para um caso', 'Classifique antes de responder, e ache o fato que aciona a regra.')
b += wide(table(['Pergunta', 'Se a resposta for…', 'Consequência'], [
    ['Quem se obrigou?', 'As duas partes: bilateral.', 'Cabem as exceções dos arts. 476 e 477.'],
    ['Quem tem vantagem?', 'As duas: oneroso.', 'Há garantia contra evicção. A contraprestação pode ser bem, serviço ou participação.'],
    ['Há risco assumido?', 'Sim: aleatório.', 'Veja se o risco é de existência, de quantidade ou de coisa exposta (arts. 458 a 460).'],
    ['Qual é o problema?', 'Direito de terceiro ou defeito físico oculto?', 'Evicção no primeiro caso; vício redibitório no segundo.'],
]))
b += chapter('07', 'c7', 'Teste')
b += quiz([
    ('A compradora é cobrada, mas o vendedor ainda não entregou o equipamento. Ela precisa pagar?', 'Não. O contrato é bilateral, e ela pode opor a exceção do contrato não cumprido (art. 476) até a entrega.'),
    ('A safra veio menor do que o esperado, e o comprador tinha assumido o risco de quantidade. Ele paga o preço inteiro?', 'Sim, se veio alguma coisa (art. 459). Se nada viesse, não haveria venda, e o preço seria devolvido.'),
    ('Depois da compra, descobre-se que um terceiro tem direito anterior sobre parte importante do imóvel, e a perda é iminente. O que o comprador pode pedir?', 'É evicção parcial considerável: ele escolhe entre desfazer o contrato ou receber a parte do preço do que perdeu (art. 455).'),
    ('Um carro tem uma pequena diferença num dado técnico, mas funciona normalmente e não perdeu valor. Cabe redibição?', 'Não. O art. 441 exige defeito que torne a coisa imprópria ao uso ou diminua seu valor.'),
    ('A doação pura é um contrato aleatório?', 'Não. É unilateral e gratuita, mas comutativa: o que se promete é certo.'),
])
page('aula-07.html', '07', 'Classificação dos contratos I',
     'Bilaterais e unilaterais (arts. 476 e 477), onerosos e gratuitos (evicção), comutativos e aleatórios (arts. 458 a 461) e vícios redibitórios.',
     ['Unidade 5 · Classificação', 'Teoria Geral dos Contratos', 'UFRGS · 2026/2'], 'Classificação', 'dos contratos I',
     'Três perguntas classificam o contrato: quem se obriga, quem tem vantagem, se alguma prestação depende de risco. Cada resposta traz suas próprias regras: <strong class="conc">defesas</strong>, <strong class="dif">garantias</strong> e distribuição de risco.',
     hero, [('Unidade', '5 · Classificação I'), ('Leitura', '≈ 20 min'), ('Antes', 'Aula 06 · Incidentes'), ('Depois', 'Aula 08 · Classificação II')], b,
     ('aula-06.html', '← Aula 06', 'Incidentes da formação'), ('aula-08.html', 'Aula 08 →', 'Classificação dos contratos II'), unit='5')
