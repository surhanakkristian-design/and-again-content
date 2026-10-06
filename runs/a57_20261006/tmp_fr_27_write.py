import json
def P(*a):
    out=[]
    for x in a:
        if isinstance(x,tuple): out.append({"text":x[0],"gap":True,"accept":list(x)})
        else: out.append({"text":x})
    return out
def T(ph,tg,v): return {"phrase":ph,"target":tg,"voice":v}
def N(w,v): return {"word":w,"voice":v}
F="female"; M="male"
docs={
27:dict(level="A",keyWord="un étudiant",
 taps=[T("ouvrir la fenêtre","l'étudiante",F),T("être posée sur les livres","la tasse",F),T("être posés sur le bureau","les livres",F)],
 nouns=[N("l'étudiante",F),N("la tasse",F),N("les livres",F),N("la fenêtre",F)],
 question="Que tient l'étudiante ?",answer="Elle tient une tasse.".split(),answerVoice=F,
 recall=[{"from":"taps","parts":P(("ouvrir",),"la fenêtre")},
         {"from":"taps","parts":P("être posée sur les",("livres",))},
         {"from":"taps","parts":P("être posés sur le",("bureau","table"))},
         {"from":"answer","parts":P("tient une",("tasse",))}],
 notes="keyWord 'un étudiant' kept; the clip shows a young woman, so pill/target use 'l'étudiante' (feminine form of the same word). No noun row: the elided pill 'l'étudiante' cannot be cut into 2-5 parts without splitting the elision, and no other row contains it. Tap 1: red box covers the whole clip, she opens the window only around 7-8 s. Tap 2: in a few boxed frames she holds the cup instead of it standing on the books; 'posée' agrees with la tasse, 'posés' with les livres."),
28:dict(level="A",keyWord="la matière",
 taps=[T("sourire à la caméra","la femme",F),T("être sur la table","les livres",F),T("jouer du piano","les mains",F)],
 nouns=[N("les cheveux",F),N("la veste",F),N("les livres",F)],
 question="Que fait la femme ?",answer="Elle sourit à la caméra.".split(),answerVoice=F,
 recall=[{"from":"taps","parts":P("sourire à la",("caméra",))},
         {"from":"taps","parts":P("être sur la",("table",))},
         {"from":"taps","parts":P("jouer du",("piano",))},
         {"from":"answer","parts":P(("sourit",),"à la caméra")}],
 notes="Key word la matière is not shown as a noun or phrase (school subjects only in quick cuts); not forced into the set. Books: she holds the stack lying on the table."),
29:dict(level="A",keyWord="le télescope",
 taps=[T("regarder dans le télescope","la femme",F),T("tenir sur trois pieds","le télescope",F),T("briller dans le ciel","la lune",F)],
 nouns=[N("le télescope",F),N("le bonnet",F),N("la veste",F),N("le ciel",F)],
 question="Que fait la femme ?",answer="Elle regarde dans un télescope.".split(),answerVoice=F,
 recall=[{"from":"taps","parts":P("regarder dans le",("télescope",))},
         {"from":"taps","parts":P("tenir sur trois",("pieds",))},
         {"from":"taps","parts":P(("briller",),"dans le ciel")},
         {"from":"answer","parts":P(("regarde",),"dans un télescope")}],
 notes="'le bonnet' for the knitted hat (natural word in France); 'la veste' for the puffer jacket (A-level; 'la doudoune' would be more precise). Tap 1: red box also covers close-ups where she looks at the camera after looking through the eyepiece."),
32:dict(level="A",keyWord="le mot",
 taps=[T("toucher sa barbe","l'homme",M),T("avoir les cheveux longs","la femme",F),T("être grande et blanche","la lettre",F)],
 nouns=[N("la lettre",F),N("la barbe",F),N("la femme",F)],
 question="Que touche l'homme ?",answer="Il touche sa barbe.".split(),answerVoice=M,
 recall=[{"from":"taps","parts":P(("toucher",),"sa barbe")},
         {"from":"taps","parts":P("avoir les",("cheveux",),"longs")},
         {"from":"taps","parts":P("être grande et",("blanche",))},
         {"from":"answer","parts":P("touche sa",("barbe",))}],
 notes="Key word le mot is not a visible thing of the set (the game is about words, only the letter B is shown); not forced. Tap 1: red box covers the whole clip, he touches his beard only in the thinking frames (about half)."),
33:dict(level="B",keyWord="la douleur",
 taps=[T("se tenir la joue enflée","l'homme",M),T("dégager de la vapeur","la tasse",M),T("pousser dans un pot en terre cuite","la plante",M)],
 nouns=[N("la plante en pot",M),N("la moustache",M),N("la poche de glace",M),N("la tasse",M)],
 question="Que fait l'homme ?",answer="Il se tient la joue enflée en grimaçant de douleur.".split(),answerVoice=M,
 recall=[{"from":"taps","parts":P("se",("tenir",),"la joue enflée")},
         {"from":"taps","parts":P("dégager de la",("vapeur",))},
         {"from":"taps","parts":P("pousser dans un",("pot",),"en terre cuite")},
         {"from":"answer","parts":P("se tient la joue enflée en grimaçant de",("douleur",))}],
 notes="Answer carries the key word in 'en grimaçant de douleur' (gapped in the answer row); fronting it would need a comma, so the chip order is unique. 'la tasse' for the mug ('le mug' also common). Tap 1: in two boxed frames he sips from the mug instead of holding his cheek. No noun row: la douleur is not a noun of the set."),
}
for i,d in docs.items():
    o={"mediaId":i,"lang":"fr"}; o.update(d); o["carousel"]=[]
    o={k:o[k] for k in ["mediaId","lang","level","keyWord","taps","nouns","question","answer","answerVoice","carousel","recall","notes"]}
    json.dump(o,open(f'content/fr/{i}.json','w'),ensure_ascii=False,indent=1)
