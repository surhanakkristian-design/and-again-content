import json
p='content/7319.json'; d=json.load(open(p))
new={0.2:dict(x=0.08,y=0.18,w=0.64,h=0.82),0.7:dict(x=0.2,y=0.2,w=0.5,h=0.65),1.2:dict(x=0.3,y=0.21,w=0.4,h=0.48),1.7:dict(x=0.37,y=0.21,w=0.32,h=0.38)}
for k in d['taps'][0]['keys']:
    if k['t'] in new: k.update(new[k['t']])
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
