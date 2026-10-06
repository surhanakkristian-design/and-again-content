import json
def T(p,t,v): return {"phrase":p,"target":t,"voice":v}
def N(w,v): return {"word":w,"voice":v}
def R(src,parts,gap):
    out=[]
    for i,p in enumerate(parts):
        if i==gap: out.append({"text":p,"gap":True,"accept":[p]})
        else: out.append({"text":p})
    return {"from":src,"parts":out}
D={}
D[540]=dict(level="B",keyWord="le penalty",
 taps=[T("accorder un penalty","l'arbitre","male"),T("tirer un penalty","l'attaquante","female"),T("plonger vers le ballon","la gardienne","female")],
 nouns=[N("les palmiers","female"),N("le but","female"),N("la gardienne","female"),N("le ballon","female")],
 question="Que fait l'attaquante ?",answer=["Elle","tire","un","penalty."],answerVoice="female",
 recall=[R("taps",["accorder un","penalty"],1),R("taps",["tirer","un penalty"],0),R("taps",["plonger","vers le ballon"],0),R("answer",["tire un","penalty"],1)],
 notes="Goalkeeper follows the English female voice: 'la gardienne' (tap target and noun 3). The keeper dives but does not reach the ball, so phrase 3 is 'plonger vers le ballon' (not 'arrêter'). Box 2 also covers placing the ball and the run-up; 'tirer un penalty' describes the action of the box as a whole. Gaps: row 1 and the answer row gap the key word 'penalty', row 2 gaps 'tirer' so no two rows look the same blanked.")
D[105]=dict(level="B",keyWord="un arc",
 taps=[T("tendre la corde de l'arc","la femme","female"),T("remettre une flèche","l'homme","male"),T("viser la cible","la femme","female")],
 nouns=[N("l'arc","female"),N("la flèche","female"),N("la tresse","female"),N("la tunique","female")],
 question="Que fait la femme ?",answer=["Elle","vise","le","centre","de","la","cible."],answerVoice="female",
 recall=[R("taps",["tendre la","corde","de l'arc"],1),R("taps",["remettre une","flèche"],1),R("taps",["viser","la cible"],0),R("answer",["vise le","centre","de la cible"],1)],
 notes="keyWord copied unchanged as 'un arc' (indefinite article in the source; the noun pill uses 'l'arc'). The key word only appears elided ('l'arc'), so no row can gap it; no extra noun row because tap row 1 contains it. Answer 'vise le centre de la cible': she hits dead centre in the clip.")
D[18]=dict(level="B",keyWord="la racine",
 taps=[T("être à genoux dans la terre","la fille","female"),T("avoir de longues racines pâles","le jeune plant","female"),T("avoir un long bec","l'arrosoir","female")],
 nouns=[N("les racines","female"),N("les feuilles","female"),N("l'arrosoir","female"),N("le mur en pierre","female")],
 question="Que fait la fille ?",answer=["Elle","soulève","un","jeune","plant","aux","longues","racines."],answerVoice="female",
 recall=[R("taps",["être à","genoux","dans la terre"],1),R("taps",["avoir de longues","racines","pâles"],1),R("taps",["avoir un long","bec"],1),R("answer",["soulève","un jeune plant aux longues racines"],0)],
 notes="'le bec' = the spout of the watering can (bec verseur). The watering can is only partly visible at the frame edge in early boxes. No noun row: tap row 2 contains the key word 'racines'.")
D[737]=dict(level="B",keyWord="le beau-père",
 taps=[T("serrer un boulon","l'homme","male"),T("se jeter dans ses bras","le garçon","male"),T("observer depuis le seuil","la femme","female")],
 nouns=[N("les lunettes","male"),N("la roue","male"),N("la selle","male"),N("la pédale","male")],
 question="Que fait l'homme ?",answer=["Il","serre","un","boulon","de","la","roue."],answerVoice="male",
 recall=[R("taps",["serrer","un boulon"],0),R("taps",["se","jeter","dans ses bras"],1),R("taps",["observer","depuis le seuil"],0),R("answer",["serre un","boulon","de la roue"],1)],
 notes="Key word note: French 'le beau-père' means both stepfather and father-in-law; the clip context (wife's son) makes stepfather clear, but the owner may want 'le beau-père (conjoint de la mère)' disambiguated elsewhere. Box 2 also covers the pancake scene, where the boy cooks rather than jumps; the phrase describes the hug at the end. Row 3 accepts only 'observer'.")
D[5325]=dict(level="B",keyWord="un époux",
 taps=[T("porter un sac de courses","la femme","female"),T("tenir ses clés de voiture","l'homme","male"),T("montrer un document du doigt","la femme","female")],
 nouns=[N("les placards","male"),N("le frigo","male"),N("les documents","male"),N("le plan de travail","male")],
 question="Que font les époux ?",answer=["Ils","signent","des","documents","sur","le","plan","de","travail."],answerVoice="male",
 recall=[R("taps",["porter un","sac","de courses"],1),R("taps",["tenir ses","clés","de voiture"],1),R("taps",["montrer","un document du doigt"],0),R("answer",["signent","des documents sur le plan de travail"],0)],
 notes="keyWord copied unchanged as 'un époux' (indefinite article in source); the question uses 'les époux' for the couple. 'Tenir ses clés de voiture' replaces 'clutch': he holds the keys in the hallway frames; the keys are small and only visible in the first boxed frames. 'le frigo' is the everyday French word.")
for i,d in D.items():
    o={"mediaId":i,"lang":"fr",**{k:d[k] for k in ["level","keyWord","taps","nouns","question","answer","answerVoice"]},"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(o,open(f"content/fr/{i}.json","w"),ensure_ascii=False,indent=2)
