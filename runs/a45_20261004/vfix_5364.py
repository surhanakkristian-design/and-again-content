import json
p='content/5364.json'; c=json.load(open(p))
for t in c['taps']:
    if t['phrase']=='to hurry up from behind': t['phrase']='to rush up from behind'
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
