import json
def P(*parts):
    out=[]
    for p in parts:
        if isinstance(p,tuple): out.append({"text":p[0],"gap":True,"accept":list(p[1])})
        else: out.append({"text":p})
    return out
F="female"; M="male"
V={
5435: dict(level="B", keyWord="ähnlich",
 taps=[("eine blaue Chipstüte hervorholen","die Frau links",F),("eine rote Chipstüte hervorholen","die Frau rechts",F),("eine blaue Chipstüte einstecken","die Frau rechts",F)],
 nouns=[("der Himmel",F),("die Bäume",F),("der Rasen",F),("der Gehweg",F)],
 q="Wie sehen die beiden Frauen aus?", a="Die beiden Frauen sehen sich zum Verwechseln ähnlich.", av=F,
 recall=[("taps",P("eine blaue Chipstüte",("hervorholen",["hervorholen","herausholen","herausziehen"]))),
         ("taps",P("eine rote",("Chipstüte",["Chipstüte","Tüte"]),"hervorholen")),
         ("taps",P("eine blaue",("Chipstüte",["Chipstüte","Tüte"]),"einstecken")),
         ("answer",P("sehen sich zum Verwechseln",("ähnlich",["ähnlich"])))],
 notes="Phrases 1 and 2 differ only by the colour, as in English (left woman takes out a blue crisp packet, right one a red one); phrase 3 = right woman puts a blue packet into her belt bag. Alternative order 'Zum Verwechseln ähnlich sehen sich die beiden Frauen.' is possible but marked; the plain order is the expected one."),
6824: dict(level="B", keyWord="die Klimaanlage",
 taps=[("sich den Schweiß von der Stirn wischen","der Mann",M),("den Druck anzeigen","die Manometer",M),("tropfendes Wasser auffangen","der Eimer",M)],
 nouns=[("die Klimaanlage",M),("der Eimer",M),("die Kappe",M),("der Himmel",M)],
 q="Was macht der Mann?", a="Er wartet die Klimaanlage.", av=M,
 recall=[("taps",P("sich den",("Schweiß",["Schweiß"]),"von der Stirn wischen")),
         ("taps",P("den Druck",("anzeigen",["anzeigen","messen"]))),
         ("taps",P("tropfendes Wasser",("auffangen",["auffangen","sammeln"]))),
         ("answer",P("wartet die",("Klimaanlage",["Klimaanlage"])))],
 notes="Noun 1: the pill sits on an outdoor unit; 'die Klimaanlage' is how Germans name such a unit in everyday speech (technically 'das Außengerät der Klimaanlage'). 'warten' (= service) is B2; 'repariert' would be the A2 alternative."),
4858: dict(level="B", keyWord="die Spirale",
 taps=[("den ersten Dominostein umstoßen","der Mann",M),("die Fäuste ballen","der Mann",M),("eine riesige Spirale bilden","die Dominosteine",M)],
 nouns=[("die Spirale",M),("der Mann",M),("der Boden",M)],
 q="Was hat der Mann gebaut?", a="Er hat eine riesige Spirale aus Dominosteinen gebaut.", av=M,
 recall=[("taps",P("den ersten Dominostein",("umstoßen",["umstoßen","anstoßen"]))),
         ("taps",P("die Fäuste",("ballen",["ballen"]))),
         ("taps",P("eine riesige",("Spirale",["Spirale"]),"bilden")),
         ("answer",P("hat eine riesige Spirale aus Dominosteinen",("gebaut",["gebaut","aufgebaut"])))],
 notes="German also allows 'Er hat aus Dominosteinen eine riesige Spirale gebaut.' with the same chips (two orders). In the box frames the man mostly points at / nudges the dominoes; phrase 1 kept as in English."),
5566: dict(level="B", keyWord="die Ankunft",
 taps=[("die Ziellinie überqueren","die Läuferin",F),("das Zielband aufheben","die Frau im Kapuzenpulli",F),("hinter den Absperrungen jubeln","die Zuschauer",F)],
 nouns=[("die Läuferin",F),("die Zuschauer",F),("die Wimpelketten",F),("die Pappbecher",F)],
 q="Was macht die Läuferin?", a="Sie überquert die Ziellinie.", av=F,
 recall=[("taps",P("die",("Ziellinie",["Ziellinie"]),"überqueren")),
         ("taps",P("das Zielband",("aufheben",["aufheben","aufsammeln"]))),
         ("taps",P("hinter den",("Absperrungen",["Absperrungen"]),"jubeln")),
         ("answer",P(("überquert",["überquert"]),"die Ziellinie"))],
 notes="Key word 'die Ankunft' appears in no exercise (as 'arrival' in the English); 'die Ankunft' is weak for crossing a finish line ('der Zieleinlauf' would fit better) - owner decides. Several strings of bunting -> plural 'die Wimpelketten'."),
4538: dict(level="B", keyWord="die Ruhe",
 taps=[("den Glastisch schrubben","die Frau",F),("einen Müllsack zubinden","die Frau",F),("sich auf dem Sofa zurücklehnen","die Frau",F)],
 nouns=[("das Sofa",F),("die Heizung",F),("die Glühbirne",F),("das Bücherregal",F)],
 q="Wo ruht sich die Frau aus?", a="Sie gönnt sich auf dem Sofa etwas Ruhe.", av=F,
 recall=[("taps",P("den Glastisch",("schrubben",["schrubben","putzen"]))),
         ("taps",P("einen",("Müllsack",["Müllsack","Müllbeutel"]),"zubinden")),
         ("taps",P("sich auf dem",("Sofa",["Sofa","Couch"]),"zurücklehnen")),
         ("answer",P("gönnt sich auf dem Sofa etwas",("Ruhe",["Ruhe"])))],
 notes="All three English tap boxes are the same box on the only person; each phrase is true only in part of the clip (scrubbing at the start, tying the bag in the close-ups, reclining at the end). Answer allows a second order 'Sie gönnt sich etwas Ruhe auf dem Sofa.'; the given order is the more natural one. 'die Heizung' = everyday word for the radiator (Heizkörper is the technical one)."),
}
for mid,d in V.items():
    o={"mediaId":mid,"lang":"de","level":d["level"],"keyWord":d["keyWord"],
       "taps":[{"phrase":p,"target":t,"voice":v} for p,t,v in d["taps"]],
       "nouns":[{"word":w,"voice":v} for w,v in d["nouns"]],
       "question":d["q"],"answer":d["a"].split(" "),"answerVoice":d["av"],"carousel":[],
       "recall":[{"from":f,"parts":p} for f,p in d["recall"]],"notes":d["notes"]}
    json.dump(o,open(f"content/de/{mid}.json","w"),ensure_ascii=False,indent=1)
