import json
def P(*xs):
    out=[]
    for x in xs:
        if isinstance(x,tuple): out.append({"text":x[0],"gap":True,"accept":list(x[1])})
        else: out.append({"text":x})
    return out
def taps(lst): return [{"phrase":p,"target":t,"voice":v} for p,t,v in lst]
def nouns(lst,v): return [{"word":w,"voice":v} for w in lst]
D={}
D[27]=dict(level="A",keyWord="el estudiante",
 taps=taps([("abrir la ventana","la estudiante","female"),("estar encima de los libros","la taza","female"),("estar sobre el escritorio","los libros","female")]),
 nouns=nouns(["la estudiante","la taza","los libros","la ventana"],"female"),
 question="¿Qué sostiene la estudiante?",answer=["Sostiene","una","taza."],answerVoice="female",
 recall=[{"from":"taps","parts":P(("abrir",["abrir"]),"la ventana")},
  {"from":"taps","parts":P("estar encima de los",("libros",["libros"]))},
  {"from":"taps","parts":P("estar sobre el",("escritorio",["escritorio","mesa"]))},
  {"from":"nouns","parts":P("la",("estudiante",["estudiante"]))},
  {"from":"answer","parts":P("Sostiene una",("taza",["taza"]))}],
 notes="Key word el estudiante: the clip shows a young woman, so the pill and target use 'la estudiante' (same word, common gender, feminine article); keyWord kept unchanged. Noun row added (la estudiante). Tap 1: the red box covers the whole clip; she opens the window only around 7-8 s (her defining action), phrase kept. Tap 2: in a few boxed frames she holds the cup instead of it standing on the books. At the still (11.5 s) she holds the cup.")
D[28]=dict(level="A",keyWord="la asignatura",
 taps=taps([("sonreír a la cámara","la mujer","female"),("estar sobre la mesa","los libros","female"),("tocar el piano","las manos","female")]),
 nouns=nouns(["el pelo","la chaqueta","los libros"],"female"),
 question="¿Qué hace la mujer?",answer=["La","mujer","sonríe","a","la","cámara."],answerVoice="female",
 recall=[{"from":"taps","parts":P("sonreír a la",("cámara",["cámara"]))},
  {"from":"taps","parts":P("estar sobre la",("mesa",["mesa"]))},
  {"from":"taps","parts":P("tocar el",("piano",["piano"]))},
  {"from":"answer","parts":P(("sonríe",["sonríe"]),"a la cámara")}],
 notes="Key word la asignatura is not a visible thing (subjects appear only as quick cuts: maths, art, music, chemistry); no exercise text contains it, same as English. 'la chaqueta' for the cream blazer (A-level word). Tap 1: the red box also covers frames where she leans on the books and talks; she smiles at the camera in most of them.")
D[29]=dict(level="A",keyWord="el telescopio",
 taps=taps([("mirar por el telescopio","la mujer","female"),("tener tres patas","el telescopio","female"),("brillar en el cielo","la luna","female")]),
 nouns=nouns(["el telescopio","el gorro","el abrigo","el cielo"],"female"),
 question="¿Qué hace la mujer?",answer=["La","mujer","mira","por","el","telescopio."],answerVoice="female",
 recall=[{"from":"taps","parts":P(("mirar",["mirar"]),"por el telescopio")},
  {"from":"taps","parts":P("tener tres",("patas",["patas"]))},
  {"from":"taps","parts":P(("brillar",["brillar"]),"en el cielo")},
  {"from":"answer","parts":P("mira por el",("telescopio",["telescopio"]))}],
 notes="'el abrigo' for her padded jacket (in Spain the usual word for a winter down jacket; 'la chaqueta' would also do). 'tener tres patas' for the tripod (patas = legs of furniture/stands). Tap 1: the red box also covers the close-ups at the end where she looks up amazed beside the eyepiece. No noun row: the key word is already in tap row 1.")
D[32]=dict(level="A",keyWord="la palabra",
 taps=taps([("tocarse la barba","el hombre","male"),("tener el pelo largo","la mujer","female"),("ser grande y blanca","la letra","female")]),
 nouns=nouns(["la letra","la barba","la mujer"],"female"),
 question="¿Qué se toca el hombre?",answer=["El","hombre","se","toca","la","barba."],answerVoice="male",
 recall=[{"from":"taps","parts":P(("tocarse",["tocarse"]),"la barba")},
  {"from":"taps","parts":P("tener el",("pelo",["pelo"]),"largo")},
  {"from":"taps","parts":P("ser grande y",("blanca",["blanca"]))},
  {"from":"answer","parts":P("se toca la",("barba",["barba"]))}],
 notes="Key word la palabra is not a visible thing (the clip shows the letter B; words are only spoken); no exercise text contains it, same as English. Tap 1: the man touches his beard only in the thinking moments (about 4.5 s, 8-10 s, 11-12 s); the box covers him the whole clip. At the still (3.5 s) he is not touching his beard; question follows the English one.")
D[33]=dict(level="B",keyWord="el dolor",
 taps=taps([("sujetarse la mejilla hinchada","el hombre","male"),("echar vapor","la taza","male"),("crecer en una maceta de barro","la planta","male")]),
 nouns=nouns(["la planta","el bigote","la bolsa de hielo","la taza"],"male"),
 question="¿Qué hace el hombre?",answer=["El","hombre","se","sujeta","la","mejilla","hinchada","con","cara","de","dolor."],answerVoice="male",
 recall=[{"from":"taps","parts":P(("sujetarse",["sujetarse","agarrarse"]),"la mejilla hinchada")},
  {"from":"taps","parts":P("echar",("vapor",["vapor"]))},
  {"from":"taps","parts":P("crecer en una",("maceta",["maceta"]),"de barro")},
  {"from":"answer","parts":P("se sujeta la",("mejilla",["mejilla"]),"hinchada con cara de dolor")}],
 notes="Answer has 10 words (limit). 'con cara de dolor' carries the key word; 'con cara de dolor' could also stand after 'El hombre,' with commas, but without commas the chip order is unique. 'la planta' for the potted plant (the pot is named in tap 3). Tap 1: in two boxed frames he sips from the mug instead of holding his cheek; he holds it in most. No noun row: el dolor is not a noun of the set.")
for i,d in D.items():
    o={"mediaId":i,"lang":"es","level":d["level"],"keyWord":d["keyWord"],"taps":d["taps"],"nouns":d["nouns"],"question":d["question"],
       "answer":d["answer"],"answerVoice":d["answerVoice"],"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(o,open(f"content/es/{i}.json","w"),ensure_ascii=False,indent=1)
