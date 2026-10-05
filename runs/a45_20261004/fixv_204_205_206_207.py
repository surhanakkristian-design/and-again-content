import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,d): json.dump(d,open(f'content/{i}.json','w'),ensure_ascii=False,indent=1)
def setkey(tap,t,**kw):
    for k in tap['keys']:
        if k['t']==t:
            k.clear(); k['t']=t; k.update(kw); return
    raise SystemExit('no key')
# 204: nurse visible again at the left edge at 8.5
d=load(204)
setkey(d['taps'][1],8.5,x=0,y=0.28,w=0.10,h=0.37)
d['notes']+=" VERIFIER: nurse box added at 8.5 (strip with the clipboard at the left edge)."
save(204,d)
# 205: A-level wording
d=load(205)
d['taps'][0]['phrase']='to dry her eyes'
d['answer']=["She","is","crying","and","drying","her","eyes."]
d['notes']+=" VERIFIER: 'to wipe her tears' -> 'to dry her eyes' and the answer accordingly (wipe / tears are above A level)."
save(205,d)
# 206: woman / dog split at 7.0 and 8.0 so her face is whole
d=load(206)
setkey(d['taps'][1],7.0,x=0.31,y=0.12,w=0.69,h=0.88)
setkey(d['taps'][2],7.0,x=0.10,y=0.49,w=0.21,h=0.14)
setkey(d['taps'][1],8.0,x=0.31,y=0.08,w=0.69,h=0.92)
setkey(d['taps'][2],8.0,x=0.09,y=0.49,w=0.22,h=0.14)
d['notes']+=" VERIFIER: woman/dog split moved to 0.31 at 7.0 and 8.0."
save(206,d)
# 207: 'to lie on a wall' also fits the white cat (1.0-2.0 and 4.0) -> man state phrase
d=load(207)
d['taps'][2]={'phrase':'to wear a blue shirt','target':'the man','voice':'male','keys':json.loads(json.dumps(d['taps'][1]['keys']))}
d['notes']+=" VERIFIER: phrase 3 'to lie on a wall' (orange cat) replaced: a white cat lies on the same wall at 1.0-2.0 and 4.0, so the phrase did not fit only its target. Now 'to wear a blue shirt' -> the man (same keys as phrase 2). All three phrases are states: both people drink, no action fits only one."
save(207,d)
