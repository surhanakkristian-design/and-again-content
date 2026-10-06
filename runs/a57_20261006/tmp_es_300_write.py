import json
def P(*parts):
    out=[]
    for p in parts:
        if isinstance(p,tuple): out.append({"text":p[0],"gap":True,"accept":list(p[1])})
        else: out.append({"text":p})
    return out
def taps(*t): return [{"phrase":a,"target":b,"voice":c} for a,b,c in t]
def nouns(*n): return [{"word":a,"voice":b} for a,b in n]
D={}
D[300]=dict(level="A",keyWord="la bandera",
 taps=taps(("tirar de la cuerda","la niña","female"),("ondear al viento","la bandera","female"),("mirar la bandera","la niña","female")),
 nouns=nouns(("la bandera","female"),("el cielo","female"),("las montañas","female"),("la niña","female")),
 question="¿Qué está mirando la niña?",answer=["Está","mirando","la","bandera."],answerVoice="female",
 recall=[{"from":"taps","parts":P("tirar de la",("cuerda",["cuerda"]))},
  {"from":"taps","parts":P(("ondear",["ondear"]),"al viento")},
  {"from":"taps","parts":P("mirar la",("bandera",["bandera"]))},
  {"from":"answer","parts":P("Está",("mirando",["mirando"]),"la bandera")}],
 notes="Phrase 1 box also covers moments where the girl ties the rope, salutes or stands with hands on hips; written for the pulling in most boxed frames. Phrase 2 box includes the first frames where the flag is still folded on the pole. 'la niña' chosen because the Pixar character looks like a child.")
D[301]=dict(level="A",keyWord="flotar",
 taps=taps(("flotar en el lago","el hombre","male"),("levantar el pulgar","el hombre","male"),("posarse sobre el hombre","el pájaro","male")),
 nouns=nouns(("el pájaro","male"),("el hombre","male"),("el lago","male")),
 question="¿Qué está haciendo el hombre?",answer=["Está","flotando","en","el","lago."],answerVoice="male",
 recall=[{"from":"taps","parts":P(("flotar",["flotar"]),"en el lago")},
  {"from":"taps","parts":P("levantar el",("pulgar",["pulgar"]))},
  {"from":"taps","parts":P(("posarse",["posarse"]),"sobre el hombre")},
  {"from":"answer","parts":P("Está flotando en el",("lago",["lago"]))}],
 notes="Phrase 2 box covers the whole clip but the thumbs up only appears at the end. Phrase 3: 'posarse' (B1-ish) is the plain right verb for a bird landing/sitting on something; the bird also flies in some boxed frames.")
D[302]=dict(level="A",keyWord="la harina",
 taps=taps(("estar tumbado en el suelo","el perro","male"),("tocarle la nariz a la mujer","el hombre","male"),("llevar un pañuelo gris","la mujer","female")),
 nouns=nouns(("la harina","male"),("los huevos","male"),("el perro","male")),
 question="¿Qué tiene el hombre en la cara?",answer=["Tiene","harina","en","la","cara."],answerVoice="male",
 recall=[{"from":"taps","parts":P("estar",("tumbado",["tumbado","echado"]),"en el suelo")},
  {"from":"taps","parts":P("tocarle la",("nariz",["nariz"]),"a la mujer")},
  {"from":"taps","parts":P("llevar un",("pañuelo",["pañuelo"]),"gris")},
  {"from":"answer","parts":P("Tiene",("harina",["harina"]),"en la cara")}],
 notes="Phrase 2: most boxed frames show the man's floury face; he touches the woman's nose only near the end. The woman's grey 'scarf' is a headscarf, so 'pañuelo'. Answer drops the subject; recall answer row = whole sentence.")
D[303]=dict(level="A",keyWord="la flor",
 taps=taps(("sostener un ramo de flores","la mujer","female"),("estar sentada junto a la ventana","la mujer","female"),("tocar una flor rosa","la mujer","female")),
 nouns=nouns(("la ventana","female"),("las flores","female"),("la mujer","female")),
 question="¿Qué tiene la mujer en las manos?",answer=["Tiene","un","ramo","de","flores."],answerVoice="female",
 recall=[{"from":"taps","parts":P("sostener un",("ramo",["ramo"]),"de flores")},
  {"from":"taps","parts":P("estar sentada junto a la",("ventana",["ventana"]))},
  {"from":"taps","parts":P("tocar una",("flor",["flor"]),"rosa")},
  {"from":"answer","parts":P("Tiene un ramo de",("flores",["flores"]))}],
 notes="All three boxes cover the whole clip for one target (the woman); close-ups of the single pink flower / hand do not show her sitting by the window. 'ramo' used for the bouquet in phrase 1 and answer.")
D[305]=dict(level="A",keyWord="la mosca",
 taps=taps(("posarse en el pan","la mosca","male"),("volar sobre la mesa","la mosca","male"),("agitar una servilleta","la mano","male")),
 nouns=nouns(("la mosca","male"),("el tarro","male"),("el té","male"),("el pan","male")),
 question="¿Qué está haciendo la mosca?",answer=["Está","posada","en","el","pan."],answerVoice="male",
 recall=[{"from":"taps","parts":P(("posarse",["posarse"]),"en el pan")},
  {"from":"taps","parts":P("volar sobre la",("mesa",["mesa"]))},
  {"from":"taps","parts":P("agitar una",("servilleta",["servilleta"]))},
  {"from":"nouns","parts":P("la",("mosca",["mosca"]))},
  {"from":"answer","parts":P("Está posada en el",("pan",["pan"]))}],
 notes="'posarse'/'posada' (B1-ish) is the plain right verb for a fly landing/sitting; no A2 alternative is natural. Phrases 1 and 2 share the same box (the fly lands on the tea glass, bread and jar and flies between them).")
for i,d in D.items():
    o={"mediaId":i,"lang":"es","level":d["level"],"keyWord":d["keyWord"],"taps":d["taps"],"nouns":d["nouns"],
       "question":d["question"],"answer":d["answer"],"answerVoice":d["answerVoice"],"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(o,open(f"content/es/{i}.json","w"),ensure_ascii=False,indent=1)
