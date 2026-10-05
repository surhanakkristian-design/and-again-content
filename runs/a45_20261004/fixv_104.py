import json
p='content/104.json'; c=json.load(open(p))
new={7.0:dict(x=0.24,y=0.10,w=0.56,h=0.66),9.0:dict(x=0.16,y=0.21,w=0.73,h=0.77),9.5:dict(x=0.14,y=0.24,w=0.84,h=0.72)}
for tap in c['taps']:
    for k in tap['keys']:
        if k['t'] in new: k.update(new[k['t']])
for n in c['nouns']:
    if n['word']=='a mask': n['y']=0.27
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
p='content/110.json'; c=json.load(open(p))
for tap in c['taps']:
    if tap['target']=='the man': tap['phrase']="to touch the cat's back"
    for k in tap['keys']:
        if k['t']==5.0 and tap['target']=='the woman': k.update(x=0.2,w=0.48)
        if k['t']==5.0 and tap['target']=='the man': k.update(x=0.69,w=0.31)
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
