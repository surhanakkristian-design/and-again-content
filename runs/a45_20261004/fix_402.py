import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,d): json.dump(d,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
def setk(d,target,t,**kw):
    n=0
    for tap in d['taps']:
        if tap['target']==target:
            for k in tap['keys']:
                if abs(k['t']-t)<1e-6: k.update(kw); n+=1
    assert n
# 402
d=load(402)
setk(d,'the man',1.0,y=0.12,h=0.71)
setk(d,'the woman',1.0,y=0.12,h=0.76)
setk(d,'the man',9.0,y=0.15,h=0.80)
setk(d,'the man',10.0,y=0.15,h=0.70)
save(402,d)
# 4190
d=load(4190)
setk(d,'the male lion',3.0,x=0.13,y=0,w=0.87,h=0.49)
setk(d,'the male lion',3.5,x=0.25,y=0,w=0.75,h=0.47)
setk(d,'the male lion',4.5,x=0.40,w=0.60)
for tap in d['taps']:
    if tap['phrase']=='to look at the camera': tap['phrase']='to be orange and white'
save(4190,d)
# 5652
d=load(5652)
for tap in d['taps']:
    if tap['phrase']=='to be taller than the dog': tap['phrase']='to be the bigger ball'
    if tap['phrase']=='to be the smallest ball': tap['phrase']='to be the smaller ball'
save(5652,d)
