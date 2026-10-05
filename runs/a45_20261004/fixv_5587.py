import json
p='content/5587.json'; d=json.load(open(p))
for tp in d['taps']:
    for k in tp['keys']:
        if k['t']==2.2:
            if tp['target']=='the woman': k.clear(); k.update({"t":2.2,"x":0.06,"y":0.43,"w":0.22,"h":0.49})
            if tp['target']=='the dog': k.clear(); k.update({"t":2.2,"x":0.0,"y":0.66,"w":0.06,"h":0.19})
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
