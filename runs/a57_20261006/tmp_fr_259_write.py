import json
def P(t,g=None,acc=None):
    d={"text":t}
    if g: d["gap"]=True; d["accept"]=acc or [t]
    return d
def gap(t,*a): return P(t,1,[t,*a])
def N(ws,v): return [{"word":w,"voice":v} for w in ws]
def T(l,v): return [{"phrase":p,"target":t,"voice":vv} for p,t,vv in l]
C={}
C[259]=dict(level="B",keyWord="inquiétant",
 taps=T([("teinter le ciel d'un rouge inquiétant","la lueur rouge","male"),("remplir la gare de triage","les wagons de marchandises","male"),("former une silhouette sombre","les arbres","male")],None),
 nouns=N(["les nuages","la boule de feu","les wagons de marchandises","les cimes des arbres"],"male"),
 question="Qu'est-ce qui se répand dans le ciel nocturne ?",
 answer="Une lueur rouge inquiétante se répand dans le ciel.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":[P("teinter le ciel d'un rouge"),gap("inquiétant","sinistre")]},
  {"from":"taps","parts":[gap("remplir","occuper"),P("la gare de triage")]},
  {"from":"taps","parts":[P("former une"),gap("silhouette"),P("sombre")]},
  {"from":"answer","parts":[P("se"),gap("répand","propage"),P("dans le ciel")]}],
 notes="'Freight yard' = 'la gare de triage' (B1/B2 collocation). Adjective inquiétant placed after the noun in the answer (natural order); key word used in phrase 1. Phrase 3 kept close to English; the trees are a black silhouette in every frame.")
C[260]=dict(level="A",keyWord="un œuf",
 taps=T([("manger du pain","l'homme","male"),("être assis à la fenêtre","le chat","male"),("tomber dans la poêle","l'œuf","male")],None),
 nouns=N(["l'homme","le chat","les tomates","l'œuf"],"male"),
 question="Que mange l'homme ?",answer="Il mange du pain avec un œuf.".split(),answerVoice="male",
 recall=[{"from":"taps","parts":[gap("manger"),P("du pain")]},
  {"from":"taps","parts":[P("être assis à la"),gap("fenêtre")]},
  {"from":"taps","parts":[P("tomber dans la"),gap("poêle")]},
  {"from":"answer","parts":[P("mange du pain avec un"),gap("œuf")]}],
 notes="The cat sits on the windowsill most of the time but stands in a few late frames; 'être assis à la fenêtre' describes most boxed frames. No noun row: the answer row already contains the key word (œuf).")
C[261]=dict(level="A",keyWord="un électricien",
 taps=T([("couper un fil","l'électricienne","female"),("porter un tee-shirt rose","la fille","female"),("avoir une barbe","l'homme","male")],None),
 nouns=N(["la porte","l'homme","la fille","l'électricienne"],"female"),
 question="Que fait l'électricienne ?",answer="Elle coupe un fil.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":[gap("couper"),P("un fil")]},
  {"from":"taps","parts":[P("porter un"),gap("tee-shirt","t-shirt"),P("rose")]},
  {"from":"taps","parts":[P("avoir une"),gap("barbe")]},
  {"from":"answer","parts":[P("coupe un"),gap("fil","câble")]}],
 notes="Key word: the worker is a woman, so the noun is the feminine 'l'électricienne' (database word 'un électricien' kept; proposal: add 'une électricienne' as the feminine form). No noun row: 'l'électricienne' is one elided chip and cannot be split into 2 parts. Noun voices copied from English (man = male).")
C[262]=dict(level="A",keyWord="un éléphant",
 taps=T([("boire avec sa trompe","l'éléphant","female"),("lever sa trompe","l'éléphant","female"),("avoir des plumes blanches","les oiseaux blancs","female")],None),
 nouns=N(["l'arbre","l'éléphant","l'oiseau","l'eau"],"female"),
 question="Que fait l'éléphant ?",answer="Il boit de l'eau avec sa trompe.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":[gap("boire"),P("avec sa trompe")]},
  {"from":"taps","parts":[P("lever sa"),gap("trompe")]},
  {"from":"taps","parts":[P("avoir des"),gap("plumes"),P("blanches")]},
  {"from":"answer","parts":[gap("boit"),P("de l'eau avec sa trompe")]}],
 notes="Answer pronoun 'il' (l'éléphant is masculine); answerVoice kept female as in English. No noun row: 'l'éléphant' is one elided chip and cannot be split into 2 parts. Phrase 2 (raising the trunk) happens in the late boxed frames only; English box covers the whole clip.")
C[263]=dict(level="B",keyWord="émerger",
 taps=T([("émerger du lac","la nageuse","female"),("relever ses lunettes de natation","la nageuse","female"),("flotter près de la rive","la barque","female")],None),
 nouns=N(["les lunettes de natation","la barque","le reflet","les montagnes"],"female"),
 question="Que fait la nageuse ?",answer="Elle émerge du lac.".split(),answerVoice="female",
 recall=[{"from":"taps","parts":[P("émerger du"),gap("lac")]},
  {"from":"taps","parts":[gap("relever","remonter"),P("ses lunettes de natation")]},
  {"from":"taps","parts":[P("flotter près de la"),gap("rive","berge")]},
  {"from":"answer","parts":[gap("émerge","surgit"),P("du lac")]}],
 notes="B words: émerger, relever ses lunettes, la rive, le reflet, la barque. The boat lies still near the shore; 'flotter' kept.")
for i,c in C.items():
    d={"mediaId":i,"lang":"fr",**{k:c[k] for k in ["level","keyWord","taps","nouns","question","answer","answerVoice"]},"carousel":[],"recall":c["recall"],"notes":c["notes"]}
    json.dump(d,open(f"content/fr/{i}.json","w"),ensure_ascii=False,indent=1)
