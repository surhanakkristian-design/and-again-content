import json
p='content/804.json'; d=json.load(open(p))
assert d['taps'][2]['phrase']=="to float in the sky"
d['taps'][2]['phrase']="to be outside the window"
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
