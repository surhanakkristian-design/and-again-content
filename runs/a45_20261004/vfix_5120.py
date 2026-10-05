import json
p='content/5120.json'; d=json.load(open(p))
for k in d['taps'][2]['keys']:
    if k['t']==2.5: k.update(y=0.08,h=0.68)
json.dump(d,open(p,'w'),indent=1)
