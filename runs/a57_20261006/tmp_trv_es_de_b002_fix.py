import json
P='/Users/kristiansurhanak/Projects/and-again-content/runs/a57_20261006/tr/b002/de/es.json'
t=json.load(open(P))
log=[]
def fix(i,field,idx,new,why):
    x=t[i]
    old = x[field][idx] if idx is not None else x[field]
    if idx is None: x[field]=new
    else: x[field][idx]=new
    log.append(f"{i} | {field}{'' if idx is None else '['+str(idx)+']'} | {old} -> {new} | {why}")
W1='"rosa rosa" is correct but clumsy; "de color rosa" is the natural wording'
fix('620','phrases',0,'oler una rosa de color rosa',W1)
fix('620','recall',0,'oler una rosa de color rosa',W1)
fix('620','answer',None,'Está oliendo una rosa de color rosa.',W1)
fix('620','recall',3,'huele una rosa de color rosa',W1)
fix('68','phrases',2,'enrollarse alrededor de la mano','source is passive with the bandage as subject; "envolver la mano" changed subject and meaning')
fix('68','recall',2,'enrollarse alrededor de la mano','same as phrase')
fix('68','answer',None,'Le está enrollando una venda alrededor de la mano.','"wickeln" = enrollar; same verb as the phrase inside the video')
fix('68','recall',3,'le enrolla una venda alrededor de la mano','same as answer')
fix('7239','phrases',2,'presionar contra la cabeza del hombre','"gegen ... drücken" = press against, not push')
fix('7239','recall',2,'presionar contra la cabeza del hombre','same as phrase')
fix('7835','phrases',0,'precipitarse por las rocas','"über die Felsen stürzen" = cascade over the rocks; "caer sobre" means landing on them')
fix('7835','recall',0,'precipitarse por las rocas','same as phrase')
fix('4156','phrases',0,'estar de pie sobre el torso del hombre','Oberkörper = torso, not only chest')
fix('4156','recall',0,'estar de pie sobre el torso del hombre','same as phrase')
fix('98','phrases',1,'cerrar los ojos con fuerza','"apretar los ojos" is unidiomatic for zukneifen')
fix('98','recall',1,'cerrar los ojos con fuerza','same as phrase')
fix('7997','phrases',1,'estar con una rodilla en el suelo','"arrodillado sobre una rodilla" is redundant and unnatural')
fix('7997','recall',1,'estar con una rodilla en el suelo','same as phrase')
W2='"osito" (diminutive) clashes with "gigante"; oso de peluche used throughout the video'
fix('4434','phrases',0,'abrazar un oso de peluche',W2)
fix('4434','recall',0,'abrazar un oso de peluche',W2)
fix('4434','nouns',3,'el oso de peluche',W2)
fix('4434','answer',None,'Abraza un oso de peluche gigante.',W2)
fix('4434','recall',4,'abraza un oso de peluche gigante',W2)
fix('5417','nouns',0,'los cables aéreos','source noun is plural (Oberleitungen); plurals stay plural')
W3='"cargar con dificultad con" is clumsy (double con)'
fix('4918','phrases',1,'cargar a duras penas con bolsas pesadas',W3)
fix('4918','recall',1,'cargar a duras penas con bolsas pesadas',W3)
W4='"pase" is kitchen jargon; Küchentheke abwischen = wipe the kitchen counter'
fix('730','phrases',0,'limpiar la barra de la cocina',W4)
fix('730','recall',0,'limpiar la barra de la cocina',W4)
W5='Hilfestellung geben = give support/spot; "asegurar" means belaying and "a su compañera" was added'
fix('5540','phrases',1,'prestar ayuda',W5)
fix('5540','recall',1,'prestar ayuda',W5)
W6='"arder de calor" is unnatural for an oven glowing with heat'
fix('4364','phrases',2,'estar al rojo vivo',W6)
fix('4364','recall',2,'estar al rojo vivo',W6)
json.dump(t,open(P,'w'),ensure_ascii=False,indent=1)
open('/Users/kristiansurhanak/Projects/and-again-content/runs/a57_20261006/tr/b002/de/tmp_trv_es_de_b002_log.txt','w').write('\n'.join(log))
print(len(log))
