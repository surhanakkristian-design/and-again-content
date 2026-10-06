import json
def P(*a):
    out=[]
    for x in a:
        if isinstance(x,tuple): out.append({"text":x[0],"gap":True,"accept":list(x[1])})
        else: out.append({"text":x})
    return out
def N(w,v): return {"word":w,"voice":v}
def T(p,t,v): return {"phrase":p,"target":t,"voice":v}
D={}
D[198]=dict(level="B",keyWord="der Krampf",
 taps=[T("sich die schmerzende Wade halten","die Frau","female"),T("auf der Laufbahn knien","der Mann","male"),T("den Daumen nach oben strecken","die Frau","female")],
 nouns=[N("die Frau","female"),N("der Mann","male"),N("die Hochhäuser","female"),N("die Laufbahn","female")],
 question="Was umklammert die Frau?",answer="Sie umklammert ihre verkrampfte Wade.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":P("sich die schmerzende",("Wade",["Wade"]),"halten")},
         {"from":"taps","parts":P("auf der",("Laufbahn",["Laufbahn","Bahn"]),"knien")},
         {"from":"taps","parts":P("den",("Daumen",["Daumen"]),"nach oben strecken")},
         {"from":"answer","parts":P("umklammert ihre",("verkrampfte",["verkrampfte","schmerzende"]),"Wade")}],
 notes="Key word der Krampf is not a noun of the set; it appears via the adjective 'verkrampfte' in the answer (B2) and is gapped there. Phrase 1 boxes also cover the opening running frames (no clutching yet); written for the sitting/clutching frames that dominate. Phrase 3 box covers the woman throughout; the thumbs up only happens at the end. 'die Hochhäuser' chosen over 'die Wolkenkratzer' as the everyday word for the lit city towers.")
D[199]=dict(level="A",keyWord="krachen",
 taps=[T("ein rotes Auto fahren","der Mann","male"),T("beide Arme hochheben","der Mann","male"),T("ein gelbes T-Shirt tragen","der Mann","male")],
 nouns=[N("der Mann","male"),N("das Auto","male"),N("der Autoscooter","male")],
 question="Was fährt der Mann?",answer="Er fährt ein rotes Auto.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":P("ein rotes",("Auto",["Auto"]),"fahren")},
         {"from":"taps","parts":P("beide",("Arme",["Arme","Hände"]),"hochheben")},
         {"from":"taps","parts":P("ein gelbes",("T-Shirt",["T-Shirt","Shirt"]),"tragen")},
         {"from":"answer","parts":P(("fährt",["fährt"]),"ein rotes Auto")}],
 notes="Key word krachen does not appear in any exercise: the English frame (drive a red car / arms up / yellow shirt; question 'what is he driving') leaves no natural slot for it. Proposal for the owner: phrase 1 could become 'in andere Autos krachen' (the red car does bump the green one), but the question/answer are about driving. 'Auto' kept at level A; the native word is 'der Autoscooter' (above A level). All three tap boxes are the same man; phrase 2 'beide Arme hochheben' only happens in the last frames, phrase 1 is true in most boxed frames. Nouns: validate57 rejects adjective+noun pills ('das rote Auto' / 'das gelbe Auto', which would be the natural pair), so noun 2 = 'das Auto' (the man's red car, same word as phrase and answer) and noun 3 = 'der Autoscooter' (the yellow one) to keep the two pills distinct; owner may prefer the colour pair. The early POV/hand frames are the man's own hand on the wheel.")
D[200]=dict(level="A",keyWord="die Sahne",
 taps=[T("die Sahne schlagen","der Mann","male"),T("eine Waffel essen","der Mann","male"),T("ein Tuch auf dem Kopf tragen","die Frau","female")],
 nouns=[N("die Sahne","male"),N("die Waffel","male"),N("der Teller","male")],
 question="Was macht der Mann?",answer="Er schlägt die Sahne.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":P("die",("Sahne",["Sahne"]),"schlagen")},
         {"from":"taps","parts":P("eine",("Waffel",["Waffel"]),"essen")},
         {"from":"taps","parts":P("ein",("Tuch",["Tuch"]),"auf dem Kopf tragen")},
         {"from":"answer","parts":P(("schlägt",["schlägt","rührt"]),"die Sahne")}],
 notes="'Sahne schlagen' is the native collocation for whisking cream (English 'mix'). Phrase 2 box covers the man through most of the clip but he only eats the waffle at the very end; written for the target's final action. Phrase 3: 'ein Tuch auf dem Kopf tragen' avoids 'Kopftuch' (religious connotation); the man's bowl-on-head moment is not a Tuch. No noun row: Sahne is in tap row 1.")
D[201]=dict(level="A",keyWord="das Krokodil",
 taps=[T("im Fluss schwimmen","das Krokodil","male"),T("aus dem Wasser kommen","das Krokodil","male"),T("das Maul weit öffnen","das Krokodil","male")],
 nouns=[N("das Krokodil","male"),N("die Bäume","male"),N("der Fluss","male")],
 question="Was macht das Krokodil?",answer="Es öffnet das Maul weit.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":P("im",("Fluss",["Fluss"]),"schwimmen")},
         {"from":"taps","parts":P("aus dem Wasser",("kommen",["kommen","kriechen"]))},
         {"from":"taps","parts":P("das Maul weit",("öffnen",["öffnen","aufmachen"]))},
         {"from":"nouns","parts":P("das",("Krokodil",["Krokodil"]))},
         {"from":"answer","parts":P("öffnet das",("Maul",["Maul"]),"weit")}],
 notes="All three tap boxes cover the same crocodile for the whole clip; each phrase is true in its part of the clip (swim at the start, come out mid, open mouth at the end). 'das Maul' is the correct word for an animal's mouth (slightly above A1 but the plain right word). Answer pronoun 'es' (das Krokodil); voice kept male as in English. Noun row added: Krokodil appears in no other row.")
D[202]=dict(level="A",keyWord="überqueren",
 taps=[T("die Straße überqueren","der Mann","male"),T("auf sein Handy schauen","der Mann","male"),T("den Daumen hochhalten","der Mann","male")],
 nouns=[N("der Mann","male"),N("das Auto","male"),N("die Häuser","male"),N("die Straße","male")],
 question="Was macht der Mann?",answer="Er überquert die Straße.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":P("die Straße",("überqueren",["überqueren"]))},
         {"from":"taps","parts":P("auf sein",("Handy",["Handy"]),"schauen")},
         {"from":"taps","parts":P("den",("Daumen",["Daumen"]),"hochhalten")},
         {"from":"answer","parts":P("überquert die",("Straße",["Straße"]))}],
 notes="All three tap boxes cover the same man for the whole clip; phrase 2 (phone) is true in the WRONG part, phrase 3 (thumb up) only in the last frames. 'die Häuser' chosen as the A-level everyday word for English 'buildings' (die Gebäude is B1).")
import sys
for i,d in D.items():
    if str(i) not in sys.argv[1:]: continue
    o={"mediaId":i,"lang":"de","level":d["level"],"keyWord":d["keyWord"],"taps":d["taps"],"nouns":d["nouns"],"question":d["question"],
       "answer":d["answer"],"answerVoice":d["answerVoice"],"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(o,open(f"content/de/{i}.json","w"),ensure_ascii=False,indent=1)
