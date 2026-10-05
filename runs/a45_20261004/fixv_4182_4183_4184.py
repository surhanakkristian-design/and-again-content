import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,d): json.dump(d,open(f'content/{i}.json','w'),ensure_ascii=False,indent=1)
d=load(4182)
for k in d['taps'][1]['keys']:
    if k['t']==9.5: k['h']=0.29
save(4182,d)
d=load(4183)
assert d['taps'][1]['phrase']=='to hold red balloons'
d['taps'][1]['phrase']='to open his arms wide'
save(4183,d)
d=load(4184)
assert d['taps'][2]['phrase']=='to throw the ball away'
d['taps'][2]['phrase']='to throw the ball'
save(4184,d)
