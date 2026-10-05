import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,d): json.dump(d,open(f'content/{i}.json','w'),ensure_ascii=False,indent=1)
def setk(d,target,t,**kw):
    for tap in d['taps']:
        if tap['target']==target:
            for j,k in enumerate(tap['keys']):
                if k['t']==t: tap['keys'][j]=dict(t=t,**kw)
# 322
d=load(322)
setk(d,'the woman',9.0,x=0.05,y=0.02,w=0.45,h=0.43)
setk(d,'the man',9.0,x=0.5,y=0.21,w=0.45,h=0.44)
setk(d,'the woman',9.5,x=0.05,y=0.07,w=0.58,h=0.6)
setk(d,'the man',9.5,x=0.63,y=0.27,w=0.37,h=0.45)
d['question']="What is the woman doing?"
d['answer']=["She","is","placing","a","huge","bet."]
save(322,d)
# 323
d=load(323)
setk(d,'the woman with red hair',0.5,x=0.24,y=0.17,w=0.76,h=0.83)
setk(d,'the man in green',0.5,x=0.24,y=0.03,w=0.22,h=0.14)
setk(d,'the man in green',5.0,x=0.12,y=0.40,w=0.26,h=0.14)
setk(d,'the ball',5.0,x=0.22,y=0.54,w=0.18,h=0.14)
save(323,d)
# 326
d=load(326)
setk(d,'the man',9.0,x=0.44,y=0.23,w=0.27,h=0.42)
for tap in d['taps']:
    if tap['target']=='the cat': tap['phrase']='to walk near the man'
save(326,d)
# 327
d=load(327)
for tap in d['taps']:
    if tap['target']=='the bee': tap['phrase']='to fly near the flowers'
save(327,d)
