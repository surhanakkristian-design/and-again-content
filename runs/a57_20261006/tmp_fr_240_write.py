import json
def g(t,acc=None): return {"text":t,"gap":True,"accept":acc or [t]}
def p(t): return {"text":t}
D={}
D[240]=dict(level="B",keyWord="le match nul",
 taps=[("porter un tee-shirt turquoise","la femme en turquoise","female"),("avoir une barbe épaisse","l'homme costaud","male"),("recouvrir les poings d'un torchon","la grand-mère","female")],
 nouns=[("le torchon","female"),("la table","female"),("la vieille dame","female")],
 question="Comment se termine le bras de fer ?",answer="Le bras de fer se termine par un match nul.",answerVoice="female",
 recall=[("taps",[p("porter un"),g("tee-shirt",["tee-shirt","t-shirt"]),p("turquoise")]),
         ("taps",[p("avoir une"),g("barbe"),p("épaisse")]),
         ("taps",[g("recouvrir",["recouvrir","couvrir"]),p("les poings d'un torchon")]),
         ("answer",[p("se termine par un"),g("match nul")])],
 notes="Phrase 3: in the first boxed frames the grandmother holds the tea towel up behind the fists; at the end she lays it over the locked fists, so 'recouvrir les poings d'un torchon' describes the drape. 'le bras de fer' = arm-wrestling; 'la vieille dame' for the elderly woman (same person as the grandmother target). B1/B2 items: turquoise, une barbe épaisse, recouvrir, le bras de fer, le match nul.")
D[241]=dict(level="A",keyWord="le dessin",
 taps=[("être assis sur les marches","l'homme","male"),("faire un dessin","l'homme","male"),("porter un chapeau jaune","la femme","female")],
 nouns=[("le dessin","male"),("le chapeau","male"),("les maisons","male"),("la chemise","male")],
 question="Que montre l'homme à la femme ?",answer="Il lui montre son dessin.",answerVoice="male",
 recall=[("taps",[p("être assis sur les"),g("marches")]),
         ("taps",[p("faire un"),g("dessin")]),
         ("taps",[p("porter un"),g("chapeau"),p("jaune")]),
         ("answer",[p("lui"),g("montre"),p("son dessin")])],
 notes="The woman's hat is a pale yellow straw hat. Key word 'le dessin' is in the tap row 'faire un dessin', so no extra noun row.")
D[243]=dict(level="A",keyWord="s'habiller",
 taps=[("mettre un pull","la femme","female"),("aider la femme à s'habiller","l'homme","male"),("se regarder dans le miroir","la femme","female")],
 nouns=[("le bonnet","female"),("le sac","female"),("la porte","female"),("le jean","female")],
 question="Que fait l'homme ?",answer="Il aide la femme à s'habiller.",answerVoice="male",
 recall=[("taps",[p("mettre un"),g("pull")]),
         ("taps",[g("aider"),p("la femme à s'habiller")]),
         ("taps",[p("se"),g("regarder"),p("dans le miroir")]),
         ("answer",[p("aide la"),g("femme",["femme","fille"]),p("à s'habiller")])],
 notes="Phrase 1: the English red box covers the woman in almost every frame (sweater, scarf, boots, mirror, door); 'mettre un pull' is what she does in the first frames, the rest is her getting dressed. 'aider la femme à s'habiller' instead of the more idiomatic 'l'aider à s'habiller' so that the gap words are not elided; the key word s'habiller (elided) is never a gap. 'le bonnet' = the beanie; 'le jean' singular as in everyday French.")
D[244]=dict(level="A",keyWord="la boisson",
 taps=[("boire du jus d'orange","l'homme","male"),("faire du jus d'orange","la femme","female"),("être posé sur un bâton","le perroquet","male")],
 nouns=[("le perroquet","male"),("l'homme","male"),("le jus","male"),("les oranges","male")],
 question="Que fait l'homme ?",answer="Il boit un verre de jus d'orange.",answerVoice="male",
 recall=[("taps",[g("boire"),p("du jus d'orange")]),
         ("taps",[p("faire du"),g("jus"),p("d'orange")]),
         ("taps",[p("être posé sur un"),g("bâton")]),
         ("answer",[p("boit un"),g("verre"),p("de jus d'orange")])],
 notes="Key word 'la boisson' appears in no text: the clip shows the drink as orange juice ('le jus'), and 'la boisson' is not a noun of the English set (English 'juice' -> 'le jus'). Proposal: owner may accept 'le jus' as the shown drink. In the last frames the woman pours juice from a jug and the man gets water poured over his head.")
D[245]=dict(level="A",keyWord="boire",
 taps=[("avoir des tresses","la femme","female"),("remplir la bouteille","l'homme","male"),("être assis sur les rochers","la marmotte","male")],
 nouns=[("le ciel","male"),("les montagnes","male"),("la femme","female"),("l'homme","male")],
 question="Que font les deux personnes ?",answer="Ils boivent de l'eau à la bouteille.",answerVoice="male",
 recall=[("taps",[p("avoir des"),g("tresses")]),
         ("taps",[g("remplir"),p("la bouteille")]),
         ("taps",[p("être assis sur les"),g("rochers")]),
         ("answer",[g("boivent"),p("de l'eau à la bouteille")])],
 notes="Phrase 1: English 'to wash her hands' is true only in the 2-3 fountain frames; in most boxed frames the woman drinks, which the man does too, so the phrase names what fits only her in all boxed frames: her two braids ('avoir des tresses'). Phrase 2: the man fills the bottle at the stone fountain. Phrase 3: the small animal is a marmot ('la marmotte', target only); it sits up on the rocks.")
for vid,d in D.items():
    out={"mediaId":vid,"lang":"fr","level":d["level"],"keyWord":d["keyWord"],
     "taps":[{"phrase":a,"target":b,"voice":c} for a,b,c in d["taps"]],
     "nouns":[{"word":a,"voice":b} for a,b in d["nouns"]],
     "question":d["question"].replace(" ?"," ?") if False else d["question"],
     "answer":d["answer"].split(" "),"answerVoice":d["answerVoice"],"carousel":[],
     "recall":[{"from":f,"parts":ps} for f,ps in d["recall"]],"notes":d["notes"]}
    json.dump(out,open(f"content/fr/{vid}.json","w"),ensure_ascii=False,indent=1)
