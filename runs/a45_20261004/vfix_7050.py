import json
p='content/7050.json'; d=json.load(open(p))
t=d['taps'][2]
t['phrase']='to jog along the water'; t['target']='the jogger'; t['voice']='female'
for k in t['keys']:
    if k['t']==1.7:
        k.clear(); k.update({'t':1.7,'x':0.0,'y':0.53,'w':0.12,'h':0.14})
for n in d['nouns']:
    if n['word']=='a woman':
        n.update({'word':'people','x':0.8,'y':0.56,'voice':'female'})
d['question']='What is the woman in front doing?'
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
