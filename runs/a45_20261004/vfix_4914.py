import json
p='content/4914.json'; c=json.load(open(p))
def setk(tap,t,box):
    for i,k in enumerate(tap['keys']):
        if abs(k['t']-t)<0.01: tap['keys'][i]=dict(t=t,**box)
setk(c['taps'][1],1.0,dict(x=0.82,y=0.41,w=0.18,h=0.34))
setk(c['taps'][1],1.5,dict(x=0.82,y=0.40,w=0.18,h=0.36))
setk(c['taps'][0],6.5,dict(x=0.36,y=0.40,w=0.64,h=0.44))
c['notes']+=' VERIFIER: runner box on at 1.0/1.5 (same teal top + bib, the runner approaching; otherwise a visible runner would be untappable). 6.5: the young man is visible mid-picture playing, box on; it also covers the duplicate guitarist at the right edge (generation artefact) so a tap on either counts.'
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
