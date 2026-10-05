import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,d): json.dump(d,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
# 4443
d=load(4443)
for t in d['taps']:
    for k in t['keys']:
        if k['t']==3.0: k.update(y=0.10,h=0.90)
        if k['t']==3.5: k.update(y=0.08,h=0.92)
        if k['t']==9.0: k.update(y=0.12,h=0.88)
for n in d['nouns']:
    if n['word']=='a suit': n.update(x=0.90,y=0.64)
save(4443,d)
# 4445
d=load(4445)
assert d['taps'][2]['phrase']=='to laugh at the camera'
d['taps'][2]['phrase']='to turn to the camera'
save(4445,d)
# 4447
d=load(4447)
new={'to drive on the wet road':'to drive in the rain','to smile at the old man':'to smile at the man','to put milk in his tea':'to put milk in tea'}
for t in d['taps']: t['phrase']=new[t['phrase']]
d['stillS']=5.5
pos={'a hat':(0.62,0.15),'milk':(0.24,0.66),'a cup':(0.54,0.79),'biscuits':(0.86,0.90)}
for n in d['nouns']: n['x'],n['y']=pos[n['word']]
save(4447,d)
# 4448
d=load(4448)
assert d['taps'][2]['phrase']=='to have a long blue handle'
d['taps'][2]['phrase']='to have a blue handle'
d['answer']=['She','is','holding','the','handle','of','the','broom.']
save(4448,d)
