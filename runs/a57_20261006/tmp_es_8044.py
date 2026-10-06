import json
def T(*p):
    out=[]
    for x in p:
        if isinstance(x,tuple): out.append({"text":x[0],"gap":True,"accept":list(x[1])})
        else: out.append({"text":x})
    return out
def taps(l): return [{"phrase":a,"target":b,"voice":c} for a,b,c in l]
def nouns(l): return [{"word":a,"voice":b} for a,b in l]
D={}
D[8044]=dict(level="B",keyWord="locamente",
 taps=taps([("pegar grandes saltos","el chico de gris","male"),("taparse la boca con asombro","la chica de lila","female"),("partirse de risa","el chico de verde","male")]),
 nouns=nouns([("las guirnaldas de luces","male"),("la novia","female"),("el fardo de paja","male"),("la corbata","male")]),
 question="¿Qué está haciendo el chico de gris?",
 answer="Está pegando saltos como un loco.".split(), answerVoice="male",
 recall=[{"from":"taps","parts":T(("pegar",["pegar","dar"]),"grandes saltos")},
         {"from":"taps","parts":T("taparse la boca con",("asombro",["asombro","sorpresa"]))},
         {"from":"taps","parts":T(("partirse",["partirse","morirse","troncharse"]),"de risa")},
         {"from":"answer","parts":T("Está pegando saltos como un",("loco",["loco"]))}],
 notes="Key word 'locamente' is mostly used in Spain with 'enamorado'; for jumping a native says 'como un loco', so the answer uses 'como un loco' and 'locamente' appears nowhere (not forced). Proposal: accept 'como un loco' as the es rendering of 'wildly' here. Phrase 2: in the first boxed frames the woman in lilac just stands; she covers her mouth in most later frames, so the phrase describes that (the bride claps instead). 'Hay bale' rendered 'el fardo de paja' (the bales look like straw; the usual Spain word).")
D[7782]=dict(level="B",keyWord="más cerca",
 taps=taps([("estirar la trompa","el elefante","female"),("reírse a carcajadas","la chica","female"),("ofrecer un plátano","la mano con el plátano","female")]),
 nouns=nouns([("la lámpara de araña","female"),("la trompa","female"),("los cruasanes","female"),("el mantel","female")]),
 question="¿Qué está haciendo el elefante?",
 answer="Está acercando la trompa al plátano.".split(), answerVoice="female",
 recall=[{"from":"taps","parts":T("estirar la",("trompa",["trompa"]))},
         {"from":"taps","parts":T("reírse a",("carcajadas",["carcajadas"]))},
         {"from":"taps","parts":T(("ofrecer",["ofrecer","dar"]),"un plátano")},
         {"from":"answer","parts":T("Está",("acercando",["acercando","arrimando"]),"la trompa al plátano")}],
 notes="Key word 'más cerca' kept; the natural answer uses the verb 'acercar' (same root) rather than forcing 'más cerca', so no row gaps the key word itself. answerVoice kept female as in English although 'el elefante' is grammatically masculine (no subject word in the sentence).")
D[1]=dict(level="A",keyWord="el descanso",
 taps=taps([("reírse con el móvil","el chico","male"),("tocarse la cabeza","el chico","male"),("abrir mucho la boca","el chico","male")]),
 nouns=nouns([("la cortina","male"),("el móvil","male"),("el jersey","male"),("los libros","male")]),
 question="¿Qué está haciendo el chico?",
 answer="Se está riendo con el móvil.".split(), answerVoice="male",
 recall=[{"from":"taps","parts":T("reírse con el",("móvil",["móvil"]))},
         {"from":"taps","parts":T(("tocarse",["tocarse"]),"la cabeza")},
         {"from":"taps","parts":T("abrir mucho la",("boca",["boca"]))},
         {"from":"answer","parts":T("Se está",("riendo",["riendo"]),"con el móvil")}],
 notes="All three targets are the same young man ('el chico', natural in Spain for a young man). Key word 'el descanso' is not one of the nouns, so no noun row; 'la pausa' would also fit, 'el descanso' is fine.")
D[2]=dict(level="B",keyWord="el certificado",
 taps=taps([("mostrar un certificado enmarcado","la chica","female"),("abrazar un montón de certificados","la chica","female"),("sonreír con orgullo","la chica","female")]),
 nouns=nouns([("el pelo rizado","female"),("el certificado","female"),("la camiseta","female")]),
 question="¿Qué está haciendo la chica?",
 answer="Está presumiendo de sus certificados enmarcados.".split(), answerVoice="female",
 recall=[{"from":"taps","parts":T("mostrar un",("certificado",["certificado","diploma"]),"enmarcado")},
         {"from":"taps","parts":T(("abrazar",["abrazar","estrechar"]),"un montón de certificados")},
         {"from":"taps","parts":T("sonreír con",("orgullo",["orgullo"]))},
         {"from":"answer","parts":T("Está",("presumiendo",["presumiendo"]),"de sus certificados enmarcados")}],
 notes="Key word noun 'el certificado' already appears in phrase rows and the answer, so no separate noun row. 'A top' rendered 'la camiseta' (the usual Spain word for this long-sleeved top).")
D[4]=dict(level="A",keyWord="el curso",
 taps=taps([("beber café con hielo","la mujer","female"),("escribir en el portátil","la mujer","female"),("crecer en una maceta","la planta","female")]),
 nouns=nouns([("el portátil","female"),("el vaso","female"),("la planta","female"),("la mesa","female")]),
 question="¿Qué está haciendo la mujer?",
 answer="Está bebiendo café en la mesa.".split(), answerVoice="female",
 recall=[{"from":"taps","parts":T("beber café con",("hielo",["hielo"]))},
         {"from":"taps","parts":T("escribir en el",("portátil",["portátil","ordenador"]))},
         {"from":"taps","parts":T(("crecer",["crecer"]),"en una maceta")},
         {"from":"answer","parts":T("Está",("bebiendo",["bebiendo","tomando"]),"café en la mesa")}],
 notes="Key word 'el curso' is not visible as a thing (only via the voiceover); not among the nouns, so no noun row. Phrase 1 box (drinking) also covers frames where she types or opens the laptop; the phrase describes the drinking moments. Phrase 3 box is off in the later frames.")
for k,v in D.items():
    o={"mediaId":k,"lang":"es",**v,"carousel":[]}
    o={key:o[key] for key in ["mediaId","lang","level","keyWord","taps","nouns","question","answer","answerVoice","carousel","recall","notes"]}
    json.dump(o,open(f"content/es/{k}.json","w"),ensure_ascii=False,indent=1)
