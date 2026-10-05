import json
p='es.json'; d=json.load(open(p))
fixes=[
 ('7075','answer',None,'Está apuntando notas en un portapapeles.','Está tomando notas en un portapapeles.'),
 ('7079','nouns',2,'una bobina','un rollo'),
 ('7127','phrases',2,'mirar el pan','levantar la vista hacia el pan'),
 ('7134','nouns',2,'un futbolista','un jugador de fútbol americano'),
 ('7144','phrases',0,'vaciar una cesta de freír','vaciar una cesta de freidora'),
 ('7147','nouns',2,'un bol','un bol para mezclar'),
 ('7155','phrases',0,'trepar por el muro','trepar por encima del muro'),
 ('7155','answer',None,'Está trepando por un muro cubierto de hiedra.','Está trepando por encima de un muro cubierto de hiedra.'),
 ('7168','nouns',0,'la aguja de una iglesia','una aguja de iglesia'),
 ('7173','phrases',1,'decorar un barco viejo','decorar un bote viejo'),
 ('7173','answer',None,'Está pegando conchas en un barco viejo.','Está pegando conchas en un bote viejo.'),
 ('7194','phrases',0,'sostener un grabado de una polilla','sostener una lámina con una polilla'),
 ('7194','answer',None,'Está fijando con chinchetas un grabado de una polilla.','Está fijando con chinchetas una lámina con una polilla.'),
]
for k,f,i,old,new in fixes:
    if i is None:
        assert d[k][f]==old,(k,f,d[k][f]); d[k][f]=new
    else:
        assert d[k][f][i]==old,(k,f,d[k][f][i]); d[k][f][i]=new
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print(len(fixes))
