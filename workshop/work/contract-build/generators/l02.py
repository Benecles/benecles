from kit import *

hero = ('<ellipse cx="540" cy="85" rx="260" ry="62" style="fill:none;stroke:var(--ink);stroke-dasharray:6 6;opacity:.5"/>'
        '<path class="draw" d="M390 85H690" style="stroke:var(--ink);stroke-width:3;fill:none"/>'
        '<g class="pop" style="--d:.6s"><circle cx="380" cy="85" r="22" style="fill:var(--conc)"/><text x="380" y="90" text-anchor="middle" style="font:700 14px var(--sans);fill:var(--paper)">A</text>'
        '<circle cx="700" cy="85" r="22" style="fill:var(--dif)"/><text x="700" y="90" text-anchor="middle" style="font:700 14px var(--sans);fill:var(--paper)">B</text></g>'
        '<g class="pop" style="--d:1.2s"><circle cx="980" cy="85" r="20" style="fill:none;stroke:var(--ink);stroke-width:2"/><text x="980" y="90" text-anchor="middle" style="font:700 14px var(--sans);fill:var(--ink)">C</text>'
        '<path d="M954 85H820" style="stroke:var(--ink);stroke-width:1.5;stroke-dasharray:4 5;fill:none"/><path d="M812 75l14 20M826 75l-14 20" style="stroke:var(--conc);stroke-width:2.5"/></g>'
        '<g class="pop" style="--d:1.6s;font:12px var(--mono);letter-spacing:1px"><text x="0" y="40" style="fill:var(--ink)">O VÍNCULO PRENDE SÓ QUEM CONTRATOU</text>'
        '<text x="1070" y="150" text-anchor="end" style="fill:var(--conc)">O TERCEIRO NÃO PODE SABOTÁ-LO</text></g>')

# ---- Fig 1: freedom ----
lib1 = (T(40, 64, 'DUAS LIBERDADES', 't-small', style='fill:var(--muted)')
        + G(box(40, 100, 520, 150, 'LIBERDADE DE CONTRATAR', 'decidir SE vai contratar', 'dif', ctx='lib1', sub2='e COM QUEM'), 'pop')
        + P('M300 250V300', 'ink', m='p-lib1-i')
        + G(box(40, 310, 520, 150, 'LIBERDADE CONTRATUAL', 'decidir O QUE contratar', 'conc', ctx='lib1', sub2='prestações · prazos · preço · riscos'), 'pop', d=.5)
        + T(300, 530, 'ambas são aplicação da autonomia privada', 't-hand', anchor='middle'))
lib2 = (R(40, 60, 520, 480, 'f-paper', style='stroke:var(--const);stroke-width:14;opacity:.9')
        + T(300, 100, 'LIMITES DO ORDENAMENTO', 't-small', anchor='middle', style='letter-spacing:.14em')
        + G(R(110, 180, 380, 240, 'w-dif ink') + T(300, 290, 'ESPAÇO DA', 't-mid tc-dif', anchor='middle') + T(300, 318, 'AUTONOMIA', 't-mid tc-dif', anchor='middle'), 'fade')
        + G(R(70, 120, 220, 40, 'w-conc ink') + T(84, 146, 'CC 421 · FUNÇÃO SOCIAL', 't-small tc-conc', maxw=200, ctx='lib2'), 'pop', d=.3)
        + G(R(310, 120, 220, 40, 'w-grey ink') + T(324, 146, 'NORMAS COGENTES', 't-small', maxw=200, ctx='lib2'), 'pop', d=.5)
        + G(R(70, 440, 220, 40, 'w-grey ink') + T(84, 466, 'CDC · REGIME ESPECIAL', 't-small', maxw=200, ctx='lib2'), 'pop', d=.7)
        + G(R(310, 440, 220, 40, 'w-grey ink') + T(324, 466, 'DIREITOS DE TERCEIROS', 't-small', maxw=200, ctx='lib2'), 'pop', d=.9)
        + G(R(170, 350, 260, 40, 'f-paper ink') + T(184, 376, 'CC 421-A · PRESUME PARIDADE', 't-small', maxw=240, ctx='lib2'), 'pop', d=1.2))
lib3 = (doc(60, 90, 140, 180, None, lines=8) + T(130, 300, 'PREDISPONENTE', 't-small', anchor='middle') + T(130, 328, 'redige tudo', 't-hand', anchor='middle')
        + person(440, 110, None) + T(440, 250, 'ADERENTE', 't-small', anchor='middle')
        + G(R(360, 270, 76, 40, 'w-dif ink', rx=20) + T(398, 295, 'ACEITO', 't-small', anchor='middle')
            + R(446, 270, 84, 40, 'w-conc ink', rx=20) + T(488, 295, 'RECUSO', 't-small', anchor='middle'), 'pop', d=.4)
        + P('M204 180H352', 'thin dash', m='p-lib3-u')
        + G(box(40, 370, 520, 70, 'ART. 423', 'cláusula ambígua ou contraditória → a favor do aderente', 'paper', tcls='t-mid', ctx='lib3'), 'pop', d=.8)
        + G(box(40, 460, 520, 70, 'ART. 424', 'renúncia antecipada a direito inerente → nula', 'paper', tcls='t-mid', ctx='lib3'), 'pop', d=1.1))

# ---- Fig 2: binding force ----
def link(x, y): return R(x, y, 70, 34, 'ink', rx=17, style='fill:none;stroke-width:5')
for1 = (person(90, 170, 'A', 'ink') + person(510, 170, 'B', 'ink')
        + G(link(160, 214) + link(210, 214) + link(260, 214) + link(310, 214) + link(360, 214), 'pop', d=.2)
        + G(R(120, 380, 360, 66, 'f-ink') + T(300, 421, 'PACTA SUNT SERVANDA', 't-mid t-light', anchor='middle'), 'pop', d=.6)
        + T(300, 496, 'cada parte pode exigir da outra', 't-hand', anchor='middle') + T(300, 528, 'a prestação prometida', 't-hand', anchor='middle'))
for2 = (person(90, 90, 'A', 'ink', s=.8) + person(510, 90, 'B', 'ink', s=.8)
        + link(160, 124) + link(210, 124) + P('M286 118l30 46', 'c-conc', style='stroke-width:4') + link(330, 124) + link(380, 124)
        + T(510, 250, 'NÃO CUMPRE', 't-small tc-conc', anchor='middle')
        + T(90, 250, 'CREDOR', 't-small', anchor='middle')
        + P('M110 270C130 330 110 330 110 360', 'c-dif grow', m='p-for2-d')
        + P('M110 270C200 330 300 320 300 360', 'c-dif grow', m='p-for2-d', extra=' style="--d:.3s"')
        + P('M110 270C300 300 490 320 490 360', 'c-dif grow', m='p-for2-d', extra=' style="--d:.6s"')
        + G(box(30, 370, 170, 110, 'EXIGIR', 'o cumprimento', 'dif', ctx='for2'), 'pop', d=.4)
        + G(box(215, 370, 170, 110, 'RESOLVER', 'o contrato', 'dif', ctx='for2'), 'pop', d=.7)
        + G(box(400, 370, 170, 110, 'COBRAR', 'perdas e danos', 'dif', ctx='for2'), 'pop', d=1.0)
        + T(300, 540, 'não se descumpre por conveniência', 't-hand', anchor='middle'))

# ---- Fig 3: relativity and the third-party interferer ----
def bond(x1, x2, y, la='A', lb='B'):
    return (P(f'M{x1+26} {y}H{x2-26}', 'ink', style='stroke-width:4')
            + C(x1, y, 26, 'f-ink', style='fill:var(--conc)') + T(x1, y + 7, la, 't-mid t-light', anchor='middle')
            + C(x2, y, 26, 'f-ink', style='fill:var(--dif)') + T(x2, y + 7, lb, 't-mid t-light', anchor='middle'))
rel1 = ('<ellipse cx="240" cy="250" rx="200" ry="110" class="thin dash" style="stroke-width:2"/>'
        + T(240, 125, 'EFEITOS DO CONTRATO', 't-small', anchor='middle', style='fill:var(--muted)')
        + bond(140, 340, 250)
        + G(C(510, 250, 26, 'ink', extra=' stroke-width="2"') + T(510, 257, 'C', 't-mid', anchor='middle') + T(510, 310, 'TERCEIRO', 't-small', anchor='middle'), 'pop', d=.4)
        + G(T(510, 338, 'não é parte', 't-hand', anchor='middle') + T(510, 368, 'não deve nada', 't-hand', anchor='middle'), 'fade', d=.8)
        + G(box(40, 430, 520, 100, 'ESTIPULAÇÃO EM FAVOR DE TERCEIRO', 'a exceção: um contrato pode BENEFICIAR alguém de fora', 'grey', ctx='rel1', sub2='(arts. 436 a 438 · Aula 06)'), 'pop', d=1.1))
rel2 = ('<ellipse cx="240" cy="200" rx="200" ry="110" class="thin dash" style="stroke-width:2"/>'
        + bond(140, 340, 200)
        + C(510, 200, 26, 'ink', extra=' stroke-width="2"') + T(510, 207, 'C', 't-mid', anchor='middle')
        + G(P('M490 150C470 110 530 110 510 150', 'ink') + C(510, 140, 4, 'f-ink') + T(510, 110, 'SABE', 't-small', anchor='middle'), 'pop', d=.2)
        + P('M484 204C420 220 300 180 250 200', 'c-conc grow', m='p-rel2-c', extra=' style="--d:.4s"')
        + G(P('M232 180l20 20-16 4 20 22', 'c-conc', style='stroke-width:3'), 'pop', d=1.0)
        + G(box(40, 360, 520, 72, 'TERCEIRO OFENSOR', 'sabe do contrato e age para que seja descumprido', 'conc', ctx='rel2'), 'pop', d=1.2)
        + G(box(40, 450, 520, 90, 'RESPONDE POR ATO PRÓPRIO', 'viola a boa-fé e o dever geral', 'ink', ctx='rel2', sub2='de respeitar contratos alheios'), 'pop', d=1.5))
rel3 = ('<ellipse cx="240" cy="200" rx="210" ry="110" class="thin dash" style="stroke-width:2"/>'
        + P('M166 200H314', 'ink', style='stroke-width:4')
        + box(40, 170, 126, 60, 'FISCHER', 'Nova Schin', 'conc', ctx='rel3')
        + box(314, 170, 126, 60, 'ZECA', 'o cantor', 'dif', ctx='rel3')
        + T(240, 140, 'CONTRATO DE CAMPANHA · 2004', 't-small', anchor='middle', style='fill:var(--muted)')
        + G(box(460, 170, 110, 60, 'ÁFRICA', 'Brahma', 'grey', ctx='rel3'), 'pop', d=.3)
        + P('M460 214C420 240 420 240 400 232', 'c-conc grow', m='p-rel3-c', extra=' style="--d:.6s"')
        + T(515, 260, 'ALICIA', 't-small tc-conc', anchor='middle')
        + G(R(120, 370, 360, 74, 'f-ink') + T(300, 405, 'STJ, 3ª TURMA, 2014', 't-small t-light', anchor='middle')
            + T(300, 430, 'ÁFRICA CONDENADA', 't-mid t-light', anchor='middle'), 'pop', d=1.1)
        + T(300, 500, 'terceiro ofensor · violação à boa-fé objetiva', 't-hand', anchor='middle'))

S = lambda panel, label, h3, body, lcls='': dict(panel=panel, label=label, lcls=lcls, h3=h3, body=body)
b = ''
b += chapter('01', 'c1', 'Liberdade contratual', 'Os princípios contratuais são seis: liberdade, relatividade, força vinculativa, boa-fé objetiva, função social e equilíbrio econômico. Esta aula trata dos três primeiros; a próxima, dos outros três.')
b += scrolly('Liberdade e seus limites', [('p-lib1', lib1, 'Duas liberdades'), ('p-lib2', lib2, 'Limites da autonomia'), ('p-lib3', lib3, 'Contrato de adesão')], [
    S('p-lib1', 'Autonomia privada', 'Liberdade de contratar e liberdade contratual', '<p>A liberdade contratual é a aplicação da autonomia privada aos contratos. Ela tem duas faces. A <strong class="dif">liberdade de contratar</strong> é decidir se vai contratar e com quem. A <strong class="conc">liberdade contratual</strong> é decidir o conteúdo: prestações, prazos, preço e riscos.</p>'),
    S('p-lib2', 'Os limites', 'Arts. 421 e 421-A', '<p>O próprio ordenamento limita essa liberdade. O art. 421 manda exercê-la nos limites da função social e, nas relações privadas, prestigia a intervenção mínima e a revisão excepcional.</p><p>O art. 421-A presume que contratos civis e empresariais são paritários e simétricos, até que elementos concretos mostrem o contrário. Manda respeitar a alocação de riscos feita pelas partes e ressalva os regimes especiais: a presunção de paridade não afasta o CDC.</p>'),
    S('p-lib3', 'Quando uma parte só adere', 'Contratos de adesão', '<p>Quando uma parte apenas adere a cláusulas já redigidas, o Código Civil a protege de duas formas. Cláusulas ambíguas ou contraditórias se interpretam a favor do aderente (art. 423), e é nula a renúncia antecipada a direito que decorre da natureza do negócio (art. 424).</p><p>As duas regras têm alcance preciso: o art. 423 depende de ambiguidade ou contradição; o art. 424, de renúncia antecipada a direito inerente ao negócio. Nas relações de consumo, valem as regras próprias do CDC.</p>', 'conc'),
])
b += chapter('02', 'c2', 'Força obrigatória', 'É o <em>pacta sunt servanda</em>: quem manifestou vontade fica vinculado.')
b += scrolly('O vínculo', [('p-for1', for1, 'O vínculo obriga'), ('p-for2', for2, 'Remédios do credor')], [
    S('p-for1', 'Pacta sunt servanda', 'O contrato faz lei entre as partes', '<p>Formado validamente, o contrato cria deveres exigíveis. Cada parte pode exigir da outra a prestação prometida, e o vínculo não desaparece só porque cumprir ficou menos vantajoso.</p>'),
    S('p-for2', 'Se uma parte não cumpre', 'Os remédios', '<p>Se uma parte não cumpre, a outra pode exigir a prestação, pedir a resolução do contrato ou cobrar perdas e danos.</p><p>A força obrigatória não é absoluta: convive com as regras de invalidade, com a boa-fé, com a função social, com o equilíbrio e com a revisão nos casos previstos em lei. O que não se admite é descumprir por conveniência.</p>'),
])
b += chapter('03', 'c3', 'Relatividade e terceiro ofensor', 'O contrato só vincula quem o celebrou. Um terceiro não vira devedor por conhecer o contrato, mas também não pode agir para destruí-lo.')
b += scrolly('Dentro e fora do contrato', [('p-rel1', rel1, 'Relatividade'), ('p-rel2', rel2, 'Terceiro ofensor'), ('p-rel3', rel3, 'O caso Zeca Pagodinho')], [
    S('p-rel1', 'Relatividade', 'A e B se obrigam entre si', '<p>Se A promete entregar um equipamento a B, só A deve a entrega. Um concorrente que ficou de fora não passa a dever nada por causa desse contrato.</p><p>Há contratos que beneficiam um terceiro, como a estipulação em favor de terceiro, mas isso vem de uma figura própria. A regra continua sendo que ninguém se torna parte só por ser mencionado ou afetado pelo contrato.</p>'),
    S('p-rel2', 'A tutela externa do crédito', 'Mas o contrato existe para todos', '<p>Relatividade não significa que o contrato seja invisível para quem está fora. Terceiros devem respeitá-lo: é o <strong>dever geral de respeito aos contratos alheios</strong>, que decorre da boa-fé objetiva e da função social.</p><p>Quem conhece um contrato e age para que ele seja descumprido é o <strong class="conc">terceiro ofensor</strong>, e responde pelos danos que causar. Não por descumprir o contrato, que nunca assinou, mas por ato próprio.</p><p>Fazer uma proposta melhor a alguém, sozinho, não é ilícito. Vira ilícito quando o terceiro, sabendo do contrato em curso, age justamente para que ele seja rompido. E o contratante que rompe continua respondendo pelo próprio inadimplemento.</p>', 'conc'),
    S('p-rel3', 'O caso-referência', 'Zeca Pagodinho', '<p>Em 2004, Zeca Pagodinho tinha contrato para estrelar a campanha da cerveja Nova Schin, criada pela agência Fischer. A agência África, que atendia a Brahma, aliciou o cantor, que abandonou a campanha e virou garoto-propaganda da concorrente. A Fischer processou a África.</p><p>O STJ (3ª Turma, 2014) manteve a condenação. A ementa resume a tese: intervenção em contrato alheio, terceiro ofensor, violação à boa-fé objetiva. O cantor responde pelo contrato que assumiu; a agência responde pelo ato ilícito que praticou.</p>'),
])
b += wide(table(['Passo', 'Pergunta', 'Para quê'], [
    ['1 · Vínculo', 'Quem assumiu cada obrigação?', 'Separa quem é parte de quem é terceiro.'],
    ['2 · Conhecimento', 'O terceiro sabia do contrato?', 'Sem conhecimento, não há interferência deliberada.'],
    ['3 · Interferência', 'Ele agiu para provocar o descumprimento?', 'Distingue concorrência normal de interferência ilícita.'],
    ['4 · Dano e nexo', 'A conduta causou prejuízo?', 'Sem dano e nexo, não há indenização.'],
    ['5 · Consequência', 'Por que o terceiro responde?', 'Pelo próprio ato, não pela prestação alheia.'],
], hcls=['', 'conc', 'dif']))
b += chapter('04', 'c4', 'Teste')
b += quiz([
    ('Uma empresa oferece cachê maior a um artista que tem contrato com a concorrente. A oferta, sozinha, faz dela terceira ofensora?', 'Não. A oferta, sozinha, é concorrência. Seria preciso que a empresa soubesse do contrato e agisse para provocar o rompimento, com dano resultante disso.'),
    ('O contrato diz que A deve prestar serviço a B. O concorrente C pode ser obrigado por esse contrato?', 'Não. C não é parte. Se interferir ilicitamente e causar dano, responde por ato próprio, nunca pela prestação que A prometeu.'),
    ('O art. 421-A torna todo contrato civil ou empresarial imune a controle?', 'Não. Cria presunções (paridade, respeito à alocação de riscos, revisão excepcional), mas ressalva regimes especiais e cede diante de elementos concretos.'),
    ('O que significa dizer que o contrato é oponível a terceiros?', 'Que terceiros devem respeitá-lo, embora não sejam obrigados por ele. Quem interfere ilicitamente responde por ato próprio.'),
])
page('aula-02.html', '02', 'Liberdade, força obrigatória e relatividade',
     'Princípios contratuais I: liberdade contratual e seus limites, força obrigatória, relatividade e terceiro ofensor.',
     ['Unidade 2 · Princípios', 'Teoria Geral dos Contratos', 'UFRGS · 2026/2'], 'Liberdade, força', 'e relatividade',
     'A <strong class="conc">liberdade</strong> deixa as partes escolherem o que pactuar; a <strong class="dif">força obrigatória</strong> as obriga a cumprir o pactuado. O vínculo prende só quem contratou, mas quem está de fora não pode sabotá-lo.',
     hero, [('Unidade', '2 · Princípios I'), ('Leitura', '≈ 15 min'), ('Antes', 'Aula 01 · Conceito'), ('Depois', 'Aula 03 · Princípios II')], b,
     ('aula-01.html', '← Aula 01', 'Conceito de contrato'), ('aula-03.html', 'Aula 03 →', 'Função social, boa-fé e equilíbrio'), unit='2')
