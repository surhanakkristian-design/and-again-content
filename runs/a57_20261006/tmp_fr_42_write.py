import json
def R(frm,text,gap,acc=()):
    w=text.split(' '); i=w.index(gap); parts=[]
    if i>0: parts.append({"text":' '.join(w[:i])})
    parts.append({"text":gap,"gap":True,"accept":[gap]+list(acc)})
    if i<len(w)-1: parts.append({"text":' '.join(w[i+1:])})
    return {"from":frm,"parts":parts}
def T(p,t,v): return {"phrase":p,"target":t,"voice":v}
def N(w,v): return {"word":w,"voice":v}
V={}
V[42]=dict(level="A",keyWord="un examen",
 taps=[T("regarder son examen","le jeune homme","male"),T("être posé sur les feuilles","le stylo","male"),T("recouvrir la table","les feuilles","male")],
 nouns=[N("la porte","male"),N("la chaise","male"),N("le mur","male"),N("les feuilles","male")],
 question="Que regarde le jeune homme ?",answer="Il regarde son examen.",answerVoice="male",
 recall=[R("taps","regarder son examen","examen"),R("taps","être posé sur les feuilles","feuilles",["papiers"]),R("taps","recouvrir la table","recouvrir",["couvrir"]),R("answer","regarde son examen","regarde")],
 notes="keyWord copied unchanged but it carries the indefinite article ('un examen'); proposal: 'l'examen' like the other languages' definite form. 'papers' -> 'les feuilles' (everyday word for loose sheets), 'papiers' accepted. Tap box 1 also covers frames where he walks to/away from the table; phrase written for the frames where he sits and looks at the papers. No noun row: 'examen' is not a noun of the set and is gapped in tap row 1.")
V[43]=dict(level="A",keyWord="tourner sur soi-même",
 taps=[T("tirer sur une ficelle","la main","male"),T("tourner sur soi-même très vite","la boule dorée","male"),T("tenir une boule dorée","la main","male")],
 nouns=[N("l'imprimante","male"),N("la boule","male"),N("le bureau","male")],
 question="Que fait la boule dorée ?",answer="Elle tourne très vite.",answerVoice="male",
 recall=[R("taps","tirer sur une ficelle","ficelle",["corde"]),R("taps","tourner sur soi-même très vite","tourner"),R("taps","tenir une boule dorée","tenir"),R("answer","tourne très vite","vite",["rapidement"])],
 notes="Strictly the ring spins around the golden ball; like the English, the whole gyroscope is called 'la boule dorée'. Tap box 1 also covers frames where the hand only places the gyroscope on the stand; phrase written for the string-pulling frames. Subject 'la boule' is feminine (pronoun 'elle'); answerVoice kept male as in English (thing, defaultVoice). Key word used in tap 2.")
V[44]=dict(level="B",keyWord="la colère",
 taps=[T("serrer les poings","la femme","female"),T("se prendre la tête à deux mains","la femme","female"),T("être éparpillées sur la table","les fleurs","female")],
 nouns=[N("les tresses","female"),N("le tablier","female"),N("le poing","female"),N("les fleurs","female")],
 question="Que fait la femme ?",answer="Elle serre les poings de colère.",answerVoice="female",
 recall=[R("taps","serrer les poings","poings"),R("taps","se prendre la tête à deux mains","tête"),R("taps","être éparpillées sur la table","éparpillées",["dispersées","étalées"]),R("answer","serre les poings de colère","colère",["rage"])],
 notes="Taps 1 and 2 share one box (same woman) as in English; the box also covers the bag-throw and kick frames - phrases written for the frames where she does them. Flowers lie on the market table. No noun row: 'la colère' is not a noun of the set and is gapped in the answer row.")
V[45]=dict(level="A",keyWord="en colère",
 taps=[T("crier sur l'homme","la femme","female"),T("être par terre","les vêtements","female"),T("porter une veste grise","l'homme","male")],
 nouns=[N("les bouteilles","female"),N("la machine à laver","female"),N("la femme","female"),N("les vêtements","female")],
 question="Que fait la femme en colère ?",answer="Elle crie très fort sur l'homme.",answerVoice="female",
 recall=[R("taps","crier sur l'homme","crier",["hurler"]),R("taps","être par terre","terre"),R("taps","porter une veste grise","veste",["gilet"]),R("answer","crie très fort sur l'homme","crie",["hurle"])],
 notes="The man's grey top looks like a zip jacket; 'veste' kept as in English, 'gilet' accepted. Tap box 1 also covers the opening frames where the woman walks in and picks up the clothes; phrase written for the shouting frames (most boxed frames). Key word 'en colère' (adjectival phrase) appears in the question only. 'très fort' added to the answer so its recall row differs from tap row 1 once blanked (the elided 'l'homme' cannot be the gap); 'Elle crie sur l'homme très fort' is a less natural second order.")
V[46]=dict(level="A",keyWord="la pomme",
 taps=[T("couper une pomme","la femme","female"),T("avoir une barbe noire","l'homme","male"),T("être posé sur une caisse","l'oiseau","female")],
 nouns=[N("l'homme","male"),N("la femme","female"),N("l'oiseau","female"),N("la pomme","female")],
 question="Que fait la femme ?",answer="Elle mange une pomme rouge.",answerVoice="female",
 recall=[R("taps","couper une pomme","couper",["trancher"]),R("taps","avoir une barbe noire","barbe"),R("taps","être posé sur une caisse","caisse"),R("answer","mange une pomme rouge","pomme")],
 notes="Tap box 1 covers the whole clip (picking, polishing, biting, then cutting on the stump); 'couper une pomme' kept as in English - only her hand holds the knife. The bird is a magpie ('une pie'); 'l'oiseau' kept as in English. No noun row: 'pomme' is already in tap row 1 and gapped in the answer row.")
for i,d in V.items():
    out={"mediaId":i,"lang":"fr","level":d["level"],"keyWord":d["keyWord"],"taps":d["taps"],"nouns":d["nouns"],
         "question":d["question"],"answer":d["answer"].split(' '),"answerVoice":d["answerVoice"],"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(out,open(f'content/fr/{i}.json','w'),ensure_ascii=False,indent=1)
