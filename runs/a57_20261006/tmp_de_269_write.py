import json
def g(t,acc=None): return {"text":t,"gap":True,"accept":acc or [t]}
def p(t): return {"text":t}
F=lambda v:"female"; 
D={
269:dict(level="B",keyWord="der Neid",
 taps=[("sehnsüchtig aus dem Fenster blicken","die Frau im Bus","female"),("am Bus vorbeiradeln","die Radfahrerin","female"),("quer auf ihrem Schoß liegen","der rostige Lenker","female")],
 nouns=[("die Radfahrerin","female"),("die Locken","female"),("das Top","female"),("der Lenker","female")],
 question="Was macht die Frau mit den Locken?",answer="Sie blickt voller Neid auf die Radfahrerin.",answerVoice="female",
 recall=[("taps",[g("sehnsüchtig",["sehnsüchtig","neidisch"]),p("aus dem Fenster blicken")]),("taps",[p("am Bus"),g("vorbeiradeln",["vorbeiradeln","vorbeifahren"])]),("taps",[p("quer auf ihrem"),g("Schoß"),p("liegen")]),("answer",[p("blickt voller"),g("Neid"),p("auf die Radfahrerin")])],
 notes="The cyclist is a woman (pink top, shorts): 'die Radfahrerin' in tap 2, noun 1 and the answer. 'sleeveless top' -> 'das Top' (in German an ärmelloses Oberteil is simply ein Top). 'curly hair' -> 'die Locken' (B1, plural). Answer: 'voller Neid' could also stand after the object ('Sie blickt auf die Radfahrerin voller Neid'), but that order is marked; the chips give one natural order. Key word Neid is gapped in the answer row; no noun row (Neid is not a noun of the set)."),
270:dict(level="A",keyWord="der Radiergummi",
 taps=[("den Radiergummi halten","das Mädchen","female"),("wie ein Berg aussehen","der Radiergummi","female"),("eine rote Sonne zeigen","die Schachtel","female")],
 nouns=[("die Schachtel","female"),("die Hand","female"),("der Radiergummi","female"),("das Papier","female")],
 question="Wie sieht der Radiergummi aus?",answer="Der Radiergummi sieht wie ein kleiner Berg aus.",answerVoice="female",
 recall=[("taps",[p("den"),g("Radiergummi"),p("halten")]),("taps",[p("wie ein Berg"),g("aussehen")]),("taps",[p("eine rote"),g("Sonne"),p("zeigen")]),("answer",[p("sieht wie ein kleiner"),g("Berg"),p("aus")])],
 notes="Tap 1: the English phrase 'to smile at the camera' fits only the selfie frames; most red-boxed frames show only her hand erasing with or holding the eraser, so the phrase is 'den Radiergummi halten' (true in the hand frames; in the opening selfie frames she holds the eraser in its box). Answer: German also allows 'Der Radiergummi sieht aus wie ein kleiner Berg.' (Ausklammerung) - both orders are natural with these chips. No noun row: Radiergummi is in tap row 1."),
272:dict(level="B",keyWord="verdunsten",
 taps=[("die leere Pfanne kippen","die Frau","female"),("aus der Pfanne verdunsten","das Wasser","female"),("eine blaue Flamme erzeugen","der Campingkocher","female")],
 nouns=[("die Schutzbrille","female"),("der Dampf","female"),("die Pfanne","female"),("der Campingkocher","female")],
 question="Was passiert mit dem Wasser?",answer="Das Wasser verdunstet in der heißen Pfanne.",answerVoice="female",
 recall=[("taps",[p("die leere Pfanne"),g("kippen",["kippen","neigen"])]),("taps",[p("aus der Pfanne"),g("verdunsten",["verdunsten","verdampfen"])]),("taps",[p("eine blaue"),g("Flamme"),p("erzeugen")]),("answer",[p("verdunstet in der"),g("heißen",["heißen"]),p("Pfanne")])],
 notes="Key word: water heated on a flame strictly 'verdampft'; 'verdunsten' is still acceptable everyday German for the puddle shrinking and vanishing, so kept; 'verdampfen' accepted in the recall row. Tap 1: the red box also covers the early frames where she only leans over the pan; phrase written for the tilt/show frames (end of clip, the still). 'frying pan' -> 'die Pfanne' everywhere for consistency. 'goggles' -> 'die Schutzbrille'."),
273:dict(level="A",keyWord="der Abend",
 taps=[("hinter den Hügeln untergehen","die Sonne","male"),("lange Haare haben","die Frau","female"),("einen grünen Pullover tragen","der Mann","male")],
 nouns=[("der Himmel","male"),("die Sonne","male"),("die Häuser","male"),("die Frau","female")],
 question="Was macht die Sonne?",answer="Die Sonne geht hinter den Hügeln unter.",answerVoice="male",
 recall=[("taps",[p("hinter den Hügeln"),g("untergehen")]),("taps",[p("lange"),g("Haare"),p("haben")]),("taps",[p("einen grünen"),g("Pullover",["Pullover","Pulli"]),p("tragen")]),("answer",[p("geht hinter den"),g("Hügeln",["Hügeln","Bergen"]),p("unter")])],
 notes="Key word 'der Abend' names the time of the clip, not a thing in the frame, so it appears in no exercise (none of the nouns is Abend; nothing forced). Answer voice stays male (narrator; die Sonne is an object)."),
274:dict(level="A",keyWord="jeder",
 taps=[("einen Schal hochhalten","der Mann mit dem Schal","male"),("auf den Schultern sitzen","der Junge","male"),("vom Dach leuchten","die Lichter","male")],
 nouns=[("die Lichter","male"),("der Junge","male"),("der Schal","male")],
 question="Was machen alle?",answer="Alle jubeln im Stadion.",answerVoice="male",
 recall=[("taps",[p("einen"),g("Schal"),p("hochhalten")]),("taps",[p("auf den"),g("Schultern"),p("sitzen")]),("taps",[p("vom Dach"),g("leuchten",["leuchten","strahlen","scheinen"])]),("answer",[g("jubeln",["jubeln","schreien"]),p("im Stadion")])],
 notes="Key word: English 'everyone' (all the people in a place) is 'alle' in natural German; 'jeder' (singular, each one) does not fit 'Was machen alle?' / 'Alle jubeln'. Kept 'jeder' as keyWord; proposal: database word 'alle'. 'jubeln' (cheer) used for the shouting with raised arms; 'schreien' accepted. Tap 2: 'auf jemandes Schultern' is above level A, so 'auf den Schultern sitzen'.")}
for i,d in D.items():
    out={"mediaId":i,"lang":"de","level":d["level"],"keyWord":d["keyWord"],
      "taps":[{"phrase":a,"target":b,"voice":c} for a,b,c in d["taps"]],
      "nouns":[{"word":a,"voice":b} for a,b in d["nouns"]],
      "question":d["question"],"answer":d["answer"].split(" "),"answerVoice":d["answerVoice"],
      "carousel":[],"recall":[{"from":f,"parts":ps} for f,ps in d["recall"]],"notes":d["notes"]}
    json.dump(out,open(f"content/de/{i}.json","w"),ensure_ascii=False,indent=1)
