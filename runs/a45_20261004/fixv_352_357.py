import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,d): json.dump(d,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
d=load(352)
d['taps'][1]['phrase']='to hold up one finger'
d['question']='What is on the grill?'
d['answer']=['Cheese','and','vegetables','are','on','the','grill.']
d['notes']+=' VERIFIER: woman phrase changed (the man in the apron also holds the plate at 8.5-9.0); question changed (cheese ends on a plate).'
save(352,d)
d=load(357)
for k in d['taps'][1]['keys']:
    if k['t']==1.0: k['h']=0.52
    if k['t']==1.5: k['h']=0.52
    if k['t']==2.0: k['h']=0.49
d['taps'][2]['phrase']='to lie by the flowers'
d['nouns'][0]['x']=0.58
d['question']='Who is holding the hairbrush?'
d['answer']=['The','woman','with','long','hair','is','holding','the','hairbrush.']
d['notes']+=' VERIFIER: cat lies (not sits); red-haired box shortened at 1.0-2.0 so the brush hand is not inside it; curtain pill moved onto the curtain; question names its subject.'
save(357,d)
