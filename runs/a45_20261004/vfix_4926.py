import json
p='content/4926.json'; d=json.load(open(p))
for tp in d['taps']:
    for k in tp['keys']:
        if tp['target']=='the man':
            if k['t']==0.0: k.clear(); k.update(t=0.0,x=0.71,y=0.7,w=0.29,h=0.3)
            if k['t']==0.5: k.clear(); k.update(t=0.5,x=0.45,y=0.72,w=0.55,h=0.28)
        else:
            if k['t']==0.5: k.update(x=0,y=0,w=1,h=0.71)
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
