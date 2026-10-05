import json
p='content/215.json';d=json.load(open(p))
def setk(ti,t,**kw):
    for k in d['taps'][ti]['keys']:
        if k['t']==t:
            b=k['y']+k['h'] if 'y' in kw and 'h' not in kw else None
            k.update(kw)
            if b is not None: k['h']=round(b-k['y'],2)
for t,y in [(3.0,0.42),(3.5,0.42),(5.0,0.40),(5.5,0.41)]: setk(0,t,y=y)
for t,y in [(3.0,0.33),(3.5,0.34),(5.0,0.33),(5.5,0.34),(6.0,0.36)]: setk(1,t,y=y)
setk(1,8.5,x=0.62,y=0.20,w=0.38,h=0.70)
setk(1,9.0,x=0.62,y=0.20,w=0.38,h=0.75)
d['stillS']=9.0
pos={'a lantern':(0.52,0.77),'a match':(0.24,0.66),'a window':(0.47,0.25),'a copper pan':(0.15,0.15)}
for n in d['nouns']: n['x'],n['y']=pos[n['word']]
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
