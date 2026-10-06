import json
def P(*a):
    out=[]
    for x in a:
        if isinstance(x,tuple): out.append({"text":x[0],"gap":True,"accept":list(x[1])})
        else: out.append({"text":x})
    return out
def T(p,t,v): return {"phrase":p,"target":t,"voice":v}
def N(w,v): return {"word":w,"voice":v}
D={}
D[246]=dict(level="A",keyWord="conducir",
 taps=[T("conducir el coche","la mujer","female"),T("llevar un gorro gris","la mujer","female"),T("sonreír a la conductora","el hombre","male")],
 nouns=[N("el retrovisor","female"),N("el mar","female"),N("la mujer","female"),N("el hombre","male")],
 question="¿Qué está haciendo la mujer?",answer="Está conduciendo un coche junto al mar.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":P(("conducir",["conducir"]),"el coche")},
         {"from":"taps","parts":P("llevar un",("gorro",["gorro"]),"gris")},
         {"from":"taps","parts":P(("sonreír",["sonreír"]),"a la conductora")},
         {"from":"answer","parts":P("Está conduciendo un coche junto al",("mar",["mar"]))}],
 notes="Source keyWord.es is the verb 'conducir' for English noun 'driving'; fits the clip. English 'a grey hat' is a knitted beanie: 'un gorro gris'. Mirror = rear-view mirror: 'el retrovisor'.")
D[248]=dict(level="B",keyWord="el cuentagotas",
 taps=[T("dosificar las gotas","la mujer","female"),T("tragarse la medicina","el hombre","male"),T("desprender vapor","la tetera de cobre","female")],
 nouns=[N("el cuentagotas","female"),N("la cuchara de madera","female"),N("el delantal","female")],
 question="¿Qué está haciendo la mujer?",answer="Está dosificando gotas con un cuentagotas.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":P(("dosificar",["dosificar","medir"]),"las gotas")},
         {"from":"taps","parts":P("tragarse la",("medicina",["medicina","medicamento"]))},
         {"from":"taps","parts":P(("desprender",["desprender","echar","soltar"]),"vapor")},
         {"from":"answer","parts":P("Está dosificando gotas con un",("cuentagotas",["cuentagotas"]))}],
 notes="Phrase 1 box also covers close-ups of the hand squeezing the bulb; 'dosificar las gotas' fits the drop-counting frames. The man drinks the dose from the wooden spoon: 'tragarse la medicina'.")
D[250]=dict(level="A",keyWord="el pato",
 taps=[T("meter la cabeza en el agua","el pato","female"),T("abrir las alas","el pato","female"),T("abrir el pico","el pato","female")],
 nouns=[N("el pato","female"),N("los árboles","female"),N("el agua","female")],
 question="¿Qué está haciendo el pato?",answer="El pato está nadando en el agua.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":P("meter la",("cabeza",["cabeza"]),"en el agua")},
         {"from":"taps","parts":P("abrir las",("alas",["alas"]))},
         {"from":"taps","parts":P("abrir el",("pico",["pico"]))},
         {"from":"nouns","parts":P("el",("pato",["pato"]))},
         {"from":"answer","parts":P("está",("nadando",["nadando"]),"en el agua")}],
 notes="All three English boxes follow the duck through the whole clip (only animal); each phrase is what it does in part of the clip, as in English. 'pico' (beak) for English 'mouth', the natural word for a bird.")
D[251]=dict(level="B",keyWord="la mancuerna",
 taps=[T("entrenar los bíceps","el hombre","male"),T("tomarse el café a sorbos","la mujer","female"),T("estar sentada con las piernas cruzadas","la mujer","female")],
 nouns=[N("la mancuerna","male"),N("la palmera","male"),N("el sillón","male"),N("la ventana","male")],
 question="¿Qué está haciendo el hombre?",answer="Está entrenando los bíceps con una mancuerna.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":P(("entrenar",["entrenar","ejercitar","trabajar"]),"los bíceps")},
         {"from":"taps","parts":P("tomarse el café a",("sorbos",["sorbos","sorbitos"]))},
         {"from":"taps","parts":P("estar sentada con las",("piernas",["piernas"]),"cruzadas")},
         {"from":"answer","parts":P("Está entrenando los bíceps con una",("mancuerna",["mancuerna"]))}],
 notes="'entrenar los bíceps' instead of the gym anglicism 'hacer curl de bíceps'; phrase 1 box also covers picking up the dumbbell and the overhead press (all training). Woman's box includes a few clapping frames; she sips coffee in most.")
D[252]=dict(level="A",keyWord="el polvo",
 taps=[T("soplar sobre una maleta","el hombre","male"),T("levantar un dedo","la mujer","female"),T("estar posado en lo alto","el pájaro","female")],
 nouns=[N("el polvo","female"),N("el hombre","male"),N("la mujer","female"),N("la maleta","female")],
 question="¿Qué está haciendo el hombre?",answer="Está soplando el polvo de una maleta.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":P(("soplar",["soplar"]),"sobre una maleta")},
         {"from":"taps","parts":P("levantar un",("dedo",["dedo"]))},
         {"from":"taps","parts":P("estar",("posado",["posado"]),"en lo alto")},
         {"from":"answer","parts":P("Está soplando el",("polvo",["polvo"]),"de una maleta")}],
 notes="Phrase 1 box also covers frames where the man only holds/lifts the suitcase before and after blowing; written for the blow, as in English. 'posado' (perched) is slightly above A2 but it is the plain right word for a bird; 'sentado' would be wrong for a bird.")
for i,d in D.items():
    o={"mediaId":i,"lang":"es"}; o.update(d); o["carousel"]=[]
    o={k:o[k] for k in ["mediaId","lang","level","keyWord","taps","nouns","question","answer","answerVoice","carousel","recall","notes"]}
    json.dump(o,open(f"content/es/{i}.json","w"),ensure_ascii=False,indent=2)
