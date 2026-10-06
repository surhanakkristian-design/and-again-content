import json
def T(p,t,v): return {"phrase":p,"target":t,"voice":v}
def N(w,v): return {"word":w,"voice":v}
def R(frm,parts):
    out=[]
    for p in parts:
        if isinstance(p,tuple): out.append({"text":p[0],"gap":True,"accept":list(p[1])})
        else: out.append({"text":p})
    return {"from":frm,"parts":out}
D={}
D[240]=dict(level="B",keyWord="el empate",
 taps=[T("llevar una camiseta turquesa","la mujer de turquesa","female"),T("tener una barba poblada","el hombre corpulento","male"),T("cubrir las manos con un paño","la abuela","female")],
 nouns=[N("el paño","female"),N("la mesa","female"),N("la anciana","female")],
 question="¿Cómo termina el pulso?",answer="El pulso termina en empate.".split(),answerVoice="female",
 recall=[R("taps",["llevar una",("camiseta",["camiseta"]),"turquesa"]),R("taps",["tener una barba",("poblada",["poblada","espesa","tupida"])]),
  R("taps",[("cubrir",["cubrir","tapar"]),"las manos con un paño"]),R("answer",["termina en",("empate",["empate"])])],
 notes="Phrase 3: the grandmother holds up the tea towel in most boxed frames and lays it over the locked hands at the end; 'cubrir las manos con un paño' describes the drape. 'el pulso' = arm-wrestling (Spain).")
D[241]=dict(level="A",keyWord="el dibujo",
 taps=[T("estar sentado en los escalones","el hombre","male"),T("hacer un dibujo","el hombre","male"),T("llevar un sombrero amarillo","la mujer","female")],
 nouns=[N("el dibujo","male"),N("el sombrero","male"),N("las casas","male"),N("la camisa","male")],
 question="¿Qué le está enseñando el hombre a la mujer?",answer="Le está enseñando su dibujo.".split(),answerVoice="male",
 recall=[R("taps",["estar sentado en los",("escalones",["escalones","peldaños"])]),R("taps",["hacer un",("dibujo",["dibujo"])]),
  R("taps",["llevar un",("sombrero",["sombrero"]),"amarillo"]),R("answer",["Le está",("enseñando",["enseñando","mostrando"]),"su dibujo"])],
 notes="Answer drops the subject (natural in Spain), so the answer row is the whole sentence. Many boxed frames for phrases 1/2 are close-ups of the pencil/face where the steps are not visible; the man sits on the steps in the wide shots.")
D[243]=dict(level="A",keyWord="vestirse",
 taps=[T("ponerse un jersey","la mujer","female"),T("ayudarla a vestirse","el hombre","male"),T("mirarse en el espejo","la mujer","female")],
 nouns=[N("el gorro","female"),N("el bolso","female"),N("la puerta","female"),N("los vaqueros","female")],
 question="¿Qué está haciendo el hombre?",answer="La está ayudando a vestirse.".split(),answerVoice="male",
 recall=[R("taps",["ponerse un",("jersey",["jersey"])]),R("taps",["ayudarla a",("vestirse",["vestirse"])]),
  R("taps",["mirarse en el",("espejo",["espejo"])]),R("answer",["La está",("ayudando",["ayudando"]),"a vestirse"])],
 notes="The English tap boxes 1 and 3 also cover the boot-lacing and door frames; phrases written for what the woman does in most boxed frames. Answer drops the subject, so the answer row is the whole sentence.")
D[244]=dict(level="A",keyWord="la bebida",
 taps=[T("beber zumo de naranja","el hombre","male"),T("hacer zumo de naranja","la mujer","female"),T("estar posado en un palo","el loro","male")],
 nouns=[N("el loro","male"),N("el hombre","male"),N("el zumo","male"),N("las naranjas","male")],
 question="¿Qué está haciendo el hombre?",answer="Está bebiendo un vaso de zumo de naranja.".split(),answerVoice="male",
 recall=[R("taps",[("beber",["beber","tomar"]),"zumo de naranja"]),R("taps",["hacer",("zumo",["zumo"]),"de naranja"]),
  R("taps",["estar posado en un",("palo",["palo"])]),R("answer",["Está bebiendo un",("vaso",["vaso"]),"de zumo de naranja"])],
 notes="'posado' (B1) is the plain right word for a bird on a perch; no A-level alternative sounds native. Key word 'la bebida' appears in no exercise (as in English, the juice is named 'zumo'). Answer drops the subject, so the answer row is the whole sentence.")
D[245]=dict(level="A",keyWord="beber",
 taps=[T("lavarse las manos","la mujer","female"),T("llenar la botella","el hombre","male"),T("estar sentado en las rocas","el animalito","male")],
 nouns=[N("el cielo","male"),N("las montañas","male"),N("la mujer","female"),N("el hombre","male")],
 question="¿Qué están haciendo los dos?",answer="Están bebiendo agua de sus botellas.".split(),answerVoice="male",
 recall=[R("taps",["lavarse las",("manos",["manos"])]),R("taps",[("llenar",["llenar","rellenar"]),"la botella"]),
  R("taps",["estar sentado en las",("rocas",["rocas","piedras"])]),R("answer",["Están",("bebiendo",["bebiendo","tomando"]),"agua de sus botellas"])],
 notes="English box 1 covers the woman mostly while she drinks (the man drinks too); she washes her hands only at the fountain frames - phrase kept as English, verifier please check. Phrase 3 target is a marmot; named 'el animalito' so 'sentado' agrees. Answer drops the subject, so the answer row is the whole sentence.")
for i,d in D.items():
    o={"mediaId":i,"lang":"es",**{k:d[k] for k in ["level","keyWord","taps","nouns","question","answer","answerVoice"]},"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(o,open(f"content/es/{i}.json","w"),ensure_ascii=False,indent=1)
