import json
d=json.load(open('content/4499.json'))
for i in (0,1):
    for k in d['taps'][i]['keys']:
        if k['t']==7.5: k['w']=0.78
json.dump(d,open('content/4499.json','w'),indent=1,ensure_ascii=False)
