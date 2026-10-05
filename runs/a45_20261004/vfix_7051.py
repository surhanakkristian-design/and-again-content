import json
p='content/7051.json'; d=json.load(open(p))
d['question']='What is the man in gloves doing?'
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
