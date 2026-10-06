import json
def P(t,g=None):
    # t list of (text, accept or None)
    return [ {"text":x} if a is None else {"text":x,"gap":True,"accept":a} for x,a in t]
def tap(p,t,v): return {"phrase":p,"target":t,"voice":v}
def N(w,v): return {"word":w,"voice":v}
D={}
D[15]=dict(level="A",keyWord="le cachet",
 taps=[tap("boire un verre d'eau","l'homme","male"),tap("verser de l'eau","la femme","female"),tap("être dans la main","le cachet","male")],
 nouns=[N("le cachet","male"),N("la main","male"),N("l'arbre","male")],
 question="Que fait l'homme ?",answer="Il prend un cachet avec de l'eau.".split(),answerVoice="male",
 recall=[("taps",[("boire un",None),("verre",["verre"]),("d'eau",None)]),
         ("taps",[("verser",["verser"]),("de l'eau",None)]),
         ("taps",[("être dans la",None),("main",["main"])]),
         ("answer",[("prend un",None),("cachet",["cachet","comprimé"]),("avec de l'eau",None)])],
 notes="Tap 1: the man's box also covers the opening frames where he holds his aching head; he drinks the glass of water later in the clip (same box as English).")
D[16]=dict(level="B",keyWord="la présentation",
 taps=[tap("faire une présentation devant la classe","l'étudiante en rouge","female"),tap("afficher les diapositives","l'écran","female"),tap("assister à la présentation","les camarades de classe","female")],
 nouns=[N("la présentation","female"),N("le pull","female"),N("le tableau blanc","female"),N("le public","female")],
 question="Que fait l'étudiante en rouge ?",answer="Elle fait une présentation devant ses camarades.".split(),answerVoice="female",
 recall=[("taps",[("faire",["faire"]),("une présentation devant la classe",None)]),
         ("taps",[("afficher les",None),("diapositives",["diapositives"])]),
         ("taps",[("assister",["assister"]),("à la présentation",None)]),
         ("answer",[("fait une",None),("présentation",["présentation"]),("devant ses camarades",None)])],
 notes="Tap 1: in the last close-up frames she stands smiling at the class rather than pointing at the slides (same box as English). The key word is also used in tap 3 (assister à la présentation), allowed by the owner decision.")
D[17]=dict(level="A",keyWord="le projet",
 taps=[tap("porter une casquette","l'homme à la casquette","male"),tap("avoir les cheveux longs","la femme","female"),tap("avoir un toit en bois","la cabane","male")],
 nouns=[N("le ciel","male"),N("le toit","male"),N("la porte","male"),N("l'herbe","male")],
 question="Que construisent les gens ?",answer="Ils construisent une cabane en bois.".split(),answerVoice="male",
 recall=[("taps",[("porter une",None),("casquette",["casquette"])]),
         ("taps",[("avoir les",None),("cheveux",["cheveux"]),("longs",None)]),
         ("taps",[("avoir un toit en",None),("bois",["bois"])]),
         ("answer",[("construisent",["construisent","bâtissent","montent"]),("une cabane en bois",None)])],
 notes="Key word le projet is not shown as a thing and appears in no exercise (as in English). 'la cabane' used for the shed (A-level everyday word; 'l'abri de jardin' is the more technical term).")
D[19]=dict(level="A",keyWord="la règle",
 taps=[tap("tracer une ligne","l'homme","male"),tap("avoir une couverture rouge","le livre","male"),tap("être longue et droite","la règle","male")],
 nouns=[N("la règle","male"),N("les lunettes","male"),N("le stylo","male"),N("la feuille","male")],
 question="Que fait l'homme ?",answer="Il trace une ligne avec une règle.".split(),answerVoice="male",
 recall=[("taps",[("tracer",["tracer","dessiner"]),("une ligne",None)]),
         ("taps",[("avoir une",None),("couverture",["couverture"]),("rouge",None)]),
         ("taps",[("être longue et",None),("droite",["droite"])]),
         ("answer",[("trace une ligne avec une",None),("règle",["règle"])])],
 notes="Tap 1: the man's box covers the whole clip; in most frames he tries the book, the calculator or searches under the desk, and he only draws the line with the ruler at the end (same box as English). English 'paper' = the sheet on the desk -> 'la feuille'.")
D[20]=dict(level="B",keyWord="un emploi du temps",
 taps=[tap("saisir l'oreiller","la main","female"),tap("être grand ouvert","le manuel","female"),tap("avoir deux bretelles qui traînent","le sac à dos","female")],
 nouns=[N("le manuel","female"),N("l'ordinateur portable","female"),N("le sac à dos","female"),N("l'oreiller","female")],
 question="Que fait la main ?",answer="Elle saisit l'oreiller sur le sol.".split(),answerVoice="female",
 recall=[("taps",[("saisir",["saisir","attraper"]),("l'oreiller",None)]),
         ("taps",[("être grand",None),("ouvert",["ouvert"])]),
         ("taps",[("avoir deux",None),("bretelles",["bretelles","sangles"]),("qui traînent",None)]),
         ("answer",[("saisit l'oreiller sur le",None),("sol",["sol","parquet"])])],
 notes="keyWord copied unchanged but it carries the indefinite article 'un'; proposal: 'l'emploi du temps' (definite, like the other database words). The schedule itself is not shown as a thing and appears in no exercise (as in English). Tap 1: in most boxed frames the hand hovers over the items; it grabs the pillow near the end.")
for i,d in D.items():
    out={"mediaId":i,"lang":"fr","level":d["level"],"keyWord":d["keyWord"],"taps":d["taps"],"nouns":d["nouns"],
         "question":d["question"],"answer":d["answer"],"answerVoice":d["answerVoice"],"carousel":[],
         "recall":[{"from":f,"parts":P(p)} for f,p in d["recall"]],"notes":d["notes"]}
    json.dump(out,open(f"content/fr/{i}.json","w"),ensure_ascii=False,indent=1)
