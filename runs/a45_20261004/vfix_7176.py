import json
p='content/7176.json'; d=json.load(open(p))
g=d['taps'][1]; g['phrase']='to sit next to the woman'
for k in g['keys']:
    if k['t']<=2.21: k['w']=round(max(k['w'],0.82-k['x'] if k['t'] in (1.7,1.2) else 0.81-k['x']),2)
d['question']='What is the goat doing?'
d['answer']=['It','is','sitting','next','to','the','woman.']
d['notes']+=' | Verifier: goat is inside the bus on the seat, so "look into the bus" was wrong; goat box widened to >=0.17.'
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
print([ (k['t'],k['x'],k['w']) for k in g['keys']])
