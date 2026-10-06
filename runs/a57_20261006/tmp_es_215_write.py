import json
def P(*a):
    out=[]
    for x in a:
        if isinstance(x,tuple): out.append({"text":x[0],"gap":True,"accept":list(x[1])})
        else: out.append({"text":x})
    return out
D={}
D[215]=dict(level="B",keyWord="la oscuridad",
 taps=[("encender una cerilla","la mujer","female"),("llevar un jersey de rayas","el hombre","male"),("brillar en la oscuridad","el farol","female")],
 nouns=[("el farol","female"),("la cerilla","female"),("la ventana","female"),("la sartén de cobre","female")],
 question="¿Qué está haciendo la mujer?",answer="Está encendiendo un farol en la oscuridad.",av="female",
 recall=[("taps",P(("encender",["encender"]),"una cerilla")),("taps",P("llevar un",("jersey",["jersey"]),"de rayas")),
  ("taps",P("brillar en la",("oscuridad",["oscuridad"]))),("answer",P("Está encendiendo un",("farol",["farol"]),"en la oscuridad"))],
 notes="Phrase 1 box also covers early frames (plates, blackout) where no match is struck; phrase written for the match-striking frames. Answer drops the subject (natural in Spain), so the answer recall row is the whole sentence.")
D[217]=dict(level="B",keyWord="el dardo",
 taps=[("apuntar a la diana","la chica","female"),("picar patatas fritas","el chico de las patatas","male"),("clavarse cerca del centro","el dardo","female")],
 nouns=[("el dardo","female"),("la diana","female"),("la pared de madera","female")],
 question="¿Qué está haciendo la chica?",answer="Está lanzando un dardo a la diana.",av="female",
 recall=[("taps",P(("apuntar",["apuntar"]),"a la diana")),("taps",P("picar",("patatas",["patatas"]),"fritas")),
  ("taps",P("clavarse cerca del",("centro",["centro"]))),("answer",P("Está lanzando un",("dardo",["dardo"]),"a la diana"))],
 notes="'la chica' used for the young woman (English 'the woman'). Answer uses 'lanzar' (she throws the dart in the clip) instead of 'apuntar con un dardo a la diana', which allows two orders of the complements. No noun row: the answer row already contains the key word dardo.")
D[218]=dict(level="B",keyWord="declarar",
 taps=[("sostener en alto un pergamino","la mujer del balcón","female"),("tirar de la cuerda","el campanero","male"),("rodear a un niño con el brazo","la mujer del pañuelo","female")],
 nouns=[("la campana","female"),("el pergamino","female"),("las palomas","female"),("el pañuelo","female")],
 question="¿Qué está pasando en el balcón?",answer="Una mujer está anunciando algo a la multitud.",av="female",
 recall=[("taps",P("sostener en alto un",("pergamino",["pergamino"]))),("taps",P(("tirar",["tirar"]),"de la cuerda")),
  ("taps",P(("rodear",["rodear","abrazar"]),"a un niño con el brazo")),("answer",P("está anunciando algo a la",("multitud",["multitud","gente"])))],
 notes="Key word 'declarar' kept, but 'declarar algo a la multitud' is not natural Spanish for a public announcement (declarar = testify / declare war / 'declarar abierto'); the answer uses 'anunciar'. Proposal: key word 'proclamar' or 'anunciar' for this sense. Phrase 3 box (blue) also covers crowd frames before the hug; written for the hug frames.")
D[219]=dict(level="A",keyWord="el ciervo",
 taps=[("mirar a la cámara","el ciervo","male"),("abrir la boca","el ciervo","male"),("salir corriendo","el ciervo","male")],
 nouns=[("el ciervo","male"),("los árboles","male"),("las plantas","male")],
 question="¿Qué hace el ciervo?",answer="El ciervo sale corriendo.",av="male",
 recall=[("taps",P("mirar a la",("cámara",["cámara"]))),("taps",P("abrir la",("boca",["boca"]))),("taps",P(("salir",["salir"]),"corriendo")),
  ("nouns",P("el",("ciervo",["ciervo"]))),("answer",P("sale",("corriendo",["corriendo"])))],
 notes="All three tap boxes are on the same deer and cover most frames; each phrase is written for the frames where that action happens (bellow ~mid clip, running at the end). 'las plantas' kept at level A (helechos would be above A).")
D[220]=dict(level="B",keyWord="descongelar",
 taps=[("descongelar un pescado","el hombre","male"),("estampar un pescado contra la encimera","el hombre","male"),("estar en remojo en un bol","el pescado","male")],
 nouns=[("el filete","male"),("el grifo","male"),("el bol","male"),("el armario","male")],
 question="¿Qué está haciendo el hombre?",answer="Está descongelando un pescado.",av="male",
 recall=[("taps",P(("descongelar",["descongelar"]),"un pescado")),("taps",P("estampar un pescado contra la",("encimera",["encimera"]))),
  ("taps",P("estar en",("remojo",["remojo"]),"en un bol")),("answer",P("Está descongelando un",("pescado",["pescado"])))],
 notes="Phrases 1 and 2 share the target (the man), as in English. Phrase 3 box also covers frames where the fish is in his hand or under the tap; written for the soaking frames.")
for i,d in D.items():
    o={"mediaId":i,"lang":"es","level":d["level"],"keyWord":d["keyWord"],
       "taps":[{"phrase":a,"target":b,"voice":c} for a,b,c in d["taps"]],
       "nouns":[{"word":a,"voice":b} for a,b in d["nouns"]],
       "question":d["question"],"answer":d["answer"].split(),"answerVoice":d["av"],"carousel":[],
       "recall":[{"from":f,"parts":p} for f,p in d["recall"]],"notes":d["notes"]}
    json.dump(o,open(f"content/es/{i}.json","w"),ensure_ascii=False,indent=1)
