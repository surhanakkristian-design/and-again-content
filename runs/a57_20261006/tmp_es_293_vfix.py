import json
def fix(i,gap,add):
    p=f'content/es/{i}.json'; d=json.load(open(p))
    for r in d['recall']:
        for part in r['parts']:
            if part.get('gap') and part['text']==gap and add not in part['accept']:
                part['accept'].append(add)
    json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
fix(293,'montada','puesta')
fix(294,'tronco','leño')
