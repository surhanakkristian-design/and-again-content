import json
def g(t,acc=None): return {"text":t,"gap":True,"accept":acc or [t]}
def p(t): return {"text":t}
D={}
D[587]=dict(level="B",keyWord="der Puck",
 taps=[("den Puck einwerfen","der Schiedsrichter","male"),("ihren Treffer bejubeln","die Spielerin in Gelb","female"),("im Netz landen","der Puck","female")],
 nouns=[("der Puck","female"),("der Handschuh","female"),("der Helm","female"),("das Trikot","female")],
 question="Was macht die Spielerin in Gelb?",answer="Sie bejubelt ihren Treffer.",answerVoice="female",
 recall=[("taps",[p("den"),g("Puck"),p("einwerfen")]),("taps",[p("ihren"),g("Treffer",["Treffer","Tor"]),p("bejubeln")]),("taps",[p("im Netz"),g("landen")]),
         ("answer",[g("bejubelt",["bejubelt","feiert"]),p("ihren Treffer")])],
 notes="'den Puck einwerfen' = the referee's face-off drop in German hockey language (Bully). Tap 2: the English green box also covers frames where she skates with the puck and shoots (box_02/03); she celebrates in box_05/06; phrase follows English. Tap 3: the blue box also covers the puck in the referee's hand, on the ice and in her glove; 'im Netz landen' describes the goal moment (box_04). No noun row: Puck is in tap row 1.")
D[7069]=dict(level="B",keyWord="vorfahren",
 taps=[("den Strohhut schwenken","der Mann","male"),("auf der Türschwelle stehen","die junge Frau","female"),("alles vom Fenster aus beobachten","die alte Frau","female")],
 nouns=[("der Traktor","male"),("die Sonnenblumen","male"),("der Strohhut","male"),("der Kies","male")],
 question="Was macht der Mann?",answer="Er fährt auf einem roten Traktor vor.",answerVoice="male",
 recall=[("taps",[p("den"),g("Strohhut",["Strohhut","Hut"]),p("schwenken")]),("taps",[p("auf der"),g("Türschwelle",["Türschwelle","Schwelle"]),p("stehen")]),
         ("taps",[p("alles vom Fenster aus"),g("beobachten",["beobachten"])]),("answer",[g("fährt"),p("auf einem roten Traktor vor")])],
 notes="Tap 1: he swings the hat in frames 5-8 only; in frames 1-4 he drives up with the hat on (English phrase is the same). Key word in the answer ('fährt ... vor'); answer row gaps 'fährt' (the key verb). German could also say 'Er fährt mit einem roten Traktor vor.' (auf/mit both fine), single chip order otherwise.")
D[7761]=dict(level="B",keyWord="das Lebewesen",
 taps=[("in ein Einmachglas greifen","der Oktopus","male"),("ein Klemmbrett halten","der Mann","male"),("in Gelächter ausbrechen","die Frau","female")],
 nouns=[("der Oktopus","male"),("das Einmachglas","male"),("die Roboter","male"),("das Klemmbrett","male")],
 question="Was macht der Oktopus?",answer="Er greift in ein Einmachglas.",answerVoice="male",
 recall=[("taps",[p("in ein Einmachglas"),g("greifen",["greifen","fassen"])]),("taps",[p("ein"),g("Klemmbrett"),p("halten")]),
         ("taps",[p("in"),g("Gelächter",["Gelächter","Lachen"]),p("ausbrechen")]),("answer",[p("greift in ein"),g("Einmachglas",["Einmachglas","Glas"])])],
 notes="Key word 'das Lebewesen' names no noun of the set and fits none of the exercises naturally (the clip contrasts a living octopus with lifeless robots); kept, owner decides. The man holds the clipboard loosely, so 'halten' not 'umklammern'. The octopus opens the jar and pulls a crab out of it; 'in ein Einmachglas greifen' covers the boxed frames.")
D[5626]=dict(level="B",keyWord="außer Betrieb sein",
 taps=[("neben dem Lieferroboter knien","der Mann","male"),("es sich zwischen den Orangen gemütlich machen","die Katze","male"),("über den Gehweg kullern","die Orange","male")],
 nouns=[("die Katze","male"),("die Straßenbahn","male"),("der Lieferroboter","male"),("die Windräder","male")],
 question="Was ist im Lieferroboter?",answer="Eine Katze hockt zwischen den Orangen.",answerVoice="male",
 recall=[("taps",[p("neben dem Lieferroboter"),g("knien")]),("taps",[p("es sich zwischen den Orangen"),g("gemütlich",["gemütlich","bequem"]),p("machen")]),
         ("taps",[p("über den Gehweg"),g("kullern",["kullern","rollen"])]),("answer",[p("hockt zwischen den"),g("Orangen")])],
 notes="Key word 'außer Betrieb sein' is not visible: the robot is not shown broken, only open with a cat inside instead of a delivery; kept, owner decides. Tap 3: the orange rolls in the first boxed frames and then lies still on the pavement. Tap 1: in the last frame the man sits on the ground. Answer voice male (cat has no natural gender; 'Katze' grammatically feminine).")
D[7929]=dict(level="B",keyWord="das Einparken",
 taps=[("zwei kleine Autos zerquetschen","der Monstertruck","male"),("beide Fäuste in die Luft recken","der Mann auf dem Truck","male"),("die Arme verschränken","die Frau vorne","female")],
 nouns=[("der Monstertruck","male"),("das Auto","male"),("die Parklücke","male"),("die Stiefel","male")],
 question="Was macht der Monstertruck?",answer="Er zerquetscht zwei kleine Autos.",answerVoice="male",
 recall=[("taps",[p("zwei kleine Autos"),g("zerquetschen",["zerquetschen","zerdrücken"])]),("taps",[p("beide"),g("Fäuste"),p("in die Luft recken")]),
         ("taps",[p("die Arme"),g("verschränken")]),("answer",[p("zerquetscht zwei kleine"),g("Autos",["Autos","Wagen"])])],
 notes="Key word 'das Einparken' is the act of parking; the clip shows the truck already standing on two cars, so it names no noun of the set; English noun 'a parking space' = 'die Parklücke' (der Parkplatz would read as the car park). Kept, owner decides. Noun 2 'das Auto' (the pill sits on the red car; the validator does not accept an adjective in a noun pill). Tap 2: in box_01 frames 1-2 the man is only partly visible.")
for i,d in D.items():
    out={"mediaId":i,"lang":"de","level":d["level"],"keyWord":d["keyWord"],
      "taps":[{"phrase":a,"target":b,"voice":c} for a,b,c in d["taps"]],
      "nouns":[{"word":a,"voice":b} for a,b in d["nouns"]],
      "question":d["question"],"answer":d["answer"].split(),"answerVoice":d["answerVoice"],"carousel":[],
      "recall":[{"from":f,"parts":ps} for f,ps in d["recall"]],"notes":d["notes"]}
    json.dump(out,open(f"content/de/{i}.json","w"),ensure_ascii=False,indent=2)
