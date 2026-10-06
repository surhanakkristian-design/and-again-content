import json
def T(p,t,v): return {"phrase":p,"target":t,"voice":v}
def N(w,v): return {"word":w,"voice":v}
def P(t,gap=None):
    d={"text":t}
    if gap is not None: d["gap"]=True; d["accept"]=gap
    return d
F=[]
F.append({"mediaId":4190,"lang":"de","level":"A","keyWord":"sich treffen",
 "taps":[T("auf einer Mauer sitzen","die Katze","female"),T("eine dunkle Mähne haben","der Löwe","female"),T("orange und weiß sein","die Katze","female")],
 "nouns":[N("die Bäume","female"),N("der Löwe","female"),N("das Gras","female"),N("die Katze","female")],
 "question":"Was macht die Katze?","answer":["Sie","trifft","einen","großen","Löwen."],"answerVoice":"female","carousel":[],
 "recall":[
  {"from":"taps","parts":[P("auf einer"),P("Mauer",["Mauer"]),P("sitzen")]},
  {"from":"taps","parts":[P("eine dunkle"),P("Mähne",["Mähne"]),P("haben")]},
  {"from":"taps","parts":[P("orange und"),P("weiß",["weiß"]),P("sein")]},
  {"from":"answer","parts":[P("trifft",["trifft"]),P("einen großen Löwen")]}],
 "notes":"Key word 'sich treffen' (reflexive) means an arranged meeting (sich mit jemandem treffen); the clip shows a chance encounter, so the answer uses transitive 'jemanden treffen' ('Sie trifft einen großen Löwen.'). Proposal: key word 'treffen' or 'begegnen'. Tap 2: a lion's hair is 'die Mähne' (above A2, but 'Haare haben' is unnatural for a lion); only the male lion has one (the lioness has none). Tap 1: in some boxed frames the cat stands up with its paws on the bars; it sits in most."})
F.append({"mediaId":5652,"lang":"de","level":"A","keyWord":"groß",
 "taps":[T("am großen Ball riechen","der Hund","female"),T("der größere Ball sein","der große Ball","female"),T("der kleinere Ball sein","der kleine Ball","female")],
 "nouns":[N("die Bäume","female"),N("der Ball","female"),N("der Hund","female"),N("das Gras","female")],
 "question":"Was macht der Hund?","answer":["Er","riecht","an","einem","großen","Ball."],"answerVoice":"female","carousel":[],
 "recall":[
  {"from":"taps","parts":[P("am"),P("großen",["großen","riesigen"]),P("Ball riechen")]},
  {"from":"taps","parts":[P("der größere"),P("Ball",["Ball"]),P("sein")]},
  {"from":"taps","parts":[P("der"),P("kleinere",["kleinere"]),P("Ball sein")]},
  {"from":"answer","parts":[P("riecht",["riecht","schnuppert","schnüffelt"]),P("an einem großen Ball")]}],
 "notes":"Answer pronoun 'er' (der Hund); answerVoice kept female as in English. Tap rows 2/3 gap different words so they do not look the same once blanked. The dog also looks straight ahead at the end of the tap-1 box."})
F.append({"mediaId":26,"lang":"de","level":"A","keyWord":"der Strohhalm",
 "taps":[T("einen langen Strohhalm halten","der Mann","male"),T("Orangensaft trinken","der Mann","male"),T("auf der Theke stehen","das Glas","male")],
 "nouns":[N("die Sonnenbrille","male"),N("der Strohhalm","male"),N("das Glas","male"),N("das Hemd","male")],
 "question":"Was macht der Mann?","answer":["Er","trinkt","Saft","durch","einen","Strohhalm."],"answerVoice":"male","carousel":[],
 "recall":[
  {"from":"taps","parts":[P("einen langen"),P("Strohhalm",["Strohhalm"]),P("halten")]},
  {"from":"taps","parts":[P("Orangensaft"),P("trinken",["trinken"])]},
  {"from":"taps","parts":[P("auf der"),P("Theke",["Theke","Tresen","Bar"]),P("stehen")]},
  {"from":"answer","parts":[P("trinkt"),P("Saft",["Saft","Orangensaft"]),P("durch einen Strohhalm")]}],
 "notes":"Tap 3: in the last boxed frames the man holds the empty glass upside down in the air; in most boxed frames it stands on the bar counter (die Theke). Answer: German also allows 'Er trinkt durch einen Strohhalm Saft.' (less natural; second order possible). No noun row: Strohhalm is in tap row 1."})
F.append({"mediaId":324,"lang":"de","level":"A","keyWord":"das Gaming",
 "taps":[T("beide Arme hochheben","das Mädchen","female"),T("das Spiel gewinnen","das Mädchen","female"),T("eine rote Jacke tragen","der Junge","male")],
 "nouns":[N("das Mädchen","female"),N("die Jacke","female"),N("die Kartons","female"),N("das Sofa","female")],
 "question":"Wer gewinnt das Spiel?","answer":["Das","Mädchen","gewinnt","das","Spiel."],"answerVoice":"female","carousel":[],
 "recall":[
  {"from":"taps","parts":[P("beide"),P("Arme",["Arme","Hände","Fäuste"]),P("hochheben")]},
  {"from":"taps","parts":[P("das Spiel"),P("gewinnen",["gewinnen"])]},
  {"from":"taps","parts":[P("eine rote"),P("Jacke",["Jacke"]),P("tragen")]},
  {"from":"answer","parts":[P("gewinnt das"),P("Spiel",["Spiel"])]}],
 "notes":"Key word 'das Gaming' does not occur naturally in any exercise (a played video game is 'das Spiel'); not forced. Tap 1: she raises both arms (fists), 'Arme' is more natural than 'Hände'; the box also covers earlier frames where she is still playing. Answer: OVS 'Das Spiel gewinnt das Mädchen.' is grammatically possible with the same chips (marked)."})
F.append({"mediaId":612,"lang":"de","level":"A","keyWord":"rechts",
 "taps":[T("nach rechts zeigen","die Frau","female"),T("einen großen Rucksack tragen","der Mann","male"),T("zum Abschied winken","die Frau","female")],
 "nouns":[N("die Lichter","female"),N("die Frau","female"),N("das Essen","female"),N("das Rad","female")],
 "question":"Wohin zeigt die Frau?","answer":["Sie","zeigt","nach","rechts."],"answerVoice":"female","carousel":[],
 "recall":[
  {"from":"taps","parts":[P("nach"),P("rechts",["rechts"]),P("zeigen")]},
  {"from":"taps","parts":[P("einen großen"),P("Rucksack",["Rucksack"]),P("tragen")]},
  {"from":"taps","parts":[P("zum Abschied"),P("winken",["winken"])]},
  {"from":"answer","parts":[P("zeigt",["zeigt"]),P("nach rechts")]}],
 "notes":"Taps 1 and 3 share the same box (the woman); in many boxed frames she points, she waves only at the end. Tap 1's box also covers frames where she holds a cloth or turns the man around."})
for d in F:
    json.dump(d,open(f"content/de/{d['mediaId']}.json","w"),ensure_ascii=False,indent=2)
