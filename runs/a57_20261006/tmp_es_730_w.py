import json
def t(p,tg,v): return {"phrase":p,"target":tg,"voice":v}
def n(w,v="female"): return {"word":w,"voice":v}
def r(frm,parts): return {"from":frm,"parts":parts}
def g(x,acc): return {"text":x,"gap":True,"accept":acc}
def p(x): return {"text":x}
D={}
D[730]=dict(level="B",keyWord="la plantilla",
 taps=[t("pasar un paño por la encimera","el cocinero","male"),t("extender un mantel","la camarera","female"),t("servir un capuchino en la barra","el camarero de la barra","male")],
 nouns=[n("la plantilla"),n("los comensales"),n("el mantel"),n("las lámparas colgantes")],
 question="¿Qué está haciendo la camarera?",answer="La camarera está extendiendo un mantel blanco.".split(),answerVoice="female",
 recall=[r("taps",[p("pasar un"),g("paño",["paño","trapo"]),p("por la encimera")]),
  r("taps",[g("extender",["extender","poner"]),p("un mantel")]),
  r("taps",[g("servir",["servir"]),p("un capuchino en la barra")]),
  r("nouns",[p("la"),g("plantilla",["plantilla","personal"])]),
  r("answer",[p("está extendiendo un"),g("mantel",["mantel"]),p("blanco")])],
 notes="Tap 1 box also covers the final group pose where the chef only stands arm in arm; the phrase describes the opening frames where he wipes the pass with a cloth. 'la plantilla' is fine for restaurant staff in Spain; 'el personal' is equally common (accepted in the noun row). The 'staff' pill sits on the waitress inside the posing group. Barman = 'el camarero de la barra' (Spain says camarero, not barman).")
D[230]=dict(level="B",keyWord="el director de cine",
 taps=[t("dar indicaciones al actor","la directora","female"),t("llevar un disfraz de pirata","el actor","male"),t("estar montada sobre un trípode","la cámara de cine","female")],
 nouns=[n("la directora de cine"),n("la cámara de cine"),n("la silla plegable"),n("el sol")],
 question="¿Qué hace la directora?",answer="La directora levanta los puños en señal de victoria.".split(),answerVoice="female",
 recall=[r("taps",[p("dar"),g("indicaciones",["indicaciones","instrucciones"]),p("al actor")]),
  r("taps",[p("llevar un"),g("disfraz",["disfraz"]),p("de pirata")]),
  r("taps",[p("estar montada sobre un"),g("trípode",["trípode"])]),
  r("nouns",[p("la"),g("directora",["directora","realizadora"]),p("de cine")]),
  r("answer",[p("levanta los"),g("puños",["puños","brazos"]),p("en señal de victoria")])],
 notes="KEY WORD: the director is a woman, so the noun is 'la directora de cine' (feminine of the database word 'el director de cine'); proposal: the concept keeps 'el director de cine', the female form is accepted. Tap 1 box covers the whole clip, where she mostly gives the actor directions (gestures, demonstrates, points); she raises her fists only at the end, so phrase 1 is 'dar indicaciones al actor' (question/answer keep the fists).")
D[7119]=dict(level="B",keyWord="el pescador",
 taps=[t("subir una red a bordo","la chica","female"),t("llevar ropa impermeable amarilla","el hombre","male"),t("rebosar de peces plateados","la red","female")],
 nouns=[n("la gaviota"),n("la red"),n("la caja"),n("la pescadora")],
 question="¿Qué hace la pescadora de naranja?",answer="La pescadora arrastra una red llena de peces.".split(),answerVoice="female",
 recall=[r("taps",[g("subir",["subir","izar"]),p("una red a bordo")]),
  r("taps",[p("llevar ropa"),g("impermeable",["impermeable"]),p("amarilla")]),
  r("taps",[g("rebosar",["rebosar"]),p("de peces plateados")]),
  r("nouns",[p("la"),g("pescadora",["pescadora"])]),
  r("answer",[g("arrastra",["arrastra","sube"]),p("una red llena de peces")])],
 notes="KEY WORD: the fisher is a woman, so the noun and the answer use 'la pescadora' (feminine of the database word 'el pescador'); proposal: accept the female form for this concept.")
D[4930]=dict(level="B",keyWord="la recompensa",
 taps=[t("levantar la mano con entusiasmo","la alumna","female"),t("enseñar su cuaderno con orgullo","la alumna","female"),t("relucir sobre la hoja","la estrella dorada","female")],
 nouns=[n("la estrella dorada"),n("el cuaderno de espiral"),n("la pizarra blanca")],
 question="¿Qué recompensa recibe la alumna?",answer="La alumna recibe una estrella dorada como recompensa.".split(),answerVoice="female",
 recall=[r("taps",[g("levantar",["levantar","alzar"]),p("la mano con entusiasmo")]),
  r("taps",[p("enseñar su"),g("cuaderno",["cuaderno","libreta"]),p("con orgullo")]),
  r("taps",[g("relucir",["relucir","brillar"]),p("sobre la hoja")]),
  r("answer",[p("recibe una estrella dorada como"),g("recompensa",["recompensa","premio"])])],
 notes="Taps 1 and 2 share the same box on the girl over the whole clip (mostly writing); phrase 1 is for the hand-raise moment, phrase 2 for the final shot where she holds the notebook up. The key word is not a noun of the set, so no noun row; it is gapped in the answer row.")
D[5358]=dict(level="B",keyWord="asomarse",
 taps=[t("asomarse entre los libros","la chica de la rebeca","female"),t("apilar libros pesados","la chica de la rebeca","female"),t("apoyar la cabeza en la mano","la chica de la izquierda","female")],
 nouns=[n("las estanterías"),n("las gafas"),n("la rebeca"),n("el libro de texto")],
 question="¿Qué está haciendo la chica escondida?",answer="La chica se asoma por un hueco entre los libros.".split(),answerVoice="female",
 recall=[r("taps",[g("asomarse",["asomarse"]),p("entre los libros")]),
  r("taps",[g("apilar",["apilar","amontonar"]),p("libros pesados")]),
  r("taps",[p("apoyar la"),g("cabeza",["cabeza","barbilla"]),p("en la mano")]),
  r("answer",[p("se asoma por un"),g("hueco",["hueco"]),p("entre los libros")])],
 notes="Taps 1 and 2 share one box on the woman for the whole clip; the opening frames show her writing, so phrase 1 fits the final frames (eyes over the book wall) and phrase 2 the middle. 'la rebeca' is the everyday Spain word for a cardigan. Key word is a verb, so no noun row.")
for i,d in D.items():
  out={"mediaId":i,"lang":"es","level":d["level"],"keyWord":d["keyWord"],"taps":d["taps"],"nouns":d["nouns"],"question":d["question"],"answer":d["answer"],"answerVoice":d["answerVoice"],"carousel":[],"recall":d["recall"],"notes":d["notes"]}
  json.dump(out,open(f"content/es/{i}.json","w"),ensure_ascii=False,indent=1)
