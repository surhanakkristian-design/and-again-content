import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,d): json.dump(d,open(f'content/{i}.json','w'),ensure_ascii=False,indent=1)
def setk(d,targets,t,**kw):
    n=0
    for tap in d['taps']:
        if tap['target'] in targets:
            for i,k in enumerate(tap['keys']):
                if abs(k['t']-t)<1e-6:
                    if 'off' in k: tap['keys'][i]={'t':k['t'],**kw}
                    else: k.update(kw)
            n+=1
    assert n
# 760
d=load(760)
setk(d,['the bottle'],1.0,y=0.60,h=0.22)
setk(d,['the bottle'],3.0,x=0.88,y=0.53,w=0.12,h=0.21)
setk(d,['the bottle'],3.5,x=0.88,y=0.54,w=0.12,h=0.21)
setk(d,['the bottle'],5.0,y=0.54,h=0.26)
for n in d['nouns']:
    if n['word']=='an ice pack': n['x'],n['y']=0.86,0.72
save(760,d)
# 761
d=load(761)
for t,b in [(1.0,.74),(1.5,.76),(3.0,.80),(3.5,.81),(5.0,.81),(7.0,.74),(7.5,.74),(9.0,.77),(9.5,.77)]:
    for tap in d['taps']:
        if tap['target']=='the woman':
            for k in tap['keys']:
                if k['t']==t: k['h']=round(b-k['y'],2)
        if tap['target']=='the cushion':
            for k in tap['keys']:
                if k['t']==t: k['y']=round(b+0.01,2); k['h']=round(0.98-k['y'],2)
for n in d['nouns']:
    if n['word']=='a cushion': n['y']=0.75
save(761,d)
# 762
d=load(762)
setk(d,['the woman'],7.0,x=0,y=0.44,w=0.20,h=0.56)
setk(d,['the woman'],7.5,x=0,y=0.43,w=0.20,h=0.57)
for n in d['nouns']:
    if n['word']=='a drawer': n['word'],n['x'],n['y']='a bed',0.44,0.72
save(762,d)
# 763
d=load(763)
setk(d,['the tablecloth'],8.0,w=0.87)
setk(d,['the tablecloth'],8.5,w=0.85)
setk(d,['the tablecloth'],9.0,y=0.50,h=0.48)
setk(d,['the cat'],8.0,x=0.88,y=0.62,w=0.12,h=0.18)
setk(d,['the cat'],8.5,x=0.86,y=0.62,w=0.14,h=0.22)
d['answer']=["They","are","spreading","the","tablecloth","over","the","table."]
save(763,d)
