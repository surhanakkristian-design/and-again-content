import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,c): json.dump(c,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
def setk(c,target,t,**kw):
    n=0
    for tap in c['taps']:
        if tap['target']==target:
            for i,k in enumerate(tap['keys']):
                if abs(k['t']-t)<0.01:
                    tap['keys'][i]={'t':k['t'],**kw}; n+=1
    assert n, (target,t)
# 584
c=load(584)
setk(c,'the woman',1.5,x=0.22,y=0.21,w=0.38,h=0.79)
setk(c,'the woman',5.0,x=0.02,y=0.18,w=0.52,h=0.82)
setk(c,'the woman',5.5,x=0.02,y=0.18,w=0.57,h=0.82)
setk(c,'the man',1.5,x=0.61,y=0.19,w=0.39,h=0.68)
setk(c,'the man',3.0,x=0.65,y=0.43,w=0.35,h=0.44)
setk(c,'the man',3.5,x=0.65,y=0.42,w=0.35,h=0.45)
setk(c,'the man',4.0,x=0.64,y=0.28,w=0.36,h=0.59)
setk(c,'the man',5.5,x=0.6,y=0.29,w=0.4,h=0.71)
save(584,c)
# 585
c=load(585)
assert c['taps'][1]['phrase']=='to sit on a black box'
c['taps'][1]['phrase']='to sit on a box'
setk(c,'the young woman',3.0,x=0.26,y=0.37,w=0.44,h=0.37)
setk(c,'the young woman',3.5,x=0.34,y=0.39,w=0.3,h=0.33)
setk(c,'the fountain',3.0,x=0.78,y=0.15,w=0.22,h=0.33)
setk(c,'the fountain',5.0,x=0.1,y=0.15,w=0.88,h=0.3)
setk(c,'the fountain',7.0,x=0.15,y=0.2,w=0.7,h=0.25)
setk(c,'the fountain',7.5,x=0.15,y=0.2,w=0.7,h=0.25)
setk(c,'the fountain',9.0,x=0.15,y=0.21,w=0.7,h=0.24)
save(585,c)
# 588
c=load(588)
setk(c,'the woman in red boots',6.5,x=0,y=0,w=0.43,h=0.63)
setk(c,'the person in black boots',6.5,x=0.51,y=0,w=0.49,h=0.58)
setk(c,'the bird',6.5,x=0.43,y=0.23,w=0.08,h=0.15)
for n in c['nouns']:
    if n['word']=='red boots': n['x'],n['y']=0.10,0.38
    if n['word']=='a bird': n['x'],n['y']=0.51,0.33
save(588,c)
# overlap check
for i in (584,585,588,589):
    c=load(i); taps=c['taps']
    for a in range(3):
        for b in range(a+1,3):
            if taps[a]['target']==taps[b]['target']:
                assert taps[a]['keys']==taps[b]['keys']; continue
            for ka,kb in zip(taps[a]['keys'],taps[b]['keys']):
                if ka.get('off') or kb.get('off'): continue
                ox=min(ka['x']+ka['w'],kb['x']+kb['w'])-max(ka['x'],kb['x'])
                oy=min(ka['y']+ka['h'],kb['y']+kb['h'])-max(ka['y'],kb['y'])
                if ox>1e-9 and oy>1e-9: print(i,'OVERLAP',ka['t'],taps[a]['target'],taps[b]['target'],round(ox,3),round(oy,3))
            for k in taps[a]['keys']+taps[b]['keys']:
                if not k.get('off') and (k['x']+k['w']>1.0001 or k['y']+k['h']>1.0001): print(i,'OUT',k)
print('checked')
