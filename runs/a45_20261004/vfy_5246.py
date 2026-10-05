import json
p='content/5246.json'; c=json.load(open(p))
for tap in c['taps'][:2]:
    for k in tap['keys']:
        if abs(k['t']-4.0)<.01: k['h']=0.93
c['taps'][2]['phrase']='to grin at the camera'
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
