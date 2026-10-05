import json
p='content/4893.json'; c=json.load(open(p))
for t in c['taps'][:2]: t['target']='the woman in the car T-shirt'
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
