import json
def setk(d, target, t, **kw):
    for tp in d['taps']:
        if tp['target']==target:
            for k in tp['keys']:
                if abs(k['t']-t)<1e-6: k.update(kw)
p='content/7786.json'; d=json.load(open(p))
for t,x,w in [(0.2,0.24,0.29),(0.7,0.24,0.35),(1.2,0.20,0.36),(1.7,0.16,0.37)]:
    setk(d,'the sofa',t,x=x,w=w)
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
p='content/7787.json'; d=json.load(open(p))
for t,x,w in [(0.2,0.22,0.66),(0.7,0.23,0.63),(1.2,0.24,0.56),(1.7,0.26,0.52)]:
    setk(d,'the woman in the cap',t,x=x,w=w)
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
