import json
def ld(i): return json.load(open(f'content/{i}.json'))
def sv(i,d): json.dump(d,open(f'content/{i}.json','w'),ensure_ascii=False,indent=1)
d=ld(282)
for n in d['nouns']:
    if n['word']=='a collar': n['x'],n['y']=0.62,0.70
    if n['word']=='a button': n['x'],n['y']=0.82,0.79
sv(282,d)
d=ld(284)
for t in d['taps']:
    for k in t['keys']:
        if k['t']==2.5:
            if t['target']=='the woman in purple': k.update(x=0,y=0,w=0.76,h=1)
            if t['target']=='the woman in grey':
                k.clear(); k.update(t=2.5,x=0.78,y=0.48,w=0.22,h=0.52)
sv(284,d)
d=ld(285)
for n in d['nouns']:
    if n['word']=='stairs': n['word']='steps'
d['question']='What is the family doing?'
d['answer']=['They','are','taking','a','family','photo.']
d['answerVoice']=d['defaultVoice']
sv(285,d)
