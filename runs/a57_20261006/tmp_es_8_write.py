import json
def row(frm,*ps):
    out=[]
    for p in ps:
        if isinstance(p,tuple): out.append({"text":p[0],"gap":True,"accept":list(p)})
        else: out.append({"text":p})
    return {"from":frm,"parts":out}
def T(p,t,v="female"): return {"phrase":p,"target":t,"voice":v}
def N(w,v="female"): return {"word":w,"voice":v}
D={}
D[8]=dict(level="B",keyWord="la tarjeta llave",
 taps=[T("acercar la tarjeta al lector","la mujer"),T("encenderse en verde","el lector de tarjetas"),T("quedarse entreabierta","la puerta")],
 nouns=[N("la puerta"),N("el lector de tarjetas"),N("la tarjeta llave"),N("la manilla")],
 question="¿Qué está haciendo la mujer?",
 answer="Está abriendo la puerta con la tarjeta llave.".split(),
 recall=[row("taps","acercar la",("tarjeta",),"al lector"),row("taps",("encenderse","ponerse"),"en verde"),
   row("taps","quedarse",("entreabierta",)),row("answer","Está abriendo la",("puerta",),"con la tarjeta llave")],
 notes="Phrase 1: the English red box ('to wheel a suitcase') shows the suitcase only in the corridor frames; in most boxed frames the woman's hand holds/taps the card at the reader, so 'acercar la tarjeta al lector'. Phrase 3: the door is shown opened part-way, hence 'quedarse entreabierta' (B2). Handle = 'la manilla' (Spain, lever handle). Answer subject dropped (natural es).")
D[9]=dict(level="B",keyWord="el laboratorio",
 taps=[T("enfundarse los guantes morados","la científica"),T("examinar un tubo de ensayo","la científica"),T("mantener congeladas las muestras","el congelador")],
 nouns=[N("las gafas de protección"),N("los tubos de ensayo"),N("la bata de laboratorio"),N("el congelador")],
 question="¿Qué está haciendo la científica?",
 answer="Está guardando los tubos de ensayo en el congelador.".split(),
 recall=[row("taps","enfundarse los",("guantes",),"morados"),row("taps",("examinar","observar"),"un tubo de ensayo"),
   row("taps","mantener congeladas las",("muestras",)),row("answer","Está guardando los tubos de ensayo en el",("congelador",))],
 notes="Phrase 2: the green box also covers pipetting, writing and freezer frames; 'examinar un tubo de ensayo' is the close-up where she looks at the tube. Key word 'el laboratorio' is not one of the four nouns; it appears inside 'la bata de laboratorio', so no noun recall row. Answer subject dropped (natural es).")
D[11]=dict(level="A",keyWord="la biblioteca",
 taps=[T("llevar un bolso grande","la mujer"),T("caminar entre las estanterías","la mujer"),T("ser alta y redonda","la torre de libros")],
 nouns=[N("los libros"),N("el pelo"),N("el abrigo"),N("el bolso")],
 question="¿Qué está haciendo la mujer?",
 answer="Está mirando los libros.".split(),
 recall=[row("taps","llevar un",("bolso",),"grande"),row("taps","caminar entre las",("estanterías",)),
   row("taps","ser alta y",("redonda",)),row("answer","Está",("mirando",),"los libros")],
 notes="Key word 'la biblioteca' is not among the nouns and fits no tap target, so no recall row can gap it. Answer simplifies 'looking up at' to 'mirando' (A level); she looks up at the shelves. 'estanterías' is A2.")
D[12]=dict(level="A",keyWord="abrazar",
 taps=[T("tener el pelo corto","el hombre","male"),T("tener el pelo largo","la mujer"),T("brillar en el cielo","el sol")],
 nouns=[N("el sol"),N("el hombre","male"),N("la mujer"),N("la hierba")],
 question="¿Qué están haciendo el hombre y la mujer?",
 answer="Se están abrazando en la hierba.".split(),
 recall=[row("taps","tener el pelo",("corto",)),row("taps","tener el",("pelo",),"largo"),
   row("taps",("brillar",),"en el cielo"),row("answer","Se están",("abrazando",),"en la hierba")],
 notes="Rows 1 and 2 gap different words ('corto' / 'pelo') so they do not look the same once blanked. Answer has no subject (natural es); key word gapped in the answer row.")
D[14]=dict(level="A",keyWord="la página",
 taps=[T("abrir un cuaderno","las manos"),T("ser amarilla","la flor"),T("pasar por las hojas verdes","el pincel")],
 nouns=[N("la página"),N("la flor"),N("el pincel"),N("la mesa")],
 question="¿Qué hay en la página?",
 answer="Hay una flor amarilla en la página.".split(),
 recall=[row("taps","abrir un",("cuaderno",)),row("taps","ser",("amarilla",)),
   row("taps","pasar por las",("hojas",),"verdes"),row("answer","Hay una flor amarilla en la",("página",))],
 notes="Phrase 1: the red box also covers frames where the fingers press the leaves and where the hands hold the notebook up; most boxed frames are the opening at the start, so 'abrir un cuaderno'. Phrase 3: the brush spreads glue over the leaves, so 'pasar por' (not 'pintar'). Answer 'Hay ...' has no subject: the row is the whole sentence; key word gapped there.")
for i,d in D.items():
    o={"mediaId":i,"lang":"es","level":d["level"],"keyWord":d["keyWord"],"taps":d["taps"],"nouns":d["nouns"],
       "question":d["question"],"answer":d["answer"],"answerVoice":"female","carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(o,open(f"content/es/{i}.json","w"),ensure_ascii=False,indent=1)
