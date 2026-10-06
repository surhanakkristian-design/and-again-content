import json
def load(i): return json.load(open(f'content/es/{i}.json'))
def save(i,d): open(f'content/es/{i}.json','w').write(json.dumps(d,ensure_ascii=False,indent=1)+"\n")
def gap(d,row): return [p for p in d['recall'][row]['parts'] if p.get('gap')][0]
d=load(198); g=gap(d,2); assert g['text']=='pulgar'; g['accept']=['pulgar']; save(198,d)
d=load(201); g=gap(d,1); assert g['text']=='agua'; g['accept']=['agua','río']; save(201,d)
d=load(202); g=gap(d,2); assert g['text']=='pulgar'; g['accept']=['pulgar']
g=gap(d,1); assert g['text']=='móvil'; g['accept']=['móvil','teléfono']
g=gap(d,3); assert g['text']=='cruzando'; g['accept']=['cruzando','atravesando']; save(202,d)
