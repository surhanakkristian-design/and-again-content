import json
def P(*a):
    out=[]
    for x in a:
        if isinstance(x,tuple): out.append({"text":x[0],"gap":True,"accept":list(x[1])})
        else: out.append({"text":x})
    return out
def tap(p,t,v): return {"phrase":p,"target":t,"voice":v}
def n(w,v): return {"word":w,"voice":v}
D={}
D[203]=dict(level="B",keyWord="el crucero",
 taps=[tap("lucir un vestido amarillo de verano","la mujer","female"),tap("llevar una camisa estampada","el hombre","male"),tap("brincar entre las olas","los delfines","male")],
 nouns=[n("el crucero","male"),n("los delfines","male"),n("las islas","male"),n("el mar","male")],
 question="¿Qué está haciendo el crucero?",answer="El crucero navega junto a islas tropicales.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":P(("lucir",["lucir","llevar"]),"un vestido amarillo de verano")},
  {"from":"taps","parts":P("llevar una",("camisa",["camisa"]),"estampada")},
  {"from":"taps","parts":P("brincar entre las",("olas",["olas"]))},
  {"from":"nouns","parts":P("el",("crucero",["crucero"]))},
  {"from":"answer","parts":P(("navega",["navega","pasa"]),"junto a islas tropicales")}],
 notes="Noun 1 'a cruise ship' = el crucero (key word; in Spain 'crucero' names the ship itself). Phrase 3: the dolphins leap in and out of the waves; 'brincar' as the B1 verb.")
D[204]=dict(level="B",keyWord="la muleta",
 taps=[tap("caminar con muletas","el chico","male"),tap("sostener una carpeta","la enfermera","female"),tap("alzar el puño cerrado","el chico","male")],
 nouns=[n("la enfermera","female"),n("la muleta","male"),n("la bota ortopédica","male"),n("el picaporte","male")],
 question="¿Qué está haciendo el chico?",answer="El chico camina apoyado en dos muletas.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":P("caminar con",("muletas",["muletas"]))},
  {"from":"taps","parts":P(("sostener",["sostener","sujetar"]),"una carpeta")},
  {"from":"taps","parts":P("alzar el",("puño",["puño"]),"cerrado")},
  {"from":"answer","parts":P(("camina",["camina","anda"]),"apoyado en dos muletas")}],
 notes="Clipboard = 'la carpeta' (carpeta con pinza); the nurse is only partly visible at the left edge in the boxed frames. Door handle = 'el picaporte' (Spain; 'la manilla' also used).")
D[205]=dict(level="A",keyWord="el llanto",
 taps=[tap("secarse los ojos","la mujer","female"),tap("abrazar a la mujer","el hombre","male"),tap("coger un pañuelo","la mujer","female")],
 nouns=[n("la mujer","female"),n("el hombre","male"),n("la manta","female"),n("los pañuelos","female")],
 question="¿Qué está haciendo la mujer?",answer="La mujer llora y se seca los ojos.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":P("secarse los",("ojos",["ojos"]))},
  {"from":"taps","parts":P(("abrazar",["abrazar"]),"a la mujer")},
  {"from":"taps","parts":P("coger un",("pañuelo",["pañuelo","clínex"]))},
  {"from":"answer","parts":P(("llora",["llora"]),"y se seca los ojos")}],
 notes="Key word 'el llanto' is B1 and rather formal for a level A video; it is not used in the texts, the A-level verb 'llorar' carries the meaning in the answer. Proposal: keep the concept but consider 'llorar' as the taught form for level A.")
D[206]=dict(level="A",keyWord="el pepino",
 taps=[tap("cortar un pepino","el hombre","male"),tap("comer un trozo de pepino","la mujer","female"),tap("mirar por encima de la mesa","el perro","male")],
 nouns=[n("la ventana","male"),n("el pepino","male"),n("la camisa","male"),n("el perro","male")],
 question="¿Qué está haciendo el hombre?",answer="El hombre corta un pepino.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":P("cortar un",("pepino",["pepino"]))},
  {"from":"taps","parts":P(("comer",["comer"]),"un trozo de pepino")},
  {"from":"taps","parts":P("mirar por encima de la",("mesa",["mesa"]))},
  {"from":"answer","parts":P(("corta",["corta","pela"]),"un pepino")}],
 notes="Phrase 1 box also covers the man snapping and peeling the cucumber; 'cortar un pepino' fits most boxed frames (snapping in half, slicing). Answer row accepts 'pela' as he peels it too.")
D[207]=dict(level="A",keyWord="la taza",
 taps=[tap("llevar un pendiente verde","la mujer","female"),tap("llevar gafas","el hombre","male"),tap("llevar una camisa azul","el hombre","male")],
 nouns=[n("el gato","female"),n("la taza","female"),n("las flores","female"),n("la tetera","female")],
 question="¿Qué está haciendo la mujer?",answer="La mujer bebe té de una taza.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":P("llevar un",("pendiente",["pendiente"]),"verde")},
  {"from":"taps","parts":P("llevar",("gafas",["gafas"]))},
  {"from":"taps","parts":P("llevar una",("camisa",["camisa"]),"azul")},
  {"from":"answer","parts":P("bebe té de una",("taza",["taza"]))}],
 notes="Phrases 2 and 3 both describe the man, as in English. The answer row gaps the key word 'taza'.")
for i,d in D.items():
    o={"mediaId":i,"lang":"es","level":d["level"],"keyWord":d["keyWord"],"taps":d["taps"],"nouns":d["nouns"],"question":d["question"],
       "answer":d["answer"],"answerVoice":d["answerVoice"],"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(o,open(f"content/es/{i}.json","w"),ensure_ascii=False,indent=1)
