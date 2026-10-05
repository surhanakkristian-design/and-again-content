import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,d): json.dump(d,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
d=load(4136)
for tp in d['taps'][:2]:
    for k in tp['keys']:
        if k['t']==5.0: k.update(y=0.23,h=0.69)
        if k['t']==5.5: k.update(y=0.22,h=0.76)
for n in d['nouns']:
    if n['word']=='trousers': n.update(x=0.28,y=0.67)
save(4136,d)
d=load(4138)
for tp in d['taps']:
    for k in tp['keys']:
        if 5.0<=k['t']<=8.0:
            if tp['target']=='the man': k.update(x=0.46,w=0.54)
            else: k.update(w=0.46)
save(4138,d)
d=load(4139)
d['taps'][0]['phrase']='to hike up a path'
save(4139,d)
