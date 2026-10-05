import json
def setk(c, tap, t, **kw):
    for k in c['taps'][tap]['keys']:
        if abs(k['t']-t)<0.01:
            k.clear(); k['t']=t; k.update(kw); return
    raise SystemExit(f'no key {t}')
p='content/5457.json'; c=json.load(open(p))
setk(c,2,4.0,x=0.26,y=0.33,w=0.18,h=0.38); setk(c,0,4.0,x=0.44,y=0.37,w=0.28,h=0.63)
setk(c,2,6.0,x=0.38,y=0.40,w=0.20,h=0.22); setk(c,1,6.0,x=0.58,y=0.04,w=0.42,h=0.66)
setk(c,2,6.5,x=0.38,y=0.35,w=0.18,h=0.24); setk(c,1,6.5,x=0.56,y=0.08,w=0.44,h=0.62)
setk(c,2,7.0,x=0.42,y=0.35,w=0.18,h=0.22); setk(c,1,7.0,x=0.60,y=0.12,w=0.40,h=0.75)
setk(c,2,7.5,x=0.44,y=0.35,w=0.18,h=0.25); setk(c,1,7.5,x=0.62,y=0.08,w=0.38,h=0.75)
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
p='content/5461.json'; c=json.load(open(p))
setk(c,2,7.0,x=0.10,y=0.30,w=0.74,h=0.67)
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
