import json
def T(p,t,v): return {"phrase":p,"target":t,"voice":v}
def N(w,v): return {"word":w,"voice":v}
def R(frm,*parts):
    out=[]
    for p in parts:
        if isinstance(p,tuple): out.append({"text":p[0],"gap":True,"accept":list(p[1])})
        else: out.append({"text":p})
    return {"from":frm,"parts":out}
D={}
D[21]=dict(keyWord="die Schule",
 taps=[T("die Tür öffnen","die Hand","male"),T("an den Tischen sitzen","die Schüler","male"),T("viele Fenster haben","das Schulgebäude","male")],
 nouns=[N("der Himmel","male"),N("die Schule","male"),N("das Gras","male")],
 question="Was machen die Schüler?",answer="Sie sitzen an den Tischen.".split(),answerVoice="male",
 recall=[R("taps","die Tür",("öffnen",["öffnen","aufmachen"])),R("taps","an den",("Tischen",["Tischen"]),"sitzen"),
  R("taps","viele",("Fenster",["Fenster"]),"haben"),R("nouns","die",("Schule",["Schule"])),
  R("answer",("sitzen",["sitzen"]),"an den Tischen")],
 notes="Target 3 'das Schulgebäude' (compound with the key word, verifier only). Noun row 'die Schule' added: no tap/answer row contains the key word. 'die Schüler' as generic masculine for the mixed group.")
D[22]=dict(keyWord="der Wissenschaftler",
 taps=[T("am Poster vorbeigehen","der Student","male"),T("ein paar Notizen schreiben","der Wissenschaftler","male"),T("auf eine Linie zeigen","der Wissenschaftler","male")],
 nouns=[N("der Wissenschaftler","male"),N("die Brille","male"),N("der Stift","male"),N("das Poster","male")],
 question="Was macht der Wissenschaftler?",answer="Der Wissenschaftler schreibt ein paar Notizen.".split(),answerVoice="male",
 recall=[R("taps","am Poster",("vorbeigehen",["vorbeigehen","vorbeilaufen"])),R("taps","ein paar",("Notizen",["Notizen"]),"schreiben"),
  R("taps","auf eine Linie",("zeigen",["zeigen"])),R("nouns","der",("Wissenschaftler",["Wissenschaftler"])),
  R("answer",("schreibt",["schreibt","macht"]),"ein paar Notizen")],
 notes="'die Brille' for the safety glasses on his forehead (level A; 'die Schutzbrille' would be more precise). Noun row added: answer row without its subject no longer contains the key word.")
D[23]=dict(keyWord="die Rede",
 taps=[T("eine Rede halten","die Frau in Grün","female"),T("etwas Wasser trinken","die Frau in Grün","female"),T("einen grauen Anzug tragen","der Mann in Grau","male")],
 nouns=[N("die Fenster","female"),N("die Frau","female"),N("das Mikrofon","female"),N("das Glas","female")],
 question="Was macht die Frau in Grün?",answer="Sie hält eine Rede.".split(),answerVoice="female",
 recall=[R("taps","eine",("Rede",["Rede"]),"halten"),R("taps","etwas Wasser",("trinken",["trinken"])),
  R("taps","einen grauen",("Anzug",["Anzug"]),"tragen"),R("answer",("hält",["hält"]),"eine Rede")],
 notes="Key word in tap row 1, so no noun row.")
D[24]=dict(keyWord="der Löffel",
 taps=[T("eine Schublade öffnen","das Mädchen","female"),T("einen Löffel nehmen","das Mädchen","female"),T("Suppe essen","das Mädchen","female")],
 nouns=[N("das Fenster","female"),N("der Löffel","female"),N("die Schüssel","female"),N("der Tisch","female")],
 question="Was macht das Mädchen?",answer="Sie isst Suppe mit einem Löffel.".split(),answerVoice="female",
 recall=[R("taps","eine",("Schublade",["Schublade"]),"öffnen"),R("taps","einen",("Löffel",["Löffel"]),"nehmen"),
  R("taps","Suppe",("essen",["essen"])),R("answer","isst",("Suppe",["Suppe"]),"mit einem Löffel")],
 notes="Pronoun 'Sie' for das Mädchen (what natives say). German also allows 'Sie isst mit einem Löffel Suppe' as a second chip order. Key word in tap row 2, so no noun row.")
D[25]=dict(keyWord="der Tacker",
 taps=[T("einen roten Tacker benutzen","der Mann","male"),T("das Papier hochheben","der Mann","male"),T("den Tacker öffnen","der Mann","male")],
 nouns=[N("der Mann","male"),N("die Pflanze","male"),N("der Tacker","male"),N("das Papier","male")],
 question="Was macht der Mann?",answer="Er benutzt einen roten Tacker.".split(),answerVoice="male",
 recall=[R("taps","einen roten",("Tacker",["Tacker","Hefter"]),"benutzen"),R("taps","das Papier",("hochheben",["hochheben","hochhalten","heben"])),
  R("taps","den Tacker",("öffnen",["öffnen","aufmachen"])),R("answer",("benutzt",["benutzt"]),"einen roten Tacker")],
 notes="'der Tacker' is the everyday word in Germany ('der Hefter' also accepted in the recall). Key word in tap rows, so no noun row.")
for i,d in D.items():
    o={"mediaId":i,"lang":"de","level":"A"}; o.update(d); o["carousel"]=[]
    o={k:o[k] for k in ["mediaId","lang","level","keyWord","taps","nouns","question","answer","answerVoice","carousel","recall","notes"]}
    json.dump(o,open(f"content/de/{i}.json","w"),ensure_ascii=False,indent=2)
