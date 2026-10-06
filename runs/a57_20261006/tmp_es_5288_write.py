import json
def P(*a):
    out=[]
    for x in a:
        if isinstance(x,tuple): out.append({"text":x[0],"gap":True,"accept":list(x[1])})
        else: out.append({"text":x})
    return out
D={}
D[5288]=dict(level="A",keyWord="el esquí",
 taps=[("bajar la pista esquiando","el esquiador de rojo","male"),("llevar un traje rojo","el esquiador de rojo","male"),("dar un salto","el esquiador de rojo","male")],
 nouns=[("los esquís","male"),("las montañas","male"),("el cielo","male"),("la nieve","male")],
 question="¿Qué está haciendo el esquiador de rojo?",answer="Está esquiando por la pista.",answerVoice="male",
 recall=[("taps",P(("bajar",["bajar"]),"la pista esquiando")),("taps",P("llevar un",("traje",["traje","mono"]),"rojo")),("taps",P("dar un",("salto",["salto"]))),
  ("nouns",P("los",("esquís",["esquís"]))),("answer",P("Está",("esquiando",["esquiando"]),"por la pista"))],
 notes="The jump ('dar un salto') is visible only in some boxed frames (box_04); most frames show him carving down the piste. 'Hill' rendered as 'la pista' (natural for a ski slope in Spain). The suit is a one-piece ('mono'), 'traje' kept as the A-level word; recall accepts 'mono'.")
D[7811]=dict(level="B",keyWord="las docenas",
 taps=[("sujetar una raqueta de tenis","la mujer de blanco","female"),("agarrar la máquina lanzapelotas","el hombre de verde","male"),("lanzar docenas de pelotas","la máquina lanzapelotas","female")],
 nouns=[("las nubes","female"),("la máquina lanzapelotas","female"),("la raqueta","female"),("las pelotas de tenis","female")],
 question="¿Qué está haciendo la máquina lanzapelotas?",answer="Está lanzando docenas de pelotas de tenis.",answerVoice="female",
 recall=[("taps",P("sujetar una",("raqueta",["raqueta"]),"de tenis")),("taps",P(("agarrar",["agarrar","coger"]),"la máquina lanzapelotas")),("taps",P("lanzar",("docenas",["docenas","decenas"]),"de pelotas")),
  ("answer",P("Está",("lanzando",["lanzando","disparando"]),"docenas de pelotas de tenis"))],
 notes="Phrase 1: the woman swings the racket only in the first two boxed frames; in most frames she stands laughing holding it lowered, so 'sujetar una raqueta de tenis'. keyWord: in Spain 'decenas' (or 'montones') is the more usual word for an indefinite 'dozens'; 'docenas' is correct and used here as the database word; recall accepts 'decenas'. Proposal: consider 'las decenas'.")
D[526]=dict(level="B",keyWord="paralizar",
 taps=[("observar al hombre paralizado","la mujer","female"),("sujetar una taza blanca","el hombre","male"),("quedarse tieso como un palo","el hombre","male")],
 nouns=[("las gafas protectoras","female"),("el cactus","female"),("el chándal","female"),("la tubería","female")],
 question="¿Qué hace la mujer?",answer="Lo paraliza con una pistola de rayos.",answerVoice="female",
 recall=[("taps",P(("observar",["observar","mirar"]),"al hombre paralizado")),("taps",P("sujetar una",("taza",["taza"]),"blanca")),("taps",P("quedarse",("tieso",["tieso","rígido"]),"como un palo")),
  ("answer",P("Lo",("paraliza",["paraliza"]),"con una pistola de rayos"))],
 notes="Phrase 1: the woman fires the ray gun only in the first boxed frames; in most frames she watches, touches and waves at the frozen man, so 'observar al hombre paralizado' (key word inside, allowed). Phrase 3: he topples backwards only in the last frames; in most frames he stands frozen rigid, so 'quedarse tieso como un palo' (covers the stiff fall too). Answer subject dropped (es); 'Lo' is the object clitic, the subject is la mujer.")
D[517]=dict(level="B",keyWord="adelantar",
 taps=[("adelantar a una autocaravana","el coche rojo","male"),("ponerse en cabeza","el coche rojo","male"),("quedarse atrás","la autocaravana","male")],
 nouns=[("la autocaravana","male"),("el descapotable","male"),("las dunas de arena","male"),("la carretera","male")],
 question="¿Qué está haciendo el coche rojo?",answer="Está adelantando a una autocaravana.",answerVoice="male",
 recall=[("taps",P("adelantar a una",("autocaravana",["autocaravana"]))),("taps",P("ponerse en",("cabeza",["cabeza"]))),("taps",P(("quedarse",["quedarse"]),"atrás")),
  ("answer",P("Está",("adelantando",["adelantando"]),"a una autocaravana"))],
 notes="'Highway' = 'la carretera': a two-lane desert road, not an 'autopista' in Spain. Phrase 2 'swing in front' rendered as 'ponerse en cabeza' (the red car pulls ahead in most frames).")
D[8027]=dict(level="B",keyWord="los montones",
 taps=[("montar en patinete","el hombre","male"),("alzar los brazos","el hombre","male"),("asomarse por detrás del cristal","la mujer","female")],
 nouns=[("el sombrero de paja","male"),("la lámpara de techo","male"),("el patinete","male"),("las bolas de plástico","male")],
 question="¿Qué está haciendo el hombre?",answer="Está montando en patinete entre montones de bolas.",answerVoice="male",
 recall=[("taps",P("montar en",("patinete",["patinete"]))),("taps",P(("alzar",["alzar","levantar"]),"los brazos")),("taps",P(("asomarse",["asomarse"]),"por detrás del cristal")),
  ("answer",P("Está montando en patinete entre",("montones",["montones"]),"de bolas"))],
 notes="Phrase 3: the woman covers her mouth only in the first two boxed frames; in most frames she leans out from behind the glass laughing, so 'asomarse por detrás del cristal' (laughing alone would fit the man too).")
for i,d in D.items():
    out={"mediaId":i,"lang":"es","level":d["level"],"keyWord":d["keyWord"],
     "taps":[{"phrase":p,"target":t,"voice":v} for p,t,v in d["taps"]],
     "nouns":[{"word":w,"voice":v} for w,v in d["nouns"]],
     "question":d["question"],"answer":d["answer"].split(" "),"answerVoice":d["answerVoice"],
     "carousel":[],"recall":[{"from":f,"parts":p} for f,p in d["recall"]],"notes":d["notes"]}
    json.dump(out,open(f"content/es/{i}.json","w"),ensure_ascii=False,indent=1)
