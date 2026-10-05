import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,d,raw):
    ind = 2 if raw.startswith('{\n  "') else (1 if raw.startswith('{\n "') else None)
    json.dump(d, open(f'content/{i}.json','w'), ensure_ascii=False, indent=ind)
def setk(tap,t,v):
    for n,k in enumerate(tap['keys']):
        if abs(k['t']-t)<1e-6:
            tap['keys'][n] = {'t':k['t'], **v} if v else {'t':k['t'],'off':True}
            return
    raise SystemExit('no key %s'%t)
# 4321
raw=open('content/4321.json').read(); d=json.loads(raw)
d['answer']=["She","is","adjusting","a","model","tower."]
d['notes']+=" | verifier: answer changed from 'a tower on the model' (a/the could swap) to one chip order."
save(4321,d,raw)
# 4324
raw=open('content/4324.json').read(); d=json.loads(raw)
assert d['taps'][1]['phrase']=='to dance in the street'
d['taps'][1]['phrase']='to dance on the cobblestones'
d['notes']+=" | verifier: phrase 2 had no B-level word ('to dance in the street')."
save(4324,d,raw)
# 4327
raw=open('content/4327.json').read(); d=json.loads(raw)
cook,guests=d['taps'][0],d['taps'][1]
B=lambda x,y,w,h:{'x':x,'y':y,'w':w,'h':h}
setk(cook,4.5,B(0.70,0.0,0.30,0.20)); setk(guests,4.5,B(0.10,0.02,0.59,0.26))
setk(cook,5.0,B(0.68,0.0,0.32,0.33)); setk(guests,5.0,B(0.10,0.02,0.57,0.26))
setk(cook,5.5,B(0.75,0.0,0.25,0.33)); setk(guests,5.5,B(0.10,0.0,0.64,0.27))
setk(cook,6.0,B(0.50,0.0,0.32,0.14)); setk(guests,6.0,B(0.10,0.0,0.39,0.22))
setk(cook,6.5,B(0.74,0.0,0.26,0.16)); setk(guests,6.5,B(0.08,0.0,0.65,0.22))
setk(guests,7.0,B(0.08,0.0,0.50,0.26)); setk(guests,7.5,B(0.08,0.0,0.50,0.27))
d['notes']+=" | verifier: cook box added at 4.5-6.5 s where his hand and arm are clearly in the picture (guests box trimmed there); guests on at 7.0-7.5 s (the man in white is visible beside the flames)."
save(4327,d,raw)
# 4329
raw=open('content/4329.json').read(); d=json.loads(raw)
assert d['taps'][2]['phrase']=='to stretch out his legs'
d['taps'][2]['phrase']='to put his feet up'
d['notes']+=" | verifier: 'stretch' is not A-level; phrase 3 now 'to put his feet up'."
save(4329,d,raw)
