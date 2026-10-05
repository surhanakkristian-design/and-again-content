import json
p='content/4892.json'; c=json.load(open(p))
c['taps'][1]['phrase']='to laugh on the water slide'
for tap in c['taps']:
    for k in tap['keys']:
        if abs(k['t']-1.5)<.01: k.update(x=0.0,w=0.70)
        if abs(k['t']-2.5)<.01: k.update(x=0.0,w=0.78)
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
