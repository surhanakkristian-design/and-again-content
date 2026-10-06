import json
def g(t,acc=None): return {"text":t,"gap":True,"accept":acc or [t]}
def p(t): return {"text":t}
T=lambda ph,t,v:dict(phrase=ph,target=t,voice=v)
N=lambda w,v:dict(word=w,voice=v)
D={}
D[34]=dict(mediaId=34,lang="fr",level="A",keyWord="une activité",
 taps=[T("porter un tee-shirt blanc","la femme","female"),T("avoir une barbe courte","l'homme","male"),T("courir à quatre pattes","le chien","female")],
 nouns=[N("le chien","female"),N("l'homme","male"),N("la femme","female"),N("l'herbe","female")],
 question="Que font l'homme et la femme ?",
 answer=["Ils","jouent","au","badminton","sur","l'herbe."],answerVoice="female",carousel=[],
 recall=[dict({"from":"taps"},parts=[p("porter un"),g("tee-shirt",["tee-shirt","t-shirt"]),p("blanc")]),
         dict({"from":"taps"},parts=[p("avoir une"),g("barbe"),p("courte")]),
         dict({"from":"taps"},parts=[g("courir"),p("à quatre pattes")]),
         dict({"from":"answer"},parts=[p("jouent au"),g("badminton"),p("sur l'herbe")])],
 notes="keyWord 'une activité' copied unchanged (indefinite article in the database word, unlike the other nouns). It is not a visible thing and not a noun of the set, so no noun row; the activity shown is badminton. The man wears a light blue T-shirt, so the white T-shirt fits only the woman. Blue box (dog) is OFF until the last frames; the man crawls on all fours earlier, but never while the dog box is on. 'l'herbe' is elided, so the answer row gaps 'badminton'.")
D[35]=dict(mediaId=35,lang="fr",level="A",keyWord="un acteur",
 taps=[T("pleurer et crier","le jeune homme","male"),T("filmer avec la caméra","l'homme à la caméra","male"),T("applaudir l'acteur","l'homme à la casquette","male")],
 nouns=[N("le micro","male"),N("la caméra","male"),N("l'acteur","male"),N("la chaise","male")],
 question="Que fait l'acteur ?",
 answer=["Il","pleure","devant","la","caméra."],answerVoice="male",carousel=[],
 recall=[dict({"from":"taps"},parts=[p("pleurer et"),g("crier",["crier","hurler"])]),
         dict({"from":"taps"},parts=[g("filmer"),p("avec la caméra")]),
         dict({"from":"taps"},parts=[g("applaudir"),p("l'acteur")]),
         dict({"from":"answer"},parts=[g("pleure",["pleure","crie"]),p("devant la caméra")])],
 notes="Tap box 1 also covers the make-up, the walk to the mark and the final laughing/bowing; the phrase describes the main scene. Phrase 2: the camera stands on a tripod, so 'filmer avec la caméra' rather than holding a big camera. The man in the cap sits and watches in about half of his boxed frames and claps at the end; 'applaudir l'acteur' is his distinctive action. 'le micro' = everyday word for the boom microphone. The key word is in tap row 3 but elided ('l'acteur'), so it cannot be a gap; no noun row because row 3 contains it.")
D[37]=dict(mediaId=37,lang="fr",level="B",keyWord="avancer",
 taps=[T("flotter au sommet","le drapeau","male"),T("saisir le mât du drapeau","l'alpiniste en rouge","male"),T("avoir une barbe fournie","l'alpiniste en bleu","male")],
 nouns=[N("le drapeau","male"),N("les pics","male"),N("les lunettes de ski","male"),N("la corde","male")],
 question="Que font les trois alpinistes ?",
 answer=["Ils","avancent","vers","le","sommet","enneigé."],answerVoice="male",carousel=[],
 recall=[dict({"from":"taps"},parts=[g("flotter"),p("au sommet")]),
         dict({"from":"taps"},parts=[p("saisir le"),g("mât",["mât","hampe"]),p("du drapeau")]),
         dict({"from":"taps"},parts=[p("avoir une barbe"),g("fournie",["fournie","touffue","épaisse"])]),
         dict({"from":"answer"},parts=[g("avancent",["avancent","progressent","montent"]),p("vers le sommet enneigé")])],
 notes="The climber in red looks female; 'l'alpiniste' is epicene, voice stays male as in English. Tap box 2 mostly shows her climbing; she grasps the flagpole only near the top. Peaks = 'les pics' so that 'le sommet' stays the one summit they reach. Goggles = 'les lunettes de ski' (everyday word; 'le masque de ski' also used in France). B words: flotter, saisir, barbe fournie, enneigé. Key word 'avancer' is the answer verb and its gap.")
D[39]=dict(mediaId=39,lang="fr",level="A",keyWord="une ambulance",
 taps=[T("regarder l'ambulance","l'homme en noir","male"),T("s'arrêter près du café","l'ambulance","male"),T("porter un sac rouge","l'homme en jaune","male")],
 nouns=[N("le ciel","male"),N("les maisons","male"),N("l'ambulance","male"),N("le sac","male")],
 question="Que fait l'homme en noir ?",
 answer=["Il","regarde","l'ambulance","arriver."],answerVoice="male",carousel=[],
 recall=[dict({"from":"taps"},parts=[g("regarder",["regarder","observer"]),p("l'ambulance")]),
         dict({"from":"taps"},parts=[p("s'arrêter près du"),g("café")]),
         dict({"from":"taps"},parts=[p("porter un"),g("sac"),p("rouge")]),
         dict({"from":"answer"},parts=[p("regarde l'ambulance"),g("arriver")])],
 notes="'arriver' added to the answer so its row differs from tap row 1 once the gap is blanked; he watches while it drives up. The woman paramedic also wears yellow but carries nothing, so the red bag fits only the man in yellow. Tap box 2 covers the ambulance driving up and standing parked. The key word is always elided ('l'ambulance'), so it cannot be a gap; no noun row because other rows contain it.")
D[40]=dict(mediaId=40,lang="fr",level="A",keyWord="la réponse",
 taps=[T("tirer une carte","la femme","female"),T("être posées sur la table","les cartes","female"),T("montrer une carte","la femme","female")],
 nouns=[N("les cheveux","female"),N("le pull","female"),N("la carte","female"),N("la table","female")],
 question="Que montre la femme ?",
 answer=["Elle","montre","une","carte."],answerVoice="female",carousel=[],
 recall=[dict({"from":"taps"},parts=[g("tirer",["tirer","choisir","prendre"]),p("une carte")]),
         dict({"from":"taps"},parts=[p("être posées sur la"),g("table")]),
         dict({"from":"taps"},parts=[p("montrer une"),g("carte")]),
         dict({"from":"answer"},parts=[p("montre une"),g("carte")])],
 notes="'tirer une carte' is the native collocation for drawing a card. Key word 'la réponse' is not a noun of the set (the card is her answer), so no noun row. English 'hair' -> 'les cheveux' (French uses the plural). Tap boxes 1 and 3 also cover opening frames where only the table and the card stack are visible. Gaps chosen so tap row 1 and the answer row do not look the same once blanked.")
for i,d in D.items():
    json.dump(d,open(f"content/fr/{i}.json","w"),ensure_ascii=False,indent=1)
