import json
def P(*a):
    out=[]
    for x in a:
        if isinstance(x,tuple): out.append({"text":x[0],"gap":True,"accept":list(x[1])})
        else: out.append({"text":x})
    return out
D={}
D[221]=dict(level="B",keyWord="le diplôme universitaire",
 taps=[("fêter sa remise de diplôme","la jeune femme","female"),("porter un sceau doré","le diplôme","female"),("voltiger dans les airs","les confettis","female")],
 nouns=[("le diplôme universitaire","female"),("la toque","female"),("le pompon","female")],
 question="Que fête la jeune femme ?",answer="Elle fête l'obtention de son diplôme universitaire.",av="female",
 recall=[("taps",P(("fêter",["fêter","célébrer"]),"sa remise de diplôme")),("taps",P("porter un",("sceau",["sceau"]),"doré")),
  ("taps",P(("voltiger",["voltiger","virevolter","tourbillonner"]),"dans les airs")),
  ("answer",P("fête","l'obtention de son",("diplôme universitaire",["diplôme universitaire"])))],
 notes="Graduation cap = 'la toque' (also 'la toque de diplômé'); French ceremonies rarely use it, but it is the usual word. Key word used in noun 1 (the certificate) and in the answer, so no extra noun row.")
D[222]=dict(level="B",keyWord="le retard",
 taps=[("barrer la porte du bus","le chauffeur","male"),("s'effondrer sur sa valise","la femme","female"),("indiquer l'heure","l'horloge","female")],
 nouns=[("l'horloge","female"),("la valise","female"),("les enseignes au néon","female"),("le chauffeur","male")],
 question="Que fait le chauffeur ?",answer="Il barre la porte du bus.",av="male",
 recall=[("taps",P(("barrer",["barrer","bloquer"]),"la porte du bus")),("taps",P("s'effondrer sur sa",("valise",["valise"]))),
  ("taps",P(("indiquer",["indiquer","afficher","montrer"]),"l'heure")),("answer",P("barre la",("porte",["porte","portière"]),"du bus"))],
 notes="Key word 'le retard' is not a noun of the set and fits no phrase naturally; the delay is shown by the clock and the waiting. Phrase 2: the woman throws up her arms in some boxed frames and collapses at the end; phrase written for the collapse.")
D[223]=dict(level="A",keyWord="la livraison",
 taps=[("être allongé sur le canapé","le chat","male"),("livrer le repas","l'homme avec le casque","male"),("porter un haut orange","la femme","female")],
 nouns=[("la lampe","male"),("la fenêtre","male"),("le chat","male"),("le canapé","male")],
 question="Qui livre le repas ?",answer="Un homme avec un casque livre le repas.",av="male",
 recall=[("taps",P("être allongé sur le",("canapé",["canapé"]))),("taps",P("livrer le",("repas",["repas"]))),
  ("taps",P("porter un",("haut",["haut"]),"orange")),("answer",P(("livre",["livre","apporte"]),"le repas"))],
 notes="Key word 'la livraison' is not a noun of the set; the phrase and answer use the verb 'livrer'. Cat box: the cat is off screen in most middle frames.")
D[224]=dict(level="B",keyWord="concevoir",
 taps=[("esquisser une chaise","l'homme","male"),("montrer le croquis du doigt","la femme","female"),("renifler la chaise en carton","le chat","female")],
 nouns=[("le croquis","female"),("le pot à crayons","female"),("la plante verte","female")],
 question="Que conçoivent-ils ?",answer="Ils conçoivent une chaise.",av="female",
 recall=[("taps",P("esquisser une",("chaise",["chaise"]))),("taps",P("montrer le",("croquis",["croquis","dessin"]),"du doigt")),
  ("taps",P(("renifler",["renifler","sentir"]),"la chaise en carton")),("answer",P(("conçoivent",["conçoivent","dessinent"]),"une chaise"))],
 notes="Key word 'concevoir' (verb) is natural here and used in question and answer. Noun 2 (English 'a jar'): it holds pencils, so 'le pot à crayons' is the everyday word; 'le bocal' would also do. 'Ils' for the mixed pair; answerVoice female kept from English.")
D[226]=dict(level="B",keyWord="le désespoir",
 taps=[("faire la manche à l'accordéon","le musicien","male"),("s'accroupir sur le sol","le musicien","male"),("rester ouvert et vide","l'étui","male")],
 nouns=[("l'accordéon","male"),("les graffitis","male"),("l'étui","male"),("le panneau d'affichage","male")],
 question="De quoi joue le musicien ?",answer="Il joue de l'accordéon.",av="male",
 recall=[("taps",P("faire la",("manche",["manche"]),"à l'accordéon")),("taps",P("s'accroupir sur le",("sol",["sol"]))),
  ("taps",P("rester ouvert et",("vide",["vide"]))),("answer",P(("joue",["joue"]),"de l'accordéon"))],
 notes="Phrase 1 'faire la manche à l'accordéon' (B2 collocation) instead of 'jouer de l'accordéon' so it does not duplicate the answer row. Model answer's B-level word is 'l'accordéon' (B1); the clip allows no richer short answer to this question. Key word 'le désespoir' not in the set (no noun row). Phrase 2: in the last frames the musician sits slumped rather than crouching; phrase written for the crouching moments.")
for i,d in D.items():
    o={"mediaId":i,"lang":"fr","level":d["level"],"keyWord":d["keyWord"],
       "taps":[{"phrase":a,"target":b,"voice":c} for a,b,c in d["taps"]],
       "nouns":[{"word":a,"voice":b} for a,b in d["nouns"]],
       "question":d["question"],"answer":d["answer"].split(" "),"answerVoice":d["av"],"carousel":[],
       "recall":[{"from":f,"parts":p} for f,p in d["recall"]],"notes":d["notes"]}
    json.dump(o,open(f"content/fr/{i}.json","w"),ensure_ascii=False,indent=1)
