import json
def P(*a):
    out=[]
    for x in a:
        if isinstance(x,tuple): out.append({"text":x[0],"gap":True,"accept":list(x[1])})
        else: out.append({"text":x})
    return out
def T(p,t,v): return {"phrase":p,"target":t,"voice":v}
def N(w,v): return {"word":w,"voice":v}
D={}
m,f="male","female"
D[21]=dict(keyWord="la escuela",
 taps=[T("abrir la puerta","la mano",m),T("estar sentados a las mesas","los estudiantes",m),T("tener muchas ventanas","el edificio de la escuela",m)],
 nouns=[N("el cielo",m),N("la escuela",m),N("el césped",m)],
 question="¿Qué están haciendo los estudiantes?",
 answer="Los estudiantes están sentados a las mesas.".split(),answerVoice=m,
 recall=[{"from":"taps","parts":P(("abrir",["abrir"]),"la puerta")},
  {"from":"taps","parts":P("estar",("sentados",["sentados"]),"a las mesas")},
  {"from":"taps","parts":P("tener muchas",("ventanas",["ventanas"]))},
  {"from":"nouns","parts":P("la",("escuela",["escuela","colegio"]))},
  {"from":"answer","parts":P("están sentados a las",("mesas",["mesas"]))}],
 notes="English 'grass' is a mowed lawn, so 'el césped' (the everyday word in Spain). In Spain a school building is often called 'el colegio'; the database word 'la escuela' is kept and 'colegio' is accepted in the noun row. Phrase 2 uses 'estar sentados' because the students are already seated in every boxed frame.")
D[22]=dict(keyWord="el científico",
 taps=[T("pasar por delante del póster","el estudiante",m),T("tomar notas","el científico",m),T("señalar una línea","el científico",m)],
 nouns=[N("el científico",m),N("las gafas",m),N("el bolígrafo",m),N("el póster",m)],
 question="¿Qué está haciendo el científico?",
 answer="El científico está tomando notas.".split(),answerVoice=m,
 recall=[{"from":"taps","parts":P("pasar por delante del",("póster",["póster","cartel"]))},
  {"from":"taps","parts":P("tomar",("notas",["notas","apuntes"]))},
  {"from":"taps","parts":P(("señalar",["señalar"]),"una línea")},
  {"from":"nouns","parts":P("el",("científico",["científico"]))},
  {"from":"answer","parts":P("está",("tomando",["tomando","escribiendo"]),"notas")}],
 notes="'tomar notas' is the natural collocation for English 'write some notes' (he writes on a clipboard). 'las gafas' = his safety glasses on the forehead.")
D[23]=dict(keyWord="el discurso",
 taps=[T("dar un discurso","la mujer de verde",f),T("beber un poco de agua","la mujer de verde",f),T("llevar un traje gris","el hombre de gris",m)],
 nouns=[N("las ventanas",f),N("la mujer",f),N("el micrófono",f),N("el vaso",f)],
 question="¿Qué está haciendo la mujer de verde?",
 answer="La mujer está dando un discurso.".split(),answerVoice=f,
 recall=[{"from":"taps","parts":P("dar un",("discurso",["discurso"]))},
  {"from":"taps","parts":P("beber un poco de",("agua",["agua"]))},
  {"from":"taps","parts":P("llevar un",("traje",["traje"]),"gris")},
  {"from":"answer","parts":P("está",("dando",["dando","pronunciando"]),"un discurso")}],
 notes="")
D[24]=dict(keyWord="la cuchara",
 taps=[T("abrir un cajón","la chica",f),T("coger una cuchara","la chica",f),T("tomar sopa","la chica",f)],
 nouns=[N("la ventana",f),N("la cuchara",f),N("el cuenco",f),N("la mesa",f)],
 question="¿Qué está haciendo la chica?",
 answer="La chica está tomando sopa con una cuchara.".split(),answerVoice=f,
 recall=[{"from":"taps","parts":P("abrir un",("cajón",["cajón"]))},
  {"from":"taps","parts":P("coger una",("cuchara",["cuchara"]))},
  {"from":"taps","parts":P(("tomar",["tomar","comer"]),"sopa")},
  {"from":"answer","parts":P("está tomando",("sopa",["sopa"]),"con una cuchara")}],
 notes="'tomar sopa' is how Spaniards say eating soup; 'comer' is accepted in the recall row. 'el cuenco' for the bowl ('el bol' is also common in Spain).")
D[25]=dict(keyWord="la grapadora",
 taps=[T("usar una grapadora roja","el hombre",m),T("levantar los papeles","el hombre",m),T("abrir la grapadora","el hombre",m)],
 nouns=[N("el hombre",m),N("la planta",m),N("la grapadora",m),N("los papeles",m)],
 question="¿Qué está haciendo el hombre?",
 answer="El hombre está usando una grapadora roja.".split(),answerVoice=m,
 recall=[{"from":"taps","parts":P("usar una",("grapadora",["grapadora"]),"roja")},
  {"from":"taps","parts":P(("levantar",["levantar"]),"los papeles")},
  {"from":"taps","parts":P(("abrir",["abrir"]),"la grapadora")},
  {"from":"answer","parts":P("está",("usando",["usando","utilizando"]),"una grapadora roja")}],
 notes="English 'paper' is a stack of sheets, so the plural 'los papeles' (more natural than mass 'el papel' for a pile) in both the phrase and the noun.")
for i,d in D.items():
    o={"mediaId":i,"lang":"es","level":"A",**{k:d[k] for k in ["keyWord","taps","nouns","question","answer","answerVoice"]},"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(o,open(f"content/es/{i}.json","w"),ensure_ascii=False,indent=1)
