import json
p='content/6973.json'; d=json.load(open(p))
assert d['taps'][2]['phrase']=='to topple over backwards'
d['taps'][2]['phrase']='to topple onto the floor'
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
