import json
def G(t,acc=None): return {"text":t,"gap":True,"accept":acc or [t]}
def P(t): return {"text":t}
D={}
D[102]=dict(level="B",keyWord="l'ennui",
 taps=[("s'affaler sur une chaise en plastique","l'homme","male"),("pendre au bout de ses doigts","la chaussette","male"),("tournoyer sur le bout de son doigt","le sac de linge","male")],
 nouns=[("la chaussette","male"),("les machines à laver","male"),("le survêtement","male"),("la basket","male")],
 question="Que fait l'homme ?",answer="Il s'affale sur une chaise en plastique.",answerVoice="male",
 recall=[("taps",[P("s'affaler sur une"),G("chaise"),P("en plastique")]),
         ("taps",[G("pendre",["pendre","pendouiller"]),P("au bout de ses doigts")]),
         ("taps",[G("tournoyer",["tournoyer","tourner"]),P("sur le bout de son doigt")]),
         ("answer",[P("s'affale sur une chaise en"),G("plastique")])],
 notes="Key word 'l'ennui' (boredom) is not shown as a nameable thing and is not a noun of the set, so it appears in no exercise and there is no noun row; it is never forced. Sock box (phrase 2): in the first boxed frames (box_01) the sock floats in the air near the ceiling light, later it hangs from his fingers (box_05), lands on his head and lies in the drum. 'flotter dans les airs' would also be true of the feather, so the phrase keeps the dangling ('pendre au bout de ses doigts'), as the English does. Phrase 1: 'the man' box also covers frames where he sits on the floor, runs, or only his shoes/hand show; slumped in the chair is the most frequent. Gaps: tap row 1 'chaise', answer row 'plastique' so the two near-identical rows differ; 's'affale(r)' is elided and is not gapped.")
D[7088]=dict(level="B",keyWord="niveler",
 taps=[("tirer une longue règle","la femme","female"),("maintenir une lourde charge en l'air","la grue","female"),("travailler à genoux sur le toit","l'ouvrier à genoux","female")],
 nouns=[("la grue","female"),("le casque de chantier","female"),("le trépied","female"),("le béton","female")],
 question="Que fait la femme ?",answer="Elle nivelle le béton frais.",answerVoice="female",
 recall=[("taps",[P("tirer une longue"),G("règle")]),
         ("taps",[P("maintenir une lourde"),G("charge"),P("en l'air")]),
         ("taps",[P("travailler à"),G("genoux"),P("sur le toit")]),
         ("answer",[G("nivelle",["nivelle","égalise","lisse"]),P("le béton frais")])],
 notes="'la règle' = the straightedge (in the trade 'la règle de maçon'; plain 'règle' is the natural short form). The kneeling worker looks male; target written 'l'ouvrier à genoux', voice copied (female). Key word 'niveler' used in the model answer and gapped there.")
D[4852]=dict(level="B",keyWord="un engrenage",
 taps=[("écarquiller les yeux","l'homme","male"),("s'allumer en rouge et en vert","le circuit imprimé","male"),("être équipée d'énormes engrenages","la machine géante","male")],
 nouns=[("les lunettes de protection","male"),("les outils","male"),("le circuit imprimé","male"),("l'étau","male")],
 question="Que construit l'homme ?",answer="Il construit une machine à engrenages métalliques.",answerVoice="male",
 recall=[("taps",[G("écarquiller"),P("les yeux")]),
         ("taps",[P("s'allumer en"),G("rouge"),P("et en vert")]),
         ("taps",[P("être équipée d'énormes"),G("engrenages")]),
         ("answer",[G("construit",["construit","fabrique"]),P("une machine à engrenages métalliques")])],
 notes="Key word: source gives 'un engrenage' (indefinite article, unlike the usual definite form) - copied unchanged; proposal 'l'engrenage'. Phrase 1: 'the man' box covers the whole clip but he raises both arms only in the last 3 frames; in most boxed frames he stares at his work wide-eyed, so 'écarquiller les yeux' (true also in the arms-up frames). Phrase 2: the board lights up red and green only in the last frames of box_02; in most boxed frames it is being tightened or held up - kept the English event (no other thing lights up). Key word in tap row 3 (gapped) and in the answer.")
D[4441]=dict(level="B",keyWord="le souffle",
 taps=[("garder les yeux fermés","la femme","female"),("dominer le paysage","le sommet","female"),("être coiffé d'un bonnet blanc","la personne au bonnet blanc","female")],
 nouns=[("le ciel","female"),("le sommet","female"),("le souffle","female"),("la doudoune","female")],
 question="Que peut-on voir dans l'air ?",answer="On peut voir le souffle de la femme.",answerVoice="female",
 recall=[("taps",[P("garder les yeux"),G("fermés",["fermés","clos"])]),
         ("taps",[G("dominer",["dominer","surplomber"]),P("le paysage")]),
         ("taps",[P("être coiffé d'un"),G("bonnet"),P("blanc")]),
         ("answer",[P("peut voir le"),G("souffle"),P("de la femme")])],
 notes="Key word 'le souffle' kept for the visible white cloud; a French native would more often say 'la buée' or 'son haleine' for breath seen in the cold - 'le souffle' is still natural ('on voit son souffle'). Noun 3 = 'le souffle' (database word). Noun 4: the jacket is a puffer, 'la doudoune' is the everyday French word. 'être coiffé' agrees with 'la personne' only loosely: the person in the white hat looks male, so masculine 'coiffé' is used. No noun row: 'souffle' is already in the answer row (gapped). Phrase 3 frames: blue box on the person in the white hat only.")
D[4721]=dict(level="B",keyWord="s'estomper",
 taps=[("montrer l'arc-en-ciel du doigt","la femme","female"),("s'estomper dans le ciel gris","l'arc-en-ciel","female"),("contempler le paysage","la femme","female")],
 nouns=[("l'arc-en-ciel","female"),("le lac","female"),("l'imperméable","female"),("la flaque","female")],
 question="Qu'arrive-t-il à l'arc-en-ciel ?",answer="L'arc-en-ciel s'estompe dans le ciel.",answerVoice="female",
 recall=[("taps",[G("montrer",["montrer","désigner"]),P("l'arc-en-ciel du doigt")]),
         ("taps",[P("s'estomper dans le ciel"),G("gris")]),
         ("taps",[G("contempler",["contempler","regarder","admirer"]),P("le paysage")]),
         ("answer",[P("s'estompe dans le"),G("ciel")])],
 notes="Boxes 1 and 3 both cover the woman over the whole clip. She points only in box_01-02 (about 9 frames) and grins at the camera only in box_01-02 (8 frames); in most boxed frames (box_03-07) she has turned away and looks out at the lake and the sky. Phrase 1 keeps the pointing (English event, the only gesture shown); phrase 3 says what she does in most boxed frames ('contempler le paysage') instead of the grin. Key word 's'estomper' is elided, so it is never the gap (gaps: 'gris' in tap row 2, 'ciel' in the answer row). Raincoat = 'l'imperméable' ('le ciré' also possible).")
for i,d in D.items():
    o={"mediaId":i,"lang":"fr","level":d["level"],"keyWord":d["keyWord"],
       "taps":[{"phrase":a,"target":b,"voice":c} for a,b,c in d["taps"]],
       "nouns":[{"word":a,"voice":b} for a,b in d["nouns"]],
       "question":d["question"],"answer":d["answer"].split(" "),"answerVoice":d["answerVoice"],
       "carousel":[],"recall":[{"from":f,"parts":p} for f,p in d["recall"]],"notes":d["notes"]}
    json.dump(o,open(f"content/fr/{i}.json","w"),ensure_ascii=False,indent=2)
