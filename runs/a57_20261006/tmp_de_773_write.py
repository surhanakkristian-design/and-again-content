import json
def G(t,acc=None): return {"text":t,"gap":True,"accept":acc or [t]}
def P(t): return {"text":t}
def T(p,t,v): return {"phrase":p,"target":t,"voice":v}
def N(w,v): return {"word":w,"voice":v}
D={}
D[773]=dict(level="B",keyWord="das Thermometer",
 taps=[T("Fieber messen","die Krankenschwester","female"),T("knallrot anlaufen","der Mann","male"),T("eine hohe Temperatur anzeigen","das Thermometer","female")],
 nouns=[N("das Fenster","female"),N("das Thermometer","female"),N("die Krankenschwester","female"),N("die Schüssel","female")],
 question="Was macht die Krankenschwester?",answer="Sie misst mit dem Thermometer Fieber.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":[G("Fieber"),P("messen")]},
         {"from":"taps","parts":[P("knallrot"),G("anlaufen",["anlaufen","werden"])]},
         {"from":"taps","parts":[P("eine hohe"),G("Temperatur",["Temperatur"]),P("anzeigen")]},
         {"from":"answer","parts":[P("misst mit dem"),G("Thermometer"),P("Fieber")]}],
 notes="Answer: 'Sie misst Fieber mit dem Thermometer.' is a second possible chip order. Window: several windows visible, English singular kept.")
D[4755]=dict(level="B",keyWord="der Knochenbruch",
 taps=[T("auf das Röntgenbild zeigen","die Ärztin","female"),T("vor Schmerz das Gesicht verziehen","der Mann","male"),T("einen Knochenbruch erkennen lassen","das Röntgenbild","male")],
 nouns=[N("das Röntgenbild","male"),N("die Ärztin","female"),N("der Gips","male"),N("die Armschlinge","male")],
 question="Worauf zeigt die Ärztin?",answer="Sie zeigt auf einen Knochenbruch im Röntgenbild.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":[P("auf das"),G("Röntgenbild"),P("zeigen")]},
         {"from":"taps","parts":[P("vor Schmerz das Gesicht"),G("verziehen")]},
         {"from":"taps","parts":[P("einen"),G("Knochenbruch",["Knochenbruch","Bruch"]),P("erkennen lassen")]},
         {"from":"answer","parts":[G("zeigt",["zeigt","deutet"]),P("auf einen Knochenbruch"),P("im Röntgenbild")]}],
 notes="Answer: 'Sie zeigt im Röntgenbild auf einen Knochenbruch.' is a second possible chip order.")
D[95]=dict(level="B",keyWord="das Rouge",
 taps=[T("Rouge auftragen","das Mädchen mit dem Zopf","female"),T("ihr über die Schulter schauen","das Mädchen mit den kurzen Haaren","female"),T("auf einem Käfig hocken","der Vogel","female")],
 nouns=[N("der Zopf","female"),N("der Pinsel","female"),N("das Rouge","female")],
 question="Was macht das Mädchen in Grün?",answer="Sie trägt mit einem Pinsel Rouge auf.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":[G("Rouge"),P("auftragen")]},
         {"from":"taps","parts":[P("ihr über die"),G("Schulter"),P("schauen")]},
         {"from":"taps","parts":[P("auf einem Käfig"),G("hocken",["hocken","sitzen"])]},
         {"from":"answer","parts":[P("trägt mit einem"),G("Pinsel"),P("Rouge auf")]}],
 notes="'Sie' for das Mädchen (what natives say). Answer: 'Sie trägt Rouge mit einem Pinsel auf.' is a second possible chip order. The bird is tiny at the top edge.")
D[137]=dict(level="B",keyWord="die Schlucht",
 taps=[T("die Felswand der Schlucht berühren","die Frau","female"),T("durch die hohlen Hände rufen","der Mann","male"),T("zwischen den Felsen hindurchscheinen","die Sonne","male")],
 nouns=[N("der Himmel","male"),N("die Sonne","male"),N("die Schlucht","male"),N("die Frau","female")],
 question="Was macht der Mann?",answer="Er ruft durch die hohlen Hände.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":[P("die Felswand der"),G("Schlucht"),P("berühren")]},
         {"from":"taps","parts":[P("durch die hohlen Hände"),G("rufen",["rufen","schreien"])]},
         {"from":"taps","parts":[P("zwischen den"),G("Felsen"),P("hindurchscheinen")]},
         {"from":"answer","parts":[P("ruft durch die hohlen"),G("Hände")]}],
 notes="")
D[354]=dict(level="B",keyWord="der Reiseführer",
 taps=[T("in einem Reiseführer blättern","die Frau","female"),T("einen Sonnenhut tragen","der Mann","male"),T("Wasser speien","der steinerne Löwe","female")],
 nouns=[N("die Statue","female"),N("der Sonnenhut","female"),N("der Ohrring","female"),N("der Reiseführer","female")],
 question="Was machen die beiden Touristen?",answer="Sie blättern in einem Reiseführer.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":[P("in einem"),G("Reiseführer"),P("blättern")]},
         {"from":"taps","parts":[P("einen"),G("Sonnenhut",["Sonnenhut","Hut"]),P("tragen")]},
         {"from":"taps","parts":[P("Wasser"),G("speien",["speien","spucken"])]},
         {"from":"answer","parts":[G("blättern"),P("in einem Reiseführer")]}],
 notes="The man's hat looks like a safari/pith helmet (Tropenhelm); 'Sonnenhut' kept as the plain word matching English. The man also touches the book in some frames.")
for vid,d in D.items():
    out={"mediaId":vid,"lang":"de",**{k:d[k] for k in ("level","keyWord","taps","nouns","question","answer","answerVoice")},"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(out,open(f'content/de/{vid}.json','w'),ensure_ascii=False,indent=1)
