import json
def P(*xs):
    out=[]
    for x in xs:
        if isinstance(x,tuple): out.append({"text":x[0],"gap":True,"accept":list(x)})
        else: out.append({"text":x})
    return out
F="female"; M="male"
D={}
D[27]=dict(level="A",keyWord="der Student",
 taps=[dict(phrase="das Fenster öffnen",target="die Studentin",voice=F),
       dict(phrase="auf den Büchern stehen",target="die Tasse",voice=F),
       dict(phrase="auf dem Schreibtisch liegen",target="die Bücher",voice=F)],
 nouns=[dict(word="die Studentin",voice=F),dict(word="die Tasse",voice=F),dict(word="die Bücher",voice=F),dict(word="das Fenster",voice=F)],
 question="Was hält die Studentin?",answer=["Sie","hält","eine","Tasse."],answerVoice=F,
 recall=[{"from":"taps","parts":P("das Fenster",("öffnen","aufmachen"))},
         {"from":"taps","parts":P("auf den",("Büchern",),"stehen")},
         {"from":"taps","parts":P("auf dem",("Schreibtisch","Tisch"),"liegen")},
         {"from":"nouns","parts":P("die",("Studentin",))},
         {"from":"answer","parts":P(("hält",),"eine Tasse")}],
 notes="Key word der Student: the clip shows a young woman, so the noun pill and target are the feminine 'die Studentin' (same entry, female form); proposal: keep der Student as database word, show Studentin for this clip. Noun row uses 'die Studentin' (gap Studentin). Tap 1: the red box covers the whole clip, she opens the window only around 7-8 s; phrase kept as in English (it is her defining action). At the still (11.5 s) she holds the cup.")
D[28]=dict(level="A",keyWord="das Fach",
 taps=[dict(phrase="in die Kamera lächeln",target="die Frau",voice=F),
       dict(phrase="auf dem Tisch liegen",target="die Bücher",voice=F),
       dict(phrase="Klavier spielen",target="die Hände am Klavier",voice=F)],
 nouns=[dict(word="die Haare",voice=F),dict(word="die Jacke",voice=F),dict(word="die Bücher",voice=F)],
 question="Was macht die Frau?",answer=["Sie","lächelt","in","die","Kamera."],answerVoice=F,
 recall=[{"from":"taps","parts":P("in die",("Kamera",),"lächeln")},
         {"from":"taps","parts":P("auf dem Tisch",("liegen",))},
         {"from":"taps","parts":P(("Klavier",),"spielen")},
         {"from":"answer","parts":P(("lächelt",),"in die Kamera")}],
 notes="Key word das Fach is not shown as a thing in the clip (subjects only appear as quick cuts: maths, music, chemistry, art) and no exercise text contains it, same as English. 'die Jacke' for the cream blazer (A-level everyday word; der Blazer would be more exact). Tap 1: box also covers frames where she leans on the books and talks; she smiles into the camera in most of them.")
D[29]=dict(level="A",keyWord="das Teleskop",
 taps=[dict(phrase="durch das Teleskop schauen",target="die Frau",voice=F),
       dict(phrase="auf drei Beinen stehen",target="das Teleskop",voice=F),
       dict(phrase="am Himmel leuchten",target="der Mond",voice=F)],
 nouns=[dict(word="das Teleskop",voice=F),dict(word="die Mütze",voice=F),dict(word="die Jacke",voice=F),dict(word="der Himmel",voice=F)],
 question="Was macht die Frau?",answer=["Sie","schaut","durch","ein","Teleskop."],answerVoice=F,
 recall=[{"from":"taps","parts":P("durch das",("Teleskop",),"schauen")},
         {"from":"taps","parts":P("auf drei",("Beinen",),"stehen")},
         {"from":"taps","parts":P("am Himmel",("leuchten",))},
         {"from":"answer","parts":P(("schaut","guckt","sieht","blickt"),"durch ein Teleskop")}],
 notes="Tap 1: the red box also covers the close-up at the end where she looks up amazed beside the eyepiece; she looks through the telescope in the backyard frames. No noun row: the key word is already in tap row 1.")
D[32]=dict(level="A",keyWord="das Wort",
 taps=[dict(phrase="seinen Bart anfassen",target="der Mann",voice=M),
       dict(phrase="lange Haare haben",target="die Frau",voice=F),
       dict(phrase="groß und weiß sein",target="der Buchstabe",voice=F)],
 nouns=[dict(word="der Buchstabe",voice=F),dict(word="der Bart",voice=F),dict(word="die Frau",voice=F)],
 question="Was fasst der Mann an?",answer=["Er","fasst","seinen","Bart","an."],answerVoice=M,
 recall=[{"from":"taps","parts":P("seinen Bart",("anfassen","berühren"))},
         {"from":"taps","parts":P("lange",("Haare",),"haben")},
         {"from":"taps","parts":P("groß und",("weiß",),"sein")},
         {"from":"answer","parts":P("fasst seinen",("Bart",),"an")}],
 notes="Key word das Wort is not a visible thing (the clip shows the letter B; words are only spoken), no text contains it, same as English. Tap 1: the man touches his beard only in the thinking moments (about 4.5 s, 8-10 s, 11-12 s); the box covers him the whole clip. At the still (3.5 s) he is not touching his beard; the question follows the English one.")
D[33]=dict(level="B",keyWord="der Schmerz",
 taps=[dict(phrase="sich die geschwollene Wange halten",target="der Mann",voice=M),
       dict(phrase="vor sich hin dampfen",target="der Becher",voice=M),
       dict(phrase="in einem Tontopf wachsen",target="die Topfpflanze",voice=M)],
 nouns=[dict(word="die Topfpflanze",voice=M),dict(word="der Schnurrbart",voice=M),dict(word="das Kühlpack",voice=M),dict(word="der Becher",voice=M)],
 question="Was macht der Mann?",answer=["Er","hält","sich","vor","Schmerzen","die","geschwollene","Wange."],answerVoice=M,
 recall=[{"from":"taps","parts":P("sich die",("geschwollene","dicke"),"Wange halten")},
         {"from":"taps","parts":P("vor sich hin",("dampfen",))},
         {"from":"taps","parts":P("in einem",("Tontopf",),"wachsen")},
         {"from":"answer","parts":P("hält sich vor",("Schmerzen",),"die geschwollene Wange")}],
 notes="Answer chips allow a second German order ('Er hält sich die geschwollene Wange vor Schmerzen.' is also grammatical, though less natural); kept for the key word Schmerzen. Tap 1: in two boxed frames he sips from the mug instead of holding his cheek; he holds the cheek in most. No noun row: der Schmerz is not a noun of the set.")
for k,v in D.items():
    o={"mediaId":k,"lang":"de"}; o.update(v); o["carousel"]=[]
    order=["mediaId","lang","level","keyWord","taps","nouns","question","answer","answerVoice","carousel","recall","notes"]
    json.dump({x:o[x] for x in order},open(f'content/de/{k}.json','w'),ensure_ascii=False,indent=2)
