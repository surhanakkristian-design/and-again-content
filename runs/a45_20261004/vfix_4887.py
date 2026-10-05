import json
p='content/4887.json'; c=json.load(open(p))
assert c['taps'][1]['phrase']=="to grin at the camera"
c['taps'][1]['phrase']="to wear sturdy hiking boots"
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
