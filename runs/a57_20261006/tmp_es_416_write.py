import json
def T(p,t,v): return {"phrase":p,"target":t,"voice":v}
def N(w,v): return {"word":w,"voice":v}
def R(frm,*parts):
    out=[]
    for p in parts:
        if isinstance(p,tuple): out.append({"text":p[0],"gap":True,"accept":list(p[1])})
        else: out.append({"text":p})
    return {"from":frm,"parts":out}
docs={}
docs[416]=dict(mediaId=416,lang="es",level="A",keyWord="el kétchup",
 taps=[T("agitar una botella de kétchup","el hombre","male"),T("mirar al hombre","la mujer","female"),T("estar en un plato","las patatas fritas","male")],
 nouns=[N("el hombre","male"),N("la mujer","female"),N("las patatas fritas","male"),N("el kétchup","male")],
 question="¿Qué está haciendo el hombre?",
 answer=["Está","agitando","una","botella","de","kétchup."],answerVoice="male",carousel=[],
 recall=[R("taps","agitar una botella de",("kétchup",["kétchup"])),
         R("taps",("mirar",["mirar","observar"]),"al hombre"),
         R("taps","estar en un",("plato",["plato"])),
         R("answer","Está",("agitando",["agitando","sacudiendo"]),"una botella de kétchup")],
 notes="Phrase 3: the ketchup also ends up on the plate; 'estar en un plato' kept as in English (fries are the main thing on the plate). Answer drops the subject (Spain usage), so the answer recall row is the whole sentence.")
docs[72]=dict(mediaId=72,lang="es",level="A",keyWord="el baloncesto",
 taps=[T("botar el balón","la chica","female"),T("saltar muy alto","la chica","female"),T("llevar gafas","el chico de las gafas","male")],
 nouns=[N("el cielo","female"),N("el balón","female"),N("la red","female"),N("la chica","female")],
 question="¿Qué está haciendo la chica?",
 answer=["Está","jugando","al","baloncesto","con","dos","chicos."],answerVoice="female",carousel=[],
 recall=[R("taps","botar el",("balón",["balón"])),
         R("taps",("saltar",["saltar"]),"muy alto"),
         R("taps","llevar",("gafas",["gafas"])),
         R("answer","Está jugando al",("baloncesto",["baloncesto"]),"con dos chicos")],
 notes="English noun 'a basketball' (the ball) = 'el balón'; the key word 'el baloncesto' is the sport, so it appears in the answer, not in the nouns. Phrase 1 box also covers the dunk frames (girl holds the ball, not bouncing); she bounces it in most boxed frames. 'Dos chicos' for English 'two men' (young players).")
docs[401]=dict(mediaId=401,lang="es",level="A",keyWord="los patines de hielo",
 taps=[T("atarse los patines de hielo","la chica","female"),T("abrir los brazos","la chica","female"),T("llevar una chaqueta verde","la persona de verde","female")],
 nouns=[N("el gorro","female"),N("los árboles","female"),N("la bufanda","female"),N("los patines de hielo","female")],
 question="¿Qué está haciendo la chica?",
 answer=["Está","patinando","sobre","el","hielo."],answerVoice="female",carousel=[],
 recall=[R("taps","atarse los",("patines",["patines"]),"de hielo"),
         R("taps","abrir los",("brazos",["brazos"])),
         R("taps","llevar una",("chaqueta",["chaqueta","cazadora"]),"verde"),
         R("answer","Está",("patinando",["patinando"]),"sobre el hielo")],
 notes="Phrase 1/2 share one box covering the whole clip: the lacing happens only in the first seconds, arms out in most later frames. The person in green (background) looks like a man; voice kept female as in English.")
docs[4210]=dict(mediaId=4210,lang="es",level="B",keyWord="sostener",
 taps=[T("sostener dos palitos de madera","el hámster","female"),T("ocultar el rostro tras los helados","el hámster","female"),T("sonreír de oreja a oreja","el hámster","female")],
 nouns=[N("el helado","female"),N("el hámster","female"),N("la encimera","female")],
 question="¿Qué está haciendo el hámster?",
 answer=["El","hámster","sostiene","dos","helados."],answerVoice="female",carousel=[],
 recall=[R("taps",("sostener",["sostener","sujetar"]),"dos palitos de madera"),
         R("taps","ocultar el",("rostro",["rostro"]),"tras los helados"),
         R("taps",("sonreír",["sonreír"]),"de oreja a oreja"),
         R("answer","sostiene dos",("helados",["helados"]))],
 notes="All three boxes cover the whole clip: 'ocultar el rostro' is true for most frames, 'sonreír de oreja a oreja' only for the last ~3 s (one target, so no confusion). 'El helado' for the chocolate-coated ice cream bar (Spain: also 'bombón helado'). Answer subject el hámster is masculine; voice kept female as in English.")
docs[402]=dict(mediaId=402,lang="es",level="A",keyWord="el hielo",
 taps=[T("deslizarse sobre el hielo","la chica","female"),T("llevar un gorro verde","el chico","male"),T("llevar una chaqueta roja","la chica","female")],
 nouns=[N("el cielo","female"),N("los árboles","female"),N("la chica","female"),N("el hielo","female")],
 question="¿Qué está haciendo la chica?",
 answer=["Se","desliza","sobre","el","hielo."],answerVoice="female",carousel=[],
 recall=[R("taps","deslizarse sobre el",("hielo",["hielo"])),
         R("taps","llevar un",("gorro",["gorro"]),"verde"),
         R("taps","llevar una chaqueta",("roja",["roja"])),
         R("answer","Se",("desliza",["desliza"]),"sobre el hielo")],
 notes="Phrase 1 box also covers the first half where the woman crouches and touches the ice; she slides in the last frames (written for the slide, as in English). Answer drops the subject, so the answer row is the whole sentence.")
for i,d in docs.items():
    json.dump(d,open(f"content/es/{i}.json","w"),ensure_ascii=False,indent=1)
