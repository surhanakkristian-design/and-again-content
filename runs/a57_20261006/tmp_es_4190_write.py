import json
def T(p,t,v): return {"phrase":p,"target":t,"voice":v}
def N(w,v): return {"word":w,"voice":v}
def R(src,*parts):
    out=[]
    for p in parts:
        if isinstance(p,tuple): out.append({"text":p[0],"gap":True,"accept":list(p)})
        else: out.append({"text":p})
    return {"from":src,"parts":out}
F="female";M="male"
D={
4190:dict(level="A",keyWord="encontrarse",
 taps=[T("estar sentado en un muro","el gato",F),T("tener una melena oscura","el león",F),T("ser naranja y blanco","el gato",F)],
 nouns=[N("los árboles",F),N("el león",F),N("la hierba",F),N("el gato",F)],
 question="¿Qué hace el gato?",answer="El gato se encuentra con un león grande.",answerVoice=F,
 recall=[R("taps","estar sentado en un",("muro","murete")),R("taps","tener una",("melena",),"oscura"),R("taps","ser",("naranja",),"y blanco"),
         R("answer","se",("encuentra",),"con un león grande")],
 notes="Phrase 1: the cat sits on a low concrete ledge (murete) by the bars; 'muro' kept as the A-level word, 'murete' accepted. Phrase 2: the lioness is also in some frames but has no mane, so 'tener una melena oscura' fits only the male lion. keyWord 'encontrarse' (con) = meet face to face; used in the answer."),
5652:dict(level="A",keyWord="grande",
 taps=[T("oler la pelota grande","el perro",F),T("ser más grande que el perro","la pelota grande",F),T("ser más pequeña que el perro","la pelota pequeña",F)],
 nouns=[N("los árboles",F),N("la pelota",F),N("el perro",F),N("la hierba",F)],
 question="¿Qué está haciendo el perro?",answer="El perro está oliendo una pelota grande.",answerVoice=F,
 recall=[R("taps",("oler","olfatear"),"la pelota grande"),R("taps","ser más",("grande",),"que el perro"),R("taps","ser más pequeña que el",("perro",)),
         R("answer","está oliendo una",("pelota",),"grande")],
 notes="Phrases 2/3 compare each ball with the dog (the giant ball is taller than the dog, the normal one much smaller) instead of 'ser la pelota más grande/pequeña', which sounds unnatural as an entry. 'la pelota' = tennis ball in Spain."),
26:dict(level="A",keyWord="la pajita",
 taps=[T("sujetar una pajita larga","el hombre",M),T("beber zumo de naranja","el hombre",M),T("estar sobre la barra","el vaso",M)],
 nouns=[N("las gafas de sol",M),N("la pajita",M),N("el vaso",M),N("la camisa",M)],
 question="¿Qué está haciendo el hombre?",answer="El hombre está bebiendo zumo con una pajita.",answerVoice=M,
 recall=[R("taps","sujetar una",("pajita",),"larga"),R("taps",("beber","tomar"),"zumo de naranja"),R("taps","estar sobre la",("barra",)),
         R("answer","está bebiendo",("zumo",),"con una pajita")],
 notes="Phrase 3: in the last boxed frames the man holds the empty glass upside down in the air; in most boxed frames it stands on the bar. Glass is a stemmed glass ('vaso' is the everyday word in Spain for a drinking glass; 'copa' also possible)."),
324:dict(level="A",keyWord="el gaming",
 taps=[T("levantar los dos brazos","la chica",F),T("ganar la partida","la chica",F),T("llevar una chaqueta roja","el chico",M)],
 nouns=[N("la chica",F),N("la chaqueta",F),N("las cajas",F),N("el sofá",F)],
 question="¿Quién está ganando la partida?",answer="La chica está ganando la partida.",answerVoice=F,
 recall=[R("taps","levantar los dos",("brazos",)),R("taps",("ganar",),"la partida"),R("taps","llevar una",("chaqueta",),"roja"),
         R("answer","está ganando la",("partida",))],
 notes="Phrase 1: English 'put both hands up'; she raises both arms with fists, so 'levantar los dos brazos'. In the first boxed frames she is still holding the controller (phrase true for most of the clip's end). keyWord 'el gaming' is not a noun of the set and is not used; it is an anglicism (B-ish), natives also say 'jugar a videojuegos'."),
612:dict(level="A",keyWord="a la derecha",
 taps=[T("señalar a la derecha","la mujer",F),T("llevar una mochila grande","el hombre",M),T("decir adiós con la mano","la mujer",F)],
 nouns=[N("las luces",F),N("la mujer",F),N("la comida",F),N("la rueda",F)],
 question="¿Hacia dónde está señalando la mujer?",answer="La mujer está señalando a la derecha.",answerVoice=F,
 recall=[R("taps","señalar a la",("derecha",)),R("taps","llevar una",("mochila",),"grande"),R("taps","decir adiós con la",("mano",)),
         R("answer","está",("señalando",),"a la derecha")],
 notes="Phrase 3: the woman waves only at the end; in earlier boxed frames she points or turns the man around (phrase written for the wave, as English). Phrase 1 likewise: she points in the middle frames."),
}
for i,d in D.items():
    o={"mediaId":i,"lang":"es","level":d["level"],"keyWord":d["keyWord"],"taps":d["taps"],"nouns":d["nouns"],
       "question":d["question"],"answer":d["answer"].split(),"answerVoice":d["answerVoice"],"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(o,open(f"content/es/{i}.json","w"),ensure_ascii=False,indent=1)
