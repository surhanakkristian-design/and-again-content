import json
p='content/5474.json'; c=json.load(open(p))
for k in c['taps'][0]['keys']:
    if abs(k['t']-4.5)<.01: k.update(y=0.34,h=0.66)
for k in c['taps'][1]['keys']:
    if abs(k['t']-4.5)<.01: k.update(x=0.6,y=0,w=0.4,h=0.32)
json.dump(c,open(p,'w'),indent=1)
c=json.load(open(p))
for k in c['taps'][1]['keys']:
    if abs(k['t']-5.5)<.01: k.update(x=0.52,y=0.03,w=0.48,h=0.32)
json.dump(c,open(p,'w'),indent=1)
