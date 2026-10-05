import json
p='content/4884.json'; c=json.load(open(p))
for k in c['taps'][2]['keys']:
    if abs(k['t']-4.0)<.01: k.clear(); k.update(t=4.0,x=0.0,y=0.22,w=1.0,h=0.13)
    if abs(k['t']-4.5)<.01: k.clear(); k.update(t=4.5,x=0.0,y=0.24,w=1.0,h=0.13)
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
