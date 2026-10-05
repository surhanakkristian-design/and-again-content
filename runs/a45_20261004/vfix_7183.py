import json
p='content/7183.json'; d=json.load(open(p))
for n in d['nouns']:
    if n['word']=='an umbrella': n['x'],n['y']=0.50,0.37
    if n['word']=='a shop window': n['x'],n['y']=0.88,0.24
d['question']='What is the woman in yellow doing?'
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
