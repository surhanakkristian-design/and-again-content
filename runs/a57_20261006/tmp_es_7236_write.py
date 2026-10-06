import json
def P(*parts):
    out=[]
    for p in parts:
        if isinstance(p,tuple): out.append({"text":p[0],"gap":True,"accept":list(p[1])})
        else: out.append({"text":p})
    return out
def T(ph,tg,v): return {"phrase":ph,"target":tg,"voice":v}
def N(w,v="female"): return {"word":w,"voice":v}
D={}
D[7236]=dict(level="B",keyWord="el huracán",
 taps=[T("rebasar el muro","la ola","female"),T("doblarse por la fuerza del viento","las palmeras","female"),T("tener la lona de rayas","la tumbona","female")],
 nouns=[N("la palmera"),N("la tumbona"),N("el cubo"),N("las chanclas")],
 question="¿Qué están haciendo las olas?",answer="Las olas están rompiendo contra el muro.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":P(("rebasar",["rebasar","saltar"]),"el muro")},
  {"from":"taps","parts":P("doblarse por la fuerza del",("viento",["viento"]))},
  {"from":"taps","parts":P("tener la lona de",("rayas",["rayas"]))},
  {"from":"answer","parts":P("están",("rompiendo",["rompiendo"]),"contra el muro")}],
 notes="Key word 'el huracán' is not one of the nouns and appears in no exercise (the storm itself is not a tappable thing). Phrase 1 'rebasar el muro' (B2): in some boxed frames the wave only breaks against the wall rather than over it.")
D[859]=dict(level="B",keyWord="el armario",
 taps=[T("rebuscar entre los abrigos","la chica","female"),T("probarse un vestido por encima","la chica","female"),T("cerrar las hojas del armario","la chica","female")],
 nouns=[N("el armario"),N("los jerséis"),N("el abrigo"),N("el vestido")],
 question="¿Qué está haciendo la chica?",answer="La chica está rebuscando en el armario.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":P("rebuscar entre los",("abrigos",["abrigos"]))},
  {"from":"taps","parts":P("probarse un",("vestido",["vestido"]),"por encima")},
  {"from":"taps","parts":P("cerrar las hojas del",("armario",["armario"]))},
  {"from":"answer","parts":P("está",("rebuscando",["rebuscando","curioseando"]),"en el armario")}],
 notes="All three phrases share the only character (the girl), as in English; each box covers the whole clip, so each phrase holds only in part of the boxed frames (browsing early, dress mid-clip, doors at the end). 'probarse un vestido por encima' = holding it against herself, the native way to say it. 'las hojas del armario' (B2) = the wardrobe's door leaves."
)
D[4809]=dict(level="B",keyWord="el pasillo",
 taps=[T("cargar con un cesto de la ropa","la mujer","female"),T("maniobrar con la bicicleta","el hombre de la sudadera","male"),T("tener el pelo rizado y abundante","el hombre del pelo rizado","male")],
 nouns=[N("los abrigos"),N("el cesto de la ropa"),N("el pasillo"),N("los zapatos")],
 question="¿Qué está haciendo la mujer?",answer="La mujer recorre el pasillo con un cesto de la ropa.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":P("cargar con un",("cesto",["cesto"]),"de la ropa")},
  {"from":"taps","parts":P(("maniobrar",["maniobrar"]),"con la bicicleta")},
  {"from":"taps","parts":P("tener el pelo",("rizado",["rizado"]),"y abundante")},
  {"from":"answer","parts":P("recorre el",("pasillo",["pasillo"]),"con un cesto de la ropa")}],
 notes="Phrase 2: 'maniobrar con la bicicleta' (he pushes and squeezes the bike past the others) rather than literal 'wheel'. Answer uses 'recorre' (B1) in the present, the natural Spanish form here; English is progressive. In the last boxed frames the woman is only peeking out of a doorway, not carrying the basket.")
D[4361]=dict(level="B",keyWord="ir de compras",
 taps=[T("presumir de sus compras","la mujer","female"),T("pasear por delante de los escaparates","la mujer","female"),T("subir por la escalera mecánica","la mujer","female")],
 nouns=[N("el rascacielos"),N("el semáforo"),N("la bolsa de papel"),N("el vestido")],
 question="¿Qué está haciendo la mujer?",answer="La mujer está de compras y presume de sus bolsas.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":P(("presumir",["presumir","fardar"]),"de sus compras")},
  {"from":"taps","parts":P("pasear por delante de los",("escaparates",["escaparates"]))},
  {"from":"taps","parts":P("subir por la",("escalera mecánica",["escalera mecánica"]))},
  {"from":"answer","parts":P("está de",("compras",["compras"]),"y presume de sus bolsas")}],
 notes="Only one person, so all three boxes cover the whole clip; each phrase holds in its own part (street, mall, escalator). The answer uses 'estar de compras' (same expression family as the key word 'ir de compras') to avoid repeating 'compras' twice.")
D[54]=dict(level="B",keyWord="el cajero automático",
 taps=[T("teclear su PIN","la mujer","female"),T("expulsar los billetes","el cajero automático","female"),T("contar el dinero en efectivo","la mujer","female")],
 nouns=[N("la lámpara"),N("el cajero automático"),N("los billetes"),N("el abrigo")],
 question="¿Qué está haciendo la mujer?",answer="La mujer está sacando dinero del cajero automático.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":P(("teclear",["teclear","marcar"]),"su PIN")},
  {"from":"taps","parts":P(("expulsar",["expulsar","dispensar"]),"los billetes")},
  {"from":"taps","parts":P("contar el dinero en",("efectivo",["efectivo"]))},
  {"from":"answer","parts":P("está sacando dinero del",("cajero automático",["cajero automático","cajero"]))}],
 notes="Boxes 1 and 3 (the woman) cover the whole clip incl. card insertion and the flower purchase; 'teclear su PIN' / 'contar el dinero en efectivo' describe what she does in the matching middle frames. Phrase 2 'expulsar los billetes' is what the ATM does while the tray slides out lit. Noun 1 'la lámpara' = the wall light above the ATM.")
for i,d in D.items():
    o={"mediaId":i,"lang":"es","level":d["level"],"keyWord":d["keyWord"],"taps":d["taps"],"nouns":d["nouns"],"question":d["question"],
       "answer":d["answer"],"answerVoice":d["answerVoice"],"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(o,open(f"content/es/{i}.json","w"),ensure_ascii=False,indent=1)
