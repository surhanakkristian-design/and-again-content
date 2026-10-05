import json
p='es.json'; d=json.load(open(p))
fixes=[
('4749','phrases',0,'darse la mano en formación','darse las manos en formación'),
('4749','answer',None,'Se están dando la mano en formación.','Se están dando las manos en formación.'),
('4752','phrases',1,'expulsar una tostada quemada','hacer saltar una tostada quemada'),
('4769','question',None,'¿Dónde está la mujer de pie?','¿Dónde está de pie la mujer?'),
('4808','phrases',0,'peinar un pelo largo','peinar una melena larga'),
('4811','phrases',0,'llevar un chaleco naranja chillón','llevar una camiseta de tirantes naranja chillón'),
('4826','phrases',0,'verterse por encima de la presa','desbordarse por encima de la presa'),
('4826','answer',None,'El agua se está vertiendo por encima de la presa.','El agua se está desbordando por encima de la presa.'),
('4830','phrases',1,'mirar hacia la luz','alzar la vista hacia la luz'),
('4833','question',None,'¿Por dónde está patinando el patinador?','¿Por dónde va el patinador?'),
('4833','answer',None,'Está patinando por la costa.','Va por la costa.'),
('4845','phrases',1,'sostener la tela blanca','sujetar la tela blanca'),
]
for k,f,i,b,a in fixes:
    if i is None: assert d[k][f]==b,(k,f); d[k][f]=a
    else: assert d[k][f][i]==b,(k,f,i); d[k][f][i]=a
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
