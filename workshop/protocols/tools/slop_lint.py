#!/usr/bin/env python3
"""Portuguese CUFRGS prose linter: findings are review prompts, not verdicts.

Usage: python3 slop_lint.py FILE_OR_DIR [...] [--json] [--max-per-1000 N]
Reads visible text from HTML and text from Markdown/plain text. No hit fails by
itself. An explicit aggregate finding-density budget can fail a file.
"""
import argparse, html, json, os, re, sys

HARD = {
    'negative-parallelism': (r'\b(?:não é|não era|não são|não foi|não se trata de|mais do que)\b', 'Retain only if both sides state a real legal distinction; otherwise state the affirmative rule.'),
    'puffery': (r'\b(?:papel (?:crucial|fundamental|central|decisivo|essencial)|desempenha(?:m)? (?:um )?papel|pedra angular|divisor de águas|ganha(?:m)? destaque|merece(?:m)? atenção especial|reflete(?:m)? a (?:importância|relevância)|evidencia(?:ndo|m)? a (?:importância|relevância))\b', 'Replace importance language with the rule, fact, or consequence that makes the point matter.'),
    'significance-gerund': (r',\s*(?:evidenciando|reforçando|consolidando|demonstrando|ressaltando|sublinhando|refletindo|destacando)\s+(?:a|o|as|os|sua|seu)\s+(?:importância|relevância|papel|centralidade|necessidade|peso|força|valor)\b', 'Delete the evaluative tail or replace it with a new fact.'),
    'formulaic-metatext': (r'\b(?:vale (?:a pena )?(?:ressaltar|destacar|notar|lembrar|mencionar)|cabe (?:ressaltar|destacar|notar|lembrar)|é (?:importante|interessante) (?:notar|ressaltar|destacar|observar|lembrar)|nesta aula (?:veremos|vamos)|como (?:vimos|veremos)|vamos entender|em conclusão|à luz do exposto)\b', 'Remove the announcement and state the legal proposition.'),
    'vague-attribution': (r'\b(?:especialistas (?:apontam|afirmam|destacam)|muitos autores|a doutrina moderna|há quem (?:diga|sustente|defenda)|alguns críticos)\b', 'Name the author, court, or position when the source does.'),
    'reader-address': (r'\b(?:você já deve ter percebido|não se preocupe|pense nisso|perceba que|repare:?)\b', 'State the rule or consequence directly.'),
    'AI-calque': (r'\b(?:no cenário (?:atual|jurídico|brasileiro)|navegar (?:por|pel[oa]s?)|abordagem holística|robust[oa]s?|(?-i:jornada)(?! (?:de trabalho|limitada|diária|semanal|máxima))|mergulh(?:ar|amos|e) (?:em|n[oa]s?))\b', 'Replace the calque with the concrete legal action or plain Portuguese verb.'),
    'backstage': (r'\b(?:(?:os|nos|dos|pelos|segundo os?) slides?|materia(?:l|is) da disciplina|nest[ae] leitura|dest[ae] leitura|prática autoral|relatad[oa]s? por|localizador(?:es)?|fontes e (?:limites|localizadores)|(?-i:C\d{1,2})\b|blueprint|cerca desta)\b', 'Move provenance to the private ledger; keep the page about the legal material.'),
    # 06/10 additions from avoid-ai-writing, stop-slop, autonovel ANTI-SLOP, MariusAure and Writing Standard D10.
    'teaser-hook': (r'(?:^|(?<=[.!?]\s))(?:O resultado|O problema|A questão|O detalhe|A resposta|O ponto|A consequência|O motivo|O curioso|O efeito|A pegadinha)\?', 'Delete the staged question and state the fact.'),
    'self-labeling': (r'\b(?:(?:esse|este|eis|aqui está|aí está) (?:é )?o (?:ponto|detalhe|dado|passo|movimento) (?:central|crucial|decisivo|essencial|mais importante|interessante|contraintuitivo)|aí está o (?:essencial|ponto))\b', 'Cut the label; let the fact show its weight.'),
    'hedge-stack': (r'\b(?:pode(?:m|ria|riam|rá)? (?:potencialmente|eventualmente|possivelmente|talvez)|talvez (?:possa|pudesse|poderia))\b', 'Keep one qualifier, where the doubt is (C7).'),
    'false-concession': (r'\b(?:embora|ainda que|apesar de)\b[^.;]{3,90},\s*[^.;]{0,40}\b(?:continua|permanece|resta|segue)\b[^.;]{0,40}\b(?:desafio|em aberto|incert[oa]|um problema)\b', 'Make the concession specific from the sources, or cut the frame (D10.5).'),
    'staged-objection': (r'\b(?:alguém poderia (?:dizer|objetar|argumentar|pensar)|poder-se-ia (?:objetar|dizer|argumentar)|pode-se objetar|seria tentador (?:pensar|concluir|dizer)|à primeira vista, (?:poder-se-ia|parece))\b', 'Fake disagreement (D10.1): dispute only named positions with reasons.'),
    'reader-steer-question': (r'\b(?:o que (?:isso|isto) significa|por que isso importa|e o que isso (?:quer dizer|muda)|qual a consequência disso)\?', 'Answer directly; drop the rhetorical question.'),
    'circular-because': (r'\bporque (?:havia|existia|há|existe) (?:a |uma )?(?:necessidade|exigência) de\b', 'Circular explanation (D10.2): name the fact, rule or actor that caused it.'),
    'rhetorical-triad': (r'\b(?:e,\s*sobretudo,|e,\s*acima de tudo,)', 'Keep the full enumeration only when each item is legally necessary; remove rhetorical emphasis.'),
}
# D9 rate signals and transferred measured-positive constructions. Limits are
# project review budgets, not linguistic laws. Each emits only after >=2 hits,
# >=250 words and >=5 sentences, except absence-based paren-scarcity.
RATE = {
 'colon-reveal': (r'\b[^\n.!?]{2,100}:\s+[^\n.!?]{3,160}[.!?]', 2.5, 'If the second clause only dramatizes/rephrases the first, state the fact directly; keep a colon that introduces real content.'),
 'denial-restatement': (r'\bnão\b[^.;:!?]{1,100}[,;]\s*(?:mas|e sim|senão)\s+[^.;:!?]{2,100}', 0.0, 'Apply the delete-the-não test. Keep both halves when they encode a legal distinction.'),
 'rather-than': (r'\b(?:em vez de|ao invés de|em lugar de|em lugar da|em lugar do)\b', 1.0, 'Use a direct affirmative verb when the contrast adds no legal condition.'),
 'triad-density': (r'\b[^,.!?;\n]{1,60},\s*[^,.!?;\n]{1,60}\s+e\s+[^.!?;\n]{1,60}', 4.0, 'Enumerate the number of legal elements the source actually provides; keep statutory triads.'),
 'stance-adverb': (r'\b(?:meramente|simplesmente|genuinamente|verdadeiramente|efetivamente|justamente|precisamente|silenciosamente)\b', 0.0, 'Remove emphasis if it adds no fact; keep an adverb that changes the legal proposition.'),
 'negation-chain': (r'\b(?:sem\s+[^,.;!?]{1,35},\s*){2,}sem\s+[^.;!?]{1,45}|(?:\bNão\s+[^.!?]{2,90}[.!?]\s*){2,}\bNão\s+[^.!?]{2,90}[.!?]', 0.0, 'Convert only rhetorical repetition; retain enumerated legal requirements.'),
 'same-opener-run': (r'(?m)(?:^|(?<=[.!?]\s))([A-ZÁÉÍÓÚÂÊÔÃÕÇ][\wÀ-ÿ-]{1,18})(?:\b[^.!?]*[.!?]\s+)(?:\1\b[^.!?]*[.!?]\s+){2}', 0.0, 'Vary openings only if the repeated subject is not required for legal clarity.'),
 'semicolon-correction': (r'[^.!?;]{3,100};\s*(?:mas|porém|antes|na verdade|e sim|em vez disso|isto é|ou seja),?\s+[^.!?]{3,120}[.!?]', 1.0, 'Keep a semicolon only when it joins independent but closely related clauses; remove correction theater.'),
 'colon-appositive': (r'\b(?:é|são|significa|consiste em|inclui|abrange)\s*:\s*[^.!?]{3,100}[.!?]', 1.0, 'Keep a colon introducing a needed definition/list; otherwise write the definition in the same sentence.'),
 'load-bearing-adverb': (r'\b(?:claramente|obviamente|naturalmente|certamente|inevitavelmente|simplesmente|basicamente|essencialmente|fundamentalmente)\b', 1.0, 'Delete it if the sentence remains equally precise; preserve genuine evidential qualification.'),
 'nominalisation-pileup': (r'\b(?:a|o|da|do|na|no)\s+(?:implementação|realização|efetivação|verificação|aplicação|ocorrência|concretização|determinação|construção|formulação)\s+(?:da|de|do|na|no)\s+(?:análise|execução|aplicação|verificação|realização|implementação|concretização|determinação)\b', 1.0, 'Put the action in a verb and name who performs it, if known.'),
 'stacked-questions': (r'[^.!?\n]{3,140}\?\s+[^.!?\n]{3,140}\?', 0.0, 'Keep at most one question; state the answers the sources give.'),
 'transition-opener': (r'(?m)^\s*(?:Além disso|Ademais|Por outro lado|Contudo|Entretanto|No entanto|Dessa forma|Desse modo|Assim sendo|Nesse sentido|Outrossim|Por fim)\b', 1.5, 'Start paragraphs with their subject; keep a connector only where the logic is invisible (C3).'),
 'fragment-run': (r'(?!)', 0.0, 'Fold staccato fragments into sentences; keep one fragment only if it earns emphasis.'),
 'uniform-paragraphs': (r'(?!)', 0.0, 'Reshape paragraphs around the argument (D9); never to a length quota.'),
 'paren-scarcity': (r'(?!)', 0.0, 'Consider parenthetical material only when it clarifies; do not add parentheses merely to satisfy this signal.'),
}
# For reports only: counts instances of parenthetical text as meaningful usage;
# zero on a long page is an absence signal, not a match-count rule.
PAREN = re.compile(r'\([^()\n]{2,100}\)')
TERMS = re.compile(r'\b(?:direitos? fundamenta(?:l|is)|princípios? fundamenta(?:l|is)|preceito fundamental|elementos? essencia(?:l|is)|erro essencial|qualidades? essencia(?:l|is)|requisitos? essencia(?:l|is)|funç(?:ão|ões) essencia(?:l|is)|serviços? essencia(?:l|is)|banco central|garantias? fundamenta(?:l|is)|questão central|figura central|posição central|núcleo essencial)\b', re.I)

def text_of(path):
    with open(path, encoding='utf-8', errors='replace') as source:
        s = source.read()
    if path.lower().endswith('.html'):
        s = re.sub(r'(?s)<!--.*?-->', ' ', s)
        s = re.sub(r'(?is)<(script|style|svg|head|nav)\b.*?</\1>', ' ', s)
        s = re.sub(r'(?is)<div hidden\b.*?(?=</body>)', ' ', s)
        s = re.sub(r'(?i)<br\s*/?>|</(?:p|li|h\d|td|th|div|figcaption|summary)>', '\n', s)
        s = html.unescape(re.sub(r'<[^>]+>', ' ', s))
    return re.sub(r'[ \t]+', ' ', s)

def finding(text, path, rule, m, fix, density=None):
    return {'file': path, 'line': text.count('\n', 0, m.start()) + 1,
            'rule': rule, 'span': re.sub(r'\s+', ' ', m.group(0)).strip(),
            'fix': fix, **({'per_1000': round(density, 3)} if density is not None else {})}

def lint(path, budget):
    t = text_of(path); words = len(re.findall(r'\b\w+\b', t, re.UNICODE)); sentences = len(re.findall(r'[.!?](?:\s|$)', t))
    out=[]
    masked=TERMS.sub(lambda m:'§'*len(m.group()),t)
    for name,(pat,fix) in HARD.items():
        for m in re.finditer(pat,masked,re.I):
            item=finding(t,path,name,m,fix); item['severity']='hard'; out.append(item)
    eligible=words>=250 and sentences>=5
    if eligible:
        for name,(pat,limit,fix) in RATE.items():
            if name=='paren-scarcity':
                if not PAREN.search(t):
                    m=re.search(r'\b\w+\b',t)
                    if m:
                        item=finding(t,path,name,m,fix,0.0)
                        item['severity']='rate'; item['limit_per_1000']=limit; item['over_limit']=False
                        out.append(item)
                continue
            if name == 'fragment-run':
                sents=list(re.finditer(r'[^.!?\n]+[.!?](?:\s+|$)', masked)); matches=[]; run=[]
                for sm in sents:
                    if 0 < len(re.findall(r"\b\w+\b", sm.group(0))) <= 3: run.append(sm)
                    else:
                        if len(run)>=3: matches.append(run[0])
                        run=[]
                if len(run)>=3: matches.append(run[0])
                if matches:
                    rate=len(matches)*1000/max(words,1)
                    for m in matches:
                        item=finding(t,path,name,m,fix,rate); item['severity']='rate'; item['limit_per_1000']=limit; item['over_limit']=True; out.append(item)
                continue
            if name == 'uniform-paragraphs':
                paras=[pm for pm in re.finditer(r'[^\n]+', t) if len(re.findall(r'\b\w+\b', pm.group(0)))>=40]
                lens=[len(re.findall(r'\b\w+\b', pm.group(0))) for pm in paras]; matches=[]; i=0
                while i+5<=len(lens):
                    w=lens[i:i+5]; mean=sum(w)/5
                    if all(abs(x-mean)<=0.15*mean for x in w): matches.append(paras[i]); i+=5
                    else: i+=1
                if matches:
                    rate=len(matches)*1000/max(words,1)
                    for m in matches:
                        item=finding(t,path,name,m,fix,rate); item['severity']='rate'; item['limit_per_1000']=limit; item['over_limit']=True; item['span']=item['span'][:80]; out.append(item)
                continue
            if name == 'same-opener-run':
                sentences_found = list(re.finditer(r'[^.!?]+[.!?](?:\s+|$)', masked))
                matches=[]; start=0; run=[]
                for sentence_match in sentences_found:
                    sentence=sentence_match.group(0)
                    opener=re.match(r'\s*([A-ZÁÉÍÓÚÂÊÔÃÕÇ][\wÀ-ÿ-]{1,18})\b', sentence)
                    key=opener.group(1).casefold() if opener else None
                    if key and run and key == run[-1][0]:
                        run.append((key,sentence_match))
                    else:
                        if len(run)>=3:
                            matches.append(run[0][1])
                        run=[(key,sentence_match)] if key else []
                if len(run)>=3: matches.append(run[0][1])
            else:
                matches=list(re.finditer(pat,masked,re.I|re.M))
            if len(matches)<2: continue
            rate=len(matches)*1000/max(words,1)
            for m in matches:
                item=finding(t,path,name,m,fix,rate)
                item['severity']='rate'; item['limit_per_1000']=limit; item['over_limit']=rate>limit
                out.append(item)
    rate=len(out)*1000/max(words,1)
    density={}
    for name,(_,limit,_) in RATE.items():
        hits=[f for f in out if f['rule']==name]
        if hits:
            density[name]={'count':len(hits),'per_1000':hits[0]['per_1000'],
                           'limit_per_1000':limit,'over_limit':hits[0]['over_limit']}
    exceeded=budget is not None and rate>budget
    return {'file':path,'words':words,'sentences':sentences,'finding_count':len(out),'findings_per_1000':round(rate,3),'density':density,'budget_per_1000':budget,'status':'FAIL' if exceeded else 'PASS','findings':out}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('paths',nargs='+'); ap.add_argument('--json',action='store_true'); ap.add_argument('--max-per-1000',type=float,default=None)
    a=ap.parse_args(); files=[]
    for p in a.paths:
        if os.path.isdir(p):
            for root,_,names in os.walk(p): files += [os.path.join(root,n) for n in names if n.lower().endswith(('.html','.md','.txt'))]
        else: files.append(p)
    results=[lint(p,a.max_per_1000) for p in sorted(set(files))]
    if a.json: print(json.dumps({'files':results},ensure_ascii=False,indent=2))
    else:
        for r in results:
            print(f"{r['status']} {r['file']} ({r['words']} words; {r['sentences']} sentences; {r['finding_count']} findings; {r['findings_per_1000']}/1000)")
            for rule,summary in r['density'].items():
                print(f"  rate {rule}: {summary['per_1000']}/1000 (review limit {summary['limit_per_1000']}; over={summary['over_limit']})")
            for f in r['findings']:
                print(f"  line {f['line']} {f['rule']}: {f['span']!r} — {f['fix']}")
    sys.exit(1 if any(r['status']=='FAIL' for r in results) else 0)
if __name__=='__main__': main()
