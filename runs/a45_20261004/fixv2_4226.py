import json
d=json.load(open('content/4226.json'))
for k in d['taps'][2]['keys']:
    if k['t']==7.0: k['h']=0.30
d['notes']+=" Verifier: at 7.0 s split horizontally (dinosaur = head above, crocodile = whole body below)."
json.dump(d,open('content/4226.json','w'),ensure_ascii=False,indent=1)
