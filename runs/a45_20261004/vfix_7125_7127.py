import json
p='content/7125.json'; d=json.load(open(p))
d['question']="What is the young woman doing?"
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
p='content/7127.json'; d=json.load(open(p))
for tp in d['taps']:
    for k in tp['keys']:
        if k['t']==2.2:
            if tp['target']=='the woman in the boat':
                k.update(x=0.61,y=0.52,w=0.37,h=0.32)
            elif tp['target']=='the dog':
                k.update(x=0.39,y=0.63,w=0.21,h=0.19)
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
