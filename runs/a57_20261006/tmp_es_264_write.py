import json
def P(t,gap=False,acc=None):
    d={"text":t}
    if gap: d["gap"]=True; d["accept"]=acc or [t]
    return d
def ch(s): return s.split()
V={}
V[264]=dict(level="B",keyWord="la emoción",
 taps=[("apretar un ramo contra el pecho","la mujer","female"),("apoyarse en la barandilla","la mujer","female"),("empujar un carrito de equipaje","el hombre","male")],
 nouns=[("el ramo","female"),("la rebeca","female"),("la barandilla","female"),("los vaqueros","female")],
 question="¿Qué está sujetando la mujer?",answer="Aprieta un ramo de flores amarillas contra el pecho.",answerVoice="female",
 recall=[("taps",[P("apretar",True,["apretar","estrechar"]),P("un ramo contra el pecho")]),
         ("taps",[P("apoyarse en la"),P("barandilla",True)]),
         ("taps",[P("empujar un"),P("carrito",True,["carrito","carro"]),P("de equipaje")]),
         ("answer",[P("Aprieta un"),P("ramo",True),P("de flores amarillas contra el pecho")])],
 notes="Key word 'la emoción' is not a visible thing, so it appears in no exercise. Answer: 'contra el pecho' could also stand right after 'Aprieta' (marked but possible order). 'la rebeca' = Spain word for cardigan. Phrase 1 kept for the boxed frames where she holds the bouquet to her chest; in the hug frames she still holds it.")
V[265]=dict(level="A",keyWord="el empleado",
 taps=[("recibir un sobre","el chico de gafas","male"),("ponerse una chaqueta","el chico de gafas","male"),("tocarle el hombro","la mujer","female")],
 nouns=[("el empleado","male"),("los papeles","male"),("el teclado","male"),("la ventana","male")],
 question="¿Qué recibe el empleado?",answer="Recibe un sobre.",answerVoice="male",
 recall=[("taps",[P("recibir un"),P("sobre",True)]),
         ("taps",[P("ponerse una"),P("chaqueta",True)]),
         ("taps",[P("tocarle",True,["tocarle"]),P("el hombro")]),
         ("nouns",[P("el"),P("empleado",True)]),
         ("answer",[P("Recibe",True,["Recibe"]),P("un sobre")])],
 notes="English 'paper' = stacks of sheets: 'los papeles' is the natural Spanish word for them. Subject dropped in the answer, so the answer row is the whole sentence.")
V[266]=dict(level="A",keyWord="la energía",
 taps=[("subir las escaleras corriendo","la mujer de blanco","female"),("dar saltos","la mujer de blanco","female"),("apoyar las manos en las rodillas","el hombre","male")],
 nouns=[("las escaleras","female"),("la farola","female"),("el muro","female"),("el cielo","female")],
 question="¿Qué hace la mujer de blanco?",answer="Sube las escaleras corriendo.",answerVoice="female",
 recall=[("taps",[P("subir las"),P("escaleras",True,["escaleras","escalones"]),P("corriendo")]),
         ("taps",[P("dar"),P("saltos",True,["saltos","brincos"])]),
         ("taps",[P("apoyar las manos en las"),P("rodillas",True)]),
         ("answer",[P("Sube",True,["Sube"]),P("las escaleras corriendo")])],
 notes="Key word 'la energía' is not a visible thing, so it appears in no exercise. Answer chips also allow 'Sube corriendo las escaleras' (equally natural); both orders are right. English 'steps' -> 'las escaleras' (everyday word for an outdoor flight of steps), used in phrase, noun and answer.")
V[267]=dict(level="A",keyWord="el ingeniero",
 taps=[("montar un robot","el chico de negro","male"),("coger un cubo blanco","el robot","male"),("aplaudir con alegría","el hombre de la bata blanca","male")],
 nouns=[("el ingeniero","male"),("el robot","male"),("el portátil","male"),("la caja","male")],
 question="¿Qué hace el ingeniero?",answer="Está montando un robot.",answerVoice="male",
 recall=[("taps",[P("montar un"),P("robot",True)]),
         ("taps",[P("coger un"),P("cubo",True),P("blanco")]),
         ("taps",[P("aplaudir",True,["aplaudir"]),P("con alegría")]),
         ("nouns",[P("el"),P("ingeniero",True)]),
         ("answer",[P("Está"),P("montando",True,["montando","construyendo"]),P("un robot")])],
 notes="English 'a box' is a clear plastic tray; 'la caja' kept at level A ('la bandeja' would be more exact, B1). 'montar' = assemble, the action shown; English phrase-1 box also covers frames where he types on the laptop. 'cubo blanco' so it is not read as a bucket.")
V[268]=dict(level="A",keyWord="el sobre",
 taps=[("besar el sobre","la mujer de rojo","female"),("sujetar una vela","la mujer de rojo","female"),("dormir detrás de la lámpara","el gato","female")],
 nouns=[("la lámpara","female"),("el gato","female"),("la vela","female"),("el sobre","female")],
 question="¿Qué besa la mujer de rojo?",answer="Besa el sobre.",answerVoice="female",
 recall=[("taps",[P("besar el"),P("sobre",True)]),
         ("taps",[P("sujetar una"),P("vela",True)]),
         ("taps",[P("dormir",True,["dormir"]),P("detrás de la lámpara")]),
         ("answer",[P("Besa",True,["Besa"]),P("el sobre")])],
 notes="English phrase-1 box also covers frames of folding the letter and sealing; phrase written for the kiss as in English. Key word noun 'el sobre' already in tap row 1, so no noun row.")
for i,v in V.items():
    d={"mediaId":i,"lang":"es","level":v["level"],"keyWord":v["keyWord"],
       "taps":[{"phrase":a,"target":b,"voice":c} for a,b,c in v["taps"]],
       "nouns":[{"word":a,"voice":b} for a,b in v["nouns"]],
       "question":v["question"],"answer":ch(v["answer"]),"answerVoice":v["answerVoice"],"carousel":[],
       "recall":[{"from":f,"parts":p} for f,p in v["recall"]],"notes":v["notes"]}
    json.dump(d,open(f"content/es/{i}.json","w"),ensure_ascii=False,indent=1)
