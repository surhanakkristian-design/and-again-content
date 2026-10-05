import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,c): json.dump(c,open(f'content/{i}.json','w'),ensure_ascii=False,indent=2)
def setk(tap,t,**kw):
    for n,k in enumerate(tap['keys']):
        if abs(k['t']-t)<1e-6:
            tap['keys'][n]={'t':k['t'],**kw}; return
    raise SystemExit(f'no key {t}')
# 788
c=load(788); boy,girl,mw=c['taps']
setk(mw,1.0,x=0.46,y=0.42,w=0.54,h=0.36)
setk(mw,1.5,x=0.47,y=0.42,w=0.53,h=0.36)
for t in (3.5,4.0,4.5): setk(mw,t,x=0.0,y=0.66,w=1.0,h=0.34)
setk(boy,9.0,x=0.0,y=0.24,w=0.49,h=0.76)
c['notes']+=" VERIFIER: microwave box raised at 1.0/1.5 (its top was cut); 3.5-4.5 (view from inside the oven) microwave = the strip below the boy; boy box at 9.0 padded on top."
save(788,c)
# 4143
c=load(4143); rac,bag,bush=c['taps']
rac['phrase']='to try to escape'; bush['phrase']='to grow in the background'
setk(rac,5.5,x=0.33,y=0.48,w=0.42,h=0.32)
c['answer']=['It','is','trying','to','escape','from','the','bin.']
c['notes']+=" VERIFIER: phrases 1 and 3 and the answer lifted to level B (escape, background); raccoon box at 5.5 padded on the left."
save(4143,c)
# 6908
c=load(6908); w,buf,hat=c['taps']
setk(buf,2.7,x=0.55,y=0.20,w=0.45,h=0.60)
setk(buf,3.2,x=0.58,y=0.21,w=0.42,h=0.60)
setk(buf,3.7,x=0.60,y=0.22,w=0.40,h=0.60)
c['notes']+=" VERIFIER: buffalo box padded on the left at 2.7-3.7."
save(6908,c)
