import json
c=json.load(open('content/386.json'))
for t in c['taps']:
    if t['target']=='the man':
        for k in t['keys']:
            if k['t']==3.0: k.update(x=0.0,y=0.08,w=0.4,h=0.92)
json.dump(c,open('content/386.json','w'),indent=1,ensure_ascii=False)
