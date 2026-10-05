import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,d): json.dump(d,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
def setk(d,target,t,**kw):
    for tap in d['taps']:
        if tap['target']==target:
            for k in tap['keys']:
                if k['t']==t: k.update(kw)
# 812
d=load(812)
for t,wy,wh in [(7.0,0.28,0.59),(7.5,0.30,0.57),(9.0,0.36,0.48),(9.5,0.36,0.48)]:
    setk(d,'the woman',t,y=wy,h=wh)
for t,my in [(7.0,0.88),(7.5,0.88),(9.0,0.86),(9.5,0.86)]:
    setk(d,'the man',t,y=my,h=round(1-my,2))
for n in d['nouns']:
    if n['word']=='a harness': n['x'],n['y']=0.46,0.53
save(812,d)
# 813
d=load(813)
for tap in d['taps']:
    if tap['phrase']=='to open its beak': tap['phrase']='to open its mouth wide'
setk(d,'the big turkey',7.5,h=0.53)
save(813,d)
# 814
d=load(814)
for tap in d['taps']:
    if tap['phrase']=='to blow a pink ribbon': tap['phrase']='to slow down and stop'
setk(d,'the girl',1.0,y=0.31,h=0.69)
save(814,d)
