import json
p='content/571.json'; d=json.load(open(p))
for t in d['taps']:
    if t['phrase']=='to raise one finger': t['phrase']='to raise her finger'
    if t['phrase']=='to stand over the fire': t['phrase']='to stand on the fire'
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
p='content/121.json'; d=json.load(open(p))
for t in d['taps']:
    if t['target']=='the man':
        for k in t['keys']:
            if k['t']==3.5: k['w']=0.92
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
