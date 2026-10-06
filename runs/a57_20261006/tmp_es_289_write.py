import json
def r(frm,*parts):
    ps=[]
    for p in parts:
        if isinstance(p,tuple): ps.append({"text":p[0],"gap":True,"accept":list(p[1:]) or [p[0]]})
        else: ps.append({"text":p})
    return {"from":frm,"parts":ps}
def T(p,t,v): return {"phrase":p,"target":t,"voice":v}
def N(w,v="female"): return {"word":w,"voice":v}
D={}
D[289]=dict(level="B",keyWord="el miedo",
 taps=[T("llevarse la mano al pecho","la mujer de azul","female"),T("aferrarse a un poste","la mujer de azul","female"),T("acercarse por detrás","la mujer de amarillo","female")],
 nouns=[N("las cumbres"),N("la barandilla"),N("el reflejo")],
 question="¿Qué hace la mujer de azul?",answer="Se aferra a un poste, muerta de miedo.".split(),answerVoice="female",
 recall=[r("taps","llevarse la mano al",("pecho",)),r("taps",("aferrarse","aferrarse","agarrarse"),"a un poste"),r("taps",("acercarse",),"por detrás"),
   r("answer","Se aferra a un poste, muerta de",("miedo",))],
 notes="Answer uses the B1 collocation 'muerta de miedo' (key word). Phrase 1: she brings her hand to her chest only in the middle boxed frames; elsewhere she grips the rail. Phrase 3: the woman in yellow walks up behind her in the boxed frames.")
D[290]=dict(level="A",keyWord="el sentimiento",
 taps=[T("tocarse el pecho","la mujer","female"),T("cerrar los ojos","la mujer","female"),T("llevar una camisa gris","el hombre del pelo largo","male")],
 nouns=[N("la bandera"),N("la mujer"),N("el vaso")],
 question="¿Qué está haciendo la mujer?",answer="Se está tocando el pecho.".split(),answerVoice="female",
 recall=[r("taps",("tocarse",),"el pecho"),r("taps","cerrar los",("ojos",)),r("taps","llevar una",("camisa",),"gris"),r("answer","Se está tocando el",("pecho",))],
 notes="Phrase 2: the English box covers the woman for most of the clip, but her eyes are closed only in a few frames (tense moment before the goal). Key word 'el sentimiento' does not appear in any exercise (abstract word, nothing to name); kept unchanged.")
D[292]=dict(level="A",keyWord="la pelea",
 taps=[T("levantar una almohada en alto","la mujer","female"),T("llevar una camiseta gris","la mujer","female"),T("tener barba","el hombre","male")],
 nouns=[N("la ventana"),N("la almohada"),N("la planta"),N("la cama")],
 question="¿Qué hacen en la cama?",answer="Tienen una pelea de almohadas.".split(),answerVoice="female",
 recall=[r("taps",("levantar","levantar","subir"),"una almohada en alto"),r("taps","llevar una",("camiseta",),"gris"),r("taps","tener",("barba",)),
   r("answer","Tienen una",("pelea","pelea","guerra"),"de almohadas")],
 notes="In Spain 'guerra de almohadas' is the most common term; 'pelea de almohadas' is also natural and uses the key word, so the answer uses it and the recall accepts 'guerra'. Phrase 1: she lifts the pillow high in several, not all, boxed frames.")
D[293]=dict(level="B",keyWord="la realización de películas",
 taps=[T("hacerse visera con la mano","la mujer de la bufanda","female"),T("agacharse detrás de la cámara","la mujer de la gorra","female"),T("estar posada en la cornisa","la paloma","female")],
 nouns=[N("el micrófono"),N("el reflector"),N("la paloma"),N("el trípode")],
 question="¿Sobre qué está montada la cámara?",answer="La cámara está montada sobre un trípode.".split(),answerVoice="female",
 recall=[r("taps","hacerse",("visera",),"con la mano"),r("taps",("agacharse","agacharse","ponerse en cuclillas"),"detrás de la cámara"),r("taps","estar",("posada",),"en la cornisa"),
   r("answer","está",("montada","montada","colocada"),"sobre un trípode")],
 notes="Key word 'la realización de películas' is correct but bookish; a Spaniard would rather say 'el rodaje' (shooting) or 'hacer cine'. Proposal: 'el rodaje' for this clip. Not used in the exercises. Phrase 1: she shades her eyes with her hand only in some boxed frames; in the others she stands by the reflector.")
D[294]=dict(level="A",keyWord="el fuego",
 taps=[T("sujetar un palo largo","la mujer","female"),T("echar un tronco al fuego","el hombre","male"),T("arder entre las piedras","el fuego","female")],
 nouns=[N("los árboles"),N("el hombre","male"),N("el fuego"),N("las piedras")],
 question="¿Qué está haciendo el hombre?",answer="Está echando un tronco al fuego.".split(),answerVoice="male",
 recall=[r("taps","sujetar un",("palo",),"largo"),r("taps","echar un",("tronco",),"al fuego"),r("taps",("arder",),"entre las piedras"),r("answer","Está echando un tronco al",("fuego",))],
 notes="English 'wood' rendered as 'un tronco' (he drops one log). Phrase 2: the man puts the log on only in the first boxed frames, later he watches the sparks. 'arder' is borderline A2/B1 but the plain right verb for a fire.")
for i,d in D.items():
    o={"mediaId":i,"lang":"es","level":d["level"],"keyWord":d["keyWord"],"taps":d["taps"],"nouns":d["nouns"],"question":d["question"],"answer":d["answer"],
       "answerVoice":d["answerVoice"],"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(o,open(f"content/es/{i}.json","w"),ensure_ascii=False,indent=1)
