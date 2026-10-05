import json
p='content/5367.json'; c=json.load(open(p))
t=c['taps'][2]; assert t['target']=='the crowd'
t['phrase']='to applaud the competitors'
for k in t['keys']:
    if abs(k['t']-7.0)<0.01: k.update(x=0.0,y=0.19,w=1.0,h=0.10)
json.dump(c,open(p,'w'),indent=2,ensure_ascii=False)
p='content/5371.json'; c=json.load(open(p))
assert c['taps'][1]['phrase']=='to dance in a circle'
c['taps'][1]['phrase']='to dance hand in hand'
json.dump(c,open(p,'w'),indent=2,ensure_ascii=False)
