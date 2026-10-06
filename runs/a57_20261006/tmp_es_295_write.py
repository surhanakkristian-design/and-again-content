import json
def P(*parts):
    out=[]
    for p in parts:
        if isinstance(p,tuple): out.append({"text":p[0],"gap":True,"accept":list(p[1])})
        else: out.append({"text":p})
    return out
def T(ph,tg,v): return {"phrase":ph,"target":tg,"voice":v}
def N(w,v): return {"word":w,"voice":v}
D={}
D[295]=dict(level="A",keyWord="mezclar",
 taps=[T("mezclar la pasta espesa","la mano","male"),T("sujetar un mango negro","la mano","male"),T("estar pegada al suelo","la cinta adhesiva","male")],
 nouns=[N("la cinta adhesiva","male"),N("el cubo","male"),N("la mano","male"),N("el zapato","male")],
 question="¿Qué está haciendo la mano?",answer="La mano está mezclando la pasta espesa.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":P(("mezclar",["mezclar","remover"]),"la pasta espesa")},
         {"from":"taps","parts":P("sujetar un",("mango",["mango"]),"negro")},
         {"from":"taps","parts":P("estar pegada al",("suelo",["suelo"]))},
         {"from":"answer","parts":P("está mezclando la",("pasta",["pasta","masa"]),"espesa")}],
 notes="Two work boots are visible; 'el zapato' kept singular at the English slot (one boot).")
D[296]=dict(level="A",keyWord="el pescado",
 taps=[T("sujetar medio limón","el hombre","male"),T("comer con tenedor","la mujer","female"),T("estar en una tabla de madera","el pescado","female")],
 nouns=[N("el mar","female"),N("la barca","female"),N("el pescado","female"),N("el fuego","female")],
 question="¿Qué está comiendo la mujer?",answer="Está comiendo pescado con tenedor.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":P("sujetar medio",("limón",["limón"]))},
         {"from":"taps","parts":P(("comer",["comer"]),"con tenedor")},
         {"from":"taps","parts":P("estar en una",("tabla",["tabla"]),"de madera")},
         {"from":"answer","parts":P("Está comiendo",("pescado",["pescado"]),"con tenedor")}],
 notes="Blue box (fish): about 9 frames over the fire, about 12 on the wooden board after cooking, so phrase 3 = 'estar en una tabla de madera' (English 'to lie over the fire' fits fewer boxed frames). The half lemon also sits on the board in two frames. Answer drops the subject (natural in es).")
D[297]=dict(level="A",keyWord="la pesca",
 taps=[T("sujetar una caña de pescar","el hombre","male"),T("sujetar una red","la mujer","female"),T("nadar en el lago","el pez","male")],
 nouns=[N("el pez","male"),N("la red","male"),N("la gorra","male"),N("los árboles","male")],
 question="¿Qué están haciendo el hombre y la mujer?",answer="Están pescando en el lago.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":P("sujetar una",("caña",["caña"]),"de pescar")},
         {"from":"taps","parts":P("sujetar una",("red",["red"]))},
         {"from":"taps","parts":P(("nadar",["nadar"]),"en el lago")},
         {"from":"answer","parts":P("Están",("pescando",["pescando"]),"en el lago")}],
 notes="Live fish = 'el pez' (not 'el pescado'). Key word 'la pesca' appears only as the verb 'pescar/pescando'. Landing net = 'la red' (A-level; 'el salabre' is too rare). Fish box: in two frames the fish is held in hands, not swimming.")
D[298]=dict(level="B",keyWord="el probador",
 taps=[T("probarse varios conjuntos","la mujer rubia","female"),T("valorar los conjuntos con el pulgar","la mujer morena","female"),T("estar tumbado en el mostrador","el perro","female")],
 nouns=[N("la cortina","female"),N("el montón de ropa","female"),N("las sandalias","female"),N("el perro","female")],
 question="¿Qué está haciendo la mujer rubia?",answer="Se está probando conjuntos en el probador.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":P("probarse varios",("conjuntos",["conjuntos","modelitos"]))},
         {"from":"taps","parts":P(("valorar",["valorar","juzgar"]),"los conjuntos con el pulgar")},
         {"from":"taps","parts":P("estar tumbado en el",("mostrador",["mostrador"]))},
         {"from":"answer","parts":P("Se está probando conjuntos en el",("probador",["probador"]))}],
 notes="Phrase 2: the dark-haired woman gives thumbs down to the first outfits and thumbs up to the last; most boxed frames show her bored or thumbs down, so 'valorar los conjuntos con el pulgar' instead of 'levantar el pulgar'. Answer drops the subject; clitic order 'Se está probando' (alternative 'Está probándose' needs different chips).")
D[299]=dict(level="A",keyWord="despertar",
 taps=[T("dormir en la cama","la mujer","female"),T("andar por la cama","el perro","female"),T("taparse la cara","la mujer","female")],
 nouns=[N("la almohada","female"),N("el perro","female"),N("la manta","female"),N("la puerta","female")],
 question="¿Qué está haciendo el perro?",answer="El perro la está despertando.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":P(("dormir",["dormir"]),"en la cama")},
         {"from":"taps","parts":P(("andar",["andar","caminar"]),"por la cama")},
         {"from":"taps","parts":P("taparse la",("cara",["cara"]))},
         {"from":"answer","parts":P("la está",("despertando",["despertando"]))}],
 notes="Phrase 3 'taparse la cara' only in the last frames; boxes 1 and 3 share the woman's region. Answer voice kept female as in English though 'el perro' is masculine.")
for i,d in D.items():
    o={"mediaId":i,"lang":"es","level":d["level"],"keyWord":d["keyWord"],"taps":d["taps"],"nouns":d["nouns"],"question":d["question"],
       "answer":d["answer"],"answerVoice":d["answerVoice"],"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(o,open(f"content/es/{i}.json","w"),ensure_ascii=False,indent=1)
