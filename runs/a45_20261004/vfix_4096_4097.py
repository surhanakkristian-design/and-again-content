import json
p='content/4096.json'; c=json.load(open(p))
for t in c['taps']:
    for i,k in enumerate(t['keys']):
        if t['target']=='the turtle' and k['t']==2.5:
            t['keys'][i]={"t":2.5,"x":0,"y":0.29,"w":1.0,"h":0.45}
        if t['target']=='the man' and k['t']==13.0:
            t['keys'][i]={"t":13.0,"x":0,"y":0.18,"w":0.18,"h":0.14}
        if t['target']=='the man' and k['t']==14.5:
            t['keys'][i]={"t":14.5,"x":0,"y":0.03,"w":0.2,"h":0.24}
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
p='content/4097.json'; c=json.load(open(p))
for t in c['taps']:
    if t['phrase']=='to jump high into the air': t['phrase']='to jump into the air'
for n in c['nouns']:
    if n['word']=='a hill': n['x'],n['y']=0.78,0.43
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
