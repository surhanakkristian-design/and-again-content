import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,d): json.dump(d,open(f'content/{i}.json','w'),ensure_ascii=False,indent=1)
def setk(d,target,t,box):
    n=0
    for tap in d['taps']:
        if tap['target']==target:
            for j,k in enumerate(tap['keys']):
                if abs(k['t']-t)<1e-6:
                    tap['keys'][j]={'t':k['t'],'x':box[0],'y':box[1],'w':box[2],'h':box[3]}; n+=1
    assert n>=1,(target,t)
def noun(d,w,x,y):
    for n in d['nouns']:
        if n['word']==w: n['x'],n['y']=x,y; return
    raise SystemExit(w)
# 153
d=load(153)
for t,b in {6.0:(0.13,0.34,0.66,0.56),6.5:(0.10,0.40,0.70,0.55),7.0:(0.30,0.14,0.27,0.52),7.5:(0.25,0.08,0.37,0.58)}.items(): setk(d,'the glasses',t,b)
for t,b in {7.0:(0.30,0.72,0.33,0.28),7.5:(0.36,0.68,0.27,0.30),8.0:(0.40,0.60,0.22,0.20),8.5:(0.40,0.57,0.22,0.19),9.0:(0.40,0.55,0.22,0.19),9.5:(0.40,0.55,0.22,0.19),10.0:(0.40,0.53,0.22,0.19)}.items(): setk(d,'the bottle',t,b)
noun(d,'a light bulb',0.5,0.13)
save(153,d)
# 154
d=load(154)
setk(d,'the man',5.0,(0.00,0.30,0.55,0.55))
setk(d,'the man',7.0,(0.51,0.07,0.37,0.90))
setk(d,'the man',7.5,(0.51,0.08,0.38,0.90))
setk(d,'the cat',7.0,(0.89,0.04,0.11,0.22))
setk(d,'the cat',7.5,(0.90,0.05,0.10,0.23))
save(154,d)
# 156
d=load(156)
noun(d,'a medal',0.47,0.84); noun(d,'flags',0.82,0.37); noun(d,'a chest',0.72,0.62)
save(156,d)
# 157
d=load(157)
for t,b in {3.0:(0.0,0.0,0.14,1.0),3.5:(0.0,0.0,0.15,1.0),4.0:(0.0,0.0,0.13,1.0),4.5:(0.0,0.0,0.26,0.45)}.items(): setk(d,'the man',t,b)
setk(d,'the woman',2.0,(0.35,0.15,0.53,0.85))
setk(d,'the bird',2.0,(0.21,0.30,0.13,0.14))
save(157,d)
