import json
p='content/447.json'; c=json.load(open(p))
def setk(i,t,**kw):
    for k in c['taps'][i]['keys']:
        if abs(k['t']-t)<0.01:
            k.clear(); k['t']=t; k.update(kw); return
    raise SystemExit('no key')
# dog
setk(2,1.0,x=0.12,y=0.18,w=0.2,h=0.18)
setk(2,1.5,x=0.17,y=0.15,w=0.17,h=0.2)
setk(2,3.5,x=0.21,y=0.1,w=0.2,h=0.19)
setk(2,4.0,x=0.2,y=0.09,w=0.21,h=0.19)
setk(2,4.5,x=0.2,y=0.09,w=0.21,h=0.19)
setk(2,5.0,x=0.2,y=0.08,w=0.19,h=0.18)
# woman: close-ups, keep mouth + hand with the lip balm
setk(0,3.5,x=0.21,y=0.3,w=0.79,h=0.7)
setk(0,4.0,x=0.2,y=0.29,w=0.8,h=0.71)
setk(0,4.5,x=0.2,y=0.29,w=0.8,h=0.71)
setk(0,5.0,x=0.2,y=0.27,w=0.8,h=0.73)
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
