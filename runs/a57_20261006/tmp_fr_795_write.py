import json
def T(*ps):
    out=[]
    for p in ps:
        if isinstance(p,tuple): out.append({"text":p[0],"gap":True,"accept":list(p[1])})
        else: out.append({"text":p})
    return out
D={}
D[795]=dict(level="A",keyWord="la serviette",
 taps=[("sortir de la piscine","l'homme","male"),("se sécher les cheveux","l'homme","male"),("secouer la tête","le chien","male")],
 nouns=[("l'homme","male"),("la serviette","male"),("le chien","male"),("l'arbre","male")],
 question="Que fait l'homme ?",answer="Il se sèche les cheveux avec une serviette.".split(),answerVoice="male",
 recall=[("taps",T("sortir de la",("piscine",["piscine"]))),("taps",T("se",("sécher",["sécher"]),"les cheveux")),
  ("taps",T(("secouer",["secouer"]),"la tête")),("answer",T("se sèche les cheveux avec une",("serviette",["serviette"])))],
 notes="Phrase 3: the wet dog shakes its head (and body) only in part of the boxed frames; 'secouer la tête' is what it does in most of them. Answer contains the key word, so no noun row.")
D[7212]=dict(level="A",keyWord="prendre le petit-déjeuner",
 taps=[("prendre le petit-déjeuner","la femme","female"),("tenir une fourchette","la femme","female"),("regarder l'assiette de la femme","l'oiseau","female")],
 nouns=[("l'oiseau","female"),("la tasse","female"),("l'assiette","female"),("le bonnet","female")],
 question="Que fait la femme ?",answer="Elle prend le petit-déjeuner au-dessus des nuages.".split(),answerVoice="female",
 recall=[("taps",T("prendre le",("petit-déjeuner",["petit-déjeuner","petit déjeuner"]))),("taps",T("tenir une",("fourchette",["fourchette"]))),
  ("taps",T(("regarder",["regarder"]),"l'assiette de la femme")),("answer",T("prend le petit-déjeuner au-dessus des",("nuages",["nuages"])))],
 notes="Key word kept with the hyphen (petit-déjeuner, reformed spelling) everywhere; recall accepts 'petit déjeuner' too. The bird is a raven/crow; 'l'oiseau' kept at level A. Phrase 3 says 'l'assiette de la femme' because 'son assiette' would be ambiguous (its/her). 'le bonnet' = the bobble hat.")
D[385]=dict(level="A",keyWord="frapper",
 taps=[("frapper la balle","la fille","female"),("tenir une batte","la fille","female"),("voler dans les airs","la balle","female")],
 nouns=[("la balle","female"),("la batte","female"),("la casquette","female")],
 question="Que fait la fille ?",answer="Elle frappe la balle avec une batte.".split(),answerVoice="female",
 recall=[("taps",T(("frapper",["frapper","taper"]),"la balle")),("taps",T(("tenir",["tenir"]),"une batte")),
  ("taps",T(("voler",["voler"]),"dans les airs")),("answer",T("frappe la balle avec une",("batte",["batte"])))],
 notes="")
D[7773]=dict(level="A",keyWord="avec précaution",
 taps=[("porter les tasses avec précaution","l'ours","female"),("être assise à une table","la femme","female"),("lever les mains","la femme","female")],
 nouns=[("les tasses","female"),("la femme","female"),("la table","female"),("l'ours","female")],
 question="Que fait l'ours ?",answer="Il porte des tasses jusqu'à la table.".split(),answerVoice="female",
 recall=[("taps",T("porter les tasses avec",("précaution",["précaution","prudence","soin"]))),("taps",T("être",("assise",["assise"]),"à une table")),
  ("taps",T(("lever",["lever"]),"les mains")),("answer",T("porte des",("tasses",["tasses"]),"jusqu'à la table"))],
 notes="answerVoice kept female as in English although the subject is 'l'ours' (il); the voice reads the sentence, not the bear. 'avec précaution' is natural but slightly formal; 'avec prudence'/'avec soin' accepted in the recall row.")
D[528]=dict(level="A",keyWord="se garer",
 taps=[("se garer entre deux voitures","la femme","female"),("être assis sur un mur","l'homme","male"),("ouvrir la portière","la femme","female")],
 nouns=[("la femme","female"),("la voiture","female"),("le ciel","female")],
 question="Que fait la femme ?",answer="Elle gare sa voiture.".split(),answerVoice="female",
 recall=[("taps",T("se",("garer",["garer"]),"entre deux voitures")),("taps",T("être assis sur un",("mur",["mur","muret"]))),
  ("taps",T("ouvrir la",("portière",["portière","porte"]))),("answer",T("gare sa",("voiture",["voiture"])))],
 notes="Key word 'se garer' (intransitive) used in phrase 1; the answer uses transitive 'garer sa voiture', the most natural full sentence. Phrase 2: the man sits on a low wall ('muret' would be more exact but is above A2; 'mur' kept, recall accepts 'muret'). Phrase 3 box also covers frames where she just stands by the open door.")
for i,d in D.items():
    out={"mediaId":i,"lang":"fr","level":d["level"],"keyWord":d["keyWord"],
     "taps":[{"phrase":p,"target":t,"voice":v} for p,t,v in d["taps"]],
     "nouns":[{"word":w,"voice":v} for w,v in d["nouns"]],
     "question":d["question"],"answer":d["answer"],"answerVoice":d["answerVoice"],"carousel":[],
     "recall":[{"from":f,"parts":p} for f,p in d["recall"]],"notes":d["notes"]}
    json.dump(out,open(f"content/fr/{i}.json","w"),ensure_ascii=False,indent=2)
