import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,d): json.dump(d,open(f'content/{i}.json','w'),ensure_ascii=False,indent=1)
def setk(tap,t,**kw):
    for k in tap['keys']:
        if k['t']==t:
            k.clear(); k['t']=t; k.update(kw); return
    raise SystemExit('no key')
d=load(4224)
liz,door=d['taps'][0],d['taps'][1]
setk(door,0.0,x=0.68,y=0.08,w=0.23,h=0.72)
setk(door,0.5,x=0.71,y=0.08,w=0.20,h=0.72)
setk(door,1.0,x=0.71,y=0.08,w=0.20,h=0.72)
setk(liz,10.5,x=0.14,y=0.24,w=0.50,h=0.56); setk(door,10.5,x=0.64,y=0.08,w=0.20,h=0.71)
setk(liz,11.0,x=0.17,y=0.20,w=0.47,h=0.60); setk(door,11.0,x=0.64,y=0.08,w=0.20,h=0.71)
setk(liz,11.5,x=0.13,y=0.25,w=0.51,h=0.55); setk(door,11.5,x=0.64,y=0.08,w=0.20,h=0.71)
save(4224,d)
d=load(4225)
d['taps'][1]['phrase']='to stand behind the box'
save(4225,d)
d=load(4226)
setk(d['taps'][0],7.0,x=0.50,y=0.12,w=0.45,h=0.19)
setk(d['taps'][1],7.0,x=0.30,y=0.31,w=0.70,h=0.26)
save(4226,d)
