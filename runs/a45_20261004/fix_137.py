import json
p='content/137.json'; d=json.load(open(p))
new={3.0:0.23,3.5:0.28,4.0:0.30,4.5:0.33}
for t in d['taps']:
    if t['target']=='the man':
        for k in t['keys']:
            if k['t'] in new: k['h']=new[k['t']]
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
