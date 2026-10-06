import json
def g(t,acc=None): return {"text":t,"gap":True,"accept":[t]+(acc or [])}
def p(t): return {"text":t}
def T(ph,tg,v): return {"phrase":ph,"target":tg,"voice":v}
def N(w,v): return {"word":w,"voice":v}
def ans(s): return s.split(" ")
D={}
D[275]=dict(level="A",keyWord="se disputer",
 taps=[T("montrer l'homme du doigt","la femme","female"),T("lever les yeux et réfléchir","l'homme","male"),T("sourire à l'homme","la femme","female")],
 nouns=[N("les rideaux","male"),N("le canapé","male"),N("la table","male"),N("l'homme","male")],
 question="Que font l'homme et la femme ?",answer=ans("Ils se disputent dans le salon."),answerVoice="male",
 recall=[{"from":"taps","parts":[p("montrer"),p("l'homme"),p("du"),g("doigt")]},
         {"from":"taps","parts":[p("lever les yeux"),p("et"),g("réfléchir",["penser"])]},
         {"from":"taps","parts":[g("sourire"),p("à l'homme")]},
         {"from":"answer","parts":[p("se"),g("disputent"),p("dans le salon")]}],
 notes="Phrase 1: she points at him with her finger ('montrer l'homme du doigt'). Key word 'se disputer' gapped in the answer row (gap 'disputent', 'se' kept as plain part).")
D[276]=dict(level="B",keyWord="une excursion",
 taps=[T("brouter à flanc de colline","les moutons","female"),T("se jeter du haut d'une falaise","la cascade","female"),T("être calé sur un rocher","le téléphone","female")],
 nouns=[N("la cascade","female"),N("l'arc-en-ciel","female"),N("le téléphone","female"),N("le rocher","female")],
 question="Que font les amis ?",answer=ans("Ils posent pour une photo de groupe."),answerVoice="female",
 recall=[{"from":"taps","parts":[g("brouter",["paître"]),p("à flanc de colline")]},
         {"from":"taps","parts":[p("se jeter"),p("du haut d'une"),g("falaise")]},
         {"from":"taps","parts":[p("être"),g("calé",["posé"]),p("sur un rocher")]},
         {"from":"answer","parts":[g("posent"),p("pour une photo de groupe")]}],
 notes="keyWord copied as in the source ('une excursion', indefinite article, unlike the other fr key words with the definite article); proposal 'l'excursion'. The key word is not a noun of the set, so no noun row and it appears in no row. Phrase 3: the phone propped up on the boulder for the group photo ('être calé sur un rocher'). Answer kept without 'devant la cascade' to keep one word order.")
D[279]=dict(level="B",keyWord="déployer de la force",
 taps=[T("déployer toute sa force","l'homme","male"),T("brandir le poing","l'homme","male"),T("rouler dans une flaque","la charrette","male")],
 nouns=[N("les sacs","male"),N("la roue","male"),N("la flaque","male")],
 question="Que fait l'homme ?",answer=ans("Il déploie toute sa force."),answerVoice="male",
 recall=[{"from":"taps","parts":[g("déployer"),p("toute sa force")]},
         {"from":"taps","parts":[p("brandir le"),g("poing")]},
         {"from":"taps","parts":[p("rouler"),p("dans une"),g("flaque")]},
         {"from":"answer","parts":[p("déploie"),p("toute sa"),g("force")]}],
 notes="Phrase 2: English 'clench his fist'; the clip shows him raising a clenched fist, so 'brandir le poing' (B2). The green box also covers frames where he pushes or lies on the handle; the fist is raised in the last frames. Phrase 1 uses the key word, as the English does.")
D[280]=dict(level="A",keyWord="le chaton",
 taps=[T("regarder la caméra","le chaton","female"),T("être assis sur un lit","le chaton","female"),T("s'approcher tout près","le chaton","female")],
 nouns=[N("le chaton","female"),N("le lit","female"),N("le téléphone","female")],
 question="Que fait le chaton ?",answer=ans("Il regarde la caméra."),answerVoice="female",
 recall=[{"from":"taps","parts":[p("regarder la"),g("caméra")]},
         {"from":"taps","parts":[p("être"),g("assis"),p("sur un lit")]},
         {"from":"taps","parts":[g("s'approcher",["s'avancer"]),p("tout près")]},
         {"from":"nouns","parts":[p("le"),g("chaton")]},
         {"from":"answer","parts":[g("regarde",["fixe"]),p("la caméra")]}],
 notes="'la caméra' = the phone's camera the kitten looks into (the phone is noun 3, 'le téléphone'). Noun row added for the key word 'le chaton'. All three phrases have the kitten as target, as in English.")
D[281]=dict(level="B",keyWord="le crayon pour les yeux",
 taps=[T("tracer un trait d'eye-liner","la femme brune","female"),T("tenir un coton-tige","la femme brune","female"),T("lever le pouce","l'amie blonde","female")],
 nouns=[N("les ampoules","female"),N("le miroir","female"),N("l'eye-liner","female"),N("le coton-tige","female")],
 question="Que fait la femme brune ?",answer=ans("Elle applique de l'eye-liner sur sa paupière."),answerVoice="female",
 recall=[{"from":"taps","parts":[p("tracer un"),g("trait"),p("d'eye-liner")]},
         {"from":"taps","parts":[p("tenir un"),g("coton-tige")]},
         {"from":"taps","parts":[p("lever le"),g("pouce")]},
         {"from":"answer","parts":[g("applique",["met"]),p("de l'eye-liner"),p("sur sa paupière")]}],
 notes="KEY WORD: 'le crayon pour les yeux' is a pencil (kohl); the clip shows a felt-tip liquid liner pen, which French calls 'l'eye-liner' (usual everyday word in France). Kept the keyWord unchanged but used 'l'eye-liner' for noun 3 and in the texts; proposal: keyWord 'l'eye-liner'. 'l'eye-liner'/'d'eye-liner' are elided so they are never gapped. Phrase 2 box also covers the first frames where she is still drawing with the pen; she holds the cotton swab in the later boxed frames.")
for i,d in D.items():
    out={"mediaId":i,"lang":"fr",**d,"carousel":[]}
    out={k:out[k] for k in ["mediaId","lang","level","keyWord","taps","nouns","question","answer","answerVoice","carousel","recall","notes"]}
    json.dump(out,open(f"content/fr/{i}.json","w"),ensure_ascii=False,indent=1)
