#!/usr/bin/env python3
"""CASA-1 rollout: Latam <p class="lex ..."> -> <aside class="fonte ..."> (one source block).
Text is moved, never edited; Spanish blocks gain a labelled 'tradução nossa'. Run once from the site repo root."""
import re, glob, pathlib, sys
SITE = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '~/Developer/ordenacoes-filipinas').expanduser()

# header text (inside <b>) -> (source, locator, kind, lang, translation, key phrase or None)
M = {
'Constituição de Cádiz, arts. 1º e 3º': ('Constituição de Cádiz','arts. 1º e 3º','dec','es','Art. 1º A Nação espanhola é a reunião de todos os espanhóis de ambos os hemisférios. Art. 3º A soberania reside essencialmente na Nação.',None),
'Constituição de Cádiz, art. 22': ('Constituição de Cádiz','art. 22','lim','es','Aos espanhóis que por qualquer linha são havidos e reputados como originários da África fica aberta a porta da virtude e do merecimento para serem Cidadãos [...].',None),
'Lei 6.683/1979, art. 1º, § 1º': ('Lei 6.683/1979','art. 1º, § 1º','dec','pt',None,None),
'Corte IDH, Gelman vs. Uruguai, § 238': ('Corte IDH · Gelman vs. Uruguai (2011)','§ 238','dec','es','O fato de a Lei de Caducidade ter sido aprovada num regime democrático e ainda ratificada ou respaldada pela cidadania em duas ocasiões não lhe concede, automaticamente nem por si só, legitimidade perante o Direito Internacional.','automáticamente ni por sí sola, legitimidad ante el Derecho Internacional'),
'Corte IDH, Gelman vs. Uruguai, § 239': ('Corte IDH · Gelman vs. Uruguai (2011)','§ 239','dec','es','A mera existência de um regime democrático não garante, por si só, o respeito permanente ao Direito Internacional [...]. A legitimação democrática de determinados fatos ou atos numa sociedade está limitada pelas normas e obrigações internacionais de proteção dos direitos humanos [...], a proteção dos direitos humanos constitui um limite intransponível à regra das maiorias, isto é, à esfera do “suscetível de ser decidido” pelas maiorias.','la protección de los derechos humanos constituye un límite infranqueable a la regla de mayorías'),
'Corte IDH, supervisão Gelman (2013), considerando 102': ('Corte IDH · supervisão Gelman (2013)','considerando 102','dec','es','A obrigação do Estado de dar pronto cumprimento às decisões da Corte […] vincula todos os seus poderes e órgãos, incluídos seus juízes […], pelo que não pode invocar disposições do direito constitucional ou outros aspectos do direito interno para justificar um descumprimento da Sentença.',None),
'Constituição da Bolívia, art. 256.I': ('Constituição da Bolívia','art. 256.I','dec','es','Os tratados e instrumentos internacionais em matéria de direitos humanos que tenham sido firmados, ratificados ou aos quais o Estado tenha aderido, que declarem direitos mais favoráveis aos contidos na Constituição, aplicar-se-ão de maneira preferencial sobre esta.',None),
'Corte IDH, OC-28/21, parte dispositiva': ('Corte IDH · OC-28/21','parte dispositiva','dec','es','2. A reeleição presidencial indefinida não constitui um direito autônomo protegido pela Convenção Americana [...]. 3. A proibição da reeleição indefinida é compatível com a Convenção Americana [...] e com a Carta Democrática Interamericana. 4. A habilitação da reeleição presidencial indefinida é contrária aos princípios de uma democracia representativa.',None),
'Corte Constitucional, T-153/1998': ('Corte Constitucional · T-153/1998','','dec','es','As prisões colombianas caracterizam-se pela superlotação, pelas graves deficiências em serviços públicos e assistenciais, pelo império da violência, pela extorsão e pela corrupção, e pela carência de oportunidades e meios para a ressocialização.',None),
'STF, ADPF 347, tese de julgamento': ('STF · ADPF 347','tese de julgamento','dec','pt',None,None),
'Corte Constitucional, T-025/2004, ordinal primeiro': ('Corte Constitucional · T-025/2004','ordinal primeiro','dec','es','Declarar a existência de um estado de coisas inconstitucional na situação da população deslocada, devido à falta de concordância entre a gravidade da afetação dos direitos reconhecidos constitucionalmente e desenvolvidos pela lei, de um lado, e o volume de recursos efetivamente destinado a assegurar o gozo efetivo de tais direitos e a capacidade institucional para implementar os correspondentes mandatos constitucionais e legais, de outro lado.',None),
'Corte Constitucional, Auto 008/2009, ordinal primeiro': ('Corte Constitucional · Auto 008/2009','ordinal primeiro','dec','es','Constatar que persiste o estado de coisas inconstitucional, apesar dos avanços alcançados. [...] O ônus de demonstrar que as condições que deram lugar à declaração do estado de coisas inconstitucional foram superadas recai sobre o governo nacional.','La carga de demostrar que las condiciones que dieron lugar a la declaratoria del estado de cosas inconstitucional han sido superadas, recae sobre el gobierno nacional.'),
'Súmula Vinculante 60': ('Súmula Vinculante 60','','dec','pt',None,None),
}

def block(m):
    head, text = m.group(1), m.group(2)
    src, loc, kind, lang, tr, key = M[head]
    if key:
        assert key in text, (head, key)
        text = text.replace(key, f'<span class="key">{key}</span>')
    h = f'<span>{src}</span>' + (f'<span class="loc">{loc}</span>' if loc else '')
    lg = f' lang="{lang}"' if lang == 'es' else ''
    out = f'<aside class="fonte {kind}" aria-label="Fonte: {src}{", " + loc if loc else ""}"><header>{h}</header><blockquote{lg}><p>{text}</p></blockquote>'
    if tr:
        out += f'<p class="tr" hidden><b>Tradução nossa</b>{tr}</p><footer><button type="button" data-tr aria-expanded="false">ver tradução</button></footer>'
    return out + '</aside>'

n = 0
for f in sorted(glob.glob(str(SITE / 'courses/direito-latino-americano/aula-0*.html'))):
    s = pathlib.Path(f).read_text()
    s2, k = re.subn(r'<p class="lex[^"]*"><b>(.*?)</b>(.*?)</p>', block, s)
    if not k: continue
    s2 = re.sub(r'\.lex[^{}]*\{[^{}]*\}', '', s2)               # inline .lex rules
    s2 = s2.replace('<link rel="stylesheet" href="assets/curso.css', '<link rel="stylesheet" href="../../assets/casa.css">\n<link rel="stylesheet" href="assets/curso.css', 1)
    s2 = s2.replace('</body>', '<script src="../../assets/casa.js" defer></script>\n</body>', 1)
    pathlib.Path(f).write_text(s2); n += k; print(f.split('/')[-1], k)
print('blocks', n)
