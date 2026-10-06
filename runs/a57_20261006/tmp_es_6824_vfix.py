import json
p='content/es/6824.json'; d=json.load(open(p))
d['taps'][0]['phrase']='secarse el sudor de la frente'
d['recall'][0]['parts']=[{"text":"secarse el"},{"text":"sudor","gap":True,"accept":["sudor"]},{"text":"de la frente"}]
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
