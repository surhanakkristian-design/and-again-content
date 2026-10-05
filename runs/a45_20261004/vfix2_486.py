import json
c=json.load(open('content/486.json')); p=c['taps'][0]
new={4.0:(0.25,0.28,0.55,0.72),4.5:(0.25,0.28,0.55,0.72),5.0:(0.25,0.32,0.55,0.68),5.5:(0.22,0.32,0.58,0.68),
     6.0:(0.25,0.35,0.55,0.65),6.5:(0.24,0.37,0.56,0.63),7.0:(0.24,0.40,0.56,0.60),7.5:(0.25,0.42,0.55,0.58)}
for n,k in enumerate(p['keys']):
    for t,(x,y,w,h) in new.items():
        if abs(k['t']-t)<0.01: p['keys'][n]={'t':k['t'],'x':x,'y':y,'w':w,'h':h}
c['notes']=c.get('notes','')+" VERIFIER: path box added 4.0-7.5 s (the worn trail between the stones under the walker plus the far zigzag); man box added 5.5/6.5/7.0 s (yellow sleeve at the left edge)."
json.dump(c,open('content/486.json','w'),ensure_ascii=False,indent=1)
