import json
def P(*a):
    out=[]
    for x in a:
        if isinstance(x,tuple): out.append({"text":x[0],"gap":True,"accept":list(x)})
        else: out.append({"text":x})
    return out
def W(i,level,kw,taps,nouns,q,ans,av,recall,notes):
    d={"mediaId":i,"lang":"es","level":level,"keyWord":kw,
       "taps":[{"phrase":p,"target":t,"voice":v} for p,t,v in taps],
       "nouns":[{"word":w,"voice":v} for w,v in nouns],
       "question":q,"answer":ans.split(),"answerVoice":av,"carousel":[],
       "recall":[{"from":f,"parts":P(*ps)} for f,ps in recall],"notes":notes}
    json.dump(d,open(f"content/es/{i}.json","w"),ensure_ascii=False,indent=1)
W(221,"B","el título universitario",
 [("celebrar su graduación","la mujer","female"),("lucir un sello dorado","el título","female"),("revolotear por el aire","el confeti","female")],
 [("el título universitario","female"),("el birrete","female"),("la borla","female")],
 "¿Qué está celebrando la mujer?","Está celebrando su graduación.","female",
 [("taps",["celebrar su",("graduación",)]),("taps",["lucir un",("sello",),"dorado"]),("taps",[("revolotear","volar"),"por el aire"]),
  ("nouns",["el",("título",),"universitario"]),("answer",["Está",("celebrando","festejando"),"su graduación"])],
 "Noun 1 'a degree certificate' = the key word 'el título universitario' (in Spain the document itself is 'el título'). Answer drops the subject, so the answer row is the whole sentence.")
W(222,"B","el retraso",
 [("impedir el paso a los pasajeros","el conductor","male"),("desplomarse sobre su maleta","la mujer","female"),("marcar la hora","el reloj","female")],
 [("el reloj","female"),("la maleta","female"),("los rótulos de neón","female"),("el conductor","male")],
 "¿Qué está haciendo el conductor?","Está bloqueando la puerta del autobús.","male",
 [("taps",[("impedir","bloquear"),"el paso a los pasajeros"]),("taps",[("desplomarse","derrumbarse"),"sobre su maleta"]),("taps",["marcar la",("hora",)]),
  ("answer",["Está",("bloqueando","tapando"),"la puerta del autobús"])],
 "Phrase 1: the driver's box also covers frames where he sits behind the windscreen (arms up, head on the wheel); the phrase describes him at the door, his main action. Key word 'el retraso' is not a noun of the set, so no noun row.")
W(223,"A","la entrega",
 [("estar tumbado en el sofá","el gato","male"),("entregar la comida","el hombre del casco","male"),("llevar una camiseta naranja","la mujer","female")],
 [("la lámpara","male"),("la ventana","male"),("el gato","male"),("el sofá","male")],
 "¿Quién está entregando la comida?","Un hombre con casco está entregando la comida.","male",
 [("taps",["estar",("tumbado","echado"),"en el sofá"]),("taps",["entregar la",("comida",)]),("taps",["llevar una",("camiseta",),"naranja"]),
  ("answer",["está",("entregando","trayendo"),"la comida"])],
 "Phrase 1: the cat lies on the sofa at the start; in late boxed frames it sits at the sofa's edge. 'Entregar' carries the key word 'la entrega' (verb form); no noun row since 'la entrega' is not a noun of the set.")
W(224,"B","diseñar",
 [("hacer el boceto de una silla","el hombre","male"),("señalar el boceto","la mujer","female"),("olfatear la silla de cartón","el gato","female")],
 [("el boceto","female"),("el tarro","female"),("la planta de interior","female")],
 "¿Qué están diseñando?","Están diseñando una silla.","female",
 [("taps",["hacer el",("boceto","dibujo"),"de una silla"]),("taps",[("señalar",),"el boceto"]),("taps",[("olfatear","oler"),"la silla de cartón"]),
  ("answer",["Están",("diseñando",),"una silla"])],
 "Key word 'diseñar' is a verb while English 'designing' is a gerund noun; the verb fits the clip and is used in the question and answer. Phrase 1: the man's box also covers model-building frames; he sketches in most of them.")
W(226,"B","la desesperación",
 [("tocar el acordeón","el músico","male"),("agacharse junto al estuche","el músico","male"),("permanecer abierto y vacío","el estuche","male")],
 [("el acordeón","male"),("los grafitis","male"),("el estuche","male"),("el tablón de anuncios","male")],
 "¿Qué está tocando el músico?","Está tocando el acordeón.","male",
 [("taps",["tocar el",("acordeón",)]),("taps",[("agacharse","acuclillarse"),"junto al estuche"]),("taps",["permanecer abierto y",("vacío",)]),
  ("answer",["Está",("tocando",),"el acordeón"])],
 "Phrases 1 and 2 share the same English box (the musician); he crouches toward the case in only some boxed frames and ends sitting on the tunnel floor. Phrase 2 is 'agacharse junto al estuche' (he bends down at the case), not 'en el suelo', to fit what he does. Key word 'la desesperación' is not shown in any text (no noun of the set).")
