import json
c = json.load(open('content/407.json'))
for i,(kw) in ((0, dict(x=0.28, y=0.32, w=0.28, h=0.11)), (1, dict(x=0.26, y=0.43, w=0.52, h=0.40))):
    ks = c['taps'][i]['keys']
    for n,k in enumerate(ks):
        if abs(k['t']-4.5)<0.01: ks[n] = {'t': 4.5, **kw}
json.dump(c, open('content/407.json','w'), indent=1, ensure_ascii=False)
