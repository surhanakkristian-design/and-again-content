import json
def P(*a):
    out=[]
    for x in a:
        if isinstance(x,tuple): out.append({"text":x[0],"gap":True,"accept":list(x[1])})
        else: out.append({"text":x})
    return out
def ch(s): return s.split(' ')
D={}
D[215]=dict(level="B",keyWord="l'obscurité",
 taps=[("craquer une allumette","la femme","female"),("porter un pull rayé","l'homme","male"),("briller dans l'obscurité","la lanterne","female")],
 nouns=[("la lanterne","female"),("l'allumette","female"),("la fenêtre","female"),("la casserole en cuivre","female")],
 question="Que fait la femme ?",answer="Elle allume une lanterne dans l'obscurité.",av="female",
 recall=[("taps",P(("craquer",["craquer","frotter"]),"une allumette")),("taps",P("porter un pull",("rayé",["rayé"]))),
  ("taps",P(("briller",["briller","luire"]),"dans l'obscurité")),("answer",P("allume une",("lanterne",["lanterne"]),"dans l'obscurité"))],
 notes="Key word l'obscurité is elided, so it is never a gap (it appears in tap 3 and the answer). 'la casserole en cuivre' for the copper pans hanging on the wall.")
D[217]=dict(level="B",keyWord="la fléchette",
 taps=[("viser la cible","la femme","female"),("grignoter des chips","l'homme aux chips","male"),("se planter près du centre","la fléchette","female")],
 nouns=[("la fléchette","female"),("la cible","female"),("le mur en bois","female")],
 question="Que fait la femme ?",answer="Elle vise la cible avec une fléchette.",av="female",
 recall=[("taps",P(("viser",["viser"]),"la cible")),("taps",P(("grignoter",["grignoter","manger"]),"des chips")),
  ("taps",P("se",("planter",["planter","ficher"]),"près du centre")),("answer",P("vise la cible avec une",("fléchette",["fléchette"])))],
 notes="'la cible' = the dartboard (natural in context; 'la cible de fléchettes' would repeat the key word). 'le centre' for the bullseye (B-level everyday word; 'le mille' is rarer).")
D[218]=dict(level="B",keyWord="déclarer",
 taps=[("brandir un parchemin","la femme au balcon","female"),("tirer la corde de la cloche","le sonneur","male"),("enlacer un petit garçon","la femme au foulard","female")],
 nouns=[("la cloche","female"),("le parchemin","female"),("les colombes","female"),("le foulard","female")],
 question="Que se passe-t-il sur le balcon ?",answer="Une femme déclare quelque chose à la foule.",av="female",
 recall=[("taps",P("brandir un",("parchemin",["parchemin"]))),("taps",P("tirer la",("corde",["corde"]),"de la cloche")),
  ("taps",P(("enlacer",["enlacer","étreindre"]),"un petit garçon")),("answer",P(("déclare",["déclare","annonce"]),"quelque chose à la foule"))],
 notes="Tap 1 'brandir' covers both holding the scroll out and raising it high; the woman only holds it at chest height in some boxed frames.")
D[219]=dict(level="A",keyWord="le cerf",
 taps=[("regarder la caméra","le cerf","male"),("ouvrir la bouche","le cerf","male"),("partir en courant","le cerf","male")],
 nouns=[("le cerf","male"),("les arbres","male"),("les plantes","male")],
 question="Que fait le cerf ?",answer="Le cerf part en courant.",av="male",
 recall=[("taps",P(("regarder",["regarder"]),"la caméra")),("taps",P("ouvrir la",("bouche",["bouche"]))),
  ("taps",P(("partir",["partir"]),"en courant")),("nouns",P("le",("cerf",["cerf"]))),("answer",P("part en",("courant",["courant"])))],
 notes="'partir en courant' (A level) instead of 's'enfuir' (B). 'les plantes' for the ferns (A level). All three phrases have the same target, as in English.")
D[220]=dict(level="B",keyWord="décongeler",
 taps=[("décongeler un poisson congelé","l'homme","male"),("poser brutalement un poisson","l'homme","male"),("tremper dans un saladier","le poisson","male")],
 nouns=[("le filet","male"),("le robinet","male"),("le saladier","male"),("le placard","male")],
 question="Que fait l'homme ?",answer="Il décongèle un poisson congelé.",av="male",
 recall=[("taps",P(("décongeler",["décongeler"]),"un poisson congelé")),("taps",P("poser",("brutalement",["brutalement","violemment"]),"un poisson")),
  ("taps",P("tremper dans un",("saladier",["saladier","bol"]))),("answer",P("décongèle un poisson",("congelé",["congelé","surgelé"])))],
 notes="Tap 2 (slam the fish down) happens only in the first seconds; the green box covers the man later too. 'le saladier' for the big metal bowl in the sink.")
for i,d in D.items():
    o={"mediaId":i,"lang":"fr","level":d["level"],"keyWord":d["keyWord"],
     "taps":[{"phrase":a,"target":b,"voice":c} for a,b,c in d["taps"]],
     "nouns":[{"word":a,"voice":b} for a,b in d["nouns"]],
     "question":d["question"],"answer":ch(d["answer"]),"answerVoice":d["av"],"carousel":[],
     "recall":[{"from":f,"parts":p} for f,p in d["recall"]],"notes":d["notes"]}
    json.dump(o,open(f"content/fr/{i}.json","w"),ensure_ascii=False,indent=1)
