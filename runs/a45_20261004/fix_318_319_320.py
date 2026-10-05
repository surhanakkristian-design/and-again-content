import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,c): json.dump(c,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
def setk(tap,t,**kw):
    for n,k in enumerate(tap['keys']):
        if abs(k['t']-t)<0.01:
            if 'off' in k: tap['keys'][n]={'t':k['t'],**kw}
            else: k.update(kw)
            return
    raise SystemExit('no key')
# 318
c=load(318); red,green,blue=c['taps']
setk(green,1.0,h=0.87); setk(blue,1.0,y=0.87,h=0.13)
setk(green,8.0,h=0.86); setk(blue,8.0,x=0.5,y=0.86,w=0.2,h=0.14)
setk(green,8.5,h=0.78); setk(blue,8.5,x=0.54,y=0.86,w=0.18,h=0.14)
setk(green,9.0,h=0.68); setk(blue,9.0,x=0.5,y=0.86,w=0.22,h=0.14)
setk(green,9.5,h=0.8);  setk(blue,9.5,x=0.5,y=0.86,w=0.22,h=0.14)
save(318,c)
# 319
c=load(319); f1,f2,fish=c['taps']
for f in (f1,f2):
    setk(f,1.5,w=0.52); setk(f,3.0,h=0.28); setk(f,3.5,h=0.28)
setk(fish,0.0,x=0.66,y=0.8,w=0.34,h=0.2)
setk(fish,0.5,x=0.7,y=0.78,w=0.3,h=0.2)
setk(fish,1.0,x=0.62,y=0.78,w=0.38,h=0.22)
setk(fish,1.5,x=0.66,y=0.67,w=0.34,h=0.33)
setk(fish,2.0,y=0.68,h=0.3)
setk(fish,2.5,y=0.66,h=0.34)
setk(fish,3.0,x=0.62,y=0.67,w=0.38,h=0.33)
setk(fish,3.5,x=0.62,y=0.68,w=0.38,h=0.32)
setk(fish,5.0,y=0.72,h=0.28)
setk(fish,5.5,y=0.73,h=0.27)
setk(fish,7.5,y=0.72,h=0.28)
save(319,c)
# 320
c=load(320); w,m,web=c['taps']
setk(w,8.5,w=0.44); setk(web,8.5,x=0.44,y=0.08,w=0.18,h=0.24)
save(320,c)
