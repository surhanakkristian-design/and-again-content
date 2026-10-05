import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,c): json.dump(c,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
def setk(c,target,t,box):
    n=0
    for tap in c['taps']:
        if tap['target']==target:
            for j,k in enumerate(tap['keys']):
                if abs(k['t']-t)<0.01:
                    tap['keys'][j]={'t':k['t'],**({'off':True} if box is None else dict(zip('xywh',box)))}; n+=1
    assert n
# 669
c=load(669)
setk(c,'the woman',3.0,(0.53,0.22,0.47,0.78))
setk(c,'the woman',7.0,(0.2,0.25,0.54,0.75))
setk(c,'the man',7.0,(0.75,0.36,0.23,0.51))
setk(c,'the man',5.0,(0,0.46,1,0.54))
for tap in c['taps']:
    if tap['phrase']=='to press the buttons': tap['phrase']='to give her the bread'
save(669,c)
# 671
c=load(671)
setk(c,'the llama',7.0,(0.52,0.53,0.27,0.14)); setk(c,'the woman',7.0,(0.55,0.67,0.45,0.33))
setk(c,'the llama',7.5,(0.52,0.52,0.28,0.15)); setk(c,'the woman',7.5,(0.57,0.67,0.43,0.33))
save(671,c)
# 672
c=load(672)
setk(c,'the man',0.0,(0,0.24,0.26,0.52)); setk(c,'the woman',0.0,(0.26,0.24,0.39,0.7))
setk(c,'the man',0.5,(0,0.25,0.27,0.55)); setk(c,'the woman',0.5,(0.27,0.26,0.37,0.66))
setk(c,'the man',3.5,(0,0.5,0.13,0.2)); setk(c,'the woman',3.5,(0.13,0.17,0.73,0.83))
for t in (6.0,6.5,7.0,7.5): setk(c,'the bird',t,(0.46,0,0.24,0.14))
for n in c['nouns']:
    if n['word']=='a towel': n['x'],n['y']=0.72,0.6
save(672,c)
# 674
c=load(674)
setk(c,'the woman',6.5,(0.24,0.22,0.28,0.66)); setk(c,'the man',6.5,(0.52,0,0.48,1))
for tap in c['taps']:
    if tap['phrase']=='to bring a cup of tea': tap['phrase']='to bring her a cup'
    if tap['phrase']=='to grow in a pot': tap['phrase']='to grow by the window'
save(674,c)
