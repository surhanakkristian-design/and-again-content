import json
def g(t,acc=None): return {"text":t,"gap":True,"accept":acc or [t]}
def p(t): return {"text":t}
def tap(ph,t,v): return {"phrase":ph,"target":t,"voice":v}
def n(w,v): return {"word":w,"voice":v}
D={}
D[210]=dict(level="A",keyWord="le client",
 taps=[tap("essayer un casque","la cliente","female"),tap("remplir un sac en papier","le vendeur","male"),tap("tenir deux boîtes","la cliente","female")],
 nouns=[n("la cliente","female"),n("le sac","female"),n("la carte","female"),n("le casque","female")],
 question="Que fait la cliente ?",answer="Elle essaie un casque blanc.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":[g("essayer"),p("un casque")]},
  {"from":"taps","parts":[p("remplir un"),g("sac"),p("en papier")]},
  {"from":"taps","parts":[p("tenir deux"),g("boîtes")]},
  {"from":"nouns","parts":[p("la"),g("cliente")]},
  {"from":"answer","parts":[p("essaie un"),g("casque"),p("blanc")]}],
 notes="keyWord le client: the customer is a woman, so the noun pill and question use the feminine 'la cliente' (same entry). Tap 2: the man puts the box into the paper bag at the counter.")
D[211]=dict(level="B",keyWord="la douane",
 taps=[tap("fouiller une valise","le douanier","male"),tap("joindre les mains","la fille","female"),tap("être couvert de piquants","le durian","female")],
 nouns=[n("le durian","female"),n("la valise","female"),n("la poubelle","female"),n("le douanier","male")],
 question="Que fait le douanier ?",answer="Le douanier fouille une valise.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":[g("fouiller",["fouiller","inspecter"]),p("une valise")]},
  {"from":"taps","parts":[g("joindre"),p("les mains")]},
  {"from":"taps","parts":[p("être couvert de"),g("piquants",["piquants","épines"])]},
  {"from":"answer","parts":[p("fouille une"),g("valise")]}],
 notes="keyWord la douane is not shown as a noun of the set; the English noun 'customs officer' is 'le douanier' (derived from douane), so no noun recall row. 'le durian' is above B level but the only word for the fruit.")
D[212]=dict(level="A",keyWord="le danseur",
 taps=[tap("étirer sa jambe","la danseuse","female"),tap("danser dans un studio","la danseuse","female"),tap("sourire à la caméra","la danseuse","female")],
 nouns=[n("la danseuse","female"),n("le miroir","female"),n("l'enceinte","female"),n("le sol","female")],
 question="Que fait la danseuse ?",answer="Elle danse dans un studio.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":[p("étirer sa"),g("jambe")]},
  {"from":"taps","parts":[g("danser"),p("dans un studio")]},
  {"from":"taps","parts":[g("sourire"),p("à la caméra")]},
  {"from":"nouns","parts":[p("la"),g("danseuse")]},
  {"from":"answer","parts":[p("danse dans un"),g("studio")]}],
 notes="keyWord le danseur: the dancer is a woman, so the pill and question use the feminine 'la danseuse' (same entry). Gaps of tap 2 and the answer row differ so the blanked rows are not identical.")
D[213]=dict(level="A",keyWord="la danse",
 taps=[tap("faire la cuisine","la femme","female"),tap("tenir la femme","l'homme","male"),tap("porter une jupe longue","la femme","female")],
 nouns=[n("la femme","female"),n("l'homme","male"),n("la radio","female"),n("le sol","female")],
 question="Que font l'homme et la femme ?",answer="Ils dansent dans la cuisine.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":[p("faire la"),g("cuisine")]},
  {"from":"taps","parts":[g("tenir"),p("la femme")]},
  {"from":"taps","parts":[p("porter une"),g("jupe"),p("longue")]},
  {"from":"answer","parts":[g("dansent"),p("dans la cuisine")]}],
 notes="keyWord la danse (noun) is not a noun of the set; the answer uses the verb 'danser'. Answer subject 'Ils' is masculine plural (mixed couple); answerVoice kept female as in English.")
D[214]=dict(level="A",keyWord="dangereux",
 taps=[tap("marcher sur la glace","le garçon","male"),tap("tirer son ami en arrière","la fille","female"),tap("se casser en morceaux","la glace","male")],
 nouns=[n("le panneau","male"),n("l'arbre","male"),n("le garçon","male"),n("la glace","male")],
 question="Que fait le garçon ?",answer="Le garçon marche sur une glace dangereuse.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":[g("marcher"),p("sur la glace")]},
  {"from":"taps","parts":[g("tirer"),p("son ami en arrière")]},
  {"from":"taps","parts":[p("se casser en"),g("morceaux")]},
  {"from":"answer","parts":[p("marche sur une glace"),g("dangereuse")]}],
 notes="Key word as adjective in the answer ('une glace dangereuse', feminine agreement).")
for i,d in D.items():
    o={"mediaId":i,"lang":"fr"}; o.update(d); o["carousel"]=[]
    o={k:o[k] for k in ["mediaId","lang","level","keyWord","taps","nouns","question","answer","answerVoice","carousel","recall","notes"]}
    json.dump(o,open(f"content/fr/{i}.json","w"),ensure_ascii=False,indent=1)
