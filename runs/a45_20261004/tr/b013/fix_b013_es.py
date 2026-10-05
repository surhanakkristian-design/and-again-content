import json
f='es.json'; d=json.load(open(f))
fixes=[
("4283","phrases",1,"poner comida en platos","English bare plural 'plates', no definite article"),
("4335","phrases",0,"ser la primera en levantar la mano","'levantar la mano la primera' is unidiomatic"),
("4376","phrases",1,"estar tumbada en la hierba","target is the woman: feminine agreement"),
("4380","phrases",1,"estar tumbada en la bañera","target is the woman: feminine agreement"),
("4385","phrases",1,"estar sentada en la cama","target is the woman: feminine agreement"),
("4391","answer",None,"Está comiendo una pizza a solas.","'una pizza sola' reads as 'a pizza on its own'"),
("4405","phrases",0,"estar sentado frente a un escritorio","'ante un escritorio' is stilted"),
("4406","phrases",0,"difuminar franjas marcadas","English has no article ('harsh stripes')"),
("4413","phrases",1,"abrir los brazos de par en par","'abrir mucho los brazos' is unnatural for arms"),
("4418","answer",None,"Sale de golpe una nube de vapor.","'bursts out' lost in 'sale'"),
("4438","phrases",0,"dar toques a un balón","football juggling is 'dar toques', not 'hacer malabares'"),
]
log=[]
for vid,field,i,new,why in fixes:
    if i is None: old=d[vid][field]; d[vid][field]=new
    else: old=d[vid][field][i]; d[vid][field][i]=new
    log.append(f"- {vid} {field}{'' if i is None else '['+str(i)+']'}: {old} -> {new} ({why})")
json.dump(d,open(f,'w'),ensure_ascii=False,indent=1)
open('_fixlog_b013_es.txt','w').write("\n".join(log)+"\n")
