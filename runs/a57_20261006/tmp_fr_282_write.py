import json
def P(*parts):
    out=[]
    for p in parts:
        if isinstance(p,tuple): out.append({"text":p[0],"gap":True,"accept":list(p[1])})
        else: out.append({"text":p})
    return out
def T(ph,tg,v): return {"phrase":ph,"target":tg,"voice":v}
def N(w,v): return {"word":w,"voice":v}
D={}
D[282]=dict(level="B",keyWord="le fard à paupières",
 taps=[T("appliquer du fard doré","le pinceau","female"),T("porter un foulard noué sur la tête","la femme au foulard","female"),T("se faire maquiller les paupières","la femme en chemise","female")],
 nouns=[N("le foulard","female"),N("le fard à paupières","female"),N("le col","female"),N("le bouton","female")],
 question="Que prend le pinceau ?",answer="Il prend du fard à paupières doré.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":P(("appliquer",["appliquer","étaler","mettre"]),"du fard doré")},
  {"from":"taps","parts":P("porter un",("foulard",["foulard","turban"]),"noué sur la tête")},
  {"from":"taps","parts":P("se faire maquiller les",("paupières",["paupières"]))},
  {"from":"answer","parts":P("prend du",("fard",["fard"]),"à paupières doré")}],
 notes="Phrase 1: the red box covers the palette shots but mostly the brush on the eyelid, so the phrase says what it does in most boxed frames (applying); the question/answer keep the English 'picking up' (first frames). Phrase 3: the blue box mostly covers close-ups of her lid being made up, only the last frames show her showing off the golden lids, so 'se faire maquiller les paupières'. 'le foulard' for the wrapped headscarf (looks like a turban; 'turban' accepted in recall).")
D[283]=dict(level="B",keyWord="le tissu",
 taps=[T("dérouler le tissu imprimé","l'homme","male"),T("découper le tissu aux ciseaux","l'homme","male"),T("serrer le tissu plié contre elle","la femme","female")],
 nouns=[N("la boucle d'oreille","female"),N("le tissu","female"),N("la table","female"),N("le mètre ruban","female")],
 question="Que fait l'homme ?",answer="Il découpe le tissu aux ciseaux.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":P(("dérouler",["dérouler"]),"le tissu imprimé")},
  {"from":"taps","parts":P("découper le tissu aux",("ciseaux",["ciseaux"]))},
  {"from":"taps","parts":P(("serrer",["serrer","presser"]),"le tissu plié contre elle")},
  {"from":"answer","parts":P("découpe le",("tissu",["tissu"]),"aux ciseaux")}],
 notes="Phrase 3: the blue box also covers the woman reaching for and feeling the cloth; she hugs the folded piece only in the last frames (kept as English). Phrases 1 and 2 both target the man as in English.")
D[284]=dict(level="B",keyWord="le masque visage",
 taps=[T("porter un bandeau en éponge","la femme en violet","female"),T("montrer son amie du doigt","la femme en gris","female"),T("se reposer sur un coussin","le chien","female")],
 nouns=[N("le bandeau","female"),N("le masque visage","female"),N("le chien","female"),N("le bol","female")],
 question="Que portent les femmes ?",answer="Elles portent des masques à l'argile verte.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":P("porter un",("bandeau",["bandeau"]),"en éponge")},
  {"from":"taps","parts":P("montrer son amie du",("doigt",["doigt"]))},
  {"from":"taps","parts":P("se reposer sur un",("coussin",["coussin"]))},
  {"from":"nouns","parts":P("le",("masque",["masque"]),"visage")},
  {"from":"answer","parts":P(("portent",["portent"]),"des masques à l'argile verte")}],
 notes="Key word 'le masque visage' is product-label French; a native says 'le masque (pour le visage)' or 'le masque à l'argile'. Kept on the noun pill; proposal: 'le masque pour le visage'. Answer uses 'des masques à l'argile verte' (plural 'masques visage' sounds odd), hence the nouns recall row. Phrase 2: the green box covers mostly the woman in grey sitting with her mask (and the spatula in one frame); she points at her friend only in the last frames. Phrase 3: only the dog's head is visible behind the women; the cushion is not clearly shown.")
D[285]=dict(level="A",keyWord="la famille",
 taps=[T("prendre une photo de famille","l'homme à l'appareil photo","male"),T("agiter les deux mains","l'homme à l'appareil photo","male"),T("monter les marches en courant","le chien","male")],
 nouns=[N("la fenêtre","male"),N("la famille","male"),N("les marches","male"),N("l'herbe","male")],
 question="Que fait la famille ?",answer="Elle prend une photo de famille.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":P("prendre une photo de",("famille",["famille"]))},
  {"from":"taps","parts":P(("agiter",["agiter","lever"]),"les deux mains")},
  {"from":"taps","parts":P("monter les",("marches",["marches"]),"en courant")},
  {"from":"answer","parts":P(("prend",["prend","fait"]),"une photo de famille")}],
 notes="Phrase 2: the green box covers the grandpa at the camera and posing; he waves both hands only in a few frames (kept as English). Phrase 3: the dog runs up the steps in two frames, in most blue frames it sits on the grandmother's lap. Answer subject 'Elle' = la famille; answerVoice kept male.")
D[287]=dict(level="A",keyWord="loin",
 taps=[T("montrer un village du doigt","la femme","female"),T("se retourner vers elle","l'homme en vert","male"),T("porter une veste rouge","la personne en rouge","female")],
 nouns=[N("le ciel","female"),N("le village","female"),N("l'herbe","female")],
 question="Que montre la femme du doigt ?",answer="Elle montre un village au loin.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":P("montrer un",("village",["village"]),"du doigt")},
  {"from":"taps","parts":P("se",("retourner",["retourner"]),"vers elle")},
  {"from":"taps","parts":P("porter une",("veste",["veste"]),"rouge")},
  {"from":"answer","parts":P("montre un village au",("loin",["loin"]))}],
 notes="Answer: 'au loin' could also stand before the object ('Elle montre au loin un village'), marked but possible. Phrases 1 and 2: in the wide shots the three just stand; the woman points and the man looks back only in the close frames (kept as English). Key word 'loin' sits in the answer as 'au loin'.")
for i,d in D.items():
    o={"mediaId":i,"lang":"fr","level":d["level"],"keyWord":d["keyWord"],"taps":d["taps"],"nouns":d["nouns"],"question":d["question"],"answer":d["answer"],"answerVoice":d["answerVoice"],"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(o,open(f"content/fr/{i}.json","w"),ensure_ascii=False,indent=1)
