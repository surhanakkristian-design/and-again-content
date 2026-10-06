import json
def g(t,acc=None): return {"text":t,"gap":True,"accept":acc or [t]}
def p(t): return {"text":t}
M="male";F="female"
D={
38:dict(level="A",keyWord="der Flughafen",
 taps=[("mit zwei Stäben winken","der Mann",M),("auf den Mann zurollen","das Flugzeug am Boden",M),("in den Himmel fliegen","das Flugzeug am Himmel",M)],
 nouns=[("das Flugzeug",M),("der Mann",M),("der Turm",M),("der Himmel",M)],
 q="Was macht der Mann?",a="Er winkt am Flughafen mit zwei Stäben.",av=M,
 recall=[("taps",[p("mit zwei Stäben"),g("winken",["winken","schwenken"])]),
         ("taps",[p("auf den Mann"),g("zurollen",["zurollen","zufahren"])]),
         ("taps",[p("in den"),g("Himmel"),p("fliegen")]),
         ("answer",[p("winkt am"),g("Flughafen"),p("mit zwei Stäben")])],
 notes="German allows two orders of the adverbials in the answer chips ('am Flughafen mit zwei Stäben' / 'mit zwei Stäben am Flughafen'); kept the airport first because it carries the key word. 'orange' left out of the phrase (orange/orangefarben is awkward to inflect at level A). Key word der Flughafen is not one of the nouns; it appears only in the answer."),
785:dict(level="A",keyWord="der Fahrplan",
 taps=[("zum Fahrplan hochschauen","der Junge",M),("Züge und Uhren zeigen","der Fahrplan",M),("am Bahnhof ankommen","der Zug",M)],
 nouns=[("der Fahrplan",M),("der Junge",M),("die Bank",M)],
 q="Was macht der Junge?",a="Er liest den Fahrplan.",av=M,
 recall=[("taps",[p("zum Fahrplan"),g("hochschauen",["hochschauen","hochsehen","aufschauen"])]),
         ("taps",[p("Züge und"),g("Uhren"),p("zeigen")]),
         ("taps",[p("am Bahnhof"),g("ankommen",["ankommen","einfahren"])]),
         ("answer",[p("liest den"),g("Fahrplan")])],
 notes="English phrase 1 is 'to look at his watch', but the boy's box mostly shows him looking up at the timetable (watch only in about 3 frames; later frames: pointing, running, boarding), so phrase 1 says what he does in most boxed frames: 'zum Fahrplan hochschauen'. Answer uses 'liest' to differ from phrase 1."),
4058:dict(level="A",keyWord="die Reise",
 taps=[("zu den Koffern hochschauen","der Mann",M),("eine rote Kappe tragen","der Mann",M),("viele Koffer schieben","die Frau",F)],
 nouns=[("der Mann",M),("die Frau",F),("die Koffer",M),("der Himmel",M)],
 q="Was macht die Frau?",a="Sie schiebt viele Koffer.",av=F,
 recall=[("taps",[p("zu den Koffern"),g("hochschauen",["hochschauen","hochsehen","aufschauen"])]),
         ("taps",[p("eine rote"),g("Kappe",["Kappe","Mütze","Cap"]),p("tragen")]),
         ("taps",[p("viele"),g("Koffer"),p("schieben")]),
         ("answer",[g("schiebt"),p("viele Koffer")])],
 notes="English phrase 1 'to pack a brown suitcase' is true only in the first frames of the man's box (plus carrying it to the car); most boxed frames show him staring up at the tower of suitcases, so phrase 1 = 'zu den Koffern hochschauen'. Key word die Reise is not shown as a thing and is not used in any text (not forced); the answer would need an invented 'für die Reise'."),
7999:dict(level="A",keyWord="im Hotel übernachten",
 taps=[("aufs Bett springen","der Hund",M),("auf dem Rücken liegen","der Hund",M),("die Koffer bringen","die Katze",M)],
 nouns=[("der Hund",M),("die Katze",M),("das Bett",M),("das Fenster",M)],
 q="Was macht der Hund?",a="Er liegt auf dem Bett.",av=M,
 recall=[("taps",[p("aufs Bett"),g("springen",["springen","hüpfen"])]),
         ("taps",[p("auf dem"),g("Rücken"),p("liegen")]),
         ("taps",[p("die"),g("Koffer"),p("bringen")]),
         ("answer",[g("liegt"),p("auf dem Bett")])],
 notes="Phrase 1 'aufs Bett springen' happens only in the first boxed frame; the rest of the shared dog box shows it lying on its back, which is phrase 2, so phrase 1 keeps the jump (the only other action that differs). Key phrase 'im Hotel übernachten' is not used in the texts (not forced)."),
7180:dict(level="A",keyWord="in den Urlaub fahren",
 taps=[("in den Pool springen","der Mann mit der Sonnenbrille",M),("ein Getränk halten","der Kellner",M),("auf dem Boden liegen","der Koffer",M)],
 nouns=[("der Koffer",M),("die Palmen",M),("der Himmel",M),("der Kellner",M)],
 q="Was macht der Mann mit der Sonnenbrille?",a="Er springt in den Pool.",av=M,
 recall=[("taps",[p("in den"),g("Pool",["Pool","Swimmingpool"]),p("springen")]),
         ("taps",[p("ein"),g("Getränk"),p("halten")]),
         ("taps",[p("auf dem"),g("Boden"),p("liegen")]),
         ("answer",[g("springt"),p("in den Pool")])],
 notes="English noun 'trees' are palm trees: 'die Palmen' is the natural German word. English phrase 3 'to fall on the ground': the suitcase falls only in the first boxed frame and lies on the ground in the rest, so 'auf dem Boden liegen'. Phrase 1: the jump is in the first frames, then he is in the water; kept the jump (it is the question's action). Key phrase 'in den Urlaub fahren' not used in the texts (not forced)."),
}
import sys
ids=[int(x) for x in sys.argv[1:]] or list(D)
for i in ids:
    d=D[i]
    out={"mediaId":i,"lang":"de","level":d["level"],"keyWord":d["keyWord"],
     "taps":[{"phrase":a,"target":b,"voice":c} for a,b,c in d["taps"]],
     "nouns":[{"word":a,"voice":b} for a,b in d["nouns"]],
     "question":d["q"],"answer":d["a"].split(),"answerVoice":d["av"],"carousel":[],
     "recall":[{"from":f,"parts":ps} for f,ps in d["recall"]],"notes":d["notes"]}
    json.dump(out,open(f"content/de/{i}.json","w"),ensure_ascii=False,indent=1)
