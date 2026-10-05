import json
def ld(i): return json.load(open(f'content/{i}.json'))
def sv(i,d): json.dump(d,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
d=ld(4305)
for tp in d['taps']:
    if tp['target']=='the man':
        for k in tp['keys']:
            if k['t']==5.0: k.update(x=0.06,w=0.69)
sv(4305,d)
d=ld(4306)
for k in d['taps'][1]['keys']:
    if k['t']==1.5: k.update(x=0.65,y=0.42,w=0.18,h=0.2)
sv(4306,d)
d=ld(4309)
d['nouns'][0].update(x=0.66,y=0.13)
sv(4309,d)
