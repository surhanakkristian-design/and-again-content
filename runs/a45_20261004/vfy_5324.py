import json
p='content/5324.json'; c=json.load(open(p))
for tap in c['taps']:
    for k in tap['keys']:
        if k['t']<1.01: k['w']=0.54
        if abs(k['t']-1.5)<.01: k['w']=0.86
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
