import json
def R(frm,*parts):
    ps=[]
    for p in parts:
        if isinstance(p,tuple): ps.append({"text":p[0],"gap":True,"accept":list(p[1:]) if len(p)>1 else [p[0]]})
        else: ps.append({"text":p})
    for p in ps:
        if p.get("gap") and p["accept"][0]!=p["text"]: p["accept"].insert(0,p["text"])
    return {"from":frm,"parts":ps}
def T(p,t,v): return {"phrase":p,"target":t,"voice":v}
def N(w,v): return {"word":w,"voice":v}
D={}
D[198]=dict(level="B",keyWord="la crampe",
 taps=[T("avoir une crampe au mollet","la femme","female"),T("s'agenouiller sur la piste","l'homme","male"),T("lever le pouce","la femme","female")],
 nouns=[N("la femme","female"),N("l'homme","male"),N("les gratte-ciel","female"),N("la piste d'athlétisme","female")],
 question="Qu'est-ce que la femme agrippe ?",answer="Elle agrippe son mollet douloureux.".split(),answerVoice="female",
 recall=[R("taps","avoir une",("crampe",),"au mollet"),R("taps","s'agenouiller sur la",("piste",)),R("taps","lever le",("pouce",)),
         R("answer",("agrippe","serre","tient"),"son mollet","douloureux")],
 notes="Phrase 1 uses the key word (avoir une crampe au mollet) instead of a translation of 'clutch her aching calf'; the clutching is in the answer (agripper, douloureux = B1/B2). Phrase 3 'lever le pouce' is a fixed collocation with no B1/B2 word; no natural B-level alternative for a thumbs up. Phrase 1 boxes also include the running frames before the cramp.")
D[199]=dict(level="A",keyWord="s'écraser",
 taps=[T("conduire une voiture rouge","l'homme","male"),T("lever les deux bras","l'homme","male"),T("porter un t-shirt jaune","l'homme","male")],
 nouns=[N("l'homme","male"),N("la voiture rouge","male"),N("la voiture jaune","male")],
 question="Que conduit l'homme ?",answer="Il conduit une voiture rouge.".split(),answerVoice="male",
 recall=[R("taps",("conduire",),"une voiture rouge"),R("taps","lever les deux",("bras",)),R("taps","porter un",("t-shirt","tee-shirt"),"jaune"),
         R("answer","conduit une",("voiture",),"rouge")],
 notes="Key word: 's'écraser' means a violent crash (plane, car wreck); bumping bumper cars is 'se rentrer dedans' / 'percuter' in French. Proposal: 'rentrer dans' or 'percuter' for this clip (owner decides). The cars are bumper cars (autos tamponneuses); kept 'voiture' as level A word. Shirt is a t-shirt.")
D[200]=dict(level="A",keyWord="la crème",
 taps=[T("mélanger la crème","l'homme","male"),T("manger une gaufre","l'homme","male"),T("porter un foulard","la femme","female")],
 nouns=[N("la crème","male"),N("la gaufre","male"),N("l'assiette","male")],
 question="Que fait l'homme ?",answer="Il mélange la crème dans un bol.".split(),answerVoice="male",
 recall=[R("taps","mélanger la",("crème",)),R("taps","manger une",("gaufre",)),R("taps","porter un",("foulard",)),
         R("answer",("mélange","bat","fouette"),"la crème","dans un bol")],
 notes="Natives say 'fouetter / monter la crème' for whisking (B1); kept A-level 'mélanger'. English 'cover her hair' rendered as 'porter un foulard' (she wears a headscarf). Phrase 1 boxes include the first frames where the woman pours.")
D[201]=dict(level="A",keyWord="le crocodile",
 taps=[T("nager dans la rivière","le crocodile","male"),T("sortir de l'eau","le crocodile","male"),T("ouvrir grand la gueule","le crocodile","male")],
 nouns=[N("le crocodile","male"),N("les arbres","male"),N("la rivière","male")],
 question="Que fait le crocodile ?",answer="Il ouvre grand la gueule.".split(),answerVoice="male",
 recall=[R("taps","nager dans la",("rivière",)),R("taps",("sortir",),"de l'eau"),R("taps","ouvrir grand la",("gueule",)),
         R("nouns","le",("crocodile",)),R("answer",("ouvre",),"grand la gueule")],
 notes="'la gueule' (animal mouth) is the natural word for a crocodile, slightly above A2; 'la bouche' would be wrong for an animal.")
D[202]=dict(level="A",keyWord="traverser",
 taps=[T("traverser la rue","l'homme","male"),T("regarder son téléphone","l'homme","male"),T("lever le pouce","l'homme","male")],
 nouns=[N("l'homme","male"),N("la voiture","male"),N("les immeubles","male"),N("la rue","male")],
 question="Que fait l'homme ?",answer="Il traverse la rue.".split(),answerVoice="male",
 recall=[R("taps",("traverser",),"la rue"),R("taps","regarder son",("téléphone","portable")),R("taps","lever le",("pouce",)),
         R("answer","traverse la",("rue",))],
 notes="")
for i,d in D.items():
    out={"mediaId":i,"lang":"fr","level":d["level"],"keyWord":d["keyWord"],"taps":d["taps"],"nouns":d["nouns"],"question":d["question"],
         "answer":d["answer"],"answerVoice":d["answerVoice"],"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(out,open(f"content/fr/{i}.json","w"),ensure_ascii=False,indent=1)
