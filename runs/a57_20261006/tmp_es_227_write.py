import json
def P(*parts):
    out=[]
    for p in parts:
        if isinstance(p,tuple): out.append({"text":p[0],"gap":True,"accept":list(p[1])})
        else: out.append({"text":p})
    return out
def W(i,level,kw,taps,nouns,q,ans,av,recall,notes):
    d={"mediaId":i,"lang":"es","level":level,"keyWord":kw,
       "taps":[{"phrase":a,"target":b,"voice":c} for a,b,c in taps],
       "nouns":[{"word":a,"voice":b} for a,b in nouns],
       "question":q,"answer":ans.split(" "),"answerVoice":av,"carousel":[],
       "recall":[{"from":f,"parts":p} for f,p in recall],"notes":notes}
    json.dump(d,open(f'content/es/{i}.json','w'),ensure_ascii=False,indent=1)
F,M='female','male'
W(227,"B","el diamante",
 [("sujetar un diamante con unas pinzas","la mujer de los guantes",F),
  ("quedarse boquiabierta","la mujer pelirroja",F),
  ("descansar en el alféizar","el gato",F)],
 [("el diamante",F),("el cojín",F),("el gato",F),("la cadena",F)],
 "¿Qué mira fijamente la mujer pelirroja?","Mira fijamente un diamante reluciente.",F,
 [("taps",P("sujetar un",("diamante",["diamante"]),"con unas pinzas")),
  ("taps",P("quedarse",("boquiabierta",["boquiabierta"]))),
  ("taps",P("descansar en el",("alféizar",["alféizar"]))),
  ("answer",P("Mira fijamente un diamante",("reluciente",["reluciente","brillante"])))],
 "Phrase 1: the gloved jeweller holds the diamond in tweezers in most boxed frames (in a few she uses the loupe or holds the ring); the English 'magnifying glass' is the loupe at her eye, tweezers are more constant. The diamond pill sits on the ring's stone.")
W(228,"A","la cena",
 [("llevar una olla caliente","la mujer de la olla",F),
  ("encender una vela","el hombre",M),
  ("estar sentado en el muro","el gato",F)],
 [("el gato",F),("la olla",F),("la ensalada",F),("el pan",F)],
 "¿Qué está haciendo la gente?","Están cenando juntos.",F,
 [("taps",P("llevar una",("olla",["olla"]),"caliente")),
  ("taps",P(("encender",["encender"]),"una vela")),
  ("taps",P("estar sentado en el",("muro",["muro"]))),
  ("answer",P("Están",("cenando",["cenando","comiendo"]),"juntos"))],
 "Phrase 2: the man lights the candle only in the first frames; in most later boxed frames he passes bread, pours water, toasts and eats. Key word la cena appears only as the verb cenar (answer); it is not one of the four nouns, so no noun row.")
W(229,"B","el diploma",
 [("cruzar el escenario","el graduado",M),
  ("estrechar la mano al graduado","el señor mayor",M),
  ("estar atado con una cinta","el diploma",M)],
 [("el diploma",M),("el birrete",M),("la toga",M),("la banda",M)],
 "¿Qué está haciendo el graduado?","Está levantando el diploma por encima de la cabeza.",M,
 [("taps",P("cruzar el",("escenario",["escenario"]))),
  ("taps",P(("estrechar",["estrechar"]),"la mano al graduado")),
  ("taps",P("estar atado con una",("cinta",["cinta","lazo"]))),
  ("answer",P("Está levantando el",("diploma",["diploma","título"]),"por encima de la cabeza"))],
 "Phrase 2: English 'congratulate'; the visible act is the handshake, so 'estrechar la mano'. Phrase 1: in the last boxed frames the graduate stands lifting the diploma rather than crossing. Sash = 'la banda' (in Spain also 'la beca' for the university sash, avoided as ambiguous).")
W(231,"B","decepcionar",
 [("romper a llorar","la mujer",F),
  ("darle una palmadita en el hombro","el hombre",M),
  ("parpadear sobre la mesa","la vela",F)],
 [("la guirnalda de luces",F),("la vela",F),("los espaguetis",F),("el regalo",F)],
 "¿Qué hace la mujer?","Rompe a llorar en la mesa.",F,
 [("taps",P("romper a",("llorar",["llorar"]))),
  ("taps",P("darle una",("palmadita",["palmadita"]),"en el hombro")),
  ("taps",P(("parpadear",["parpadear","titilar"]),"sobre la mesa")),
  ("answer",P("Rompe a llorar en la",("mesa",["mesa"])))],
 "Phrase 2: the man touches her shoulder only in a few boxed frames; in most he arrives, waves, points at his watch and apologises. Phrase 1: in the first boxed frames the woman is still happy. Key word decepcionar does not appear in the texts (nothing natural and visible).")
W(232,"B","decepcionado",
 [("frotarse las manos con impaciencia","el hombre del chubasquero",M),
  ("parecer muy decepcionado","el hombre del chubasquero",M),
  ("contener una ración diminuta","la bandeja del hombre",M)],
 [("el gorro",M),("la barba",M),("el chubasquero",M),("la bandeja",M)],
 "¿Qué aspecto tiene el hombre de delante?","Parece decepcionado con su bandeja vacía.",M,
 [("taps",P("frotarse las manos con",("impaciencia",["impaciencia","ganas"]))),
  ("taps",P("parecer muy",("decepcionado",["decepcionado"]))),
  ("taps",P("contener una",("ración",["ración","porción"]),"diminuta")),
  ("answer",P("Parece decepcionado con su",("bandeja",["bandeja"]),"vacía"))],
 "Phrases 1 and 2 share the same target (as in English). Raincoat = 'el chubasquero' (everyday Spain word). Phrase 1: he rubs his hands only in the first boxed frames.")
