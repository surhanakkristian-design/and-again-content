import json
p='content/7054.json'; d=json.load(open(p))
for k in d['taps'][1]['keys']:
    if k['t']==0.2: k.update({'x':0.08,'y':0.36,'w':0.17,'h':0.15})
nn=[]
for n in d['nouns']:
    if n['word']=='a beach umbrella': continue
    if n['word']=='an iron': n.update({'x':0.48,'y':0.56})
    nn.append(n)
nn.insert(2,{'word':'an ironing board','x':0.15,'y':0.645,'voice':'male'})
d['nouns']=nn
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
