import json
def P(t,gap=False,acc=None):
    d={"text":t}
    if gap: d["gap"]=True; d["accept"]=acc or [t]
    return d
def T(ph,tg,v): return {"phrase":ph,"target":tg,"voice":v}
def N(w,v): return {"word":w,"voice":v}
D={}
D[419]=dict(level="A",keyWord="chutar",
 taps=[T("llevar una camiseta naranja","la mujer","female"),T("llevar una camiseta morada","el hombre","male"),T("volar por el aire","la pelota","male")],
 nouns=[N("el cielo","male"),N("los edificios","male"),N("la mujer","female"),N("la pelota","male")],
 question="¿Qué están haciendo?",answer="Están chutando la pelota.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":[P("llevar una"),P("camiseta",True),P("naranja")]},
         {"from":"taps","parts":[P("llevar una camiseta"),P("morada",True,["morada","lila"])]},
         {"from":"taps","parts":[P("volar",True),P("por el aire")]},
         {"from":"answer","parts":[P("Están"),P("chutando",True,["chutando"]),P("la pelota")]}],
 notes="Key word 'chutar': in Spain it is mostly 'to shoot/kick hard at goal'; for the playful keep-ups 'dar patadas/dar toques al balón' is the everyday phrase. Kept 'chutar' in the answer (natural enough for kicking a ball to each other); proposal: 'dar una patada' as the concept word. Ball looks like a volleyball, so 'la pelota' (not 'el balón')."
)
D[383]=dict(level="A",keyWord="el senderismo",
 taps=[T("llevar una mochila azul","la mujer","female"),T("llevar gafas de sol","el hombre","male"),T("volar sobre las montañas","los pájaros","male")],
 nouns=[N("el cielo","male"),N("las montañas","male"),N("la mujer","female"),N("la hierba","male")],
 question="¿Qué están haciendo las dos personas?",answer="Están haciendo senderismo en las montañas.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":[P("llevar una"),P("mochila",True),P("azul")]},
         {"from":"taps","parts":[P("llevar"),P("gafas",True),P("de sol")]},
         {"from":"taps","parts":[P("volar",True),P("sobre las montañas")]},
         {"from":"answer","parts":[P("Están haciendo"),P("senderismo",True),P("en las montañas")]}],
 notes="Phrase 2: English 'to drink from a bottle' happens only in the last summit frames; in most boxed frames the man walks with his sunglasses and hat on, so 'llevar gafas de sol' (the woman wears none). Answer subject is dropped (Spanish), so the answer row is the whole sentence without the full stop."
)
D[13]=dict(level="A",keyWord="la servilleta",
 taps=[T("doblar una servilleta","la mujer","female"),T("limpiarse la boca","la mujer","female"),T("sentarse en una silla","la mujer","female")],
 nouns=[N("la mujer","female"),N("la servilleta","female"),N("la silla","female"),N("la mesa","female")],
 question="¿Qué está haciendo la mujer?",answer="Está doblando una servilleta.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":[P("doblar una"),P("servilleta",True)]},
         {"from":"taps","parts":[P("limpiarse",True),P("la boca")]},
         {"from":"taps","parts":[P("sentarse en una"),P("silla",True)]},
         {"from":"answer","parts":[P("Está"),P("doblando",True),P("una servilleta")]}],
 notes="All three English tap boxes are the same woman over the whole clip; phrases follow the English order (folding, wiping her mouth, sitting at the end)."
)
D[6949]=dict(level="A",keyWord="el chocolate caliente",
 taps=[T("servir chocolate caliente","la mujer","female"),T("llevar un vestido dorado","la mujer","female"),T("beber de una taza","el hombre del gorro","male")],
 nouns=[N("el chocolate caliente","female"),N("el vestido","female"),N("la mano","female")],
 question="¿Qué está haciendo la mujer?",answer="Está sirviendo chocolate caliente en una taza.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":[P("servir"),P("chocolate",True),P("caliente")]},
         {"from":"taps","parts":[P("llevar un"),P("vestido",True),P("dorado")]},
         {"from":"taps","parts":[P("beber",True),P("de una taza")]},
         {"from":"answer","parts":[P("Está"),P("sirviendo",True,["sirviendo","echando"]),P("chocolate caliente en una taza")]}],
 notes="'servir' (not 'verter', which is formal) is how a Spaniard says it at A level. Target 3: the man wears a knitted cap, so 'el hombre del gorro'. The glass cup has a handle, so 'la taza'. Some people in the crowd also hold cups; in the boxed frames only he drinks."
)
D[330]=dict(level="A",keyWord="la puerta",
 taps=[T("correr hacia la puerta de embarque","la chica","female"),T("enseñar su billete","la chica","female"),T("sujetar la puerta","el hombre","male")],
 nouns=[N("la ventana","female"),N("la puerta de embarque","female"),N("la chica","female"),N("la maleta","female")],
 question="¿Adónde corre la chica?",answer="Corre hacia la puerta de embarque.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":[P("correr hacia la"),P("puerta",True),P("de embarque")]},
         {"from":"taps","parts":[P("enseñar su"),P("billete",True,["billete","tarjeta"])]},
         {"from":"taps","parts":[P("sujetar",True,["sujetar","aguantar"]),P("la puerta")]},
         {"from":"answer","parts":[P("Corre",True,["Corre","Va"]),P("hacia la puerta de embarque")]}],
 notes="Key word 'la puerta' alone does not name an airport gate; in Spain it is 'la puerta de embarque' (used for the noun and phrase 1; it contains the key word). Proposal: database word 'la puerta de embarque'. Phrase 3: the man holds the gate door / plane door with his hand in the wide shots; in the counter close-ups he holds the scanner instead. 'enseñar su billete' = the boarding pass (Spain: 'tarjeta de embarque', but 'billete' is the A-level word)."
)
for i,d in D.items():
    out={"mediaId":i,"lang":"es","level":d["level"],"keyWord":d["keyWord"],"taps":d["taps"],"nouns":d["nouns"],
         "question":d["question"],"answer":d["answer"],"answerVoice":d["answerVoice"],"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(out,open(f"content/es/{i}.json","w"),ensure_ascii=False,indent=1)
