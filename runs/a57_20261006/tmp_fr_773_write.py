import json
def T(p,t,v):return {"phrase":p,"target":t,"voice":v}
def N(w,v):return {"word":w,"voice":v}
def R(src,*parts):
    out=[]
    for p in parts:
        if isinstance(p,tuple): out.append({"text":p[0],"gap":True,"accept":list(p[1])})
        else: out.append({"text":p})
    return {"from":src,"parts":out}
D={}
D[773]=dict(level="B",keyWord="le thermomètre",
 taps=[T("prendre sa température","l'infirmière","female"),T("devenir écarlate","l'homme","male"),T("indiquer une température élevée","le thermomètre","female")],
 nouns=[N("la fenêtre","female"),N("le thermomètre","female"),N("l'infirmière","female"),N("le bol","female")],
 question="Que fait l'infirmière ?",answer="Elle prend sa température avec un thermomètre.".split(),answerVoice="female",
 recall=[R("taps",("prendre",["prendre","mesurer"]),"sa température"),R("taps","devenir",("écarlate",["écarlate","rouge"])),
   R("taps",("indiquer",["indiquer","afficher"]),"une température élevée"),R("answer","prend sa température avec un",("thermomètre",["thermomètre"]))],
 notes="'devenir écarlate' (B2) for 'turn bright red'; the man is red only in part of his boxed frames (he is red in the middle of the clip, normal at start and after the ice). 'sa température' = his temperature (the man's). Key word 'thermomètre' gapped in the answer row, so no noun row.")
D[4755]=dict(level="B",keyWord="la fracture",
 taps=[T("montrer la radiographie du doigt","la médecin","female"),T("grimacer de douleur","le jeune homme","male"),T("révéler une fracture","la radiographie","male")],
 nouns=[N("la radiographie","male"),N("la médecin","female"),N("le plâtre","male"),N("l'écharpe","male")],
 question="Que montre la médecin ?",answer="Elle montre une fracture sur la radiographie.".split(),answerVoice="female",
 recall=[R("taps","montrer la",("radiographie",["radiographie","radio"]),"du doigt"),R("taps",("grimacer",["grimacer"]),"de douleur"),
   R("taps","révéler une",("fracture",["fracture"])),R("answer",("montre",["montre","désigne"]),"une fracture sur la radiographie")],
 notes="Doctor is a woman: 'la médecin' (current standard French; 'la docteure' also possible). Sling = 'l'écharpe' (medical term, 'le bras en écharpe'). In the late boxed frames of phrase 2 the young man looks down with a pained face rather than an explicit wince; phrase fits most frames.")
D[95]=dict(level="B",keyWord="le fard à joues",
 taps=[T("appliquer du fard à joues","la fille à la tresse","female"),T("jeter un œil par-dessus son épaule","la fille aux cheveux courts","female"),T("être perché sur une cage","l'oiseau","female")],
 nouns=[N("la tresse","female"),N("le pinceau","female"),N("le fard à joues","female")],
 question="Que fait la fille en vert ?",answer="Elle applique du fard à joues avec un pinceau.".split(),answerVoice="female",
 recall=[R("taps",("appliquer",["appliquer","mettre"]),"du fard à joues"),R("taps","jeter un œil par-dessus son",("épaule",["épaule"])),
   R("taps","être",("perché",["perché"]),"sur une cage"),R("answer","applique du",("fard à joues",["fard à joues","blush"]),"avec un pinceau")],
 notes="Key word 'le fard à joues' kept; in France 'le blush' is at least as common in everyday speech (accepted in the answer row). The bird in the small blue box at the top is barely visible in the frames; phrase 3 follows the English target. Gap of the answer row is the multi-word key word 'fard à joues'.")
D[137]=dict(level="B",keyWord="le canyon",
 taps=[T("toucher la paroi du canyon","la femme","female"),T("crier les mains en porte-voix","l'homme","male"),T("briller entre les parois rocheuses","le soleil","male")],
 nouns=[N("le ciel","male"),N("le soleil","male"),N("le canyon","male"),N("la femme","female")],
 question="Que fait l'homme ?",answer="Il crie en faisant porte-voix avec ses mains.".split(),answerVoice="male",
 recall=[R("taps","toucher la paroi du",("canyon",["canyon"])),R("taps","crier les mains en",("porte-voix",["porte-voix"])),
   R("taps",("briller",["briller"]),"entre les parois rocheuses"),R("answer",("crie",["crie","hurle"]),"en faisant porte-voix avec ses mains")],
 notes="In the first boxed frames the woman is walking through the canyon, she touches the wall in most of the later boxed frames. The man only cups his hands in the second half; phrase 2 kept as English.")
D[354]=dict(level="B",keyWord="le guide touristique",
 taps=[T("feuilleter un guide touristique","la femme","female"),T("porter un casque colonial","l'homme","male"),T("cracher de l'eau","le lion de pierre","female")],
 nouns=[N("la statue","female"),N("le casque colonial","female"),N("la boucle d'oreille","female"),N("le guide touristique","female")],
 question="Que font les deux touristes ?",answer="Ils feuillettent un guide touristique.".split(),answerVoice="female",
 recall=[R("taps",("feuilleter",["feuilleter"]),"un guide touristique"),R("taps","porter un",("casque",["casque","chapeau"]),"colonial"),
   R("taps",("cracher",["cracher"]),"de l'eau"),R("answer","feuillettent un",("guide",["guide"]),"touristique")],
 notes="English 'sun hat' is a pith helmet in the clip: French 'le casque colonial' (the usual name; 'chapeau de soleil' is not idiomatic), accepted 'chapeau' in the recall row. Answer subject 'Ils' = the woman and the man; voice kept female as in English.")
for i,d in D.items():
    o={"mediaId":i,"lang":"fr",**{k:d[k] for k in ["level","keyWord","taps","nouns","question","answer","answerVoice"]},"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(o,open(f"content/fr/{i}.json","w"),ensure_ascii=False,indent=1)
