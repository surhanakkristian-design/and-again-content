import json
p='content/4763.json'; c=json.load(open(p))
new={3.0:(0.00,0.09,0.93,0.86),3.5:(0.00,0.15,0.80,0.80),4.0:(0.00,0.17,0.80,0.78)}
for tap in c['taps']:
    if tap['target']!='the woman at the desk': continue
    for k in tap['keys']:
        for t,(x,y,w,h) in new.items():
            if abs(k['t']-t)<0.01: k.update(x=x,y=y,w=w,h=h)
json.dump(c,open(p,'w'),ensure_ascii=False,indent=2)
