import json
def g(t,acc=None): return {"text":t,"gap":True,"accept":acc or [t]}
def p(t): return {"text":t}
def tap(ph,tg,v): return {"phrase":ph,"target":tg,"voice":v}
def n(w,v): return {"word":w,"voice":v}
D={}
D[233]=dict(level="B",keyWord="luxer",
 taps=[tap("se tenir l'épaule blessée","l'homme","male"),tap("s'agenouiller à côté du grimpeur","la femme","female"),tap("être enroulée dans l'herbe","la corde","male")],
 nouns=[n("le casque","male"),n("l'épaule","male"),n("la veste","male"),n("l'herbe","male")],
 question="Que fait l'homme ?",answer=["Il","se","tient","l'épaule","blessée."],answerVoice="male",
 recall=[{"from":"taps","parts":[p("se tenir l'épaule"),g("blessée")]},
  {"from":"taps","parts":[p("s'agenouiller à côté du"),g("grimpeur")]},
  {"from":"taps","parts":[p("être"),g("enroulée"),p("dans l'herbe")]},
  {"from":"answer","parts":[p("se"),g("tient"),p("l'épaule blessée")]}],
 notes="Key word 'luxer' is not used in the texts: the clip shows the injury but 'luxer' is medical and the man's action is holding his shoulder; 'se luxer l'épaule' would be the natural collocation if the owner wants it in. The red box also covers the opening frames (jump, fall, on all fours) where he does not yet hold his shoulder; phrase 1 is what he does in most boxed frames. The elided key-part words (l'épaule, s'agenouiller, l'herbe) are never gaps.")
D[235]=dict(level="B",keyWord="rapporter",
 taps=[tap("rapporter une balle rouge","le chien","female"),tap("caresser le ventre du chien","la femme","female"),tap("être chargé de pommes rouges","le pommier","female")],
 nouns=[n("le pommier","female"),n("la clôture","female"),n("le chien","female"),n("la pelouse","female")],
 question="Que fait le chien ?",answer=["Le","chien","rapporte","une","balle","rouge."],answerVoice="female",
 recall=[{"from":"taps","parts":[g("rapporter"),p("une balle rouge")]},
  {"from":"taps","parts":[p("caresser le"),g("ventre"),p("du chien")]},
  {"from":"taps","parts":[p("être"),g("chargé"),p("de pommes rouges")]},
  {"from":"answer","parts":[p("rapporte une"),g("balle"),p("rouge")]}],
 notes="The woman's box also covers early frames where only her hand holds/throws the ball; she rubs the dog's belly in the last frames. 'être chargé de' (laden with) gives the tree phrase a B1 collocation; target 'le pommier' = English 'the tree'.")
D[237]=dict(level="A",keyWord="un âne",
 taps=[tap("ouvrir grand la bouche","l'âne","male"),tap("se rouler par terre","l'âne","male"),tap("chercher à manger près de l'âne","les oiseaux","male")],
 nouns=[n("les oranges","male"),n("la maison","male"),n("l'âne","male"),n("les oiseaux","male")],
 question="Que fait l'âne ?",answer=["L'âne","se","roule","par","terre."],answerVoice="male",
 recall=[{"from":"taps","parts":[g("ouvrir"),p("grand la bouche")]},
  {"from":"taps","parts":[p("se"),g("rouler"),p("par terre")]},
  {"from":"taps","parts":[p("chercher à"),g("manger"),p("près de l'âne")]},
  {"from":"answer","parts":[p("se roule par"),g("terre")]}],
 notes="keyWord copied as in the database ('un âne', indefinite article); the noun pill uses 'l'âne'. A separate noun row 'l'âne' cannot be cut into 2 parts without splitting the elision, so phrase 3 says 'près de l'âne' (the birds peck on the cobbles beside the donkey) and carries the key word; it cannot be the gap (elided). Phrase 1's box covers the whole clip; the donkey opens its mouth wide (braying) in the middle frames, in other boxed frames it stands, rolls or trots. Phrase 1 and 2 share the target, as in English.")
D[238]=dict(level="A",keyWord="voler",
 taps=[tap("voler une canette","l'homme","male"),tap("porter un sac blanc","l'homme","male"),tap("avoir des fleurs roses","le buisson","male")],
 nouns=[n("le ciel","male"),n("les fleurs","male"),n("l'herbe","male"),n("les canettes","male")],
 question="Que fait l'homme ?",answer=["Il","vole","une","canette."],answerVoice="male",
 recall=[{"from":"taps","parts":[p("voler une"),g("canette")]},
  {"from":"taps","parts":[p("porter un"),g("sac"),p("blanc")]},
  {"from":"taps","parts":[p("avoir des"),g("fleurs"),p("roses")]},
  {"from":"answer","parts":[g("vole"),p("une canette")]}],
 notes="Phrase 2's box covers frames after he has put the white bag down next to the cans (he then carries a can); he carries the bag on the way in. Phrase 1's box includes the approach frames before the theft.")
D[239]=dict(level="B",keyWord="douter",
 taps=[tap("examiner une bague en or","l'homme","male"),tap("adresser un grand sourire au client","la vieille dame","female"),tap("froncer les sourcils d'un air sceptique","l'homme","male")],
 nouns=[n("la bague","male"),n("le foulard","male"),n("la veste","male"),n("les nuages","male")],
 question="Qu'est-ce que l'homme examine ?",answer=["Il","examine","une","bague","en","or."],answerVoice="male",
 recall=[{"from":"taps","parts":[p("examiner une"),g("bague"),p("en or")]},
  {"from":"taps","parts":[p("adresser un grand"),g("sourire"),p("au client")]},
  {"from":"taps","parts":[p("froncer les sourcils d'un air"),g("sceptique",["sceptique","dubitatif"])]},
  {"from":"answer","parts":[g("examine"),p("une bague en or")]}],
 notes="Key word 'douter' is not used in the texts (the clip shows doubt, not the verb); 'd'un air sceptique' carries the meaning. Phrase 1 gaps 'bague' so it does not look like the answer row ('examine une bague en or') once blanked. The man also smiles slightly in the last frames, but only the old woman grins at the customer.")
for i,d in D.items():
    c={"mediaId":i,"lang":"fr",**{k:d[k] for k in ["level","keyWord","taps","nouns","question","answer","answerVoice"]},"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(c,open(f"content/fr/{i}.json","w"),ensure_ascii=False,indent=2)
