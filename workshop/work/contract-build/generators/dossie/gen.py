import re, json, html as H, os, glob
W = '/private/tmp/claude-501/-Users-benecles/6ba9d1ed-6a88-4cf1-8437-12aaf015e3ac/scratchpad/pdf/'
SITE = '/Users/benecles/Documents/Codex/2026-09-05/okay-couple-things-so-first-of/work/study-lab-publish/courses/teoria-geral-dos-contratos/'
CB = '/Users/benecles/Documents/Codex/2026-09-23/you-h/work/contract-build/'
LAW = json.load(open(W + 'law.json'))
esc = H.escape

# ---------- statutes
NOISE = re.compile(r'\((?:Redação dada|Incluíd[oa]|Revogad[oa]|Vide|Vigência|Regulamento|Produção de efeitos)[^)]*\)|Produção de\s+efeitos|\(Vigência\)', re.S)
def clean_article(lines):
    t = ' '.join(lines)
    t = re.sub(r'\s+', ' ', t)
    t = NOISE.sub('', t)
    t = re.sub(r'\s+', ' ', t).strip()
    # break before paragraphs, incisos, alíneas
    t = re.sub(r'\s(Parágrafo único\.)', r'\n\1', t)
    t = re.sub(r'\s(§\s*\d+[º°o]?)', r'\n\1', t)
    t = re.sub(r'\s([IVXL]+\s*[-–]\s)', r'\n\1', t)
    t = re.sub(r'\s([a-z]\)\s)', r'\n\1', t)
    return t
def law_block(code, ranges, title):
    arts = LAW[code]
    out = [f'<h3>{title}</h3>']
    keys = list(arts.keys())
    def num(k):
        m = re.match(r'(\d+)(-[A-Z])?', k); return (int(m.group(1)), m.group(2) or '')
    for a, b in ranges:
        for k in keys:
            n, suf = num(k)
            if a <= n <= b:
                txt = clean_article(arts[k])
                if re.fullmatch(r'Art\. \d+(-[A-Z])?\.?\s*', txt): txt += ' (revogado)'
                out.append('<div class="art">' + esc(txt).replace('\n', '<br>') + '</div>')
    return '\n'.join(out)
def dedupe_order(code):
    pass

CC_RANGES = [(104, 114), (138, 157), (166, 172), (178, 179), (184, 188), (233, 246), (286, 303), (313, 317),
             (389, 420), (421, 480)]
CDC_RANGES = [(2, 4), (6, 6), (29, 31), (35, 35), (46, 54)]

# ---------- site pages → clean HTML
def clean_page(fn, keep_quiz=True):
    s = open(SITE + fn).read()
    title = re.search(r'<title>(.*?)</title>', s).group(1)
    b = s[s.index('<body'):]
    b = re.sub(r'<nav class="topbar".*?</nav>', '', b, flags=re.S)
    b = re.sub(r'<nav class="endnav".*?</nav>', '', b, flags=re.S)
    b = re.sub(r'<footer.*?</footer>', '', b, flags=re.S)
    b = re.sub(r'<script.*?</script>', '', b, flags=re.S)
    b = re.sub(r'<svg.*?</svg>', '', b, flags=re.S)
    b = re.sub(r'<div class="stage".*?</figure></div>', '', b, flags=re.S)
    b = re.sub(r'<div class="titleblock.*?</div>\s*</div>', '', b, flags=re.S)
    b = re.sub(r'<div class="titleblock[^>]*>(?:<div role="listitem">.*?</div>)+</div>', '', b, flags=re.S)
    b = re.sub(r'<div class="kicker label">.*?</div>', '', b, flags=re.S)
    b = re.sub(r'<span class="num[^"]*"[^>]*>.*?</span>', '', b, flags=re.S)
    b = re.sub(r'<h1>(.*?)</h1>', lambda m: '<h3 class="lt">' + re.sub('<[^>]+>', ' ', m.group(1)) + '</h3>', b, flags=re.S)
    b = re.sub(r'<h2([^>]*)>', r'<h4\1>', b).replace('</h2>', '</h4>')
    b = re.sub(r'<h3>', '<h5>', b).replace('</h3>', '</h5>')
    b = b.replace('<h3 class="lt">', '<h3>').replace('</h3 class="lt">', '</h3>')
    b = re.sub(r'<summary>(.*?)</summary>', r'<p class="q"><b>Pergunta:</b> \1</p>', b, flags=re.S)
    b = re.sub(r'<details[^>]*>|</details>', '', b)
    b = re.sub(r'<(/?)(body|header|section|main|figure|figcaption)[^>]*>', '', b)
    b = re.sub(r'class="[^"]*"', '', b)
    b = re.sub(r'<(div|span|article|p|strong|b|em|li|ul|ol|table|tr|td|th|thead|tbody|h\d)\s+[^>]*>', r'<\1>', b)
    b = re.sub(r'<span>(.*?)</span>', r'<b>\1</b> ', b, flags=re.S)
    b = re.sub(r'</?html>', '', b)
    b = re.sub(r'\n\s*\n+', '\n', b)
    return title, b

def pre(path, maxlen=None):
    t = open(path, errors='replace').read()
    if maxlen: t = t[:maxlen]
    t = re.sub(r'[ \t]+\n', '\n', t)
    t = re.sub(r'\n{3,}', '\n\n', t)
    return '<pre>' + esc(t) + '</pre>'

parts = []
A = parts.append
A('''<h1>Teoria Geral dos Contratos · UFRGS 2026/2</h1>
<p class="sub">Dossiê de estudo para a <b>Primeira Prova (25/09/2026)</b> · DIR02023 · Profa. Giovana Benetti · com apêndice da P2</p>''')

A('''<h2 class="first">0. Instruções para a IA que vai usar este material</h2>
<div class="box">
<p>Você está ajudando um estudante de Direito da UFRGS a se preparar para a <b>Primeira Prova de Teoria Geral dos Contratos</b> (Profa. Giovana Benetti, 25/09/2026). Use este dossiê como fonte principal. Regras:</p>
<ol>
<li><b>Escopo da P1:</b> unidades 1 a 5 do plano de ensino (conceito; princípios; formação; incidentes da formação; classificação), cobertas pelas Aulas 01 a 08 deste dossiê. A prova <b>não é cumulativa</b>: interpretação, revisão, cessão e extinção são da P2 (apêndice).</li>
<li><b>Formato provável:</b> questões objetivas com um caso concreto e alternativas (a–d), como as duas listas oficiais da Parte 8. Ao corrigir ou criar questões, siga esse padrão e o raciocínio dos gabaritos oficiais.</li>
<li><b>Hierarquia de fontes:</b> (1) gabaritos oficiais da professora; (2) slides da professora (Parte 6); (3) texto de lei vigente (Parte 5, transcrito do Planalto em 25/09/2026); (4) resumos e aulas (Partes 3 e 4). Em conflito, prevalece essa ordem.</li>
<li><b>Pontos de atenção já verificados:</b>
 <ul>
 <li><b>Laudêmio e integralização de capital:</b> o gabarito considera a transferência <b>onerosa</b> (laudêmio devido), seguindo os EREsp 1.104.363/PE da Corte Especial e o Tema Repetitivo 332 do STJ. O REsp 1.104.363/PE de 2009 (Segunda Turma), que dizia o contrário, foi superado.</li>
 <li><b>Art. 418 do CC</b> tem redação nova (Lei 14.905/2024): se o inadimplemento é de quem recebeu as arras, quem as deu pode desfazer o contrato e exigir a devolução mais o equivalente, com atualização monetária, juros e honorários.</li>
 <li><b>Art. 456 do CC foi revogado</b> pelo CPC/2015 (denunciação da lide na evicção).</li>
 <li><b>Responsabilidade pré-contratual:</b> a professora a fundamenta no <b>art. 187</b> (abuso do direito), com a boa-fé do art. 422 como reforço; o art. 422 fala literalmente em “conclusão” e “execução”.</li>
 <li><b>Proposta:</b> requisitos de firmeza (seriedade), completude e adequação formal (determinabilidade). A oferta jocosa não é proposta.</li>
 <li><b>Silêncio (art. 432):</b> só forma o contrato se não for costume a aceitação expressa <b>ou</b> o proponente a tiver dispensado, e a recusa não chegar a tempo.</li>
 </ul></li>
<li>Responda em português, cite o artigo e o fato do enunciado que aciona a regra, e aponte a “armadilha” de cada alternativa errada.</li>
</ol>
<p><b>Sumário:</b> 1. Plano de ensino · 2. Mapa da prova · 3. Resumo por unidade e 10 casos resolvidos · 4. Aulas 01–08 completas · 5. Legislação (CC e CDC, texto integral) · 6. Slides da professora (texto) · 7. Jurisprudência do curso · 8. Listas oficiais de exercícios com gabarito · 9. Banco de perguntas com respostas · Apêndice: P2.</p>
</div>''')

A('<h2>1. Plano de ensino (texto integral)</h2>' + pre(W + 'plano.txt'))

A('''<h2>2. Mapa da prova</h2>
<table><tr><th>Unidade do programa</th><th>Aulas</th><th>Artigos centrais</th><th>Casos</th></tr>
<tr><td>1. Conceito e funções; contrato no CC e no CDC</td><td>01</td><td>CC 104, 421; CDC 2º, 3º, 4º, 6º</td><td>Consumidor PJ (finalismo aprofundado)</td></tr>
<tr><td>2. Princípios (liberdade, força obrigatória, relatividade, função social, boa-fé, equilíbrio)</td><td>02, 03</td><td>CC 421, 421-A, 422, 423, 424, 187, 113, 157, 317, 478</td><td>Zeca Pagodinho (terceiro ofensor); Enunciados 22 e 23 da Jornada; supressio (consórcio)</td></tr>
<tr><td>3. Formação: contrato como processo; tratativas; proposta e aceitação</td><td>04, 05</td><td>CC 187, 422, 427–435; CDC 30, 35</td><td>Supermercado × banco; evento; bilhete; proposta jocosa</td></tr>
<tr><td>4. Incidentes: terceiros, pessoa a declarar, promessa de fato de terceiro, preliminar, arras</td><td>06</td><td>CC 436–440, 462–471, 416–420</td><td>Shopping e lojas-âncora; preliminar × definitivo</td></tr>
<tr><td>5. Classificação</td><td>07, 08</td><td>CC 476, 477, 447–457, 458–461, 441–446, 107–109, 423–425, 478; CDC 47</td><td>Exclusividade no shopping; elevador; costura; lotes/evicção; swap; loteria; laudêmio; carro</td></tr></table>''')

t, b = clean_page('revisao-p1.html')
A('<h2>3. Resumo por unidade e 10 casos resolvidos (revisão da P1)</h2>' + b)
A('<h2>4. Aulas 01 a 08 (texto integral)</h2>')
for n in range(1, 9):
    t, b = clean_page('aula-%02d.html' % n)
    A(f'<div class="aula"><h3 class="aulah">Aula {n:02d} · {esc(t.split(" · ")[0])}</h3>{b}</div>')

A('<h2>5. Legislação (texto vigente, Planalto, consultado em 25/09/2026)</h2><p class="note">Anotações de alteração legislativa foram removidas para facilitar a leitura; artigos revogados aparecem marcados.</p>')
A(law_block('cc', CC_RANGES, 'Código Civil (Lei 10.406/2002): artigos usados no curso'))
A(law_block('cdc', CDC_RANGES, 'Código de Defesa do Consumidor (Lei 8.078/1990): artigos usados no curso'))

A('<h2>6. Slides da professora (texto extraído)</h2><p class="note">Texto extraído dos PDFs das aulas, página a página. É a formulação da própria professora: use-a para calibrar vocabulário e ênfase.</p>')
for f in ['Slides - Aula 1 até 26.txt', 'Aula 2 - Slides 27 a 45.txt', 'Slides Aula 3.txt', 'Slides Aula 5 Moodle.txt', 'Moodle Aula 6.txt', 'Slides Exceção e Classificação.txt']:
    A(f'<h3>{esc(f[:-4])}</h3>' + pre(CB + 'slides/text/' + f))
A('<h3>Slides extras Aula 7</h3>' + pre(W + 'slides-extras-aula7.txt'))
A('<h3>Leitura visual de slides-chave (o que os diagramas mostram)</h3>' + pre(CB + 'slides/visual-digest-p1.md'))

A('''<h2>7. Jurisprudência usada nas listas</h2>
<table><tr><th>Decisão</th><th>Tema</th><th>O que foi decidido</th></tr>
<tr><td>REsp 1.689.225/SP (STJ, 3ª Turma)</td><td>Swap cambial (derivativo de hedge)</td><td>Recurso desprovido. CDC não se aplica; cláusula de limite de risco válida; a variação cambial é a álea normal do derivativo, o que afasta imprevisão e revisão por onerosidade excessiva. Exposição desigual ao risco, conhecida na contratação, não viola a boa-fé.</td></tr>
<tr><td>REsp 586.458/DF (STJ, 4ª Turma)</td><td>Loteria “Certo ou Errado”; contrato aleatório</td><td>Recurso não conhecido. O cedente aceitou o risco de nada receber se a arrecadação não superasse o dobro do patamar; a CEF não prometeu manter a proporção entre as loterias. Sem descumprimento nem ilícito.</td></tr>
<tr><td>EREsp 1.104.363/PE (STJ, Corte Especial) e Tema 332</td><td>Laudêmio na integralização de capital</td><td>A transferência do domínio útil de terreno de marinha para integralizar capital é <b>onerosa</b> (o sócio recebe quotas/ações): o laudêmio é devido. Superou o REsp 1.104.363/PE de 2009, da 2ª Turma, que a tratava como gratuita.</td></tr>
<tr><td>AgInt no AREsp 1.684.366/SP (STJ)</td><td>Responsabilidade pré-contratual</td><td>Exige expectativa legítima de conclusão do contrato e dano efetivo. O tribunal estadual reconheceu negociações avançadas, quebra da boa-fé, dano e nexo; rever isso esbarra na Súmula 7.</td></tr>
<tr><td>AgInt no AREsp 2.282.332/SP (STJ, 4ª Turma)</td><td>Exceptio non adimpleti contractus (serralheria)</td><td>Defeito comprovado na serralheria contratada: a parcela correspondente não era devida (art. 476). Rever exigiria reexame de provas (Súmula 7).</td></tr>
</table>
<p class="note">Outros casos do curso (Zeca Pagodinho, supermercado × banco, shopping e lojas-âncora, elevador, costura, lotes/evicção, carro) estão descritos nas aulas da Parte 4.</p>''')
A('<h3>Ementas e trechos iniciais (OCR dos acórdãos)</h3>')
for f in sorted(glob.glob(CB + 'ocr/cases/*.txt')):
    t = open(f, errors='replace').read()
    pages = re.split(r'(?==+ ?PDF PAGE)', t)
    head = ''.join(pages[:3])[:9000]
    A(f'<h4>{esc(os.path.basename(f))}</h4><pre>{esc(head)}</pre>')

A('<h2>8. Listas oficiais de exercícios e gabaritos da professora</h2>')
for f, tt in [('exercicios-primeira-lista.txt', 'Primeira lista de exercícios (enunciados)'), ('gabarito-primeira-lista.txt', 'Gabarito comentado da primeira lista'),
              ('questoes-extra.txt', 'Questões extra (enunciados)'), ('gabarito-questoes-extra.txt', 'Gabarito comentado das questões extra')]:
    A(f'<h3>{tt}</h3>' + pre(CB + 'ocr/practice/' + f))
A('''<table><tr><th>Lista</th><th>Q</th><th>Tema</th><th>Gabarito</th></tr>
<tr><td>1ª</td><td>1</td><td>Proposta em tom jocoso: falta firmeza</td><td>B</td></tr>
<tr><td>1ª</td><td>2</td><td>Terceiro ofensor (contrato de exclusividade)</td><td>B</td></tr>
<tr><td>1ª</td><td>3</td><td>Swap cambial: álea normal, sem revisão</td><td>B</td></tr>
<tr><td>1ª</td><td>4</td><td>Remuneração ligada à arrecadação: contrato aleatório</td><td>B</td></tr>
<tr><td>1ª</td><td>5</td><td>Integralização de capital: onerosa, laudêmio devido</td><td>B</td></tr>
<tr><td>1ª</td><td>6</td><td>Ruptura de negociações avançadas: responsabilidade pré-contratual</td><td>C</td></tr>
<tr><td>Extra</td><td>1</td><td>Exceptio non adimpleti contractus em serviço defeituoso</td><td>C</td></tr>
<tr><td>Extra</td><td>2</td><td>Locação de equipamento imprestável</td><td>B</td></tr>
<tr><td>Extra</td><td>3</td><td>Reparos inadequados em navio: exceptio non rite adimpleti contractus</td><td>C</td></tr>
<tr><td>Extra</td><td>4</td><td>Vícios redibitórios, adequação do veículo e dano moral</td><td>C</td></tr></table>''')

A('<h2>9. Banco de perguntas com respostas (Aulas 01–08)</h2>')
qs = []
for n in range(1, 9):
    s = open(SITE + 'aula-%02d.html' % n).read()
    q = s[s.rindex('<div class="quiz">'):]; q = q[:q.index('</div>')]
    for sm, ans in re.findall(r'<details><summary>(.*?)</summary><p>(.*?)</p></details>', q, re.S):
        qs.append((n, sm, ans))
for i, (n, sm, ans) in enumerate(qs, 1):
    A(f'<p class="q"><b>{i}. (Aula {n:02d})</b> {sm}</p><p class="a"><b>Resposta:</b> {ans}</p>')

A('<h2 class="apx">Apêndice · P2 (27/11/2026): interpretação, revisão, cessão e extinção</h2><p class="note">Não cai na P1. Incluído para uso futuro.</p>')
t, b = clean_page('revisao-p2.html'); A('<h3>Revisão da P2</h3>' + b)
for n in range(9, 18):
    t, b = clean_page('aula-%02d.html' % n)
    A(f'<div class="aula"><h3 class="aulah">Aula {n:02d} · {esc(t.split(" · ")[0])}</h3>{b}</div>')

CSS = '''
@page{size:A4;margin:16mm 15mm}
body{font:10.5pt/1.45 Georgia,'Times New Roman',serif;color:#111}
h1{font:700 24pt/1.1 Helvetica,Arial,sans-serif;margin:0 0 4mm}
.sub{font:11pt Helvetica,Arial,sans-serif;color:#444;margin-bottom:8mm}
h2{font:700 16pt/1.2 Helvetica,Arial,sans-serif;border-bottom:2px solid #b4432a;padding-bottom:2mm;margin:10mm 0 4mm;page-break-before:always}
h2.apx{border-color:#2b5597}
h2.first{page-break-before:auto}
h3{font:700 13pt Helvetica,Arial,sans-serif;margin:6mm 0 2mm}
h3.aulah{background:#f2eee3;padding:2mm 3mm;border-left:4px solid #b4432a}
h4{font:700 11.5pt Helvetica,Arial,sans-serif;margin:4mm 0 1mm}
h5{font:700 10.5pt Helvetica,Arial,sans-serif;margin:3mm 0 1mm}
pre{font:8.3pt/1.35 Menlo,'Courier New',monospace;white-space:pre-wrap;background:#fafaf7;border:1px solid #ddd;padding:3mm}
table{border-collapse:collapse;width:100%;margin:3mm 0;font-size:9.5pt;page-break-inside:auto}
td,th{border:1px solid #bbb;padding:1.5mm 2mm;vertical-align:top;text-align:left}
th{background:#eee}
.art{margin:0 0 2.2mm;padding-left:2mm;border-left:2px solid #ddd}
.box{border:1.5px solid #111;padding:4mm;background:#fbfaf6}
.note{color:#555;font-style:italic}
p.q{margin:3mm 0 0}
p.a{margin:1mm 0 2mm 4mm;color:#222}
.aula{page-break-before:always}
b,strong{font-weight:700}
'''
doc = '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Teoria Geral dos Contratos · Dossiê P1</title><style>' + CSS + '</style></head><body>' + '\n'.join(parts) + '</body></html>'
open(W + 'dossie.html', 'w').write(doc)
print('html', len(doc), 'questions', len(qs))
