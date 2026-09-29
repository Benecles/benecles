import re, html as H
OUT = "/Users/benecles/Documents/Codex/2026-09-05/okay-couple-things-so-first-of/work/study-lab-publish/courses/teoria-geral-dos-contratos/"
p1 = open(OUT + 'revisao-p1.html').read()
head = p1[:p1.index('<style>')]
head = head.replace('<title>Revisão para a P1 · Teoria Geral dos Contratos</title>', '<title>Artigos do curso · Teoria Geral dos Contratos</title>')
head = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="Índice dos artigos do Código Civil, do CDC e do CPC usados em Teoria Geral dos Contratos: a regra em uma linha e as aulas que a explicam.">', head)

CC = [
 ('107', 'Liberdade de forma: a declaração de vontade só depende de forma especial quando a lei exigir.', ['08']),
 ('108', 'Escritura pública para negócios sobre direitos reais em imóveis acima de 30 salários mínimos.', ['08']),
 ('109', 'Forma convencional: se as partes combinarem que o negócio só vale com instrumento público, ele é da substância do ato.', ['08']),
 ('112', 'Atende-se mais à intenção consubstanciada na declaração do que ao sentido literal da linguagem.', ['09']),
 ('113', 'Interpretação conforme a boa-fé e os usos; § 1º traz cinco referências; § 2º permite regras de interpretação pactuadas.', ['03', '09', '10']),
 ('114', 'Negócios benéficos e renúncia se interpretam estritamente.', ['07', '10']),
 ('157', 'Lesão: premente necessidade ou inexperiência + prestação manifestamente desproporcional, pelos valores da celebração; § 2º permite conservar o negócio.', ['03', '11']),
 ('178, II', 'Prazo decadencial de quatro anos para anular por lesão, contado da celebração.', ['11']),
 ('187', 'Abuso do direito: exceder manifestamente os limites da boa-fé, dos bons costumes ou do fim econômico e social é ato ilícito.', ['03', '04']),
 ('234', 'Coisa certa perdida sem culpa antes da tradição: a obrigação fica resolvida para ambas as partes; com culpa, equivalente + perdas e danos.', ['15']),
 ('246', 'Coisa incerta: antes da escolha, o devedor não pode alegar perda ou deterioração, nem por força maior.', ['15']),
 ('286–298', 'Cessão de crédito: transfere o crédito, com os acessórios, salvo ajuste diferente.', ['14']),
 ('290', 'A cessão de crédito só vale contra o devedor depois de notificada a ele.', ['14']),
 ('295', 'Na cessão onerosa, o cedente responde pela existência do crédito.', ['07']),
 ('299', 'Assunção de dívida exige consentimento expresso do credor; o silêncio após o prazo assinado vale como recusa.', ['14']),
 ('300', 'Na assunção de dívida, as garantias especiais dadas pelo devedor original se extinguem, salvo assentimento dele.', ['14']),
 ('317', 'Motivo imprevisível + desproporção manifesta entre o valor devido e o da execução: o juiz corrige o valor, a pedido da parte.', ['03', '12', '15']),
 ('392', 'Nos contratos benéficos, responde por culpa quem é favorecido e só por dolo quem não é.', ['07']),
 ('393', 'Caso fortuito ou força maior: o devedor não responde pelos prejuízos, salvo se expressamente assumiu esse risco.', ['17']),
 ('394–396', 'Mora: atraso imputável; sem fato ou omissão imputável ao devedor, não há mora (396).', ['17']),
 ('395, p. ú.', 'Se a prestação, pela mora, se tornar inútil, o credor pode enjeitá-la e exigir perdas e danos.', ['17']),
 ('397', 'Obrigação a termo: a mora é automática; sem termo, depende de interpelação.', ['17']),
 ('399', 'O devedor em mora responde pela impossibilidade, mesmo por fortuito, salvo se provar ausência de culpa ou que o dano ocorreria de todo modo.', ['15']),
 ('416', 'A cláusula penal pode ser exigida sem prova de prejuízo.', ['06']),
 ('417–419', 'Arras confirmatórias: descumpriu quem deu, perde; quem recebeu, devolve + equivalente; valem como indenização mínima.', ['06']),
 ('420', 'Arras penitenciais: com direito de arrependimento, função só indenizatória, sem indenização suplementar.', ['06']),
 ('421', 'A liberdade contratual é exercida nos limites da função social do contrato; nas relações privadas, intervenção mínima e revisão excepcional.', ['01', '02', '03']),
 ('421-A', 'Contratos civis e empresariais presumem-se paritários e simétricos até prova em contrário.', ['02', '08']),
 ('422', 'Os contratantes devem guardar probidade e boa-fé na conclusão e na execução do contrato.', ['03', '04']),
 ('423', 'Na adesão, cláusulas ambíguas ou contraditórias se interpretam a favor do aderente.', ['02', '08', '10']),
 ('424', 'Na adesão, é nula a renúncia antecipada do aderente a direito resultante da natureza do negócio.', ['02', '08']),
 ('425', 'É lícito celebrar contratos atípicos, observadas as normas gerais do Código.', ['08']),
 ('427', 'A proposta obriga o proponente, salvo se o contrário resultar dos termos, da natureza do negócio ou das circunstâncias.', ['05']),
 ('428', 'Quando a proposta deixa de obrigar: presente sem aceitação imediata, ausente após tempo suficiente, prazo expirado, retratação que chega antes ou junto.', ['05']),
 ('429', 'Oferta ao público vale como proposta quando contém os requisitos essenciais; revogável pela mesma via, se ressalvado.', ['05']),
 ('430', 'Aceitação que chega tarde por imprevisto: o proponente deve avisar imediatamente, sob pena de perdas e danos.', ['05']),
 ('431', 'Aceitação fora do prazo, com adições, restrições ou modificações, vale como nova proposta.', ['05']),
 ('432', 'Silêncio forma o contrato só se não for costume a aceitação expressa ou se o proponente a dispensou, e a recusa não chegar a tempo.', ['05']),
 ('433', 'A aceitação é inexistente se a retratação chegar antes dela ou junto com ela.', ['05']),
 ('434', 'Entre ausentes, o contrato se forma com a expedição da aceitação, salvo as exceções do artigo.', ['05']),
 ('435', 'O contrato se reputa celebrado no lugar em que foi proposto.', ['05']),
 ('436–438', 'Estipulação em favor de terceiro: estipulante e beneficiário podem exigir; substituição do beneficiário se reservada.', ['06']),
 ('439–440', 'Promessa de fato de terceiro: quem prometeu responde por perdas e danos; nada deve se o terceiro se obrigou e descumpriu.', ['06']),
 ('441–446', 'Vícios redibitórios: defeito oculto em contrato comutativo; redibir ou abater; prazos de 30 dias (móvel) e 1 ano (imóvel).', ['03', '07']),
 ('447–457', 'Evicção: nos contratos onerosos, o alienante responde pela perda do bem por direito anterior de terceiro (456 revogado).', ['07']),
 ('458–461', 'Contratos aleatórios: risco de existência (458), de quantidade (459), coisa exposta a risco (460); anulação por dolo (461).', ['07']),
 ('462–466', 'Contrato preliminar: requisitos do definitivo exceto a forma; exigir a celebração, suprimento judicial, perdas e danos; promessa unilateral.', ['04', '06']),
 ('467–471', 'Contrato com pessoa a declarar: indicação em cinco dias, aceitação na mesma forma; sem ela, o contrato fica com os originais.', ['06']),
 ('472', 'O distrato faz-se pela mesma forma exigida para o contrato.', ['16']),
 ('473', 'Resilição unilateral por denúncia notificada, onde a lei permita; com investimentos consideráveis, efeito só após prazo compatível.', ['16']),
 ('474', 'A cláusula resolutiva expressa opera de pleno direito; a tácita depende de interpelação judicial.', ['17']),
 ('475', 'O lesado pelo inadimplemento pode pedir a resolução ou exigir o cumprimento, com perdas e danos em qualquer caso.', ['17']),
 ('476', 'Exceção do contrato não cumprido: quem não cumpriu não pode exigir o cumprimento do outro.', ['07', '17']),
 ('477', 'Exceção de inseguridade: diminuição patrimonial posterior autoriza suspender até a prestação ou garantia.', ['07']),
 ('478', 'Resolução por onerosidade excessiva: execução continuada ou diferida, extrema vantagem, fato extraordinário e imprevisível.', ['03', '08', '12']),
 ('479', 'A resolução pode ser evitada se o réu se oferecer a modificar equitativamente as condições.', ['12']),
 ('480', 'Obrigações de uma só parte: ela pode pedir redução da prestação ou outro modo de executá-la.', ['12']),
 ('555', 'A doação pode ser revogada por ingratidão do donatário ou por inexecução do encargo.', ['16']),
 ('682', 'Causas de cessação do mandato, entre elas a revogação e a renúncia.', ['16']),
]
CDC = [
 ('2º', 'Consumidor é quem adquire ou utiliza produto ou serviço como destinatário final.', ['01']),
 ('3º', 'Fornecedor: quem desenvolve atividade de produção, comercialização ou prestação de serviços no mercado.', ['01']),
 ('4º, I', 'Reconhecimento da vulnerabilidade do consumidor.', ['01']),
 ('6º, V', 'Modificação de cláusulas desproporcionais e revisão por fato superveniente que torne a prestação excessivamente onerosa.', ['12']),
 ('30', 'Informação ou publicidade suficientemente precisa obriga o fornecedor e integra o contrato.', ['05']),
 ('35', 'Recusa de cumprir a oferta: cumprimento forçado, produto equivalente ou rescisão com perdas e danos.', ['05']),
 ('47', 'As cláusulas se interpretam da maneira mais favorável ao consumidor.', ['08', '10']),
 ('51', 'Cláusulas abusivas são nulas de pleno direito; o contrato subsiste, salvo ônus excessivo na integração.', ['11']),
]
CPC = [
 ('966, V', 'Ação rescisória por violação manifesta de norma jurídica: exige interpretação insustentável, não mera divergência.', ['10']),
]

TXT = {}
for _n in range(1, 18):
    _s = open(OUT + 'aula-%02d.html' % _n).read()
    _s = re.sub(r'<script.*?</script>|<style.*?</style>', ' ', _s, flags=re.S)
    TXT['%02d' % _n] = re.sub(r'<[^>]+>', ' ', _s)
def found(code, a, declared):
    first = re.split(r'[–, ]', a)[0].replace('º', '')
    near = re.compile(r'(?<!\d)' + re.escape(first) + r'(?![\d-])')
    art = re.compile(r'art(igo)?s?\.?\s*' + re.escape(first) + r'(?![\d-])')
    keep = [x for x in declared if near.search(TXT[x])]
    extra = [k for k in TXT if k not in declared and art.search(TXT[k])]
    if code == 'CDC':  # only count CDC hits in lessons that mention the CDC
        extra = [k for k in extra if 'CDC' in TXT[k]]
    return sorted(set(keep + extra))
def rows(code, items):
    o = ''
    for a, rule, aulas in items:
        aulas = found(code, a, aulas)
        assert aulas, (code, a)
        p2 = all(int(x) >= 9 for x in aulas)
        tag = 'p2' if p2 else ('p1' if all(int(x) <= 8 for x in aulas) else 'both')
        links = ''.join(f'<a href="aula-{x}.html">{x}</a>' for x in aulas)
        key = H.escape(f'{code} art {a} {rule}'.lower())
        o += (f'<tr data-k="{key}" class="{tag}"><th scope="row"><span class="code">{code}</span> {a}</th>'
              f'<td>{rule}</td><td class="aulas">{links}</td></tr>\n')
    return o

style = '''<style>
.artigos{max-width:1180px;margin:0 auto;padding:0 clamp(16px,4vw,48px) 30px}
.art-tools{position:sticky;top:0;z-index:5;display:flex;flex-wrap:wrap;gap:10px 18px;align-items:center;padding:12px 0;background:var(--paper);border-bottom:1.5px solid var(--ink)}
.art-tools input{flex:1 1 260px;min-height:42px;padding:8px 12px;border:1.5px solid var(--ink);background:var(--paper);color:var(--ink);font:500 16px var(--sans)}
.art-tools input:focus-visible{outline:2px solid var(--dif);outline-offset:2px}
.art-tools .chips{display:flex;gap:6px}
.art-tools button{min-height:36px;padding:6px 12px;border:1px solid var(--ink);background:var(--paper);color:var(--ink);font:11px var(--mono);letter-spacing:.08em;text-transform:uppercase;cursor:pointer}
.art-tools button[aria-pressed="true"]{background:var(--ink);color:var(--paper)}
.art-tools .count{font:11px var(--mono);letter-spacing:.08em;color:var(--muted);text-transform:uppercase}
.art-table{width:100%;border-collapse:collapse;margin:18px 0 0;font-size:16px}
.art-table caption{text-align:left;font:700 22px var(--sans);padding:26px 0 10px}
.art-table th,.art-table td{padding:10px 12px;border-bottom:1px solid var(--rule);vertical-align:top;text-align:left}
.art-table th{white-space:nowrap;font:600 15px var(--sans);width:9.5em}
.art-table .code{font:500 10px var(--mono);letter-spacing:.08em;color:var(--muted)}
.art-table tr.p1 th{box-shadow:inset 3px 0 0 var(--conc)}
.art-table tr.p2 th{box-shadow:inset 3px 0 0 var(--dif)}
.art-table tr.both th{box-shadow:inset 3px 0 0 var(--ink)}
.art-table .aulas{white-space:nowrap;width:1%}
.art-table .aulas a{display:inline-block;min-width:32px;margin:0 4px 4px 0;padding:3px 6px;border:1px solid var(--ink);font:500 12px var(--mono);text-align:center;text-decoration:none}
.art-table .aulas a:hover{background:var(--paper-2)}
.art-table tr[hidden]{display:none}
.art-empty{padding:20px 0;color:var(--muted)}
.art-key{display:flex;flex-wrap:wrap;gap:6px 18px;font:11px var(--mono);letter-spacing:.06em;text-transform:uppercase;color:var(--ink-2);margin:14px 0 0}
.art-key i{display:inline-block;width:14px;height:10px;margin-right:6px;vertical-align:-1px}
@media(max-width:620px){.art-table,.art-table tbody,.art-table tr,.art-table th,.art-table td{display:block;width:auto}.art-table tr{padding:10px 0 10px 12px;border-bottom:1px solid var(--rule)}.art-table th,.art-table td{border:0;padding:2px 0}.art-table tr.p1{box-shadow:inset 3px 0 0 var(--conc)}.art-table tr.p2{box-shadow:inset 3px 0 0 var(--dif)}.art-table tr.both{box-shadow:inset 3px 0 0 var(--ink)}.art-table tr th{box-shadow:none!important}.art-table .aulas{white-space:normal;width:auto;padding-top:6px}}
</style>
</head>
'''
body = f'''<body>
<nav class="topbar"><a href="index.html">← Teoria Geral dos Contratos</a><span>Artigos</span><button class="theme-toggle" type="button" aria-pressed="false" title="Alternar modo noite"><span class="tt-track" aria-hidden="true"><span class="tt-knob"></span></span><span class="tt-label">Modo noite</span></button></nav>
<header class="hero">
  <div class="kicker label"><span>Consulta rápida</span><span>Código Civil · CDC · CPC</span><span>Teoria Geral dos Contratos</span></div>
  <h1><span class="split">Artigos</span><span class="split">do curso</span></h1>
  <p class="deck">Cada artigo que aparece nas aulas, com a regra em uma linha e as aulas que a explicam. Procure pelo número ou por uma palavra: “lesão”, “adesão”, “mora”.</p>
</header>
<div class="artigos">
  <div class="art-tools" role="search">
    <input type="search" id="q" placeholder="Buscar: 478, silêncio, arras…" aria-label="Buscar artigo ou tema" autocomplete="off">
    <div class="chips" role="group" aria-label="Filtrar por prova"><button type="button" data-f="all" aria-pressed="true">Todos</button><button type="button" data-f="p1" aria-pressed="false">P1</button><button type="button" data-f="p2" aria-pressed="false">P2</button></div>
    <span class="count" id="count" aria-live="polite"></span>
  </div>
  <p class="art-key"><span><i style="background:var(--conc)"></i>Aulas da P1</span><span><i style="background:var(--dif)"></i>Aulas da P2</span><span><i style="background:var(--ink)"></i>As duas</span></p>
  <table class="art-table"><caption>Código Civil</caption><tbody>
{rows('CC', CC)}</tbody></table>
  <table class="art-table"><caption>Código de Defesa do Consumidor</caption><tbody>
{rows('CDC', CDC)}</tbody></table>
  <table class="art-table"><caption>Código de Processo Civil</caption><tbody>
{rows('CPC', CPC)}</tbody></table>
  <p class="art-empty" id="empty" hidden>Nenhum artigo encontrado. Tente o número (“473”) ou um tema (“denúncia”).</p>
</div>
<footer class="endnav"><a href="index.html"><span>Curso</span>Voltar ao índice</a><a href="revisao-p2.html"><span>Revisão</span>Revisão para a P2</a></footer>
<script>
(function(){{
  var q=document.getElementById('q'),rows=[].slice.call(document.querySelectorAll('.art-table tbody tr')),f='all',cnt=document.getElementById('count'),empty=document.getElementById('empty');
  function norm(s){{return s.toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g,'')}}
  var keys=rows.map(function(r){{return norm(r.getAttribute('data-k'))}});
  function run(){{
    var t=norm(q.value.trim()),n=0;
    rows.forEach(function(r,i){{
      var okF=f==='all'||r.classList.contains(f)||r.classList.contains('both');
      var ok=okF&&(!t||keys[i].indexOf(t)>-1);r.hidden=!ok;if(ok)n++;
    }});
    document.querySelectorAll('.art-table').forEach(function(tb){{tb.hidden=!tb.querySelector('tbody tr:not([hidden])')}});
    cnt.textContent=n+(n===1?' artigo':' artigos');empty.hidden=n>0;
  }}
  q.addEventListener('input',run);
  document.querySelectorAll('.chips button').forEach(function(b){{b.addEventListener('click',function(){{
    f=b.getAttribute('data-f');document.querySelectorAll('.chips button').forEach(function(x){{x.setAttribute('aria-pressed',x===b)}});run();
  }})}});
  run();
}})();
</script>
<script src="assets/curso.js?v=20260925d"></script>
</body>
</html>
'''
open(OUT + 'artigos.html', 'w').write(head + style + body)
print('ok', len(CC) + len(CDC) + len(CPC), 'rows')
