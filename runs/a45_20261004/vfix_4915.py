import json
p='content/4915.json'; c=json.load(open(p))
for i,k in enumerate(c['taps'][1]['keys']):
    if abs(k['t']-6.0)<0.01: c['taps'][1]['keys'][i]=dict(t=6.0,x=0.53,y=0.68,w=0.22,h=0.32)
c['notes']+=' VERIFIER: 6.0 the girl in the dress is visible (tie-dye hem + legs behind the curly-haired man): box on.'
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
