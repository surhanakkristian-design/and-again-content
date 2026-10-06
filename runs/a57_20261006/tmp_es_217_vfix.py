import json
def fix(i, rowidx, gaptext, add):
    p=f'content/es/{i}.json'; d=json.load(open(p))
    for part in d['recall'][rowidx]['parts']:
        if part.get('gap') and part['text']==gaptext:
            for a in add:
                if a not in part['accept']: part['accept'].append(a)
    json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
fix(217,2,'centro',['blanco'])
fix(220,3,'pescado',['filete'])
