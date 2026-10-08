from kit import *

# hero: a quoted word under a lens, pulled into meaning by three context lines
hero = ('<g class="pop" style="--d:.2s"><rect x="440" y="40" width="200" height="80" style="fill:var(--paper);stroke:var(--ink);stroke-width:2"/>'
        '<text x="540" y="90" text-anchor="middle" style="font:600 24px var(--sans);fill:var(--ink)">“AVAL”</text></g>'
        '<path class="draw" style="--d:.5s;stroke:var(--conc);stroke-width:2;fill:none" d="M60 40C200 40 300 80 436 80"/>'
        '<path class="draw" style="--d:.7s;stroke:var(--conc);stroke-width:2;fill:none" d="M60 150C200 150 300 90 436 88"/>'
        '<path class="draw" style="--d:.9s;stroke:var(--dif);stroke-width:2;fill:none" d="M644 80C800 80 880 80 1020 80"/>'
        '<g class="pop" style="--d:1.2s;font:12px var(--mono);letter-spacing:1px">'
        '<text x="60" y="30" style="fill:var(--conc)">OUTRAS CLÁUSULAS</text><text x="60" y="140" style="fill:var(--conc)">CONDUTA · USOS</text>'
        '<text x="1020" y="110" text-anchor="end" style="fill:var(--dif)">SENTIDO JURÍDICO</text></g>'
        '<g class="pop" style="--d:1.5s"><circle cx="1030" cy="80" r="9" style="fill:var(--dif)"/></g>')

# ---- Fig 1: from declaration to meaning (layers)
def layers(k):
    L = [('TEXTO', 'as palavras usadas', 'grey'), ('CONTRATO INTEIRO', 'as outras cláusulas', 'conc'),
         ('CIRCUNSTÂNCIAS', 'negociação, operação, conduta', 'conc'), ('SENTIDO', 'o que foi manifestado', 'dif')]
    o = T(40, 64, 'ART. 112 · DA DECLARAÇÃO AO SENTIDO', 't-small', style='letter-spacing:.1em')
    for i, (a, b, tone) in enumerate(L):
        y = 96 + i * 108
        on = i <= k
        o += G(box(80 + i * 20, y, 440 - i * 40, 84, a, b, tone if on else 'grey', ctx='lay'), 'pop' if on else '', d=.15 * i,
               extra='' if on else ' opacity=".3"')
        if i < 3: o += P(f'M300 {y+84}V{y+104}', 'ink' if i < k else 'thin', m='p-lay%d-i' % k)
    o += G(T(300, 560, ['comece pelo texto', 'leia com o resto', 'e com o que cerca', 'sem vontade secreta'][k], 't-hand', anchor='middle'), 'fade', d=.6)
    return o
aval = (T(40, 64, 'REsp 1.013.976/SP · MÚTUO', 't-small', style='letter-spacing:.1em')
        + G(doc(60, 90, 220, 260, None, lines=9), 'pop', d=.1)
        + G(R(70, 118, 204, 26, 'w-grey ink') + T(82, 136, '“avalista-interveniente”', 't-small'), 'pop', d=.3)
        + G(R(70, 246, 204, 26, 'w-conc ink') + T(82, 264, 'cl. 8.7 · coobrigado', 't-small tc-conc'), 'pop', d=.6)
        + G(lens(170, 260, 40), 'pop', d=.9)
        + P('M290 220C340 220 350 200 380 200', 'c-dif grow', m='p-aval-d', extra=' style="--d:1.1s"')
        + G(box(384, 150, 176, 100, 'COOBRIGADO', 'fica na execução', 'dif', ctx='aval'), 'pop', d=1.3)
        + G(T(300, 420, 'o rótulo sozinho não decide:', 't-hand', anchor='middle') + T(300, 450, 'o contrato inteiro decide', 't-hand', anchor='middle'), 'fade', d=1.5)
        + G(R(40, 490, 520, 60, 'f-ink') + T(300, 526, '“AVAL” FORA DE TÍTULO DE CRÉDITO: RÓTULO IMPRECISO', 't-small t-light', anchor='middle'), 'pop', d=1.7))
quot = (T(40, 64, 'TJSP · CESSÃO DE QUOTAS', 't-small', style='letter-spacing:.1em')
        + P('M60 250H540', 'ink', style='stroke-width:2')
        + G(C(90, 250, 10, 'f-ink') + T(90, 290, 'CESSÃO', 't-small', anchor='middle') + T(90, 308, 'assinada', 't-small', anchor='middle'), 'pop', d=.1)
        + G(C(270, 250, 10, 'f-ink', style='fill:var(--conc)') + T(270, 290, 'ADQUIRENTE', 't-small tc-conc', anchor='middle') + T(270, 308, 'assume a gestão', 't-small', anchor='middle'), 'pop', d=.4)
        + G(C(450, 250, 10, 'f-ink', style='fill:var(--conc)') + T(450, 290, 'CONTRATOS', 't-small tc-conc', anchor='middle') + T(450, 308, 'renovados', 't-small', anchor='middle'), 'pop', d=.7)
        + P('M450 236C400 150 150 150 94 236', 'c-dif grow', m='p-quot-d', extra=' style="--d:1s"')
        + G(T(270, 150, 'lê-se o passado pela conduta', 't-hand', anchor='middle'), 'fade', d=1.3)
        + G(box(40, 360, 520, 100, 'EFEITOS DESDE A CELEBRAÇÃO', 'pedidos principais acolhidos,', 'dif', ctx='quot', sub2='reconvenção rejeitada'), 'pop', d=1.5)
        + T(300, 530, 'a conduta pesou junto com o texto', 't-hand', anchor='middle'))

# ---- Fig 2: the five references of art. 113 §1
crit = [('I', 'CONDUTA POSTERIOR', 'como as partes executaram'), ('II', 'USOS E PRÁTICAS', 'do tipo de negócio'), ('III', 'BOA-FÉ', 'confiança e coerência'),
        ('IV', 'QUEM NÃO REDIGIU', 'se der para identificar'), ('V', 'NEGOCIAÇÃO RAZOÁVEL', 'racionalidade e informação')]
import math
def star(k):
    o = G(R(220, 250, 160, 70, 'f-ink') + T(300, 292, 'CLÁUSULA', 't-small t-light', anchor='middle'), 'pop', d=0)
    pos = [(300, 110), (500, 210), (470, 440), (130, 440), (100, 210)]
    for i, ((n, a, b), (x, y)) in enumerate(zip(crit, pos)):
        on = k == 5 or i == k
        tone = 'dif' if on else 'grey'
        o += P(f'M300 285L{x} {y}', 'c-dif' if on else 'thin', style='stroke-width:1.5' if on else '')
        o += G(C(x, y, 30, f'w-{tone} ink') + T(x, y + 7, n, 't-mid' + (' tc-dif' if on else ''), anchor='middle'), 'pop', d=.1 * i)
        ly = y - 44 if i == 0 else y + 50
        o += G(T(x, ly, a, 't-small' + (' tc-dif' if on else ''), anchor='middle', style='' if on else 'opacity:.45'), 'fade', d=.1 * i)
        if on and k < 5: o += G(T(x, ly + 18, b, 't-small', anchor='middle'), 'fade', d=.4)
    if k == 5:
        o += G(T(300, 572, 'juntos, sem hierarquia', 't-hand', anchor='middle'), 'fade', d=.8)
    return o
regra = (T(40, 64, 'ART. 113, § 2º · O MANUAL DAS PARTES', 't-small', style='letter-spacing:.1em')
         + G(doc(80, 100, 200, 250, 'CONTRATO', lines=9), 'pop', d=.1)
         + G(R(320, 140, 220, 170, 'w-dif ink') + T(334, 172, 'CLÁUSULA DE', 't-small tc-dif') + T(334, 192, 'INTERPRETAÇÃO', 't-small tc-dif')
             + P('M334 216h180M334 240h150M334 264h170M334 288h110', 'thin'), 'pop', d=.5)
         + P('M284 225H316', 'c-dif grow', m='p-regra-d', extra=' style="--d:.8s"')
         + G(box(40, 400, 520, 110, 'AS PARTES PODEM COMBINAR', 'regras de interpretação, de preenchimento', 'dif', ctx='regra', sub2='de lacunas e de integração, dentro da lei'), 'pop', d=1.0))

def jul(tone, b, span, corpo, tese):
    return f'<article class="julgado {tone}"><header><b>{b}</b><span>{span}</span></header><div class="corpo"><p>{corpo}</p></div><div class="tese">{tese}</div></article>'

S = lambda panel, label, h3, body, lcls='': dict(panel=panel, label=label, lcls=lcls, h3=h3, body=body)
b = ''
b += chapter('01', 'c1', 'Da declaração ao sentido', 'O art. 112 manda buscar a intenção que aparece na declaração. Não manda procurar uma vontade que ninguém declarou.')
b += scrolly('Ler em camadas', [(f'p-lay{k}', layers(k), l) for k, l in enumerate(['Texto', 'Contrato inteiro', 'Circunstâncias', 'Sentido'])], [
    S('p-lay0', 'Art. 112', 'Comece pelas palavras', '<p>“Nas declarações de vontade se atenderá mais à intenção nelas consubstanciada do que ao sentido literal da linguagem.” A intenção que conta é a que está <strong>na declaração</strong>. O texto é o ponto de partida e continua sendo a principal prova do que foi combinado.</p>'),
    S('p-lay1', 'O conjunto', 'Leia a cláusula com o resto do contrato', '<p>Uma cláusula isolada pode ter dois sentidos; lida com as outras, costuma ter um só. Um termo técnico usado fora do lugar, uma definição em outra cláusula, a estrutura de pagamentos: tudo isso mostra o que as partes quiseram dizer.</p>', 'conc'),
    S('p-lay2', 'O contexto', 'E com as circunstâncias', '<p>A negociação, a operação econômica e a conduta das partes depois de assinar ajudam a escolher entre sentidos possíveis. O art. 113 manda considerar a boa-fé e os usos do lugar da celebração.</p>', 'conc'),
    S('p-lay3', 'O limite', 'O sentido tem de caber no que foi dito', '<p>O resultado é o sentido jurídico que cabe no que as partes manifestaram. Interpretar não autoriza trocar a declaração por uma intenção secreta, nem inventar uma cláusula que ninguém escreveu.</p>', 'dif'),
])
b += scrolly('Dois casos', [('p-aval', aval, 'Aval ou coobrigação'), ('p-quot', quot, 'Conduta posterior')], [
    S('p-aval', 'REsp 1.013.976/SP', 'Um rótulo não explica a obrigação inteira', '<p>Um sócio assinou um contrato de mútuo como “avalista-interveniente”. Só que aval é instituto de título de crédito, e a cláusula 8.7 do mesmo contrato o descrevia como <strong>coobrigado</strong>.</p><p>O STJ leu o instrumento como um todo e manteve o signatário no polo passivo da execução: ele tinha assumido a obrigação, e o rótulo impreciso não mudava isso. O tribunal interpretou o que estava escrito; não criou uma vontade que não aparecia no contrato.</p>'),
    S('p-quot', 'TJSP · cessão de quotas', 'A conduta posterior resolve uma dúvida', '<p>Numa cessão onerosa de quotas, discutia-se se a eficácia dependia da renovação de contratos administrativos da sociedade. Depois de assinar, a adquirente assumiu a administração, e os contratos foram em boa parte renovados.</p><p>O TJSP concluiu que a cessão produzira efeitos desde a celebração: reformou a sentença, acolheu os pedidos principais e rejeitou a reconvenção. A conduta posterior pesou muito, mas junto com o texto e a operação inteira. Ela não derruba sozinha qualquer condição escrita.</p>', 'dif'),
])
b += chapter('02', 'c2', 'Cinco referências do art. 113', 'Desde 2019, o § 1º lista o que orienta a escolha do sentido. As referências trabalham juntas; nenhuma vem antes das outras por definição.', 'dif')
b += scrolly('Os critérios do § 1º', [(f'p-cr{k}', star(k), crit[k][1] if k < 5 else 'Todos') for k in range(6)] + [('p-regra', regra, '§ 2º')], [
    S('p-cr0', 'Inciso I', 'Conduta posterior', '<p>Vale o sentido confirmado pelo comportamento das partes depois de celebrar o negócio. Como executaram o contrato mostra como o entenderam.</p>', 'dif'),
    S('p-cr1', 'Inciso II', 'Usos, costumes e práticas do mercado', '<p>Vale o sentido que corresponde às práticas daquele tipo de negócio. Um termo pode ter significado técnico estável num setor.</p>'),
    S('p-cr2', 'Inciso III', 'Boa-fé', '<p>Entre dois sentidos possíveis, prefira o que é compatível com a confiança, a lealdade e a coerência entre as partes.</p>'),
    S('p-cr3', 'Inciso IV', 'A parte que não redigiu', '<p>Vale o sentido mais benéfico à parte que não redigiu o dispositivo, <strong>se for possível identificar</strong> quem redigiu. É parente do art. 423, que a Aula 10 trata.</p>', 'conc'),
    S('p-cr4', 'Inciso V', 'A negociação razoável', '<p>Vale o sentido que corresponderia a uma negociação razoável sobre o ponto discutido, inferida das demais cláusulas, da racionalidade econômica das partes e das informações disponíveis na celebração.</p>'),
    S('p-cr5', 'Em conjunto', 'Referências, não degraus', '<p>O parágrafo não cria uma ordem de aplicação. Os critérios se somam para justificar um sentido, e nenhum deles autoriza escolher simplesmente o resultado mais conveniente.</p>', 'dif'),
    S('p-regra', '§ 2º', 'As partes podem escrever as próprias regras', '<p>O contrato pode trazer regras próprias de interpretação, de preenchimento de lacunas e de integração, diferentes das legais. O limite são as normas que as partes não podem afastar.</p>'),
])
b += chapter('03', 'c3', 'Teste', 'Em cada caso, separe o que está escrito, o fato provado e a conclusão jurídica.')
b += quiz([
    ('Uma fiança chama a sócia de “avalista”, mas outra cláusula diz que ela responde solidariamente pelo empréstimo. Qual leitura usar?', 'Leia as cláusulas juntas. Como no REsp 1.013.976/SP, o rótulo isolado não decide se o resto do contrato mostra que ela assumiu a obrigação.'),
    ('Depois de assinar uma cessão, a compradora assume a empresa e as partes passam a agir como se a transferência estivesse feita. Isso prova, sozinho, que uma condição escrita foi afastada?', 'Não. A conduta posterior (art. 113, § 1º, I) se lê junto com a cláusula e o contrato inteiro. No caso do TJSP, foi a combinação desses elementos que sustentou a conclusão.'),
    ('O contrato diz “entrega imediata”, mas prevê pagamento em três etapas e liberação do bem depois da última. Por onde começar?', 'Pela leitura da expressão junto com as outras cláusulas e com as informações disponíveis na celebração. Nem o sentido literal isolado, nem um acordo que não aparece no contrato.'),
    ('O contrato traz uma cláusula dizendo como resolver dúvidas sobre prazos. O juiz pode ignorá-la e aplicar só o art. 113, § 1º?', 'Em regra, não. O § 2º permite que as partes pactuem regras próprias de interpretação e integração, respeitados os limites da lei.'),
])
page('aula-09.html', '09', 'Interpretação: o sentido do acordo',
     'Interpretação dos contratos: arts. 112 e 113 do Código Civil, leitura em contexto, conduta posterior e os critérios do § 1º.',
     ['Unidade 6 · Interpretação', 'Teoria Geral dos Contratos', 'UFRGS · 2026/2'], 'O sentido', 'do acordo',
     'Uma cláusula não se lê sozinha. O <strong class="conc">texto</strong>, as outras cláusulas e as circunstâncias mostram qual <strong class="dif">sentido</strong> as partes deram ao que escreveram.',
     hero, [('Unidade', '6 · Interpretação I'), ('Leitura', '≈ 12 min'), ('Antes', 'Aula 08 · Classificação II'), ('Depois', 'Aula 10 · Regras especiais')], b,
     ('aula-08.html', '← Aula 08', 'Classificação dos contratos II'), ('aula-10.html', 'Aula 10 →', 'Regras especiais de interpretação'), unit='6')
