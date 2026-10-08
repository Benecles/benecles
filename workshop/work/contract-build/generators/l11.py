from kit import *

# hero: a timeline with the crack at the signature, and a later event greyed out
hero = ('<path class="draw" d="M30 90H1050" style="stroke:var(--ink);stroke-width:3;fill:none"/>'
        '<g class="pop" style="--d:.6s"><circle cx="240" cy="90" r="14" style="fill:var(--conc)"/>'
        '<path d="M232 60l10 12l-8 6l10 12" style="stroke:var(--conc);stroke-width:3;fill:none"/></g>'
        '<g class="pop" style="--d:1s;font:12px var(--mono);letter-spacing:1px"><text x="240" y="40" text-anchor="middle" style="fill:var(--conc)">ASSINATURA · O DEFEITO JÁ ESTÁ AQUI</text>'
        '<text x="240" y="130" text-anchor="middle" style="fill:var(--ink)">CLÁUSULA ABUSIVA · LESÃO</text></g>'
        '<g class="pop" style="--d:1.4s;opacity:.4"><circle cx="820" cy="90" r="10" style="fill:var(--paper);stroke:var(--ink);stroke-width:2"/>'
        '<text x="820" y="130" text-anchor="middle" style="font:12px var(--mono);letter-spacing:1px;fill:var(--ink)">FATO POSTERIOR · AULA 12</text></g>')

def scale(tilt, left, right, lsub, rsub, lcls='conc', rcls='dif', extra=''):
    # a balance beam around (300,190); tilt in degrees (positive = left side down)
    o = P('M300 190V420', 'ink', style='stroke-width:3') + P('M240 420h120', 'ink', style='stroke-width:3')
    o += C(300, 190, 7, 'f-ink')
    o += (f'<g style="transform:rotate({-tilt}deg);transform-origin:300px 190px;transition:transform .8s">'
          + P('M100 190H500', 'ink', style='stroke-width:3')
          + P('M100 190l-40 90h80zM500 190l-40 90h80z', 'thin')
          + R(50, 280, 100, 14, f'w-{lcls} ink') + R(450, 280, 100, 14, f'w-{rcls} ink')
          + T(100, 320, left, f't-small tc-{lcls}', anchor='middle') + T(100, 338, lsub, 't-small', anchor='middle')
          + T(500, 320, right, f't-small tc-{rcls}', anchor='middle') + T(500, 338, rsub, 't-small', anchor='middle')
          + extra + '</g>')
    return o

# ---- Fig 1: where is the defect?
when = (T(40, 64, 'QUANDO NASCEU O PROBLEMA?', 't-small', style='letter-spacing:.1em')
        + P('M60 200H540', 'ink', style='stroke-width:2')
        + G(C(150, 200, 12, 'f-ink', style='fill:var(--conc)') + T(150, 240, 'ASSINATURA', 't-small tc-conc', anchor='middle'), 'pop', d=.1)
        + G(C(430, 200, 9, 'f-paper ink') + T(430, 240, 'EXECUÇÃO', 't-small', anchor='middle'), 'pop', d=.3)
        + G(box(40, 300, 250, 130, 'NA ORIGEM', 'cláusula abusiva', 'conc', ctx='when', sub2='lesão (art. 157)') + T(54, 412, 'esta aula', 't-small'), 'pop', d=.6)
        + G(box(310, 300, 250, 130, 'DEPOIS', 'fato superveniente', 'grey', ctx='when', sub2='arts. 317 e 478') + T(324, 412, 'Aulas 12 e 13', 't-small'), 'pop', d=.9)
        + T(300, 510, 'a data do ato questionado decide', 't-hand', anchor='middle'))
def clause(k):
    o = T(40, 64, 'CLÁUSULA ABUSIVA · O ALVO É UMA REGRA', 't-small', style='letter-spacing:.1em')
    o += R(150, 90, 300, 330, 'f-paper ink')
    for i in range(11):
        if i in (5, 6): continue
        o += P(f'M175 {118+i*26}h{250 if i % 4 else 190}', 'thin')
    if k == 0:
        o += G(R(165, 244, 270, 46, 'w-conc ink') + T(300, 272, 'custo sem relação com o fim', 't-small tc-conc', anchor='middle'), 'pop', d=.3)
        o += G(lens(420, 300, 30), 'pop', d=.6)
        o += G(T(300, 470, 'função · finalidade · partes · contexto', 't-hand', anchor='middle'), 'fade', d=.9)
        o += T(300, 510, 'a mesma redação pode ser válida noutro contrato', 't-small', anchor='middle')
    else:
        o += G(R(470, 244, 110, 46, 'w-conc ink', style='opacity:.6') + T(525, 272, 'retirada', 't-small tc-conc', anchor='middle'), 'pop', d=.2)
        o += P('M435 267H466', 'c-conc grow', m='p-cl1-c', extra=' style="--d:.1s"')
        o += G(R(165, 244, 270, 46, 'w-dif', extra=' stroke="none"') + T(300, 272, 'lacuna integrada', 't-small tc-dif', anchor='middle'), 'pop', d=.7)
        o += G(box(40, 450, 250, 100, 'CDC · ART. 51', 'nula de pleno direito;', 'dif', ctx='cl', sub2='o resto do contrato fica'), 'pop', d=1.0)
        o += G(box(310, 450, 250, 100, 'FORA DO CONSUMO', 'boa-fé: retirar e', 'grey', ctx='cl', sub2='integrar (doutrina)'), 'pop', d=1.2)
    return o
les0 = (T(40, 64, 'LESÃO · ART. 157', 't-small', style='letter-spacing:.1em')
        + scale(14, 'PRESTAÇÃO', 'PRESTAÇÃO', 'assumida', 'oposta')
        + G(box(40, 460, 250, 100, 'DESPROPORÇÃO', 'manifesta, pelos valores', 'conc', ctx='les', sub2='da celebração (§ 1º)'), 'pop', d=.6)
        + G(box(310, 460, 250, 100, 'E TAMBÉM', 'premente necessidade', 'conc', ctx='les', sub2='ou inexperiência'), 'pop', d=.9))
les1 = (T(40, 64, 'LESÃO · § 2º · CONSERVAR O NEGÓCIO', 't-small', style='letter-spacing:.1em')
        + scale(0, 'PRESTAÇÃO', 'PRESTAÇÃO', 'assumida', 'oposta + suplemento',
                extra=G(R(470, 250, 60, 30, 'w-dif ink') + T(500, 270, '+', 't-mid tc-dif', anchor='middle'), 'pop', d=.5))
        + G(box(40, 460, 250, 100, 'ANULÁVEL', 'a regra: desfazer', 'conc', ctx='les1', sub2='o negócio'), 'pop', d=.6)
        + G(box(310, 460, 250, 100, 'OU AJUSTAR', 'suplemento suficiente', 'dif', ctx='les1', sub2='ou redução do proveito'), 'pop', d=.9))

# ---- Fig 2: the musical distrato
show = (T(40, 64, 'TJDFT · O DISTRATO DA ARTISTA', 't-small', style='letter-spacing:.1em')
        + scale(18, '35 SHOWS', 'DOMÍNIO', 'jan/2011–mai/2012', 'do site')
        + G(R(50, 356, 100, 60, 'w-conc ink') + T(100, 382, 'MULTA', 't-small tc-conc', anchor='middle') + T(100, 402, '138 SM', 't-small', anchor='middle'), 'pop', d=.6)
        + G(T(430, 110, 'artista inexperiente', 't-hand', anchor='middle'), 'fade', d=.8)
        + G(R(40, 470, 520, 80, 'f-ink') + T(300, 504, 'DISTRATO ANULADO · COBRANÇA DA MULTA IMPROCEDENTE', 't-small t-light', anchor='middle')
            + T(300, 528, 'apelação do empresário desprovida', 't-small t-light', anchor='middle'), 'pop', d=1.1))

def jul(tone, b, span, corpo, tese):
    return f'<article class="julgado {tone}"><header><b>{b}</b><span>{span}</span></header><div class="corpo">{corpo}</div><div class="tese">{tese}</div></article>'

S = lambda panel, label, h3, body, lcls='': dict(panel=panel, label=label, lcls=lcls, h3=h3, body=body)
b = ''
b += chapter('01', 'c1', 'O problema já estava no contrato?', 'Revisar começa por uma data. Se o desequilíbrio nasceu na assinatura, as ferramentas são a cláusula abusiva e a lesão. Se veio depois, são outras.', 'conc')
b += scrolly('Onde está o defeito', [('p-when', when, 'Quando'), ('p-cl0', clause(0), 'Cláusula'), ('p-cl1', clause(1), 'Remédio'), ('p-les0', les0, 'Lesão'), ('p-les1', les1, 'Conservação')], [
    S('p-when', 'A pergunta inicial', 'Quando nasceu o desequilíbrio?', '<p>“Esse contrato é injusto” não identifica causa nenhuma. A primeira pergunta é temporal: o problema estava no ato quando ele foi assinado, ou surgiu durante a execução?</p><p>Cada ato tem sua própria data. Um distrato assinado um ano depois do contrato original é examinado pela data do distrato.</p>', 'conc'),
    S('p-cl0', 'Cláusula abusiva', 'O alvo é uma regra do contrato', '<p>Aqui o ataque vai contra uma cláusula, muitas vezes acessória, que no contexto desequilibra as posições ou frustra expectativas legítimas. O exame olha para a função da cláusula, a finalidade do contrato, a condição das partes e as circunstâncias. Por isso a mesma redação pode ser abusiva num contrato e razoável em outro.</p>', 'conc'),
    S('p-cl1', 'O remédio', 'Retirar a cláusula e preencher o espaço', '<p>No consumo, o art. 51 do CDC declara nulas de pleno direito as cláusulas abusivas que lista, e o contrato continua, salvo se a integração deixar ônus excessivo para uma das partes.</p><p>Fora do consumo, não há lista equivalente no Código Civil. A doutrina usa a boa-fé objetiva para retirar a cláusula e integrar a lacuna, respeitando a intenção comum. É uma construção doutrinária, e vale dizer isso na prova.</p>', 'dif'),
    S('p-les0', 'Art. 157', 'Lesão: a troca inteira desequilibrada', '<p>Há lesão quando alguém, <strong>sob premente necessidade ou por inexperiência</strong>, se obriga a prestação <strong>manifestamente desproporcional</strong> ao valor da prestação oposta. Os dois elementos são necessários.</p><p>A desproporção se mede pelos valores vigentes quando o negócio foi celebrado (§ 1º). Comparar com o mercado de hoje não prova lesão.</p>', 'conc'),
    S('p-les1', '§ 2º', 'Anular ou salvar o negócio', '<p>O negócio lesivo é anulável. Mas a anulação não é decretada se for oferecido suplemento suficiente, ou se a parte favorecida concordar em reduzir o proveito. A lei prefere reequilibrar a desfazer.</p><p>O prazo para pedir a anulação é de quatro anos, contado do dia em que o negócio foi celebrado (art. 178, II).</p>', 'dif'),
])
b += wide(table(['', 'Cláusula abusiva', 'Lesão · art. 157'], [
    ['O que se ataca', 'Uma regra do contrato que, no contexto, desequilibra as posições.', 'A prestação assumida, manifestamente desproporcional à oposta.'],
    ['O que provar', 'Texto e função da cláusula, finalidade, condição das partes, circunstâncias.', 'Desproporção manifesta na data do negócio e necessidade premente ou inexperiência.'],
    ['Consequência', 'No CDC, nulidade da cláusula (art. 51). Fora dele, retirada e integração pela boa-fé.', 'Anulabilidade, evitável por suplemento ou redução do proveito (§ 2º).'],
], hcls=['', 'conc', 'dif']))
b += chapter('02', 'c2', 'O distrato da artista', 'Um caso em que o desequilíbrio estava no acordo de saída, e não no contrato original.')
b += scrolly('A balança do distrato', [('p-show', show, 'TJDFT')], [
    S('p-show', 'TJDFT · Apelação 20130111161742APC · 2014', 'Trinta e cinco shows por um domínio de site', '<p>Um contrato de atividade musical começou em 2009. No distrato de 2010, a artista se obrigou a fazer 35 apresentações entre janeiro de 2011 e maio de 2012; o empresário, a transferir o domínio do site. Se qualquer obrigação fosse descumprida, a multa era de 138 salários mínimos.</p><p>Depois de três shows, o empresário cobrou a multa e a artista alegou lesão em reconvenção. A 6ª Turma Cível manteve a anulação do distrato, apontando a inexperiência da artista e a desproporção entre as obrigações e a penalidade. Sem distrato, a cobrança caiu.</p><p>O problema estava na formação do distrato, não numa crise durante a execução. E o acórdão não fixou nenhum percentual que, sozinho, caracterize lesão.</p>'),
])
b += chapter('03', 'c3', 'Teste', 'Localize o defeito antes de escolher a prova.')
b += quiz([
    ('Um contrato de serviços empresariais transfere ao cliente um custo sem relação clara com a finalidade do acordo. O que apurar antes de chamar a cláusula de abusiva?', 'A função da cláusula, a finalidade do negócio, a condição das partes e as circunstâncias. Se houver relação de consumo, testar também o art. 51 do CDC.'),
    ('Uma pessoa inexperiente aceitou prestação manifestamente desproporcional. Anos depois, o preço de mercado mudou muito. Que data mede a desproporção?', 'A da celebração do negócio (art. 157, § 1º).'),
    ('O contrato era equilibrado na assinatura; anos depois, um fato imprevisível tornou uma prestação muito onerosa. Lesão?', 'Não. A causa é posterior. Lesão exige desproporção e necessidade ou inexperiência no momento de contratar. Veja a Aula 12.'),
    ('Provada a lesão, a parte favorecida oferece complementar o preço. O juiz deve anular mesmo assim?', 'Não, se o suplemento for suficiente (art. 157, § 2º). O mesmo vale se ela concordar em reduzir o próprio proveito.'),
    ('No caso da artista, por que a quantidade de shows e a multa importavam?', 'Porque foram comparadas com a obrigação do empresário, a transferência do domínio do site. Somada à inexperiência da artista, a desproporção levou à anulação do distrato.'),
])
page('aula-11.html', '11', 'Revisão: desequilíbrio na formação',
     'Revisão dos contratos I: cláusulas abusivas e lesão (art. 157), com o caso do distrato musical.',
     ['Unidade 7 · Revisão', 'Teoria Geral dos Contratos', 'UFRGS · 2026/2'], 'Desequilíbrio', 'na origem',
     'Quando a desproporção nasce na assinatura, há dois suspeitos: uma <strong class="conc">cláusula abusiva</strong> ou a <strong class="conc">lesão</strong>. Cada um pede uma prova diferente e tem um remédio diferente.',
     hero, [('Unidade', '7 · Revisão I'), ('Leitura', '≈ 12 min'), ('Antes', 'Aula 10 · Regras especiais'), ('Depois', 'Aula 12 · Fato superveniente')], b,
     ('aula-10.html', '← Aula 10', 'Regras especiais de interpretação'), ('aula-12.html', 'Aula 12 →', 'O que mudou na execução'), unit='7')
