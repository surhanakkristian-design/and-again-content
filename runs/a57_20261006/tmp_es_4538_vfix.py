import json
p='content/es/4538.json'; d=json.load(open(p))
d['recall'][2]['parts'][0]['accept']=["recostarse","tumbarse","echarse"]
d['recall'][3]['parts'][1]['accept']=["descanso","respiro"]
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
