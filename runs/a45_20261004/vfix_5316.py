import json
p='content/5316.json'; d=json.load(open(p))
for t in d['taps']:
    for k in t['keys']:
        if k['t']==8.5: k['x'],k['w']=0.14,0.86
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
