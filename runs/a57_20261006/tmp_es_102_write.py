import json
def P(*parts):
    out=[]
    for p in parts:
        if isinstance(p,tuple): out.append({"text":p[0],"gap":True,"accept":list(p[1])})
        else: out.append({"text":p})
    return out
def ans(s): return s.split()
D={}
D[102]=dict(mediaId=102,lang="es",level="B",keyWord="el aburrimiento",
 taps=[dict(phrase="repantigarse en una silla de plástico",target="el hombre",voice="male"),
       dict(phrase="colgar de sus dedos",target="el calcetín",voice="male"),
       dict(phrase="dar vueltas sobre la punta del dedo",target="la bolsa de la ropa",voice="male")],
 nouns=[dict(word="el calcetín",voice="male"),dict(word="las lavadoras",voice="male"),dict(word="el chándal",voice="male"),dict(word="la zapatilla",voice="male")],
 question="¿Qué hace el hombre?",answer=ans("Se repantiga en una silla de plástico."),answerVoice="male",carousel=[],
 recall=[dict(**{"from":"taps"},parts=P(("repantigarse",["repantigarse","apoltronarse"]),"en una silla de plástico")),
         dict(**{"from":"taps"},parts=P(("colgar",["colgar"]),"de sus dedos")),
         dict(**{"from":"taps"},parts=P("dar vueltas sobre la",("punta",["punta"]),"del dedo")),
         dict(**{"from":"answer"},parts=P("Se repantiga en una",("silla",["silla"]),"de plástico"))],
 notes="The sock box also covers frames where the sock floats down from the ceiling, lies in the drum and sits on his head; 'colgar de sus dedos' kept for the frames where he holds it up (the feather also floats, so 'flotar' would not be unique). Key word 'el aburrimiento' is not a visible thing, so it appears in no exercise. 'repantigarse' = B2, very common in Spain.")
D[7088]=dict(mediaId=7088,lang="es",level="B",keyWord="nivelar",
 taps=[dict(phrase="arrastrar una regla larga",target="la mujer",voice="female"),
       dict(phrase="sostener una carga pesada en el aire",target="la grúa",voice="female"),
       dict(phrase="trabajar de rodillas en la azotea",target="el obrero arrodillado",voice="female")],
 nouns=[dict(word="la grúa",voice="female"),dict(word="el casco",voice="female"),dict(word="el trípode",voice="female"),dict(word="el hormigón",voice="female")],
 question="¿Qué está haciendo la mujer?",answer=ans("Está nivelando el hormigón fresco."),answerVoice="female",carousel=[],
 recall=[dict(**{"from":"taps"},parts=P("arrastrar una",("regla",["regla"]),"larga")),
         dict(**{"from":"taps"},parts=P(("sostener",["sostener","sujetar"]),"una carga pesada en el aire")),
         dict(**{"from":"taps"},parts=P("trabajar de",("rodillas",["rodillas"]),"en la azotea")),
         dict(**{"from":"answer"},parts=P("Está",("nivelando",["nivelando","alisando"]),"el hormigón fresco"))],
 notes="'regla' is the Spanish building-site word for the straightedge (regla de albañil).")
D[4852]=dict(mediaId=4852,lang="es",level="B",keyWord="el engranaje",
 taps=[dict(phrase="quedarse boquiabierto",target="el chico",voice="male"),
       dict(phrase="iluminarse en rojo y verde",target="la placa de circuito",voice="male"),
       dict(phrase="tener grandes engranajes metálicos",target="la máquina enorme",voice="male")],
 nouns=[dict(word="las gafas de protección",voice="male"),dict(word="las herramientas",voice="male"),dict(word="la placa de circuito",voice="male"),dict(word="el tornillo de banco",voice="male")],
 question="¿Qué está construyendo el chico?",answer=ans("Está construyendo una máquina con engranajes metálicos."),answerVoice="male",carousel=[],
 recall=[dict(**{"from":"taps"},parts=P("quedarse",("boquiabierto",["boquiabierto"]))),
         dict(**{"from":"taps"},parts=P(("iluminarse",["iluminarse","encenderse"]),"en rojo y verde")),
         dict(**{"from":"taps"},parts=P("tener grandes",("engranajes",["engranajes"]),"metálicos")),
         dict(**{"from":"answer"},parts=P("Está",("construyendo",["construyendo","montando"]),"una máquina con engranajes metálicos"))],
 notes="Phrase 1: the man's box covers the whole clip but he raises both arms only in the last frames; in most boxed frames he stares open-mouthed at his work, so 'quedarse boquiabierto' (B2) instead of 'levantar los brazos'. The board lights up red and green only in a few boxed frames (English phrase kept). Target called 'el chico' (young man) consistently.")
D[4441]=dict(mediaId=4441,lang="es",level="B",keyWord="el aliento",
 taps=[dict(phrase="mantener los ojos cerrados",target="la mujer",voice="female"),
       dict(phrase="dominar el paisaje",target="el pico",voice="female"),
       dict(phrase="llevar un gorro blanco",target="la persona del gorro blanco",voice="female")],
 nouns=[dict(word="el cielo",voice="female"),dict(word="el pico",voice="female"),dict(word="el aliento",voice="female"),dict(word="la chaqueta",voice="female")],
 question="¿Qué se puede ver en el aire?",answer=ans("Se puede ver el aliento de la mujer."),answerVoice="female",carousel=[],
 recall=[dict(**{"from":"taps"},parts=P("mantener los ojos",("cerrados",["cerrados"]))),
         dict(**{"from":"taps"},parts=P(("dominar",["dominar"]),"el paisaje")),
         dict(**{"from":"taps"},parts=P("llevar un",("gorro",["gorro"]),"blanco")),
         dict(**{"from":"answer"},parts=P("Se puede ver el",("aliento",["aliento","vaho"]),"de la mujer"))],
 notes="Key word 'el aliento' kept; the visible white cloud of breath is most precisely 'el vaho' in Spain (accepted in the answer row). Impersonal 'se puede ver' has no subject, so the answer row is the whole sentence. 'llevar un gorro blanco' is A2 vocabulary only; no natural B1 word for it.")
D[4721]=dict(mediaId=4721,lang="es",level="B",keyWord="desvanecerse",
 taps=[dict(phrase="señalar el arcoíris por encima del hombro",target="la mujer",voice="female"),
       dict(phrase="desvanecerse en el cielo",target="el arcoíris",voice="female"),
       dict(phrase="contemplar el cielo gris",target="la mujer",voice="female")],
 nouns=[dict(word="el arcoíris",voice="female"),dict(word="el lago",voice="female"),dict(word="el impermeable",voice="female"),dict(word="el charco",voice="female")],
 question="¿Qué le está pasando al arcoíris?",answer=ans("El arcoíris se está desvaneciendo en el cielo."),answerVoice="female",carousel=[],
 recall=[dict(**{"from":"taps"},parts=P("señalar el arcoíris por encima del",("hombro",["hombro"]))),
         dict(**{"from":"taps"},parts=P(("desvanecerse",["desvanecerse","borrarse"]),"en el cielo")),
         dict(**{"from":"taps"},parts=P("contemplar el",("cielo",["cielo"]),"gris")),
         dict(**{"from":"answer"},parts=P("se está",("desvaneciendo",["desvaneciendo","borrando"]),"en el cielo"))],
 notes="Both woman boxes cover the whole clip; she points and grins at the camera only in the first ~4 s, then turns her back and looks at the sky. Phrase 3 rewritten from 'grin at the camera' to what she does in most boxed frames: 'contemplar el cielo gris'. Phrase 1 (pointing) kept from English although it covers only the opening frames.")
for k,v in D.items():
    json.dump(v,open(f'content/es/{k}.json','w'),ensure_ascii=False,indent=1)
