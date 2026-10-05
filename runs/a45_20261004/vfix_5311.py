import json
p='content/5311.json'; d=json.load(open(p))
t=d['taps']
for k in t[0]['keys']:
    if k['t'] in (0.0,0.5): k.clear(); k.update({'t':0.0 if not k else 0.0})
t[0]['keys'][0]={'t':0.0,'x':0,'y':0,'w':0.95,'h':1.0}
t[0]['keys'][1]={'t':0.5,'x':0,'y':0,'w':0.95,'h':1.0}
t[1]['phrase']='to doze under a chunky blanket'
for k in t[2]['keys']:
    if k['t']==7.0: k['h']=0.15
    if k['t'] in (8.0,8.5): k['h']=0.15
d['answer']=['They','are','snuggling','under','cosy','blankets.']
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
