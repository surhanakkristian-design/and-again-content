import json
def T(p,t,v): return {"phrase":p,"target":t,"voice":v}
def N(w,v): return {"word":w,"voice":v}
def R(frm,parts):
    out=[]
    for p in parts:
        if isinstance(p,tuple): out.append({"text":p[0],"gap":True,"accept":list(p[1])})
        else: out.append({"text":p})
    return {"from":frm,"parts":out}
D={}
D[264]=dict(level="B",keyWord="die Emotion",
 taps=[T("einen Blumenstrauß umklammern","die Frau","female"),T("sich an das Geländer lehnen","die Frau","female"),T("einen Gepäckwagen schieben","der Mann","male")],
 nouns=[N("der Blumenstrauß","female"),N("die Strickjacke","female"),N("das Geländer","female"),N("die Jeans","female")],
 question="Was hält die Frau in den Händen?",answer="Sie umklammert einen gelben Blumenstrauß.".split(),answerVoice="female",
 recall=[R("taps",["einen Blumenstrauß",("umklammern",["umklammern","festhalten"])]),
         R("taps",["sich an das",("Geländer",["Geländer"]),"lehnen"]),
         R("taps",["einen",("Gepäckwagen",["Gepäckwagen","Kofferkuli"]),"schieben"]),
         R("answer",["umklammert einen",("gelben",["gelben"]),"Blumenstrauß"])],
 notes="Key word die Emotion is not a pill or phrase (same as English). Gepäckwagen/Kofferkuli both accepted. 'sich an das Geländer lehnen': she stands at the railing with hands/bouquet resting on it.")
D[265]=dict(level="A",keyWord="der Angestellte",
 taps=[T("einen Umschlag bekommen","der Mann mit Brille","male"),T("eine Jacke anziehen","der Mann mit Brille","male"),T("ihm auf die Schulter klopfen","die Frau","female")],
 nouns=[N("der Angestellte","male"),N("das Papier","male"),N("die Tastatur","male"),N("das Fenster","male")],
 question="Was bekommt der Angestellte?",answer="Er bekommt einen Umschlag.".split(),answerVoice="male",
 recall=[R("taps",["einen Umschlag",("bekommen",["bekommen","kriegen"])]),
         R("taps",["eine Jacke",("anziehen",["anziehen"])]),
         R("taps",["ihm auf die",("Schulter",["Schulter"]),"klopfen"]),
         R("nouns",["der",("Angestellte",["Angestellte","Mitarbeiter"])]),
         R("answer",["bekommt einen",("Umschlag",["Umschlag","Briefumschlag"])])],
 notes="Phrase 3: the boss pats his shoulder -> 'ihm auf die Schulter klopfen' (more natural than 'seine Schulter berühren'). The boss is drawn silver-haired; target kept as English 'die Frau'.")
D[266]=dict(level="A",keyWord="die Energie",
 taps=[T("die Treppe hinauflaufen","die Frau in Weiß","female"),T("auf und ab springen","die Frau in Weiß","female"),T("die Hände auf die Knie legen","der Mann","male")],
 nouns=[N("die Treppe","female"),N("die Straßenlaterne","female"),N("die Mauer","female"),N("der Himmel","female")],
 question="Was macht die Frau in Weiß?",answer="Sie läuft die Treppe hinauf.".split(),answerVoice="female",
 recall=[R("taps",["die",("Treppe",["Treppe"]),"hinauflaufen"]),
         R("taps",["auf und ab",("springen",["springen","hüpfen"])]),
         R("taps",["die Hände auf die",("Knie",["Knie"]),"legen"]),
         R("answer",[("läuft",["läuft","rennt"]),"die Treppe hinauf"])],
 notes="Key word die Energie is not a pill or phrase (same as English). English 'steps' -> 'die Treppe' (the everyday word for a flight of steps; 'die Stufen' also possible). Phrase 3 'die Hände auf die Knie legen' chosen over 'sich auf die Knie stützen' (B1) for level A.")
D[267]=dict(level="A",keyWord="der Ingenieur",
 taps=[T("einen Roboter bauen","der Mann in Schwarz","male"),T("einen Würfel hochheben","der Roboter","male"),T("in die Hände klatschen","der Mann im weißen Kittel","male")],
 nouns=[N("der Ingenieur","male"),N("der Roboter","male"),N("der Laptop","male"),N("die Box","male")],
 question="Was macht der Ingenieur?",answer="Er baut einen kleinen Roboter.".split(),answerVoice="male",
 recall=[R("taps",["einen Roboter",("bauen",["bauen"])]),
         R("taps",["einen",("Würfel",["Würfel"]),"hochheben"]),
         R("taps",["in die Hände",("klatschen",["klatschen"])]),
         R("nouns",["der",("Ingenieur",["Ingenieur"])]),
         R("answer",["baut einen kleinen",("Roboter",["Roboter","Roboterarm"])])],
 notes="English 'box' is a clear plastic tray -> 'die Box' (everyday word for a plastic container; 'die Schale' would also fit). Phrase 1 box also covers typing frames; building is what he does in most of them.")
D[268]=dict(level="A",keyWord="der Umschlag",
 taps=[T("den Umschlag küssen","die Frau in Rot","female"),T("eine Kerze halten","die Frau in Rot","female"),T("hinter der Lampe schlafen","die Katze","female")],
 nouns=[N("die Lampe","female"),N("die Katze","female"),N("die Kerze","female"),N("der Umschlag","female")],
 question="Was küsst die Frau in Rot?",answer="Sie küsst den Umschlag.".split(),answerVoice="female",
 recall=[R("taps",["den Umschlag",("küssen",["küssen"])]),
         R("taps",["eine",("Kerze",["Kerze"]),"halten"]),
         R("taps",["hinter der Lampe",("schlafen",["schlafen"])]),
         R("answer",["küsst den",("Umschlag",["Umschlag","Briefumschlag"])])],
 notes="Key word appears in phrase 1 and the answer, so no noun row. The kiss is only briefly visible; verifier please check the boxed frames.")
for mid,d in D.items():
    o={"mediaId":mid,"lang":"de","level":d["level"],"keyWord":d["keyWord"],"taps":d["taps"],"nouns":d["nouns"],"question":d["question"],
       "answer":d["answer"],"answerVoice":d["answerVoice"],"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(o,open(f"content/de/{mid}.json","w"),ensure_ascii=False,indent=2)
