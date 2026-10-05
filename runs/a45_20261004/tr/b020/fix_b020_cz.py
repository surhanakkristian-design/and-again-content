import json
p='cz.json'; d=json.load(open(p))
F=[
("5224","answer",None,"Uklání se králi.","Uklánějí se králi.","3rd person plural made unambiguous (uklání reads as singular)"),
("5259","phrases",1,"lapat po dechu překvapením","překvapeně zalapat po dechu","lapat po dechu = struggle for breath; a gasp of surprise is perfective zalapat"),
("5298","phrases",2,"zalapat po dechu překvapením","překvapeně zalapat po dechu","more natural word order, same wording as 5259"),
("5298","phrases",1,"sáhnout po další lahvičce","sáhnout po dalším flakonu","same word for the bottles as the noun flakony parfému"),
("5265","answer",None,"Dívá se svým dalekohledem.","Dívá se dalekohledem.","redundant possessive is unnatural in Czech"),
("5292","answer",None,"Usíná u svého stolu.","Usíná u stolu.","redundant possessive is unnatural in Czech"),
("5270","phrases",0,"brát krabice cereálií","popadat krabice cereálií","grab = seize quickly, brát is too weak"),
("5276","phrases",2,"ležet na žulové lince","ležet na žulové pracovní desce","counter = worktop (pracovní deska), linka is the kitchen unit"),
("5276","nouns",3,"žulová linka","žulová pracovní deska","same as the phrase fix"),
("5294","answer",None,"Chodí v bačkorách.","Jde v bačkorách.","ongoing walking now = jde (chodí is habitual), matches phrase jít chodbou"),
("5327","answer",None,"Stříká lak na vlasy na vyčesaný účes.","Stříká vyčesaný účes lakem na vlasy.","clumsy double na"),
("5336","phrases",1,"svírat svou bekovku","svírat bekovku","redundant possessive"),
("5336","question",None,"Co dělá muž s šedivými vousy?","Co dělá muž se šedivými vousy?","vocalised preposition se before š"),
]
log=[]
for vid,f,i,b,a,why in F:
    if i is None:
        assert d[vid][f]==b,(vid,f,d[vid][f]); d[vid][f]=a
    else:
        assert d[vid][f][i]==b,(vid,f,d[vid][f][i]); d[vid][f][i]=a
    log.append(f"- {vid}, {f}{'' if i is None else '['+str(i)+']'}: {b} -> {a} ({why})")
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
open('_fixlog_b020_cz.txt','w').write("\n".join(log)+"\n")
