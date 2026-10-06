import json
def T(t): return {"text": t}
def G(t,*acc): return {"text": t, "gap": True, "accept": [t,*acc]}
def ans(s): return s.split(" ")
V = {}
V[7756] = dict(level="B", keyWord="automobil",
 taps=[("ein Vorderrad montieren","der Bär","female"),("einen Schraubenschlüssel umklammern","der Waschbär","female"),("auf einer Hebebühne stehen","der rote Sportwagen","female")],
 nouns=[("der Bär","female"),("der Waschbär","female"),("die Reifen","female"),("der Sportwagen","female")],
 question="Was macht der Bär?", answer="Er montiert ein Rad an den Sportwagen.", answerVoice="female",
 recall=[("taps",[T("ein"),G("Vorderrad","Rad"),T("montieren")]),
         ("taps",[T("einen Schraubenschlüssel"),G("umklammern","festhalten","halten")]),
         ("taps",[T("auf einer"),G("Hebebühne"),T("stehen")]),
         ("answer",[G("montiert","schraubt","befestigt"),T("ein Rad an den Sportwagen")])],
 notes="keyWord 'automobil' is an adjective that German hardly uses on its own (natives say 'Auto-'/'Kfz-' in compounds: die Autowerkstatt, die Kfz-Branche); nothing in the clip carries it, so it appears in no exercise. Proposal for the owner: 'die Autowerkstatt' or 'die Kfz-Werkstatt' as the German word for this clip. Bear box: in the last frames the bear has let go and stands back; 'ein Vorderrad montieren' describes most boxed frames. Answer: 'Er montiert an den Sportwagen ein Rad.' is also possible but marked; the given order is the natural one. Bear -> 'er' (der Bär); answerVoice female copied from English.")
V[733] = dict(level="B", keyWord="der Staat",
 taps=[("einen Messingstempel hochheben","die Frau mit der türkisfarbenen Schärpe","female"),("skeptisch auf das Dokument schauen","der grauhaarige Mann","male"),("mit einem weißen Kreis bedruckt sein","das türkisfarbene Banner","male")],
 nouns=[("der Kronleuchter","male"),("der Kreis","male"),("das Dreieck","male"),("der Marmorboden","male")],
 question="Was machen die beiden Staatsoberhäupter?", answer="Sie schütteln sich vor ihren Bannern die Hand.", answerVoice="male",
 recall=[("taps",[T("einen"),G("Messingstempel","Stempel"),T("hochheben")]),
         ("taps",[T("skeptisch auf das"),G("Dokument","Papier"),T("schauen")]),
         ("taps",[T("mit einem weißen"),G("Kreis"),T("bedruckt sein")]),
         ("answer",[G("schütteln"),T("sich vor ihren"),T("Bannern die Hand")])],
 notes="keyWord 'der Staat' names no visible thing (two state leaders sign a treaty); it appears only inside the compound 'die Staatsoberhäupter' in the question. No noun row: 'der Staat' is not one of the four nouns. Red and green boxes also cover the later handshake/standing frames; the phrases describe the stamping moment as in English (her stamp is brass, his has a dark wooden handle, so 'Messingstempel' fits only her; only he frowns at the document). 'Staatsoberhäupter' is gender-neutral (woman + man). Answer: 'Sie schütteln sich die Hand vor ihren Bannern.' is also possible German word order; 'geben sich ... die Hand' would be equally right, but the answer row gap 'schütteln' only fits with 'die Hand' wording kept, so accept only 'schütteln'. Banner = 'das Banner' throughout.")
V[788] = dict(level="B", keyWord="in der Mikrowelle erhitzen",
 taps=[("seine Nudeln in der Mikrowelle erhitzen","der Junge","male"),("den Jungen angrinsen","das Mädchen","female"),("innen aufleuchten","die Mikrowelle","male")],
 nouns=[("die Mikrowelle","male"),("die Nudeln","male"),("das Regal","male"),("der Kapuzenpullover","male")],
 question="Was macht der Junge?", answer="Er erhitzt eine Schüssel Nudeln in der Mikrowelle.", answerVoice="male",
 recall=[("taps",[T("seine Nudeln in der Mikrowelle"),G("erhitzen","erwärmen","aufwärmen")]),
         ("taps",[T("den Jungen"),G("angrinsen","anlächeln")]),
         ("taps",[T("innen"),G("aufleuchten","leuchten")]),
         ("answer",[T("erhitzt eine"),G("Schüssel","Schale"),T("Nudeln in der Mikrowelle")])],
 notes="Key word used in tap phrase 1 and the answer. No noun row (key word is a verb phrase). Answer: 'Er erhitzt in der Mikrowelle eine Schüssel Nudeln.' is also possible German word order. The girl appears only in the last two frames; she grins/smiles while pointing at the boy.")
V[4143] = dict(level="B", keyWord="die Tonne",
 taps=[("der Tonne entkommen wollen","der Waschbär","male"),("zerknüllt daliegen","der grüne Müllsack","male"),("im Hintergrund wachsen","die Büsche","male")],
 nouns=[("der Waschbär","male"),("der Müllsack","male"),("die Tonne","male"),("die Büsche","male")],
 question="Was versucht der Waschbär?", answer="Er versucht, aus der Tonne zu entkommen.", answerVoice="male",
 recall=[("taps",[T("der"),G("Tonne","Mülltonne"),T("entkommen wollen")]),
         ("taps",[T("zerknüllt"),G("daliegen","liegen")]),
         ("taps",[T("im"),G("Hintergrund"),T("wachsen")]),
         ("answer",[T("versucht, aus der Tonne zu"),G("entkommen","fliehen","klettern")])],
 notes="Raccoon box: in many frames the raccoon only sits or curls up and looks at the camera; the escape attempt (standing, paws up the wall, slipping back) is the clear action, as in English. 'der Tonne entkommen wollen' (dative) carries the key word; no noun row because 'Tonne' is already in tap row 1. Answer chip 'versucht,' carries the comma of the infinitive clause.")
V[6908] = dict(level="B", keyWord="der Bison",
 taps=[("ein Sandwich umklammern","die Frau","female"),("am Cabrio vorbeitrotten","der große Bison","female"),("auf dem Asphalt liegen","der Strohhut","female")],
 nouns=[("der Bison","female"),("der Strohhut","female"),("das Cabrio","female"),("die Berge","female")],
 question="Was macht der große Bison?", answer="Er trottet am Cabrio vorbei.", answerVoice="female",
 recall=[("taps",[T("ein Sandwich"),G("umklammern","festhalten","halten")]),
         ("taps",[T("am"),G("Cabrio","Auto"),T("vorbeitrotten")]),
         ("taps",[T("auf dem"),G("Asphalt"),T("liegen")]),
         ("nouns",[T("der"),G("Bison","Büffel")]),
         ("answer",[G("trottet","läuft","geht"),T("am Cabrio vorbei")])],
 notes="English 'buffalo' = the American bison; German 'der Bison' (keyWord) is the correct everyday word, 'Büffel' accepted in the noun row. The car is 'das Cabrio' in phrase, noun and answer (English used 'car' and 'convertible' for the same thing). The other bison cross the road behind but do not pass the car, so phrase 2 fits only the big one. Noun row added: 'Bison' appears in no other row. Bison -> 'er'; answerVoice female copied from English.")
for mid,d in V.items():
    out = {"mediaId": mid, "lang": "de", "level": d["level"], "keyWord": d["keyWord"],
      "taps":[{"phrase":p,"target":t,"voice":v} for p,t,v in d["taps"]],
      "nouns":[{"word":w,"voice":v} for w,v in d["nouns"]],
      "question": d["question"], "answer": ans(d["answer"]), "answerVoice": d["answerVoice"],
      "carousel": [], "recall":[{"from":f,"parts":p} for f,p in d["recall"]], "notes": d["notes"]}
    json.dump(out, open(f"content/de/{mid}.json","w"), ensure_ascii=False, indent=2)
