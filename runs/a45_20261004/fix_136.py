import json
f='content/136.json'; c=json.load(open(f))
new={('the cat',7.5):(.40,.42,.22,.14),('the cat',8.0):(.40,.42,.23,.14),
     ('the woman',7.5):(0,.14,.40,.62),('the woman',8.0):(0,.15,.40,.60),
     ('the candle',7.5):(.47,.56,.18,.38)}
for t in c['taps']:
    for k in t['keys']:
        v=new.get((t['target'],k['t']))
        if v:
            k.pop('off',None); k.update(dict(zip('xywh',v)))
for n in c['nouns']:
    if n['word']=='a cat': n['x']=0.62
json.dump(c,open(f,'w'),indent=1,ensure_ascii=False)
