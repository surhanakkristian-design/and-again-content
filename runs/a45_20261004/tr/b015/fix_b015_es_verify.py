import json
p='es.json'; d=json.load(open(p))
def rep(i,field,idx,old,new):
    cur=d[i][field] if idx is None else d[i][field][idx]
    assert cur==old,(i,field,cur)
    if idx is None: d[i][field]=new
    else: d[i][field][idx]=new
rep('4617','nouns',3,'una armadura','armadura')
rep('4645','phrases',2,'estar lleno de agujeros','estar llena de agujeros')
rep('4652','answer',None,'Dos personas están compitiendo en un pulso.','Dos personas están echando un pulso.')
rep('4684','answer',None,'Se están saludando chocando los codos.','Están chocando los codos unos con otros.')
rep('4698','nouns',2,'un mono de trabajo','mono de trabajo')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
