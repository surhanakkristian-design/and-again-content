import json
def setk(d, target, t, **kw):
    for tap in d['taps']:
        if tap['target']==target:
            for i,k in enumerate(tap['keys']):
                if k['t']==t:
                    tap['keys'][i]={'t':t,**kw}
p='content/4404.json'; d=json.load(open(p))
setk(d,'the man',1.5,x=0.0,y=0.10,w=0.88,h=0.90)
setk(d,'the man',2.0,x=0.0,y=0.08,w=1.0,h=0.92)
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
p='content/4406.json'; d=json.load(open(p))
setk(d,'the makeup artist',8.5,x=0.0,y=0.25,w=0.18,h=0.75)
setk(d,'the woman',8.5,x=0.19,y=0.10,w=0.81,h=0.90)
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
