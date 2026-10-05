import json
p='content/869.json'; d=json.load(open(p))
assert d['taps'][1]['phrase']=='to lift a big ball'
d['taps'][1]['phrase']='to have a black beard'
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
