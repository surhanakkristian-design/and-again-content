import json
def fix(i, rowidx, add):
    p=f'content/es/{i}.json'; d=json.load(open(p))
    for part in d['recall'][rowidx]['parts']:
        if part.get('gap'):
            if add not in part['accept']: part['accept'].append(add)
    json.dump(d,open(p,'w'),ensure_ascii=False,indent=1); open(p,'a').write('\n') if False else None
fix(4210,1,'cara')
fix(72,3,'básquet')
