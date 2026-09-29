from kit import *

# ---------- hero: an operation enters, a binding form leaves ----------
hero = (
    '<path class="draw" d="M0 60H430" style="stroke:var(--conc);stroke-width:3;fill:none"/>'
    '<path class="draw" d="M650 110H1070" style="stroke:var(--dif);stroke-width:3;fill:none"/>'
    '<g class="pop" style="--d:.9s"><rect x="470" y="18" width="140" height="134" style="fill:var(--paper);stroke:var(--ink);stroke-width:1.6"/>'
    '<path d="M492 50h96M492 70h96M492 90h70M492 110h84" style="stroke:var(--ink);opacity:.5"/>'
    '<text x="540" y="140" text-anchor="middle" style="font:500 12px var(--mono);fill:var(--ink)">CONTRATO</text></g>'
    '<g class="pop" style="--d:1.5s;font:12px var(--mono);letter-spacing:1px">'
    '<text x="0" y="44" style="fill:var(--conc)">OPERAÇÃO ECONÔMICA · A RIQUEZA CIRCULA</text>'
    '<text x="1070" y="140" text-anchor="end" style="fill:var(--dif)">FORMA JURÍDICA · O VÍNCULO OBRIGA</text></g>')

# ---------- Fig. 1: the ladder of legal facts ----------
rungs = [('FATO JURÍDICO EM SENTIDO ESTRITO', 'fato da natureza · nascimento, morte'),
         ('ATO-FATO', 'ação humana, vontade irrelevante · caça, posse'),
         ('ATO JURÍDICO EM SENTIDO ESTRITO', 'vontade age, a lei fixa os efeitos · domicílio'),
         ('NEGÓCIO JURÍDICO', 'a vontade escolhe o conteúdo · o CONTRATO')]
def ladder(active):
    o = P('M44 552V70', 's-accent', m='PL-a', extra=' stroke-width="2"')
    o += T(30, 330, 'MAIS ESPAÇO PARA A VONTADE', 't-small', anchor='middle', style='fill:var(--muted)', )
    o = o.replace('<text x="30" y="330"', '<text x="30" y="330" transform="rotate(-90 30 330)"')
    for i, (t, s) in enumerate(rungs):
        y = 452 - i * 118
        x = 78 + i * 22
        w = 500 - i * 22
        on = i == active
        tone = ('conc' if i == 3 else 'dif') if on else 'grey'
        g = box(x, y, w, 96, t, s, tone=tone, ctx=f'ladder{i}')
        if i == 3 and on:
            g += R(x + w - 118, y + 26, 100, 44, 'f-ink') + T(x + w - 68, y + 54, 'CONTRATO', 't-small t-light', anchor='middle')
        o += G(g, 'pop' if on else '', d=.1 if on else None, extra='' if on or i < active else ' opacity=".32"')
    return o.replace('PL-a', 'XX')
lad = []
for k in range(4):
    inner = ladder(k).replace('XX', f'p-lad{k}-a')
    lad.append((f'p-lad{k}', inner, 'Escada dos fatos jurídicos'))

# ---------- Fig. 2: three elements ----------
def speech(x, y, w, label, tone):
    rc = 'w-conc' if tone == 'conc' else 'w-dif'
    return R(x, y, w, 58, rc + ' ink', rx=12) + T(x + w / 2, y + 36, label, f't-mid tc-{tone}', anchor='middle', maxw=w - 16, ctx='speech')
est = (person(110, 330, 'A') + person(490, 330, 'B')
       + G(speech(40, 170, 190, 'PROPOSTA', 'conc') + P('M150 228 L160 262 L182 228', 'w-conc ink'), 'pop', d=.2)
       + G(speech(370, 170, 190, 'ACEITAÇÃO', 'dif') + P('M450 228 L440 262 L420 228', 'w-dif ink'), 'pop', d=.7)
       + P('M232 200C270 200 270 120 300 120', 'c-conc grow', m='p-est-c', extra=' style="--d:.4s"')
       + P('M368 200C330 200 330 120 300 120', 'c-dif grow', m='p-est-d', extra=' style="--d:.9s"')
       + G(C(300, 96, 34, 'f-ink') + T(300, 101, 'ACORDO', 't-small t-light', anchor='middle'), 'pop', d=1.3)
       + T(300, 560, 'DUAS DECLARAÇÕES UNILATERAIS QUE SE ENCONTRAM', 't-small', anchor='middle', style='fill:var(--muted)'))
sub = (box(30, 190, 190, 150, 'PATRIMÔNIO A', 'vende', 'grey', ctx='sub') + box(380, 190, 190, 150, 'PATRIMÔNIO B', 'compra', 'grey', ctx='sub')
       + P('M222 232C290 180 310 180 378 232', 'c-conc grow', m='p-sub-c')
       + T(300, 168, 'BEM · SERVIÇO · USO · CRÉDITO', 't-small tc-conc', anchor='middle')
       + P('M378 300C310 352 290 352 222 300', 'c-dif grow', m='p-sub-d', extra=' style="--d:.6s"')
       + G(coin(300, 338), 'pop', d=1.1) + T(300, 392, 'PREÇO', 't-small tc-dif', anchor='middle')
       + G(R(90, 440, 420, 62, 'f-ink') + T(300, 478, 'CIRCULAÇÃO DE RIQUEZA', 't-mid t-light', anchor='middle'), 'pop', d=1.4)
       + T(300, 560, 'A OPERAÇÃO ECONÔMICA É O ELEMENTO SUBSTANCIAL', 't-small', anchor='middle', style='fill:var(--muted)'))
nor = (R(40, 60, 520, 470, 'f-paper', style='stroke:var(--const);stroke-width:3')
       + T(60, 92, 'ORDENAMENTO JURÍDICO', 't-small', style='letter-spacing:.14em')
       + G(box(170, 200, 260, 110, 'A ⇄ B', 'a operação econômica', 'grey', ctx='nor'), 'fade')
       + G(R(60, 120, 230, 44, 'w-conc ink') + T(74, 148, 'CC 421 · FUNÇÃO SOCIAL', 't-small tc-conc', maxw=210, ctx='nor'), 'pop', d=.3)
       + G(R(310, 120, 230, 44, 'w-dif ink') + T(324, 148, 'CC 421-A · PARIDADE', 't-small tc-dif', maxw=210, ctx='nor'), 'pop', d=.6)
       + G(R(60, 350, 230, 44, 'w-grey ink') + T(74, 378, 'NORMAS COGENTES', 't-small', maxw=210, ctx='nor'), 'pop', d=.9)
       + G(R(310, 350, 230, 44, 'w-grey ink') + T(324, 378, 'CDC · REGIME ESPECIAL', 't-small', maxw=210, ctx='nor'), 'pop', d=1.2)
       + G(T(300, 452, 'a forma jurídica dá força obrigatória', 't-hand', anchor='middle') + T(300, 480, 'e o Direito fixa os limites', 't-hand', anchor='middle'), 'fade', d=1.5)
       + T(300, 568, 'ELEMENTO NORMATIVO', 't-small', anchor='middle', style='fill:var(--muted)'))
exs = [('COMPRA PARA USO', 'necessidade'), ('SEGURO DE UM BEM', 'proteção'), ('SERVIÇO P/ A ATIVIDADE', 'organização'), ('DERIVATIVO', 'aposta no índice')]
esp = T(300, 70, 'TODAS SÃO OPERAÇÕES ECONÔMICAS', 't-small', anchor='middle')
for i, (a, b) in enumerate(exs):
    spec = i == 3
    esp += G(box(90, 100 + i * 104, 420, 84, a, b, 'conc' if spec else 'grey', ctx='esp'), 'pop', d=.15 * i)
    esp += G(T(492, 150 + i * 104, 'ESPECULATIVA' if spec else '', 't-small tc-conc', anchor='end'), 'fade', d=.9)
esp += T(300, 552, 'só uma delas é especulação', 't-hand', anchor='middle')

# ---------- Fig. 3: consumer law ----------
dest = (box(40, 60, 200, 80, 'FORNECEDOR', 'atua no mercado', 'grey', ctx='dest')
        + P('M240 100H340', 'ink', m='p-dest-i') + T(290, 88, 'PRODUTO', 't-small', anchor='middle')
        + box(350, 60, 210, 80, 'ADQUIRENTE', 'PF ou PJ', 'paper', ctx='dest')
        + P('M455 140V200', 'ink') + C(455, 206, 6, 'f-ink')
        + G(P('M455 212C455 260 360 260 330 290', 'c-dif grow', m='p-dest-d')
            + box(60, 290, 270, 110, 'USO PRÓPRIO', 'o bem sai do mercado', 'dif', ctx='dest', sub2='DESTINATÁRIO FINAL · CDC'), '', d=.2)
        + G(P('M455 212V420', 'c-conc grow', m='p-dest-c', extra=' style="--d:.7s"')
            + box(330, 430, 240, 110, 'VOLTA AO MERCADO', 'insumo · revenda · produção', 'conc', ctx='dest', sub2='CONSUMO INTERMEDIÁRIO'), '', d=.7)
        + T(60, 470, 'A PERGUNTA:', 't-small', style='fill:var(--muted)')
        + T(60, 494, 'para que o bem', 't-hand') + T(60, 524, 'foi adquirido?', 't-hand'))
teo = T(40, 64, 'QUEM É DESTINATÁRIO FINAL?', 't-small', style='fill:var(--muted)')
rows = [('FINALISTA', 'destinatário fático e econômico', 'grey', 'mais restritiva'),
        ('MAXIMALISTA', 'basta ser destinatário fático', 'grey', 'mais ampla'),
        ('FINALISMO APROFUNDADO', 'finalista + vulnerabilidade provada', 'dif', 'adotada pelo STJ')]
for i, (a, b, t, c) in enumerate(rows):
    y = 96 + i * 150
    teo += G(box(40, y, 400, 110, a, b, t, ctx='teo', sub2=c.upper()), 'pop', d=.25 * i)
    teo += G(P(f'M460 {y+20}v70', 's-accent' if i == 2 else 'thin', extra=' stroke-width="6"'), 'fade', d=.25 * i)
teo += G(R(470, 390, 90, 44, 'f-ink') + T(515, 417, 'STJ', 't-small t-light', anchor='middle'), 'pop', d=.9)
cas = (box(40, 60, 250, 90, 'AERONAVE', 'comprada por', 'grey', ctx='cas', sub2='administradora de imóveis')
       + P('M165 150V208', 'ink', m='p-cas-i') + box(40, 212, 250, 70, 'USO PRÓPRIO', None, 'dif', ctx='cas')
       + G(C(165, 360, 38, 'w-dif ink') + check(165, 362) , 'pop', d=.5) + T(165, 430, 'CDC SE APLICA', 't-small tc-dif', anchor='middle')
       + box(310, 60, 250, 90, 'PAGAMENTOS', 'contratados por', 'grey', ctx='cas', sub2='vendedora de ingressos')
       + P('M435 150V208', 'ink', m='p-cas-i') + box(310, 212, 250, 70, 'NA ATIVIDADE', None, 'conc', ctx='cas')
       + G(C(435, 360, 38, 'w-conc ink') + check(435, 360, False), 'pop', d=.9) + T(435, 430, 'SEM VULNERABILIDADE: NÃO', 't-small tc-conc', anchor='middle')
       + T(300, 520, 'mesmo critério, fatos diferentes', 't-hand', anchor='middle'))

S = lambda panel, label, h3, body, lcls='': dict(panel=panel, label=label, lcls=lcls, h3=h3, body=body)
body = ''
body += chapter('01', 'c1', 'Onde o contrato se encaixa', 'Os fatos jurídicos vão do que acontece sem ninguém querer até aquilo que as pessoas regulam por vontade própria. O contrato está no último degrau.')
body += scrolly('Os fatos jurídicos', lad, [
    S('p-lad0', 'Degrau 1', 'Fato jurídico em sentido estrito', '<p>Fato da natureza, que produz efeitos jurídicos sem depender de ação humana: o nascimento, a morte, o decurso do tempo.</p>'),
    S('p-lad1', 'Degrau 2', 'Ato-fato', '<p>Exige uma ação humana, mas a vontade não importa para o Direito, só o resultado. Exemplos: a caça, a tomada de posse.</p>'),
    S('p-lad2', 'Degrau 3', 'Ato jurídico em sentido estrito', '<p>Há ação voluntária e consciente, mas os efeitos já vêm prontos da lei. Quem fixa domicílio quer mudar de endereço; as consequências jurídicas, a lei é que define.</p>'),
    S('p-lad3', 'Degrau 4', 'Negócio jurídico', '<p>A vontade escolhe o conteúdo e os efeitos da relação, dentro dos limites que a lei deixa. O contrato é a principal espécie de negócio jurídico. Por isso as regras gerais do direito contratual estão, em boa parte, na Parte Geral do Código Civil.</p>', 'conc'),
])
body += chapter('02', 'c2', 'Os três elementos do contrato', 'O mesmo contrato pode ser lido de três jeitos: como acordo de vontades, como operação econômica e como relação que o Direito reconhece.')
body += scrolly('Três leituras do contrato', [('p-est', est, 'Elemento estrutural'), ('p-sub', sub, 'Elemento substancial'), ('p-esp', esp, 'Operação não é especulação'), ('p-nor', nor, 'Elemento normativo')], [
    S('p-est', 'Elemento estrutural', 'O acordo de vontades', '<p>Estruturalmente, o contrato é um acordo: duas declarações unilaterais, a proposta e a aceitação, que se encontram. É o que faz dele um negócio jurídico <em>bilateral</em> quanto à formação, mesmo quando só uma parte se obriga.</p>', 'conc'),
    S('p-sub', 'Elemento substancial', 'A operação econômica', '<p>Na linguagem comum, contrato é \"o negócio\". Por trás do acordo há uma operação que faz a riqueza circular: bens, serviços, crédito, uso de coisas, riscos. Por isso a função do contrato é a circulação de riqueza.</p><p>Como diz Orlando Gomes, ninguém sobrevive no meio social sem praticar diariamente uma série de contratos.</p>'),
    S('p-esp', 'Um cuidado', 'Operação econômica não é especulação', '<p>Comprar algo para uso próprio, fazer seguro de um bem ou contratar um serviço para tocar uma atividade são operações econômicas, mesmo sem nenhuma aposta ou busca de lucro. Há contratos especulativos, como os derivativos, mas eles são uma parte pequena do todo.</p>'),
    S('p-nor', 'Elemento normativo', 'O contrato no Direito', '<p>A palavra \"contrato\" serve tanto para a operação quanto para sua roupagem jurídica. É a forma jurídica que dá força obrigatória à operação, e é o ordenamento que diz como interpretá-la, executá-la e limitá-la.</p><p>O Código Civil brasileiro não define contrato. O italiano define: é o acordo entre duas ou mais partes para constituir, regular ou extinguir entre elas uma relação jurídica patrimonial (art. 1.321). Onde não há norma cogente, as partes decidem como compor seus interesses (Enzo Roppo). Mas o art. 421 submete a liberdade à função social, e o art. 421-A presume paritários os contratos civis e empresariais, ressalvados os regimes especiais, como o do consumidor.</p>', 'dif'),
])
body += chapter('03', 'c3', 'Quando se aplica o CDC', 'Nem todo contrato é de consumo. O CDC se aplica conforme quem contrata, o que é fornecido e para onde vai o produto ou serviço.')
body += wide(table(['Elemento', 'Quem é', 'Detalhe'], [
    ['Consumidor', 'Pessoa física ou jurídica que adquire ou utiliza produto ou serviço como <strong>destinatária final</strong> (CDC, art. 2º).', 'Equipara-se a consumidor a coletividade que intervém na relação de consumo (art. 2º, parágrafo único).'],
    ['Fornecedor', 'Pessoa física ou jurídica, pública ou privada, nacional ou estrangeira, ou ente despersonalizado, que atua no mercado produzindo, distribuindo ou comercializando produtos ou prestando serviços (art. 3º).', 'O poder público também, quando atua como agente econômico: deve serviços adequados, eficientes, seguros e, se essenciais, contínuos (art. 22).'],
    ['Objeto', 'Produto é qualquer bem, material ou imaterial. Serviço é atividade fornecida no mercado mediante remuneração, inclusive bancária e securitária.', 'Ficam de fora as relações de caráter trabalhista.'],
]))
body += scrolly('Destinação final', [('p-dest', dest, 'Destinação final'), ('p-teo', teo, 'As três correntes'), ('p-cas', cas, 'Dois casos do STJ')], [
    S('p-dest', 'A pergunta central', 'O bem termina no uso ou volta para o mercado?', '<p>O que decide é o que o adquirente faz com o bem ou serviço. Se atende a uma necessidade própria e não é revendido nem usado para produzir o que ele oferece a terceiros, ele é <strong class="dif">destinatário final</strong>, e há relação de consumo.</p><p>Se o bem entra na atividade como insumo, ferramenta, peça ou mercadoria para revenda, o consumo é <strong class="conc">intermediário</strong>. Conta a função econômica real, e não o fato de o bem se desgastar com o uso.</p>'),
    S('p-teo', 'Pessoa jurídica consumidora', 'Três correntes', '<p>O art. 2º menciona a pessoa jurídica, mas quando ela é destinatária final? Para os <strong>finalistas</strong>, só quem retira o bem do mercado de fato e economicamente. Para os <strong>maximalistas</strong>, basta ser destinatário de fato. O <strong class="dif">finalismo aprofundado</strong>, adotado pelo STJ, parte do critério finalista mas o flexibiliza quando a empresa prova vulnerabilidade técnica, jurídica, fática ou econômica diante do fornecedor.</p><p>A razão do cuidado: se todos fossem consumidores, ninguém teria tratamento diferenciado, e a proteção especial do CDC viraria direito comum.</p>'),
    S('p-cas', 'Na jurisprudência', 'Mesmo critério, resultados opostos', '<p>Uma administradora de imóveis comprou uma aeronave. O STJ aplicou o CDC: o avião atendia a uma necessidade própria e não fazia parte do serviço que a empresa vendia.</p><p>Já uma vendedora de ingressos contratou intermediação de pagamentos para operar o negócio. O STJ afastou o CDC: o serviço integrava a atividade, e não houve prova de vulnerabilidade.</p>'),
])
body += wide('<div class="par"><div class="regra"><span class="label">Vulnerabilidade</span>O CDC existe porque reconhece a <strong>vulnerabilidade</strong> do consumidor no mercado (art. 4º, I) e se apoia em transparência, boa-fé, equilíbrio e confiança. Daí os direitos básicos do art. 6º: informação clara, proteção contra práticas e cláusulas abusivas, revisão de prestações desproporcionais ou excessivamente onerosas.</div><div class="excecao"><span class="label">Adesão ≠ consumo</span>Contrato de adesão não é o mesmo que contrato de consumo. Há adesão fora do CDC e relação de consumo em contrato negociado. O Código Civil tem regras próprias para a adesão (arts. 423 e 424).</div></div>')
body += chapter('04', 'c4', 'Teste')
body += quiz([
    ('Uma empresa compra uma máquina para a linha de produção. É destinatária final?', 'Em regra, não. A máquina entra diretamente na produção: é consumo intermediário. Só mudaria se a empresa provasse vulnerabilidade diante do fornecedor (finalismo aprofundado).'),
    ('Uma empresa contrata seguro para o próprio imóvel. Pode ser relação de consumo?', 'Sim. O seguro protege patrimônio próprio e não integra o que a empresa oferece ao mercado.'),
    ('Em que degrau está a fixação de domicílio, e por quê?', 'Ato jurídico em sentido estrito: há vontade de mudar de endereço, mas os efeitos jurídicos vêm prontos da lei.'),
    ('Qual é a diferença entre o elemento estrutural e o substancial do contrato?', 'O estrutural é o acordo de vontades (proposta + aceitação); o substancial é a operação econômica que esse acordo realiza, a circulação de riqueza.'),
    ('Contrato de adesão é sempre contrato de consumo?', 'Não. Adesão é um modo de contratar; consumo depende dos sujeitos, do objeto e da destinação.'),
])
page('aula-01.html', '01', 'Conceito de contrato',
     'Conceito de contrato: negócio jurídico, operação econômica, elemento normativo e o contrato de consumo.',
     ['Unidade 1 · Conceito', 'Teoria Geral dos Contratos', 'UFRGS · 2026/2'], 'Conceito', 'de contrato',
     'Todo contrato tem dois lados: uma <strong class="conc">operação econômica</strong>, que faz a riqueza circular, e uma <strong class="dif">forma jurídica</strong>, que torna essa operação obrigatória.',
     hero, [('Unidade', '1 · Conceito'), ('Leitura', '≈ 15 min'), ('Depois', 'Aula 02 · Princípios I')], body,
     ('index.html', 'Curso', 'Índice'), ('aula-02.html', 'Aula 02 →', 'Liberdade, força e relatividade'), unit='1')
