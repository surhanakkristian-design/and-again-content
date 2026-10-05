import json
p='content/562.json'; d=json.load(open(p))
def setk(tap,t,**kw):
    for k in tap['keys']:
        if k['t']==t:
            k.clear(); k['t']=t; k.update(kw)
setk(d['taps'][2],1.0,x=0.22,y=0.02,w=0.78,h=0.98)
setk(d['taps'][2],9.0,x=0.18,y=0.12,w=0.30,h=0.13)
setk(d['taps'][0],9.0,x=0,y=0.26,w=0.56,h=0.71)
d['question']="What is the woman holding?"
d['answer']=["She","is","holding","a","white","plug."]
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
p='content/564.json'; d=json.load(open(p))
for n in d['nouns']:
    if n['word']=='a leotard': n.update(word='a fist',x=0.72,y=0.13)
    if n['word']=='the ceiling': n.update(x=0.25,y=0.05)
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
