import json
def P(*parts):
    out=[]
    for p in parts:
        if isinstance(p,tuple): out.append({"text":p[0],"gap":True,"accept":list(p)})
        else: out.append({"text":p})
    return out
def T(ph,tg,v): return {"phrase":ph,"target":tg,"voice":v}
def N(w,v): return {"word":w,"voice":v}
D={}
D[282]=dict(level="B",keyWord="der Lidschatten",
 taps=[T("goldenen Lidschatten aufnehmen","der Pinsel","female"),T("ein Kopftuch tragen","die Frau mit dem Kopftuch","female"),T("goldene Lider zur Schau stellen","die Frau in der Bluse","female")],
 nouns=[N("das Kopftuch","female"),N("der Lidschatten","female"),N("der Kragen","female"),N("der Knopf","female")],
 question="Was nimmt der Pinsel auf?",answer=["Er","nimmt","goldenen","Lidschatten","auf."],answerVoice="female",
 recall=[{"from":"taps","parts":P("goldenen",("Lidschatten",),"aufnehmen")},
         {"from":"taps","parts":P("ein",("Kopftuch","Tuch"),"tragen")},
         {"from":"taps","parts":P("goldene",("Lider","Augenlider"),"zur Schau stellen")},
         {"from":"answer","parts":P(("nimmt",),"goldenen Lidschatten auf")}],
 notes="Answer subject 'Er' = der Pinsel; answerVoice kept female as in English (no natural gender). 'zur Schau stellen' is the B1/B2 collocation for 'show off'.")
D[283]=dict(level="B",keyWord="der Stoff",
 taps=[T("den gemusterten Stoff ausrollen","der Mann","male"),T("den Stoff mit einer Schere zuschneiden","der Mann","male"),T("den gefalteten Stoff an sich drücken","die Frau","female")],
 nouns=[N("der Ohrring","female"),N("der Stoff","female"),N("der Tisch","female"),N("das Maßband","female")],
 question="Was macht der Mann?",answer=["Er","schneidet","den","Stoff","mit","einer","Schere","zu."],answerVoice="male",
 recall=[{"from":"taps","parts":P("den gemusterten Stoff",("ausrollen","abrollen"))},
         {"from":"taps","parts":P("den Stoff mit einer Schere",("zuschneiden","schneiden"))},
         {"from":"taps","parts":P("den gefalteten",("Stoff",),"an sich drücken")},
         {"from":"answer","parts":P("schneidet den Stoff mit einer",("Schere",),"zu")}],
 notes="English 'cloth' and 'fabric' both = der Stoff (one thing, one word). Phrase 2 adds 'den Stoff' as object (zuschneiden needs one). German also allows 'Er schneidet mit einer Schere den Stoff zu.' (second chip order).")
D[284]=dict(level="B",keyWord="die Gesichtsmaske",
 taps=[T("ein flauschiges Haarband tragen","die Frau in Lila","female"),T("mit dem Finger auf ihre Freundin zeigen","die Frau in Grau","female"),T("auf einem Kissen ruhen","der Hund","female")],
 nouns=[N("das Haarband","female"),N("die Gesichtsmaske","female"),N("der Hund","female"),N("die Schüssel","female")],
 question="Was tragen die Frauen?",answer=["Sie","tragen","grüne","Gesichtsmasken."],answerVoice="female",
 recall=[{"from":"taps","parts":P("ein flauschiges",("Haarband",),"tragen")},
         {"from":"taps","parts":P("mit dem Finger auf ihre Freundin",("zeigen","deuten"))},
         {"from":"taps","parts":P("auf einem",("Kissen",),"ruhen")},
         {"from":"answer","parts":P("tragen grüne",("Gesichtsmasken","Masken"))}],
 notes="Key word noun row skipped: the answer row contains Gesichtsmasken (plural).")
D[285]=dict(level="A",keyWord="die Familie",
 taps=[T("ein Familienfoto machen","der Mann mit der Kamera","male"),T("mit beiden Händen winken","der Mann mit der Kamera","male"),T("die Treppe hochlaufen","der Hund","male")],
 nouns=[N("das Fenster","male"),N("die Familie","male"),N("die Treppe","male"),N("das Gras","male")],
 question="Was macht die Familie?",answer=["Sie","macht","ein","Familienfoto."],answerVoice="male",
 recall=[{"from":"taps","parts":P("ein",("Familienfoto",),"machen")},
         {"from":"taps","parts":P("mit beiden Händen",("winken",))},
         {"from":"taps","parts":P("die Treppe",("hochlaufen","hochrennen","hinauflaufen"))},
         {"from":"answer","parts":P(("macht",),"ein Familienfoto")}],
 notes="English 'steps' = die Treppe (everyday word for porch steps, same word in phrase 3 and noun 3). 'Sie macht' agrees with die Familie (singular). Red box also covers the grandpa setting up the camera; he is taking the family photo in most boxed frames. No noun row: Familienfoto contains the key word (compound rule).")
D[287]=dict(level="A",keyWord="weit",
 taps=[T("auf ein Dorf zeigen","die Frau","female"),T("zu ihr zurückschauen","der Mann in Grün","male"),T("eine rote Jacke tragen","die Person in Rot","female")],
 nouns=[N("der Himmel","female"),N("das Dorf","female"),N("das Gras","female")],
 question="Worauf zeigt die Frau?",answer=["Sie","zeigt","auf","ein","weit","entferntes","Dorf."],answerVoice="female",
 recall=[{"from":"taps","parts":P("auf ein",("Dorf",),"zeigen")},
         {"from":"taps","parts":P("zu ihr",("zurückschauen","zurückblicken"))},
         {"from":"taps","parts":P("eine rote",("Jacke",),"tragen")},
         {"from":"answer","parts":P("zeigt auf ein",("weit",),"entferntes Dorf")}],
 notes="'weit entfernt' is the natural German for 'far away' (entfernt slightly above A2, but it is the plain right word with the key word weit).")
for i,d in D.items():
    o={"mediaId":i,"lang":"de","level":d["level"],"keyWord":d["keyWord"],"taps":d["taps"],"nouns":d["nouns"],"question":d["question"],
       "answer":d["answer"],"answerVoice":d["answerVoice"],"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(o,open(f"content/de/{i}.json","w"),ensure_ascii=False,indent=1)
