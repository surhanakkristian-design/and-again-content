import json
p='content/7177.json'; d=json.load(open(p))
d['taps'][2]['phrase']='to lean back in her harness'
d['notes']+=' | Verifier: phrase 3 "push against the rock" had no B1/B2 word -> "lean back in her harness".'
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
