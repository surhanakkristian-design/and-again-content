import json
def ld(i): return json.load(open(f'content/{i}.json'))
def sv(i,c): json.dump(c, open(f'content/{i}.json','w'), indent=1, ensure_ascii=False)
def setk(tap, t, **kw):
    for k in tap['keys']:
        if abs(k['t']-t)<0.01:
            k.clear(); k['t']=t; k.update(kw)
c=ld(5014)
c['taps'][1]['phrase']='to hold a hot dish'
setk(c['taps'][1],4.0,x=0.2,y=0.2,w=0.8,h=0.7)
setk(c['taps'][2],9.0,x=0.08,y=0.36,w=0.84,h=0.33)
setk(c['taps'][2],10.0,x=0.21,y=0.4,w=0.56,h=0.25)
c['question']='What is the woman holding?'
c['answer']=['She','is','holding','a','hot','dish.']
sv(5014,c)
c=ld(5016)
setk(c['taps'][2],2.0,x=0.86,y=0.3,w=0.14,h=0.7)
setk(c['taps'][2],2.5,x=0.87,y=0.25,w=0.13,h=0.75)
for n in c['nouns']:
    if n['word']=='a knee': n['x']=0.43; n['y']=0.7
sv(5016,c)
