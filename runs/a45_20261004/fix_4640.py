import json
p='content/4640.json'; d=json.load(open(p))
man=d['taps'][0]['keys']
def setk(t,**kw):
    for k in man:
        if abs(k['t']-t)<1e-6: k.clear(); k.update(dict(t=t,**kw))
setk(4.5,x=0,y=0,w=0.86,h=0.62)
setk(6.0,x=0,y=0.08,w=0.56,h=0.8)
setk(7.0,x=0,y=0.55,w=0.95,h=0.45)
d['taps'][1]['keys']=json.loads(json.dumps(man))
d['taps'][2]={"phrase":"to slide the drawer shut","target":"the man","voice":"male","keys":json.loads(json.dumps(man))}
d['notes']+=" VERIFIER: 'to spin the laundry' replaced (no frame shows the drum turning; the 8.0-9.5 s shots show the door opened/closed and still laundry) by 'to slide the drawer shut' (6.0-6.5 s); all three phrases now on the man; boxes widened at 4.5, 6.0, 7.0 s."
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
