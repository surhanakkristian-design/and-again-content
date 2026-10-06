import json
def P(t,gap=False,acc=None):
    d={"text":t}
    if gap: d["gap"]=True; d["accept"]=acc or [t]
    return d
def T(*parts): return {"from":"taps","parts":list(parts)}
def A(*parts): return {"from":"answer","parts":list(parts)}
files={}
files[5288]={"mediaId":5288,"lang":"fr","level":"A","keyWord":"le ski",
 "taps":[{"phrase":"descendre la piste à ski","target":"le skieur en rouge","voice":"male"},
         {"phrase":"être habillé en rouge","target":"le skieur en rouge","voice":"male"},
         {"phrase":"sauter en l'air","target":"le skieur en rouge","voice":"male"}],
 "nouns":[{"word":"les skis","voice":"male"},{"word":"les montagnes","voice":"male"},{"word":"le ciel","voice":"male"},{"word":"la neige","voice":"male"}],
 "question":"Que fait le skieur en rouge ?",
 "answer":["Il","descend","la","piste","à","ski."],"answerVoice":"male","carousel":[],
 "recall":[T(P("descendre la piste à"),P("ski",True)),
           T(P("être"),P("habillé",True,["habillé"]),P("en rouge")),
           T(P("sauter",True),P("en l'air")),
           A(P("descend la"),P("piste",True,["piste","pente"]),P("à ski"))],
 "notes":"Level A: 'combinaison' (suit) is above A2, so phrase 2 says 'être habillé en rouge' (A2 words, fits only the skier in red). 'piste' used for the slope (A2 in a ski context); answer row also accepts 'pente'. Phrase 3 'sauter en l'air' is only visible in the jump frames (box_04); in the other boxed frames he carves down the piste. Other skiers in the background also ski, as in English. No noun row: the key word 'ski' is already in tap row 1 and the answer row."}
files[7811]={"mediaId":7811,"lang":"fr","level":"B","keyWord":"les dizaines",
 "taps":[{"phrase":"donner un coup de raquette","target":"la femme en blanc","voice":"female"},
         {"phrase":"s'emparer du lance-balles","target":"l'homme en vert","voice":"male"},
         {"phrase":"projeter des dizaines de balles","target":"le lance-balles","voice":"female"}],
 "nouns":[{"word":"les nuages","voice":"female"},{"word":"le lance-balles","voice":"female"},{"word":"la raquette","voice":"female"},{"word":"les balles de tennis","voice":"female"}],
 "question":"Que fait le lance-balles ?",
 "answer":["Il","projette","des","dizaines","de","balles","de","tennis."],"answerVoice":"female","carousel":[],
 "recall":[T(P("donner un coup de"),P("raquette",True)),
           T(P("s'emparer du"),P("lance-balles",True)),
           T(P("projeter des"),P("dizaines",True),P("de balles")),
           A(P("projette",True,["projette","lance","envoie"]),P("des dizaines de balles de tennis"))],
 "notes":"Phrase 1: the woman swings her racket at the balls in the early boxed frames; later she only holds it and laughs. Other players at the far fence carry rackets but do not swing them. 'le lance-balles' is the usual French word for a tennis ball machine. Answer subject 'Il' = le lance-balles; answerVoice kept female as in English (thing, not a person)."}
files[526]={"mediaId":526,"lang":"fr","level":"B","keyWord":"paralyser",
 "taps":[{"phrase":"faire feu avec un pistolet à rayons","target":"la femme","voice":"female"},
         {"phrase":"serrer une tasse blanche","target":"l'homme","voice":"male"},
         {"phrase":"basculer en arrière","target":"l'homme","voice":"male"}],
 "nouns":[{"word":"les lunettes de protection","voice":"female"},{"word":"le cactus","voice":"female"},{"word":"le survêtement","voice":"female"},{"word":"le tuyau","voice":"female"}],
 "question":"Que fait la femme ?",
 "answer":["Elle","le","paralyse","avec","un","pistolet","à","rayons."],"answerVoice":"female","carousel":[],
 "recall":[T(P("faire feu avec un"),P("pistolet",True),P("à rayons")),
           T(P("serrer une"),P("tasse",True,["tasse","mug"]),P("blanche")),
           T(P("basculer",True,["basculer","tomber"]),P("en arrière")),
           A(P("le"),P("paralyse",True),P("avec un pistolet à rayons"))],
 "notes":"Phrase 1: she fires only at the start (box_01); in most red-boxed frames she holds the gun, then waves at and catches the frozen man - phrase kept as English. Phrase 3: the man only tips over backwards at the end (box_05-06); in most blue-boxed frames he stands frozen. The mug ('la tasse', 'mug' also accepted) is visible in his hand until he falls. 'pistolet à rayons' = sci-fi ray gun."}
files[517]={"mediaId":517,"lang":"fr","level":"B","keyWord":"doubler",
 "taps":[{"phrase":"doubler un camping-car","target":"le cabriolet rouge","voice":"male"},
         {"phrase":"se rabattre devant le camping-car","target":"le cabriolet rouge","voice":"male"},
         {"phrase":"se faire distancer par le cabriolet","target":"le camping-car","voice":"male"}],
 "nouns":[{"word":"le camping-car","voice":"male"},{"word":"le cabriolet","voice":"male"},{"word":"les dunes","voice":"male"},{"word":"la route","voice":"male"}],
 "question":"Que fait le cabriolet rouge ?",
 "answer":["Il","double","un","camping-car."],"answerVoice":"male","carousel":[],
 "recall":[T(P("doubler",True,["doubler","dépasser"]),P("un camping-car")),
           T(P("se"),P("rabattre",True),P("devant le camping-car")),
           T(P("se faire distancer par le"),P("cabriolet",True)),
           A(P("double un"),P("camping-car",True))],
 "notes":"The red car is called 'le cabriolet' everywhere (noun 2 = convertible) so the same thing keeps one word; question says 'le cabriolet rouge' instead of 'la voiture rouge'. 'la route' for the two-lane desert highway (not an autoroute). Phrase 2: in the early boxed frames the convertible is still alongside; it pulls in ahead in the later ones."}
files[8027]={"mediaId":8027,"lang":"fr","level":"B","keyWord":"les tonnes",
 "taps":[{"phrase":"rouler en trottinette","target":"l'homme","voice":"male"},
         {"phrase":"lever les bras au ciel","target":"l'homme","voice":"male"},
         {"phrase":"se pencher pour regarder","target":"la femme","voice":"female"}],
 "nouns":[{"word":"le chapeau de paille","voice":"male"},{"word":"le plafonnier","voice":"male"},{"word":"la trottinette","voice":"male"},{"word":"les balles en plastique","voice":"male"}],
 "question":"Que fait l'homme ?",
 "answer":["Il","roule","en","trottinette","au","milieu","de","tonnes","de","balles."],"answerVoice":"male","carousel":[],
 "recall":[T(P("rouler en"),P("trottinette",True)),
           T(P("lever les"),P("bras",True),P("au ciel")),
           T(P("se"),P("pencher",True),P("pour regarder")),
           A(P("roule en trottinette au milieu de"),P("tonnes",True),P("de balles"))],
 "notes":"Phrase 3: the woman covers her mouth only in the first boxed frames; in most of them she leans out from behind the glass to watch him, laughing - so 'se pencher pour regarder' instead of 'pouffer derrière ses mains' (the man laughs too, so a plain 'rire' would not fit only her). 'des tonnes de' (key word) is informal but standard. Answer: 'en trottinette' and 'au milieu de tonnes de balles' could in theory swap; the given order is the natural one."}
for k,v in files.items():
    json.dump(v,open(f"content/fr/{k}.json","w"),ensure_ascii=False,indent=2)
