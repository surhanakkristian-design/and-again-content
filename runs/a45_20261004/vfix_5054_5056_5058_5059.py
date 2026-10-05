import json
def setk(c, targets, t, **kw):
    for tap in c['taps']:
        if tap['target'] in targets:
            for k in tap['keys']:
                if abs(k['t']-t)<0.01:
                    k.clear(); k.update({'t':t, **kw})
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,c): json.dump(c, open(f'content/{i}.json','w'), indent=1, ensure_ascii=False)
c=load(5054); M=['the man']
setk(c,M,1.0,x=0.03,y=0.18,w=0.97,h=0.82)
setk(c,M,3.0,x=0.11,y=0.14,w=0.57,h=0.66)
setk(c,M,5.0,x=0.14,y=0.29,w=0.86,h=0.67)
setk(c,M,5.5,x=0.42,y=0.20,w=0.58,h=0.77)
save(5054,c)
c=load(5056); M=['the maid']
setk(c,M,1.0,x=0.38,y=0.32,w=0.29,h=0.43)
setk(c,M,5.0,x=0.12,y=0.05,w=0.88,h=0.63)
save(5056,c)
c=load(5058); P=['the postman']
setk(c,P,4.5,x=0.34,y=0.11,w=0.66,h=0.89)
setk(c,P,5.0,x=0.28,y=0.12,w=0.72,h=0.88)
setk(c,P,5.5,x=0.29,y=0.12,w=0.71,h=0.88)
setk(c,P,6.0,x=0.35,y=0.10,w=0.65,h=0.90)
setk(c,P,6.5,x=0.27,y=0.10,w=0.73,h=0.90)
setk(c,P,7.0,x=0.36,y=0.11,w=0.64,h=0.89)
save(5058,c)
c=load(5059); M=['the man']; P=['the postman']
setk(c,M,1.0,x=0.42,y=0.0,w=0.58,h=1.0)
setk(c,M,7.5,x=0.65,y=0.20,w=0.35,h=0.72)
setk(c,M,8.0,x=0.12,y=0.16,w=0.88,h=0.84)
setk(c,P,6.0,x=0.36,y=0.0,w=0.64,h=1.0)
for n in c['nouns']:
    if n['word']=='a box': n['word']='a parcel'
save(5059,c)
