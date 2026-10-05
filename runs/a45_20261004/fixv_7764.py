import json
p='content/7764.json'; c=json.load(open(p))
c['taps'][0]['target']='the woman in front'
c['question']='What is the woman in front eating?'
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
