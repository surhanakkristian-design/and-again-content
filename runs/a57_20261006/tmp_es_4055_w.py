import json
def row(frm,parts):
    out=[]
    for p in parts:
        if isinstance(p,list): out.append({"text":p[0],"gap":True,"accept":p})
        else: out.append({"text":p})
    return {"from":frm,"parts":out}
def mk(i,kw,taps,nouns,q,a,av,rec,notes):
    d={"mediaId":i,"lang":"es","level":"A","keyWord":kw,
       "taps":[{"phrase":p,"target":t,"voice":v} for p,t,v in taps],
       "nouns":[{"word":w,"voice":v} for w,v in nouns],
       "question":q,"answer":a.split(),"answerVoice":av,"carousel":[],
       "recall":[row(f,p) for f,p in rec],"notes":notes}
    json.dump(d,open(f'content/es/{i}.json','w'),ensure_ascii=False,indent=1)
m,f="male","female"
mk(4055,"el dinosaurio",
 [("levantar la cabeza","el perro",m),("sentarse entre dos juguetes","el perro",m),("tener los ojos rojos","el dinosaurio gris",m)],
 [("el perro",m),("el dinosaurio",m),("la cama",m)],
 "¿Dónde está sentado el perro?","Está sentado entre dos dinosaurios.",m,
 [("taps",["levantar la",["cabeza"]]),("taps",[["sentarse"],"entre dos juguetes"]),("taps",["tener los",["ojos"],"rojos"]),
  ("answer",["Está sentado entre dos",["dinosaurios"]])],
 "Subject dropped (answer row = whole sentence). No noun row: the answer row contains the key word (dinosaurios) and gaps it. Only the grey dinosaur has red eyes.")
mk(665,"la oveja",
 [("comer hierba verde","la oveja grande",m),("abrir mucho la boca","la oveja grande",m),("caminar por el campo","la oveja grande",m)],
 [("la oveja",m),("el muro",m),("el cielo",m),("la hierba",m)],
 "¿Qué está haciendo la oveja?","Está caminando por el campo.",m,
 [("taps",["comer",["hierba"],"verde"]),("taps",["abrir mucho la",["boca"]]),("taps",[["caminar"],"por el campo"]),
  ("nouns",["la",["oveja"]]),("answer",["Está caminando por el",["campo"]])],
 "Subject dropped. 'el muro' = the dry-stone wall in the background. Sheep trots at the end; 'caminar' kept at level A.")
mk(518,"el búho",
 [("estar posado en una rama","el búho",f),("girar la cabeza","el búho",f),("volar entre los árboles","el búho",f)],
 [("el búho",f),("la rama",f),("el árbol",f)],
 "¿Qué está haciendo el búho?","Está posado en una rama.",f,
 [("taps",["estar",["posado"],"en una rama"]),("taps",["girar la",["cabeza"]]),("taps",["volar entre los",["árboles"]]),
  ("nouns",["el",["búho"]]),("answer",["Está posado en una",["rama"]])],
 "'posado' (A2/B1) is the plain natural word for a bird on a branch; 'sentado' would be wrong for a bird. Subject dropped.")
mk(332,"la jirafa",
 [("comer hojas verdes","la jirafa",f),("bajar la cabeza","la jirafa",f),("beber agua","la jirafa",f)],
 [("la jirafa",f),("la cebra",f),("el agua",f),("el cielo",f)],
 "¿Qué está haciendo la jirafa?","Está bebiendo agua.",f,
 [("taps",["comer",["hojas"],"verdes"]),("taps",[["bajar"],"la cabeza"]),("taps",["beber",["agua"]]),
  ("nouns",["la",["jirafa"]]),("answer",["Está",["bebiendo","tomando"],"agua"])],
 "Several zebras in the background; noun kept singular as in English (pill on one zebra). Subject dropped.")
mk(82,"la abeja",
 [("posarse en una flor","la abeja",f),("volar sobre la hierba","la abeja",f),("entrar en una colmena","la abeja",f)],
 [("la abeja",f),("la flor",f),("la hoja",f)],
 "¿Qué está haciendo la abeja?","Está posada en una flor.",f,
 [("taps",[["posarse"],"en una flor"]),("taps",["volar sobre la",["hierba"]]),("taps",["entrar en una",["colmena"]]),
  ("nouns",["la",["abeja"]]),("answer",["Está posada en una",["flor"]])],
 "Phrase 3: English 'box' is a wooden beehive; a native says 'colmena' (A2/B1) rather than 'caja', used as the plain right word. The insect is a bumblebee (abejorro), but the key word 'la abeja' is what a learner names it. Subject dropped.")
