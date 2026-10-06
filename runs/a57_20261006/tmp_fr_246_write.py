import json
def P(t,gap=None,acc=None):
    d={"text":t}
    if gap: d["gap"]=True; d["accept"]=acc or [t]
    return d
def R(frm,*parts): return {"from":frm,"parts":list(parts)}
def T(p,t,v): return {"phrase":p,"target":t,"voice":v}
def N(w,v): return {"word":w,"voice":v}
data={
246:dict(level="A",keyWord="conduire",
 taps=[T("conduire la voiture","la femme","female"),T("porter un bonnet gris","la femme","female"),T("sourire à la conductrice","l'homme","male")],
 nouns=[N("le rétroviseur","female"),N("la mer","female"),N("la femme","female"),N("l'homme","male")],
 question="Que fait la femme ?",answer="Elle conduit une voiture au bord de la mer.".split(),answerVoice="female",
 recall=[R("taps",P("conduire",1),P("la voiture")),R("taps",P("porter un"),P("bonnet",1),P("gris")),
         R("taps",P("sourire",1),P("à la conductrice")),R("answer",P("conduit une voiture"),P("au bord de la"),P("mer",1))],
 notes="Key word 'conduire' is a verb while English 'driving' is a noun (the activity); kept unchanged, it reads naturally in phrase 1 and the answer (owner may prefer 'la conduite'). The grey hat is a knitted beanie: 'un bonnet' is the everyday French word. Mirror = the rear-view mirror: 'le rétroviseur' is the only natural word (slightly above A2, plain right word). In the first box frames only hands on the wheel are visible (still the woman driving)."),
248:dict(level="B",keyWord="le compte-gouttes",
 taps=[T("verser le remède goutte à goutte","la femme","female"),T("avaler le remède","l'homme","male"),T("dégager de la vapeur","la bouilloire en cuivre","female")],
 nouns=[N("le compte-gouttes","female"),N("la cuillère en bois","female"),N("le tablier","female")],
 question="Que fait la femme ?",answer="Elle dose le remède au compte-gouttes.".split(),answerVoice="female",
 recall=[R("taps",P("verser le"),P("remède",1,["remède","médicament"]),P("goutte à goutte")),
         R("taps",P("avaler",1),P("le remède")),
         R("taps",P("dégager de la"),P("vapeur",1)),
         R("answer",P("dose le remède"),P("au"),P("compte-gouttes",1))],
 notes="B1/B2 words: 'remède', 'goutte à goutte', 'dégager', 'doser', 'au compte-gouttes'. The medicine is called 'le remède' everywhere (old apothecary setting); recall row 1 also accepts 'médicament'. The man drinks the dose from the spoon in the boxed frames ('avaler')."),
250:dict(level="A",keyWord="le canard",
 taps=[T("mettre la tête sous l'eau","le canard","female"),T("ouvrir les ailes","le canard","female"),T("ouvrir le bec","le canard","female")],
 nouns=[N("le canard","female"),N("les arbres","female"),N("l'eau","female")],
 question="Que fait le canard ?",answer="Le canard nage sur l'eau.".split(),answerVoice="female",
 recall=[R("taps",P("mettre la"),P("tête",1),P("sous l'eau")),R("taps",P("ouvrir les"),P("ailes",1)),
         R("taps",P("ouvrir",1),P("le bec")),R("nouns",P("le"),P("canard",1)),R("answer",P("nage",1),P("sur l'eau"))],
 notes="The only animal in the clip is the duck, so all three phrases are about it (as in English). Duck's mouth = 'le bec'."),
251:dict(level="B",keyWord="un haltère",
 taps=[T("muscler ses biceps","l'homme","male"),T("siroter son café","la femme","female"),T("être assise en tailleur","la femme","female")],
 nouns=[N("l'haltère","male"),N("le palmier","male"),N("le fauteuil","male"),N("la fenêtre","male")],
 question="Que fait l'homme ?",answer="Il muscle ses biceps avec un haltère.".split(),answerVoice="male",
 recall=[R("taps",P("muscler",1,["muscler","travailler"]),P("ses biceps")),R("taps",P("siroter son"),P("café",1)),
         R("taps",P("être assise en"),P("tailleur",1)),R("answer",P("muscle ses biceps"),P("avec un"),P("haltère",1))],
 notes="Source keyWord.fr 'un haltère' carries the indefinite article (other key-word nouns carry the definite one); kept unchanged, proposal: 'l'haltère' (masculine, h muet), which is the noun pill. English 'to do biceps curls' -> 'muscler ses biceps' (natural French; 'faire des curls' is gym jargon); the box also covers the overhead press, still working his arms. B1/B2: muscler, siroter, en tailleur."),
252:dict(level="A",keyWord="la poussière",
 taps=[T("souffler sur une valise","l'homme","male"),T("lever un doigt","la femme","female"),T("être perché tout en haut","l'oiseau","female")],
 nouns=[N("la poussière","female"),N("l'homme","male"),N("la femme","female"),N("la valise","female")],
 question="Que fait l'homme ?",answer="Il souffle sur une valise pleine de poussière.".split(),answerVoice="male",
 recall=[R("taps",P("souffler",1),P("sur une valise")),R("taps",P("lever un"),P("doigt",1)),
         R("taps",P("être"),P("perché",1),P("tout en haut")),R("answer",P("souffle sur une valise"),P("pleine de"),P("poussière",1))],
 notes="'être perché' is the plain right verb for a bird sitting up high (slightly above A2). In the first boxed frames of phrase 1 the man is only lifting the case; he blows on it in most boxed frames. The woman's finger is raised from the first shots (dusty fingertip)."),
}
for i,d in data.items():
    out={"mediaId":i,"lang":"fr"}; out.update(d); out["carousel"]=[]
    order=["mediaId","lang","level","keyWord","taps","nouns","question","answer","answerVoice","carousel","recall","notes"]
    out={k:out[k] for k in order}
    json.dump(out,open(f"content/fr/{i}.json","w"),ensure_ascii=False,indent=2)
