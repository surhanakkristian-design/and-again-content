import json
def T(*parts):
    out=[]
    for p in parts:
        if isinstance(p,tuple): out.append({"text":p[0],"gap":True,"accept":list(p[1:]) if len(p)>1 else [p[0]]})
        else: out.append({"text":p})
    return out
def g(w,*alt): return (w,w)+alt
V={}
V[233]=dict(level="B",keyWord="dislocar",
 taps=[("agarrarse el hombro lesionado","el hombre","male"),("arrodillarse junto al escalador","la mujer","female"),("estar enrollada sobre la hierba","la cuerda","male")],
 nouns=[("el casco","male"),("el hombro","male"),("la chaqueta","male"),("la hierba","male")],
 question="¿Qué está haciendo el hombre?",answer="El hombre se está agarrando el hombro lesionado.",av="male",
 recall=[("taps",T("agarrarse el",g("hombro"),"lesionado")),("taps",T(g("arrodillarse"),"junto al escalador")),("taps",T("estar",g("enrollada"),"sobre la hierba")),
         ("answer",T("se está agarrando el hombro",g("lesionado","herido")))],
 notes="Key word 'dislocar' is not shown as such (fall + clutching the shoulder); not forced into the phrases. Phrase 1 box also covers the opening frames of the fall/landing; written for what the man does in most boxed frames.")
V[235]=dict(level="B",keyWord="traer",
 taps=[("traer de vuelta una pelota roja","el perro","female"),("rascarle la barriga al perro","la mujer","female"),("estar cargado de manzanas rojas","el manzano","female")],
 nouns=[("el manzano","female"),("la valla","female"),("el perro","female"),("el césped","female")],
 question="¿Qué está haciendo el perro?",answer="El perro está trayendo de vuelta una pelota roja.",av="female",
 recall=[("taps",T("traer de vuelta una",g("pelota","bola"),"roja")),("taps",T("rascarle la",g("barriga","tripa"),"al perro")),("taps",T("estar",g("cargado"),"de manzanas rojas")),
         ("answer",T("está",g("trayendo"),"de vuelta una pelota roja"))],
 notes="'traer' is A1; 'traer de vuelta' used so phrase and answer carry a B1 collocation. Phrase 2: rubbing a dog's belly is 'rascarle la barriga' in Spain. The dog's fetch box also covers frames where it only waits or lies on its back.")
V[237]=dict(level="A",keyWord="el burro",
 taps=[("abrir mucho la boca","el burro","male"),("rodar por el suelo","el burro","male"),("buscar comida","los pájaros","male")],
 nouns=[("las naranjas","male"),("la casa","male"),("el burro","male"),("los pájaros","male")],
 question="¿Qué está haciendo el burro?",answer="El burro está rodando por el suelo.",av="male",
 recall=[("taps",T("abrir mucho la",g("boca"))),("taps",T(g("rodar","revolcarse"),"por el suelo")),("taps",T(g("buscar"),"comida")),
         ("nouns",T("el",g("burro"))),("answer",T("está rodando por el",g("suelo")))],
 notes="Phrase 2: 'revolcarse' is the most natural verb but above A2; 'rodar por el suelo' used (revolcarse accepted in recall). Phrases 1 and 2 share the donkey as target as in English; the two boxes overlap, each phrase fits a different moment.")
V[238]=dict(level="A",keyWord="robar",
 taps=[("robar una lata","el hombre","male"),("llevar una bolsa blanca","el hombre","male"),("tener flores rosas","el arbusto","male")],
 nouns=[("el cielo","male"),("las flores","male"),("el césped","male"),("las latas","male")],
 question="¿Qué está haciendo el hombre?",answer="El hombre está robando una lata.",av="male",
 recall=[("taps",T("robar una",g("lata"))),("taps",T("llevar una",g("bolsa"),"blanca")),("taps",T("tener",g("flores"),"rosas")),
         ("answer",T("está",g("robando","cogiendo"),"una lata"))],
 notes="Noun 3 'grass' = the front lawn, so 'el césped' (A2, usual in Spain). Phrase 1 box also covers the approach and the run away; written for the theft.")
V[239]=dict(level="B",keyWord="dudar",
 taps=[("examinar un anillo de oro","el hombre","male"),("sonreír de oreja a oreja","la anciana","female"),("fruncir el ceño con desconfianza","el hombre","male")],
 nouns=[("el anillo","male"),("el pañuelo","male"),("la chaqueta","male"),("las nubes","male")],
 question="¿Qué está examinando el hombre?",answer="El hombre está examinando un anillo de oro.",av="male",
 recall=[("taps",T(g("examinar","observar"),"un anillo de oro")),("taps",T(g("sonreír"),"de oreja a oreja")),("taps",T("fruncir el",g("ceño"),"con desconfianza")),
         ("answer",T("está examinando un",g("anillo"),"de oro"))],
 notes="Key word 'dudar' not forced into the texts; phrase 3 expresses the doubt ('con desconfianza'). Headscarf = 'el pañuelo' (the usual word in Spain).")
for i,v in V.items():
    d={"mediaId":i,"lang":"es","level":v["level"],"keyWord":v["keyWord"],
       "taps":[{"phrase":p,"target":t,"voice":vo} for p,t,vo in v["taps"]],
       "nouns":[{"word":w,"voice":vo} for w,vo in v["nouns"]],
       "question":v["question"],"answer":v["answer"].split(" "),"answerVoice":v["av"],"carousel":[],
       "recall":[{"from":f,"parts":p} for f,p in v["recall"]],"notes":v["notes"]}
    json.dump(d,open(f"content/es/{i}.json","w"),ensure_ascii=False,indent=1)
