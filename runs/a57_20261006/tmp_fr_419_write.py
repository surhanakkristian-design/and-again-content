import json
def P(*a):
    out=[]
    for x in a:
        if isinstance(x,tuple): out.append({"text":x[0],"gap":True,"accept":list(x)})
        else: out.append({"text":x})
    return out
def W(i,level,kw,taps,nouns,q,ans,av,rec,notes):
    d={"mediaId":i,"lang":"fr","level":level,"keyWord":kw,
       "taps":[{"phrase":p,"target":t,"voice":v} for p,t,v in taps],
       "nouns":[{"word":w,"voice":v} for w,v in nouns],
       "question":q,"answer":ans.split(" "),"answerVoice":av,"carousel":[],
       "recall":[{"from":f,"parts":P(*parts)} for f,parts in rec],"notes":notes}
    json.dump(d,open(f'content/fr/{i}.json','w'),ensure_ascii=False,indent=1)
W(419,"A","donner un coup de pied",
 [("porter un tee-shirt orange","la femme","female"),("porter un tee-shirt violet","l'homme","male"),("voler dans les airs","le ballon","male")],
 [("le ciel","male"),("les immeubles","male"),("la femme","female"),("le ballon","male")],
 "Que font-ils ?","Ils donnent des coups de pied dans le ballon.","male",
 [("taps",[("porter",),"un tee-shirt orange"]),("taps",["porter un tee-shirt",("violet",)]),("taps",["voler dans les",("airs",)]),
  ("answer",["donnent des coups de",("pied",),"dans le ballon"])],
 "Key word as plural 'des coups de pied' in the answer (repeated kicks). 'Ils' = mixed pair, male voice kept.")
W(383,"A","la randonnée",
 [("porter un sac à dos bleu","la femme","female"),("porter un sac à dos jaune","l'homme","male"),("voler au-dessus des montagnes","les oiseaux","male")],
 [("le ciel","male"),("les montagnes","male"),("la femme","female"),("l'herbe","male")],
 "Que font les deux personnes ?","Ils font de la randonnée en montagne.","male",
 [("taps",["porter un",("sac",),"à dos bleu"]),("taps",["porter un sac à dos",("jaune",)]),("taps",[("voler",),"au-dessus des montagnes"]),
  ("answer",["font de la",("randonnée",),"en montagne"])],
 "Phrase 2 changed: the man drinks from a bottle only in the last boxed frame; in most boxed frames he hikes with a yellow backpack, so 'porter un sac à dos jaune'. The woman's phrase is also true of the blue backpack only (his is yellow).")
W(13,"A","la serviette",
 [("plier une serviette","la femme","female"),("s'essuyer la bouche","la femme","female"),("s'asseoir sur une chaise","la femme","female")],
 [("la femme","female"),("la serviette","female"),("la chaise","female"),("la table","female")],
 "Que fait la femme ?","Elle plie une serviette.","female",
 [("taps",["plier une",("serviette",)]),("taps",["s'essuyer la",("bouche",)]),("taps",["s'asseoir sur une",("chaise",)]),
  ("answer",[("plie",),"une serviette"])],
 "All three taps target the same woman with the same boxes (as in English); each phrase is true only at its own moment. 'la serviette' = table napkin here (also means towel; the clip makes the sense clear).")
W(6949,"A","le chocolat chaud",
 [("verser du chocolat chaud","la femme","female"),("porter une robe dorée","la femme","female"),("boire dans une tasse","l'homme au bonnet","male")],
 [("le chocolat chaud","female"),("la robe","female"),("la main","female")],
 "Que fait la femme ?","Elle verse du chocolat chaud dans une tasse.","female",
 [("taps",["verser du",("chocolat",),"chaud"]),("taps",["porter une",("robe",),"dorée"]),("taps",[("boire",),"dans une tasse"]),
  ("answer",[("verse",),"du chocolat chaud dans une tasse"])],
 "English 'the man in the hat' wears a knitted beanie: target named 'l'homme au bonnet'. Many people in the crowd hold cups; the boxed man is the one drinking. The cup is a glass mug; 'tasse' is the natural word.")
W(330,"A","la porte",
 [("courir vers la porte d'embarquement","la fille","female"),("montrer son billet","la fille","female"),("tenir la porte ouverte","l'homme","male")],
 [("la fenêtre","female"),("la porte d'embarquement","female"),("la fille","female"),("la valise","female")],
 "Où court la fille ?","Elle court vers la porte d'embarquement.","female",
 [("taps",[("courir",),"vers la porte d'embarquement"]),("taps",["montrer son",("billet",)]),("taps",[("tenir",),"la porte ouverte"]),
  ("answer",["court vers la",("porte",),"d'embarquement"])],
 "Key word 'la porte' kept: alone it is ambiguous here (the plane door is also 'la porte', phrase 3), so the gate is 'la porte d'embarquement' in phrase 1, noun 2 and the answer; proposal: keyWord 'la porte d'embarquement'. Phrase 3: the man holds the plane door open only in the later boxed frames; earlier he scans her pass at the gate. 'son billet' kept at A level (strictly 'carte d'embarquement').")
