import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,c): json.dump(c,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
c=load(543)
for t in c['taps']:
    if t['phrase']=='to show a bowl of pasta': t['phrase']='to show his pasta'
save(543,c)
c=load(545)
for t in c['taps']:
    if t['target']=='the woman in the jacket':
        for k in t['keys']:
            if k['t']==1.0: k.update(x=0,y=0.38,w=0.23,h=0.60)
save(545,c)
c=load(546)
for t in c['taps']:
    if t['phrase']=='to smell her wrist': t['phrase']='to smell the perfume'
    if t['target']=='the woman in blue':
        for k in t['keys']:
            if k['t']==4.5: k.update(x=0.44,y=0.26,w=0.56,h=0.74)
c['answer']=['She','is','putting','perfume','on','her','arm.']
save(546,c)
