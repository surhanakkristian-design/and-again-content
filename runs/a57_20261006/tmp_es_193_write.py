import json
def T(p,t,v): return {"phrase":p,"target":t,"voice":v}
def N(w,v): return {"word":w,"voice":v}
def R(src, parts):
    out=[]
    for x in parts:
        if isinstance(x,str): out.append({"text":x})
        else: out.append({"text":x[0],"gap":True,"accept":x[1]})
    return {"from":src,"parts":out}
D={}
D[193]=dict(level="B",keyWord="corrupto",
 taps=[T("aceptar un soborno","el hombre","male"),T("sellar el documento","el hombre","male"),T("meter la mano en el bolsillo","la mujer","female")],
 nouns=[N("el sello","male"),N("el bigote","male"),N("el documento","male"),N("el delantal","male")],
 question="¿Qué está haciendo el hombre?",
 answer="El funcionario corrupto está aceptando un soborno.".split(),answerVoice="male",
 recall=[R("taps",["aceptar un",("soborno",["soborno"])]),
         R("taps",[("sellar",["sellar"]),"el documento"]),
         R("taps",["meter la mano en el",("bolsillo",["bolsillo"])]),
         R("answer",["está",("aceptando",["aceptando","cogiendo"]),"un soborno"])],
 notes="Key word 'corrupto' (adjective) appears only in the answer subject 'El funcionario corrupto', which the A57 answer row drops, so no recall row gaps the key word. 'el sello' = the rubber stamp object (also used in 'sellar'). Phrase 3: she reaches into her apron pocket; 'el bolsillo' is the apron pocket.")
D[194]=dict(level="A",keyWord="el algodón",
 taps=[T("sostener un poco de algodón","la chica","female"),T("soplar el algodón","la chica","female"),T("llevar una camiseta blanca","el chico","male")],
 nouns=[N("el sol","female"),N("el sombrero","female"),N("el algodón","female"),N("la camiseta","female")],
 question="¿Qué tiene la chica en la mano?",
 answer="Tiene algodón en la mano.".split(),answerVoice="female",
 recall=[R("taps",[("sostener",["sostener","coger"]),"un poco de algodón"]),
         R("taps",[("soplar",["soplar"]),"el algodón"]),
         R("taps",["llevar una",("camiseta",["camiseta"]),"blanca"]),
         R("answer",["Tiene",("algodón",["algodón"]),"en la mano"])],
 notes="Phrase 2 box (same box as phrase 1) covers mostly frames where she only holds the cotton; she blows it away only at the end. Kept 'soplar el algodón' because phrase 1 already says she holds it. 'la chica'/'el chico' for the young couple. Answer has no subject (natural Spanish), so the answer row is the whole sentence.")
D[195]=dict(level="A",keyWord="la tos",
 taps=[T("toser en la mano","la chica","female"),T("traer un té caliente","el chico","male"),T("andar sobre la manta","el gato","female")],
 nouns=[N("las plantas","female"),N("la taza","female"),N("la manta","female"),N("el gato","female")],
 question="¿Qué está haciendo la chica enferma?",
 answer="Está tosiendo en la mano.".split(),answerVoice="female",
 recall=[R("taps",["toser en la",("mano",["mano"])]),
         R("taps",["traer un",("té",["té"]),"caliente"]),
         R("taps",["andar sobre la",("manta",["manta"])]),
         R("answer",["Está",("tosiendo",["tosiendo"]),"en la mano"])],
 notes="Key word 'la tos' (noun) is not a thing of the noun set; the clip shows the verb 'toser' (phrase 1, answer). Phrase 1 box covers the whole clip: she coughs in the first half, later sips the tea; phrase written for the coughing. Phrase 3: the cat steps onto her lap/blanket only in the last frames.")
D[196]=dict(level="B",keyWord="la valentía",
 taps=[T("mantener el equilibrio sobre una tabla","la chica","female"),T("agarrarse al cable de acero","la chica","female"),T("llegar a la plataforma de madera","la chica","female")],
 nouns=[N("el casco","female"),N("el arnés","female"),N("la tabla","female"),N("los árboles","female")],
 question="¿Qué está haciendo la chica?",
 answer="Mantiene el equilibrio sobre una tabla estrecha.".split(),answerVoice="female",
 recall=[R("taps",["mantener el",("equilibrio",["equilibrio"]),"sobre una tabla"]),
         R("taps",[("agarrarse",["agarrarse","sujetarse"]),"al cable de acero"]),
         R("taps",["llegar a la",("plataforma",["plataforma"]),"de madera"]),
         R("answer",["Mantiene el equilibrio sobre una tabla",("estrecha",["estrecha"])])],
 notes="Key word 'la valentía' is abstract and not shown as a thing or action; it is not used in any exercise (not forced). All three boxes cover the whole clip (one girl); phrase 3 happens only at the end (platform). Answer has no subject, so the answer row is the whole sentence.")
D[197]=dict(level="A",keyWord="la vaca",
 taps=[T("comer hierba verde","la vaca","female"),T("beber la leche","el ternero","female"),T("echar la leche","la mujer","female")],
 nouns=[N("la vaca","female"),N("la mujer","female"),N("el cencerro","female"),N("la leche","female")],
 question="¿Qué está comiendo la vaca?",
 answer="La vaca está comiendo hierba verde.".split(),answerVoice="female",
 recall=[R("taps",["comer",("hierba",["hierba"]),"verde"]),
         R("taps",["beber la",("leche",["leche"])]),
         R("taps",[("echar",["echar","verter"]),"la leche"]),
         R("nouns",["la",("vaca",["vaca"])]),
         R("answer",["está",("comiendo",["comiendo"]),"hierba verde"])],
 notes="'el cencerro' is the exact Spanish word for a cowbell but above A2 (plain 'la campana' would be wrong for a cowbell); kept. Phrase 2: the calf only stands in the background in the early boxed frames and drinks the milk at the end. 'echar la leche' (Spain, A-level) for pouring.")
for i,d in D.items():
    c={"mediaId":i,"lang":"es","level":d["level"],"keyWord":d["keyWord"],"taps":d["taps"],"nouns":d["nouns"],
       "question":d["question"],"answer":d["answer"],"answerVoice":d["answerVoice"],"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(c,open(f"content/es/{i}.json","w"),ensure_ascii=False,indent=1)
