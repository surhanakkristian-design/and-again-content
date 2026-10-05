import json
def L(i): return json.load(open(f'content/{i}.json'))
def S(i,c): json.dump(c,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
c=L(5071); c['taps'][0]['phrase']='to grin at the camera'; S(5071,c)
c=L(5073)
for n in c['nouns']:
    if n['word']=='pills': n.update(word='a lid',x=0.66,y=0.91)
S(5073,c)
c=L(5074)
c['question']='What is the woman in orange carrying?'
for tap in c['taps']:
    for k in tap['keys']:
        if abs(k['t']-8.5)<0.01:
            if tap['target']=='the team': k.clear(); k.update(t=8.5,x=0.63,y=0.28,w=0.2,h=0.3)
            else: k['w']=0.61
S(5074,c)
c=L(5075)
c['taps'][2]['phrase']='to be full of ice cubes'
for n in c['nouns']:
    if n['word']=='an ice cream': n['y']=0.53
S(5075,c)
c=L(5075)
for n in c['nouns']:
    if n['word']=='sunglasses': n['x']=0.6
S(5075,c)
