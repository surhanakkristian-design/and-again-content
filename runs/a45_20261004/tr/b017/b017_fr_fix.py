import json
p='fr.json'; d=json.load(open(p))
fixes=[
("4865","nouns",0,"une tour de l'horloge","une tour d'horloge","specific 'la tour de l'horloge' wrong for indefinite 'a clock tower'"),
("4866","phrases",1,"planer au-dessus du champ","rester en vol stationnaire au-dessus du champ","'planer' = glide; a hovering drone is 'en vol stationnaire'"),
("4866","answer",None,"Le drone plane bas au-dessus du champ.","Le drone reste en vol stationnaire juste au-dessus du champ.","same sense fix as phrase; 'plane bas' unidiomatic"),
("4870","phrases",1,"se pencher sur le client","se pencher au-dessus du client","'se pencher sur' reads as 'study/examine'; physical leaning = 'au-dessus de'"),
("4870","answer",None,"Il se penche sur le client.","Il se penche au-dessus du client.","consistency with phrase"),
("4870","nouns",1,"de la barbe de trois jours","une barbe de trois jours","'barbe de trois jours' is a count expression; partitive unidiomatic"),
("4894","phrases",0,"se tenir devant","se tenir à l'avant","'se tenir devant' dangles without an object"),
("4908","phrases",0,"se plier en forme de S","se courber en forme de S","'se plier' = fold; bend into a curve = 'se courber'"),
("4929","phrases",0,"courir en cours","courir pour aller en cours","'courir en cours' is ungrammatical for motion to class"),
("4929","answer",None,"Il court en cours.","Il court pour aller en cours.","same as phrase"),
("4936","nouns",0,"un chapeau","une toque","the cook's tall white hat is 'une toque' (right sense)"),
("4958","question",None,"Que fait la femme en crème ?","Que fait la femme habillée en crème ?","'la femme en crème' unidiomatic/ambiguous"),
("4961","phrases",0,"attraper une souris en jouet","attraper une souris jouet","natural compound is 'souris jouet'"),
("4961","nouns",3,"une souris en jouet","une souris jouet","same"),
("4961","answer",None,"Il joue avec une souris en jouet.","Il joue avec une souris jouet.","same"),
("4968","phrases",0,"ramasser une carte","prendre une carte","'ramasser' = pick up from the ground; card is taken from the counter"),
("4972","answer",None,"Elle a des peintures patriotiques sur les joues.","Elle a du maquillage patriotique sur les joues.","'des peintures' = paintings; face paint = maquillage"),
]
log=[]
for vid,f,i,old,new,why in fixes:
    cur=d[vid][f][i] if i is not None else d[vid][f]
    assert cur==old,(vid,f,cur)
    if i is None: d[vid][f]=new
    else: d[vid][f][i]=new
    log.append(f"- {vid}, {f}{'' if i is None else '['+str(i)+']'}: {old} -> {new} ({why})")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
n=sum(len(v['phrases'])+len(v['nouns'])+2 for v in d.values())
open('b017_fr_fixlog.txt','w').write(str(n)+"\n"+"\n".join(log)+"\n")
print(n,len(log))
