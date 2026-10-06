import json
def t(p,tg,v): return {"phrase":p,"target":tg,"voice":v}
def n(w,v): return {"word":w,"voice":v}
def row(f,*ps):
    out=[]
    for p in ps:
        if isinstance(p,tuple): out.append({"text":p[0],"gap":True,"accept":list(p[1])})
        else: out.append({"text":p})
    return {"from":f,"parts":out}
D={}
D[253]=dict(level="A",keyWord="l'époussetage",
 taps=[t("nettoyer le haut de la porte","l'homme","male"),t("porter un foulard gris","la femme","female"),t("marcher sur l'étagère","le chat","male")],
 nouns=[n("le chat","male"),n("les livres","male"),n("l'étagère","male"),n("la lampe","male")],
 question="Que fait l'homme ?",answer=["Il","nettoie","le","haut","de","la","porte."],answerVoice="male",
 recall=[row("taps",("nettoyer",["nettoyer","essuyer"]),"le haut de la porte"),row("taps","porter un",("foulard",["foulard"]),"gris"),
         row("taps",("marcher",["marcher"]),"sur l'étagère"),row("answer","nettoie le haut de la",("porte",["porte"]))],
 notes="Key word 'l'époussetage' is above level A and rare in everyday French; natives say 'faire la poussière' / 'épousseter'. Proposal: key word 'faire la poussière'. Not forced into the texts. The man wipes the top of the door frame with a cloth: 'le haut de la porte' kept simple for level A instead of 'le chambranle'. The man's box also covers gasp, dust cloud and thumbs-up moments shared with the woman; the door moment is the distinctive one. Grey hijab -> 'foulard gris'. No noun row: the key word is not one of the nouns.")
D[254]=dict(level="A",keyWord="la Terre",
 taps=[t("arrêter le globe qui tourne","la femme","female"),t("avoir les cheveux bouclés","l'homme","male"),t("dormir près de la fenêtre","le chat","female")],
 nouns=[n("le soleil","female"),n("la mer","female"),n("le chat","female"),n("le globe","female")],
 question="Que fait le chat ?",answer=["Le","chat","dort","près","de","la","fenêtre."],answerVoice="female",
 recall=[row("taps","arrêter le",("globe",["globe"]),"qui tourne"),row("taps","avoir les cheveux",("bouclés",["bouclés"])),
         row("taps",("dormir",["dormir"]),"près de la fenêtre"),row("answer","dort près de la",("fenêtre",["fenêtre"]))],
 notes="Key word 'la Terre' (the planet) is not named in any exercise: the clip shows a desk globe ('le globe'), not the planet itself; not forced. The woman's hair is dark and straight, the man's dark and curly, so 'les cheveux bouclés' fits only him. No noun row: the key word is not one of the nouns.")
D[255]=dict(level="A",keyWord="l'est",
 taps=[t("montrer le ciel du doigt","la femme","female"),t("se lever à l'est","le soleil","female"),t("lever les bras","les gens","female")],
 nouns=[n("le ciel","female"),n("le soleil","female"),n("les gens","female"),n("les rochers","female")],
 question="Que fait le soleil ?",answer=["Le","soleil","se","lève","au-dessus","des","nuages."],answerVoice="female",
 recall=[row("taps","montrer le",("ciel",["ciel"]),"du doigt"),row("taps","se",("lever",["lever"]),"à l'est"),
         row("taps","lever les",("bras",["bras"])),row("answer","se lève au-dessus des",("nuages",["nuages"]))],
 notes="Key word 'l'est' used in tap 2 (elided, so the gap there is 'lever'). Tap 3: English 'raise their cups'; in the clip the group mainly cheers with raised arms (cups are hardly visible), so 'lever les bras'. No noun row: the key word is not one of the nouns and is already in tap row 2.")
D[256]=dict(level="A",keyWord="manger",
 taps=[t("sentir la soupe chaude","la jeune femme","female"),t("avoir une barbe brune","l'homme","male"),t("cuisiner dans la rue","la cuisinière","female")],
 nouns=[n("le panneau","female"),n("la barbe","female"),n("les bols","female"),n("le jean","female")],
 question="Que mangent l'homme et la femme ?",answer=["Ils","mangent","une","soupe","de","nouilles."],answerVoice="female",
 recall=[row("taps","sentir la",("soupe",["soupe"]),"chaude"),row("taps","avoir une",("barbe",["barbe"]),"brune"),
         row("taps",("cuisiner",["cuisiner"]),"dans la rue"),row("answer",("mangent",["mangent"]),"une soupe de nouilles")],
 notes="Key word 'manger' gapped in the answer row. 'a sign' -> 'le panneau' (A-level; 'l'enseigne' would be B). 'jeans' -> 'le jean' (singular in French). 'hot' dropped from the answer to keep one chip order; the soup is hot in tap 1. Answer subject 'Ils' (mixed couple); answerVoice kept female as in English. The cook in the background is a woman -> 'la cuisinière'.")
D[258]=dict(level="B",keyWord="le bord",
 taps=[t("garder l'équilibre sur des planches étroites","la personne aux cheveux bleus","female"),t("avoir une barbe rousse","l'homme","male"),t("recouvrir la pelouse","la bâche","female")],
 nouns=[n("les pins","female"),n("les rochers","female"),n("le lac","female"),n("les planches","female")],
 question="Que fait la personne aux cheveux bleus ?",answer=["Elle","garde","l'équilibre","sur","des","planches","étroites."],answerVoice="female",
 recall=[row("taps","garder l'équilibre sur des",("planches",["planches"]),"étroites"),row("taps","avoir une",("barbe",["barbe"]),"rousse"),
         row("taps",("recouvrir",["recouvrir","couvrir"]),"la pelouse"),row("answer",("garde",["garde"]),"l'équilibre sur des planches étroites")],
 notes="B1/B2 items: 'garder l'équilibre', 'étroites', 'roux/rousse', 'recouvrir', 'la pelouse', 'la bâche'. Key word 'le bord' not forced into the texts (the clip's balancing/beard/tarp frame does not name an edge). Tap 1's English box also covers the opening shots of a hand on the picnic-table rim (not balancing); phrase written for the dock frames, which are the majority. 'boulders' -> 'les rochers'. No noun row: the key word is not one of the nouns.")
for i,d in D.items():
    o={"mediaId":i,"lang":"fr",**d,"carousel":[]}
    o={k:o[k] for k in ["mediaId","lang","level","keyWord","taps","nouns","question","answer","answerVoice","carousel","recall","notes"]}
    json.dump(o,open(f"content/fr/{i}.json","w"),ensure_ascii=False,indent=2)
