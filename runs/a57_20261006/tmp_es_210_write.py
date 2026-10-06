import json
def P(*a):
    out=[]
    for x in a:
        if isinstance(x,tuple): out.append({"text":x[0],"gap":True,"accept":list(x[1:]) if len(x)>1 else [x[0]]})
        else: out.append({"text":x})
    for o in out:
        if o.get("gap") and o["accept"][0]!=o["text"]: o["accept"].insert(0,o["text"])
    return out
D={
210:dict(level="A",keyWord="el cliente",
 taps=[("probarse unos auriculares","la clienta","female"),("meter una caja en una bolsa","el dependiente","male"),("sujetar dos cajas","la clienta","female")],
 nouns=[("la clienta","female"),("la bolsa","female"),("la tarjeta","female"),("los auriculares","female")],
 q="¿Qué está haciendo la clienta?",a="Se está probando unos auriculares blancos.",av="female",
 recall=[("taps",P(("probarse",),"unos auriculares")),("taps",P("meter una caja en una",("bolsa",))),("taps",P("sujetar","dos",("cajas",))),
  ("nouns",P("la",("clienta","cliente"))),("answer",P("Se está probando unos",("auriculares","cascos"),"blancos"))],
 notes="Key word 'el cliente': the customer is a woman, so the noun pill uses the feminine 'la clienta' (same database concept). Tap 2: the man (shop assistant) puts the boxed headphones into the paper bag; 'meter una caja en una bolsa' says what he visibly does."),
211:dict(level="B",keyWord="la aduana",
 taps=[("registrar una maleta","el agente de aduanas","male"),("juntar las manos","la chica","female"),("estar cubierto de pinchos","el durián","female")],
 nouns=[("el durián","female"),("la maleta","female"),("la papelera","female"),("el agente de aduanas","male")],
 q="¿Qué está haciendo el agente de aduanas?",a="El agente de aduanas está registrando una maleta.",av="male",
 recall=[("taps",P("registrar","una",("maleta",))),("taps",P(("juntar",),"las manos")),("taps",P("estar cubierto de",("pinchos","espinas"))),
  ("answer",P("está",("registrando","inspeccionando"),"una maleta"))],
 notes="Key word 'la aduana' appears inside 'el agente de aduanas' (noun 4, question, answer). 'registrar una maleta' = B1 collocation for a customs search. Bin = 'la papelera' (metal bin, Spain usage)."),
212:dict(level="A",keyWord="el bailarín",
 taps=[("estirar la pierna","la bailarina","female"),("bailar en un estudio","la bailarina","female"),("sonreír a la cámara","la bailarina","female")],
 nouns=[("la bailarina","female"),("el espejo","female"),("el altavoz","female"),("el suelo","female")],
 q="¿Qué está haciendo la bailarina?",a="Está bailando en un estudio.",av="female",
 recall=[("taps",P("estirar la",("pierna",))),("taps",P(("bailar",),"en un estudio")),("taps",P(("sonreír",),"a la cámara")),
  ("nouns",P("la",("bailarina","bailarín"))),("answer",P("Está bailando en un",("estudio",)))],
 notes="Key word 'el bailarín': the dancer is a woman, so the noun pill and question use the feminine 'la bailarina' (same concept). Answer drops the subject (natural in Spain) to avoid 'la bailarina está bailando'."),
213:dict(level="A",keyWord="el baile",
 taps=[("cocinar en los fogones","la mujer","female"),("sujetar a la mujer","el hombre","male"),("llevar una falda larga","la mujer","female")],
 nouns=[("la mujer","female"),("el hombre","male"),("la radio","female"),("el suelo","female")],
 q="¿Qué están haciendo el hombre y la mujer?",a="Están bailando en la cocina.",av="female",
 recall=[("taps",P(("cocinar",),"en los fogones")),("taps",P(("sujetar",),"a la mujer")),("taps",P("llevar una",("falda",),"larga")),
  ("answer",P("Están",("bailando",),"en la cocina"))],
 notes="Key word 'el baile' (noun) is not one of the four pills, so no noun recall row; the answer uses the verb 'bailar'."),
214:dict(level="A",keyWord="peligroso",
 taps=[("caminar sobre el hielo","el niño","male"),("tirar de su amigo","la niña","female"),("romperse en pedazos","el hielo","male")],
 nouns=[("el cartel","male"),("el árbol","male"),("el niño","male"),("el hielo","male")],
 q="¿Qué está haciendo el niño?",a="El niño está caminando sobre hielo peligroso.",av="male",
 recall=[("taps",P(("caminar",),"sobre el hielo")),("taps",P(("tirar",),"de su amigo")),("taps",P("romperse en",("pedazos","trozos"))),
  ("answer",P("está caminando sobre hielo",("peligroso",)))],
 notes="Tap 1 box also covers moments where the boy stands frozen on the floes; phrase describes him stepping onto the ice. Tap 2: the girl pulls the boy back to the dock."),
}
for i,d in D.items():
    o={"mediaId":i,"lang":"es","level":d["level"],"keyWord":d["keyWord"],
       "taps":[{"phrase":p,"target":t,"voice":v} for p,t,v in d["taps"]],
       "nouns":[{"word":w,"voice":v} for w,v in d["nouns"]],
       "question":d["q"],"answer":d["a"].split(),"answerVoice":d["av"],"carousel":[],
       "recall":[{"from":f,"parts":p} for f,p in d["recall"]],"notes":d["notes"]}
    json.dump(o,open(f"content/es/{i}.json","w"),ensure_ascii=False,indent=1)
