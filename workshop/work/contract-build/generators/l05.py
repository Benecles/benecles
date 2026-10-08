from kit import *

hero = ('<path class="draw" d="M20 70H500" style="stroke:var(--conc);stroke-width:3;fill:none"/>'
        '<path class="draw" d="M1060 110H580" style="stroke:var(--dif);stroke-width:3;fill:none"/>'
        '<g class="pop" style="--d:1s"><path d="M500 70C560 70 520 110 580 110" style="stroke:var(--ink);stroke-width:3;fill:none"/><circle cx="540" cy="90" r="9" style="fill:var(--ink)"/></g>'
        '<g class="pop" style="--d:1.5s;font:12px var(--mono);letter-spacing:1px"><text x="20" y="50" style="fill:var(--conc)">PROPOSTA · ART. 427</text>'
        '<text x="1060" y="146" text-anchor="end" style="fill:var(--dif)">ACEITAÇÃO · ART. 431</text>'
        '<text x="540" y="146" text-anchor="middle" style="fill:var(--ink)">CONTRATO</text></g>')

def env(x, y, cls='f-paper ink', label=None, lcls='t-small'):
    o = R(x, y, 64, 42, cls) + P(f'M{x} {y}l32 22 32-22', 'ink')
    if label: o += T(x + 32, y + 62, label, lcls, anchor='middle')
    return o

req = (T(40, 64, 'REQUISITOS DA PROPOSTA', 't-small', style='letter-spacing:.1em')
       + G(box(100, 90, 460, 90, 'FIRMEZA', 'vontade séria de contratar', 'conc', ctx='req') + R(40, 118, 34, 34, 'f-paper ink') + check(57, 135), 'pop', d=.2)
       + G(box(100, 200, 460, 90, 'COMPLETUDE', 'elementos essenciais do contrato', 'conc', ctx='req') + R(40, 228, 34, 34, 'f-paper ink') + check(57, 245), 'pop', d=.5)
       + G(box(100, 310, 460, 90, 'DETERMINABILIDADE', 'basta um "aceito" para concluir', 'conc', ctx='req', sub2='(adequação formal)') + R(40, 338, 34, 34, 'f-paper ink') + check(57, 355), 'pop', d=.8)
       + G(R(40, 440, 520, 110, 'f-ink') + T(300, 480, 'ART. 427', 't-mid t-light', anchor='middle')
           + T(300, 508, 'a proposta obriga, salvo se o contrário resultar', 't-small t-light', anchor='middle')
           + T(300, 528, 'dos termos, da natureza do negócio ou das circunstâncias', 't-small t-light', anchor='middle'), 'pop', d=1.2))
joke = (person(150, 180, None) + person(450, 180, None)
        + G(R(40, 60, 250, 70, 'w-conc ink', rx=14) + T(165, 90, '"vendo a casa', 't-serif', anchor='middle') + T(165, 114, 'por 10 mil!"', 't-serif', anchor='middle'), 'pop', d=.2)
        + G(T(300, 150, 'haha', 't-hand', anchor='middle') + T(360, 120, 'haha', 't-hand', anchor='middle') + T(250, 190, 'haha', 't-hand', anchor='middle'), 'fade', d=.6)
        + G(box(40, 360, 250, 90, 'FIRMEZA', 'o contexto afasta', 'conc', ctx='joke', sub2='a vontade de contratar') + check(262, 405, False), 'pop', d=1.0)
        + G(box(310, 360, 250, 90, 'RESULTADO', 'não há proposta,', 'ink', ctx='joke', sub2='logo não há contrato'), 'pop', d=1.3)
        + T(300, 520, 'preço e objeto não bastam', 't-hand', anchor='middle'))
cases428 = [('I', 'PRESENTE, SEM PRAZO', 'não aceita de imediato', 'telefone conta como presença'),
            ('II', 'AUSENTE, SEM PRAZO', 'passou tempo suficiente', 'para a resposta chegar'),
            ('III', 'AUSENTE, COM PRAZO', 'resposta não expedida', 'dentro do prazo'),
            ('IV', 'RETRATAÇÃO', 'chegou antes da proposta', 'ou junto com ela')]
c428 = T(40, 64, 'ART. 428 · A PROPOSTA DEIXA DE OBRIGAR', 't-small', style='letter-spacing:.1em')
for i, (n, a, b1, b2) in enumerate(cases428):
    y = 92 + i * 118
    c428 += G(C(62, y + 44, 22, 'f-ink') + T(62, y + 50, n, 't-small t-light', anchor='middle')
              + box(100, y, 460, 92, a, b1, 'grey', ctx='c428', sub2=b2), 'pop', d=.2 + .25 * i)
pub = (T(150, 64, 'CÓDIGO CIVIL', 't-mid', anchor='middle') + T(450, 64, 'CDC', 't-mid tc-conc', anchor='middle') + P('M300 80V560', 'thin dash')
       + G(box(40, 100, 220, 120, 'ART. 429', 'oferta ao público vale', 'grey', ctx='pub', sub2='como proposta'), 'pop', d=.2)
       + G(box(40, 240, 220, 120, 'REVOGAÇÃO', 'pela mesma via, se', 'grey', ctx='pub', sub2='ressalvada na oferta'), 'pop', d=.4)
       + G(box(40, 380, 220, 120, 'ESTOQUE', 'em regra, oferta sob', 'grey', ctx='pub', sub2='reserva de estoque'), 'pop', d=.6)
       + G(box(340, 100, 220, 120, 'ART. 30', 'publicidade precisa', 'conc', ctx='pub', sub2='obriga e integra'), 'pop', d=.8)
       + G(box(340, 240, 220, 120, 'ART. 35', 'recusa: exigir, trocar', 'conc', ctx='pub', sub2='ou desfazer + danos'), 'pop', d=1.0)
       + G(box(340, 380, 220, 120, 'ESTOQUE', 'o fornecedor responde', 'conc', ctx='pub', sub2='(vulnerabilidade)'), 'pop', d=1.2))
swap = (C(120, 150, 34, 'f-ink', style='fill:var(--conc)') + T(120, 157, 'A', 't-mid t-light', anchor='middle')
        + C(480, 150, 34, 'f-ink', style='fill:var(--dif)') + T(480, 157, 'B', 't-mid t-light', anchor='middle')
        + P('M160 130H440', 'c-conc grow', m='p-swap-c') + T(300, 118, 'PROPOSTA · R$ 100, ENTREGA DIA 10', 't-small tc-conc', anchor='middle')
        + P('M440 176H160', 'c-dif grow', m='p-swap-d', extra=' style="--d:.5s"') + T(300, 206, '"ACEITO, MAS ENTREGA DIA 20"', 't-small tc-dif', anchor='middle')
        + G(box(80, 270, 440, 110, 'NOVA PROPOSTA', 'aceitação com modificação', 'mix', ctx='swap', sub2='(ou fora do prazo) · art. 431'), 'pop', d=1.0)
        + G(T(300, 450, 'os papéis se invertem:', 't-hand', anchor='middle') + T(300, 480, 'agora é A quem aceita ou não', 't-hand', anchor='middle'), 'fade', d=1.3))
exp = (T(40, 64, 'ENTRE AUSENTES · QUANDO SE FORMA?', 't-small', style='letter-spacing:.1em')
       + P('M60 250H560', 'ink', style='stroke-width:2')
       + G(env(70, 150, 'w-dif ink', 'B ESCREVE'), 'pop', d=.1)
       + G(env(220, 150, 'w-dif ink') + P('M252 230V250', 'c-dif'), 'pop', d=.3) + G(C(252, 250, 10, 'f-ink', style='fill:var(--dif)'), 'pop', d=.6)
       + T(252, 290, 'EXPEDIÇÃO', 't-mid tc-dif', anchor='middle') + T(252, 314, 'art. 434 · a regra', 't-small', anchor='middle')
       + G(env(370, 150, 'f-paper ink') + C(402, 250, 8, 'f-paper ink'), 'pop', d=.8) + T(402, 290, 'RECEPÇÃO', 't-small', anchor='middle')
       + G(C(520, 250, 8, 'f-paper ink') + lens(520, 180, 20), 'pop', d=1.0) + T(520, 290, 'COGNIÇÃO', 't-small', anchor='middle')
       + G(box(40, 370, 520, 170, 'EXCEÇÕES (ART. 434)', '• retratação da aceitação que chega antes (art. 433)', 'grey', ctx='exp', sub2='• proponente se comprometeu a esperar'), 'pop', d=1.3)
       + T(54, 510, '• aceitação que não chega no prazo combinado', 't-small'))
sil = (G(R(200, 80, 200, 80, 'f-paper ink', rx=20) + T(300, 132, '. . .', 't-big', anchor='middle'), 'pop', d=.1)
       + T(300, 196, 'EM REGRA, QUEM CALA NÃO ACEITA', 't-small', anchor='middle')
       + G(box(40, 240, 250, 110, 'COSTUME', 'não se costuma', 'dif', ctx='sil', sub2='aceitar expressamente'), 'pop', d=.4)
       + T(300, 228, 'OU', 't-mid', anchor='middle')
       + G(box(310, 240, 250, 110, 'DISPENSA', 'o proponente', 'dif', ctx='sil', sub2='dispensou a resposta'), 'pop', d=.7)
       + P('M165 350C165 400 300 390 300 420M435 350C435 400 300 390 300 420', 'c-dif grow', extra=' style="--d:1s"')
       + G(box(100, 430, 400, 90, 'E A RECUSA NÃO CHEGA A TEMPO', '→ contrato formado (art. 432)', 'ink', ctx='sil'), 'pop', d=1.3))
def race(win):
    o = T(40, 64, 'A CORRIDA DA RETRATAÇÃO', 't-small', style='letter-spacing:.1em')
    o += P('M60 200H520', 'ink', style='stroke-width:2') + P('M60 340H520', 'ink', style='stroke-width:2') + P('M520 150V390', 'ink', style='stroke-width:4')
    o += T(530, 140, 'DESTINATÁRIO', 't-small', anchor='end')
    a, r = (380, 470) if win else (470, 380)
    o += P(f'M70 181H{a-74}', 'c-conc grow') + P(f'M70 321H{r-74}', 'c-dif grow', extra=' style="--d:.2s"')
    o += G(env(a - 70, 160, 'w-conc ink'), 'pop', d=.3) + T(80, 190, 'PROPOSTA', 't-small tc-conc')
    o += G(env(r - 70, 300, 'w-dif ink'), 'pop', d=.3) + T(80, 330, 'RETRATAÇÃO', 't-small tc-dif')
    msg = ('RETRATAÇÃO CHEGOU PRIMEIRO', 'a proposta não obriga (428, IV)') if win else ('PROPOSTA CHEGOU PRIMEIRO', 'a retratação não a desfaz')
    o += G(box(60, 430, 480, 90, msg[0], msg[1], 'dif' if win else 'conc', ctx='race'), 'pop', d=.9)
    return o
S = lambda panel, label, h3, body, lcls='': dict(panel=panel, label=label, lcls=lcls, h3=h3, body=body)
b = ''
b += chapter('01', 'c1', 'A proposta', 'Quem faz uma proposta de verdade fica vinculado a ela, nos limites do que declarou (art. 427).', 'conc')
b += scrolly('A proposta', [('p-req', req, 'Requisitos'), ('p-joke', joke, 'A brincadeira'), ('p-428', c428, 'Art. 428'), ('p-pub', pub, 'Oferta ao público')], [
    S('p-req', 'Declaração receptícia', 'O que é a proposta', '<p>A proposta é uma declaração unilateral de vontade <strong>receptícia</strong>: parte do proponente e precisa chegar ao destinatário. Deve permitir que um simples \"aceito\" forme o contrato, sem nova negociação.</p><p>Seus requisitos são três. <strong>Firmeza</strong>: vontade séria de contratar. <strong>Completude</strong>: os elementos essenciais e os que as partes tornaram essenciais. <strong>Determinabilidade</strong>, ou adequação formal: conteúdo definido o bastante para que a aceitação conclua o negócio.</p>', 'conc'),
    S('p-joke', 'Caso', 'A proposta em tom de brincadeira', '<p>Num jantar de comemoração, alguém oferece, rindo, um bem valioso por uma fração do preço. Todos riem, ninguém fala em condições. No dia seguinte, a outra pessoa aparece para fechar a compra.</p><p>Não há contrato: faltou <strong>firmeza</strong>. O art. 427 afasta a força obrigatória quando as circunstâncias mostram o contrário. Uma declaração completa sem vontade séria não é proposta.</p>'),
    S('p-428', 'Art. 428', 'Quando a proposta deixa de obrigar', '<p>O art. 428 lista quatro casos: <strong>(I)</strong> feita sem prazo a pessoa presente, não foi aceita de imediato; <strong>(II)</strong> feita sem prazo a pessoa ausente, passou tempo suficiente para a resposta chegar; <strong>(III)</strong> feita a ausente com prazo, a resposta não foi expedida dentro dele; <strong>(IV)</strong> a retratação chegou ao destinatário antes da proposta ou junto com ela.</p><p>\"Presente\" e \"ausente\" se referem ao meio de comunicação, não à distância: numa ligação telefônica, a resposta deve ser imediata.</p>'),
    S('p-pub', 'Oferta ao público', 'Código Civil × CDC', '<p>A oferta ao público vale como proposta quando traz os elementos essenciais, salvo se as circunstâncias ou os usos indicarem o contrário, e só pode ser revogada pela mesma via se essa faculdade foi ressalvada (art. 429).</p><p>No CDC, a regra é mais dura: toda informação ou publicidade suficientemente precisa obriga o fornecedor e integra o contrato (art. 30); se ele se recusar a cumprir, o consumidor pode exigir o cumprimento forçado, aceitar produto equivalente ou desfazer o contrato com perdas e danos (art. 35). E se o estoque acabar? No CDC, o fornecedor responde; no Código Civil, em geral se entende a oferta como feita sob reserva de estoque.</p>'),
])
b += chapter('02', 'c2', 'A aceitação', 'A aceitação também é declaração receptícia, e precisa concordar exatamente com a proposta.', 'dif')
b += scrolly('A aceitação', [('p-swap', swap, 'Nova proposta'), ('p-exp', exp, 'Teoria da expedição'), ('p-sil', sil, 'O silêncio'), ('p-race1', race(True), 'Retratação a tempo'), ('p-race2', race(False), 'Retratação tardia')], [
    S('p-swap', 'Art. 431', 'Aceitação com modificações', '<p>Se a aceitação chegar fora do prazo ou trouxer adições, restrições ou modificações, vale como <strong>nova proposta</strong> (art. 431), e os papéis se invertem: agora é o primeiro proponente quem decide se aceita.</p><p>Não confunda com o art. 430: se a aceitação foi enviada a tempo, mas chegou tarde por um imprevisto, o proponente deve avisar o aceitante imediatamente, sob pena de responder por perdas e danos.</p>'),
    S('p-exp', 'Art. 434', 'Entre ausentes: a expedição', '<p>Entre ausentes, o contrato se forma quando a aceitação é <strong>expedida</strong>. É a teoria da expedição. Outras teorias exigiriam a chegada da aceitação (recepção) ou que o proponente tomasse conhecimento dela (cognição).</p><p>O próprio art. 434 traz três exceções: se houver retratação da aceitação (art. 433), se o proponente se comprometeu a esperar a resposta, ou se a aceitação não chegar no prazo combinado. O contrato se considera celebrado no lugar em que foi proposto (art. 435).</p>', 'dif'),
    S('p-sil', 'Art. 432', 'O silêncio', '<p>Em regra, quem cala não aceita. O silêncio só forma o contrato quando não é costume haver aceitação expressa naquele tipo de negócio, ou quando o proponente a dispensou, desde que a recusa não chegue a tempo.</p>'),
    S('p-race1', 'Retratação', 'Retirar a proposta a tempo', '<p>A proposta pode ser retirada, mas só se a retratação chegar ao destinatário antes dela ou junto com ela (art. 428, IV). O que conta é a chegada, não o envio.</p>'),
    S('p-race2', 'Retratação', 'Quando a retratação chega tarde', '<p>Se a proposta chegou primeiro, a retratação não a desfaz. A mesma lógica vale para a aceitação: sua retratação precisa chegar ao proponente antes dela ou junto com ela (art. 433); se a aceitação chegou primeiro, o contrato já está formado.</p>'),
])
b += chapter('03', 'c3', 'Teste')
b += quiz([
    ('A oferta foi feita por telefone, sem prazo, e aceita duas horas depois. Há contrato?', 'Não. Telefone conta como presença (art. 428, I); sem aceitação imediata, a proposta caducou. A resposta tardia vale, no máximo, como nova proposta.'),
    ('A resposta aceita o preço, mas exige entrega em outra data. Houve aceitação?', 'Não. Mudar a data é modificar a proposta: a resposta vale como nova proposta (art. 431).'),
    ('A aceitação foi enviada no último dia, mas o proponente tinha se comprometido a esperar a resposta. Quando se forma o contrato?', 'Não basta a expedição: o compromisso de esperar é exceção (art. 434, II). O contrato se forma quando a aceitação chegar, dentro do prazo.'),
    ('A proposta dispensou expressamente a resposta. O silêncio basta?', 'Sim. O art. 432 exige costume de não haver aceitação expressa ou dispensa pelo proponente; aqui houve dispensa, então basta que a recusa não chegue a tempo.'),
    ('Quais são os três requisitos da proposta?', 'Firmeza, completude e determinabilidade (adequação formal).'),
])
page('aula-05.html', '05', 'Proposta e aceitação',
     'Formação do contrato: requisitos da proposta, art. 428, oferta ao público, aceitação, teoria da expedição, silêncio e retratação.',
     ['Unidade 3 · Formação', 'Teoria Geral dos Contratos', 'UFRGS · 2026/2'], 'Proposta', 'e aceitação',
     'O contrato se forma quando uma <strong class="conc">proposta</strong> séria encontra uma <strong class="dif">aceitação</strong> que corresponde a ela. Prazos, meios de comunicação e o contexto decidem se isso aconteceu.',
     hero, [('Unidade', '3 · Formação II'), ('Leitura', '≈ 14 min'), ('Antes', 'Aula 04 · Tratativas'), ('Depois', 'Aula 06 · Incidentes')], b,
     ('aula-04.html', '← Aula 04', 'Tratativas'), ('aula-06.html', 'Aula 06 →', 'Incidentes da formação'), unit='3')
