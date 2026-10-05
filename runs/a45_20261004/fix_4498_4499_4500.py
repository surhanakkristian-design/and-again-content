import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,d): json.dump(d,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
def setkey(tap,t,**kw):
    for k in tap['keys']:
        if k['t']==t:
            k.clear(); k['t']=t; k.update(kw); return
    raise SystemExit('no key')
d=load(4498)
setkey(d['taps'][0],10.0,x=0.18,y=0.2,w=0.69,h=0.72)
setkey(d['taps'][2],10.0,x=0.88,y=0.33,w=0.12,h=0.62)
setkey(d['taps'][1],4.0,x=0,y=0.05,w=0.13,h=0.6)
setkey(d['taps'][1],4.5,x=0,y=0.05,w=0.13,h=0.6)
save(4498,d)
d=load(4499)
for i in (0,1): setkey(d['taps'][i],7.5,x=0.03,y=0.43,w=0.87,h=0.57)
setkey(d['taps'][2],5.0,x=0,y=0.3,w=1,h=0.34)
save(4499,d)
d=load(4500)
d['taps'][1]['target']='the goalkeeper'
d['question']='What is the woman in jeans doing?'
d['answer']=['She','is','catching','a','small','ball.']
d['answerVoice']='female'
save(4500,d)
