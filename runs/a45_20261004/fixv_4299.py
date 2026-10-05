import json
p='content/4299.json'; d=json.load(open(p))
man={4.5:0.11,5.0:0.12,5.5:0.11,6.0:0.13,6.5:0.11,7.0:0.09,7.5:0.07}
wom={2.0:dict(x=0.87,y=0.22,w=0.13,h=0.43),2.5:dict(x=0.85,y=0.15,w=0.15,h=0.52)}
womy={5.0:0.15,7.0:0.17,7.5:0.15}
n=0
for t in d['taps']:
    for k in t['keys']:
        if t['target']=='the man' and k['t'] in man:
            k['y']=man[k['t']]; k['h']=round(1-k['y'],2); n+=1
        if t['target']=='the woman':
            if k['t'] in wom:
                k.pop('off',None); k.update(wom[k['t']]); n+=1
            if k['t'] in womy:
                k['y']=womy[k['t']]; k['h']=round(1-k['y'],2); n+=1
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print(n)
