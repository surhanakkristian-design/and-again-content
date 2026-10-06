import json
def g(t,acc=None): return {"text":t,"gap":True,"accept":acc or [t]}
def p(t): return {"text":t}
def tap(ph,tg,v): return {"phrase":ph,"target":tg,"voice":v}
def n(w,v): return {"word":w,"voice":v}
def ans(s): return s.split()
D={}
D[587]=dict(level="B",keyWord="el disco",
 taps=[tap("soltar el disco","el árbitro","male"),tap("celebrar su gol","la jugadora de amarillo","female"),tap("colarse en la portería","el disco","female")],
 nouns=[n("el disco","female"),n("el guante","female"),n("el casco","female"),n("la camiseta","female")],
 question="¿Qué está haciendo la jugadora de amarillo?",answer=ans("Está celebrando su gol."),answerVoice="female",
 recall=[{"from":"taps","parts":[p("soltar el"),g("disco")]},
         {"from":"taps","parts":[p("celebrar su"),g("gol")]},
         {"from":"taps","parts":[g("colarse",["colarse","meterse","entrar"]),p("en la portería")]},
         {"from":"answer","parts":[p("Está"),g("celebrando",["celebrando","festejando"]),p("su gol")]}],
 notes="Spain hockey usage: el disco (puck), la portería (net/goal). Answer drops the subject (Está celebrando...). Tap 1 box also covers close-ups where the referee only holds the puck up; phrase written for the drop (face-off).")
D[7069]=dict(level="B",keyWord="llegar conduciendo",
 taps=[tap("quitarse el sombrero de paja","el hombre","male"),tap("estar de pie en el umbral","la joven","female"),tap("asomarse a la ventana","la anciana","female")],
 nouns=[n("el tractor","male"),n("los girasoles","male"),n("el sombrero de paja","male"),n("la grava","male")],
 question="¿Qué hace el hombre?",answer=ans("Llega conduciendo un tractor rojo."),answerVoice="male",
 recall=[{"from":"taps","parts":[p("quitarse el"),g("sombrero"),p("de paja")]},
         {"from":"taps","parts":[p("estar de pie en el"),g("umbral")]},
         {"from":"taps","parts":[g("asomarse"),p("a la ventana")]},
         {"from":"answer","parts":[p("Llega"),g("conduciendo"),p("un tractor rojo")]}],
 notes="Key word 'llegar conduciendo' is a paraphrase, not a dictionary entry; used naturally in the answer. Answer drops the subject; question in simple present (natural es for an ongoing action). 'quitarse el sombrero' = lifting the hat off in greeting, as shown.")
D[7761]=dict(level="B",keyWord="el ser",
 taps=[tap("meterse en un tarro","el pulpo","male"),tap("sujetar un portapapeles","el hombre","male"),tap("echarse a reír","la mujer","female")],
 nouns=[n("el pulpo","male"),n("el tarro","male"),n("los robots","male"),n("el portapapeles","male")],
 question="¿Qué hace el pulpo?",answer=ans("Se mete en un tarro de cristal."),answerVoice="male",
 recall=[{"from":"taps","parts":[p("meterse en un"),g("tarro",["tarro","bote"])]},
         {"from":"taps","parts":[p("sujetar un"),g("portapapeles")]},
         {"from":"taps","parts":[p("echarse a"),g("reír")]},
         {"from":"answer","parts":[p("Se"),g("mete",["mete","cuela"]),p("en un tarro de cristal")]}],
 notes="keyWord 'el ser' on its own mostly means 'being' in the abstract/philosophical sense; for 'a living thing that can act by itself' Spain says 'el ser vivo'. Proposal: keyWord 'el ser vivo'. The key word is not in the noun set and is not forced into the texts.")
D[5626]=dict(level="B",keyWord="estar averiado",
 taps=[tap("arrodillarse en la acera","el hombre","male"),tap("sentarse entre las naranjas","el gato","male"),tap("rodar por la acera","la naranja suelta","male")],
 nouns=[n("el gato","male"),n("el tranvía","male"),n("el robot de reparto","male"),n("los aerogeneradores","male")],
 question="¿Qué hay dentro del robot de reparto?",answer=ans("Hay un gato sentado entre las naranjas."),answerVoice="male",
 recall=[{"from":"taps","parts":[g("arrodillarse"),p("en la acera")]},
         {"from":"taps","parts":[p("sentarse entre las"),g("naranjas")]},
         {"from":"taps","parts":[g("rodar"),p("por la acera")]},
         {"from":"answer","parts":[p("Hay un"),g("gato"),p("sentado entre las naranjas")]}],
 notes="Answer is an existential 'Hay...' sentence (what a native says); it has no subject, so the recall row is the whole sentence. Key word 'estar averiado': the clip shows the robot with its lid open and a cat inside, not clearly a broken machine (same issue as English). Last tap-1 frame shows the man sitting down; phrase written for the kneeling in most boxes.")
D[7929]=dict(level="B",keyWord="el aparcamiento",
 taps=[tap("aplastar dos coches pequeños","el camión monstruo","male"),tap("levantar los dos puños","el chico del camión","male"),tap("cruzarse de brazos","la mujer de delante","female")],
 nouns=[n("el camión monstruo","male"),n("el coche rojo","male"),n("la plaza de aparcamiento","male"),n("las botas","male")],
 question="¿Qué está haciendo el camión monstruo?",answer=ans("Está aplastando dos coches aparcados."),answerVoice="male",
 recall=[{"from":"taps","parts":[g("aplastar",["aplastar"]),p("dos coches pequeños")]},
         {"from":"taps","parts":[p("levantar los dos"),g("puños")]},
         {"from":"taps","parts":[g("cruzarse"),p("de brazos")]},
         {"from":"nouns","parts":[p("la plaza de"),g("aparcamiento")]},
         {"from":"answer","parts":[p("Está aplastando dos coches"),g("aparcados")]}],
 notes="'el aparcamiento' in Spain mainly means the car park (shown) and also the act of parking; noun 3 'la plaza de aparcamiento' carries the key word, so the noun row gaps it. 'el camión monstruo' is the usual Spanish term (some say 'monster truck').")
for i,d in D.items():
    o={"mediaId":i,"lang":"es","level":d["level"],"keyWord":d["keyWord"],"taps":d["taps"],"nouns":d["nouns"],"question":d["question"],
       "answer":d["answer"],"answerVoice":d["answerVoice"],"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(o,open(f"content/es/{i}.json","w"),ensure_ascii=False,indent=2)
