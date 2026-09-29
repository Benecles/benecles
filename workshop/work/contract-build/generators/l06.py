from kit import *

hero = ('<g class="pop" style="--d:.2s"><circle cx="160" cy="85" r="34" style="fill:var(--conc-wash);stroke:var(--conc);stroke-width:2"/><text x="160" y="92" text-anchor="middle" style="font:600 20px var(--sans);fill:var(--conc)">A</text></g>'
        '<g class="pop" style="--d:.4s"><circle cx="540" cy="85" r="34" style="fill:var(--conc-wash);stroke:var(--conc);stroke-width:2"/><text x="540" y="92" text-anchor="middle" style="font:600 20px var(--sans);fill:var(--conc)">B</text></g>'
        '<path class="draw" d="M196 85H504" style="stroke:var(--ink);stroke-width:3;fill:none"/>'
        '<path class="draw" d="M576 85C700 85 760 85 880 85" style="stroke:var(--dif);stroke-width:3;fill:none;stroke-dasharray:8 6"/>'
        '<g class="pop" style="--d:1.3s"><circle cx="920" cy="85" r="34" style="fill:var(--dif-wash);stroke:var(--dif);stroke-width:2"/><text x="920" y="92" text-anchor="middle" style="font:600 20px var(--sans);fill:var(--dif)">T</text></g>'
        '<g class="pop" style="--d:1.6s;font:12px var(--mono);letter-spacing:1px"><text x="350" y="140" text-anchor="middle" style="fill:var(--ink)">O CONTRATO</text>'
        '<text x="920" y="150" text-anchor="middle" style="fill:var(--dif)">O TERCEIRO</text></g>')

def node(cx, cy, l, tone='conc', label=None, r=30):
    o = C(cx, cy, r, f'w-{tone} c-{tone}', extra=' stroke-width="2"') + T(cx, cy + 8, l, f't-mid tc-{tone}', anchor='middle')
    if label: o += T(cx, cy + r + 22, label, 't-small', anchor='middle')
    return o

# ---- Fig 1: three structures on the same triangle
def tri(k):
    A, B, Tt = (130, 150), (470, 150), (300, 420)
    o = P('M160 150H440', 'ink', style='stroke-width:2.5') + T(300, 136, 'CONTRATO', 't-small', anchor='middle')
    names = [('ESTIPULANTE', 'PROMITENTE', 'BENEFICIÁRIO'), ('PROMISSÁRIO', 'PROMITENTE', 'TERCEIRO'), ('CONTRATANTE', 'OUTRA PARTE', 'NOMEADO')][k]
    o += node(*A, 'A', label=names[0]) + node(*B, 'B', label=names[1])
    tone = ['dif', 'grey', 'mix'][k]
    if k == 0:
        o += P('M455 180L320 392', 'c-dif grow', m='p-tri0-d') + T(420, 300, 'PRESTAÇÃO', 't-small tc-dif')
        o += P('M285 392L145 200', 'c-dif grow dash', m='p-tri0-d', extra=' style="--d:.6s"') + T(110, 300, 'PODE EXIGIR', 't-small tc-dif')
        o += G(node(*Tt, 'T', 'dif', names[2]), 'pop', d=.3)
        o += G(T(300, 540, 'recebe uma vantagem', 't-hand', anchor='middle'), 'fade', d=1)
    elif k == 1:
        o += G(C(300, 420, 30, 'f-paper ink', style='stroke-dasharray:5 4') + T(300, 428, 'T', 't-mid', anchor='middle') + T(300, 472, names[2], 't-small', anchor='middle'), 'pop', d=.2)
        o += P('M455 180L322 392', 'thin dash') + T(410, 300, 'NÃO SE OBRIGA', 't-small')
        o += P('M470 190C470 260 200 240 150 190', 'c-conc grow', m='p-tri1-c', extra=' style="--d:.6s"') + T(300, 256, 'PERDAS E DANOS', 't-small tc-conc', anchor='middle')
        o += G(T(300, 540, 'quem prometeu responde', 't-hand', anchor='middle'), 'fade', d=1.1)
    else:
        o += G(C(130, 150, 42, 'c-mix', style='fill:none;stroke-width:2;stroke-dasharray:4 4'), 'pulse')
        o += P('M290 390L150 205', 'c-mix grow', m='p-tri2-m', extra=' style="--d:.4s"') + T(110, 310, 'ASSUME O LUGAR', 't-small', style='fill:var(--mix)')
        o += G(node(*Tt, 'N', 'mix', names[2]), 'pop', d=.2)
        o += G(T(300, 540, 'entra no contrato desde o início', 't-hand', anchor='middle'), 'fade', d=1.1)
    return o

# ---- Fig 2: seguro de vida + regras da estipulação
sv = (G(node(120, 140, 'E', 'conc', 'SEGURADO'), 'pop', d=.1) + G(node(480, 140, 'P', 'conc', 'SEGURADORA'), 'pop', d=.3)
      + P('M155 132H445', 'ink', m='p-sv-i') + T(300, 118, 'PRÊMIO', 't-small', anchor='middle')
      + P('M445 152H155', 'ink', m='p-sv-i') + T(300, 176, 'COBERTURA', 't-small', anchor='middle')
      + G(node(300, 400, 'B', 'dif', 'BENEFICIÁRIO'), 'pop', d=.6)
      + P('M470 176L325 372', 'c-dif grow', m='p-sv-d', extra=' style="--d:.9s"') + T(420, 290, 'INDENIZAÇÃO', 't-small tc-dif')
      + G(T(300, 520, 'não pagou nada e não assinou,', 't-hand', anchor='middle') + T(300, 550, 'mas pode cobrar', 't-hand', anchor='middle'), 'fade', d=1.3))
rules = [('ART. 436', 'o estipulante pode exigir;', 'o beneficiário também, se anuir'), ('ART. 437', 'se o beneficiário pode reclamar,', 'o estipulante não libera o promitente'),
         ('ART. 438', 'reservado o direito, pode trocar', 'o beneficiário, até por testamento')]
est = T(40, 64, 'AS REGRAS DA ESTIPULAÇÃO', 't-small', style='letter-spacing:.1em')
for i, (a, b1, b2) in enumerate(rules):
    est += G(box(40, 90 + i * 130, 520, 110, a, b1, 'dif', ctx='est', sub2=b2), 'pop', d=.2 + .3 * i)
est += G(T(300, 520, 'gratuidade · aceitar ou recusar', 't-hand', anchor='middle'), 'fade', d=1.2)

# ---- Fig 3: promessa de fato de terceiro
fl = (G(box(150, 60, 300, 76, 'PROMESSA', 'B garante a A que T fará algo', 'grey', ctx='fl'), 'pop', d=.1)
      + P('M300 136V176', 'ink', m='p-fl-i') + G(box(150, 180, 300, 76, 'T NÃO FAZ', 'e nunca se obrigou', 'grey', ctx='fl'), 'pop', d=.4)
      + P('M300 256V296', 'ink', m='p-fl-i') + G(box(150, 300, 300, 76, 'B RESPONDE', 'perdas e danos · art. 439', 'conc', ctx='fl'), 'pop', d=.7)
      + G(R(40, 420, 250, 130, 'f-paper ink', style='stroke-dasharray:5 4') + T(56, 450, 'EXCEÇÃO 1 · 439, P.U.', 't-small')
          + T(56, 476, 'T é cônjuge, o ato depende', 't-small') + T(56, 494, 'da anuência dele e a conta', 't-small') + T(56, 512, 'cairia sobre os bens do casal', 't-small'), 'pop', d=1.0)
      + G(R(310, 420, 250, 130, 'f-paper ink', style='stroke-dasharray:5 4') + T(326, 450, 'EXCEÇÃO 2 · ART. 440', 't-small')
          + T(326, 476, 'T se obrigou e depois', 't-small') + T(326, 494, 'descumpriu: agora quem', 't-small') + T(326, 512, 'responde é T', 't-small'), 'pop', d=1.2))
def store(x, y, w, h, label, ghost=False):
    st = 'stroke-dasharray:6 5' if ghost else ''
    return R(x, y, w, h, 'f-paper ink', style=st) + T(x + w / 2, y + h / 2 + 5, label, 't-small', anchor='middle', style='opacity:.6' if ghost else '')
shop = (T(40, 64, 'SHOPPING CENTER', 't-small', style='letter-spacing:.1em') + R(40, 80, 520, 300, 'f-paper ink')
        + G(store(60, 100, 150, 120, 'ÂNCORA?', True), 'pop', d=.1) + G(store(390, 100, 150, 120, 'ÂNCORA?', True), 'pop', d=.3)
        + G(store(230, 100, 140, 120, '') + R(230, 100, 140, 120, 'w-dif', extra=' stroke="none"') + T(300, 164, 'LOJISTA', 't-small tc-dif', anchor='middle'), 'pop', d=.5)
        + P('M60 250H540', 'thin') + T(300, 300, 'CORREDOR VAZIO', 't-small', anchor='middle', style='opacity:.5')
        + G(box(40, 410, 250, 130, 'O QUE PESOU', 'promessa feita, decisiva', 'grey', ctx='shop', sub2='mudança omitida'), 'pop', d=.9)
        + G(box(310, 410, 250, 130, 'RESULTADO', 'condenação do', 'conc', ctx='shop', sub2='empreendedor mantida'), 'pop', d=1.2))

# ---- Fig 4: pessoa a declarar
nom = (T(40, 64, 'NOMEAÇÃO · ARTS. 467 A 471', 't-small', style='letter-spacing:.1em')
       + P('M60 150H540', 'ink', style='stroke-width:2') + C(60, 150, 8, 'f-ink') + T(60, 184, 'CONTRATO', 't-small')
       + T(60, 202, 'com reserva (467)', 't-small')
       + G(P('M60 130C200 90 380 90 520 130', 'c-mix grow', m='p-nom-m') + T(290, 90, '5 DIAS, SALVO OUTRO PRAZO (468)', 't-small', anchor='middle', style='fill:var(--mix)'), '', d=.2)
       + C(540, 150, 8, 'f-paper ink')
       + G(box(40, 250, 250, 130, 'NOMEAÇÃO EFICAZ', 'aceita com a forma do', 'dif', ctx='nom', sub2='contrato → assume tudo') + T(54, 368, 'desde a celebração (469)', 't-small'), 'pop', d=.8)
       + G(box(310, 250, 250, 130, 'SÓ OS ORIGINAIS', 'sem nomeação ou recusa', 'conc', ctx='nom', sub2='nomeado insolvente') + T(324, 368, 'ou incapaz (470, 471)', 't-small'), 'pop', d=1.1)
       + P('M300 160C300 210 165 210 165 246M300 160C300 210 435 210 435 246', 'thin grow', extra=' style="--d:.6s"')
       + G(T(300, 460, 'para fechar o negócio', 't-hand', anchor='middle') + T(300, 490, 'sem revelar ainda quem fica com ele', 't-hand', anchor='middle'), 'fade', d=1.4))

# ---- Fig 5: contrato preliminar
pre = (G(doc(60, 120, 150, 190, 'PRELIMINAR', lines=6), 'pop', d=.1) + G(doc(390, 120, 150, 190, 'DEFINITIVO', 'w-dif ink', lines=6), 'pop', d=.6)
       + P('M220 215H380', 'c-dif grow', m='p-pre-d', extra=' style="--d:.3s"') + T(300, 200, 'OBRIGA A CELEBRAR', 't-small tc-dif', anchor='middle')
       + G(box(60, 380, 480, 110, 'ART. 462', 'todos os requisitos essenciais do definitivo', 'dif', ctx='pre', sub2='menos a forma'), 'pop', d=.9)
       + G(T(300, 540, 'o registro dá eficácia perante terceiros', 't-hand', anchor='middle'), 'fade', d=1.2))
rec = (G(box(170, 50, 260, 70, 'RECUSA', 'sem cláusula de arrependimento', 'grey', ctx='rec'), 'pop', d=.1)
       + P('M300 120V150', 'ink') + P('M140 150H460', 'ink') + P('M140 150V190M300 150V190M460 150V190', 'ink', m='p-rec-i')
       + G(box(40, 196, 170, 130, 'EXIGIR', 'com prazo', 'dif', ctx='rec', sub2='art. 463'), 'pop', d=.4)
       + G(box(215, 196, 170, 130, 'JUIZ SUPRE', 'a vontade', 'dif', ctx='rec', sub2='art. 464'), 'pop', d=.6)
       + G(box(390, 196, 170, 130, 'RESOLVER', 'perdas e danos', 'conc', ctx='rec', sub2='art. 465'), 'pop', d=.8)
       + G(box(40, 380, 520, 100, 'PROMESSA UNILATERAL', 'só uma parte promete; o credor aceita no prazo,', 'grey', ctx='rec', sub2='ou a promessa perde eficácia (art. 466)'), 'pop', d=1.1)
       + G(T(300, 540, 'as duas partes, juntas, podem mudar o definitivo', 't-hand', anchor='middle'), 'fade', d=1.4))

# ---- Fig 6: arras
def arras(pen):
    o = T(40, 64, ('PENITENCIAIS · ART. 420' if pen else 'CONFIRMATÓRIAS · ARTS. 418 E 419'), 't-small', style='letter-spacing:.1em')
    o += node(110, 150, 'A', 'conc', 'DEU O SINAL') + node(490, 150, 'B', 'conc', 'RECEBEU')
    o += G(coin(300, 150, 22), 'pop', d=.2) + P('M145 150H270M330 150H455', 'thin') + P('M330 150H452', 'ink', m=('p-arr1-i' if pen else 'p-arr0-i'))
    q = 'SE A DESISTE' if pen else 'SE A DESCUMPRE'
    r_ = 'SE B DESISTE' if pen else 'SE B DESCUMPRE'
    o += G(box(40, 250, 250, 140, q, 'perde o sinal', 'conc', ctx='arr', sub2=('e nada mais' if pen else 'B desfaz e retém')), 'pop', d=.5)
    o += G(box(310, 250, 250, 140, r_, 'devolve o sinal', 'dif', ctx='arr', sub2='+ o equivalente'), 'pop', d=.8)
    if pen:
        o += G(R(40, 420, 520, 100, 'f-ink') + T(300, 462, 'SEM INDENIZAÇÃO SUPLEMENTAR', 't-small t-light', anchor='middle')
               + T(300, 486, 'o arrependimento tem preço fixo', 't-small t-light', anchor='middle'), 'pop', d=1.1)
    else:
        o += G(R(40, 420, 520, 100, 'f-ink') + T(300, 462, 'SINAL = INDENIZAÇÃO MÍNIMA', 't-small t-light', anchor='middle')
               + T(300, 486, 'prejuízo maior pode ser provado e cobrado', 't-small t-light', anchor='middle'), 'pop', d=1.1)
    return o

S = lambda panel, label, h3, body, lcls='': dict(panel=panel, label=label, lcls=lcls, h3=h3, body=body)
b = ''
b += chapter('01', 'c1', 'Três formas de envolver um terceiro', 'O terceiro recebe uma vantagem, deve praticar um ato ou passa a ocupar o lugar de uma das partes? Cada resposta leva a uma figura diferente.')
b += scrolly('O terceiro no contrato', [('p-tri0', tri(0), 'Estipulação'), ('p-tri1', tri(1), 'Promessa de fato'), ('p-tri2', tri(2), 'Pessoa a declarar')], [
    S('p-tri0', 'Arts. 436 a 438', 'Estipulação: o terceiro recebe', '<p>Estipulante e promitente combinam uma prestação a favor de um terceiro. O estipulante pode exigir o cumprimento, e o beneficiário também, sujeito às condições do contrato.</p>', 'dif'),
    S('p-tri1', 'Arts. 439 e 440', 'Promessa de fato de terceiro: o promitente responde', '<p>Uma parte promete à outra que um terceiro fará algo. O terceiro não fica obrigado por isso. Se ele não fizer, quem prometeu paga perdas e danos.</p>', 'conc'),
    S('p-tri2', 'Arts. 467 a 471', 'Pessoa a declarar: o nomeado assume o lugar', '<p>Uma parte contrata e reserva o direito de indicar depois quem assumirá seus direitos e obrigações. Se a indicação não acontecer como a lei exige, o contrato fica entre os contratantes originais.</p>'),
])
b += wide(table(['', 'O que acontece com o terceiro', 'Se algo falhar'], [
    ['Em favor de terceiro', 'Recebe a prestação e pode exigi-la, sujeito às condições do contrato.', 'O promitente continua obrigado perante o estipulante.'],
    ['Promessa de fato', 'Não fica obrigado só porque alguém prometeu por ele.', 'O promitente paga perdas e danos (art. 439).'],
    ['Pessoa a declarar', 'Nomeado e aceito, assume direitos e deveres desde a celebração.', 'Sem nomeação eficaz, o contrato fica com os originais (arts. 470 e 471).'],
]) + '<p class="note">Uma empresa paga uma clínica para atender sua equipe: estipulação a favor dos trabalhadores. Promete ao shopping que uma loja âncora vai se instalar: promessa de fato de terceiro, e a loja não vira parte. Compra um imóvel reservando-se o direito de nomear a sociedade que ficará com ele: pessoa a declarar.</p>')
b += chapter('02', 'c2', 'Estipulação em favor de terceiro', 'O acordo é entre estipulante e promitente, mas a prestação vai para o beneficiário.', 'dif')
b += scrolly('A estipulação', [('p-sv', sv, 'Seguro de vida'), ('p-est', est, 'Regras')], [
    S('p-sv', 'O exemplo clássico', 'Seguro de vida', '<p>O estipulante contrata em nome próprio com o promitente para que este cumpra uma prestação em favor de um terceiro. No seguro de vida, o segurado paga o prêmio, a seguradora se obriga, e quem recebe a indenização é o beneficiário, que não participou da negociação.</p>', 'dif'),
    S('p-est', 'Arts. 436 a 438', 'Quem pode exigir e quem pode mudar', '<p>O estipulante pode exigir o cumprimento (art. 436), e o beneficiário também, se anuir às condições do contrato (parágrafo único). Se o contrato deu ao beneficiário o direito de reclamar a execução, o estipulante não pode exonerar o promitente (art. 437). E, se reservou esse direito, pode substituir o beneficiário sem a anuência dele nem do promitente, por ato entre vivos ou por testamento (art. 438).</p><p>Duas marcas da figura: a <strong>gratuidade</strong>, porque o beneficiário recebe sem dar nada em troca, e a possibilidade de ele <strong>aceitar ou recusar</strong> o benefício.</p>'),
])
b += chapter('03', 'c3', 'Promessa de fato de terceiro', 'O terceiro não fica obrigado porque alguém prometeu por ele. Quem prometeu é que responde.', 'conc')
b += scrolly('A promessa de fato de terceiro', [('p-fl', fl, 'Regra e exceções'), ('p-shop', shop, 'Lojas-âncora')], [
    S('p-fl', 'Arts. 439 e 440', 'Regra e exceções', '<p>O promitente se compromete, perante o promissário, a que um terceiro realize uma prestação. Se o terceiro não a realiza, o promitente responde por perdas e danos (art. 439).</p><p>Há duas exceções. Não há responsabilidade se o terceiro for cônjuge do promitente, o ato depender da anuência dele e, pelo regime de bens, a indenização acabar recaindo sobre os bens do casal (parágrafo único). E nada deve o promitente se o terceiro chegou a se obrigar e depois descumpriu (art. 440): aí quem responde é o próprio terceiro.</p>', 'conc'),
    S('p-shop', 'Na jurisprudência', 'Shopping e lojas-âncora', '<p>O empreendedor de um shopping prometeu a instalação de lojas-âncora, e isso pesou na decisão de um lojista de investir. As lojas não vieram, e o lojista não foi avisado da mudança de planos. O STJ manteve a condenação do empreendedor.</p><p>Nem todo anúncio de shopping é promessa indenizável. Pesou que a promessa foi feita, que foi decisiva para o lojista e que a mudança foi omitida.</p>'),
])
b += chapter('04', 'c4', 'Contrato com pessoa a declarar', 'Uma das partes contrata sabendo que poderá se fazer substituir por outra pessoa, que assume o contrato como se o tivesse celebrado.')
b += scrolly('A nomeação', [('p-nom', nom, 'Prazo e efeitos')], [
    S('p-nom', 'Arts. 467 a 471', 'Prazo, forma e efeitos', '<p>A reserva precisa constar do contrato (art. 467). A indicação deve ser comunicada à outra parte em cinco dias, salvo outro prazo, e a aceitação do nomeado precisa ter a mesma forma do contrato (art. 468).</p><p>Com indicação válida, o nomeado adquire os direitos e assume as obrigações desde a celebração (art. 469). O contrato fica só entre os originais se não houver indicação, se o nomeado recusar, se for insolvente sem que o outro soubesse (art. 470) ou se for incapaz ou insolvente no momento da nomeação (art. 471).</p><p>Diferença para a estipulação: aqui o nomeado assume direitos <em>e</em> deveres; lá, o terceiro só recebe.</p>'),
])
b += chapter('05', 'c5', 'Contrato preliminar', 'É um contrato cujo objeto é outro contrato: as partes se obrigam a celebrar o definitivo depois.', 'dif')
b += scrolly('Do preliminar ao definitivo', [('p-pre', pre, 'A ponte'), ('p-rec', rec, 'A recusa')], [
    S('p-pre', 'Art. 462', 'Por que fazer um preliminar', '<p>As partes ainda não querem os efeitos do negócio, mas querem a garantia de que ele vai sair. Em vez de depender da boa vontade do outro, transformam o compromisso em vínculo.</p><p>Por isso o preliminar deve ter todos os requisitos essenciais do definitivo, exceto a forma (art. 462). O registro previsto no art. 463, parágrafo único, não é requisito de validade: serve para dar eficácia perante terceiros.</p>', 'dif'),
    S('p-rec', 'Arts. 463 a 466', 'Quando uma parte se recusa', '<p>Sem cláusula de arrependimento, qualquer parte pode exigir que a outra celebre o definitivo, fixando prazo (art. 463). Se a outra não cumprir, o juiz pode suprir sua vontade e dar caráter definitivo ao preliminar, se a natureza da obrigação permitir (art. 464). A parte lesada também pode preferir resolver o contrato com perdas e danos (art. 465).</p><p>Se só uma parte prometeu contratar, o credor precisa manifestar aceitação no prazo previsto, ou num prazo razoável que o devedor lhe der; sem isso, a promessa perde eficácia (art. 466).</p><p>Num caso de venda de empreendimento, as partes assinaram uma proposta e depois um definitivo com outra divisão de responsabilidades. O STJ fez valer o definitivo: juntas, as partes podem mudar o que prometeram. Uma delas sozinha, não.</p>'),
])
b += chapter('06', 'c6', 'Arras ou sinal', 'O sinal confirma o negócio. Se o contrato for cumprido, é devolvido ou abatido do preço; se for descumprido, serve de indenização.', 'conc')
b += scrolly('O destino do sinal', [('p-arr0', arras(False), 'Confirmatórias'), ('p-arr1', arras(True), 'Penitenciais')], [
    S('p-arr0', 'Regra geral', 'Arras confirmatórias', '<p>Arras são dinheiro ou outro bem móvel entregue por uma parte à outra na conclusão do contrato (art. 417). Cumprido o contrato, são devolvidas ou abatidas da prestação, se forem do mesmo gênero.</p><p>Se quem deu as arras descumpre, a outra parte pode desfazer o contrato e retê-las. Se quem descumpre é quem as recebeu, quem as deu pode desfazer o contrato e exigir a devolução mais o equivalente, com atualização monetária, juros e honorários (art. 418). A parte inocente pode provar prejuízo maior e cobrar a diferença, ou exigir o cumprimento, usando as arras como mínimo da indenização (art. 419).</p>', 'conc'),
    S('p-arr1', 'Art. 420', 'Arras penitenciais', '<p>Se o contrato dá a qualquer parte o direito de se arrepender, as arras passam a ter função só indenizatória: quem as deu e desiste perde o sinal; quem as recebeu e desiste devolve o sinal mais o equivalente. Não há indenização suplementar (art. 420).</p><p>Quem prevê o arrependimento troca o direito de exigir a execução por uma saída de preço conhecido.</p>'),
])
b += wide(table(['', 'Arras', 'Cláusula penal'], [
    ['Quando', 'Entregues na conclusão do contrato.', 'Combinada para o caso de inadimplemento ou mora.'],
    ['Função', 'Confirmar o negócio e servir de indenização mínima (art. 419).', 'Pena prefixada, cobrável sem prova de prejuízo (art. 416).'],
    ['Há entrega?', 'Sim, de dinheiro ou bem móvel.', 'Não: é só uma cláusula.'],
], hcls=['', 'conc', 'dif']))
b += chapter('07', 'c7', 'Teste')
b += quiz([
    ('Um contrato prevê que o pagamento será feito diretamente a uma pessoa que não o assinou. Que figura é essa?', 'Estipulação em favor de terceiro (arts. 436 a 438). O estipulante pode exigir o pagamento, e o beneficiário também, sujeito às condições do contrato.'),
    ('Um empreendedor promete a um lojista que lojas-âncora vão se instalar no shopping. Elas não vêm. As lojas-âncora respondem?', 'Não. A promessa de fato de terceiro não obriga o terceiro. Quem responde por perdas e danos é o empreendedor, que prometeu (art. 439).'),
    ('O comprador indicou, no sexto dia, a sociedade que ficaria com o imóvel. O contrato não fixava prazo. E agora?', 'O prazo legal é de cinco dias (art. 468). Sem indicação eficaz no prazo, o contrato produz efeitos entre os contratantes originais (art. 470, I).'),
    ('Uma parte se recusa a assinar o contrato definitivo. O que a outra pode fazer?', 'Se o preliminar tem os requisitos essenciais e não prevê arrependimento, pode exigir o definitivo, e o juiz supre a vontade de quem se recusa (arts. 463 e 464). Ou pode pedir perdas e danos (art. 465).'),
    ('O contrato prevê direito de arrependimento, e houve sinal. Quem recebeu o sinal desiste. O que acontece?', 'As arras são penitenciais: devolve o sinal mais o equivalente, e não há indenização suplementar (art. 420).'),
])
page('aula-06.html', '06', 'Incidentes da formação',
     'Estipulação em favor de terceiro, promessa de fato de terceiro, contrato com pessoa a declarar, contrato preliminar e arras.',
     ['Unidade 4 · Incidentes da formação', 'Teoria Geral dos Contratos', 'UFRGS · 2026/2'], 'Incidentes', 'da formação',
     'Um contrato pode beneficiar quem não o assinou, prometer o ato de outra pessoa ou reservar um lugar para alguém que ainda será indicado. Fecham a aula o <strong class="dif">contrato preliminar</strong> e as <strong class="conc">arras</strong>.',
     hero, [('Unidade', '4 · Incidentes'), ('Leitura', '≈ 16 min'), ('Antes', 'Aula 05 · Proposta e aceitação'), ('Depois', 'Aula 07 · Classificação I')], b,
     ('aula-05.html', '← Aula 05', 'Proposta e aceitação'), ('aula-07.html', 'Aula 07 →', 'Classificação dos contratos'), unit='4')
