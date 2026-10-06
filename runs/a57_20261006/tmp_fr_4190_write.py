import json
def P(*parts):
    out=[]
    for p in parts:
        if isinstance(p,tuple): out.append({"text":p[0],"gap":True,"accept":list(p[1])})
        else: out.append({"text":p})
    return out
def T(phrase,target,voice): return {"phrase":phrase,"target":target,"voice":voice}
def N(w,v): return {"word":w,"voice":v}
D={}
D[4190]=dict(level="A",keyWord="se rencontrer",
 taps=[T("être assis sur un petit mur","le chat","female"),T("avoir une grande crinière","le lion","female"),T("être roux et blanc","le chat","female")],
 nouns=[N("les arbres","female"),N("le lion","female"),N("l'herbe","female"),N("le chat","female")],
 question="Que fait le chat ?",answer=["Il","rencontre","un","gros","lion."],answerVoice="female",
 recall=[{"from":"taps","parts":P("être",("assis",["assis"]),"sur un petit mur")},
         {"from":"taps","parts":P("avoir une grande",("crinière",["crinière"]))},
         {"from":"taps","parts":P("être",("roux",["roux"]),"et blanc")},
         {"from":"answer","parts":P(("rencontre",["rencontre"]),"un gros lion")}],
 notes="Key word 'se rencontrer' is reciprocal (the cat and the lion meet each other); with the cat as subject French uses transitive 'rencontrer' ('Il rencontre un gros lion'), so the reflexive form does not appear. Proposal: keep the database word; a learner sees the same verb. 'la crinière' is the only natural word for the lion's long dark hair (above A2; plain right word, noted). The low concrete ledge is 'un petit mur' (a native might say 'un muret', avoided as less basic). A ginger cat is 'roux' in French, not 'orange'. Lioness also visible but has no mane, so phrase 2 fits only the male lion. 'gros lion' is the natural French for a big lion."
)
D[5652]=dict(level="A",keyWord="grand",
 taps=[T("renifler la grosse balle","le chien","female"),T("être la plus grosse balle","la grosse balle","female"),T("être la plus petite balle","la petite balle","female")],
 nouns=[N("les arbres","female"),N("la balle","female"),N("le chien","female"),N("l'herbe","female")],
 question="Que fait le chien ?",answer=["Il","renifle","une","grosse","balle."],answerVoice="female",
 recall=[{"from":"taps","parts":P(("renifler",["renifler","sentir"]),"la grosse balle")},
         {"from":"taps","parts":P("être la plus",("grosse",["grosse","grande"]),"balle")},
         {"from":"taps","parts":P("être la plus petite",("balle",["balle"]))},
         {"from":"answer","parts":P(("renifle",["renifle","sent"]),"une grosse balle")}],
 notes="Key word 'grand' kept, but for a ball (volume) French natives say 'gros/grosse' ('une grosse balle'), not 'grande balle'; so 'grand' does not appear. Proposal: map this video to 'gros' for French, or accept 'grande' as an alternative (the recall row for phrase 2 accepts 'grande'). 'renifler' (to sniff) is everyday French; 'sentir' accepted as synonym."
)
D[26]=dict(level="A",keyWord="la paille",
 taps=[T("tenir une longue paille","l'homme","male"),T("boire du jus d'orange","l'homme","male"),T("être posé sur le comptoir","le verre","male")],
 nouns=[N("les lunettes de soleil","male"),N("la paille","male"),N("le verre","male"),N("la chemise","male")],
 question="Que fait l'homme ?",answer=["Il","boit","du","jus","avec","une","paille."],answerVoice="male",
 recall=[{"from":"taps","parts":P("tenir une longue",("paille",["paille"]))},
         {"from":"taps","parts":P("boire du",("jus",["jus"]),"d'orange")},
         {"from":"taps","parts":P("être posé sur le",("comptoir",["comptoir","bar"]))},
         {"from":"answer","parts":P(("boit",["boit"]),"du jus avec une paille")}],
 notes="English 'the bar' (the counter) is 'le comptoir' in French ('le bar' is the place); 'bar' accepted in recall. The glass stands on the counter in the wide shots; in the close-ups the counter is out of frame and near the end the man lifts the empty glass upside down, so phrase 3 describes most boxed frames."
)
D[324]=dict(level="A",keyWord="le gaming",
 taps=[T("lever les deux bras","la fille","female"),T("gagner la partie","la fille","female"),T("porter une veste rouge","le garçon","male")],
 nouns=[N("la fille","female"),N("la veste","female"),N("les cartons","female"),N("le canapé","female")],
 question="Qui gagne la partie ?",answer=["La","fille","gagne","la","partie."],answerVoice="female",
 recall=[{"from":"taps","parts":P(("lever",["lever"]),"les deux bras")},
         {"from":"taps","parts":P(("gagner",["gagner"]),"la partie")},
         {"from":"taps","parts":P("porter une",("veste",["veste"]),"rouge")},
         {"from":"answer","parts":P("gagne la",("partie",["partie"]))}],
 notes="Key word 'le gaming' is not a thing in the noun set and none of the exercises names it naturally (a native says 'jouer aux jeux vidéo'); not forced. The girl only raises both arms (fists) in the last part of the clip; in the earlier boxed frames she holds the controller, so phrase 1 describes the ending (as in English). The boxes on the shelves look like cardboard storage boxes: 'les cartons'."
)
D[612]=dict(level="A",keyWord="à droite",
 taps=[T("montrer la droite du doigt","la femme","female"),T("porter un gros sac à dos","l'homme","male"),T("faire au revoir de la main","la femme","female")],
 nouns=[N("les lumières","female"),N("la femme","female"),N("la nourriture","female"),N("la roue","female")],
 question="Quelle direction montre la femme ?",answer=["Elle","montre","la","droite."],answerVoice="female",
 recall=[{"from":"taps","parts":P("montrer la",("droite",["droite"]),"du doigt")},
         {"from":"taps","parts":P("porter un gros",("sac",["sac"]),"à dos")},
         {"from":"taps","parts":P("faire au revoir de la",("main",["main"]))},
         {"from":"answer","parts":P(("montre",["montre","indique"]),"la droite")}],
 notes="Key word 'à droite' (adverbial) kept; with 'montrer' French natives say 'montrer la droite' / 'vers la droite', so the exact form 'à droite' does not appear (the word 'droite' does). Proposal: accept 'la droite' for this video. Phrase 3: the woman waves goodbye only in the last frames; in most boxed frames she points or turns the man around (same as the English box). The man also waves a thumbs-up, not goodbye, so phrase 3 fits only her."
)
for mid,d in D.items():
    o={"mediaId":mid,"lang":"fr","level":d["level"],"keyWord":d["keyWord"],"taps":d["taps"],"nouns":d["nouns"],
       "question":d["question"],"answer":d["answer"],"answerVoice":d["answerVoice"],"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(o,open(f"content/fr/{mid}.json","w"),ensure_ascii=False,indent=2)
