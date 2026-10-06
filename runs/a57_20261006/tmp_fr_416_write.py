import json
def P(t,g=None,acc=None):
    d={"text":t}
    if g: d["gap"]=True; d["accept"]=acc or [t]
    return d
def row(f,*parts): return {"from":f,"parts":list(parts)}
def N(w,v): return {"word":w,"voice":v}
def T(p,t,v): return {"phrase":p,"target":t,"voice":v}
C={}
C[416]=dict(level="A",keyWord="le ketchup",
 taps=[T("secouer une bouteille de ketchup","l'homme","male"),T("regarder l'homme","la femme","female"),T("être dans une assiette","les frites","male")],
 nouns=[N("l'homme","male"),N("la femme","female"),N("les frites","male"),N("le ketchup","male")],
 question="Que fait l'homme ?",answer=["Il","secoue","une","bouteille","de","ketchup."],answerVoice="male",
 recall=[row("taps",P("secouer",1,["secouer"]),P("une bouteille de ketchup")),
         row("taps",P("regarder",1,["regarder","observer"]),P("l'homme")),
         row("taps",P("être dans une"),P("assiette",1)),
         row("answer",P("secoue une bouteille de"),P("ketchup",1))],
 notes="Phrase 3: like the English 'lie on a plate', the ketchup also ends up in the plate in the later frames; the fries are in it in every boxed frame. French says 'dans une assiette'. In the last frames the woman also holds the bottle, but the man shakes it in most boxed frames.")
C[72]=dict(level="A",keyWord="le basketball",
 taps=[T("faire rebondir un ballon","la fille","female"),T("sauter très haut","la fille","female"),T("porter des lunettes","l'homme à lunettes","male")],
 nouns=[N("le ciel","female"),N("le ballon de basket","female"),N("le filet","female"),N("la fille","female")],
 question="Que fait la fille ?",answer=["Elle","joue","au","basketball","avec","deux","hommes."],answerVoice="female",
 recall=[row("taps",P("faire"),P("rebondir",1,["rebondir"]),P("un ballon")),
         row("taps",P("sauter",1,["sauter"]),P("très haut")),
         row("taps",P("porter des"),P("lunettes",1)),
         row("answer",P("joue au"),P("basketball",1,["basketball","basket"]),P("avec deux hommes"))],
 notes="Key word 'le basketball' is the sport in French; English noun 2 'a basketball' (the ball) is 'le ballon de basket', so the key word appears in the answer ('joue au basketball'), not as the noun pill. Box 3 is OFF in two dunk frames (fine). 'deux hommes' copies the English 'two men' (they look like young men).")
C[401]=dict(level="A",keyWord="les patins à glace",
 taps=[T("lacer ses patins à glace","la femme","female"),T("écarter les bras","la femme","female"),T("porter une veste verte","la personne en vert","female")],
 nouns=[N("le bonnet","female"),N("les arbres","female"),N("l'écharpe","female"),N("les patins à glace","female")],
 question="Que fait la femme ?",answer=["Elle","patine","sur","la","glace."],answerVoice="female",
 recall=[row("taps",P("lacer ses"),P("patins",1,["patins"]),P("à glace")),
         row("taps",P("écarter",1,["écarter","ouvrir"]),P("les bras")),
         row("taps",P("porter une"),P("veste",1,["veste","doudoune"]),P("verte")),
         row("answer",P("patine",1,["patine"]),P("sur la glace"))],
 notes="Box 3 is OFF in most frames; the person in green is only visible at the end (far left).")
C[4210]=dict(level="B",keyWord="tenir",
 taps=[T("agripper deux bâtonnets en bois","le hamster","female"),T("dissimuler son visage","le hamster","female"),T("sourire de toutes ses dents","le hamster","female")],
 nouns=[N("l'esquimau","female"),N("le hamster","female"),N("le plan de travail","female")],
 question="Que fait le hamster ?",answer=["Il","tient","deux","esquimaux","par","leurs","bâtonnets."],answerVoice="female",
 recall=[row("taps",P("agripper",1,["agripper","serrer","tenir"]),P("deux bâtonnets en bois")),
         row("taps",P("dissimuler son"),P("visage",1,["visage"])),
         row("taps",P("sourire de toutes ses"),P("dents",1)),
         row("answer",P("tient",1,["tient"]),P("deux esquimaux par leurs bâtonnets"))],
 notes="'l'esquimau' = the usual French (France) word for a chocolate-coated ice cream on a stick (B1). B words: agripper, dissimuler, sourire de toutes ses dents, esquimau. Answer voice kept female as in English although le hamster -> il. Phrase 2 holds in the first ~14 boxed frames (bars in front of the face); phrase 3 in the last frames.")
C[402]=dict(level="A",keyWord="la glace",
 taps=[T("glisser sur la glace","la femme","female"),T("porter un bonnet vert","l'homme","male"),T("porter une veste rouge","la femme","female")],
 nouns=[N("le ciel","female"),N("les arbres","female"),N("la femme","female"),N("la glace","female")],
 question="Que fait la femme ?",answer=["Elle","glisse","sur","la","glace."],answerVoice="female",
 recall=[row("taps",P("glisser sur la"),P("glace",1)),
         row("taps",P("porter un"),P("bonnet",1),P("vert")),
         row("taps",P("porter une"),P("veste",1,["veste","doudoune"]),P("rouge")),
         row("answer",P("glisse",1,["glisse"]),P("sur la glace"))],
 notes="Phrase 1: the woman slides only in the last boxed frames; in the first ones she crouches on the ice and touches it (as in English).")
for i,c in C.items():
    d={"mediaId":i,"lang":"fr"}; d.update(c); d["carousel"]=[]
    order=["mediaId","lang","level","keyWord","taps","nouns","question","answer","answerVoice","carousel","recall","notes"]
    d={k:d[k] for k in order}
    json.dump(d,open(f"content/fr/{i}.json","w"),ensure_ascii=False,indent=2)
