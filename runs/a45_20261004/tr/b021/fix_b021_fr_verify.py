import json
p='fr.json'; d=json.load(open(p))
fixes=[
("5351","phrases",1,"lever les yeux avec émerveillement","entry form: participle agreement replaced by neutral infinitive phrase"),
("5352","phrases",1,"se prendre la tête entre les mains","bare 'se prendre la tête' is the idiom 'to get worked up', not the gesture"),
("5352","answer",None,"Elle se prend la tête entre les mains, frustrée.","same gesture as the phrase"),
("5356","nouns",1,"la silhouette de la ville","'les gratte-ciel' = skyscrapers, not skyline"),
("5360","phrases",1,"entrer en station","metro trains pull into a 'station', not a 'gare'"),
("5360","nouns",2,"un blouson teddy","usual French term for a varsity jacket"),
("5360","answer",None,"Il traverse une station bondée.","underground station = station, not gare"),
("5366","phrases",0,"viser à l'abri d'une barricade","'viser derrière' reads as aiming at a point behind the barricade"),
("5366","nouns",1,"un baril","an oil drum is a metal drum; 'bidon d'huile' is a can of oil"),
("5367","answer",None,"Elle s'enfourne un burger dans la bouche.","'s'enfoncer' is not the idiom for stuffing food; s'enfourner"),
("5373","phrases",2,"se gonfler jusqu'à devenir un château","'se gonfler en château' is not French"),
("5375","phrases",0,"faire un swing avec un club de golf","'balancer un club' suggests throwing it"),
("5375","answer",None,"Elle se balance au bout d'une grosse corde.","'se balancer à une corde' unidiomatic"),
("5383","nouns",2,"un manteau à imprimé léopard","correct form of the print noun"),
("5385","phrases",0,"se regrouper en cercle serré","'tight circle' was lost; more natural"),
("5391","phrases",1,"toucher le panneau","basketball backboard = le panneau"),
("5402","phrases",1,"boire de l'eau à grandes gorgées","'avaler un peu d'eau d'un trait' contradictory and unnatural"),
("5403","nouns",1,"une fiche horaire","singular 'a timetable' must stay singular"),
("5411","answer",None,"Elle presse du dentifrice sur trois brosses à dents.","'squeezing' was lost ('met')"),
("5415","nouns",3,"une moto","English label is motorbike; meaning identical to English"),
("5416","phrases",0,"regarder avec stupéfaction","entry form without participle agreement"),
("5437","phrases",1,"lever un pain tressé","braided loaf = pain tressé; brioche is a narrower sense"),
("5437","nouns",1,"un pain tressé","same word as the phrase"),
("5437","answer",None,"Elle lève un pain tressé.","same word as the phrase"),
("5438","nouns",0,"de la garniture","fruit filling is 'garniture'; 'farce' is savoury stuffing"),
("5455","phrases",2,"regarder son passeport d'un air radieux","entry form without comma/participle"),
("5455","answer",None,"Il regarde son passeport d'un air radieux.","matches the phrase"),
("5460","answer",None,"Ils se penchent au-dessus des poubelles.","ongoing action, not a resulting state"),
("5462","question",None,"Que fait la femme au chemisier moutarde ?","'la femme en moutarde' is not French"),
("5469","phrases",0,"marcher à grands pas avec des bâtons de marche","same word as the answer (walking poles)"),
]
log=[]
for vid,f,i,new,why in fixes:
    if i is None: old=d[vid][f]; d[vid][f]=new
    else: old=d[vid][f][i]; d[vid][f][i]=new
    log.append(f"- {vid} {f}{'' if i is None else '['+str(i)+']'}: {old} -> {new} ({why})")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
open('_fixlog_b021_fr.txt','w').write("\n".join(log)+"\n")
print(len(log))
