import json
def R(frm,*parts):
    out=[]
    for p in parts:
        if isinstance(p,tuple): out.append({"text":p[0],"gap":True,"accept":list(p)})
        else: out.append({"text":p})
    return {"from":frm,"parts":out}
def T(p,t,v): return {"phrase":p,"target":t,"voice":v}
def N(w,v): return {"word":w,"voice":v}
D={}
D[275]=dict(level="A",keyWord="discutir",
 taps=[T("señalar con el dedo","la mujer","female"),T("mirar hacia arriba y pensar","el hombre","male"),T("sonreír al hombre","la mujer","female")],
 nouns=[N("las cortinas","male"),N("el sofá","male"),N("la mesa","male"),N("el hombre","male")],
 question="¿Qué hacen el hombre y la mujer?",answer="El hombre y la mujer discuten en el salón.".split(),answerVoice="male",
 recall=[R("taps","señalar con el",("dedo",)),R("taps","mirar hacia arriba y",("pensar",)),R("taps",("sonreír",),"al hombre"),R("answer",("discuten",),"en el salón")],
 notes="Answer subject 'El hombre y la mujer' is mixed; voice kept male as in English.")
D[276]=dict(level="B",keyWord="la excursión",
 taps=[T("pastar en una ladera","las ovejas","female"),T("precipitarse por un acantilado","la cascada","female"),T("estar apoyado en una roca","el móvil","female")],
 nouns=[N("la cascada","female"),N("el arcoíris","female"),N("el móvil","female"),N("la roca","female")],
 question="¿Qué están haciendo los amigos?",answer="Los amigos están posando delante de una cascada.".split(),answerVoice="female",
 recall=[R("taps","pastar en una",("ladera",)),R("taps","precipitarse por un",("acantilado",)),R("taps","estar",("apoyado","colocado"),"en una roca"),R("answer","están",("posando",),"delante de una cascada")],
 notes="Key word 'la excursión' is not a noun pill (as in English), so no noun recall row. 'la roca' used for boulder (everyday Spain word; 'peñasco' is rare). Tap 1/2 boxes are OFF in many frames (sheep and waterfall only visible part of the clip).")
D[279]=dict(level="B",keyWord="ejercer fuerza",
 taps=[T("ejercer mucha fuerza","el hombre","male"),T("alzar el puño","el hombre","male"),T("rodar por un charco","el carro","male")],
 nouns=[N("los sacos","male"),N("la rueda","male"),N("el charco","male")],
 question="¿Qué hace el hombre?",answer="El hombre empuja el carro con todas sus fuerzas.".split(),answerVoice="male",
 recall=[R("taps","ejercer mucha",("fuerza",)),R("taps","alzar el",("puño",)),R("taps","rodar por un",("charco",)),R("answer",("empuja",),"el carro con todas sus fuerzas")],
 notes="Phrase 2: the man raises his clenched fist ('alzar el puño', visible) rather than only clenching it. Model answer uses 'empujar el carro con todas sus fuerzas' (natural B1 collocation); the key word is in phrase 1.")
D[280]=dict(level="A",keyWord="el gatito",
 taps=[T("mirar a la cámara","el gatito","female"),T("estar sentado en una cama","el gatito","female"),T("acercarse mucho a la cámara","el gatito","female")],
 nouns=[N("el gatito","female"),N("la cama","female"),N("el móvil","female")],
 question="¿Qué hace el gatito?",answer="El gatito mira a la cámara.".split(),answerVoice="female",
 recall=[R("taps",("mirar",),"a la cámara"),R("taps","estar sentado en una",("cama",)),R("taps",("acercarse",),"mucho a la cámara"),R("nouns","el",("gatito",)),R("answer","mira a la",("cámara",))],
 notes="All three taps target the kitten (the only one in the clip), as in English.")
D[281]=dict(level="B",keyWord="el delineador de ojos",
 taps=[T("aplicarse el delineador de ojos","la mujer morena","female"),T("sujetar un bastoncillo","la mujer morena","female"),T("levantar el pulgar en señal de aprobación","la amiga rubia","female")],
 nouns=[N("las bombillas","female"),N("el espejo","female"),N("el delineador de ojos","female"),N("el bastoncillo","female")],
 question="¿Qué está haciendo la mujer morena?",answer="La mujer morena se pinta la raya del ojo.".split(),answerVoice="female",
 recall=[R("taps","aplicarse el",("delineador",),"de ojos"),R("taps",("sujetar","sostener"),"un bastoncillo"),R("taps","levantar el",("pulgar",),"en señal de aprobación"),R("answer","se pinta la",("raya",),"del ojo")],
 notes="'Pintarse la raya del ojo' is the everyday Spain expression for applying eyeliner; 'con rabillo' (winged) left out to keep the phrase natural. Tap 1 box also covers later frames where she wipes with the swab; phrase written for most boxed frames. 'el bastoncillo' = cotton swab (Spain).")
for i,d in D.items():
    o={"mediaId":i,"lang":"es","level":d["level"],"keyWord":d["keyWord"],"taps":d["taps"],"nouns":d["nouns"],"question":d["question"],
       "answer":d["answer"],"answerVoice":d["answerVoice"],"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(o,open(f"content/es/{i}.json","w"),ensure_ascii=False,indent=1)
