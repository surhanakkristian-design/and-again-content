import json
p='content/5317.json'; d=json.load(open(p))
assert d['taps'][1]['phrase']=='to stamp her heels'
d['taps'][1]['phrase']='to stamp her feet'
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
