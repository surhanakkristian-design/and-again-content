import json
p='content/5145.json'; c=json.load(open(p))
for tap in c['taps'][:2]:
    for k in tap['keys']:
        if abs(k['t']-9.0)<0.01: k.update(y=0.19,h=0.66)
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
