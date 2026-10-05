import json
p='content/5277.json'; c=json.load(open(p))
for t in c['taps']:
    if t['phrase']=='to wear blue jeans': t['phrase']='to wear jeans'
    if t['phrase']=='to wear a grey dress': t['phrase']='to wear a dress'
json.dump(c,open(p,'w'),indent=2,ensure_ascii=False)
