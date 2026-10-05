import json
c=json.load(open('content/387.json'))
for t in c['taps']:
    for k in t['keys']:
        if k['t']==7.0:
            if t['target']=='the dog': k.update(x=0.18,y=0.51,w=0.32,h=0.35)
            else: k.update(x=0.4,y=0.36,w=0.6,h=0.15)
json.dump(c,open('content/387.json','w'),indent=1,ensure_ascii=False)
