import json
p='content/5144.json'; c=json.load(open(p))
for k in c['taps'][1]['keys']:
    if abs(k['t']-2.5)<0.01: k.update(y=0.18,h=0.82)
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
