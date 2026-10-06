import json
def T(p,t,v): return {"phrase":p,"target":t,"voice":v}
def N(w,v): return {"word":w,"voice":v}
def R(src,*parts):
    ps=[]
    for p in parts:
        if isinstance(p,tuple): ps.append({"text":p[0],"gap":True,"accept":list(p[1])})
        else: ps.append({"text":p})
    return {"from":src,"parts":ps}
D=[
dict(mediaId=8044,lang="de",level="B",keyWord="wild",
 taps=[T("einen Luftsprung machen","der Mann in Grau","male"),T("fassungslos zuschauen","die Frau in Flieder","female"),T("sich vor Lachen krümmen","der Mann in Grün","male")],
 nouns=[N("die Lichterketten","male"),N("die Braut","female"),N("der Heuballen","male"),N("die Krawatte","male")],
 question="Was macht der Mann in Grau?",answer="Er springt wild in die Luft.".split(),answerVoice="male",carousel=[],
 recall=[R("taps","einen",("Luftsprung",["Luftsprung"]),"machen"),R("taps",("fassungslos",["fassungslos","ungläubig"]),"zuschauen"),
  R("taps","sich vor Lachen",("krümmen",["krümmen"])),R("answer","springt",("wild",["wild"]),"in die Luft")],
 notes="Phrase 2: the woman in lilac stands still at first, then holds her hands to her mouth - 'fassungslos zuschauen' covers both. In the last box the man lands on his knees; phrase 1 describes most boxed frames. keyWord 'wild' is the adverb sense (extreme degree): 'wild springen' fits."),
dict(mediaId=7782,lang="de",level="B",keyWord="näher",
 taps=[T("seinen Rüssel ausstrecken","der Elefant","female"),T("sich köstlich amüsieren","die Frau","female"),T("eine Banane hinhalten","die Hand mit der Banane","female")],
 nouns=[N("der Kronleuchter","female"),N("der Rüssel","female"),N("die Croissants","female"),N("die Tischdecke","female")],
 question="Was macht der Elefant?",answer="Er streckt seinen Rüssel immer näher an die Banane heran.".split(),answerVoice="female",carousel=[],
 recall=[R("taps","seinen Rüssel",("ausstrecken",["ausstrecken","strecken"])),R("taps","sich köstlich",("amüsieren",["amüsieren"])),
  R("taps","eine",("Banane",["Banane"]),"hinhalten"),R("answer","streckt seinen Rüssel immer",("näher",["näher"]),"an die Banane heran")],
 notes="answerVoice kept female as in English (subject 'er' = der Elefant, grammatical gender only, English 'it')."),
dict(mediaId=1,lang="de",level="A",keyWord="die Pause",
 taps=[T("über sein Handy lachen","der Mann","male"),T("sich an den Kopf fassen","der Mann","male"),T("den Mund weit aufmachen","der Mann","male")],
 nouns=[N("der Vorhang","male"),N("das Handy","male"),N("der Pullover","male"),N("die Bücher","male")],
 question="Was macht der Mann?",answer="Er lacht über sein Handy.".split(),answerVoice="male",carousel=[],
 recall=[R("taps","über sein Handy",("lachen",["lachen"])),R("taps","sich an den",("Kopf",["Kopf"]),"fassen"),
  R("taps","den",("Mund",["Mund"]),"weit aufmachen"),R("answer","lacht über sein",("Handy",["Handy","Smartphone"]))],
 notes="All three English tap boxes cover the whole clip; each phrase is true only in part of it (laughing first, then hand on head, then mouth wide open). 'die Pause' is not a noun of the set, so no noun row."),
dict(mediaId=2,lang="de",level="B",keyWord="das Zertifikat",
 taps=[T("ein gerahmtes Zertifikat präsentieren","die Frau","female"),T("mehrere Zertifikate an sich drücken","die Frau","female"),T("vor Stolz strahlen","die Frau","female")],
 nouns=[N("die Locken","female"),N("das Zertifikat","female"),N("das Oberteil","female")],
 question="Was macht die Frau?",answer="Sie präsentiert ihre gerahmten Zertifikate.".split(),answerVoice="female",carousel=[],
 recall=[R("taps","ein gerahmtes",("Zertifikat",["Zertifikat"]),"präsentieren"),R("taps","mehrere Zertifikate an sich",("drücken",["drücken","pressen"])),
  R("taps","vor",("Stolz",["Stolz"]),"strahlen"),R("answer",("präsentiert",["präsentiert","zeigt"]),"ihre gerahmten Zertifikate")],
 notes="'curly hair' -> 'die Locken' (natural German noun for curly hair). For framed documents Germans also say 'die Urkunde'; 'das Zertifikat' fits the definition (proof of a finished course) and is kept. The noun row is skipped because the key word already appears in tap row 1."),
dict(mediaId=4,lang="de",level="A",keyWord="der Kurs",
 taps=[T("Eiskaffee trinken","die Frau","female"),T("am Laptop arbeiten","die Frau","female"),T("im Topf wachsen","die Pflanze","female")],
 nouns=[N("der Laptop","female"),N("das Glas","female"),N("die Pflanze","female"),N("der Tisch","female")],
 question="Was macht die Frau?",answer="Sie trinkt einen Eiskaffee.".split(),answerVoice="female",carousel=[],
 recall=[R("taps","Eiskaffee",("trinken",["trinken"])),R("taps","am",("Laptop",["Laptop","Computer"]),"arbeiten"),
  R("taps","im",("Topf",["Topf","Blumentopf"]),"wachsen"),R("answer","trinkt einen",("Eiskaffee",["Eiskaffee","Kaffee"]))],
 notes="Answer is 'Sie trinkt einen Eiskaffee.' instead of the English 'at the table' version, to keep one word order ('am Tisch' could stand in two places). 'der Kurs' is not a noun of the set (the online course is not visible), so no noun row."),
]
for d in D:
    json.dump(d,open(f"content/de/{d['mediaId']}.json","w"),ensure_ascii=False,indent=1)
