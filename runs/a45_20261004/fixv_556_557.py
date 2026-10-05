import json
def fix(i, target, edits):
    p=f'content/{i}.json'; d=json.load(open(p))
    for tp in d['taps']:
        if tp['target']==target:
            for k in tp['keys']:
                if k['t'] in edits: k.update(edits[k['t']])
    json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
fix(556,'the woman',{5.0:dict(x=0,y=0.38,w=0.2,h=0.54)})
fix(557,'the woman',{9.0:dict(x=0.05,y=0.12,w=0.45,h=0.57),9.5:dict(x=0.12,y=0.13,w=0.42,h=0.57)})
