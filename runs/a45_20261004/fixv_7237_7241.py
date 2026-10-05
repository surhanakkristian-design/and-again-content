import json
p='content/7237.json'; d=json.load(open(p))
f=d['taps'][2]; f['phrase']='to flicker on a metal rod'
for k in f['keys']:
    if k['t']==0.2: k.update(x=0.17,w=0.18)
    if k['t']==0.7: k.update(x=0.18,w=0.18)
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
p='content/7241.json'; d=json.load(open(p))
for tap in d['taps'][:2]:
    for k in tap['keys']:
        if k['t']==3.2: k.update(x=0.0,y=0.43,w=0.91,h=0.57)
        if k['t']==3.7: k.update(x=0.0,y=0.42,w=0.93,h=0.58)
for k in d['taps'][2]['keys']:
    if k['t']==3.2: k.clear(); k.update(t=3.2,x=0.37,y=0.29,w=0.18,h=0.14)
    if k['t']==3.7: k.clear(); k.update(t=3.7,x=0.33,y=0.28,w=0.18,h=0.14)
d['notes']="Pilot's head stays visible beside her head at 3.2/3.7 s: boxes split by y there (woman box starts at her forehead). Dog and shouting man skipped as targets because their boxes would overlap hers."
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
