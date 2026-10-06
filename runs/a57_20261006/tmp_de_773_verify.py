import json
def fix(i, row, text, add):
    p=f'content/de/{i}.json'; d=json.load(open(p))
    for part in d['recall'][row]['parts']:
        if part['text']==text and part.get('gap'):
            for a in add:
                if a not in part['accept']: part['accept'].append(a)
            break
    else: raise SystemExit(f'not found {i} {text}')
    json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
fix(773,0,'Fieber',['Temperatur'])
fix(4755,0,'Röntgenbild',['Bild'])
fix(137,2,'Felsen',['Felswänden'])
