import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,c): json.dump(c, open(f'content/{i}.json','w'), indent=1, ensure_ascii=False)
def setk(c, ti, t, **kw):
    for k in c['taps'][ti]['keys']:
        if abs(k['t']-t)<0.01:
            k.update(kw); return
    raise SystemExit('no key')
c = load(477)
setk(c,2,0.5,x=0.34,w=0.66)
setk(c,2,1.0,x=0.39,w=0.61)
setk(c,1,7.0,y=0.17,h=0.28)
setk(c,2,7.0,y=0.46,h=0.32)
setk(c,2,7.5,h=0.27)
c['answer'] = ["He","is","taking","the","plate","out","of","the","microwave."]
save(477,c)
c = load(479)
setk(c,0,8.5,x=0,y=0.22,w=0.14,h=0.78)
setk(c,1,8.5,x=0.15,y=0.54,w=0.85,h=0.27)
for n in c['nouns']:
    if n['word']=='a thought bubble': n['x'],n['y']=0.47,0.25
save(479,c)
