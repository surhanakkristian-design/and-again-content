import json
p='content/5024.json'; c=json.load(open(p))
assert c['taps'][1]['phrase']=='to put her hands together'
c['taps'][1]['phrase']='to press her hands together'
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
