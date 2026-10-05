import json
p='content/5142.json'; c=json.load(open(p))
def setk(tap,t,**v):
    for k in tap['keys']:
        if abs(k['t']-t)<0.01: k.clear(); k.update(dict(t=t,**v))
man,girl,nb=c['taps']
setk(man,5.0,x=0.0,y=0.25,w=0.92,h=0.75)
setk(nb,8.5,x=0.5,y=0.33,w=0.29,h=0.16)
setk(man,9.0,x=0.51,y=0.37,w=0.42,h=0.63)
setk(nb,9.0,x=0.29,y=0.34,w=0.22,h=0.18)
setk(nb,9.5,x=0.08,y=0.32,w=0.88,h=0.10)
setk(man,9.5,x=0.3,y=0.42,w=0.42,h=0.58)
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
