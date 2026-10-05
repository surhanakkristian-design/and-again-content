import json
p='es.json'; d=json.load(open(p))
fixes=[
 ('5351','answer',None,'Está mirando asombrada las guirnaldas de luces.','Está alzando la vista hacia las guirnaldas de luces.'),
 ('5355','nouns',2,'un gato pelirrojo','un gato naranja'),
 ('5367','phrases',1,'llevar una camiseta teñida','llevar una camiseta tie-dye'),
 ('5371','phrases',0,'poner el poste en pie','empujar el poste hasta ponerlo derecho'),
 ('5383','nouns',2,'un abrigo de leopardo','un abrigo de estampado de leopardo'),
 ('5396','nouns',1,'banderas','banderines'),
 ('5396','answer',None,'Está marcando una línea con banderas naranjas.','Está marcando una línea con banderines naranjas.'),
 ('5400','phrases',2,'llevar un bolso plateado','sostener un bolso plateado'),
 ('5418','phrases',1,'asomarse por el vagón','asomarse fuera del vagón'),
 ('5453','phrases',1,'arreglar las flores','colocar las flores'),
 ('5453','answer',None,'Está arreglando flores en un jarrón.','Está colocando flores en un jarrón.'),
 ('5462','answer',None,'Se está poniendo la mano en el pecho.','Está apoyando la mano en el pecho.'),
 ('5477','phrases',2,'desplomarse en un montón','caer todos amontonados'),
]
for k,f,i,b,a in fixes:
    if i is None:
        assert d[k][f]==b,(k,f,d[k][f]); d[k][f]=a
    else:
        assert d[k][f][i]==b,(k,f,i,d[k][f][i]); d[k][f][i]=a
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print(len(fixes))
