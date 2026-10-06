import json
def P(*parts):
    out=[]
    for p in parts:
        if isinstance(p,tuple): out.append({"text":p[0],"gap":True,"accept":list(p)})
        else: out.append({"text":p})
    return out
def T(ph,tg,v): return {"phrase":ph,"target":tg,"voice":v}
def N(w,v): return {"word":w,"voice":v}
D={}
D[47]=dict(level="B",keyWord="une arène",
 taps=[T("brandir le poing","l'homme","male"),T("lancer son pop-corn en l'air","le garçon","male"),T("être suspendu au-dessus du terrain","le tableau d'affichage","male")],
 nouns=[N("le tableau d'affichage","male"),N("les spectateurs","male"),N("le terrain","male"),N("le pop-corn","male")],
 question="Où sont l'homme et le garçon ?",answer="Ils sont dans une arène bondée.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":P(("brandir","lever"),"le poing")},
         {"from":"taps","parts":P("lancer son",("pop-corn",),"en l'air")},
         {"from":"taps","parts":P("être",("suspendu",),"au-dessus du terrain")},
         {"from":"answer","parts":P("sont dans une",("arène","salle"),"bondée")}],
 notes="keyWord 'une arène' kept (copied with its indefinite article as in the source). For an indoor basketball hall a French native mostly says 'une salle' or 'un palais des sports'; 'arène' works through names like 'Accor Arena'. Proposal: 'la salle de sport' / 'le palais des sports' if the owner prefers. Box 1 (the man) also covers the tunnel frames before he raises his fist; phrase written for the fist-pump at the end. 'brandir le poing' = B2 collocation; 'bondée' B2.")
D[48]=dict(level="A",keyWord="arriver",
 taps=[T("ouvrir la porte","l'homme","male"),T("avoir des draps blancs","le lit","male"),T("avoir de petites vagues blanches","la mer","male")],
 nouns=[N("le ciel","male"),N("la mer","male"),N("le sable","male"),N("les palmiers","male")],
 question="Que fait l'homme ?",answer="Il ouvre la porte.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":P(("ouvrir",),"la porte")},
         {"from":"taps","parts":P("avoir des",("draps",),"blancs")},
         {"from":"taps","parts":P("avoir de petites",("vagues",),"blanches")},
         {"from":"answer","parts":P("ouvre la",("porte",))}],
 notes="Box 1 (the man) also covers walking frames on the path and the selfie; phrase written for the door-opening frames (most boxed frames). English 'trees' -> 'les palmiers' (they are palm trees; A2 everyday word). Key word 'arriver' fits no visible-action row naturally, so it appears in no recall row.")
D[49]=dict(level="B",keyWord="la flèche",
 taps=[T("récupérer sa flèche","la femme","female"),T("reposer sur un chevalet","la cible","female"),T("se tenir derrière l'archère","l'homme","male")],
 nouns=[N("le ciel","female"),N("la flèche","female"),N("la cible","female"),N("l'herbe","female")],
 question="Qu'a touché la flèche ?",answer="La flèche a atteint le centre de la cible.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":P("récupérer sa",("flèche",))},
         {"from":"taps","parts":P("reposer sur un",("chevalet","support"))},
         {"from":"taps","parts":P("se tenir derrière",("l'archère",))},
         {"from":"answer","parts":P("a atteint le",("centre","cœur"),"de la cible")}],
 notes="Box 1 (the woman) covers her whole clip (showing, nocking, shooting); phrase written for the end where she pulls the arrow out of the target. Answer uses 'atteindre' (B1) instead of 'toucher' to hit the B level. Gap 'l'archère' is a whole elided word (not cut inside).")
D[50]=dict(level="A",keyWord="le pot",
 taps=[T("tenir la poche à douille","la main","female"),T("porter un gant noir","la main","female"),T("se remplir de crème","le pot","female")],
 nouns=[N("le gant","female"),N("la poche à douille","female"),N("le pot","female"),N("la table","female")],
 question="Que fait la main ?",answer="Elle remplit un pot de crème.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":P("tenir la",("poche",),"à douille")},
         {"from":"taps","parts":P("porter un",("gant",),"noir")},
         {"from":"taps","parts":P("se",("remplir",),"de crème")},
         {"from":"answer","parts":P("remplit un",("pot",),"de crème")}],
 notes="English 'bag' = piping bag: the natural French word is 'la poche à douille' (above A level, but 'le sac' would be wrong); used in noun 2 and phrase 1. Phrases 1 and 2 share the target 'la main' as in English.")
D[51]=dict(level="B",keyWord="presser",
 taps=[T("presser le slime","la main","male"),T("saisir une poignée de perles","la main","male"),T("se trouver à l'arrière-plan","le mug","male")],
 nouns=[N("le mug","male"),N("le pouce","male"),N("le poignet","male"),N("les perles","male")],
 question="Que fait la main ?",answer="Elle presse une poignée de perles.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":P(("presser","serrer","malaxer"),"le slime")},
         {"from":"taps","parts":P("saisir une",("poignée",),"de perles")},
         {"from":"taps","parts":P("se",("trouver",),"à l'arrière-plan")},
         {"from":"answer","parts":P(("presse","serre"),"une poignée de perles")}],
 notes="'le slime' is the usual word in France for this toy. Answer voice male copied from English although 'la main' -> 'Elle' (the voice follows the English hand voice). Box 1 also covers the first frames where the hand only lies flat on the slime.")
for i,d in D.items():
    o={"mediaId":i,"lang":"fr","level":d["level"],"keyWord":d["keyWord"],"taps":d["taps"],"nouns":d["nouns"],"question":d["question"],
       "answer":d["answer"],"answerVoice":d["answerVoice"],"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(o,open(f"content/fr/{i}.json","w"),ensure_ascii=False,indent=2)
