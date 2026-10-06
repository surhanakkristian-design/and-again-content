import json
def P(t,g=False,acc=None):
    d={"text":t}
    if g: d["gap"]=True; d["accept"]=acc or [t]
    return d
def taps(l): return [{"phrase":p,"target":t,"voice":v} for p,t,v in l]
def nouns(l): return [{"word":w,"voice":v} for w,v in l]
V={}
V[246]=dict(level="A",keyWord="das Fahren",
 taps=taps([("Auto fahren","die Frau","female"),("das Lenkrad halten","die Frau","female"),("die Fahrerin anlächeln","der Mann","male")]),
 nouns=nouns([("der Spiegel","female"),("das Meer","female"),("die Frau","female"),("der Mann","male")]),
 question="Was macht die Frau?",answer="Sie fährt mit dem Auto am Meer entlang.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":[P("Auto"),P("fahren",1)]},
  {"from":"taps","parts":[P("das"),P("Lenkrad",1),P("halten")]},
  {"from":"taps","parts":[P("die Fahrerin"),P("anlächeln",1,["anlächeln","anlachen"])]},
  {"from":"answer","parts":[P("fährt mit dem Auto am"),P("Meer",1),P("entlang")]}],
 notes="Phrase 2: the English tap box 2 ('to wear a grey hat') is the same box as phrase 1 and shows only her hands on the steering wheel in most boxed frames (the hat is visible only in the last seconds), so the phrase says what she does there: 'das Lenkrad halten'. Noun 1 is the rear-view mirror: 'der Spiegel' (A-level) rather than 'der Rückspiegel'. Key word 'das Fahren' is the noun; the phrase uses the verb 'Auto fahren' and the answer 'fährt'; not a noun of the set, so no noun row. Answer: German also allows 'Sie fährt am Meer mit dem Auto entlang' (less natural).")
V[248]=dict(level="B",keyWord="die Pipette",
 taps=taps([("die Tropfen genau abmessen","die Frau","female"),("die Medizin einnehmen","der Mann","male"),("Dampf abgeben","der Kupferkessel","female")]),
 nouns=nouns([("die Pipette","female"),("der Holzlöffel","female"),("die Schürze","female")]),
 question="Was macht die Frau?",answer="Sie misst mit der Pipette die Tropfen ab.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":[P("die Tropfen genau"),P("abmessen",1,["abmessen","abzählen"])]},
  {"from":"taps","parts":[P("die"),P("Medizin",1,["Medizin","Arznei"]),P("einnehmen")]},
  {"from":"taps","parts":[P("Dampf",1),P("abgeben")]},
  {"from":"answer","parts":[P("misst mit der"),P("Pipette",1),P("die Tropfen ab")]}],
 notes="Target 3 is the copper kettle ('der Kupferkessel'; a native could also say 'der Wasserkessel'). Answer: German also allows 'Sie misst die Tropfen mit der Pipette ab' (two orders). Key word 'die Pipette' is in the answer row, so no separate noun row.")
V[250]=dict(level="A",keyWord="die Ente",
 taps=taps([("den Kopf unter Wasser stecken","die Ente","female"),("die Flügel ausbreiten","die Ente","female"),("den Schnabel aufmachen","die Ente","female")]),
 nouns=nouns([("die Ente","female"),("die Bäume","female"),("das Wasser","female")]),
 question="Was macht die Ente?",answer="Die Ente schwimmt auf dem Wasser.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":[P("den"),P("Kopf",1),P("unter Wasser stecken")]},
  {"from":"taps","parts":[P("die Flügel"),P("ausbreiten",1,["ausbreiten","öffnen","aufmachen"])]},
  {"from":"taps","parts":[P("den"),P("Schnabel",1),P("aufmachen")]},
  {"from":"nouns","parts":[P("die"),P("Ente",1)]},
  {"from":"answer","parts":[P("schwimmt",1),P("auf dem Wasser")]}],
 notes="English 'to open its mouth' -> 'den Schnabel aufmachen' (a duck has a beak in German). All three English boxes cover the whole duck for the whole clip; each phrase is true only in part of it (head under water early, wings in the middle, beak open at the end).")
V[251]=dict(level="B",keyWord="die Hantel",
 taps=taps([("den Bizeps trainieren","der Mann","male"),("an ihrem Kaffee nippen","die Frau","female"),("im Schneidersitz sitzen","die Frau","female")]),
 nouns=nouns([("die Hantel","male"),("die Palme","male"),("der Sessel","male"),("das Fenster","male")]),
 question="Was macht der Mann?",answer="Er stemmt eine schwere Hantel.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":[P("den Bizeps"),P("trainieren",1)]},
  {"from":"taps","parts":[P("an ihrem Kaffee"),P("nippen",1)]},
  {"from":"taps","parts":[P("im"),P("Schneidersitz",1),P("sitzen")]},
  {"from":"answer","parts":[P("stemmt eine schwere"),P("Hantel",1)]}],
 notes="Answer uses 'stemmen' (B2) rather than the gym loanword 'Bizepscurls': he curls and also presses the dumbbell overhead. Key word 'die Hantel' is in the answer row, so no separate noun row.")
V[252]=dict(level="A",keyWord="der Staub",
 taps=taps([("auf einen Koffer pusten","der Mann","male"),("einen Finger hochhalten","die Frau","female"),("hoch oben sitzen","der Vogel","female")]),
 nouns=nouns([("der Staub","female"),("der Mann","male"),("die Frau","female"),("der Koffer","female")]),
 question="Was macht der Mann?",answer="Er pustet den Staub vom Koffer.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":[P("auf einen Koffer"),P("pusten",1,["pusten","blasen"])]},
  {"from":"taps","parts":[P("einen"),P("Finger",1),P("hochhalten")]},
  {"from":"taps","parts":[P("hoch oben"),P("sitzen",1)]},
  {"from":"answer","parts":[P("pustet den"),P("Staub",1),P("vom Koffer")]}],
 notes="Phrase 2: the woman's box also covers the start (her finger drawing a line through the dust on the shelf) and the end (she laughs); she holds up one finger in most boxed frames. Key word 'der Staub' is in the answer row, so no separate noun row.")
for i,v in V.items():
    d={"mediaId":i,"lang":"de","level":v["level"],"keyWord":v["keyWord"],"taps":v["taps"],"nouns":v["nouns"],"question":v["question"],
       "answer":v["answer"],"answerVoice":v["answerVoice"],"carousel":[],"recall":v["recall"],"notes":v["notes"]}
    json.dump(d,open(f"content/de/{i}.json","w"),ensure_ascii=False,indent=1)
