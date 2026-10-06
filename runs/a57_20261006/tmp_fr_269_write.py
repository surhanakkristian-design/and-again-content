import json
def T(p,t,v): return {"phrase":p,"target":t,"voice":v}
def N(w,v): return {"word":w,"voice":v}
def R(frm,*parts):
    out=[]
    for p in parts:
        if isinstance(p,tuple): out.append({"text":p[0],"gap":True,"accept":list(p[1])})
        else: out.append({"text":p})
    return {"from":frm,"parts":out}
F="female"; M="male"
D={}
D[269]=dict(level="B",keyWord="l'envie",
 taps=[T("regarder par la vitre avec envie","la femme",F),T("doubler le bus à vélo","la cycliste",F),T("reposer en travers de ses genoux","le guidon rouillé",F)],
 nouns=[N("la cycliste",F),N("les cheveux bouclés",F),N("le débardeur",F),N("le guidon",F)],
 question="Que fait la femme aux cheveux bouclés ?",
 answer=["Elle","fixe","la","cycliste","avec","envie."],answerVoice=F,
 recall=[R("taps","regarder par la vitre avec",("envie",["envie"])),
         R("taps",("doubler",["doubler","dépasser"]),"le bus à vélo"),
         R("taps","reposer en travers de ses",("genoux",["genoux"])),
         R("answer",("fixe",["fixe","regarde"]),"la cycliste avec envie")],
 notes="The cyclist is a woman in the clip -> 'la cycliste' (noun 1 and answer). 'avec envie' could also stand before 'la cycliste' ('Elle fixe avec envie la cycliste'), but the given order is the natural one. Key word 'l'envie' appears in tap 1 and the answer as 'avec envie'.")
D[270]=dict(level="A",keyWord="la gomme",
 taps=[T("sourire à la caméra","la fille",F),T("ressembler à une montagne","la gomme",F),T("montrer un soleil rouge","la boîte",F)],
 nouns=[N("la boîte",F),N("la main",F),N("la gomme",F),N("le papier",F)],
 question="À quoi ressemble la gomme ?",
 answer=["La","gomme","ressemble","à","une","petite","montagne."],answerVoice=F,
 recall=[R("taps",("sourire",["sourire"]),"à la caméra"),
         R("taps",("ressembler",["ressembler"]),"à une montagne"),
         R("taps","montrer un",("soleil",["soleil"]),"rouge"),
         R("nouns","la",("gomme",["gomme"])),
         R("answer","ressemble à une petite",("montagne",["montagne"]))],
 notes="")
D[272]=dict(level="B",keyWord="s'évaporer",
 taps=[T("incliner la poêle vide","la femme",F),T("s'évaporer de la poêle","l'eau",F),T("produire une flamme bleue","le réchaud",F)],
 nouns=[N("les lunettes de protection",F),N("la vapeur",F),N("la poêle",F),N("le réchaud",F)],
 question="Qu'arrive-t-il à l'eau ?",
 answer=["L'eau","s'évapore","de","la","poêle","chaude."],answerVoice=F,
 recall=[R("taps",("incliner",["incliner","pencher"]),"la poêle vide"),
         R("taps","s'évaporer de la",("poêle",["poêle"])),
         R("taps","produire une",("flamme",["flamme"]),"bleue"),
         R("answer","s'évapore de la poêle",("chaude",["chaude","brûlante"]))],
 notes="The key word 's'évaporer' is elided, so by the rule it is never a gap; it stands in tap 2 and the answer. 'le réchaud' used for the camping stove (everyday word; 'le réchaud de camping' also possible).")
D[273]=dict(level="A",keyWord="le soir",
 taps=[T("disparaître derrière les collines","le soleil",M),T("avoir les cheveux longs","la femme",F),T("porter un pull vert","l'homme",M)],
 nouns=[N("le ciel",M),N("le soleil",M),N("les maisons",M),N("la femme",F)],
 question="Que fait le soleil ?",
 answer=["Le","soleil","se","couche","derrière","les","collines."],answerVoice=M,
 recall=[R("taps","disparaître derrière les",("collines",["collines"])),
         R("taps","avoir les",("cheveux",["cheveux"]),"longs"),
         R("taps","porter un",("pull",["pull"]),"vert"),
         R("answer","se",("couche",["couche"]),"derrière les collines")],
 notes="Key word 'le soir' is not a thing in the noun set and appears in no exercise text (as in English). The sun is visible in the boxed frames before it sets; in the later frames it is gone.")
D[274]=dict(level="A",keyWord="tout le monde",
 taps=[T("lever une écharpe","l'homme à l'écharpe",M),T("être assis sur les épaules d'un homme","le garçon",M),T("éclairer le stade","les lumières",M)],
 nouns=[N("les lumières",M),N("le garçon",M),N("l'écharpe",M)],
 question="Que fait tout le monde ?",
 answer=["Tout","le","monde","crie","dans","le","stade."],answerVoice=M,
 recall=[R("taps","lever une",("écharpe",["écharpe"])),
         R("taps","être assis sur les",("épaules",["épaules"]),"d'un homme"),
         R("taps",("éclairer",["éclairer"]),"le stade"),
         R("answer",("crie",["crie","hurle"]),"dans le stade")],
 notes="Key word 'tout le monde' is a pronoun phrase: it is the question and answer subject, so it is not in any recall row. Tap 3 'éclairer le stade' instead of a literal 'briller depuis le toit' (unnatural).")
for i,d in D.items():
    o={"mediaId":i,"lang":"fr","level":d["level"],"keyWord":d["keyWord"],"taps":d["taps"],"nouns":d["nouns"],
       "question":d["question"],"answer":d["answer"],"answerVoice":d["answerVoice"],"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(o,open(f"content/fr/{i}.json","w"),ensure_ascii=False,indent=1)
