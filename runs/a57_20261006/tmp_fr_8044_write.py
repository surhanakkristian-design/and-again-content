import json
def g(t,acc=None): return {"text":t,"gap":True,"accept":acc or [t]}
def p(t): return {"text":t}
D={}
D[8044]=dict(level="B",keyWord="follement",
 taps=[("bondir dans les airs","l'homme en gris","male"),("rester bouche bée","la femme en lilas","female"),("se tordre de rire","l'homme en vert","male")],
 nouns=[("les guirlandes lumineuses","male"),("la mariée","female"),("la botte de foin","male"),("la cravate","male")],
 question="Que fait l'homme en gris ?",answer="Il bondit follement dans les airs.".split(),answerVoice="male",
 recall=[("taps",[g("bondir",["bondir","sauter"]),p("dans les airs")]),("taps",[p("rester"),g("bouche"),p("bée")]),
  ("taps",[p("se tordre de"),g("rire")]),("answer",[p("bondit"),g("follement"),p("dans les airs")])],
 notes="'rester bouche bée' (B2) for the woman in lilac: she covers her mouth in shock in most boxed frames; in the first two frames she still stands smiling. 'follement' with 'bondir' is natural ('comme un fou' would be the most colloquial, but the key word is kept).")
D[7782]=dict(level="B",keyWord="plus près",
 taps=[("allonger sa trompe","l'éléphant","female"),("rire aux éclats","la femme","female"),("tendre une banane","la main","female")],
 nouns=[("le lustre","female"),("la trompe","female"),("les croissants","female"),("la nappe","female")],
 question="Que fait l'éléphant ?",answer="Il avance sa trompe plus près de la banane.".split(),answerVoice="female",
 recall=[("taps",[g("allonger",["allonger","tendre"]),p("sa trompe")]),("taps",[p("rire aux"),g("éclats")]),
  ("taps",[p("tendre une"),g("banane")]),("answer",[p("avance sa trompe"),g("plus près"),p("de la banane")])],
 notes="Answer subject 'Il' = l'éléphant (masc.); answerVoice kept female as in English (voice of the clip). Gap of the answer row is the key word 'plus près' (two words in one gap).")
D[1]=dict(level="A",keyWord="la pause",
 taps=[("rire devant son téléphone","l'homme","male"),("se toucher la tête","l'homme","male"),("ouvrir grand la bouche","l'homme","male")],
 nouns=[("le rideau","male"),("le téléphone","male"),("le pull","male"),("les livres","male")],
 question="Que fait l'homme ?",answer="Il rit devant son téléphone.".split(),answerVoice="male",
 recall=[("taps",[p("rire devant son"),g("téléphone")]),("taps",[p("se toucher la"),g("tête")]),
  ("taps",[p("ouvrir grand la"),g("bouche")]),("answer",[g("rit"),p("devant son téléphone")])],
 notes="All three boxes cover the whole man in every frame; phrases describe his action in most frames of each phase (laughing first, then hand on head, then mouth wide open).")
D[2]=dict(level="B",keyWord="le certificat",
 taps=[("présenter un certificat encadré","la femme","female"),("serrer plusieurs certificats contre soi","la femme","female"),("rayonner de fierté","la femme","female")],
 nouns=[("les cheveux bouclés","female"),("le certificat","female"),("le haut","female")],
 question="Que fait la femme ?",answer="Elle montre fièrement ses certificats encadrés.".split(),answerVoice="female",
 recall=[("taps",[g("présenter",["présenter","montrer"]),p("un certificat encadré")]),("taps",[g("serrer"),p("plusieurs certificats contre soi")]),
  ("taps",[p("rayonner de"),g("fierté")]),("answer",[p("montre fièrement ses"),g("certificats"),p("encadrés")])],
 notes="'fièrement' could in theory also stand at the end ('Elle montre ses certificats encadrés fièrement'), but that order is unnatural; the chips have one natural order.")
D[4]=dict(level="A",keyWord="le cours",
 taps=[("boire du café glacé","la femme","female"),("taper sur un ordinateur portable","la femme","female"),("pousser dans un pot","la plante","female")],
 nouns=[("l'ordinateur portable","female"),("le verre","female"),("la plante","female"),("la table","female")],
 question="Que fait la femme ?",answer="Elle boit du café à table.".split(),answerVoice="female",
 recall=[("taps",[g("boire"),p("du café glacé")]),("taps",[g("taper"),p("sur un ordinateur portable")]),
  ("taps",[p("pousser dans un"),g("pot")]),("answer",[p("boit du"),g("café"),p("à table")])],
 notes="The key word 'le cours' is not a visible thing (online course only in the transcript); no noun row. 'à table' is the natural French for 'at the table'.")
for i,d in D.items():
    o={"mediaId":i,"lang":"fr","level":d["level"],"keyWord":d["keyWord"],
       "taps":[{"phrase":a,"target":b,"voice":c} for a,b,c in d["taps"]],
       "nouns":[{"word":a,"voice":b} for a,b in d["nouns"]],
       "question":d["question"],"answer":d["answer"],"answerVoice":d["answerVoice"],"carousel":[],
       "recall":[{"from":f,"parts":ps} for f,ps in d["recall"]],"notes":d["notes"]}
    json.dump(o,open(f"content/fr/{i}.json","w"),ensure_ascii=False,indent=2)
