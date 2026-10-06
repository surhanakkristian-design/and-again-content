import json
def P(*a):
    out=[]
    for x in a:
        if isinstance(x,tuple): out.append({"text":x[0],"gap":True,"accept":list(x[1:]) if len(x)>1 else [x[0]]})
        else: out.append({"text":x})
    return out
def G(t,*acc): return (t,)+((t,)+acc if True else ())
V={}
V[203]=dict(level="B",keyWord="la croisière",
 taps=[("être vêtue d'une robe d'été jaune","la femme","female"),("arborer une chemise à fleurs","l'homme","male"),("bondir au-dessus des vagues","les dauphins","male")],
 nouns=[("le bateau de croisière","male"),("les dauphins","male"),("les îles","male"),("la mer","male")],
 question="Que fait le bateau de croisière ?",answer="Il longe des îles tropicales.",av="male",
 recall=[("taps",P("être vêtue d'une",G("robe"),"d'été jaune")),("taps",P(G("arborer","porter"),"une chemise à fleurs")),
  ("taps",P("bondir au-dessus des",G("vagues"))),("answer",P(G("longe","passe devant"),"des îles tropicales"))],
 notes="Key word la croisière is not itself a noun of the set; it appears inside the noun le bateau de croisière (and the question). B-level words: vêtue de, arborer, bondir, longer. Phrase 1 is in the feminine (être vêtue) because its target is the woman.")
V[204]=dict(level="B",keyWord="la béquille",
 taps=[("se déplacer à l'aide de béquilles","le garçon","male"),("tenir un porte-bloc","l'infirmière","female"),("brandir le poing","le garçon","male")],
 nouns=[("l'infirmière","female"),("la béquille","male"),("la botte orthopédique","male"),("la poignée de porte","male")],
 question="Que fait le garçon ?",answer="Il se déplace avec deux béquilles.",av="male",
 recall=[("taps",P("se",G("déplacer","marcher"),"à l'aide de béquilles")),("taps",P("tenir un",G("porte-bloc"))),
  ("taps",P(G("brandir","lever"),"le poing")),("answer",P("se déplace avec deux",G("béquilles")))],
 notes="No noun row: the key word (béquilles) is already in tap row 1 and the answer row. 'Medical boot' rendered as la botte orthopédique (also called botte de marche in France). Several nurses are visible behind the boy; the clipboard is held by the nurse on the left.")
V[205]=dict(level="A",keyWord="les pleurs",
 taps=[("s'essuyer les yeux","la femme","female"),("prendre la femme dans ses bras","l'homme","male"),("prendre un mouchoir","la femme","female")],
 nouns=[("la femme","female"),("l'homme","male"),("la couverture","female"),("les mouchoirs","female")],
 question="Que fait la femme ?",answer="Elle pleure et s'essuie les yeux.",av="female",
 recall=[("taps",P("s'essuyer les",G("yeux"))),("taps",P("prendre la femme dans ses",G("bras"))),
  ("taps",P("prendre un",G("mouchoir"))),("answer",P(G("pleure"),"et s'essuie les yeux"))],
 notes="Key word les pleurs: kept, but it is a B1+/written noun and not A-level French; at A level French teaches the verb pleurer (used in the answer: 'Elle pleure'). Proposal: le verbe pleurer, or 'les larmes' if a noun is needed. The man also tears up, but only the woman wipes her eyes and takes a tissue.")
V[206]=dict(level="A",keyWord="le concombre",
 taps=[("couper un concombre","l'homme","male"),("manger du concombre","la femme","female"),("regarder par-dessus la table","le chien","male")],
 nouns=[("la fenêtre","male"),("le concombre","male"),("la chemise","male"),("le chien","male")],
 question="Que fait l'homme ?",answer="Il coupe un concombre.",av="male",
 recall=[("taps",P("couper un",G("concombre"))),("taps",P(G("manger"),"du concombre")),
  ("taps",P("regarder par-dessus la",G("table"))),("answer",P(G("coupe"),"un concombre"))],
 notes="No noun row: le concombre is already in tap rows 1-2 and the answer. Gaps moved so row 1 (couper un ___) and the answer (___ un concombre) do not look alike. The dog peeks over the edge of the counter/table.")
V[207]=dict(level="A",keyWord="la tasse",
 taps=[("porter une boucle d'oreille verte","la femme","female"),("porter des lunettes","l'homme","male"),("porter un t-shirt bleu","l'homme","male")],
 nouns=[("le chat","female"),("la tasse","female"),("les fleurs","female"),("la théière","female")],
 question="Que fait la femme ?",answer="Elle boit du thé dans une tasse.",av="female",
 recall=[("taps",P("porter une",G("boucle d'oreille"),"verte")),("taps",P("porter des",G("lunettes"))),
  ("taps",P("porter un",G("t-shirt","tee-shirt"),"bleu")),("answer",P("boit du thé dans une",G("tasse")))],
 notes="The man's top is a short-sleeved blue T-shirt, so 'un t-shirt bleu' (English 'shirt'). The cups are small handleless tea bowls; la tasse is still the natural word. No noun row: la tasse is in the answer row.")
for i,v in V.items():
    d={"mediaId":i,"lang":"fr","level":v["level"],"keyWord":v["keyWord"],
       "taps":[{"phrase":p,"target":t,"voice":vo} for p,t,vo in v["taps"]],
       "nouns":[{"word":w,"voice":vo} for w,vo in v["nouns"]],
       "question":v["question"],"answer":v["answer"].split(),"answerVoice":v["av"],"carousel":[],
       "recall":[{"from":f,"parts":p} for f,p in v["recall"]],"notes":v["notes"]}
    json.dump(d,open(f"content/fr/{i}.json","w"),ensure_ascii=False,indent=1)
