import json
def P(*a):
    out=[]
    for x in a:
        if isinstance(x,tuple): out.append({"text":x[0],"gap":True,"accept":list(x[1:]) or [x[0]]} if len(x)>1 else {"text":x[0],"gap":True,"accept":[x[0]]})
        else: out.append({"text":x})
    return out
D={}
D[300]=dict(level="A",keyWord="le drapeau",
 taps=[("tirer sur la corde","la fille","female"),("flotter au vent","le drapeau","female"),("lever les yeux vers le drapeau","la fille","female")],
 nouns=[("le drapeau","female"),("le ciel","female"),("les montagnes","female"),("la fille","female")],
 question="Que regarde la fille ?",answer="Elle regarde le drapeau.",av="female",
 recall=[("taps",P("tirer sur la",("corde",))),("taps",P("flotter au",("vent",))),("taps",P("lever les yeux vers le",("drapeau",))),("answer",P(("regarde",),"le drapeau"))],
 notes="")
D[301]=dict(level="A",keyWord="flotter",
 taps=[("flotter sur le lac","l'homme","male"),("lever le pouce","l'homme","male"),("se poser sur l'homme","l'oiseau","male")],
 nouns=[("l'oiseau","male"),("l'homme","male"),("le lac","male")],
 question="Que fait l'homme ?",answer="Il flotte sur le lac.",av="male",
 recall=[("taps",P(("flotter",),"sur le lac")),("taps",P("lever le",("pouce",))),("taps",P("se",("poser",),"sur l'homme")),("answer",P("flotte sur le",("lac",)))],
 notes="Tap 3: English 'sit on the man'; the bird lands on his belly, then on his head, so 'se poser sur l'homme' (the natural French verb for a bird).")
D[302]=dict(level="A",keyWord="la farine",
 taps=[("être couché par terre","le chien","male"),("toucher le nez de la femme","l'homme","male"),("porter un foulard gris","la femme","female")],
 nouns=[("la farine","male"),("les œufs","male"),("le chien","male")],
 question="Qu'y a-t-il sur le visage de l'homme ?",answer="Il a de la farine sur le visage.",av="male",
 recall=[("taps",P("être",("couché",),"par terre")),("taps",P("toucher le",("nez",),"de la femme")),("taps",P("porter un",("foulard",),"gris")),("answer",P("a de la",("farine",),"sur le visage"))],
 notes="Tap 1: the dog lies on the floor behind the table (only head visible in some frames). Answer uses the natural French 'Il a de la farine sur le visage' (English 'There is flour on his face').")
D[303]=dict(level="A",keyWord="la fleur",
 taps=[("tenir un bouquet de fleurs","la femme","female"),("être assise près de la fenêtre","la femme","female"),("toucher une fleur rose","la femme","female")],
 nouns=[("la fenêtre","female"),("les fleurs","female"),("la femme","female")],
 question="Que tient la femme ?",answer="Elle tient des fleurs.",av="female",
 recall=[("taps",P("tenir un",("bouquet",),"de fleurs")),("taps",P("être assise près de la",("fenêtre",))),("taps",P("toucher une",("fleur",),"rose")),("answer",P(("tient",),"des fleurs"))],
 notes="Tap 2's box also covers close-ups of the flowers where the window is not visible; phrase written for the wide shots.")
D[305]=dict(level="A",keyWord="la mouche",
 taps=[("se poser sur la tartine","la mouche","male"),("voler au-dessus de la table","la mouche","male"),("agiter une serviette","la main","male")],
 nouns=[("la mouche","male"),("le pot","male"),("le thé","male"),("la tartine","male")],
 question="Que fait la mouche ?",answer="Elle est posée sur la tartine.",av="male",
 recall=[("taps",P("se",("poser",),"sur la tartine")),("taps",P(("voler",),"au-dessus de la table")),("taps",P("agiter une",("serviette",))),("nouns",P("la",("mouche",))),("answer",P("est posée sur la",("tartine",)))],
 notes="English 'bread' = a slice of toast with jam: 'la tartine' is the everyday French word for it (A2). Answer subject 'Elle' (la mouche) while answerVoice stays male as in English (voice copied).")
for i,d in D.items():
    o={"mediaId":i,"lang":"fr","level":d["level"],"keyWord":d["keyWord"],
       "taps":[{"phrase":p,"target":t,"voice":v} for p,t,v in d["taps"]],
       "nouns":[{"word":w,"voice":v} for w,v in d["nouns"]],
       "question":d["question"],"answer":d["answer"].split(" "),"answerVoice":d["av"],
       "carousel":[],"recall":[{"from":f,"parts":p} for f,p in d["recall"]],"notes":d["notes"]}
    json.dump(o,open(f"content/fr/{i}.json","w"),ensure_ascii=False,indent=1)
