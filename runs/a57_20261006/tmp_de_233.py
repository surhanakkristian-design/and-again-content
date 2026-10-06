import json
def g(t,acc=None): return {"text":t,"gap":True,"accept":acc or [t]}
def p(t): return {"text":t}
def tap(ph,t,v): return {"phrase":ph,"target":t,"voice":v}
def n(w,v): return {"word":w,"voice":v}
D={}
D[233]=dict(level="B",keyWord="ausrenken",
 taps=[tap("sich die ausgerenkte Schulter halten","der Mann","male"),tap("neben dem Kletterer knien","die Frau","female"),tap("aufgerollt im Gras liegen","das Seil","male")],
 nouns=[n("der Helm","male"),n("die Schulter","male"),n("die Jacke","male"),n("das Gras","male")],
 question="Was macht der Mann?",answer="Er hält sich die ausgerenkte Schulter.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":[p("sich die"),g("ausgerenkte",["ausgerenkte","verletzte"]),p("Schulter halten")]},
  {"from":"taps","parts":[p("neben dem"),g("Kletterer"),p("knien")]},
  {"from":"taps","parts":[g("aufgerollt"),p("im Gras liegen")]},
  {"from":"answer","parts":[g("hält",["hält","umklammert"]),p("sich die ausgerenkte Schulter")]}],
 notes="Key word ausrenken used as the participle 'ausgerenkte Schulter' (phrase 1 + answer); the clip shows a hurt shoulder, the dislocation itself is not visible, 'verletzte' accepted in recall. Red box 1 also covers the fall and crawling frames (box_01-02) before he clutches the shoulder; phrase written for the clutching frames. Rope phrase: the rope lies coiled in the grass.")
D[235]=dict(level="B",keyWord="apportieren",
 taps=[tap("einen roten Ball apportieren","der Hund","female"),tap("dem Hund den Bauch kraulen","die Frau","female"),tap("voller reifer Äpfel hängen","der Baum","female")],
 nouns=[n("der Apfelbaum","female"),n("der Zaun","female"),n("der Hund","female"),n("der Rasen","female")],
 question="Was macht der Hund?",answer="Der Hund apportiert einen roten Ball.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":[p("einen roten"),g("Ball"),p("apportieren")]},
  {"from":"taps","parts":[p("dem Hund den Bauch"),g("kraulen",["kraulen","streicheln"])]},
  {"from":"taps","parts":[p("voller reifer"),g("Äpfel"),p("hängen")]},
  {"from":"answer","parts":[g("apportiert"),p("einen roten Ball")]}],
 notes="Box 1 also covers the opening frames where the dog waits and the closing belly-rub frames; phrase written for the fetch. 'voller reifer Äpfel hängen' = idiomatic 'der Baum hängt voller Äpfel'.")
D[237]=dict(level="A",keyWord="der Esel",
 taps=[tap("das Maul weit aufmachen","der Esel","male"),tap("sich auf dem Boden rollen","der Esel","male"),tap("nach Futter suchen","die Vögel","male")],
 nouns=[n("die Orangen","male"),n("das Haus","male"),n("der Esel","male"),n("die Vögel","male")],
 question="Was macht der Esel?",answer="Der Esel rollt sich auf dem Boden.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":[p("das"),g("Maul",["Maul","Mund"]),p("weit aufmachen")]},
  {"from":"taps","parts":[p("sich auf dem Boden"),g("rollen",["rollen","wälzen"])]},
  {"from":"taps","parts":[p("nach"),g("Futter",["Futter","Essen"]),p("suchen")]},
  {"from":"nouns","parts":[p("der"),g("Esel")]},
  {"from":"answer","parts":[p("rollt sich auf dem"),g("Boden")]}],
 notes="Boxes 1 and 2 are identical and cover the whole clip (braying at the start, rolling in the middle); phrases written for the respective moments. 'sich rollen' chosen for level A; the more idiomatic 'sich wälzen' (B1) is accepted in recall. 'das Maul' is the correct word for an animal's mouth.")
D[238]=dict(level="A",keyWord="stehlen",
 taps=[tap("eine Dose stehlen","der Mann","male"),tap("eine weiße Tüte bringen","der Mann","male"),tap("rosa blühen","der Busch","male")],
 nouns=[n("der Himmel","male"),n("die Blumen","male"),n("das Gras","male"),n("die Dosen","male")],
 question="Was macht der Mann?",answer="Er stiehlt eine Dose.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":[p("eine"),g("Dose"),p("stehlen")]},
  {"from":"taps","parts":[p("eine weiße"),g("Tüte",["Tüte","Tasche"]),p("bringen")]},
  {"from":"taps","parts":[p("rosa"),g("blühen")]},
  {"from":"answer","parts":[g("stiehlt",["stiehlt","klaut"]),p("eine Dose")]}],
 notes="Phrase 2: box 2 also covers the frames after he has put the bag down, so 'eine weiße Tüte bringen' (delivers it) instead of 'tragen' (only the approach frames). Box 1 also covers his approach; phrase written for the theft. Noun 2 'die Blumen' kept at level A (botanically 'die Blüten', B1).")
D[239]=dict(level="B",keyWord="bezweifeln",
 taps=[tap("einen goldenen Ring begutachten","der Mann","male"),tap("über das ganze Gesicht strahlen","die alte Frau","female"),tap("skeptisch die Stirn runzeln","der Mann","male")],
 nouns=[n("der Ring","male"),n("das Kopftuch","male"),n("die Jacke","male"),n("die Wolken","male")],
 question="Was begutachtet der Mann?",answer="Er begutachtet einen goldenen Ring.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":[p("einen goldenen Ring"),g("begutachten",["begutachten","prüfen","untersuchen"])]},
  {"from":"taps","parts":[p("über das ganze Gesicht"),g("strahlen")]},
  {"from":"taps","parts":[p("skeptisch die"),g("Stirn"),p("runzeln")]},
  {"from":"answer","parts":[p("begutachtet einen goldenen"),g("Ring")]}],
 notes="Key word 'bezweifeln' does not appear in the exercises (the clip shows doubt through the frown; 'skeptisch' carries it). Boxes 1 and 3 also cover the last frames where he has put the ring down and talks; phrases written for the examining frames. Phrase 2: the old woman beams at him (English 'grin at the customer').")
for i,d in D.items():
    out={"mediaId":i,"lang":"de",**{k:d[k] for k in ["level","keyWord","taps","nouns","question","answer","answerVoice"]},"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(out,open(f"content/de/{i}.json","w"),ensure_ascii=False,indent=1)
