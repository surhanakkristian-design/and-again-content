import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,c): json.dump(c, open(f'content/{i}.json','w'), ensure_ascii=False, indent=1)
def setk(tap,t,**kw):
    for n,k in enumerate(tap['keys']):
        if abs(k['t']-t)<0.01:
            tap['keys'][n]={'t':k['t'],**kw} if 'x' in kw and len(kw)==4 else {**k,**kw}; return
    raise SystemExit('no key')
# 483: man's box misses head / hat
c=load(483); m=c['taps'][2]
setk(m,5.0,y=0.76,h=0.24); setk(m,5.5,y=0.56,h=0.42); setk(m,7.0,y=0.42,h=0.58)
save(483,c)
# 485
c=load(485)
for n in c['nouns']:
    if n['word']=='a braid': n['word']='braids'
    if n['word']=='a fist': n['x'],n['y']=0.80,0.80
save(485,c)
# 486
c=load(486); p=c['taps'][0]; man=c['taps'][2]
setk(p,0.5,x=0.08,y=0.05,w=0.92,h=0.95)
setk(p,1.0,x=0.40,y=0.18,w=0.60,h=0.82)
setk(p,1.5,x=0.38,y=0.28,w=0.62,h=0.72)
setk(p,3.0,x=0.20,y=0.44,w=0.80,h=0.56)
setk(p,3.5,x=0.15,y=0.51,w=0.85,h=0.49)
setk(man,5.5,x=0.0,y=0.60,w=0.20,h=0.40)
setk(man,6.5,x=0.0,y=0.62,w=0.22,h=0.32)
setk(man,7.0,x=0.0,y=0.62,w=0.22,h=0.36)
save(486,c)
