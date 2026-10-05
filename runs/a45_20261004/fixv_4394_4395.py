import json
p='content/4394.json'; c=json.load(open(p))
new={1.0:(0.13,0.75),1.5:(0.13,0.74),3.0:(0.11,0.87),3.5:(0.39,0.61),4.0:(0.42,0.58),5.0:(0.41,0.59),5.5:(0.48,0.52)}
for t in c['taps']:
    if t['target']=='the woman in yellow':
        for k in t['keys']:
            if k['t'] in new: k['y'],k['h']=new[k['t']]
json.dump(c,open(p,'w'),ensure_ascii=False,indent=1)
p='content/4395.json'; c=json.load(open(p))
c['defaultVoice']='male'
for n in c['nouns']: n['voice']='male'
json.dump(c,open(p,'w'),ensure_ascii=False,indent=1)
