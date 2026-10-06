import json
def T(p,t,v): return {"phrase":p,"target":t,"voice":v}
def N(w,v="female"): return {"word":w,"voice":v}
def R(src,*parts):
    out=[]
    for x in parts:
        if isinstance(x,tuple): out.append({"text":x[0],"gap":True,"accept":list(x[1])})
        else: out.append({"text":x})
    return {"from":src,"parts":out}
F="female"; M="male"
data={
8:dict(level="B",keyWord="la carte-clé",
 taps=[T("passer la carte-clé devant le lecteur","la femme",F),T("passer au vert","le lecteur de cartes",F),T("s'ouvrir sur la chambre","la porte",F)],
 nouns=[N("la porte"),N("le lecteur de cartes"),N("la carte-clé"),N("la poignée")],
 question="Que fait la femme ?",answer="Elle déverrouille la porte avec sa carte-clé.".split(),answerVoice=F,
 recall=[R("taps","passer la",("carte-clé",["carte-clé"]),"devant le lecteur"),
         R("taps",("passer",["passer"]),"au vert"),
         R("taps","s'ouvrir sur la",("chambre",["chambre"])),
         R("answer",("déverrouille",["déverrouille","ouvre"]),"la porte avec sa carte-clé")],
 notes="Phrase 1: the red box covers the walk with the suitcase only in the first two frames; in most boxed frames the woman holds the card to the reader, so 'passer la carte-clé devant le lecteur' instead of 'tirer sa valise'. Phrase 2 'passer au vert': the reader flashes red first, then turns green. Phrase 3: the door opens onto the lit room behind it. Noun 2 'le lecteur de cartes' (also 'le lecteur' in phrase 1). Answer: 'avec sa carte-clé' could also stand first ('Avec sa carte-clé, elle...'), but only with a comma, so one chip order."),
9:dict(level="B",keyWord="le laboratoire",
 taps=[T("enfiler des gants violets","la scientifique",F),T("examiner un petit tube","la scientifique",F),T("conserver les échantillons au froid","le congélateur",F)],
 nouns=[N("les lunettes de protection"),N("les tubes à essai"),N("la blouse"),N("le congélateur")],
 question="Que fait la scientifique ?",answer="Elle range des tubes à essai dans le congélateur.".split(),answerVoice=F,
 recall=[R("taps",("enfiler",["enfiler","mettre"]),"des gants violets"),
         R("taps","examiner un petit",("tube",["tube"])),
         R("taps","conserver les",("échantillons",["échantillons"]),"au froid"),
         R("answer",("range",["range","met","place"]),"des tubes à essai dans le congélateur")],
 notes="Key word 'le laboratoire' is the setting only; no noun of the set names it, so it appears in no text (same as English). Phrases 1 and 2 both have the scientist as target (as in English). 'la blouse' = lab coat (white coat visible). The green box (phrase 2) spans the whole frame in the opening frames where she puts on the coat."),
11:dict(level="A",keyWord="la bibliothèque",
 taps=[T("porter un grand sac","la femme",F),T("marcher entre les étagères","la femme",F),T("être grande et ronde","la tour de livres",F)],
 nouns=[N("les livres"),N("les cheveux"),N("le manteau"),N("le sac")],
 question="Que fait la femme ?",answer="Elle lève les yeux vers les livres.".split(),answerVoice=F,
 recall=[R("taps","porter un grand",("sac",["sac"])),
         R("taps",("marcher",["marcher"]),"entre les étagères"),
         R("taps","être grande et",("ronde",["ronde"])),
         R("answer","lève les yeux vers les",("livres",["livres"]))],
 notes="Phrase 2: the green box also covers the frames where she stands still and looks up at the tower; she walks between the shelves in the first half. Key word 'la bibliothèque' is the setting, not a noun of the set, so it appears in no text. 'la tour de livres' is the target name only."),
12:dict(level="A",keyWord="serrer dans ses bras",
 taps=[T("avoir les cheveux courts","l'homme",M),T("avoir les cheveux longs","la femme",F),T("briller dans le ciel","le soleil",F)],
 nouns=[N("le soleil"),N("l'homme",M),N("la femme"),N("l'herbe")],
 question="Que font l'homme et la femme ?",answer="Ils se serrent dans leurs bras.".split(),answerVoice=F,
 recall=[R("taps","avoir les",("cheveux",["cheveux"]),"courts"),
         R("taps","avoir les cheveux",("longs",["longs"])),
         R("taps",("briller",["briller"]),"dans le ciel"),
         R("answer","se",("serrent",["serrent"]),"dans leurs bras")],
 notes="Answer uses the key word 'serrer dans ses bras' (reciprocal: 'Ils se serrent dans leurs bras'); English 'in the grass' left out to avoid 'dans ... dans'. answerVoice kept female as in English ('Ils' = mixed couple)."),
14:dict(level="A",keyWord="la page",
 taps=[T("ouvrir un carnet","les mains",F),T("être jaune vif","la fleur",F),T("passer sur les feuilles vertes","le pinceau",F)],
 nouns=[N("la page"),N("la fleur"),N("le pinceau"),N("la table")],
 question="Qu'est-ce qu'il y a sur la page ?",answer="Il y a une fleur jaune sur la page.".split(),answerVoice=F,
 recall=[R("taps","ouvrir un",("carnet",["carnet","cahier"])),
         R("taps","être",("jaune",["jaune"]),"vif"),
         R("taps","passer sur les",("feuilles",["feuilles"]),"vertes"),
         R("answer","Il y a une fleur jaune sur la",("page",["page"]))],
 notes="Phrase 1: the red box also covers frames where the fingers press the leaves and hold the notebook up; most boxed frames show the hands opening and flattening the small notebook ('un carnet'). Phrase 3: the brush spreads glue over the leaves ('passer sur'). Answer 'Il y a ...' has only the impersonal 'il': the answer row keeps the whole sentence (as es), key word gapped there. Question 8 words incl. 'Qu'est-ce'."),
}
for i,d in data.items():
    out={"mediaId":i,"lang":"fr",**{k:d[k] for k in ("level","keyWord","taps","nouns","question","answer","answerVoice")},"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(out,open(f"content/fr/{i}.json","w"),ensure_ascii=False,indent=1)
