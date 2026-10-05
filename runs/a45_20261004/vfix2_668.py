import json
d=json.load(open('content/668.json'))
for k in d['taps'][1]['keys']:
    if k['t']==7.5:
        k.clear(); k.update({'t':7.5,'off':True})
d['notes']=d['notes'].replace('at 7.5-8.0 s','at 8.0 s (7.5 s stays off: only a sliver of his leg behind her)')
json.dump(d,open('content/668.json','w'),ensure_ascii=False,indent=1)
