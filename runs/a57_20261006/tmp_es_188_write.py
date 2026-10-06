import json
def g(t,acc=None): return {"text":t,"gap":True,"accept":acc or [t]}
def p(t): return {"text":t}
V={}
V[188]=dict(level="B",keyWord="la constitución",
 taps=[("inclinarse sobre la mesa","el político","male"),("llevar una peluca empolvada","el juez","male"),("llevar dos sellos de lacre","el libro","male")],
 nouns=[("la peluca","male"),("la constitución","male"),("el mármol","male")],
 question="¿Qué está leyendo el político?",answer="Está leyendo una página de la constitución.",av="male",
 recall=[("taps",[g("inclinarse"),p("sobre la mesa")]),("taps",[p("llevar una"),g("peluca"),p("empolvada")]),("taps",[p("llevar dos"),g("sellos"),p("de lacre")]),
  ("answer",[p("Está leyendo una página de la"),g("constitución")])],
 notes="Phrase 1: in many boxed frames the politician is shown in a close-up (sitting, hand on chin, or listening); he leans across the table only in the late frames - phrase written for that. 'el juez' for the wigged official (English 'the judge', male voice). Answer without subject pronoun, as natives say it.")
V[189]=dict(level="B",keyWord="el convoy",
 taps=[("encabezar el convoy","el coche gris","male"),("aparcar entre dos vehículos","el coche negro","male"),("cerrar la marcha","el coche blanco","male")],
 nouns=[("el convoy","male"),("los árboles","male"),("el asfalto","male"),("el cielo","male")],
 question="¿Qué hacen los tres coches?",answer="Circulan en convoy.",av="male",
 recall=[("taps",[g("encabezar",["encabezar","liderar"]),p("el convoy")]),("taps",[p("aparcar entre dos"),g("vehículos",["vehículos","coches"])]),("taps",[g("cerrar"),p("la marcha")]),
  ("answer",[p("Circulan en"),g("convoy")])],
 notes="Phrase 2: the black car's box also covers the driving shots (it drives in the middle) and close-ups of its grille, wheel and spoiler; it is parked between the grey and the white car under the bridge. Question in simple present ('¿Qué hacen...?'), the natural Spanish form for an ongoing action; answer without subject. 'Van en convoy' would be equally natural.")
V[190]=dict(level="A",keyWord="la galleta",
 taps=[("comer una galleta grande","la chica","female"),("tener una cuchara en la mano","el chico","male"),("estar tumbado junto a la ventana","el gato","female")],
 nouns=[("la ventana","female"),("el gato","female"),("las galletas","female"),("la mesa","female")],
 question="¿Qué está comiendo la chica?",answer="Está comiendo una galleta grande.",av="female",
 recall=[("taps",[g("comer"),p("una galleta grande")]),("taps",[p("tener una"),g("cuchara"),p("en la mano")]),("taps",[p("estar"),g("tumbado",["tumbado","echado"]),p("junto a la ventana")]),
  ("answer",[p("Está comiendo una"),g("galleta"),p("grande")])],
 notes="'la chica' / 'el chico' for the young woman and man (everyday Spain usage). Phrase 1: the woman's box also covers her taking the tray out and dunking the cookie; she eats it in the later frames. Phrase 2: the man holds the spoon in the late frames only.")
V[191]=dict(level="B",keyWord="el sacacorchos",
 taps=[("olfatear el corcho","el hombre","male"),("enroscarse en el corcho","el sacacorchos","male"),("llevar una camisa de manga larga","la mujer","female")],
 nouns=[("el sacacorchos","male"),("el corcho","male"),("la botella","male"),("la olla","male")],
 question="¿Cómo abre el hombre la botella?",answer="Abre la botella con un sacacorchos.",av="male",
 recall=[("taps",[g("olfatear",["olfatear","oler"]),p("el corcho")]),("taps",[p("enroscarse en el"),g("corcho")]),("taps",[p("llevar una camisa de"),g("manga"),p("larga")]),
  ("answer",[p("Abre la botella con un"),g("sacacorchos")])],
 notes="Phrase 1: the man's box also covers his hands working the corkscrew, pouring and drinking; he sniffs the cork in the middle frames (the only one who does). Phrase 2: in the last frames the corkscrew lies on the counter; it screws into the cork in most boxed frames. The man wears short sleeves, so phrase 3 fits only the woman.")
V[192]=dict(level="A",keyWord="la esquina",
 taps=[("encajar en la esquina","la tabla","female"),("llevar ropa naranja","la chica","female"),("llevar gafas","el chico","male")],
 nouns=[("el cielo","female"),("la esquina","female"),("la chica","female"),("el chico","male")],
 question="¿Dónde están poniendo la tabla?",answer="Están poniendo la tabla en la esquina.",av="female",
 recall=[("taps",[g("encajar",["encajar","caber"]),p("en la esquina")]),("taps",[p("llevar"),g("ropa"),p("naranja")]),("taps",[p("llevar"),g("gafas")]),
  ("answer",[p("Están poniendo la tabla en la"),g("esquina")])],
 notes="'encajar' is the plain right verb for the perfect fit (B1-ish; A2 alternative 'caber' accepted in recall). The corner shown is an outer corner (pillar edge, building edge), so 'la esquina' (not 'el rincón') fits the clip. 'la tabla' = the triangular wooden boards (two halves forming one triangle). Answer repeats 'la tabla' instead of the clitic so the chip order is unique.")
for i,v in V.items():
    out={"mediaId":i,"lang":"es","level":v["level"],"keyWord":v["keyWord"],
     "taps":[{"phrase":a,"target":b,"voice":c} for a,b,c in v["taps"]],
     "nouns":[{"word":a,"voice":b} for a,b in v["nouns"]],
     "question":v["question"],"answer":v["answer"].split(" "),"answerVoice":v["av"],"carousel":[],
     "recall":[{"from":f,"parts":ps} for f,ps in v["recall"]],"notes":v["notes"]}
    json.dump(out,open(f"content/es/{i}.json","w"),ensure_ascii=False,indent=1)
