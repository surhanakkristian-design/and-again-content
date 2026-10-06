import json
def R(frm,text,gap,acc=()):
    i=text.split(' ').index(gap); w=text.split(' ')
    parts=[]
    if i>0: parts.append({"text":' '.join(w[:i])})
    parts.append({"text":gap,"gap":True,"accept":[gap]+list(acc)})
    if i<len(w)-1: parts.append({"text":' '.join(w[i+1:])})
    return {"from":frm,"parts":parts}
def T(p,t,v): return {"phrase":p,"target":t,"voice":v}
def N(w,v): return {"word":w,"voice":v}
V={}
V[42]=dict(level="A",keyWord="el examen",
 taps=[T("mirar su examen","el chico","male"),T("estar encima de los papeles","el bolígrafo","male"),T("cubrir la mesa","los papeles","male")],
 nouns=[N("la puerta","male"),N("la silla","male"),N("la pared","male"),N("los papeles","male")],
 question="¿Qué está mirando el chico?",answer="Está mirando su examen.",answerVoice="male",
 recall=[R("taps","mirar su examen","examen"),R("taps","estar encima de los papeles","papeles",["folios"]),R("taps","cubrir la mesa","cubrir",["tapar"]),R("answer","Está mirando su examen","mirando",["viendo"])],
 notes="Target 'el chico' (young man; 'el hombre' also possible). Tap box 1 also covers frames where he walks to/away from the table; phrase written for the frames where he sits and looks at the papers. No noun row: 'el examen' is not a noun of the set and is gapped in tap row 1.")
V[43]=dict(level="A",keyWord="girar",
 taps=[T("tirar de una cuerda","la mano","male"),T("girar muy rápido","la bola dorada","male"),T("sujetar una bola dorada","la mano","male")],
 nouns=[N("la impresora","male"),N("la bola","male"),N("el escritorio","male")],
 question="¿Qué está haciendo la bola dorada?",answer="Está girando muy rápido.",answerVoice="male",
 recall=[R("taps","tirar de una cuerda","cuerda",["cordel"]),R("taps","girar muy rápido","girar",["dar vueltas"]),R("taps","sujetar una bola dorada","sujetar",["sostener","coger"]),R("answer","Está girando muy rápido","rápido",["deprisa"])],
 notes="Strictly the ring spins around the golden ball; like the English, the whole gyroscope is called 'la bola dorada'. Tap box 1 also covers frames where the hand only places the gyroscope on the stand; phrase written for the string-pulling frames, as in English. Subject is a thing; answerVoice kept male. Key word gapped in tap row 2.")
V[44]=dict(level="B",keyWord="la ira",
 taps=[T("apretar los puños","la mujer","female"),T("llevarse las manos a la cabeza","la mujer","female"),T("estar esparcidas por la mesa","las flores","female")],
 nouns=[N("las trenzas","female"),N("el delantal","female"),N("el puño","female"),N("las flores","female")],
 question="¿Qué está haciendo la mujer?",answer="Aprieta los puños llena de ira.",answerVoice="female",
 recall=[R("taps","apretar los puños","apretar",["cerrar"]),R("taps","llevarse las manos a la cabeza","cabeza"),R("taps","estar esparcidas por la mesa","esparcidas",["tiradas","desperdigadas"]),R("answer","Aprieta los puños llena de ira","ira",["rabia"])],
 notes="'la rabia' is the more colloquial word in Spain; 'la ira' (database word) used in the answer with 'llena de ira' (B1). Taps 1 and 2 share one box (same woman) as in English; boxes also cover the kick and bag-throw frames - phrases written for the frames where she does them. Flowers lie on the market table (as in the description). No noun row: 'la ira' is not a noun of the set and is gapped in the answer row.")
V[45]=dict(level="A",keyWord="enfadado",
 taps=[T("gritarle al hombre","la mujer","female"),T("estar en el suelo","la ropa","female"),T("llevar una chaqueta gris","el hombre","male")],
 nouns=[N("las botellas","female"),N("la lavadora","female"),N("la mujer","female"),N("la ropa","female")],
 question="¿Qué está haciendo la mujer enfadada?",answer="Le está gritando al hombre.",answerVoice="female",
 recall=[R("taps","gritarle al hombre","gritarle",["chillarle"]),R("taps","estar en el suelo","suelo"),R("taps","llevar una chaqueta gris","chaqueta",["sudadera"]),R("answer","Le está gritando al hombre","gritando",["chillando"])],
 notes="The man's grey top looks like a sweatshirt jacket; 'chaqueta' kept as in English, 'sudadera' accepted. Tap box 1 also covers the opening frames where the woman walks in and picks up the clothes; phrase written for the shouting frames (most boxed frames). Key word 'enfadado' (adjective) appears in the question only ('la mujer enfadada'); no recall row can carry it naturally.")
V[46]=dict(level="A",keyWord="la manzana",
 taps=[T("cortar una manzana","la mujer","female"),T("tener la barba negra","el hombre","male"),T("estar encima de una caja","el pájaro","female")],
 nouns=[N("el hombre","male"),N("la mujer","female"),N("el pájaro","female"),N("la manzana","female")],
 question="¿Qué está haciendo la mujer?",answer="Está comiendo una manzana roja.",answerVoice="female",
 recall=[R("taps","cortar una manzana","cortar",["partir"]),R("taps","tener la barba negra","barba"),R("taps","estar encima de una caja","caja"),R("answer","Está comiendo una manzana roja","manzana")],
 notes="Tap box 1 covers the whole clip (picking, polishing, biting, then cutting); kept 'cortar una manzana' as in English because the man never cuts (he also eats). The bird is a magpie; 'el pájaro' kept as in English. No noun row: 'la manzana' is already in tap row 1 and gapped in the answer row.")
for i,d in V.items():
    out={"mediaId":i,"lang":"es","level":d["level"],"keyWord":d["keyWord"],"taps":d["taps"],"nouns":d["nouns"],
         "question":d["question"],"answer":d["answer"].split(' '),"answerVoice":d["answerVoice"],"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(out,open(f'content/es/{i}.json','w'),ensure_ascii=False,indent=1)
