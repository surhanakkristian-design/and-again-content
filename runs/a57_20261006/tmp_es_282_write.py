import json
def P(*parts):
    out=[]
    for p in parts:
        if isinstance(p,tuple): out.append({"text":p[0],"gap":True,"accept":list(p[1])})
        else: out.append({"text":p})
    return out
def T(ph,tg,v): return {"phrase":ph,"target":tg,"voice":v}
def N(w,v): return {"word":w,"voice":v}
V={}
V[282]=dict(level="B",keyWord="la sombra de ojos",
 taps=[T("aplicar sombra de ojos dorada","la brocha","female"),T("llevar un turbante de satén","la chica del turbante","female"),T("lucir los párpados dorados","la chica de la camisa","female")],
 nouns=[N("el turbante","female"),N("la sombra de ojos","female"),N("el cuello","female"),N("el botón","female")],
 question="¿Qué hace la brocha?",answer="Aplica sombra de ojos dorada en el párpado.",answerVoice="female",
 recall=[{"from":"taps","parts":P(("aplicar",["aplicar","extender"]),"sombra de ojos dorada")},
         {"from":"taps","parts":P("llevar un",("turbante",["turbante"]),"de satén")},
         {"from":"taps","parts":P(("lucir",["lucir","enseñar","mostrar"]),"los párpados dorados")},
         {"from":"answer","parts":P("Aplica",("sombra de ojos",["sombra de ojos"]),"dorada en el párpado")}],
 notes="Phrase 1: English 'pick up gold eyeshadow', but in most boxed frames the brush is applying/patting the eyeshadow on the eyelid (it picks it up only in the first two frames), so I wrote 'aplicar sombra de ojos dorada' and asked what the brush does. Headscarf: she wears a knotted satin head wrap; 'el turbante' is the natural Spanish word for this tied style (pañuelo would also be possible). Collar = 'el cuello' (of the shirt). No noun row: the key word is already in rows 1 and 4.")
V[283]=dict(level="B",keyWord="la tela",
 taps=[T("desenrollar la tela estampada","el hombre","male"),T("cortar la tela con unas tijeras","el hombre","male"),T("abrazar la tela doblada","la chica","female")],
 nouns=[N("el pendiente","female"),N("la tela","female"),N("la mesa","female"),N("la cinta métrica","female")],
 question="¿Qué está haciendo el hombre?",answer="Está cortando la tela con unas tijeras.",answerVoice="male",
 recall=[{"from":"taps","parts":P(("desenrollar",["desenrollar","extender"]),"la tela estampada")},
         {"from":"taps","parts":P("cortar la tela con unas",("tijeras",["tijeras"]))},
         {"from":"taps","parts":P(("abrazar",["abrazar","estrechar"]),"la tela doblada")},
         {"from":"answer","parts":P("Está cortando la",("tela",["tela"]),"con unas tijeras")}],
 notes="B level: phrases carry desenrollar / estampada / tijeras / doblada; the answer's B-level word is 'tijeras' (and 'cortar la tela' collocation). Green box also covers frames where he measures with the tape before cutting. Earring: only one visible in most frames, singular as in English. No noun row: 'tela' is in every row.")
V[284]=dict(level="B",keyWord="la mascarilla facial",
 taps=[T("llevar una diadema esponjosa","la chica de morado","female"),T("señalar a su amiga","la chica de gris","female"),T("asomar la cabeza entre las dos","el perro","female")],
 nouns=[N("la diadema","female"),N("la mascarilla facial","female"),N("el perro","female"),N("el bol","female")],
 question="¿Qué llevan las chicas en la cara?",answer="Llevan una mascarilla facial verde.",answerVoice="female",
 recall=[{"from":"taps","parts":P("llevar una",("diadema",["diadema"]),"esponjosa")},
         {"from":"taps","parts":P(("señalar",["señalar"]),"a su amiga")},
         {"from":"taps","parts":P("asomar la",("cabeza",["cabeza"]),"entre las dos")},
         {"from":"answer","parts":P("Llevan una",("mascarilla",["mascarilla"]),"facial verde")}],
 notes="Phrase 2: the woman in grey points at her friend only in the last frames; the green box also covers frames where she just sits (and the close-ups of the mask being spread). Phrase 3: English 'rest on a cushion', but only the dog's head is visible, peeking out between the two women; the cushion is not clearly visible, so I wrote 'asomar la cabeza entre las dos'. Answer uses the distributive singular ('Llevan una mascarilla'), the natural Spanish form. 'la mascarilla facial' is fine; in Spain plain 'la mascarilla' is the everyday word in this context.")
V[285]=dict(level="A",keyWord="la familia",
 taps=[T("hacer una foto de familia","el abuelo","male"),T("saludar con las dos manos","el abuelo","male"),T("subir los escalones corriendo","el perro","male")],
 nouns=[N("la ventana","male"),N("la familia","male"),N("los escalones","male"),N("la hierba","male")],
 question="¿Qué está haciendo la familia?",answer="Se está haciendo una foto de familia.",answerVoice="male",
 recall=[{"from":"taps","parts":P("hacer una foto de",("familia",["familia"]))},
         {"from":"taps","parts":P(("saludar",["saludar"]),"con las dos manos")},
         {"from":"taps","parts":P("subir los",("escalones",["escalones","escaleras"]),"corriendo")},
         {"from":"answer","parts":P("Se está haciendo una",("foto",["foto"]),"de familia")}],
 notes="'la familia' is grammatically singular in Spanish, so the answer is 'Se está haciendo una foto de familia' (English 'They are taking'). answerVoice kept male as in English. 'Subir los escalones corriendo' could also be 'subir corriendo los escalones'; the row is fixed as written. Lawn = 'la hierba' (A1; 'el césped' also possible).")
V[287]=dict(level="A",keyWord="lejos",
 taps=[T("señalar un pueblo","la mujer","female"),T("mirar hacia atrás","el hombre de verde","male"),T("llevar una chaqueta roja","la persona de rojo","female")],
 nouns=[N("el cielo","female"),N("el pueblo","female"),N("la hierba","female")],
 question="¿Qué está señalando la mujer?",answer="Está señalando un pueblo que está muy lejos.",answerVoice="female",
 recall=[{"from":"taps","parts":P("señalar un",("pueblo",["pueblo"]))},
         {"from":"taps","parts":P(("mirar",["mirar"]),"hacia atrás")},
         {"from":"taps","parts":P("llevar una",("chaqueta",["chaqueta","cazadora"]),"roja")},
         {"from":"answer","parts":P("Está señalando un pueblo que está muy",("lejos",["lejos"]))}],
 notes="Phrase 1: she points only in the close-up frames; in the wide shots the red box holds her standing. Phrase 2: 'mirar hacia atrás' (he turns back to look at her) - A level, the man in green is the only one doing it. The village is a tiny white settlement on the horizon. Key word 'lejos' (adverb) is gapped in the answer row; no noun row.")
for i,d in V.items():
    ans=d.pop("answer").split(" ")
    out={"mediaId":i,"lang":"es","level":d["level"],"keyWord":d["keyWord"],"taps":d["taps"],"nouns":d["nouns"],
         "question":d["question"],"answer":ans,"answerVoice":d["answerVoice"],"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(out,open(f"content/es/{i}.json","w"),ensure_ascii=False,indent=2)
