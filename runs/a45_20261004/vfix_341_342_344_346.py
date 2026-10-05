import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,c): json.dump(c, open(f'content/{i}.json','w'), indent=1, ensure_ascii=False)
def setk(c, target, t, **kw):
    for tap in c['taps']:
        if tap['target']==target:
            for k in tap['keys']:
                if abs(k['t']-t)<0.01: k.update(kw)
c=load(341); setk(c,'the goat',6.0,w=0.93); save(341,c)
c=load(342)
setk(c,'the man',2.0,x=0,w=1); setk(c,'the man',2.5,x=0,w=1)
for n in c['nouns']:
    if n['word']=='water': n['x'],n['y']=0.66,0.07
c['answer']=["She","is","putting on","blue","goggles."]
save(342,c)
c=load(344); setk(c,'the woman',9.0,y=0.22,h=0.63); save(344,c)
c=load(346)
setk(c,'the woman',0.5,y=0.32,w=0.42,h=0.68)
setk(c,'the woman',6.0,h=0.17); setk(c,'the ball',6.0,y=0.47)
save(346,c)
