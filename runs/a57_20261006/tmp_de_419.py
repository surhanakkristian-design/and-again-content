import json
def P(*a):
    out=[]
    for x in a:
        if isinstance(x,tuple): out.append({"text":x[0],"gap":True,"accept":list(x[1])})
        else: out.append({"text":x})
    return out
def tap(p,t,v): return {"phrase":p,"target":t,"voice":v}
def n(w,v): return {"word":w,"voice":v}
D={}
D[419]=dict(level="A",keyWord="kicken",
 taps=[tap("ein orangefarbenes T-Shirt tragen","die Frau","female"),tap("ein lila T-Shirt tragen","der Mann","male"),tap("durch die Luft fliegen","der Ball","male")],
 nouns=[n("der Himmel","male"),n("die Gebäude","male"),n("die Frau","female"),n("der Ball","male")],
 question="Was machen die beiden?",answer=["Sie","kicken","den","Ball","hin","und","her."],answerVoice="male",
 recall=[{"from":"taps","parts":P("ein orangefarbenes",("T-Shirt",["T-Shirt","Shirt","Top"]),"tragen")},
         {"from":"taps","parts":P("ein lila T-Shirt",("tragen",["tragen","anhaben"]))},
         {"from":"taps","parts":P("durch die Luft",("fliegen",["fliegen"]))},
         {"from":"answer","parts":P(("kicken",["kicken","schießen"]),"den Ball","hin und her")}],
 notes="The woman wears an orange crop top: 'T-Shirt' kept as in English (accept Shirt/Top). 'lila' stays uninflected (standard). Answer: 'hin und her' only natural at the end, one word order. Key word 'kicken' is used in the answer and its recall gap.")
D[383]=dict(level="A",keyWord="das Wandern",
 taps=[tap("einen blauen Rucksack tragen","die Frau","female"),tap("einen Hut tragen","der Mann","male"),tap("über die Berge fliegen","die Vögel","male")],
 nouns=[n("der Himmel","male"),n("die Berge","male"),n("die Frau","female"),n("das Gras","male")],
 question="Was machen die beiden?",answer=["Sie","wandern","in","den","Bergen."],answerVoice="male",
 recall=[{"from":"taps","parts":P("einen blauen",("Rucksack",["Rucksack"]),"tragen")},
         {"from":"taps","parts":P("einen",("Hut",["Hut","Sonnenhut"]),"tragen")},
         {"from":"taps","parts":P("über die Berge",("fliegen",["fliegen"]))},
         {"from":"answer","parts":P(("wandern",["wandern"]),"in den Bergen")}],
 notes="Phrase 2: English 'to drink from a bottle' only happens in the last frames; in most boxed frames the man walks with a yellow backpack and a hat. Written 'einen Hut tragen' (the woman wears a headband, no hat), so it fits only him in all boxed frames. Key word 'das Wandern' (noun) appears as the verb 'wandern' in the answer; no noun row (not a noun of the set). Question 'die beiden' = English 'the two people'.")
D[13]=dict(level="A",keyWord="die Serviette",
 taps=[tap("eine Serviette falten","die Frau","female"),tap("sich den Mund abwischen","die Frau","female"),tap("auf einem Stuhl sitzen","die Frau","female")],
 nouns=[n("die Frau","female"),n("die Serviette","female"),n("der Stuhl","female"),n("der Tisch","female")],
 question="Was macht die Frau?",answer=["Sie","faltet","eine","Serviette."],answerVoice="female",
 recall=[{"from":"taps","parts":P("eine",("Serviette",["Serviette"]),"falten")},
         {"from":"taps","parts":P("sich den Mund",("abwischen",["abwischen","abtupfen","abputzen"]))},
         {"from":"taps","parts":P("auf einem",("Stuhl",["Stuhl"]),"sitzen")},
         {"from":"answer","parts":P(("faltet",["faltet"]),"eine Serviette")}],
 notes="All three English targets are the same woman and the three boxes cover her through the whole clip (each phrase true only in part of it: folding first, wiping mid, sitting at the end). No noun row: Serviette is in tap row 1.")
D[6949]=dict(level="A",keyWord="die heiße Schokolade",
 taps=[tap("heiße Schokolade eingießen","die Frau","female"),tap("ein goldenes Kleid tragen","die Frau","female"),tap("aus einer Tasse trinken","der Mann mit der Mütze","male")],
 nouns=[n("die Schokolade","female"),n("das Kleid","female"),n("die Hand","female")],
 question="Was macht die Frau?",answer=["Sie","gießt","heiße","Schokolade","in","eine","Tasse."],answerVoice="female",
 recall=[{"from":"taps","parts":P("heiße",("Schokolade",["Schokolade","Trinkschokolade"]),"eingießen")},
         {"from":"taps","parts":P("ein goldenes",("Kleid",["Kleid"]),"tragen")},
         {"from":"taps","parts":P("aus einer Tasse",("trinken",["trinken"]))},
         {"from":"answer","parts":P(("gießt",["gießt","schüttet"]),"heiße Schokolade","in eine Tasse")}],
 notes="English 'the man in the hat' wears a dark knit cap: target 'der Mann mit der Mütze'. Noun 1 = 'die Schokolade' (the validator rejects the lower-case adjective of the key word 'die heiße Schokolade' in a noun pill; the key word stays in tap row 1 and the answer). The cups are glass mugs; 'Tasse' used everywhere. Answer: 'Sie gießt in eine Tasse heiße Schokolade' is also possible German but marked; the given order is the natural one. No noun row: the key word is in tap row 1.")
D[330]=dict(level="A",keyWord="das Gate",
 taps=[tap("zum Gate rennen","das Mädchen","female"),tap("das Ticket zeigen","das Mädchen","female"),tap("die Tür aufhalten","der Mann","male")],
 nouns=[n("das Fenster","female"),n("das Gate","female"),n("das Mädchen","female"),n("der Koffer","female")],
 question="Wohin rennt das Mädchen?",answer=["Sie","rennt","zum","Gate."],answerVoice="female",
 recall=[{"from":"taps","parts":P("zum",("Gate",["Gate","Flugsteig"]),"rennen")},
         {"from":"taps","parts":P("das",("Ticket",["Ticket","Flugticket","Bordkarte"]),"zeigen")},
         {"from":"taps","parts":P("die",("Tür",["Tür"]),"aufhalten")},
         {"from":"answer","parts":P(("rennt",["rennt","läuft"]),"zum Gate")}],
 notes="'das Gate' is the everyday German airport word (formal: der Flugsteig). Pronoun 'sie' for das Mädchen (what natives say). Tap boxes 1 and 2 are the same box on the girl (running most of the time, showing the ticket in the middle). Phrase 3: the man scans the pass at the desk in the middle frames and holds the plane door open at the end; English phrase kept. No noun row: Gate is in tap row 1.")
for i,d in D.items():
    o={"mediaId":i,"lang":"de"}; o.update(d); o["carousel"]=[]
    o={k:o[k] for k in ["mediaId","lang","level","keyWord","taps","nouns","question","answer","answerVoice","carousel","recall","notes"]}
    json.dump(o,open(f"content/de/{i}.json","w"),ensure_ascii=False,indent=1)
