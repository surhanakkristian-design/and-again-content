import json
def R(frm,*parts):
    ps=[]
    for p in parts:
        if isinstance(p,tuple): ps.append({"text":p[0],"gap":True,"accept":list(p)})
        else: ps.append({"text":p})
    return {"from":frm,"parts":ps}
def T(p,t,v): return {"phrase":p,"target":t,"voice":v}
def N(w,v="female"): return {"word":w,"voice":v}
D={
289:dict(level="B",keyWord="die Angst",
 taps=[T("sich an die Brust greifen","die Frau in Blau","female"),T("sich an einen Pfosten klammern","die Frau in Blau","female"),T("sich von hinten nähern","die Frau in Gelb","female")],
 nouns=[N("die Gipfel"),N("das Geländer"),N("die Spiegelung")],
 question="Was macht die Frau in Blau?",answer=["Sie","klammert","sich","vor","Angst","an","einen","Pfosten."],answerVoice="female",
 recall=[R("taps","sich an die",("Brust",),"greifen"),R("taps","sich an einen Pfosten",("klammern","festhalten")),R("taps","sich von hinten",("nähern",)),R("answer","klammert sich vor",("Angst",),"an einen Pfosten")],
 notes="'Blau' kept from English (the jacket is turquoise). 'vor Angst' could also stand after 'an einen Pfosten' (marked, less natural); the chosen order is the standard one. Tap 1 box also covers frames where she grips the railing; most boxed frames show the hand at the chest. Tap 3: the woman in yellow is mostly standing/walking behind; 'sich von hinten nähern' fits her only. Accept 'festhalten' in row 2 does not fit grammatically with 'an' + 'sich' ... see: 'sich an einen Pfosten festhalten' is fine colloquially. No noun row: Angst is not a noun of the set; the answer row gaps the key word."),
290:dict(level="A",keyWord="das Gefühl",
 taps=[T("die Hand auf die Brust legen","die Frau","female"),T("die Augen schließen","die Frau","female"),T("ein graues Hemd tragen","der Mann mit den langen Haaren","male")],
 nouns=[N("die Fahne"),N("die Frau"),N("das Glas")],
 question="Was macht die Frau?",answer=["Sie","legt","die","Hand","auf","die","Brust."],answerVoice="female",
 recall=[R("taps","die Hand auf die",("Brust",)," legen".strip()),R("taps","die Augen",("schließen","zumachen")),R("taps","ein graues",("Hemd",),"tragen"),R("answer",("legt",),"die Hand auf die Brust")],
 notes="Key word 'das Gefühl' is not a visible thing; not forced into the texts. Tap 2 box also covers frames where her eyes are open; she closes them in several boxed frames and nobody else does. 'die Fahne' chosen over 'die Flagge' (everyday word, A2). Tap 1 and answer gaps differ (Brust vs legt) so the rows do not look alike."),
292:dict(level="A",keyWord="der Kampf",
 taps=[T("ein Kissen hochheben","die Frau","female"),T("ein graues T-Shirt tragen","die Frau","female"),T("einen Bart haben","der Mann","male")],
 nouns=[N("das Fenster"),N("das Kissen"),N("die Pflanze"),N("das Bett")],
 question="Was machen sie auf dem Bett?",answer=["Sie","machen","eine","Kissenschlacht."],answerVoice="female",
 recall=[R("taps","ein",("Kissen",),"hochheben"),R("taps","ein graues T-Shirt",("tragen","anhaben")),R("taps","einen",("Bart",),"haben"),R("answer","machen eine",("Kissenschlacht",))],
 notes="Key word 'der Kampf': a pillow fight is 'die Kissenschlacht' in German ('Kissenkampf' is not used), so the answer uses Kissenschlacht; the key word itself does not appear naturally. Proposal: owner may consider 'die Schlacht'/'Kissenschlacht' for this video. Tap 1: the man also lifts his pillow at times; the woman's raised pillow over her head is the clearest. Tap 3 box frame 1 has the man off screen."),
293:dict(level="B",keyWord="das Filmemachen",
 taps=[T("die Augen mit der Hand abschirmen","die Frau mit dem Schal","female"),T("hinter der Kamera hocken","die Frau mit der Kappe","female"),T("auf der Brüstung sitzen","die Taube","female")],
 nouns=[N("das Mikrofon"),N("der Reflektor"),N("die Taube"),N("das Stativ")],
 question="Worauf ist die Kamera montiert?",answer=["Die","Kamera","ist","auf","einem","Stativ","montiert."],answerVoice="female",
 recall=[R("taps","die Augen mit der Hand",("abschirmen","schützen")),R("taps","hinter der Kamera",("hocken","kauern")),R("taps","auf der",("Brüstung",),"sitzen"),R("answer","ist auf einem",("Stativ",),"montiert")],
 notes="Key word 'das Filmemachen' is an activity, not a visible noun; not forced. Tap 1: the woman in the scarf shields her eyes only in some boxed frames, otherwise she stands posing/smiling; phrase written for the shielding moment. Tap 3: pigeon box is OFF in a few frames."),
294:dict(level="A",keyWord="das Feuer",
 taps=[T("einen langen Stock halten","die Frau","female"),T("Holz aufs Feuer legen","der Mann","male"),T("zwischen den Steinen brennen","das Feuer","female")],
 nouns=[N("die Bäume"),N("der Mann","male"),N("das Feuer"),N("die Steine")],
 question="Was macht der Mann?",answer=["Er","legt","Holz","aufs","Feuer."],answerVoice="male",
 recall=[R("taps","einen langen",("Stock",),"halten"),R("taps","Holz aufs",("Feuer",),"legen"),R("taps","zwischen den Steinen",("brennen",)),R("answer","legt",("Holz",),"aufs Feuer")],
 notes="Tap 2 box covers the whole clip but the man puts the log on only at the start; later he sits and looks at the sparks. Phrase kept as in English. No noun row: Feuer is in tap row 2 and the answer row."),
}
for i,d in D.items():
    out={"mediaId":i,"lang":"de",**{k:d[k] for k in ["level","keyWord","taps","nouns","question","answer","answerVoice"]},"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(out,open(f"content/de/{i}.json","w"),ensure_ascii=False,indent=2)
