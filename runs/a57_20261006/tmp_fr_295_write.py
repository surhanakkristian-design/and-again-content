import json,os
os.makedirs('content/fr',exist_ok=True)
def R(frm,*parts):
    ps=[]
    for p in parts:
        if isinstance(p,tuple): ps.append({"text":p[0],"gap":True,"accept":list(p[1])})
        else: ps.append({"text":p})
    return {"from":frm,"parts":ps}
def T(p,t,v): return {"phrase":p,"target":t,"voice":v}
def N(w,v): return {"word":w,"voice":v}
D={}
D[295]=dict(level="A",keyWord="mélanger",
 taps=[T("mélanger la pâte épaisse","la main","male"),T("tenir un manche noir","la main","male"),T("être collé au sol","le ruban adhésif bleu","male")],
 nouns=[N("le ruban adhésif","male"),N("le seau","male"),N("la main","male"),N("la chaussure","male")],
 question="Que fait la main ?",answer="La main mélange la pâte épaisse.".split(),answerVoice="male",
 recall=[R("taps",("mélanger",["mélanger","remuer"]),"la pâte épaisse"),R("taps","tenir un",("manche",["manche"]),"noir"),
         R("taps","être",("collé",["collé","fixé"]),"au sol"),R("answer","mélange la",("pâte",["pâte"]),"épaisse")],
 notes="'le manche' (handle of the putty knife) is the exact word, maybe slightly above A2; 'la poignée' would be the alternative. Two shoes are visible; kept singular like English.")
D[296]=dict(level="A",keyWord="le poisson",
 taps=[T("tenir un demi-citron","l'homme","male"),T("manger avec une fourchette","la femme","female"),T("griller au-dessus du feu","le poisson","female")],
 nouns=[N("la mer","female"),N("le bateau","female"),N("le poisson","female"),N("le feu","female")],
 question="Que mange la femme ?",answer="Elle mange du poisson avec une fourchette.".split(),answerVoice="female",
 recall=[R("taps","tenir un",("demi-citron",["demi-citron"])),R("taps","manger avec une",("fourchette",["fourchette"])),
         R("taps",("griller",["griller","cuire"]),"au-dessus du feu"),R("answer","mange du",("poisson",["poisson"]),"avec une fourchette")],
 notes="Blue box (fish) also covers later frames where the grilled fish lies on a wooden board, not over the fire; phrase written for the grilling frames (majority). No noun row: 'poisson' is already in the answer row.")
D[297]=dict(level="A",keyWord="la pêche",
 taps=[T("tenir une canne à pêche","l'homme","male"),T("tenir un filet","la femme","female"),T("nager dans le lac","le poisson","male")],
 nouns=[N("le poisson","male"),N("le filet","male"),N("la casquette","male"),N("les arbres","male")],
 question="Que font l'homme et la femme ?",answer="Ils pêchent dans le lac.".split(),answerVoice="male",
 recall=[R("taps","tenir une canne à",("pêche",["pêche"])),R("taps","tenir un",("filet",["filet","épuisette"])),
         R("taps",("nager",["nager"]),"dans le lac"),R("answer","pêchent dans le",("lac",["lac"]))],
 notes="The landing net is 'une épuisette' in precise French, but that is above level A; used the plain A word 'le filet' everywhere. Key word 'la pêche' appears inside 'canne à pêche' and as the verb 'pêcher' in the answer.")
D[298]=dict(level="B",keyWord="la cabine d'essayage",
 taps=[T("essayer plusieurs tenues","la femme blonde","female"),T("donner son avis avec le pouce","la femme brune","female"),T("se prélasser sur le comptoir","le chien","female")],
 nouns=[N("le rideau","female"),N("la pile de vêtements","female"),N("les sandales","female"),N("le chien","female")],
 question="Que fait la femme blonde ?",answer="Elle essaie des tenues dans une cabine d'essayage.".split(),answerVoice="female",
 recall=[R("taps",("essayer",["essayer"]),"plusieurs tenues"),R("taps","donner son",("avis",["avis"]),"avec le pouce"),
         R("taps","se prélasser sur le",("comptoir",["comptoir"])),R("answer","essaie des tenues dans une",("cabine",["cabine"]),"d'essayage")],
 notes="Phrase 2: the dark-haired woman gives thumbs down in most boxed frames and thumbs up only at the end, so 'donner son avis avec le pouce' (covers both) instead of 'lever le pouce'. No noun row: the key word is in the answer row.")
D[299]=dict(level="A",keyWord="réveiller",
 taps=[T("dormir dans son lit","la femme","female"),T("marcher sur le lit","le chien","female"),T("se cacher le visage","la femme","female")],
 nouns=[N("l'oreiller","female"),N("le chien","female"),N("la couette","female"),N("la porte","female")],
 question="Que fait le chien ?",answer="Le chien réveille la femme.".split(),answerVoice="female",
 recall=[R("taps",("dormir",["dormir"]),"dans son lit"),R("taps","marcher sur le",("lit",["lit"])),
         R("taps","se cacher le",("visage",["visage"])),R("answer",("réveille",["réveille"]),"la femme")],
 notes="'a blanket' is a duvet in the clip: 'la couette' is the everyday French word. Phrase 3: she hides her face in her hands, so 'se cacher le visage' (English 'cover').")
for i,d in D.items():
    o={"mediaId":i,"lang":"fr","level":d["level"],"keyWord":d["keyWord"],"taps":d["taps"],"nouns":d["nouns"],"question":d["question"],
       "answer":d["answer"],"answerVoice":d["answerVoice"],"carousel":[],"recall":d["recall"],"notes":d["notes"]}
    json.dump(o,open(f'content/fr/{i}.json','w'),ensure_ascii=False,indent=1)
