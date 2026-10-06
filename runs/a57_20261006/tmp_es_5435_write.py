import json
def R(src,*parts):
    out=[]
    for p in parts:
        if isinstance(p,tuple): out.append({"text":p[0],"gap":True,"accept":list(p[1])})
        else: out.append({"text":p})
    return {"from":src,"parts":out}
D={}
D[5435]=dict(level="B",keyWord="parecido",
 taps=[dict(phrase="sacar algo azul de la riñonera",target="la chica de la izquierda",voice="female"),
       dict(phrase="sacar algo rojo de la riñonera",target="la chica de la derecha",voice="female"),
       dict(phrase="guardar algo azul en la riñonera",target="la chica de la derecha",voice="female")],
 nouns=[dict(word="el cielo",voice="female"),dict(word="los árboles",voice="female"),dict(word="el césped",voice="female"),dict(word="la acera",voice="female")],
 question="¿Cómo son las dos chicas?",answer="Las dos chicas son muy parecidas.".split(),answerVoice="female",
 recall=[R("taps",("sacar",["sacar"]),"algo azul de la riñonera"),
         R("taps","sacar algo rojo de la",("riñonera",["riñonera"])),
         R("taps",("guardar",["guardar","meter"]),"algo azul en la riñonera"),
         R("answer","son muy",("parecidas",["parecidas"]))],
 notes="Key word parecido is an adjective, so no noun row. The blue and red things are crisp packets taken from / put into the bum bags (riñonera, B1). The two chicas are early 20s; 'chicas' is what a Spanish teacher says (English 'women'). Answer 'muy parecidas' renders 'exactly alike' without forcing 'idénticas', so the key word stays in the answer.")
D[6824]=dict(level="B",keyWord="el aire acondicionado",
 taps=[dict(phrase="secarse la frente sudorosa",target="el hombre",voice="male"),
       dict(phrase="marcar la presión",target="los manómetros",voice="male"),
       dict(phrase="recoger el agua que gotea",target="el cubo",voice="male")],
 nouns=[dict(word="el aire acondicionado",voice="male"),dict(word="el cubo",voice="male"),dict(word="la gorra",voice="male"),dict(word="el cielo",voice="male")],
 question="¿Qué está haciendo el hombre?",answer="El hombre está revisando el aire acondicionado.".split(),answerVoice="male",
 recall=[R("taps","secarse la",("frente",["frente"]),"sudorosa"),
         R("taps","marcar la",("presión",["presión"])),
         R("taps","recoger el agua que",("gotea",["gotea","cae"])),
         R("answer","está revisando el",("aire acondicionado",["aire acondicionado"]))],
 notes="Noun 1 points at the outdoor unit; 'el aire acondicionado' is how Spaniards name the unit too (more precisely 'el aparato de aire acondicionado'). Key word is in the answer row, so no separate noun row; its gap is the two-word key word 'aire acondicionado'. Phrase 2 uses 'marcar' (a gauge 'marca' the pressure), the natural Spanish verb. Phrase 3: the bucket box goes OFF in later frames; water drips into it in the boxed frames.")
D[4858]=dict(level="B",keyWord="la espiral",
 taps=[dict(phrase="derribar la primera ficha",target="el chico",voice="male"),
       dict(phrase="apretar los puños",target="el chico",voice="male"),
       dict(phrase="formar una espiral enorme",target="las fichas de dominó",voice="male")],
 nouns=[dict(word="la espiral",voice="male"),dict(word="el chico",voice="male"),dict(word="el suelo",voice="male")],
 question="¿Qué ha construido el chico?",answer="El chico ha construido una espiral enorme de fichas de dominó.".split(),answerVoice="male",
 recall=[R("taps",("derribar",["derribar","tirar"]),"la primera ficha"),
         R("taps","apretar los",("puños",["puños"])),
         R("taps","formar una",("espiral",["espiral"]),"enorme"),
         R("answer",("ha construido",["ha construido","ha montado","ha hecho"]),"una espiral enorme de fichas de dominó")],
 notes="English 'a man' -> 'el chico' (he is early 20s; used the same in target, noun and answer). The man's boxes (phrases 1 and 2) also cover the middle frames where he only points along the rows; he topples the first piece at the start and clenches his fists at the end. Answer has 10 chips (upper limit). Key word espiral is in the phrase-3 row, so no noun row. Answer-row gap is the perfect 'ha construido' as one part.")
D[5566]=dict(level="B",keyWord="la llegada",
 taps=[dict(phrase="cruzar la línea de meta",target="la corredora",voice="female"),
       dict(phrase="recoger la cinta del suelo",target="la chica de la sudadera",voice="female"),
       dict(phrase="aplaudir detrás de las vallas",target="los espectadores",voice="female")],
 nouns=[dict(word="la corredora",voice="female"),dict(word="los espectadores",voice="female"),dict(word="los banderines",voice="female"),dict(word="los vasos de papel",voice="female")],
 question="¿Qué está haciendo la corredora?",answer="La corredora está cruzando la línea de meta.".split(),answerVoice="female",
 recall=[R("taps",("cruzar",["cruzar","atravesar"]),"la línea de meta"),
         R("taps","recoger la",("cinta",["cinta"]),"del suelo"),
         R("taps","aplaudir detrás de las",("vallas",["vallas","barreras"])),
         R("answer","está cruzando la línea de",("meta",["meta","llegada"]))],
 notes="Key word 'la llegada' names the arrival at the finish; in Spain the finish line is usually 'la línea de meta' ('línea de llegada' is also said), so the answer-row gap accepts 'llegada'. The key word is not a noun of the set, so no noun row. Phrase 3 uses 'aplaudir' (the spectators clap; the man in the rust T-shirt also claps, but in front of the barriers, so 'detrás de las vallas' keeps it unique).")
D[4538]=dict(level="B",keyWord="el descanso",
 taps=[dict(phrase="frotar la mesa de cristal",target="la mujer",voice="female"),
       dict(phrase="atar la bolsa de basura",target="la mujer",voice="female"),
       dict(phrase="recostarse en el sofá",target="la mujer",voice="female")],
 nouns=[dict(word="el sofá",voice="female"),dict(word="el radiador",voice="female"),dict(word="la bombilla",voice="female"),dict(word="la estantería",voice="female")],
 question="¿Dónde descansa la mujer?",answer="La mujer se toma un descanso en el sofá.".split(),answerVoice="female",
 recall=[R("taps",("frotar",["frotar","limpiar"]),"la mesa de cristal"),
         R("taps","atar la",("bolsa",["bolsa"]),"de basura"),
         R("taps",("recostarse",["recostarse"]),"en el sofá"),
         R("answer","se toma un",("descanso",["descanso"]),"en el sofá")],
 notes="All three English boxes follow the woman through the whole clip (scrubbing, then tying the bag, then reclining), so each phrase is true only in its own part of the clip. Answer uses the key word via 'tomarse un descanso' (B1 collocation). Key word is not a noun of the set, so no noun row.")
for mid,d in D.items():
    o={"mediaId":mid,"lang":"es",**{k:d[k] for k in ["level","keyWord","taps","nouns","question","answer","answerVoice"]},"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(o,open(f"content/es/{mid}.json","w"),ensure_ascii=False,indent=1)
