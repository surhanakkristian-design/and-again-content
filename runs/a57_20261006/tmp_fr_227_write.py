import json
def g(t,acc=None): return {"text":t,"gap":True,"accept":acc or [t]}
def p(t): return {"text":t}
def tap(ph,tg,v): return {"phrase":ph,"target":tg,"voice":v}
def n(w,v): return {"word":w,"voice":v}
C={}
C[227]=dict(level="B",keyWord="le diamant",
 taps=[tap("manipuler le diamant avec une pince","la bijoutière","female"),
       tap("rester bouche bée","la femme rousse","female"),
       tap("se prélasser à la fenêtre","le chat","female")],
 nouns=[n("le diamant","female"),n("le coussin","female"),n("le chat","female"),n("la chaîne","female")],
 question="Que fixe la femme rousse ?",answer=["Elle","fixe","un","diamant","étincelant."],answerVoice="female",
 recall=[{"from":"taps","parts":[p("manipuler le"),g("diamant"),p("avec une pince")]},
         {"from":"taps","parts":[p("rester"),g("bouche bée")]},
         {"from":"taps","parts":[p("se prélasser à la"),g("fenêtre")]},
         {"from":"answer","parts":[p("fixe un diamant"),g("étincelant",["étincelant","brillant"])]}],
 notes="Phrase 1: the English 'magnifying glass' is the loupe, at her eye only in a few boxed frames; in most boxed frames she handles the diamond with tweezers, so 'manipuler le diamant avec une pince'. The diamond pill sits on the ring's stone. Key word in phrase 1, so no noun row.")
C[228]=dict(level="A",keyWord="le dîner",
 taps=[tap("porter une casserole chaude","la femme à la casserole","female"),
       tap("allumer une bougie","l'homme","male"),
       tap("être assis sur le mur","le chat","female")],
 nouns=[n("le chat","female"),n("la casserole","female"),n("la salade","female"),n("le pain","female")],
 question="Que font les gens ?",answer=["Ils","dînent","ensemble."],answerVoice="female",
 recall=[{"from":"taps","parts":[p("porter une"),g("casserole"),p("chaude")]},
         {"from":"taps","parts":[g("allumer"),p("une bougie")]},
         {"from":"taps","parts":[p("être assis sur le"),g("mur",["mur","muret"])]},
         {"from":"answer","parts":[g("dînent",["dînent","mangent"]),p("ensemble")]}],
 notes="Phrase 1: the red box also covers later frames where the woman sits and eats; she carries the pot in the boxed frames where she stands. Phrase 2: the man lights the candle only in the first boxed frames; later he passes bread, pours water, toasts and eats (no single other action dominates, so the English action is kept). Key word le dîner appears only as the verb dîner in the answer; it is not one of the nouns, so no noun row. 'la casserole' chosen over 'la marmite' / 'la cocotte' for level A.")
C[229]=dict(level="B",keyWord="le diplôme",
 taps=[tap("traverser l'estrade","le diplômé","male"),
       tap("féliciter le diplômé","le monsieur âgé","male"),
       tap("être noué d'un ruban","le diplôme","male")],
 nouns=[n("le diplôme","male"),n("le chapeau de diplômé","male"),n("la toge","male"),n("l'étole","male")],
 question="Que fait le diplômé ?",answer=["Il","brandit","son","diplôme","au-dessus","de","sa","tête."],answerVoice="male",
 recall=[{"from":"taps","parts":[g("traverser"),p("l'estrade")]},
         {"from":"taps","parts":[g("féliciter"),p("le diplômé")]},
         {"from":"taps","parts":[p("être noué d'un"),g("ruban")]},
         {"from":"answer","parts":[p("brandit son"),g("diplôme"),p("au-dessus de sa tête")]}],
 notes="Phrase 1: in the last boxed frames the graduate stands on the stage lifting the diploma rather than crossing it. Phrase 2: the visible act is the handshake; 'serrer la main' avoided because the graduate does it too. Cap = 'le chapeau de diplômé' (formal: 'le mortier'); the gold band is a graduation stole, so 'l'étole' (not 'l'écharpe'). Key word in the answer, so no noun row.")
C[231]=dict(level="B",keyWord="décevoir",
 taps=[tap("fondre en larmes","la femme","female"),
       tap("décevoir la femme","l'homme","male"),
       tap("vaciller sur la table","la bougie","female")],
 nouns=[n("les guirlandes lumineuses","female"),n("la bougie","female"),n("les spaghettis","female"),n("le cadeau","female")],
 question="Que fait la femme ?",answer=["Elle","fond","en","larmes","à","table."],answerVoice="female",
 recall=[{"from":"taps","parts":[p("fondre en"),g("larmes")]},
         {"from":"taps","parts":[g("décevoir"),p("la femme")]},
         {"from":"taps","parts":[g("vaciller"),p("sur la table")]},
         {"from":"answer","parts":[g("fond"),p("en larmes à table")]}],
 notes="Phrase 2: the English 'pat her shoulder' is visible only in a few boxed frames; in most he arrives, points at his watch and apologises, and she ends up in tears, so the key word is used: 'décevoir la femme' (visible through her reaction, verifier please check). Phrase 1: in the first boxed frames the woman is still happy; in the last ones she sits sad with her chin in her hand.")
C[232]=dict(level="B",keyWord="déçu",
 taps=[tap("se frotter les mains d'impatience","l'homme à l'imperméable","male"),
       tap("avoir l'air profondément déçu","l'homme à l'imperméable","male"),
       tap("contenir une portion minuscule","la barquette de l'homme","male")],
 nouns=[n("le bonnet","male"),n("la barbe","male"),n("l'imperméable","male"),n("la barquette","male")],
 question="Quel air a l'homme au premier plan ?",answer=["Il","a","l'air","déçu","par","sa","barquette","vide."],answerVoice="male",
 recall=[{"from":"taps","parts":[p("se"),g("frotter"),p("les mains d'impatience")]},
         {"from":"taps","parts":[p("avoir l'air profondément"),g("déçu")]},
         {"from":"taps","parts":[p("contenir une portion"),g("minuscule",["minuscule","toute petite"])]},
         {"from":"answer","parts":[p("a l'air déçu par sa"),g("barquette"),p("vide")]}],
 notes="Phrases 1 and 2 share the same target (as in English). He rubs his hands only in the first boxed frames. The tray is a disposable street-food tray: 'la barquette' (the everyday French word), used for the noun, phrase 3 and the answer. Raincoat noun 'l'imperméable' (it is the shiny 'ciré' type; target named 'l'homme à l'imperméable' for the verifier only - could be unified to 'l'imperméable').")
for i,c in C.items():
    d={"mediaId":i,"lang":"fr"}; d.update(c); d["carousel"]=[]
    d={k:d[k] for k in ["mediaId","lang","level","keyWord","taps","nouns","question","answer","answerVoice","carousel","recall","notes"]}
    json.dump(d,open(f"content/fr/{i}.json","w"),ensure_ascii=False,indent=1)
