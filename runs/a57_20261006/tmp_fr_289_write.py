import json
def g(t,acc=None): return {"text":t,"gap":True,"accept":acc or [t]}
def p(t): return {"text":t}
def tap(ph,tg,v): return {"phrase":ph,"target":tg,"voice":v}
def n(w,v="female"): return {"word":w,"voice":v}
def ans(s): return s.split(" ")
D={}
D[289]=dict(level="B",keyWord="la peur",
 taps=[tap("porter la main à la poitrine","la femme en bleu","female"),
       tap("s'agripper à un poteau","la femme en bleu","female"),
       tap("s'approcher par-derrière","la femme en jaune","female")],
 nouns=[n("les sommets"),n("la rambarde"),n("le reflet")],
 question="Que fait la femme en bleu ?",
 answer=ans("Elle s'agrippe à un poteau, paralysée par la peur."),answerVoice="female",
 recall=[{"from":"taps","parts":[p("porter la main à la"),g("poitrine")]},
         {"from":"taps","parts":[p("s'agripper à un"),g("poteau")]},
         {"from":"taps","parts":[p("s'approcher"),g("par-derrière",["par-derrière","par derrière"])]},
         {"from":"answer","parts":[p("s'agrippe à un poteau, paralysée par la"),g("peur")]}],
 notes="Phrase 3: the woman in yellow walks up behind the woman in blue (behind her in frame, approaching along the skywalk). 'le reflet' = the yellow woman's reflection in the glass floor. B1/B2 items: porter la main à la poitrine, s'agripper, par-derrière, la rambarde, les sommets, paralysée par la peur. Answer: the comma stays on the 'poteau,' chip, so only one chip order.")
D[290]=dict(level="A",keyWord="le sentiment",
 taps=[tap("mettre la main sur la poitrine","la femme","female"),
       tap("fermer les yeux","la femme","female"),
       tap("porter une chemise grise","l'homme aux cheveux longs","male")],
 nouns=[n("le drapeau"),n("la femme"),n("le verre")],
 question="Que fait la femme ?",
 answer=ans("Elle met la main sur la poitrine."),answerVoice="female",
 recall=[{"from":"taps","parts":[p("mettre la"),g("main"),p("sur la poitrine")]},
         {"from":"taps","parts":[g("fermer"),p("les yeux")]},
         {"from":"taps","parts":[p("porter une"),g("chemise"),p("grise")]},
         {"from":"answer","parts":[p("met la main sur la"),g("poitrine")]}],
 notes="Key word: 'le sentiment' is kept, but for the sense 'an emotion, like joy or sadness' (what the clip shows: nervousness then joy) a French native says 'l'émotion' far more often; proposal: 'l'émotion' for this concept (owner decides). The key word is not used in the exercises (nothing natural). 'mettre la main sur la poitrine' is the natural French for the English 'touch her chest'; same wording in the answer.")
D[292]=dict(level="A",keyWord="la bagarre",
 taps=[tap("lever un oreiller très haut","la femme","female"),
       tap("porter un tee-shirt gris","la femme","female"),
       tap("avoir une barbe","l'homme","male")],
 nouns=[n("la fenêtre"),n("l'oreiller"),n("la plante"),n("le lit")],
 question="Que font-ils sur le lit ?",
 answer=ans("Ils font une bataille d'oreillers."),answerVoice="female",
 recall=[{"from":"taps","parts":[p("lever un"),g("oreiller"),p("très haut")]},
         {"from":"taps","parts":[p("porter un"),g("tee-shirt",["tee-shirt","t-shirt"]),p("gris")]},
         {"from":"taps","parts":[p("avoir une"),g("barbe")]},
         {"from":"answer","parts":[p("font une"),g("bataille",["bataille","bagarre"]),p("d'oreillers")]}],
 notes="Key word: a pillow fight is 'une bataille d'oreillers' in France; 'une bagarre d'oreillers' is heard but less natural, so the answer uses 'bataille' (the recall row also accepts 'bagarre'). 'la bagarre' fits a real scuffle; proposal for this clip: 'la bataille' (owner decides). The man has a white T-shirt, so phrase 2 fits only the woman.")
D[293]=dict(level="B",keyWord="la réalisation de films",
 taps=[tap("poser devant le réflecteur","la femme à l'écharpe","female"),
       tap("s'accroupir derrière la caméra","la femme à la casquette","female"),
       tap("être perché sur le muret","le pigeon","female")],
 nouns=[n("le micro"),n("le réflecteur"),n("le pigeon"),n("le trépied")],
 question="Sur quoi la caméra est-elle montée ?",
 answer=ans("La caméra est montée sur un trépied."),answerVoice="female",
 recall=[{"from":"taps","parts":[p("poser devant le"),g("réflecteur")]},
         {"from":"taps","parts":[p("s'accroupir derrière la"),g("caméra")]},
         {"from":"taps","parts":[p("être"),g("perché",["perché","posé"]),p("sur le muret")]},
         {"from":"answer","parts":[p("est montée sur un"),g("trépied")]}],
 notes="Phrase 1: the English 'shield her eyes' happens only in about 3 of the boxed frames; in most boxed frames the woman in the scarf stands posing in front of the reflector, so 'poser devant le réflecteur' (she later laughs with the crew, still in her place). 'le muret' = the low wall at the roof edge (the English 'ledge'). 'le micro' = the boom microphone. Key word: 'la réalisation de films' is correct but bookish; what the clip shows (a shoot) is 'le tournage', and the general activity is 'la réalisation' / 'faire des films'; proposal 'le tournage' (owner decides). Not used in the exercises. B1/B2 items: poser, s'accroupir, perché, le muret, le trépied, monté sur.")
D[294]=dict(level="A",keyWord="le feu",
 taps=[tap("tenir un long bâton","la femme","female"),
       tap("mettre du bois dans le feu","l'homme","male"),
       tap("brûler entre les pierres","le feu","female")],
 nouns=[n("les arbres"),n("l'homme","male"),n("le feu"),n("les pierres")],
 question="Que fait l'homme ?",
 answer=ans("Il met du bois dans le feu."),answerVoice="male",
 recall=[{"from":"taps","parts":[p("tenir un long"),g("bâton")]},
         {"from":"taps","parts":[p("mettre du bois dans le"),g("feu")]},
         {"from":"taps","parts":[g("brûler"),p("entre les pierres")]},
         {"from":"answer","parts":[p("met du"),g("bois"),p("dans le feu")]}],
 notes="Phrase 2 / answer: the man puts the log on the fire only in the first part of the clip (about 4 of the boxed frames); afterwards he sits and watches the sparks. Nothing else he does in most frames is his alone (the woman also sits and looks up), so the wood action is kept, as in English. No nouns recall row: 'le feu' already appears in the phrase-2 and answer rows.")
for i,d in D.items():
    out={"mediaId":i,"lang":"fr","level":d["level"],"keyWord":d["keyWord"],"taps":d["taps"],"nouns":d["nouns"],
         "question":d["question"],"answer":d["answer"],"answerVoice":d["answerVoice"],"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(out,open(f"content/fr/{i}.json","w"),ensure_ascii=False,indent=1)
