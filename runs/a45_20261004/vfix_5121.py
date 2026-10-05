import json
p='content/5121.json'; d=json.load(open(p))
for k in d['taps'][1]['keys']:
    if k['t']==7.0: k.update(x=0.70,w=0.30)
for n in d['nouns']:
    if n['word']=='a rack': n.update(word='an oven',x=0.12,y=0.27)
json.dump(d,open(p,'w'),indent=1)
