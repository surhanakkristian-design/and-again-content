import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,d): json.dump(d,open(f'content/{i}.json','w'),ensure_ascii=False,indent=1)
def setk(tap,t,**kw):
    for k in tap['keys']:
        if k['t']==t:
            k.pop('off',None); k.update(kw); return
    raise SystemExit('no key')
d=load(664)
setk(d['taps'][0],1.0,x=0.66,y=0.18,w=0.34,h=0.82)
setk(d['taps'][1],6.5,x=0,y=0.5,w=0.8,h=0.5)
setk(d['taps'][1],7.0,x=0,y=0.54,w=0.86,h=0.46)
save(664,d)
d=load(668)
m=d['taps'][1]
setk(m,7.5,x=0.78,y=0.18,w=0.18,h=0.3)
setk(m,8.0,x=0.7,y=0,w=0.3,h=0.38)
setk(m,8.5,x=0,y=0,w=0.38,h=1)
d['taps'][2]['phrase']='to walk through water'
d['notes']+=' VERIFIER: phrase 3 changed to "to walk through water" (puddle is above level A); man boxed on his legs at 7.5-8.0 s, his box at 8.5 s now includes his head.'
save(668,d)
