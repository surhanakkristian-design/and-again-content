import json
def T(p,t,v): return {"phrase":p,"target":t,"voice":v}
def N(w,v): return {"word":w,"voice":v}
def R(frm,parts,gi,acc):
    ps=[{"text":x} for x in parts]; ps[gi]["gap"]=True; ps[gi]["accept"]=acc
    return {"from":frm,"parts":ps}
def A(s): return s.split()
D={}
m="male";f="female"
D[47]=dict(level="B",keyWord="die Arena",
 taps=[T("die Faust in die Luft recken","der Mann",m),T("sein Popcorn in die Luft werfen","der Junge",m),T("über dem Spielfeld hängen","die Anzeigetafel",m)],
 nouns=[N("die Anzeigetafel",m),N("die Zuschauer",m),N("das Spielfeld",m),N("das Popcorn",m)],
 question="Wo sind der Mann und der Junge?",answer=A("Sie sind in einer vollbesetzten Arena."),answerVoice=m,
 recall=[R("taps",["die","Faust","in die Luft recken"],1,["Faust"]),
         R("taps",["sein","Popcorn","in die Luft werfen"],1,["Popcorn"]),
         R("taps",["über dem","Spielfeld","hängen"],1,["Spielfeld"]),
         R("answer",["sind in einer","vollbesetzten","Arena"],2,["Arena","Halle"])],
 notes="Key word die Arena (not among the nouns) appears in the model answer and is gapped there. The boy also raises his arm in the last frames, but only the man clenches a fist.")
D[48]=dict(level="A",keyWord="ankommen",
 taps=[T("die Tür öffnen","der Mann",m),T("weiße Laken haben","das Bett",m),T("kleine weiße Wellen haben","das Meer",m)],
 nouns=[N("der Himmel",m),N("das Meer",m),N("der Sand",m),N("die Palmen",m)],
 question="Was macht der Mann?",answer=A("Er öffnet die Tür."),answerVoice=m,
 recall=[R("taps",["die Tür","öffnen"],1,["öffnen","aufmachen"]),
         R("taps",["weiße","Laken","haben"],1,["Laken"]),
         R("taps",["kleine weiße","Wellen","haben"],1,["Wellen"]),
         R("answer",["öffnet die","Tür"],1,["Tür"])],
 notes="English 'trees' are palm trees: 'die Palmen' is the natural German word (A2). Key word ankommen is shown by the whole clip but no exercise text uses it naturally.")
D[49]=dict(level="B",keyWord="der Pfeil",
 taps=[T("ihren Pfeil aus der Zielscheibe ziehen","die Frau",f),T("auf einem Gestell stehen","die Zielscheibe",f),T("hinter der Bogenschützin stehen","der Mann",m)],
 nouns=[N("der Himmel",f),N("der Pfeil",f),N("die Zielscheibe",f),N("das Gras",f)],
 question="Was hat der Pfeil getroffen?",answer=A("Der Pfeil hat die Mitte der Zielscheibe getroffen."),answerVoice=f,
 recall=[R("taps",["ihren","Pfeil","aus der Zielscheibe ziehen"],1,["Pfeil"]),
         R("taps",["auf einem","Gestell","stehen"],1,["Gestell","Ständer"]),
         R("taps",["hinter der","Bogenschützin","stehen"],1,["Bogenschützin"]),
         R("answer",["hat die Mitte der Zielscheibe","getroffen"],1,["getroffen"])],
 notes="Phrase 1 boxes also cover the frames where she holds the arrow up before shooting; written for the retrieval (pulling it out of the target) seen in the later boxed frames.")
D[50]=dict(level="A",keyWord="das Glas",
 taps=[T("den Spritzbeutel halten","die Hand",f),T("einen schwarzen Handschuh tragen","die Hand",f),T("sich mit Creme füllen","das Glas",f)],
 nouns=[N("der Handschuh",f),N("der Spritzbeutel",f),N("das Glas",f),N("der Tisch",f)],
 question="Was macht die Hand?",answer=A("Sie füllt ein Glas mit Creme."),answerVoice=f,
 recall=[R("taps",["den Spritzbeutel","halten"],1,["halten"]),
         R("taps",["einen schwarzen","Handschuh","tragen"],1,["Handschuh"]),
         R("taps",["sich mit","Creme","füllen"],1,["Creme"]),
         R("answer",["füllt ein","Glas","mit Creme"],1,["Glas"])],
 notes="'der Spritzbeutel' (piping bag) is above level A but is the only right word; 'die Tüte' would be wrong. The jars may be clear plastic; 'das Glas' still names a jar naturally in German. Answer word order: 'mit Creme' could also stand before 'ein Glas' only unnaturally, so one order.")
D[51]=dict(level="B",keyWord="zusammendrücken",
 taps=[T("den Schleim zusammendrücken","die Hand",m),T("eine Handvoll packen","die Hand",m),T("im Hintergrund stehen","die Tasse",m)],
 nouns=[N("die Tasse",m),N("der Daumen",m),N("das Handgelenk",m),N("die Perlen",m)],
 question="Was macht die Hand?",answer=A("Sie drückt eine Handvoll Perlen zusammen."),answerVoice=m,
 recall=[R("taps",["den Schleim","zusammendrücken"],1,["zusammendrücken","zusammenquetschen"]),
         R("taps",["eine","Handvoll","packen"],1,["Handvoll"]),
         R("taps",["im","Hintergrund","stehen"],1,["Hintergrund"]),
         R("answer",["drückt eine Handvoll","Perlen","zusammen"],1,["Perlen"])],
 notes="Mug with a handle = 'die Tasse' (more natural than 'der Becher'). Slime = 'der Schleim' (young speakers also say 'der Slime').")
for i,d in D.items():
    out={"mediaId":i,"lang":"de",**d,"carousel":[]}
    out={k:out[k] for k in ["mediaId","lang","level","keyWord","taps","nouns","question","answer","answerVoice","carousel","recall","notes"]}
    json.dump(out,open(f"content/de/{i}.json","w"),ensure_ascii=False,indent=1)
