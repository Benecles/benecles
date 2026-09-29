import re,html,json
def text(fn):
    s=open(fn,'rb').read().decode('cp1252',errors='replace')
    s=re.sub(r'(?is)<(strike|s|del)\b.*?</\1>','',s)
    s=re.sub(r'(?is)<(script|style)\b.*?</\1>','',s)
    s=re.sub(r'(?i)<br\s*/?>','\n',s)
    s=re.sub(r'(?i)</(p|div|h\d|li|tr)>','\n',s)
    s=re.sub(r'<[^>]+>','',s)
    s=html.unescape(s).replace('\xa0',' ')
    s=re.sub(r'[ \t]+',' ',s)
    lines=[l.strip() for l in s.split('\n')]
    return [l for l in lines if l]
def articles(lines):
    arts={}; cur=None
    for l in lines:
        m=re.match(r'^Art\.\s*(\d+(?:\.\d+)?)\s*[º°o]?(-[A-Z])?\s*[\.\-–]?',l)
        if m:
            num=m.group(1).replace('.','')+(m.group(2) or '')
            cur=num; arts.setdefault(cur,[]).append(l); continue
        if cur and re.match(r'^(CAPÍTULO|TÍTULO|Seção|SEÇÃO|LIVRO|Subseção)',l): cur=None; continue
        if cur: arts[cur].append(l)
    return arts
cc=articles(text('cc.htm')); cdc=articles(text('cdc.htm'))
json.dump({'cc':cc,'cdc':cdc},open('law.json','w'),ensure_ascii=False)
print(len(cc),len(cdc)); print('\n'.join(cc['421'])); print('\n'.join(cc['421-A'][:3])); print('\n'.join(cc['418'])); print('\n'.join(cdc['47'])); print(cc.get('456'))
