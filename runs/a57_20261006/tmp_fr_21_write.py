import json
def g(t,acc=None): return {"text":t,"gap":True,"accept":[t]+(acc or [])}
def p(t): return {"text":t}
def T(ph,tg,v): return {"phrase":ph,"target":tg,"voice":v}
def N(w,v): return {"word":w,"voice":v}
C={}
C[21]=dict(level="A",keyWord="une école",
 taps=[T("ouvrir la porte de l'école","la main","male"),T("être assis autour des tables","les élèves","male"),T("avoir beaucoup de fenêtres","le bâtiment de l'école","male")],
 nouns=[N("le ciel","male"),N("l'école","male"),N("la pelouse","male")],
 question="Que font les élèves ?",answer="Ils sont assis autour des tables.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":[p("ouvrir la"),g("porte"),p("de l'école")]},
  {"from":"taps","parts":[p("être"),g("assis"),p("autour des tables")]},
  {"from":"taps","parts":[p("avoir beaucoup de"),g("fenêtres")]},
  {"from":"answer","parts":[p("sont assis autour des"),g("tables")]}],
 notes="keyWord 'une école' copied unchanged (indefinite article); the noun pill uses 'l'école'. Phrase 1 says 'la porte de l'école' (the entrance doors) so the key word sits in a tap row; no noun row because 'l'école' is elided and cannot be gapped. 'la pelouse' for the mowed lawn (English 'grass'). Students look older but 'les élèves' is the A-level school word.")
C[22]=dict(level="A",keyWord="le scientifique",
 taps=[T("passer devant l'affiche","l'étudiant","male"),T("prendre des notes","le scientifique","male"),T("montrer une ligne du doigt","le scientifique","male")],
 nouns=[N("le scientifique","male"),N("les lunettes","male"),N("le stylo","male"),N("l'affiche","male")],
 question="Que fait le scientifique ?",answer="Le scientifique prend des notes.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":[g("passer"),p("devant l'affiche")]},
  {"from":"taps","parts":[p("prendre des"),g("notes")]},
  {"from":"taps","parts":[p("montrer une"),g("ligne",["courbe"]),p("du doigt")]},
  {"from":"nouns","parts":[p("le"),g("scientifique")]},
  {"from":"answer","parts":[g("prend",["écrit"]),p("des notes")]}],
 notes="'les lunettes' are safety glasses pushed up on his head (A-level word kept plain). 'l'affiche' for the research poster ('le poster' is also used in France).")
C[23]=dict(level="A",keyWord="le discours",
 taps=[T("faire un discours","la femme en vert","female"),T("boire de l'eau","la femme en vert","female"),T("porter un costume gris","l'homme en gris","male")],
 nouns=[N("les fenêtres","female"),N("la femme","female"),N("le micro","female"),N("le verre","female")],
 question="Que fait la femme en vert ?",answer="Elle fait un discours.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":[g("faire"),p("un discours")]},
  {"from":"taps","parts":[g("boire"),p("de l'eau")]},
  {"from":"taps","parts":[p("porter un"),g("costume"),p("gris")]},
  {"from":"answer","parts":[p("fait un"),g("discours")]}],
 notes="'le micro' is the everyday word for the microphone.")
C[24]=dict(level="A",keyWord="la cuillère",
 taps=[T("ouvrir un tiroir","la fille","female"),T("prendre une cuillère","la fille","female"),T("manger de la soupe","la fille","female")],
 nouns=[N("la fenêtre","female"),N("la cuillère","female"),N("le bol","female"),N("la table","female")],
 question="Que fait la fille ?",answer="Elle mange de la soupe avec une cuillère.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":[p("ouvrir un"),g("tiroir")]},
  {"from":"taps","parts":[p("prendre une"),g("cuillère")]},
  {"from":"taps","parts":[g("manger"),p("de la soupe")]},
  {"from":"answer","parts":[p("mange de la"),g("soupe"),p("avec une cuillère")]}],
 notes="")
C[25]=dict(level="A",keyWord="une agrafeuse",
 taps=[T("utiliser une agrafeuse rouge","l'homme","male"),T("soulever le papier","l'homme","male"),T("ouvrir l'agrafeuse","l'homme","male")],
 nouns=[N("l'homme","male"),N("la plante","male"),N("l'agrafeuse","male"),N("le papier","male")],
 question="Que fait l'homme ?",answer="Il utilise une agrafeuse rouge.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":[p("utiliser une"),g("agrafeuse"),p("rouge")]},
  {"from":"taps","parts":[g("soulever",["lever"]),p("le papier")]},
  {"from":"taps","parts":[g("ouvrir"),p("l'agrafeuse")]},
  {"from":"answer","parts":[g("utilise"),p("une agrafeuse rouge")]}],
 notes="keyWord 'une agrafeuse' copied unchanged (indefinite article); the noun pill uses 'l'agrafeuse'.")
for i,c in C.items():
    d={"mediaId":i,"lang":"fr","level":c["level"],"keyWord":c["keyWord"],"taps":c["taps"],"nouns":c["nouns"],"question":c["question"],
       "answer":c["answer"],"answerVoice":c["answerVoice"],"carousel":[],"recall":c["recall"],"notes":c["notes"]}
    json.dump(d,open(f"content/fr/{i}.json","w"),ensure_ascii=False,indent=1)
