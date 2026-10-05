import json
p='es.json'; d=json.load(open(p))
fixes=[
 ('4865','nouns',0,'una torre del reloj','una torre de reloj'),
 ('4866','phrases',2,'romper en aplausos','estallar en aplausos'),
 ('4874','phrases',0,'estar sentado en una bicicleta','estar sentada en una bicicleta'),
 ('4888','phrases',0,'llevar un sencillo vestido de verano blanco','llevar un sencillo vestido blanco de verano'),
 ('4900','phrases',1,'derramar la compra sobre el césped','desparramar la compra por el césped'),
 ('4924','answer',None,'Está mirando su móvil.','Está mirando el móvil.'),
 ('4932','nouns',3,'una manija de puerta','una manilla de puerta'),
]
for i,f,k,a,b in fixes:
    if k is None: assert d[i][f]==a,(i,f); d[i][f]=b
    else: assert d[i][f][k]==a,(i,f,k); d[i][f][k]=b
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
