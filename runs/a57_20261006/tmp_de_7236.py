import json
def T(p,t,v="female"): return {"phrase":p,"target":t,"voice":v}
def N(w,v="female"): return {"word":w,"voice":v}
def R(frm,*parts):
    out=[]
    for p in parts:
        if isinstance(p,str): out.append({"text":p})
        else: out.append({"text":p[0],"gap":True,"accept":list(p)})
    return {"from":frm,"parts":out}
F="female"
files={
7236:dict(level="B",keyWord="der Hurrikan",
 taps=[T("über die Ufermauer schlagen","die Welle"),T("sich im Wind biegen","die Palmen"),T("einen gestreiften Bezug haben","der Liegestuhl")],
 nouns=[N("die Palme"),N("der Liegestuhl"),N("der Eimer"),N("die Flipflops")],
 question="Was machen die Wellen?",answer="Die Wellen schlagen über die Ufermauer.".split(),answerVoice=F,
 recall=[R("taps","über die",("Ufermauer","Mauer"),"schlagen"),R("taps","sich im Wind",("biegen","beugen")),R("taps","einen gestreiften",("Bezug","Stoff"),"haben"),R("answer",("schlagen","brechen"),"über die Ufermauer")],
 notes="Key word 'der Hurrikan' is not named in any exercise (as in English: the storm is the setting); no noun row because the key word is not a noun of the set. 'Ufermauer' = the sea wall of the promenade (B-level word); 'Bezug' = the striped fabric seat of the deckchair. Noun 1 singular 'die Palme' (English 'a palm tree', pill on one tree); 'die Flipflops' plural (one pair). Phrase 1 target: English 'the wave', several waves break over the wall across the boxes."),
859:dict(level="B",keyWord="der Kleiderschrank",
 taps=[T("in den Mänteln stöbern","das Mädchen"),T("ein Kleid vor sich halten","das Mädchen"),T("die Türen des Kleiderschranks zudrücken","das Mädchen")],
 nouns=[N("der Kleiderschrank"),N("die Pullover"),N("der Mantel"),N("das Kleid")],
 question="Was macht das Mädchen?",answer="Sie stöbert im Kleiderschrank.".split(),answerVoice=F,
 recall=[R("taps","in den Mänteln",("stöbern","wühlen")),R("taps","ein",("Kleid",),"vor sich halten"),R("taps","die Türen des Kleiderschranks",("zudrücken","schließen","zumachen")),R("answer","stöbert im",("Kleiderschrank","Schrank"))],
 notes="All three English tap boxes cover the girl for the whole clip (only one person): each phrase is true in its part of the clip. 'ein Kleid vor sich halten' = she holds the red dress against herself. 'sie' for das Mädchen (what natives say), used consistently. No noun row: Kleiderschrank is in tap row 3 and the answer row."),
4809:dict(level="B",keyWord="der Korridor",
 taps=[T("einen Wäschekorb tragen","die Frau"),T("ein Fahrrad schieben","der Mann im Kapuzenpulli","male"),T("dichte Locken haben","der Mann mit den Locken","male")],
 nouns=[N("die Jacken"),N("der Wäschekorb"),N("der Korridor"),N("die Schuhe")],
 question="Was macht die Frau?",answer="Sie trägt einen Wäschekorb durch den Korridor.".split(),answerVoice=F,
 recall=[R("taps","einen",("Wäschekorb",),"tragen"),R("taps","ein Fahrrad",("schieben",)),R("taps","dichte",("Locken",),"haben"),R("answer","trägt einen Wäschekorb durch den",("Korridor","Flur","Gang"))],
 notes="Key word kept: in a flat 'der Flur' is the more everyday German word; 'der Korridor' is correct and B-level (accepted in the answer gap together with Flur/Gang). English 'coats' -> 'die Jacken': the things on the hooks are jackets/parkas, the natural German word. German also allows 'Sie trägt durch den Korridor einen Wäschekorb.' (marked, but grammatical). No noun row: Korridor is in the answer row."),
4361:dict(level="B",keyWord="einkaufen",
 taps=[T("stolz ihre Einkaufstüten hochhalten","die Frau"),T("an Schaufenstern vorbeischlendern","die Frau"),T("mit der Rolltreppe hochfahren","die Frau")],
 nouns=[N("der Wolkenkratzer"),N("die Ampel"),N("die Papiertüte"),N("das Kleid")],
 question="Was macht die Frau?",answer="Sie kauft ein und präsentiert ihre Einkäufe.".split(),answerVoice=F,
 recall=[R("taps","stolz ihre Einkaufstüten",("hochhalten","hochheben")),R("taps","an",("Schaufenstern",),"vorbeischlendern"),R("taps","mit der",("Rolltreppe",),"hochfahren"),R("answer",("kauft",),"ein und präsentiert ihre Einkäufe")],
 notes="All three English tap boxes cover the woman for the whole clip (only person): phrase 1 = street scene (she holds both bags up), phrase 2 = shopping centre, phrase 3 = escalator. Answer avoids 'stolz' so the chips have one word order. Answer gap = the key word's verb 'kauft' (separable 'ein' stays visible)."),
54:dict(level="B",keyWord="der Geldautomat",
 taps=[T("ihre PIN eingeben","die Frau"),T("das Bargeld auszahlen","der Geldautomat"),T("die Geldscheine zählen","die Frau")],
 nouns=[N("die Lampe"),N("der Geldautomat"),N("die Geldscheine"),N("der Mantel")],
 question="Was macht die Frau?",answer="Sie hebt Bargeld am Geldautomaten ab.".split(),answerVoice=F,
 recall=[R("taps","ihre PIN",("eingeben","eintippen")),R("taps","das",("Bargeld","Geld"),"auszahlen"),R("taps","die Geldscheine",("zählen",)),R("answer","hebt Bargeld am",("Geldautomaten","Automaten"),"ab")],
 notes="Phrase 2 uses 'auszahlen', not 'ausgeben': 'das Bargeld ausgeben' would also read as 'spend the cash', which the woman does (she buys flowers). Phrase 1/3 boxes cover the woman for most of the clip; she types the PIN early and holds/fans the notes in the middle. German also allows 'Sie hebt am Geldautomaten Bargeld ab.' (two orders). No noun row: Geldautomat is in the answer row."),
}
for mid,d in files.items():
    o={"mediaId":mid,"lang":"de",**{k:d[k] for k in ["level","keyWord","taps","nouns","question","answer","answerVoice"]},"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(o,open(f"content/de/{mid}.json","w"),ensure_ascii=False,indent=2)
