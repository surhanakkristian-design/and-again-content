import json
p='content/4021.json'; c=json.load(open(p))
for t in c['taps']:
    for i,k in enumerate(t['keys']):
        if t['target']=='the spoon' and k['t'] in (3.5,4.0): t['keys'][i]={'t':k['t'],'off':True}
        if t['target']=='the fork' and k['t']==6.0: k['w']=0.56
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
p='content/4023.json'; c=json.load(open(p))
for t in c['taps']:
    if t['phrase']=='to carry two men': t['phrase']='to carry the men'
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
