import json
def P(*parts):
    out=[]
    for p in parts:
        if isinstance(p,tuple): out.append({"text":p[0],"gap":True,"accept":list(p[1])})
        else: out.append({"text":p})
    return out
def T(ph,tg,v): return {"phrase":ph,"target":tg,"voice":v}
def N(w,v): return {"word":w,"voice":v}
D={}
D[773]=dict(level="B",keyWord="el termómetro",
 taps=[T("tomarle la temperatura","la enfermera","female"),T("ponerse rojo como un tomate","el hombre","male"),T("marcar una temperatura alta","el termómetro","female")],
 nouns=[N("la ventana","female"),N("el termómetro","female"),N("la enfermera","female"),N("el cuenco","female")],
 question="¿Qué está haciendo la enfermera?",answer="Le está tomando la temperatura con un termómetro.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":P("tomarle la",("temperatura",["temperatura"]))},
  {"from":"taps","parts":P("ponerse",("rojo",["rojo"]),"como un tomate")},
  {"from":"taps","parts":P(("marcar",["marcar","indicar"]),"una temperatura alta")},
  {"from":"answer","parts":P("Le está tomando la temperatura con un",("termómetro",["termómetro"]))}],
 notes="Answer drops the subject (la enfermera), as natives do; the answer row is the whole sentence without the full stop. Tap 2 idiom 'ponerse rojo como un tomate' = turn bright red (B1 collocation).")
D[4755]=dict(level="B",keyWord="la fractura",
 taps=[T("señalar la radiografía","la doctora","female"),T("hacer una mueca de dolor","el chico","male"),T("mostrar una fractura","la radiografía","male")],
 nouns=[N("la radiografía","male"),N("la doctora","female"),N("la escayola","male"),N("el cabestrillo","male")],
 question="¿Qué está señalando la doctora?",answer="Está señalando una fractura en la radiografía.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":P(("señalar",["señalar"]),"la radiografía")},
  {"from":"taps","parts":P("hacer una",("mueca",["mueca"]),"de dolor")},
  {"from":"taps","parts":P(("mostrar",["mostrar","revelar","enseñar"]),"una fractura")},
  {"from":"answer","parts":P("Está señalando una",("fractura",["fractura"]),"en la radiografía")}],
 notes="Target of tap 2 is the young man ('el chico'). 'la escayola' = Spain word for a plaster cast. Answer drops the subject (la doctora).")
D[95]=dict(level="B",keyWord="el colorete",
 taps=[T("ponerse colorete en las mejillas","la chica de la trenza","female"),T("asomarse por encima de su hombro","la chica del pelo corto","female"),T("estar posado en la jaula","el periquito","female")],
 nouns=[N("la trenza","female"),N("la brocha","female"),N("el colorete","female")],
 question="¿Qué está haciendo la chica de verde?",answer="Se está poniendo colorete con una brocha.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":P("ponerse",("colorete",["colorete"]),"en las mejillas")},
  {"from":"taps","parts":P(("asomarse",["asomarse","mirar"]),"por encima de su hombro")},
  {"from":"taps","parts":P("estar",("posado",["posado"]),"en la jaula")},
  {"from":"answer","parts":P("Se está poniendo colorete con una",("brocha",["brocha"]))}],
 notes="In a few frames (about 3-4 s) the short-haired girl also brushes her own cheek, so tap 1 is not strictly unique to the braid girl in those frames; the braid girl does it in most boxed frames. The bird is a budgie (el periquito) sitting on top of a cage. Answer drops the subject.")
D[137]=dict(level="B",keyWord="el cañón",
 taps=[T("tocar la pared del cañón","la mujer","female"),T("gritar haciendo bocina con las manos","el hombre","male"),T("asomar entre las rocas","el sol","male")],
 nouns=[N("el cielo","male"),N("el sol","male"),N("el cañón","male"),N("la mujer","female")],
 question="¿Qué está haciendo el hombre?",answer="Está gritando haciendo bocina con las manos.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":P("tocar la pared del",("cañón",["cañón"]))},
  {"from":"taps","parts":P("gritar haciendo",("bocina",["bocina"]),"con las manos")},
  {"from":"taps","parts":P(("asomar",["asomar","brillar"]),"entre las rocas")},
  {"from":"answer","parts":P("Está",("gritando",["gritando"]),"haciendo bocina con las manos")}],
 notes="The woman touches the wall only around 2.5-3 s; in many boxed frames she walks or looks up (the boxed early frames show both walking). 'hacer bocina con las manos' = cup hands around the mouth (B2 collocation). Answer drops the subject.")
D[354]=dict(level="B",keyWord="la guía turística",
 taps=[T("hojear una guía turística","la mujer","female"),T("llevar un salacot","el hombre","male"),T("echar agua por la boca","el león de piedra","female")],
 nouns=[N("la estatua","female"),N("el salacot","female"),N("el pendiente","female"),N("la guía turística","female")],
 question="¿Qué están haciendo los dos turistas?",answer="Están hojeando una guía turística.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":P(("hojear",["hojear"]),"una guía turística")},
  {"from":"taps","parts":P("llevar un",("salacot",["salacot"]))},
  {"from":"taps","parts":P(("echar",["echar","escupir"]),"agua por la boca")},
  {"from":"answer","parts":P("Están hojeando una",("guía",["guía"]),"turística")}],
 notes="The man's hat is a pith helmet: Spanish 'el salacot' is the exact word ('sombrero de sol' is not natural); fallback would be 'el sombrero de explorador'. In the last boxed frames the tourists run off with the book (not flipping). Answer drops the subject.")
for i,d in D.items():
    o={"mediaId":i,"lang":"es","level":d["level"],"keyWord":d["keyWord"],"taps":d["taps"],"nouns":d["nouns"],"question":d["question"],
       "answer":d["answer"],"answerVoice":d["answerVoice"],"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(o,open(f"content/es/{i}.json","w"),ensure_ascii=False,indent=1)
