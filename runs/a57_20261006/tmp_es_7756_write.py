import json
def P(*parts):
    out=[]
    for p in parts:
        if isinstance(p,tuple): out.append({"text":p[0],"gap":True,"accept":list(p[1])})
        else: out.append({"text":p})
    return out
def ans(s): return s.split(" ")
D={}
f="female"; m="male"
D[7756]=dict(level="B",keyWord="automotriz",
 taps=[("montar la rueda delantera","el oso",f),("empuñar una llave inglesa","el mapache",f),("estar subido al elevador","el coche rojo",f)],
 nouns=[("el oso",f),("el mapache",f),("los neumáticos",f),("el coche deportivo",f)],
 question="¿Qué está haciendo el oso?",answer="Está montando una rueda en el coche deportivo.",av=f,
 recall=[("taps",P("montar la",("rueda",["rueda"]),"delantera")),
         ("taps",P(("empuñar",["empuñar","sujetar","agarrar"]),"una llave inglesa")),
         ("taps",P("estar subido al",("elevador",["elevador"]))),
         ("answer",P("Está",("montando",["montando","colocando","poniendo"]),"una rueda en el coche deportivo"))],
 notes="keyWord 'automotriz' is an adjective and does not fit a phrase or noun pill here; in Spain 'automovilístico' / 'de automoción' (sector) is more usual than 'automotriz' (more Latin American) - proposal: keep 'automotriz' or switch to 'automovilístico'. The red car is lifted on a two-post lift ('el elevador'). The raccoon holds the spanner in most boxed frames, also after getting up.")
D[733]=dict(level="B",keyWord="el Estado",
 taps=[("alzar un sello de latón","la mujer de la banda turquesa",f),("fruncir el ceño ante el documento","el hombre canoso",m),("lucir un círculo blanco","el estandarte turquesa",m)],
 nouns=[("la lámpara de araña",m),("el círculo",m),("el triángulo",m),("el suelo de mármol",m)],
 question="¿Qué están haciendo los dos jefes de Estado?",answer="Se están dando la mano delante de sus estandartes.",av=m,
 recall=[("taps",P("alzar un",("sello",["sello"]),"de latón")),
         ("taps",P("fruncir el ceño ante el",("documento",["documento"]))),
         ("taps",P(("lucir",["lucir","mostrar","llevar"]),"un círculo blanco")),
         ("answer",P("Se están",("dando",["dando","estrechando"]),"la mano delante de sus estandartes"))],
 notes="Key word 'el Estado' is used inside 'jefes de Estado' in the question (the two leaders with sashes; the transcript speaks of two nations) - the clip shows the leaders, not the state itself. The red box (woman) also covers the walking, handshake and posing frames: the stamp is raised only in the first shots (the brass stamp is visible in her hand there). The man frowns at the document only in his close-ups; later he shakes hands. Answer without subject (Spanish drops it; with 'Los dos jefes de Estado' it would be 12 words).")
D[788]=dict(level="B",keyWord="calentar en el microondas",
 taps=[("calentar sus fideos en el microondas","el chico",m),("sonreír de oreja a oreja","la chica",f),("iluminarse por dentro","el microondas",m)],
 nouns=[("el microondas",m),("los fideos",m),("el estante",m),("la sudadera",m)],
 question="¿Qué está haciendo el chico?",answer="Está calentando un cuenco de fideos en el microondas.",av=m,
 recall=[("taps",P("calentar sus fideos en el",("microondas",["microondas"]))),
         ("taps",P(("sonreír",["sonreír"]),"de oreja a oreja")),
         ("taps",P(("iluminarse",["iluminarse","encenderse"]),"por dentro")),
         ("answer",P("Está",("calentando",["calentando"]),"un cuenco de fideos en el microondas"))],
 notes="The blue box (microwave) covers many frames where it is not lit (door open, steam, bowl taken out); the inside lights up while it runs (warm light in the close-ups of the turning bowl). 'la sudadera' = the grey hoodie (Spain: 'sudadera' is the everyday word, 'con capucha' left out).")
D[4143]=dict(level="B",keyWord="el cubo",
 taps=[("mirar fijamente hacia arriba","el mapache",m),("estar arrugada en el fondo","la bolsa verde",m),("asomar por detrás del cubo","los arbustos",m)],
 nouns=[("el mapache",m),("la bolsa de basura",m),("el cubo de basura",m),("los arbustos",m)],
 question="¿Qué está intentando hacer el mapache?",answer="Está intentando escaparse del cubo de basura.",av=m,
 recall=[("taps",P(("mirar",["mirar"]),"fijamente hacia arriba")),
         ("taps",P("estar",("arrugada",["arrugada"]),"en el fondo")),
         ("taps",P("asomar por detrás del",("cubo",["cubo"]))),
         ("answer",P("Está intentando",("escaparse",["escaparse","salir"]),"del cubo de basura"))],
 notes="Tap 1 is not 'intentar escaparse' (that is the answer): in most boxed frames the raccoon sits and stares up at the camera; the escape attempt (paws up the wall) is only a few frames. Noun 3 is 'el cubo de basura' (contains the key word 'cubo'): 'el cubo' alone reads as 'bucket' in Spain; a big wheelie bin like this one is also called 'el contenedor' - proposal: keep 'el cubo' (de basura). No nouns recall row: tap 3 already contains 'cubo'.")
D[6908]=dict(level="B",keyWord="el bisonte",
 taps=[("sostener un sándwich","la mujer",f),("pasar lentamente junto al descapotable","el bisonte grande",f),("estar tirado en el asfalto","el sombrero de paja",f)],
 nouns=[("el bisonte",f),("el sombrero de paja",f),("el descapotable",f),("las montañas",f)],
 question="¿Qué está haciendo el bisonte grande?",answer="Está pasando lentamente junto al descapotable.",av=f,
 recall=[("taps",P("sostener un",("sándwich",["sándwich"]))),
         ("taps",P(("pasar",["pasar","caminar","andar"]),"lentamente junto al descapotable")),
         ("taps",P("estar tirado en el",("asfalto",["asfalto","suelo"]))),
         ("nouns",P("el",("bisonte",["bisonte"]))),
         ("answer",P("Está pasando lentamente junto al",("descapotable",["descapotable","coche"])))],
 notes="English 'buffalo' = 'el bisonte' (American bison; 'búfalo' would be the wrong animal). 'sándwich' (sliced bread), not 'bocadillo' (baguette in Spain). Other bison cross the road in the background but none passes the car.")
for i,d in D.items():
    o={"mediaId":i,"lang":"es","level":d["level"],"keyWord":d["keyWord"],
       "taps":[{"phrase":a,"target":b,"voice":c} for a,b,c in d["taps"]],
       "nouns":[{"word":a,"voice":b} for a,b in d["nouns"]],
       "question":d["question"],"answer":ans(d["answer"]),"answerVoice":d["av"],"carousel":[],
       "recall":[{"from":fr,"parts":p} for fr,p in d["recall"]],"notes":d["notes"]}
    json.dump(o,open(f"content/es/{i}.json","w"),ensure_ascii=False,indent=1)
