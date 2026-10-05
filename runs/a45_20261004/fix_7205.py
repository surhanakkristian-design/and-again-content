import json
p='content/7203.json'; d=json.load(open(p))
d['answer']=["It","is","standing","on","a","block","of","lava."]
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
p='content/7205.json'; d=json.load(open(p))
w=d['taps'][0]['keys']
for k in w:
    if k['t']==2.7: k.update(x=0.23,y=0.19,w=0.73,h=0.78)
    if k['t']==3.2: k.update(x=0.22,y=0.15,w=0.78,h=0.85)
d['taps'][1]['phrase']='to look sadly at the bird'
d['taps'][2]={'phrase':'to get up from the sand','target':'the woman','voice':'female','keys':json.loads(json.dumps(w))}
d['taps'][1]['keys']=json.loads(json.dumps(w))
for n in d['nouns']:
    if n['word']=='a bird': n['x']=0.53; n['y']=0.62
d['notes']+=" VERIFIER: 'to carry a black box' dropped (a second worker carries a crate at 3.2 s, and the left-edge figure at 0.2-1.7 s is unclear); 'kneel' replaced (above A level); woman used for all three phrases, her box widened at 2.7/3.2 s; bird pill moved onto the bird's body."
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
