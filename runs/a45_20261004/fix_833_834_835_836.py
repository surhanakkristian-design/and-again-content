import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,c): json.dump(c, open(f'content/{i}.json','w'), indent=1, ensure_ascii=False)
def setk(c, target, t, **kw):
    n=0
    for tap in c['taps']:
        if tap['target']==target:
            for k in tap['keys']:
                if abs(k['t']-t)<0.01: k.update(kw); n+=1
    assert n, (target,t)
c=load(833); setk(c,'the woman',9.0,y=0.11,h=0.56); save(833,c)
c=load(834)
for t in (9.0,9.5):
    setk(c,'the hostess',t,y=0.13,h=0.38); setk(c,'the man in glasses',t,y=0.52,h=0.48)
save(834,c)
c=load(835)
setk(c,'the man in the blue polo',14.5,y=0.31,h=0.69)
setk(c,'the man in the blue polo',15.0,y=0.33,h=0.67)
for n in c['nouns']:
    if n['word']=='a wrench': n['y']=0.5
    if n['word']=='a toilet': n['y']=0.62
save(835,c)
c=load(836)
b='the boy with the backpack'; g='the girl in the striped sweater'
setk(c,b,11.0,y=0.43,h=0.55); setk(c,b,11.5,y=0.52,h=0.46); setk(c,b,12.0,y=0.52,h=0.44)
setk(c,g,11.0,y=0.28,h=0.54); setk(c,g,11.5,y=0.27,h=0.55); setk(c,g,12.0,y=0.26,h=0.44)
save(836,c)
