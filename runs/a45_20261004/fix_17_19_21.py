import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,c): json.dump(c, open(f'content/{i}.json','w'), indent=1, ensure_ascii=False)
def setk(tap, t, **kw):
    for n,k in enumerate(tap['keys']):
        if abs(k['t']-t)<0.01:
            tap['keys'][n] = {'t': k['t'], **kw}; return
    raise SystemExit(f'no key {t}')
B=lambda x,y,w,h: dict(x=x,y=y,w=w,h=h)
# 17
c=load(17); cap,wom,shed=c['taps']
setk(cap,6.5,**B(0.84,0.27,0.16,0.41)); setk(wom,6.5,**B(0.56,0.33,0.28,0.65))
setk(cap,8.5,**B(0,0.18,0.14,0.6))
setk(cap,9.0,**B(0,0.12,0.56,0.37))
setk(shed,7.0,**B(0.05,0.25,0.74,0.62)); setk(shed,7.5,**B(0.07,0.25,0.67,0.61))
setk(shed,8.0,**B(0.2,0.03,0.8,0.8)); setk(shed,8.5,**B(0.14,0,0.86,0.82))
setk(shed,9.0,**B(0,0.49,1,0.51)); setk(shed,9.5,**B(0,0,1,0.6)); setk(shed,10.0,**B(0,0,1,0.45))
save(17,c)
# 19
c=load(19); man,book,ruler=c['taps']
setk(man,0.0,**B(0,0.04,1,0.84)); setk(man,2.5,**B(0,0.1,1,0.55))
setk(book,4.5,**B(0.5,0.33,0.5,0.27))
save(19,c)
# 21
c=load(21); hand,stu,sch=c['taps']
setk(stu,6.5,**B(0.03,0.31,0.89,0.34)); setk(stu,7.5,**B(0,0.36,0.88,0.6))
setk(sch,13.0,**B(0,0.22,1,0.4)); setk(sch,14.0,**B(0,0,1,0.44))
save(21,c)
