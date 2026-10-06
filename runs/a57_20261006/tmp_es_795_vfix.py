import json
def add(i, rowtext_gap, extra):
    p=f'content/es/{i}.json'; d=json.load(open(p))
    for r in d['recall']:
        for x in r['parts']:
            if x.get('gap') and x['text']==rowtext_gap:
                for e in extra:
                    if e not in x['accept']: x['accept'].append(e)
    json.dump(d,open(p,'w'),ensure_ascii=False,indent=1); open(p,'a').write('\n')
add(385,'golpear',['batear'])
add(7212,'mirar',['observar'])
add(7773,'Lleva',['Trae'])
add(7773,'levantar',['alzar'])
add(528,'aparcar',['estacionar'])
