import json
p='content/4707.json'; c=json.load(open(p))
for t in c['taps']:
    if t['phrase']=='to wait in a line': t['phrase']='to wait in line'
json.dump(c,open(p,'w'),indent=2,ensure_ascii=False)
