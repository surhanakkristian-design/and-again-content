import json
p='content/6975.json'; d=json.load(open(p))
new={2.7:dict(x=0.08,y=0.17,w=0.30,h=0.23),3.2:dict(x=0.05,y=0.13,w=0.32,h=0.23),3.7:dict(x=0.06,y=0.12,w=0.31,h=0.24)}
for k in d['taps'][2]['keys']:
    if k['t'] in new: k.update(new[k['t']])
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
