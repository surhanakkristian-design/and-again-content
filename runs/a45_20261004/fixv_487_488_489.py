import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,d): json.dump(d,open(f'content/{i}.json','w'),ensure_ascii=False,indent=1)
d=load(487)
for t in d['taps']:
    if t['target']=='the mouse':
        for k in t['keys']:
            if k['t']==9.5: k.update(x=0.05,y=0.36,w=0.75,h=0.32)
save(487,d)
d=load(488)
for t in d['taps']:
    for i,k in enumerate(t['keys']):
        if k['t']==2.5:
            if t['target']=='the woman': k.update(x=0.42,y=0.27,w=0.48,h=0.73)
            if t['target']=='the man in black': t['keys'][i]={'t':2.5,'x':0.90,'y':0.22,'w':0.10,'h':0.36}
save(488,d)
d=load(489)
for t in d['taps']:
    if t['phrase']=='to have white spots': t['phrase']='to be red and white'
save(489,d)
