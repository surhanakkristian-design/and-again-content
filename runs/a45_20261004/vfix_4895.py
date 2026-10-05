import json
p='content/4895.json'; c=json.load(open(p))
for k in c['taps'][1]['keys']:
    if abs(k['t']-2.0)<.01: k.clear(); k.update(t=2.0,x=0.65,y=0.51,w=0.21,h=0.40)
for k in c['taps'][2]['keys']:
    if abs(k['t']-2.0)<.01: k.clear(); k.update(t=2.0,x=0.86,y=0.66,w=0.14,h=0.34)
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
