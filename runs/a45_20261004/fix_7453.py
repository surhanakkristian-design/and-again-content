import json
def ld(i): return json.load(open(f'content/{i}.json'))
def sv(i,d): json.dump(d,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
d=ld(7453)
d['taps'][2]['phrase']='to burn beneath the wok'
for k in d['taps'][1]['keys']:
    if k['t']==0.7:
        k.clear(); k.update({"t":0.7,"x":0.64,"y":0.33,"w":0.24,"h":0.2})
sv(7453,d)
d=ld(7883)
for k in d['taps'][2]['keys']:
    if k['t']==0.2:
        k.update({"x":0.70,"y":0.26,"w":0.16,"h":0.44})
sv(7883,d)
d=ld(4364)
d['taps'][2]['phrase']='to glow with heat'
sv(4364,d)
