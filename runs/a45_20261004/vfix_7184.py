import json
p='content/7184.json'; d=json.load(open(p))
for n in d['nouns']:
    if n['word']=='an ice cream': n['x'],n['y']=0.66,0.87
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
