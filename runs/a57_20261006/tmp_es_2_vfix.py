import json
p='content/es/2.json'; d=json.load(open(p))
d['recall'][1]['parts'][0]['accept']=['abrazar']
d['recall'][3]['parts'][1]['accept']=['presumiendo','fardando']
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
