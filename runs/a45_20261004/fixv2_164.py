import json
c=json.load(open('content/164.json'))
for tap in c['taps']:
    if tap['target']=='the open steamer':
        for k in tap['keys']:
            if abs(k['t']-3.5)<0.01: k['w']=0.24
json.dump(c, open('content/164.json','w'), ensure_ascii=False, indent=1)
