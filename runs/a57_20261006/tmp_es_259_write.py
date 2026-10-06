import json
def T(*ps):
    out=[]
    for p in ps:
        if isinstance(p,tuple): out.append({"text":p[0],"gap":True,"accept":list(p[1])})
        else: out.append({"text":p})
    return out
def N(ws,v): return [{"word":w,"voice":v} for w in ws]
D={}
D[259]=dict(level="B",keyWord="inquietante",
 taps=[("teñir el cielo de un rojo inquietante","el resplandor rojo","male"),("llenar la estación de mercancías","los vagones de mercancías","male"),("formar una silueta oscura","los árboles","male")],
 nouns=N(["las nubes","la bola de fuego","los vagones de mercancías","las copas de los árboles"],"male"),
 question="¿Qué se extiende por el cielo nocturno?",
 answer="Un inquietante resplandor rojo se extiende por el cielo.",answerVoice="male",
 recall=[("taps",T("teñir el cielo de un rojo",("inquietante",["inquietante"]))),
         ("taps",T("llenar la",("estación",["estación"]),"de mercancías")),
         ("taps",T("formar una",("silueta",["silueta"]),"oscura")),
         ("answer",T("se",("extiende",["extiende","propaga"]),"por el cielo"))],
 notes="Phrase 1 is not a literal 'extenderse por el cielo': 'teñir el cielo de un rojo inquietante' says what the glow does and carries the key word. The answer subject 'Un inquietante resplandor rojo' holds the key word, so the answer recall row (subject removed) does not; the key word is gapped in tap row 1. The glow is faint in the first boxed frames and swells later.")
D[260]=dict(level="A",keyWord="el huevo",
 taps=[("comer pan con huevo","el hombre","male"),("estar junto a la ventana","el gato","male"),("caer en la sartén","el huevo","male")],
 nouns=N(["el hombre","el gato","los tomates","el huevo"],"male"),
 question="¿Qué está comiendo el hombre?",
 answer="Está comiendo pan con huevo.",answerVoice="male",
 recall=[("taps",T(("comer",["comer"]),"pan con huevo")),
         ("taps",T("estar junto a la",("ventana",["ventana"]))),
         ("taps",T("caer en la",("sartén",["sartén"]))),
         ("answer",T("Está comiendo pan con",("huevo",["huevo"])))],
 notes="The man's tap box also covers the early frames where he picks shell out of the bowl; phrase 1 describes what he does in the eating frames (most of the boxed ones at the end). Spanish answer drops the subject, so the answer row is the whole sentence.")
D[261]=dict(level="A",keyWord="el electricista",
 taps=[("cortar un cable","la electricista","female"),("llevar una camiseta rosa","la niña","female"),("tener barba","el hombre","male")],
 nouns=N(["la puerta"],"female")+N(["el hombre"],"male")+N(["la niña","la electricista"],"female"),
 question="¿Qué está haciendo la electricista?",
 answer="Está cortando un cable.",answerVoice="female",
 recall=[("taps",T("cortar un",("cable",["cable"]))),
         ("taps",T("llevar una",("camiseta",["camiseta"]),"rosa")),
         ("taps",T("tener",("barba",["barba"]))),
         ("nouns",T("la",("electricista",["electricista"]))),
         ("answer",T("Está",("cortando",["cortando"]),"un cable"))],
 notes="keyWord 'el electricista' kept as given, but the electrician in the clip is a woman, so the noun pill, target and question use 'la electricista' (same word, feminine article). Proposal: allow 'la electricista' as the shown form. Phrase 1 box also covers frames where she fits/switches the breaker; cutting is the main boxed action.")
D[262]=dict(level="A",keyWord="el elefante",
 taps=[("beber con la trompa","el elefante","female"),("levantar la trompa","el elefante","female"),("tener plumas blancas","los pájaros blancos","female")],
 nouns=N(["el árbol","el elefante","el pájaro","el agua"],"female"),
 question="¿Qué está haciendo el elefante?",
 answer="Está bebiendo agua con la trompa.",answerVoice="female",
 recall=[("taps",T("beber con la",("trompa",["trompa"]))),
         ("taps",T(("levantar",["levantar","alzar"]),"la trompa")),
         ("taps",T("tener",("plumas",["plumas"]),"blancas")),
         ("nouns",T("el",("elefante",["elefante"]))),
         ("answer",T("Está",("bebiendo",["bebiendo"]),"agua con la trompa"))],
 notes="Phrases 1 and 2 share one box (the elephant) as in English; the elephant also splashes and sprays itself in several boxed frames. 'el agua' keeps the masculine article (feminine noun with stressed a-).")
D[263]=dict(level="B",keyWord="emerger",
 taps=[("emerger del lago","la nadadora","female"),("subirse las gafas de natación","la nadadora","female"),("flotar cerca de la orilla","la barca","female")],
 nouns=N(["las gafas de natación","la barca de remos","el reflejo","las montañas"],"female"),
 question="¿Qué está haciendo la nadadora?",
 answer="Está emergiendo del lago.",answerVoice="female",
 recall=[("taps",T(("emerger",["emerger","salir"]),"del lago")),
         ("taps",T(("subirse",["subirse","levantarse"]),"las gafas de natación")),
         ("taps",T("flotar cerca de la",("orilla",["orilla"]))),
         ("answer",T("Está emergiendo del",("lago",["lago","agua"])))],
 notes="Phrase 1 box also covers frames after she has surfaced (smiling, lifting goggles, arms up); the emerging itself is the splash frames. 'la barca' is the target name for the rowing boat.")
for i,d in D.items():
    a=d["answer"].split()
    o={"mediaId":i,"lang":"es","level":d["level"],"keyWord":d["keyWord"],
       "taps":[{"phrase":p,"target":t,"voice":v} for p,t,v in d["taps"]],
       "nouns":d["nouns"],"question":d["question"],"answer":a,"answerVoice":d["answerVoice"],
       "carousel":[],"recall":[{"from":f,"parts":p} for f,p in d["recall"]],"notes":d["notes"]}
    json.dump(o,open(f"content/es/{i}.json","w"),ensure_ascii=False,indent=1)
