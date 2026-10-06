import json
def P(text, gap=None, acc=None):
    # split text into parts around gap word
    w = text.split(' ')
    i = w.index(gap)
    parts = []
    if i>0: parts.append({"text":" ".join(w[:i])})
    parts.append({"text":gap,"gap":True,"accept":acc or [gap]})
    if i<len(w)-1: parts.append({"text":" ".join(w[i+1:])})
    return parts
def T(phrase,target,voice): return {"phrase":phrase,"target":target,"voice":voice}
def N(word,voice): return {"word":word,"voice":voice}
D = {}
D[15] = dict(level="A", keyWord="la pastilla",
 taps=[T("beber agua","el hombre","male"),T("echar agua en un vaso","la mujer","female"),T("estar en la mano","la pastilla","male")],
 nouns=[N("la pastilla","male"),N("la mano","male"),N("el árbol","male")],
 question="¿Qué hace el hombre?", answer="Se toma una pastilla con agua.", answerVoice="male",
 recall=[("taps","beber agua","beber",["beber","tomar"]),("taps","echar agua en un vaso","echar",["echar","servir"]),
         ("taps","estar en la mano","mano",["mano"]),("answer","Se toma una pastilla con agua","pastilla",["pastilla"])],
 notes="Phrase 1: the man's box also covers frames where he holds his head or takes the pill; written for the drinking. Phrase 3: the pill lies in the woman's open hand. Answer has no subject (natural Spanish), so the answer row is the whole sentence.")
D[16] = dict(level="B", keyWord="la presentación",
 taps=[T("hacer una presentación en clase","la alumna de rojo","female"),T("proyectar las diapositivas","la pantalla","female"),T("estar sentados entre el público","los compañeros de clase","female")],
 nouns=[N("la presentación","female"),N("el jersey","female"),N("la pizarra blanca","female"),N("el público","female")],
 question="¿Qué está haciendo la alumna de rojo?", answer="Está haciendo una presentación ante sus compañeros.", answerVoice="female",
 recall=[("taps","hacer una presentación en clase","presentación",["presentación","exposición"]),("taps","proyectar las diapositivas","proyectar",["proyectar","mostrar"]),
         ("taps","estar sentados entre el público","público",["público"]),("answer","Está haciendo una presentación ante sus compañeros","compañeros",["compañeros"])],
 notes="'alumna' (school class) rather than 'estudiante'. B1/B2 items: presentación, proyectar, diapositivas, público, ante. Answer has no subject, so the answer row is the whole sentence.")
D[17] = dict(level="A", keyWord="el proyecto",
 taps=[T("llevar una gorra","el hombre de la gorra","male"),T("tener el pelo largo","la mujer","female"),T("tener un tejado de madera","la caseta","male")],
 nouns=[N("el cielo","male"),N("el tejado","male"),N("la puerta","male"),N("la hierba","male")],
 question="¿Qué están construyendo los jóvenes?", answer="Están construyendo una caseta de madera.", answerVoice="male",
 recall=[("taps","llevar una gorra","gorra",["gorra"]),("taps","tener el pelo largo","pelo",["pelo"]),
         ("taps","tener un tejado de madera","tejado",["tejado","techo"]),("answer","Están construyendo una caseta de madera","construyendo",["construyendo","haciendo"])],
 notes="Key word el proyecto is abstract (only in the transcript) and appears in no exercise; kept unchanged. Shed = la caseta (A-level; el cobertizo would be B). Answer has no subject, so the answer row is the whole sentence.")
D[19] = dict(level="A", keyWord="la regla",
 taps=[T("dibujar una línea","el hombre","male"),T("tener las tapas rojas","el libro","male"),T("ser larga y recta","la regla","male")],
 nouns=[N("la regla","male"),N("las gafas","male"),N("el bolígrafo","male"),N("el papel","male")],
 question="¿Qué está haciendo el hombre?", answer="Está dibujando una línea con una regla.", answerVoice="male",
 recall=[("taps","dibujar una línea","dibujar",["dibujar","trazar","hacer"]),("taps","tener las tapas rojas","tapas",["tapas"]),
         ("taps","ser larga y recta","recta",["recta"]),("answer","Está dibujando una línea con una regla","regla",["regla"])],
 notes="Phrase 1 box also covers frames where he searches (under the desk, with the book and calculator); written for the drawing. The book's cover is dark red. Answer has no subject, so the answer row is the whole sentence.")
D[20] = dict(level="B", keyWord="el horario",
 taps=[T("agarrar la almohada","la mano","female"),T("estar abierto por la mitad","el libro de texto","female"),T("tener las dos correas sueltas","la mochila","female")],
 nouns=[N("el libro de texto","female"),N("el portátil","female"),N("la mochila","female"),N("la almohada","female")],
 question="¿Qué está haciendo la mano?", answer="Está agarrando la almohada del suelo.", answerVoice="female",
 recall=[("taps","agarrar la almohada","agarrar",["agarrar","coger"]),("taps","estar abierto por la mitad","abierto",["abierto"]),
         ("taps","tener las dos correas sueltas","correas",["correas","tiras"]),("answer","Está agarrando la almohada del suelo","almohada",["almohada"])],
 notes="Key word el horario is not a visible thing (only implied by the labels Revise/Work/Gym/Sleep) and appears in no exercise; kept unchanged. Phrase 1: the hand hovers over the items in most boxed frames and grabs the pillow at the end; written for the grab. 'abierto de par en par' avoided (used for doors/windows); 'abierto por la mitad' is what natives say of a book. Answer has no subject, so the answer row is the whole sentence.")
for i,d in D.items():
    out = {"mediaId":i,"lang":"es","level":d["level"],"keyWord":d["keyWord"],"taps":d["taps"],"nouns":d["nouns"],
           "question":d["question"],"answer":d["answer"].split(" "),"answerVoice":d["answerVoice"],"carousel":[],
           "recall":[{"from":f,"parts":P(t,g,a)} for f,t,g,a in d["recall"]],"notes":d["notes"]}
    json.dump(out, open(f"content/es/{i}.json","w"), ensure_ascii=False, indent=1)
