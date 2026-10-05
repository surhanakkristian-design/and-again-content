import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,c): json.dump(c,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
# 4140
c=load(4140)
for n in c['nouns']:
    if n['word']=='friends': n['word']='people'
c['question']='Where are the three people sitting?'
save(4140,c)
# 4141
c=load(4141)
t=c['taps'][1]; t['phrase']='to lead down a cliff'
for k in t['keys']:
    if not k.get('off'):
        k['y']=round(k['y']-0.06,2); k['h']=round(1.0-k['y'],2)
for k in c['taps'][0]['keys']:
    if k['t']==1.0: k['y']=0.62; k['h']=0.38
for n in c['nouns']:
    if n['word']=='a hillside': n['word']='a cliff'
c['question']='What are the six men doing?'
c['answer']=['They','are','lying','flat','on','their','backs.']
save(4141,c)
# 4144
c=load(4144)
for k in c['taps'][0]['keys']:
    if k['t']==2.0: k.update(x=0.0,y=0.15,w=1.0,h=0.31)
new={5.0:(0.33,0.67),5.5:(0.35,0.65),9.0:(0.32,0.68)}
for ti in (1,2):
    for k in c['taps'][ti]['keys']:
        if k['t'] in new: k['x'],k['w']=new[k['t']]
save(4144,c)
