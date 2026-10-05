import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,d): json.dump(d,open(f'content/{i}.json','w'),ensure_ascii=False,indent=1)
def setk(d,target,t,**kw):
    for tap in d['taps']:
        if tap['target']==target:
            for j,k in enumerate(tap['keys']):
                if abs(k['t']-t)<1e-6:
                    tap['keys'][j]={'t':k['t'],**kw}
d=load(439)
setk(d,'the dog',7.0,x=0,y=0.62,w=0.28,h=0.36)
setk(d,'the red flowers',5.5,x=0.26,y=0.11,w=0.5,h=0.39)
setk(d,'the red flowers',7.0,x=0.01,y=0.22,w=0.33,h=0.26)
save(439,d)
d=load(440)
setk(d,'the man',5.0,x=0,y=0.28,w=0.98,h=0.72)
for n in d['nouns']:
    if n['word']=='a belt': n['x'],n['y']=0.40,0.85
save(440,d)
d=load(442)
setk(d,'the woman',6.5,x=0.07,y=0.22,w=0.33,h=0.78)
setk(d,'the man',6.5,x=0.6,y=0.23,w=0.4,h=0.77)
setk(d,'the woman',7.0,x=0.14,y=0.25,w=0.29,h=0.73)
setk(d,'the man',7.0,x=0.58,y=0.26,w=0.36,h=0.72)
save(442,d)
