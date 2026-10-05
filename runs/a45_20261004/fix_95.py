import json
p='content/95.json'; d=json.load(open(p))
assert d['taps'][0]['phrase']=='to apply blush with a brush'
d['taps'][0]['phrase']='to apply blush'
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
