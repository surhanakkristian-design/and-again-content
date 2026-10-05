import json
p='content/5589.json'; d=json.load(open(p))
t2=d['taps'][1]; assert t2['target']=='the man'
t2['phrase']='to walk with a wheelbarrow'
for k in t2['keys']:
    if k['t']==3.7: k.clear(); k.update({"t":3.7,"x":0.88,"y":0.32,"w":0.12,"h":0.26})
d['notes']=d['notes']+" | Verifier: 'push' changed to 'walk with' (he trails the wheelbarrow behind him at 0.2 s, direction unclear later); man's box added at 3.7 s (head and torso at the right edge)."
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
