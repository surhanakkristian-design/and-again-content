import json
def P(*a):
    out=[]
    for x in a:
        if isinstance(x,tuple): out.append({"text":x[0],"gap":True,"accept":list(x[1])})
        else: out.append({"text":x})
    return out
D={}
D[15]=dict(level="A",keyWord="die Tablette",
 taps=[("Wasser trinken","der Mann","male"),("Wasser eingießen","die Frau","female"),("in der Hand liegen","die Tablette","male")],
 nouns=[("die Tablette","male"),("die Hand","male"),("der Baum","male")],
 question="Was macht der Mann?",answer="Er nimmt eine Tablette mit Wasser ein.",av="male",
 recall=[("taps",P(("Wasser",["Wasser"]),"trinken")),("taps",P("Wasser",("eingießen",["eingießen","einschenken"]))),
  ("taps",P("in der",("Hand",["Hand"]),"liegen")),("answer",P("nimmt eine",("Tablette",["Tablette"]),"mit Wasser ein"))],
 notes="Answer: 'mit Wasser' could also stand before 'eine Tablette' (less natural). Phrase 3: the pill lies in the woman's hand.")
D[16]=dict(level="B",keyWord="die Präsentation",
 taps=[("eine Präsentation halten","die Schülerin im roten Pullover","female"),("die Folien zeigen","die Leinwand","female"),("im Publikum sitzen","die Mitschüler","female")],
 nouns=[("die Präsentation","female"),("der Pullover","female"),("das Whiteboard","female"),("das Publikum","female")],
 question="Was macht die Schülerin in Rot?",answer="Sie hält eine Präsentation vor ihren Mitschülern.",av="female",
 recall=[("taps",P("eine",("Präsentation",["Präsentation"]),"halten")),("taps",P("die",("Folien",["Folien"]),"zeigen")),
  ("taps",P("im",("Publikum",["Publikum"]),"sitzen")),("answer",P(("hält",["hält"]),"eine Präsentation vor ihren Mitschülern"))],
 notes="German also allows 'Sie hält vor ihren Mitschülern eine Präsentation.' (second chip order). Schülerin (school class) rather than Studentin.")
D[17]=dict(level="A",keyWord="das Projekt",
 taps=[("eine Kappe tragen","der Mann mit der Kappe","male"),("lange Haare haben","die Frau","female"),("ein Dach aus Holz haben","die Hütte","male")],
 nouns=[("der Himmel","male"),("das Dach","male"),("die Tür","male"),("das Gras","male")],
 question="Was bauen die Leute?",answer="Sie bauen eine Hütte aus Holz.",av="male",
 recall=[("taps",P("eine",("Kappe",["Kappe","Mütze"]),"tragen")),("taps",P("lange",("Haare",["Haare"]),"haben")),
  ("taps",P("ein",("Dach",["Dach"]),"aus Holz haben")),("answer",P(("bauen",["bauen"]),"eine Hütte aus Holz"))],
 notes="Key word das Projekt is abstract and appears in no exercise (it is only the transcript's word); kept unchanged. Shed = die Hütte (A-level; der Schuppen would be B).")
D[19]=dict(level="A",keyWord="das Lineal",
 taps=[("eine Linie ziehen","der Mann","male"),("dick und rot sein","das Buch","male"),("lang und gerade sein","das Lineal","male")],
 nouns=[("das Lineal","male"),("die Brille","male"),("der Stift","male"),("das Papier","male")],
 question="Was macht der Mann?",answer="Er zieht eine Linie mit einem Lineal.",av="male",
 recall=[("taps",P("eine Linie",("ziehen",["ziehen","zeichnen"]))),("taps",P("dick und",("rot",["rot"]),"sein")),
  ("taps",P("lang und",("gerade",["gerade"]),"sein")),("answer",P("zieht eine",("Linie",["Linie"]),"mit einem Lineal")),],
 notes="Phrase 2 avoids 'Einband' (above A level): the book is thick and dark red. Answer also allows 'Er zieht mit einem Lineal eine Linie.' Phrase 1 box covers searching frames too; written for the drawing.")
D[20]=dict(level="B",keyWord="der Zeitplan",
 taps=[("sich das Kissen schnappen","die Hand","female"),("aufgeschlagen auf dem Boden liegen","das Lehrbuch","female"),("zwei lose Gurte haben","der Rucksack","female")],
 nouns=[("das Lehrbuch","female"),("der Laptop","female"),("der Rucksack","female"),("das Kissen","female")],
 question="Was macht die Hand?",answer="Sie schnappt sich das Kissen vom Boden.",av="female",
 recall=[("taps",P("sich das Kissen",("schnappen",["schnappen","greifen"]))),("taps",P(("aufgeschlagen",["aufgeschlagen"]),"auf dem Boden liegen")),
  ("taps",P("zwei lose",("Gurte",["Gurte","Riemen"]),"haben")),("answer",P("schnappt sich das",("Kissen",["Kissen"]),"vom Boden"))],
 notes="Key word der Zeitplan is not a visible thing (shown only through the labels Revise/Work/Gym/Sleep); appears in no exercise; kept unchanged.")
for i,d in D.items():
    o={"mediaId":i,"lang":"de","level":d["level"],"keyWord":d["keyWord"],
       "taps":[{"phrase":a,"target":b,"voice":c} for a,b,c in d["taps"]],
       "nouns":[{"word":a,"voice":b} for a,b in d["nouns"]],
       "question":d["question"],"answer":d["answer"].split(),"answerVoice":d["av"],"carousel":[],
       "recall":[{"from":f,"parts":p} for f,p in d["recall"]],"notes":d["notes"]}
    json.dump(o,open(f"content/de/{i}.json","w"),ensure_ascii=False,indent=1)
