import json
p='content/5156.json'; c=json.load(open(p))
for t in c['taps'][:2]:
    for k in t['keys']:
        if k['t']==2.5: k.update(x=0.44,y=0.27,w=0.27,h=0.25)
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
