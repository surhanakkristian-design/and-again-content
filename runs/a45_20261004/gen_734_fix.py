import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,d): json.dump(d,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
def setk(d,target,t,**kw):
    for tap in d['taps']:
        if tap['target']==target:
            for k in tap['keys']:
                if abs(k['t']-t)<1e-6:
                    k.clear(); k['t']=t; k.update(kw)
# 734
d=load(734)
setk(d,'the man',8.0,x=0,y=0,w=0.72,h=0.74)
for tap in d['taps']:
    if tap['target']=='the dog': tap['phrase']='to watch the man'
save(734,d)
# 735
d=load(735)
setk(d,'the man',0.0,x=0.63,y=0.34,w=0.37,h=0.48)
setk(d,'the cat',0.0,x=0.14,y=0.39,w=0.49,h=0.21)
setk(d,'the man',0.5,x=0.60,y=0.33,w=0.40,h=0.50)
setk(d,'the man',1.0,x=0.62,y=0.38,w=0.38,h=0.45)
setk(d,'the man',1.5,x=0.58,y=0.25,w=0.42,h=0.62)
setk(d,'the woman',6.0,x=0.25,y=0.30,w=0.65,h=0.46)
setk(d,'the woman',6.5,x=0.22,y=0.28,w=0.61,h=0.25)
setk(d,'the woman',7.0,x=0.20,y=0.30,w=0.65,h=0.18)
setk(d,'the woman',7.5,x=0.22,y=0.32,w=0.64,h=0.18)
setk(d,'the woman',8.0,x=0.18,y=0.32,w=0.69,h=0.17)
setk(d,'the woman',9.0,x=0.47,y=0.27,w=0.41,h=0.58)
setk(d,'the man',9.0,x=0.88,y=0.30,w=0.12,h=0.70)
save(735,d)
# 736
d=load(736)
for n in d['nouns']:
    if n['word']=='roses': n['x'],n['y']=0.90,0.21
save(736,d)
