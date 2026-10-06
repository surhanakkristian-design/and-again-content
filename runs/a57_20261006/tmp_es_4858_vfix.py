import json
p='content/es/4858.json'; d=json.load(open(p))
d['answer']=["El","chico","ha","construido","una","espiral","de","fichas","de","dominó."]
d['recall'][3]['parts'][1]['text']="una espiral de fichas de dominó"
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
