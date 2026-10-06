import json
def g(t,acc=None): return {"text":t,"gap":True,"accept":acc or [t]}
def p(t): return {"text":t}
D={
288:dict(level="A",keyWord="la moda",
 taps=[("llevar un traje blanco","la mujer","female"),("hacer una foto","el hombre","male"),("llevar un jersey gris","el perro","female")],
 nouns=[("los árboles","female"),("la mujer","female"),("el hombre","male"),("el perro","female")],
 question="¿Qué llevan las dos personas?",answer="Llevan unos trajes muy grandes.",av="female",
 recall=[("taps",[p("llevar un"),g("traje"),p("blanco")]),("taps",[g("hacer",["hacer","sacar"]),p("una foto")]),("taps",[p("llevar un"),g("jersey"),p("gris")]),("answer",[p("Llevan unos trajes muy"),g("grandes")])],
 notes="Key word 'la moda' is abstract and is not named naturally by any thing in the clip; not forced into the texts. Phrase 2: the man takes photos only in the first boxed frames; in most boxed frames he walks next to the woman - 'hacer una foto' kept as the English (only he holds a phone). The woman's suit is cream: 'blanco' as in English."),
242:dict(level="A",keyWord="el vestido",
 taps=[("colgar de una percha","el vestido","female"),("dar vueltas sin parar","la chica","female"),("aplaudir a la chica","el hombre","male")],
 nouns=[("los limones","female"),("el hombre","male"),("el vestido","female"),("el espejo","female")],
 question="¿Qué hace la chica?",answer="Da vueltas con un vestido rojo.",av="female",
 recall=[("taps",[p("colgar de una"),g("percha")]),("taps",[p("dar"),g("vueltas"),p("sin parar")]),("taps",[g("aplaudir"),p("a la chica")]),("answer",[p("Da vueltas con un"),g("vestido"),p("rojo")])],
 notes="Phrase 2: in the first boxed frames the woman walks out of the door before she spins; phrase written for the spinning (most boxed frames)."),
868:dict(level="A",keyWord="la ola",
 taps=[("crecer cada vez más","la ola","female"),("llevar una camiseta blanca","la mujer","female"),("llevar una camiseta oscura","el hombre","male")],
 nouns=[("la ola","female"),("la mujer","female"),("el hombre","male"),("la arena","female")],
 question="¿Qué hacen las dos personas?",answer="Escapan corriendo de una ola grande.",av="female",
 recall=[("taps",[g("crecer"),p("cada vez más")]),("taps",[p("llevar una"),g("camiseta"),p("blanca")]),("taps",[p("llevar una camiseta"),g("oscura",["oscura","negra"])]),("answer",[p("Escapan corriendo de una"),g("ola"),p("grande")])],
 notes="Phrase 1: the wave grows in the first half; in the later boxed frames it has broken and a wave stands behind them on the shore. The man's top is a dark long-sleeved shirt: 'camiseta oscura'."),
4015:dict(level="A",keyWord="la orilla",
 taps=[("saltar por encima del agua","la oveja que salta","male"),("vigilar a las ovejas","el perro","male"),("ser alto y delgado","el árbol","male")],
 nouns=[("el árbol","male"),("el perro","male"),("la orilla","male"),("el agua","male")],
 question="¿Qué hacen las ovejas?",answer="Saltan de una orilla a la otra.",av="male",
 recall=[("taps",[p("saltar por encima del"),g("agua")]),("taps",[g("vigilar",["vigilar","mirar"]),p("a las ovejas")]),("taps",[p("ser alto y"),g("delgado",["delgado","fino"])]),("answer",[p("Saltan de una"),g("orilla"),p("a la otra")])],
 notes="Answer uses the key word ('de una orilla a la otra') instead of repeating phrase 1."),
291:dict(level="A",keyWord="el campo",
 taps=[("abrir mucho los brazos","la chica","female"),("correr detrás de la chica","el chico","male"),("estar en fila","los árboles","female")],
 nouns=[("el cielo","female"),("los árboles","female"),("el campo","female"),("el camino","female")],
 question="¿Qué hace la chica?",answer="Corre por un campo de trigo.",av="female",
 recall=[("taps",[p("abrir mucho los"),g("brazos")]),("taps",[g("correr"),p("detrás de la chica")]),("taps",[p("estar en"),g("fila")]),("answer",[p("Corre por un"),g("campo"),p("de trigo")])],
 notes="Phrase 1/2: in the early boxed frames the couple walks side by side; written for the running shots (arms open, man behind her). 'el chico/la chica' used for the young couple."),
}
for i,d in D.items():
    out={"mediaId":i,"lang":"es","level":d["level"],"keyWord":d["keyWord"],
     "taps":[{"phrase":a,"target":b,"voice":c} for a,b,c in d["taps"]],
     "nouns":[{"word":a,"voice":b} for a,b in d["nouns"]],
     "question":d["question"],"answer":d["answer"].split(),"answerVoice":d["av"],"carousel":[],
     "recall":[{"from":f,"parts":ps} for f,ps in d["recall"]],"notes":d["notes"]}
    json.dump(out,open(f"content/es/{i}.json","w"),ensure_ascii=False,indent=1)
