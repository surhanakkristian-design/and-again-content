import json
p='content/es/241.json'
d=json.load(open(p))
d['question']="¿Qué le enseña el hombre a la mujer?"
d['answer']=["Le","enseña","su","dibujo."]
d['recall'][3]={"from":"answer","parts":[{"text":"Le"},{"text":"enseña","gap":True,"accept":["enseña","muestra"]},{"text":"su dibujo"}]}
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
