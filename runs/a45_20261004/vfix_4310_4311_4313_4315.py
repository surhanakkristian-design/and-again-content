import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,c): json.dump(c,open(f'content/{i}.json','w'),ensure_ascii=False,indent=1)
def setk(tap,t,**kw):
    for n,k in enumerate(tap['keys']):
        if k['t']==t:
            tap['keys'][n]={'t':t,**kw}; return
    raise SystemExit('no key')
# 4310
c=load(4310)
flag=c['taps'][1]; fans=c['taps'][2]
setk(flag,5.0,x=0.64,y=0.09,w=0.26,h=0.22); setk(fans,5.0,x=0.0,y=0.32,w=1.0,h=0.48)
setk(flag,5.5,x=0.68,y=0.15,w=0.26,h=0.23); setk(fans,5.5,x=0.0,y=0.39,w=1.0,h=0.49)
c['question']='Why is the footballer covering her face?'
save(4310,c)
# 4311
c=load(4311)
c['taps'][0]['phrase']='to have curly brown hair'
c['taps'][1]['phrase']='to carry a brown paper bag'
setk(c['taps'][0],4.0,x=0.62,y=0.42,w=0.38,h=0.58)
save(4311,c)
# 4313
c=load(4313)
y=c['taps'][2]
setk(y,8.0,x=0.0,y=0.40,w=0.20,h=0.24)
setk(y,8.5,x=0.0,y=0.30,w=0.17,h=0.34)
setk(y,9.0,x=0.0,y=0.36,w=0.19,h=0.46)
save(4313,c)
# 4315
c=load(4315)
for n in c['nouns']:
    if n['word']=='a coat': n.update(word='a wall',x=0.70,y=0.22)
save(4315,c)
