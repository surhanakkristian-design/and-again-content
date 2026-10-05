import json
p='content/4755.json'; d=json.load(open(p))
new={('the man',1.0):dict(x=0.73,y=0.42,w=0.27,h=0.58),('the man',1.5):dict(x=0.71,y=0.43,w=0.29,h=0.57),
('the X-ray',1.0):dict(x=0.33,y=0.23,w=0.39,h=0.34),('the X-ray',1.5):dict(x=0.28,y=0.22,w=0.42,h=0.35)}
for t in d['taps']:
    for k in t['keys']:
        v=new.get((t['target'],k['t']))
        if v: k.update(v)
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
