import json
def P(*parts):
    out=[]
    for p in parts:
        if isinstance(p,tuple): out.append({"text":p[0],"gap":True,"accept":list(p[1:]) or [p[0]]})
        else: out.append({"text":p})
    return out
def acc(t,*o): return (t,t,*o)
def W(mid,kw,taps,nouns,q,ans,av,rec,notes,voice):
    d={"mediaId":mid,"lang":"es","level":"A","keyWord":kw,
       "taps":[{"phrase":p,"target":t,"voice":v} for p,t,v in taps],
       "nouns":[{"word":w,"voice":v} for w,v in nouns],
       "question":q,"answer":ans.split(),"answerVoice":av,"carousel":[],
       "recall":[{"from":f,"parts":p} for f,p in rec],"notes":notes}
    json.dump(d,open(f"content/es/{mid}.json","w"),ensure_ascii=False,indent=1)
m,f="male","female"
W(795,"la toalla",
 [("salir de la piscina","el hombre",m),("secarse el pelo","el hombre",m),("sacudirse el agua","el perro",m)],
 [("el hombre",m),("la toalla",m),("el perro",m),("el árbol",m)],
 "¿Qué hace el hombre?","Se seca el pelo con una toalla.",m,
 [("taps",P("salir de la",acc("piscina"))),("taps",P(acc("secarse"),"el pelo")),("taps",P(acc("sacudirse"),"el agua")),
  ("answer",P("Se seca el pelo con una",acc("toalla")))],
 "Key word la toalla appears in noun 2 and the answer row (gap), so no extra noun row. Tap 1 red box covers the whole clip although the man leaves the pool only at the start. Tap 3: the dog shakes the water off its head (sacudirse el agua); the blue box also covers the end where it is wrapped in the towel.",m)
W(7212,"desayunar",
 [("tomar el desayuno","la mujer",f),("sujetar un tenedor","la mujer",f),("mirar la comida","el pájaro",f)],
 [("el pájaro",f),("la taza",f),("el plato",f),("el gorro",f)],
 "¿Qué hace la mujer?","Está desayunando por encima de las nubes.",f,
 [("taps",P("tomar el",acc("desayuno"))),("taps",P("sujetar un",acc("tenedor"))),("taps",P(acc("mirar"),"la comida")),
  ("answer",P("Está",acc("desayunando"),"por encima de las nubes"))],
 "Tap 1 uses 'tomar el desayuno' (a one-word phrase 'desayunar' cannot be cut into recall parts); the key word desayunar is in the answer and gapped there. Tap 3: the raven sits next to her and looks towards her mug, fork and plate; 'mirar la comida' is the closest fit. Bird = 'el pájaro' (A1) rather than 'el cuervo'.",f)
W(385,"golpear",
 [("golpear la pelota","la chica",f),("sujetar un bate","la chica",f),("volar por el aire","la pelota",f)],
 [("la pelota",f),("el bate",f),("la gorra",f)],
 "¿Qué hace la chica?","Golpea la pelota con un bate.",f,
 [("taps",P(acc("golpear"),"la pelota")),("taps",P("sujetar un",acc("bate"))),("taps",P(acc("volar"),"por el aire")),
  ("answer",P("Golpea la",acc("pelota"),"con un bate"))],
 "Tap 1 red box also covers the swing-through and the start of her run; 'golpear la pelota' describes the main boxed action.",f)
W(7773,"con cuidado",
 [("llevar las tazas con cuidado","el oso",f),("estar sentada a la mesa","la mujer",f),("levantar las manos","la mujer",f)],
 [("las tazas",f),("la mujer",f),("la mesa",f),("el oso",f)],
 "¿Qué hace el oso?","Lleva las tazas a la mesa.",f,
 [("taps",P("llevar las tazas con",acc("cuidado"))),("taps",P("estar",acc("sentada"),"a la mesa")),("taps",P(acc("levantar"),"las manos")),
  ("answer",P(acc("Lleva"),"las tazas a la mesa"))],
 "Key word 'con cuidado' is in tap 1 (gap 'cuidado'); kept out of the answer to avoid two possible chip orders. Answer voice female copied from English although el oso is masculine (no pronoun in the Spanish sentence). Tap 2 'estar sentada' because she is already seated throughout.",f)
W(528,"aparcar",
 [("aparcar el coche","la mujer",f),("estar sentado en un muro","el hombre",m),("abrir la puerta del coche","la mujer",f)],
 [("la mujer",f),("el coche",f),("el cielo",f)],
 "¿Qué hace la mujer?","Aparca su coche.",f,
 [("taps",P(acc("aparcar"),"el coche")),("taps",P("estar",acc("sentado"),"en un muro")),("taps",P("abrir la",acc("puerta"),"del coche")),
  ("answer",P("Aparca su",acc("coche")))],
 "Tap 3 blue box also covers the driving and key frames where she does not open the door yet; the phrase describes the moment she gets out. The man sits on a low wall (muro).",f)
