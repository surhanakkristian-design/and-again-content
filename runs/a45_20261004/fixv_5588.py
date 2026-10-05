import json
p='content/5588.json'; d=json.load(open(p))
t3=d['taps'][2]; assert t3['target']=='the dog'
t3['phrase']='to wake from a nap'
for k in t3['keys']:
    k['y']=round(k['y']-0.02,2); k['h']=round(min(k['h']+0.04,1-k['y']),2)
d['question']='Where is the dog lying?'
d['answer']=["It","is","lying","on","a","sun","lounger."]
d['notes']=d['notes']+" | Verifier: the dog dozes only at 0.2 s (head up, eyes open from 0.7 s), so phrase 3 -> 'to wake from a nap' and question -> where it lies; dog boxes made taller (min height)."
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
