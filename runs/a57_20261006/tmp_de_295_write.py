import json
def T(p,t,v): return {"phrase":p,"target":t,"voice":v}
def N(w,v): return {"word":w,"voice":v}
def R(src,*parts):
    out=[]
    for p in parts:
        if isinstance(p,tuple): out.append({"text":p[0],"gap":True,"accept":list(p[1])})
        else: out.append({"text":p})
    return {"from":src,"parts":out}
D={}
D[295]=dict(level="A",keyWord="mischen",
 taps=[T("die dicke Paste mischen","die Hand","male"),T("einen schwarzen Griff halten","die Hand","male"),T("am Boden kleben","das blaue Klebeband","male")],
 nouns=[N("das Klebeband","male"),N("der Eimer","male"),N("die Hand","male"),N("der Schuh","male")],
 question="Was macht die Hand?",answer="Die Hand mischt die dicke Paste.".split(),answerVoice="male",
 recall=[R("taps","die dicke Paste",("mischen",["mischen","verrühren","rühren"])),
         R("taps","einen schwarzen",("Griff",["Griff"]),"halten"),
         R("taps","am Boden",("kleben",["kleben"])),
         R("answer","mischt die dicke",("Paste",["Paste","Masse"]))],
 notes="Phrase 1 and 2 share the same target (the hand), as in English. 'die Paste' used for the joint compound throughout (A-level everyday word; 'die Spachtelmasse' would be the trade term).")
D[296]=dict(level="A",keyWord="der Fisch",
 taps=[T("einen Fisch grillen","der Mann","male"),T("mit einer Gabel essen","die Frau","female"),T("auf einem Holzbrett liegen","der Fisch","female")],
 nouns=[N("das Meer","female"),N("das Boot","female"),N("der Fisch","female"),N("das Feuer","female")],
 question="Was isst die Frau?",answer="Sie isst Fisch mit einer Gabel.".split(),answerVoice="female",
 recall=[R("taps","einen",("Fisch",["Fisch"]),"grillen"),
         R("taps","mit einer Gabel",("essen",["essen"])),
         R("taps","auf einem",("Holzbrett",["Holzbrett","Brett"]),"liegen"),
         R("answer","isst Fisch mit einer",("Gabel",["Gabel"]))],
 notes="Phrase 1: English 'hold half a lemon' is true only in 2-3 boxed frames; in most boxed frames the man holds the grill basket over the fire, brushes and squeezes lemon on the fish, so 'einen Fisch grillen' (fits only him). Phrase 3: the fish lies over the fire in ~9 boxed frames and on a wooden board in ~12, so 'auf einem Holzbrett liegen' (most boxed frames); 'über dem Feuer liegen' would be the alternative. Key word noun is in rows 1 and answer, so no noun row.")
D[297]=dict(level="A",keyWord="das Angeln",
 taps=[T("eine Angel halten","der Mann","male"),T("ein Netz halten","die Frau","female"),T("im See schwimmen","der Fisch","male")],
 nouns=[N("der Fisch","male"),N("das Netz","male"),N("die Kappe","male"),N("die Bäume","male")],
 question="Was machen der Mann und die Frau?",answer="Sie angeln im See.".split(),answerVoice="male",
 recall=[R("taps","eine",("Angel",["Angel"]),"halten"),
         R("taps","ein",("Netz",["Netz","Kescher"]),"halten"),
         R("taps","im See",("schwimmen",["schwimmen"])),
         R("answer",("angeln",["angeln"]),"im See")],
 notes="'das Netz' for the landing net (A-level; the exact word 'der Kescher' is above level, accepted in recall). Key word is the noun 'das Angeln'; the answer uses the verb 'angeln' (same lemma family). Phrase 1: in the last boxed frames the man holds the fish / high-fives instead of the rod; the rod is in most boxed frames. Phrase 2: the woman points/cheers in some boxed frames, holds the net in most.")
D[298]=dict(level="B",keyWord="die Umkleidekabine",
 taps=[T("mehrere Outfits anprobieren","die blonde Frau","female"),T("die Outfits bewerten","die dunkelhaarige Frau","female"),T("auf dem Tresen dösen","der Hund","female")],
 nouns=[N("der Vorhang","female"),N("der Kleiderhaufen","female"),N("die Sandalen","female"),N("der Hund","female")],
 question="Was macht die blonde Frau?",answer="Sie probiert in einer Umkleidekabine Outfits an.".split(),answerVoice="female",
 recall=[R("taps","mehrere Outfits",("anprobieren",["anprobieren"])),
         R("taps","die Outfits",("bewerten",["bewerten","beurteilen"])),
         R("taps","auf dem",("Tresen",["Tresen","Theke"]),"dösen"),
         R("answer","probiert in einer",("Umkleidekabine",["Umkleidekabine","Umkleide"]),"Outfits an")],
 notes="Phrase 2: English 'give a thumbs up' happens only in the last boxed frames; in most boxed frames the friend yawns, gives thumbs down, then thumbs up, so 'die Outfits bewerten' (B1). Phrase 3: the dog lies still with its head down ('dösen', B2); it sits up in the last frames. Answer: German also allows 'Sie probiert Outfits in einer Umkleidekabine an.' (second chip order). Key word not a noun of the set, so no noun row.")
D[299]=dict(level="A",keyWord="wecken",
 taps=[T("im Bett schlafen","die Frau","female"),T("auf dem Bett herumlaufen","der Hund","female"),T("sich die Hände vors Gesicht halten","die Frau","female")],
 nouns=[N("das Kissen","female"),N("der Hund","female"),N("die Decke","female"),N("die Tür","female")],
 question="Was macht der Hund?",answer="Der Hund weckt die Frau.".split(),answerVoice="female",
 recall=[R("taps","im Bett",("schlafen",["schlafen"])),
         R("taps","auf dem Bett",("herumlaufen",["herumlaufen","laufen"])),
         R("taps","sich die Hände vors",("Gesicht",["Gesicht"]),"halten"),
         R("answer",("weckt",["weckt"]),"die Frau")],
 notes="Phrases 1 and 3 have the same box (the woman) for the whole clip, as in English: she sleeps in most frames and covers her face only at the end. Answer uses 'die Frau' instead of 'sie' so 'wecken' (not 'aufwecken') stays the key word without a trailing 'auf'. 'die Tür' = the closet door.")
for i,d in D.items():
    o={"mediaId":i,"lang":"de","level":d["level"],"keyWord":d["keyWord"],"taps":d["taps"],"nouns":d["nouns"],
       "question":d["question"],"answer":d["answer"],"answerVoice":d["answerVoice"],"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(o,open(f"content/de/{i}.json","w"),ensure_ascii=False,indent=1)
