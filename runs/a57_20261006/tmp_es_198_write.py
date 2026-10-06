import json
def T(p,t,v):return {"phrase":p,"target":t,"voice":v}
def N(w,v):return {"word":w,"voice":v}
def R(f,parts):return {"from":f,"parts":[({"text":x[0],"gap":True,"accept":x[1]} if isinstance(x,tuple) else {"text":x}) for x in parts]}
D={}
D[198]=dict(level="B",keyWord="el calambre",
 taps=[T("agarrarse la pantorrilla dolorida","la mujer","female"),T("arrodillarse en la pista","el hombre","male"),T("levantar el pulgar","la mujer","female")],
 nouns=[N("la mujer","female"),N("el hombre","male"),N("los rascacielos","female"),N("la pista de atletismo","female")],
 question="¿Qué se está agarrando la mujer?",answer="Se está agarrando la pantorrilla dolorida.".split(),answerVoice="female",
 recall=[R("taps",["agarrarse la",("pantorrilla",["pantorrilla"]),"dolorida"]),R("taps",[("arrodillarse",["arrodillarse"]),"en la pista"]),R("taps",["levantar el",("pulgar",["pulgar","dedo"])]),R("answer",["Se está",("agarrando",["agarrando","sujetando"]),"la pantorrilla dolorida"])],
 notes="Key word 'el calambre' is not a noun of the set and appears in no exercise (the clip shows the cramp only through her pain). Subject dropped in the answer, so the answer row is the whole sentence. Tap 3 box also covers frames where she clutches her leg / runs; the thumbs up is in the final frames.")
D[199]=dict(level="A",keyWord="estrellarse",
 taps=[T("conducir un coche rojo","el hombre","male"),T("levantar los dos brazos","el hombre","male"),T("llevar una camiseta amarilla","el hombre","male")],
 nouns=[N("el hombre","male"),N("el coche rojo","male"),N("el coche amarillo","male")],
 question="¿Qué está conduciendo el hombre?",answer="Está conduciendo un coche rojo.".split(),answerVoice="male",
 recall=[R("taps",["conducir un",("coche",["coche"]),"rojo"]),R("taps",["levantar los dos",("brazos",["brazos"])]),R("taps",["llevar una",("camiseta",["camiseta"]),"amarilla"]),R("answer",["Está",("conduciendo",["conduciendo"]),"un coche rojo"])],
 notes="Key word: for bumper cars a native in Spain says 'chocar' ('chocar con los coches'), 'estrellarse' (crash and wreck) does not fit the clip; proposal: chocar. The cars are 'coches de choque'; kept 'coche' at level A. Shirt shown is a T-shirt, so 'camiseta'.")
D[200]=dict(level="A",keyWord="la nata",
 taps=[T("batir la nata","el hombre","male"),T("comer un gofre","el hombre","male"),T("llevar un pañuelo en la cabeza","la mujer","female")],
 nouns=[N("la nata","male"),N("el gofre","male"),N("el plato","male")],
 question="¿Qué está haciendo el hombre?",answer="Está batiendo la nata.".split(),answerVoice="male",
 recall=[R("taps",["batir la",("nata",["nata"])]),R("taps",["comer un",("gofre",["gofre"])]),R("taps",["llevar un",("pañuelo",["pañuelo"]),"en la cabeza"]),R("answer",["Está",("batiendo",["batiendo","montando"]),"la nata"])],
 notes="'batir' (whisk) rather than 'mezclar': it is what he does with the whisk. Tap 3: she wears a headscarf, so 'llevar un pañuelo en la cabeza' instead of a literal 'cubrirse el pelo'. Tap 1 box also covers the bowl-on-head and tasting frames.")
D[201]=dict(level="A",keyWord="el cocodrilo",
 taps=[T("nadar en el río","el cocodrilo","male"),T("salir del agua","el cocodrilo","male"),T("abrir mucho la boca","el cocodrilo","male")],
 nouns=[N("el cocodrilo","male"),N("los árboles","male"),N("el río","male")],
 question="¿Qué está haciendo el cocodrilo?",answer="Está abriendo mucho la boca.".split(),answerVoice="male",
 recall=[R("taps",[("nadar",["nadar"]),"en el río"]),R("taps",["salir del",("agua",["agua"])]),R("taps",["abrir mucho la",("boca",["boca"])]),R("nouns",["el",("cocodrilo",["cocodrilo"])]),R("answer",["Está",("abriendo",["abriendo"]),"mucho la boca"])],
 notes="All three boxes cover the whole crocodile throughout, so each phrase is true only in part of the boxed frames (swimming early, on the mud later), same as English. Answer: 'mucho' before 'la boca' is the natural order.")
D[202]=dict(level="A",keyWord="cruzar",
 taps=[T("cruzar la calle","el hombre","male"),T("mirar el móvil","el hombre","male"),T("levantar el pulgar","el hombre","male")],
 nouns=[N("el hombre","male"),N("el coche","male"),N("los edificios","male"),N("la calle","male")],
 question="¿Qué está haciendo el hombre?",answer="Está cruzando la calle.".split(),answerVoice="male",
 recall=[R("taps",["cruzar la",("calle",["calle"])]),R("taps",["mirar el",("móvil",["móvil"])]),R("taps",["levantar el",("pulgar",["pulgar","dedo"])]),R("answer",["Está",("cruzando",["cruzando"]),"la calle"])],
 notes="Only one person in the boxes, so each phrase fits only him; boxes also cover frames where he does something else (phone, thumbs up only in parts).")
for i,d in D.items():
    o={"mediaId":i,"lang":"es","level":d["level"],"keyWord":d["keyWord"],"taps":d["taps"],"nouns":d["nouns"],"question":d["question"],"answer":d["answer"],"answerVoice":d["answerVoice"],"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(o,open(f"content/es/{i}.json","w"),ensure_ascii=False,indent=1)
