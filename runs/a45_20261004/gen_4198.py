import json
p='content/4198.json';c=json.load(open(p))
for k in c['taps'][2]['keys']:
    if k['t']==1.5: k.update(x=0,y=0.08,w=0.21,h=0.62)
c['notes']=c.get('notes','')+' VERIFIER: sea box at 1.5 s moved from the top band to the glittering water on the left.'
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
