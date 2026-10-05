import json
p='content/825.json';d=json.load(open(p))
for t in d['taps']:
    if t['target']=='the clouds': t['phrase']='to hang over the mountains'
d['notes']+=" Verifier: 'to float in the sky' -> 'to hang over the mountains' ('float' is B2, not level A)."
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
p='content/826.json';d=json.load(open(p))
nx={2.5:0.46,3.5:0.48,4.5:0.48}
for t in d['taps']:
    if t['target']=='the cameraman':
        for k in t['keys']:
            if k['t'] in nx and not k.get('off'): k['x']=nx[k['t']]
d['notes']+=" Verifier: cameraman box at 2.5/3.5/4.5 s moved left onto camera + his head, off the standing man's back."
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
