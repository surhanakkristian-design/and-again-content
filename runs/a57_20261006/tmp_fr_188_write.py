import json,os
def g(t,acc=None): return {"text":t,"gap":True,"accept":acc or [t]}
def p(t): return {"text":t}
def tap(ph,tg,v): return {"phrase":ph,"target":tg,"voice":v}
def n(w,v): return {"word":w,"voice":v}
D={}
D[188]=dict(level="B",keyWord="la constitution",
 taps=[tap("se pencher au-dessus de la table","le politicien","male"),tap("porter une perruque poudrée","le juge","male"),tap("porter deux sceaux de cire","le livre","male")],
 nouns=[n("la perruque","male"),n("la constitution","male"),n("le marbre","male")],
 question="Que lit le politicien ?",answer="Il lit une page de la constitution.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":[p("se"),g("pencher"),p("au-dessus de la table")]},
  {"from":"taps","parts":[p("porter une"),g("perruque"),p("poudrée")]},
  {"from":"taps","parts":[p("porter deux"),g("sceaux"),p("de cire")]},
  {"from":"answer","parts":[p("lit une page de la"),g("constitution")]}],
 notes="Tap 1: in many boxed frames the politician sits and gestures; the lean across the table is at the end (same box as English).")
D[189]=dict(level="B",keyWord="le convoi",
 taps=[tap("mener le convoi","la voiture grise","male"),tap("se garer entre deux véhicules","la voiture noire","male"),tap("fermer la marche","la voiture blanche","male")],
 nouns=[n("le convoi","male"),n("les arbres","male"),n("l'asphalte","male"),n("le ciel","male")],
 question="Que font les trois voitures ?",answer="Elles roulent en convoi.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":[g("mener",["mener","diriger"]),p("le convoi")]},
  {"from":"taps","parts":[p("se garer entre deux"),g("véhicules",["véhicules","voitures"])]},
  {"from":"taps","parts":[g("fermer"),p("la marche")]},
  {"from":"answer","parts":[p("roulent en"),g("convoi")]}],
 notes="Subject 'elles' (les voitures) is feminine; answerVoice kept male as in English (no speaker in the clip).")
D[190]=dict(level="A",keyWord="le cookie",
 taps=[tap("manger un gros cookie","la femme","female"),tap("tenir une cuillère","l'homme","male"),tap("être couché près de la fenêtre","le chat","female")],
 nouns=[n("la fenêtre","female"),n("le chat","female"),n("les cookies","female"),n("la table","female")],
 question="Que mange la femme ?",answer="Elle mange un gros cookie.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":[p("manger un gros"),g("cookie",["cookie","biscuit"])]},
  {"from":"taps","parts":[p("tenir une"),g("cuillère")]},
  {"from":"taps","parts":[p("être"),g("couché",["couché","allongé"]),p("près de la fenêtre")]},
  {"from":"answer","parts":[g("mange"),p("un gros cookie")]}],
 notes="")
D[191]=dict(level="B",keyWord="le tire-bouchon",
 taps=[tap("renifler le bouchon","l'homme","male"),tap("s'enfoncer dans le bouchon","le tire-bouchon","male"),tap("porter une chemise à manches longues","la femme","female")],
 nouns=[n("le tire-bouchon","male"),n("le bouchon","male"),n("la bouteille","male"),n("la marmite","male")],
 question="Comment l'homme ouvre-t-il la bouteille ?",answer="Il ouvre la bouteille avec un tire-bouchon.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":[g("renifler",["renifler","sentir"]),p("le bouchon")]},
  {"from":"taps","parts":[p("s'enfoncer dans le"),g("bouchon")]},
  {"from":"taps","parts":[p("porter une chemise à"),g("manches"),p("longues")]},
  {"from":"answer","parts":[p("ouvre la bouteille avec un"),g("tire-bouchon")]}],
 notes="Phrase 2: 's'enfoncer dans' (screw going into the cork) is the natural French for 'twist into'.")
D[192]=dict(level="A",keyWord="le coin",
 taps=[tap("rentrer dans le coin","la planche","female"),tap("porter des vêtements orange","la femme","female"),tap("porter des lunettes","l'homme","male")],
 nouns=[n("le ciel","female"),n("le coin","female"),n("la femme","female"),n("l'homme","male")],
 question="Où mettent-ils la planche ?",answer="Ils la mettent dans le coin.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":[g("rentrer",["rentrer","entrer"]),p("dans le coin")]},
  {"from":"taps","parts":[p("porter des"),g("vêtements"),p("orange")]},
  {"from":"taps","parts":[p("porter des"),g("lunettes")]},
  {"from":"answer","parts":[p("la mettent dans le"),g("coin")]}],
 notes="Subject 'ils' = the woman and the man; answerVoice kept female as in English.")
os.makedirs("content/fr",exist_ok=True)
for k,v in D.items():
  o={"mediaId":k,"lang":"fr",**{x:v[x] for x in ["level","keyWord","taps","nouns","question","answer","answerVoice"]},"carousel":[],"recall":v["recall"],"notes":v["notes"]}
  json.dump(o,open(f"content/fr/{k}.json","w"),ensure_ascii=False,indent=1)
