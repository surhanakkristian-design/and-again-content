import json
def T(p,t,v): return {"phrase":p,"target":t,"voice":v}
def N(w,v): return {"word":w,"voice":v}
def R(frm,*parts):
    out=[]
    for p in parts:
        if isinstance(p,tuple): out.append({"text":p[0],"gap":True,"accept":list(p[1])})
        else: out.append({"text":p})
    return {"from":frm,"parts":out}
D={}
m="male"
D[102]=dict(level="B",keyWord="die Langeweile",
 taps=[T("sich im Plastikstuhl lümmeln","der Mann",m),T("durch die Luft wirbeln","die Socke",m),T("sich auf seiner Fingerspitze drehen","der Wäschesack",m)],
 nouns=[N("die Socke",m),N("die Waschmaschinen",m),N("der Trainingsanzug",m),N("der Turnschuh",m)],
 question="Was macht der Mann?",answer="Er lümmelt sich im Plastikstuhl.".split(),answerVoice=m,
 recall=[R("taps","sich im","Plastikstuhl",("lümmeln",["lümmeln","fläzen"])),
         R("taps","durch die Luft",("wirbeln",["wirbeln","fliegen"])),
         R("taps","sich auf seiner",("Fingerspitze",["Fingerspitze"]),"drehen"),
         R("answer","lümmelt sich im",("Plastikstuhl",["Plastikstuhl","Stuhl"]))],
 notes="Key word 'die Langeweile' (boredom) is not a thing in the noun set and appears in no exercise, as in English; no noun row. Sock box (phrase 2): English 'dangle from his fingers' is true only in box_05 (3 frames); in most boxed frames the sock tumbles through the air (box_01), so 'durch die Luft wirbeln'; it also lies in the drum (box_04) and on his head (box_05/06). The feather also floats, but only in frames where the sock box is OFF. Man box (phrase 1) also covers floor/feet/finger/running frames; the slumped sitting is the majority.")
f="female"
D[7088]=dict(level="B",keyWord="ebnen",
 taps=[T("eine lange Latte durch den Beton ziehen","die Frau",f),T("eine schwere Last in der Luft halten","der Kran",f),T("auf dem Dach knien","der kniende Arbeiter",f)],
 nouns=[N("der Kran",f),N("der Schutzhelm",f),N("das Stativ",f),N("der Beton",f)],
 question="Was macht die Frau?",answer="Sie zieht den nassen Beton glatt.".split(),answerVoice=f,
 recall=[R("taps","eine lange",("Latte",["Latte","Abziehlatte"]),"durch den Beton","ziehen"),
         R("taps","eine schwere",("Last",["Last"]),"in der Luft halten"),
         R("taps","auf dem Dach",("knien",["knien"])),
         R("answer","zieht den nassen",("Beton",["Beton"]),"glatt")],
 notes="Key word 'ebnen' kept, but for wet concrete natives say 'glattziehen' or 'abziehen' ('ebnen' is mostly 'den Boden ebnen' or figurative 'den Weg ebnen'); proposal: key word 'glattziehen' (or 'abziehen'). So the answer uses 'zieht ... glatt', not 'ebnet'. The kneeling worker's gender is unclear: target written as 'der kniende Arbeiter' (verifier only). 'die Latte' for the straightedge (technical: Abziehlatte, accepted in recall).")
D[4852]=dict(level="B",keyWord="das Zahnrad",
 taps=[T("mit offenem Mund staunen","der Mann",m),T("mit kleinen Bauteilen bestückt sein","die Platine",m),T("große Zahnräder aus Metall haben","die riesige Maschine",m)],
 nouns=[N("die Schutzbrille",m),N("die Werkzeuge",m),N("die Platine",m),N("der Schraubstock",m)],
 question="Was baut der Mann?",answer="Er baut eine Maschine mit Zahnrädern aus Metall.".split(),answerVoice=m,
 recall=[R("taps","mit offenem Mund",("staunen",["staunen"])),
         R("taps","mit kleinen",("Bauteilen",["Bauteilen"]),"bestückt sein"),
         R("taps","große",("Zahnräder",["Zahnräder"]),"aus Metall haben"),
         R("answer","baut eine",("Maschine",["Maschine"]),"mit Zahnrädern aus Metall")],
 notes="Man box (phrase 1): English 'raise both arms' is true only in the last 3 frames (box_05); in most boxed frames he stares wide-eyed with his mouth open, so 'mit offenem Mund staunen' (the first 2 frames show only his hands with the spanner). Board box (phrase 2): it glows red and green only in 2 frames (box_02); in all boxed frames it is visibly fitted with small components, so 'mit kleinen Bauteilen bestückt sein'. No noun row: 'Zahnräder' is in tap row 3 and the answer.")
D[4441]=dict(level="B",keyWord="der Atem",
 taps=[T("die Augen geschlossen halten","die Frau",f),T("die Landschaft überragen","der Berggipfel",f),T("eine weiße Strickmütze tragen","die Person mit der weißen Mütze",f)],
 nouns=[N("der Himmel",f),N("der Gipfel",f),N("der Atem",f),N("die Jacke",f)],
 question="Was sieht man in der Luft?",answer="Man sieht den Atem der Frau.".split(),answerVoice=f,
 recall=[R("taps","die Augen",("geschlossen",["geschlossen","zu"]),"halten"),
         R("taps","die",("Landschaft",["Landschaft"]),"überragen"),
         R("taps","eine weiße",("Strickmütze",["Strickmütze","Mütze"]),"tragen"),
         R("answer","sieht den",("Atem",["Atem"]),"der Frau")],
 notes="Key word 'der Atem' is noun 3 and the answer's gap; no separate noun row since the answer row contains it. Woman box: in the last frames her face is hidden in the breath cloud. 'die Augen geschlossen halten' only for the woman (the walkers' eyes are not visible).")
D[4721]=dict(level="B",keyWord="verblassen",
 taps=[T("über die Schulter deuten","die Frau",f),T("am Himmel verblassen","der Regenbogen",f),T("in die Ferne blicken","die Frau",f)],
 nouns=[N("der Regenbogen",f),N("der See",f),N("die Regenjacke",f),N("die Pfütze",f)],
 question="Was passiert mit dem Regenbogen?",answer="Der Regenbogen verblasst am Himmel.".split(),answerVoice=f,
 recall=[R("taps","über die",("Schulter",["Schulter"]),"deuten"),
         R("taps","am Himmel",("verblassen",["verblassen"])),
         R("taps","in die",("Ferne",["Ferne"]),"blicken"),
         R("answer",("verblasst",["verblasst"]),"am Himmel")],
 notes="Phrases 1 and 3 have the same target and the same box (the woman, whole clip). English 'point over her shoulder' (phrase 1) is true only in the first ~10 frames; kept as 'über die Schulter deuten' so the two phrases differ. English 'grin at the camera' (phrase 3) is true only in the first ~8 frames; for most boxed frames she looks away into the distance, so phrase 3 = 'in die Ferne blicken'. Rainbow box is OFF once the rainbow is gone. 'die Regenjacke' (hooded rain jacket) is the everyday word, not 'Regenmantel'.")
for i,d in D.items():
    o={"mediaId":i,"lang":"de","level":d["level"],"keyWord":d["keyWord"],"taps":d["taps"],"nouns":d["nouns"],"question":d["question"],
       "answer":d["answer"],"answerVoice":d["answerVoice"],"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(o,open(f"content/de/{i}.json","w"),ensure_ascii=False,indent=2)
