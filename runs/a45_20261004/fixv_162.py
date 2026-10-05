import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,c): json.dump(c, open(f'content/{i}.json','w'), ensure_ascii=False, indent=1)
def setk(c, targets, t, **kw):
    n=0
    for tap in c['taps']:
        if tap['target'] in targets:
            for k in tap['keys']:
                if abs(k['t']-t)<0.01: k.update(kw); n+=1
    assert n, (targets,t)
# 162
c=load(162)
setk(c,['the dog'],9.0,y=0.57,h=0.43); setk(c,['the dog'],9.5,y=0.56,h=0.44)
for n in c['nouns']:
    if n['word']=='chocolate': n['x'],n['y']=0.56,0.58
save(162,c)
# 164
c=load(164)
setk(c,['the man'],2.0,w=0.86)
setk(c,['the man'],3.5,h=0.25); setk(c,['the open steamer'],3.5,y=0.82,h=0.18)
setk(c,['the man'],5.0,h=0.23); setk(c,['the open steamer'],5.0,y=0.80,h=0.20)
save(164,c)
# 165
c=load(165)
for tap in c['taps']:
    if tap['phrase']=='to hold the popcorn': tap['phrase']='to hold the popcorn box'
for t in (3.0,3.5): setk(c,['the girl'],t,y=0.54,h=0.44)
setk(c,['the girl'],5.0,y=0.16,h=0.84); setk(c,['the girl'],5.5,y=0.14,h=0.86)
save(165,c)
# 167
c=load(167)
W=['the woman in the headscarf']
setk(c,W,1.5,x=0.35,w=0.65,h=0.86)
setk(c,W,3.5,h=0.58); setk(c,['the rubbish bag'],3.5,y=0.68,h=0.32)
setk(c,W,5.0,h=0.46); setk(c,['the rubbish bag'],5.0,y=0.71,h=0.29)
setk(c,W,5.5,h=0.46); setk(c,['the rubbish bag'],5.5,y=0.70,h=0.30)
for n in c['nouns']:
    if n['word']=='a headscarf': n['y']=0.40
save(167,c)
