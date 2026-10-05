import json
p='content/4181.json'; c=json.load(open(p))
assert c['taps'][1]['phrase']=="to reach for the cake"
c['taps'][1]['phrase']="to smile at the camera"
c['answer']=["She","is","riding","a","red","scooter."]
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
