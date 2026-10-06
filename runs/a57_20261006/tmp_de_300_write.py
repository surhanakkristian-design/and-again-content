import json
def T(p,t,v): return {"phrase":p,"target":t,"voice":v}
def N(w,v): return {"word":w,"voice":v}
def R(src,parts): return {"from":src,"parts":[{"text":p} if isinstance(p,str) else {"text":p[0],"gap":True,"accept":p[1]} for p in parts]}
D={}
D[300]=dict(keyWord="die Fahne",
 taps=[T("am Seil ziehen","das Mädchen","female"),T("im Wind wehen","die Fahne","female"),T("zur Fahne hochschauen","das Mädchen","female")],
 nouns=[N("die Fahne","female"),N("der Himmel","female"),N("die Berge","female"),N("das Mädchen","female")],
 question="Wohin schaut das Mädchen?", answer="Sie schaut zur Fahne hoch.".split(), answerVoice="female",
 recall=[R("taps",["am",("Seil",["Seil"]),"ziehen"]),R("taps",["im Wind",("wehen",["wehen","flattern"])]),
   R("taps",["zur",("Fahne",["Fahne","Flagge"]),"hochschauen"]),R("answer",[("schaut",["schaut","sieht","blickt"]),"zur Fahne hoch"])],
 notes="Answer uses 'Sie' for das Mädchen (what natives say). In the last boxed frames of tap 1 the girl has let go of the rope (hands on hips); phrase written for the majority of boxed frames. 'Wohin schaut ...?' is the natural German question for 'What is the girl looking at?'.")
D[301]=dict(keyWord="treiben",
 taps=[T("auf dem See treiben","der Mann","male"),T("den Daumen hochhalten","der Mann","male"),T("auf dem Mann sitzen","der Vogel","male")],
 nouns=[N("der Vogel","male"),N("der Mann","male"),N("der See","male")],
 question="Was macht der Mann?", answer="Er treibt auf dem See.".split(), answerVoice="male",
 recall=[R("taps",["auf dem See",("treiben",["treiben"])]),R("taps",["den",("Daumen",["Daumen"]),"hochhalten"]),
   R("taps",["auf dem Mann",("sitzen",["sitzen"])]),R("answer",["treibt auf dem",("See",["See"])])],
 notes="Tap 2 box covers the whole clip; the thumbs up only comes at the end (earlier he waves). Key word 'treiben' fits; a native might also say 'sich auf dem See treiben lassen', kept the plain A-level form. In the first boxed frames of tap 3 the bird is still flying towards the man.")
D[302]=dict(keyWord="das Mehl",
 taps=[T("auf dem Boden liegen","der Hund","male"),T("der Frau an die Nase tippen","der Mann","male"),T("ein graues Kopftuch tragen","die Frau","female")],
 nouns=[N("das Mehl","male"),N("die Eier","male"),N("der Hund","male")],
 question="Was hat der Mann im Gesicht?", answer="Er hat Mehl im Gesicht.".split(), answerVoice="male",
 recall=[R("taps",["auf dem Boden",("liegen",["liegen"])]),R("taps",["der Frau an die",("Nase",["Nase"]),"tippen"]),
   R("taps",["ein graues",("Kopftuch",["Kopftuch","Tuch"]),"tragen"]),R("answer",["hat",("Mehl",["Mehl"]),"im Gesicht"])],
 notes="English 'to touch her nose' -> 'der Frau an die Nase tippen' (noun instead of an unanchored 'ihr'); the man touches her nose only in the last boxed frames, before that he stands surprised with flour on his face. The woman's grey scarf is worn on the head -> 'Kopftuch'. Question rephrased natively ('Was hat der Mann im Gesicht?') instead of a genitive.")
D[303]=dict(keyWord="die Blume",
 taps=[T("einen Blumenstrauß halten","die Frau","female"),T("am Fenster sitzen","die Frau","female"),T("eine rosa Blume berühren","die Frau","female")],
 nouns=[N("das Fenster","female"),N("die Blumen","female"),N("die Frau","female")],
 question="Was hält die Frau?", answer="Sie hält einen Blumenstrauß.".split(), answerVoice="female",
 recall=[R("taps",["einen",("Blumenstrauß",["Blumenstrauß","Strauß"]),"halten"]),R("taps",["am",("Fenster",["Fenster"]),"sitzen"]),
   R("taps",["eine rosa",("Blume",["Blume"]),"berühren"]),R("answer",[("hält",["hält"]),"einen Blumenstrauß"])],
 notes="All three boxes cover the whole clip with the same target; in the close-up frames she is not visibly by the window or holding the whole bouquet, phrases written for the majority of frames. 'Blumenstrauß' counts as containing the key word (owner decision 404).")
D[305]=dict(keyWord="die Fliege",
 taps=[T("auf dem Brot landen","die Fliege","male"),T("über den Tisch fliegen","die Fliege","male"),T("mit einer Serviette wedeln","die Hand","male")],
 nouns=[N("die Fliege","male"),N("das Marmeladenglas","male"),N("der Tee","male"),N("das Brot","male")],
 question="Was macht die Fliege?", answer="Sie sitzt auf dem Brot.".split(), answerVoice="male",
 recall=[R("taps",["auf dem Brot",("landen",["landen"])]),R("taps",["über den",("Tisch",["Tisch"]),"fliegen"]),
   R("taps",["mit einer",("Serviette",["Serviette"]),"wedeln"]),R("nouns",["die",("Fliege",["Fliege"])]),
   R("answer",["sitzt auf dem",("Brot",["Brot","Toast"])])],
 notes="Taps 1 and 2 share identical boxes (the fly); phrase 1 is true while it lands/sits on the toast, phrase 2 while it flies around - in the boxed frames the fly also sits on the tea glass and the jar. 'a jar' -> 'das Marmeladenglas' (plain 'das Glas' would clash with the tea glass). The bread is toast; 'das Brot' kept throughout, 'Toast' accepted. answerVoice kept male (a fly has no natural gender; 'sie' is only grammatical).")
for i,d in D.items():
    src=json.load(open(f'src/{i}.json'))
    out={"mediaId":i,"lang":"de","level":src["level"],"keyWord":d["keyWord"],"taps":d["taps"],"nouns":d["nouns"],
         "question":d["question"],"answer":d["answer"],"answerVoice":d["answerVoice"],"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    assert out["keyWord"]==src["keyWord"]["de"]
    json.dump(out,open(f'content/de/{i}.json','w'),ensure_ascii=False,indent=1)
