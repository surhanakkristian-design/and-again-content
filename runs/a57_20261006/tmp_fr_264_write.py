import json
def P(t,gap=False,acc=None):
    d={"text":t}
    if gap: d["gap"]=True; d["accept"]=acc or [t]
    return d
V={}
V[264]=dict(level="B",keyWord="une émotion",
 taps=[("serrer un bouquet contre son cœur","la femme","female"),("s'appuyer sur la rambarde","la femme","female"),("pousser un chariot à bagages","l'homme","male")],
 nouns=[("le bouquet","female"),("le gilet","female"),("la rambarde","female"),("le jean","female")],
 question="Que tient la femme ?",answer="Elle serre un bouquet de fleurs jaunes.",answerVoice="female",
 recall=[("taps",[P("serrer",True,["serrer"]),P("un bouquet contre son cœur")]),
         ("taps",[P("s'appuyer sur la"),P("rambarde",True,["rambarde","barrière"])]),
         ("taps",[P("pousser un"),P("chariot",True,["chariot"]),P("à bagages")]),
         ("answer",[P("serre un"),P("bouquet",True,["bouquet"]),P("de fleurs jaunes")])],
 notes="Key word 'une émotion' is not a visible thing, so it appears in no exercise. English 'jeans' -> 'le jean' (French singular). Phrase 1 written for the boxed frames where she holds the bouquet at her chest; in the hug frames she still holds it.")
V[265]=dict(level="A",keyWord="un employé",
 taps=[("recevoir une enveloppe","le garçon à lunettes","male"),("mettre sa veste","le garçon à lunettes","male"),("lui toucher l'épaule","la femme","female")],
 nouns=[("l'employé","male"),("les papiers","male"),("le clavier","male"),("la fenêtre","male")],
 question="Que reçoit l'employé ?",answer="Il reçoit une enveloppe.",answerVoice="male",
 recall=[("taps",[P("recevoir une"),P("enveloppe",True)]),
         ("taps",[P("mettre sa"),P("veste",True)]),
         ("taps",[P("lui"),P("toucher",True),P("l'épaule")]),
         ("answer",[P("reçoit",True),P("une enveloppe")])],
 notes="Key word noun 'l'employé' is elided, so it cannot be gapped in a noun row; it is in the nouns and the question only. English 'paper' (stacks of sheets) -> 'les papiers'.")
V[266]=dict(level="A",keyWord="l'énergie",
 taps=[("monter les marches en courant","la femme en blanc","female"),("sauter sur place","la femme en blanc","female"),("poser les mains sur les genoux","l'homme","male")],
 nouns=[("les marches","female"),("le lampadaire","female"),("le mur","female"),("le ciel","female")],
 question="Que fait la femme en blanc ?",answer="Elle monte les marches en courant.",answerVoice="female",
 recall=[("taps",[P("monter les"),P("marches",True),P("en courant")]),
         ("taps",[P("sauter",True,["sauter","bondir"]),P("sur place")]),
         ("taps",[P("poser les mains sur les"),P("genoux",True)]),
         ("answer",[P("monte",True),P("les marches en courant")])],
 notes="Key word 'l'énergie' is not a visible thing, so it appears in no exercise. Phrase 3: other exhausted people in the background also bend over with hands on knees, as in English; the blue box marks the man.")
V[267]=dict(level="A",keyWord="un ingénieur",
 taps=[("construire un robot","le garçon en noir","male"),("prendre un cube blanc","le robot","male"),("taper dans ses mains","l'homme en blouse blanche","male")],
 nouns=[("l'ingénieur","male"),("le robot","male"),("l'ordinateur portable","male"),("la boîte","male")],
 question="Que fait l'ingénieur ?",answer="Il construit un petit robot.",answerVoice="male",
 recall=[("taps",[P("construire",True,["construire","monter"]),P("un robot")]),
         ("taps",[P("prendre un"),P("cube",True),P("blanc")]),
         ("taps",[P("taper dans ses"),P("mains",True)]),
         ("answer",[P("construit un petit"),P("robot",True)])],
 notes="Key word noun 'l'ingénieur' is elided, so no noun row; it is in the nouns and the question. English 'a box' is a clear plastic tray: 'la boîte' kept for level A ('le bac' would be more exact). Phrase-1 box also covers frames where he types on the laptop. 'l'ordinateur portable' (not 'le portable' = phone in France).")
V[268]=dict(level="A",keyWord="une enveloppe",
 taps=[("embrasser l'enveloppe","la femme en rouge","female"),("tenir une bougie","la femme en rouge","female"),("dormir derrière la lampe","le chat","female")],
 nouns=[("la lampe","female"),("le chat","female"),("la bougie","female"),("l'enveloppe","female")],
 question="Que fait la femme en rouge ?",answer="Elle donne un bisou à l'enveloppe.",answerVoice="female",
 recall=[("taps",[P("embrasser",True,["embrasser"]),P("l'enveloppe")]),
         ("taps",[P("tenir une"),P("bougie",True)]),
         ("taps",[P("dormir",True),P("derrière la lampe")]),
         ("answer",[P("donne un"),P("bisou",True,["bisou","baiser"]),P("à l'enveloppe")])],
 notes="Key word 'l'enveloppe' is elided, so it is never a gap; it stands in tap row 1 and the answer row. Answer uses 'donner un bisou' so its row differs from tap row 1. Phrase-1 box also covers folding the letter and sealing; written for the kiss, as in English. Question asks 'Que fait' (English asks what she kisses).")
for i,v in V.items():
    d={"mediaId":i,"lang":"fr","level":v["level"],"keyWord":v["keyWord"],
       "taps":[{"phrase":a,"target":b,"voice":c} for a,b,c in v["taps"]],
       "nouns":[{"word":a,"voice":b} for a,b in v["nouns"]],
       "question":v["question"],"answer":v["answer"].split(),"answerVoice":v["answerVoice"],"carousel":[],
       "recall":[{"from":f,"parts":p} for f,p in v["recall"]],"notes":v["notes"]}
    json.dump(d,open(f"content/fr/{i}.json","w"),ensure_ascii=False,indent=1)
