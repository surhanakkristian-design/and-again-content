import json
def P(*parts):
    out=[]
    for p in parts:
        if isinstance(p,tuple): out.append({"text":p[0],"gap":True,"accept":list(p[1])})
        else: out.append({"text":p})
    return out
D={}
D[42]=dict(mediaId=42,lang="de",level="A",keyWord="die Prüfung",
 taps=[dict(phrase="sich seine Prüfung ansehen",target="der Mann",voice="male"),
       dict(phrase="auf den Blättern liegen",target="der Stift",voice="male"),
       dict(phrase="den Tisch bedecken",target="die Blätter",voice="male")],
 nouns=[dict(word="die Tür",voice="male"),dict(word="der Stuhl",voice="male"),dict(word="die Wand",voice="male"),dict(word="die Blätter",voice="male")],
 question="Was sieht sich der Mann an?",answer=["Er","sieht","sich","seine","Prüfung","an."],answerVoice="male",carousel=[],
 recall=[dict(**{"from":"taps"},parts=P("sich seine",("Prüfung",["Prüfung"]),"ansehen")),
         dict(**{"from":"taps"},parts=P("auf den",("Blättern",["Blättern","Papieren"]),"liegen")),
         dict(**{"from":"taps"},parts=P("den Tisch",("bedecken",["bedecken"]))),
         dict(**{"from":"answer"},parts=P(("sieht",["sieht","schaut"]),"sich seine Prüfung an"))],
 notes="Papers = 'die Blätter' (everyday word for sheets of paper; 'die Papiere' would suggest documents). Tap box 1 also covers frames where the man walks to/away from the table; phrase written for the frames where he sits and looks down at the papers. No noun row: 'die Prüfung' is not one of the nouns and is already in tap row 1 and the answer.")
D[43]=dict(mediaId=43,lang="de",level="A",keyWord="sich drehen",
 taps=[dict(phrase="an einer Schnur ziehen",target="die Hand",voice="male"),
       dict(phrase="sich sehr schnell drehen",target="die goldene Kugel",voice="male"),
       dict(phrase="eine goldene Kugel halten",target="die Hand",voice="male")],
 nouns=[dict(word="der Drucker",voice="male"),dict(word="die Kugel",voice="male"),dict(word="der Schreibtisch",voice="male")],
 question="Was macht die goldene Kugel?",answer=["Sie","dreht","sich","sehr","schnell."],answerVoice="male",carousel=[],
 recall=[dict(**{"from":"taps"},parts=P("an einer",("Schnur",["Schnur","Leine"]),"ziehen")),
         dict(**{"from":"taps"},parts=P("sich sehr schnell",("drehen",["drehen"]))),
         dict(**{"from":"taps"},parts=P("eine goldene",("Kugel",["Kugel"]),"halten")),
         dict(**{"from":"answer"},parts=P("dreht sich sehr",("schnell",["schnell"])))],
 notes="Strictly the ring spins around the golden ball; like the English, the whole gyroscope is called 'die goldene Kugel'. Tap box 1 ('an einer Schnur ziehen') also covers later frames where the hand only places the gyroscope on the stand; phrase written for the string-pulling frames, as in English. 'Sie' = die Kugel; answerVoice kept male (narrator voice, subject is a thing). Key word in tap row 2.")
D[44]=dict(mediaId=44,lang="de",level="B",keyWord="die Wut",
 taps=[dict(phrase="die Fäuste ballen",target="die Frau",voice="female"),
       dict(phrase="sich an den Kopf fassen",target="die Frau",voice="female"),
       dict(phrase="verstreut herumliegen",target="die Blumen",voice="female")],
 nouns=[dict(word="die Zöpfe",voice="female"),dict(word="die Schürze",voice="female"),dict(word="die Faust",voice="female"),dict(word="die Blumen",voice="female")],
 question="Was macht die Frau?",answer=["Sie","ballt","vor","Wut","die","Fäuste."],answerVoice="female",carousel=[],
 recall=[dict(**{"from":"taps"},parts=P("die Fäuste",("ballen",["ballen"]))),
         dict(**{"from":"taps"},parts=P("sich an den",("Kopf",["Kopf"]),"fassen")),
         dict(**{"from":"taps"},parts=P(("verstreut",["verstreut"]),"herumliegen")),
         dict(**{"from":"answer"},parts=P("ballt vor",("Wut",["Wut","Zorn"]),"die Fäuste"))],
 notes="German also allows 'Sie ballt die Fäuste vor Wut.' (both orders correct; chips allow two orders). Taps 1 and 2 share one box (same woman) as in English; tap boxes also cover the kick and bag-throw frames - phrases written for the frames where she does them. Braids are cornrows; 'die Zöpfe' is the everyday word. No noun row: 'die Wut' is not a noun of the set and is in the answer row.")
D[45]=dict(mediaId=45,lang="de",level="A",keyWord="wütend",
 taps=[dict(phrase="den Mann anschreien",target="die Frau",voice="female"),
       dict(phrase="auf dem Boden liegen",target="die Wäsche",voice="female"),
       dict(phrase="eine graue Jacke tragen",target="der Mann",voice="male")],
 nouns=[dict(word="die Flaschen",voice="female"),dict(word="die Waschmaschine",voice="female"),dict(word="die Frau",voice="female"),dict(word="die Wäsche",voice="female")],
 question="Was macht die wütende Frau?",answer=["Sie","schreit","den","Mann","an."],answerVoice="female",carousel=[],
 recall=[dict(**{"from":"taps"},parts=P("den",("Mann",["Mann"]),"anschreien")),
         dict(**{"from":"taps"},parts=P("auf dem",("Boden",["Boden"]),"liegen")),
         dict(**{"from":"taps"},parts=P("eine graue",("Jacke",["Jacke"]),"tragen")),
         dict(**{"from":"answer"},parts=P(("schreit",["schreit"]),"den Mann an"))],
 notes="Clothes = 'die Wäsche' (natural word for laundry in a laundromat). Tap box 1 also covers the opening frames where the woman walks in and picks up the clothes; phrase written for the shouting frames (most boxed frames). Key word 'wütend' (adjective) appears in the question only; no recall row can carry it naturally.")
D[46]=dict(mediaId=46,lang="de",level="A",keyWord="der Apfel",
 taps=[dict(phrase="einen Apfel aufschneiden",target="die Frau",voice="female"),
       dict(phrase="einen schwarzen Bart haben",target="der Mann",voice="male"),
       dict(phrase="auf einer Kiste stehen",target="der Vogel",voice="female")],
 nouns=[dict(word="der Mann",voice="male"),dict(word="die Frau",voice="female"),dict(word="der Vogel",voice="female"),dict(word="der Apfel",voice="female")],
 question="Was macht die Frau?",answer=["Sie","isst","einen","roten","Apfel."],answerVoice="female",carousel=[],
 recall=[dict(**{"from":"taps"},parts=P("einen",("Apfel",["Apfel"]),"aufschneiden")),
         dict(**{"from":"taps"},parts=P("einen schwarzen",("Bart",["Bart"]),"haben")),
         dict(**{"from":"taps"},parts=P("auf einer",("Kiste",["Kiste"]),"stehen")),
         dict(**{"from":"answer"},parts=P(("isst",["isst"]),"einen roten Apfel"))],
 notes="Tap box 1 covers the whole clip (picking, polishing, biting, then cutting); kept 'aufschneiden' as in English because it is the only apple action the man never does (he also eats/bites). The bird is a magpie; 'der Vogel' kept as in English. No noun row: 'der Apfel' is already in tap row 1 and the answer row.")
for k,v in D.items():
    json.dump(v,open(f"content/de/{k}.json","w"),ensure_ascii=False,indent=2)
