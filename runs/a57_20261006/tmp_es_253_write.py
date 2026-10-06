import json
def g(t,acc=None): return {"text":t,"gap":True,"accept":acc or [t]}
def p(t): return {"text":t}
T=lambda ph,t,v:dict(phrase=ph,target=t,voice=v)
N=lambda w,v:dict(word=w,voice=v)
D={}
D[253]=dict(mediaId=253,lang="es",level="A",keyWord="quitar el polvo",
 taps=[T("quitar el polvo de la puerta","el hombre","male"),T("llevar un pañuelo gris","la mujer","female"),T("andar por la estantería","el gato","male")],
 nouns=[N("el gato","male"),N("los libros","male"),N("la estantería","male"),N("la lámpara","male")],
 question="¿Qué hace el hombre?",answer=["Quita","el","polvo","de","la","puerta."],answerVoice="male",carousel=[],
 recall=[dict(**{"from":"taps"},parts=[p("quitar el"),g("polvo"),p("de la puerta")]),
         dict(**{"from":"taps"},parts=[p("llevar un"),g("pañuelo"),p("gris")]),
         dict(**{"from":"taps"},parts=[p("andar por la"),g("estantería")]),
         dict(**{"from":"answer"},parts=[g("Quita",["Quita","Limpia"]),p("el polvo de la puerta")])],
 notes="Key word 'quitar el polvo' used in tap 1 and the answer. The man wipes the top of the door frame ('de la puerta' kept simple for level A instead of 'del marco'). The man's box also covers the gasp, dust cloud and thumbs-up moments, which the woman shares; the door moment is the distinctive one. Grey hijab -> 'pañuelo gris'. Answer drops the subject, so the answer row is the whole sentence; it differs from tap 1 by the gapped word (verb vs noun). No noun row: key word is not a noun.")
D[254]=dict(mediaId=254,lang="es",level="A",keyWord="la Tierra",
 taps=[T("parar el globo terráqueo","la mujer","female"),T("tener el pelo oscuro y rizado","el hombre","male"),T("dormir junto a la ventana","el gato","female")],
 nouns=[N("el sol","female"),N("el mar","female"),N("el gato","female"),N("el globo terráqueo","female")],
 question="¿Qué hace el gato?",answer=["El","gato","duerme","junto","a","la","ventana."],answerVoice="female",carousel=[],
 recall=[dict(**{"from":"taps"},parts=[g("parar",["parar","detener"]),p("el globo terráqueo")]),
         dict(**{"from":"taps"},parts=[p("tener el"),g("pelo"),p("oscuro y rizado")]),
         dict(**{"from":"taps"},parts=[p("dormir junto a la"),g("ventana")]),
         dict(**{"from":"answer"},parts=[g("duerme"),p("junto a la ventana")])],
 notes="Key word 'la Tierra' appears in no exercise: the clip shows a desk globe ('el globo terráqueo', literally the earth globe), and no English noun or phrase names the planet; proposal: owner may accept as is. The woman's box mostly shows her pointing at the globe (the man points too), so the distinctive stopping of the turning globe is kept. 'el globo terráqueo' is used in tap 1 and the noun for the same thing.")
D[255]=dict(mediaId=255,lang="es",level="A",keyWord="el este",
 taps=[T("señalar el horizonte","la mujer","female"),T("salir por el este","el sol","female"),T("levantar las tazas","la gente","female")],
 nouns=[N("el cielo","female"),N("el sol","female"),N("la gente","female"),N("las rocas","female")],
 question="¿Qué hace el sol?",answer=["El","sol","sale","sobre","las","nubes."],answerVoice="female",carousel=[],
 recall=[dict(**{"from":"taps"},parts=[g("señalar"),p("el horizonte")]),
         dict(**{"from":"taps"},parts=[p("salir por el"),g("este")]),
         dict(**{"from":"taps"},parts=[p("levantar las"),g("tazas")]),
         dict(**{"from":"answer"},parts=[g("sale"),p("sobre las nubes")])],
 notes="The woman points at the red stripe on the horizon, not up at the sky: 'señalar el horizonte'. The people's box covers the whole group standing and watching; they raise their mugs only at the end, but standing/watching is not distinctive, so the English action is kept ('las tazas' = mugs). 'people' -> 'la gente' (collective singular, the everyday word). Key word 'el este' in tap 2 ('salir por el este', the natural Spanish collocation).")
D[256]=dict(mediaId=256,lang="es",level="A",keyWord="comer",
 taps=[T("oler la sopa de fideos","la chica","female"),T("tener barba oscura","el hombre","male"),T("cocinar en la calle","la cocinera","female")],
 nouns=[N("el cartel","female"),N("la barba","female"),N("los cuencos","female"),N("los vaqueros","female")],
 question="¿Qué comen el hombre y la chica?",answer=["Comen","sopa","de","fideos","caliente."],answerVoice="female",carousel=[],
 recall=[dict(**{"from":"taps"},parts=[g("oler"),p("la sopa de fideos")]),
         dict(**{"from":"taps"},parts=[p("tener"),g("barba"),p("oscura")]),
         dict(**{"from":"taps"},parts=[p("cocinar en la"),g("calle")]),
         dict(**{"from":"answer"},parts=[g("Comen",["Comen","Toman"]),p("sopa de fideos caliente")])],
 notes="Key word 'comer' is in the question and the answer (gapped in the answer row). The young woman smells the soup only at the start; for most of her box she eats, but the man eats too, so the English action is kept. Soup = 'sopa de fideos' in tap 1 and the answer. The cook is a woman -> 'la cocinera'. 'young woman' -> 'la chica' (target and question). Answer drops the subject 'Ellos' as natives do, so the answer row is the whole sentence.")
D[258]=dict(mediaId=258,lang="es",level="B",keyWord="el borde",
 taps=[T("caminar en equilibrio sobre tablones estrechos","la persona del pelo azul","female"),T("lucir una barba pelirroja","el hombre","male"),T("cubrir el césped","la lona","female")],
 nouns=[N("los pinos","female"),N("las rocas","female"),N("el lago","female"),N("los tablones","female")],
 question="¿Qué hace la persona del pelo azul?",answer=["Camina","en","equilibrio","sobre","unos","tablones","estrechos."],answerVoice="female",carousel=[],
 recall=[dict(**{"from":"taps"},parts=[p("caminar en"),g("equilibrio"),p("sobre tablones estrechos")]),
         dict(**{"from":"taps"},parts=[g("lucir",["lucir","tener","llevar"]),p("una barba pelirroja")]),
         dict(**{"from":"taps"},parts=[p("cubrir el"),g("césped")]),
         dict(**{"from":"answer"},parts=[p("Camina en equilibrio sobre unos"),g("tablones",["tablones","tablas"]),p("estrechos")])],
 notes="Key word 'el borde' appears in no exercise: no English noun or phrase names the edge (the clip shows a finger on the table edge = 'el borde de la mesa', and the person stopping at the end of the dock = 'el borde del muelle'); proposal: owner may accept as is, or a phrase like 'llegar al borde del muelle' if the frame may change. The person's box also covers the opening shots of the plaid-sleeved hand on the table edge and the rope; walking along the dock planks is most of the boxed frames and kept. Level B words: caminar en equilibrio, tablones, lucir, pelirroja, césped, lona. Answer drops the subject, so the answer row is the whole sentence; it differs from tap 1 by the gapped word.")
for k,v in D.items():
    json.dump(v,open(f"content/es/{k}.json","w"),ensure_ascii=False,indent=2)
