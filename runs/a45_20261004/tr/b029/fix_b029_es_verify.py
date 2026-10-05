import json
p='es.json'; d=json.load(open(p))
fixes=[
('7765','phrases',0,'cortar sus tortitas','cortar las tortitas'),
('7785','phrases',1,'derramar su bebida','derramar la bebida'),
('7796','phrases',1,'estampar un informe sobre el mostrador','dejar un informe de golpe'),
('7796','phrases',2,'alzar los brazos','levantar las manos'),
('7812','phrases',1,'tirar su café','tirar el café'),
('7818','phrases',2,'echar un vistazo a su reloj','echar un vistazo al reloj'),
('7824','phrases',0,'agacharse sobre su tabla','agacharse sobre la tabla'),
('7829','question',None,'¿Qué está haciendo la mujer de coral?','¿Qué está haciendo la mujer de color coral?'),
('7834','question',None,'¿Qué está haciendo la mujer de cuero?','¿Qué está haciendo la mujer de la chaqueta de cuero?'),
]
for k,f,i,a,b in fixes:
    if i is None:
        assert d[k][f]==a,(k,f); d[k][f]=b
    else:
        assert d[k][f][i]==a,(k,f,i); d[k][f][i]=b
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
print('ok',len(fixes))
