import json
p='content/4642.json'; d=json.load(open(p))
for t in d['taps']:
    if t['target']=='the boy': t['target']='the young man'
d['question']='What is the young man digging?'
d['notes']+=" VERIFIER: target 'the boy' renamed 'the young man' (an adult, early 20s, not a child); question changed to match."
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
