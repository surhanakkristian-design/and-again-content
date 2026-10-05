import json
p='content/4193.json'; d=json.load(open(p))
for tp in d['taps']:
    for i,k in enumerate(tp['keys']):
        if k['t']==0.5:
            if tp['target']=='the car': tp['keys'][i]={"t":0.5,"x":0.06,"y":0.52,"w":0.32,"h":0.12}
            else: tp['keys'][i]={"t":0.5,"x":0.38,"y":0.44,"w":0.62,"h":0.26}
d['question']="What is the car doing?"
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
p='content/4194.json'; d=json.load(open(p))
for n in d['nouns']:
    if n['word']=='a car': n['y']=0.52
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
