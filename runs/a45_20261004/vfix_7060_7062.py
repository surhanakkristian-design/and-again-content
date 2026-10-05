import json
p='content/7060.json'; d=json.load(open(p))
adj={'the young man':(0.32,0.56),'the red-haired woman':(0.33,0.44),'the mover':(0.31,0.56)}
for t in d['taps']:
    y,h=adj[t['target']]
    for k in t['keys']:
        if not k.get('off'): k['y']=y; k['h']=h
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
p='content/7062.json'; d=json.load(open(p))
d['taps'][2]['phrase']='to stand on a red stool'
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
