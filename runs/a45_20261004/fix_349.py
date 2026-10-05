import json
p='content/349.json'; d=json.load(open(p))
gf=d['taps'][0]['keys']; boy=d['taps'][1]['keys']
def setk(keys,t,**kw):
    for k in keys:
        if k['t']==t: k.update(kw); return
    raise SystemExit('no key')
setk(gf,1.0,y=0.06,h=0.33)
setk(boy,1.0,y=0.39,h=0.61)
setk(gf,4.5,h=0.78)
setk(gf,5.0,h=0.82)
setk(gf,5.5,h=0.86)
setk(gf,6.0,h=0.90)
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
p='content/350.json'; d=json.load(open(p))
d['nouns']=[n for n in d['nouns'] if n['word']!='glasses']
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
