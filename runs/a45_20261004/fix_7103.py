import json
p='content/7103.json'; d=json.load(open(p))
for k in d['taps'][0]['keys']:
    if k['t']==0.2: k.update(x=0.56,w=0.19,h=0.15)
    if k['t']==0.7: k.update(w=0.19)
    if k['t']==1.2: k.update(y=0.27,h=0.15)
    if k['t']==2.7: k.update(x=0.59,w=0.19,h=0.15)
json.dump(d,open(p,'w'),indent=1)
