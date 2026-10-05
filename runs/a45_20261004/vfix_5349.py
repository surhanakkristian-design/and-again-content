import json
p='content/5349.json'; d=json.load(open(p))
t=d['taps'][1]
t['phrase']="to shake the officer's hand"
for k in t['keys']:
    if k['t']==2.0: k.update(x=0.59,y=0.15,w=0.19,h=0.79)
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
