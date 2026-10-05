import json
p='content/4488.json'; c=json.load(open(p))
m=max(k['y']+k['h'] for k in c['taps'][0]['keys']); print('man bottom max',m)
for k in c['taps'][2]['keys']: k.update(x=0.0,y=0.71,w=0.82,h=0.29)
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
