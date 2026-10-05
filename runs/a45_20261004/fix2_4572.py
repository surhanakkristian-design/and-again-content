import json
c=json.load(open('content/4572.json'))
new={5.5:(.28,.10,.37,.55),6.0:(.20,.08,.60,.54),6.5:(.20,.10,.46,.52)}
for t in c['taps']:
    for k in t['keys']:
        if k['t'] in new: k['x'],k['y'],k['w'],k['h']=new[k['t']]
json.dump(c,open('content/4572.json','w'),indent=1,ensure_ascii=False)
