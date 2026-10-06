import json
def P(*a):
    out=[]
    for x in a:
        if isinstance(x,tuple): out.append({"text":x[0],"gap":True,"accept":list(x[1])})
        else: out.append({"text":x})
    return out
def W(i,level,kw,taps,nouns,q,ans,av,recall,notes):
    d={"mediaId":i,"lang":"es","level":level,"keyWord":kw,
       "taps":[{"phrase":p,"target":t,"voice":v} for p,t,v in taps],
       "nouns":[{"word":w,"voice":v} for w,v in nouns],
       "question":q,"answer":ans.split(),"answerVoice":av,"carousel":[],
       "recall":[{"from":f,"parts":p} for f,p in recall],"notes":notes}
    json.dump(d,open(f"content/es/{i}.json","w"),ensure_ascii=False,indent=1)
m,f="male","female"
W(47,"B","el pabellón deportivo",
 [("alzar el puño","el hombre",m),("lanzar las palomitas al aire","el niño",m),("estar suspendido sobre la pista","el marcador",m)],
 [("el marcador",m),("los espectadores",m),("la pista",m),("las palomitas",m)],
 "¿Dónde están el hombre y el niño?","Están en un pabellón deportivo abarrotado.",m,
 [("taps",P(("alzar",["alzar","levantar"]),"el puño")),
  ("taps",P("lanzar las",("palomitas",["palomitas"]),"al aire")),
  ("taps",P("estar",("suspendido",["suspendido","colgado"]),"sobre la pista")),
  ("answer",P("Están en un",("pabellón",["pabellón"]),"deportivo abarrotado"))],
 "Court = 'la pista' (usual in Spain for basketball). At the end the boy also raises his arms, but while throwing popcorn; only the man raises a clenched fist.")
W(48,"A","llegar",
 [("abrir la puerta","el hombre",m),("tener sábanas blancas","la cama",m),("tener pequeñas olas blancas","el mar",m)],
 [("el cielo",m),("el mar",m),("la arena",m),("las palmeras",m)],
 "¿Qué está haciendo el hombre?","Está abriendo la puerta.",m,
 [("taps",P("abrir la",("puerta",["puerta"]))),
  ("taps",P("tener",("sábanas",["sábanas"]),"blancas")),
  ("taps",P("tener pequeñas",("olas",["olas"]),"blancas")),
  ("answer",P("Está",("abriendo",["abriendo"]),"la puerta"))],
 "English 'trees' are palm trees: 'las palmeras' is the everyday Spanish word (A2). Key word llegar appears in no exercise (the clip's exercises do not need it).")
W(49,"B","la flecha",
 [("recuperar su flecha","la mujer",f),("descansar sobre un soporte","la diana",f),("quedarse detrás de la arquera","el hombre",m)],
 [("el cielo",f),("la flecha",f),("la diana",f),("la hierba",f)],
 "¿Dónde se ha clavado la flecha?","La flecha se ha clavado en el centro de la diana.",f,
 [("taps",P("recuperar su",("flecha",["flecha"]))),
  ("taps",P("descansar sobre un",("soporte",["soporte"]))),
  ("taps",P("quedarse detrás de la",("arquera",["arquera"]))),
  ("answer",P("se ha",("clavado",["clavado"]),"en el centro de la diana"))],
 "Question 'What has the arrow hit?' rendered as '¿Dónde se ha clavado la flecha?' (natural; '¿En qué ha dado?' sounds odd). The man is only visible in the last frames.")
W(50,"A","el tarro",
 [("sujetar la manga pastelera","la mano",f),("llevar un guante negro","la mano",f),("llenarse de crema","el tarro",f)],
 [("el guante",f),("la manga pastelera",f),("el tarro",f),("la mesa",f)],
 "¿Qué está haciendo la mano?","Está llenando un tarro de crema.",f,
 [("taps",P(("sujetar",["sujetar","sostener","agarrar"]),"la manga pastelera")),
  ("taps",P("llevar un",("guante",["guante"]),"negro")),
  ("taps",P(("llenarse",["llenarse"]),"de crema")),
  ("answer",P("Está llenando un",("tarro",["tarro"]),"de crema"))],
 "'la manga pastelera' is the only natural word for the piping bag (above A2, plain right word). Phrases 1 and 2 both have the hand as target, as in English.")
W(51,"B","apretar",
 [("estrujar el slime","la mano",m),("agarrar un puñado","la mano",m),("estar en segundo plano","la taza",m)],
 [("la taza",m),("el pulgar",m),("la muñeca",m),("las bolitas",m)],
 "¿Qué está haciendo la mano?","Está apretando un puñado de bolitas.",m,
 [("taps",P(("estrujar",["estrujar","apretar"]),"el slime")),
  ("taps",P("agarrar un",("puñado",["puñado"]))),
  ("taps",P("estar en segundo",("plano",["plano"]))),
  ("answer",P("Está",("apretando",["apretando","estrujando"]),"un puñado de bolitas"))],
 "Water beads = 'las bolitas' (everyday Spain; 'bolitas de gel'). 'el slime' is the usual word in Spain. Answer voice kept male (English), although 'la mano' is grammatically feminine.")
