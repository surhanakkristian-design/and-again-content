import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]}) for t,r in zip(T,rows)]
run=K([(.38,.34,.40,.56),(.36,.34,.40,.57),(.37,.35,.40,.62),(.38,.41,.40,.57),(.35,.44,.46,.52),(.37,.42,.44,.52),(.40,.39,.40,.58),(.44,.38,.40,.59)])
stw=K([(0,.36,.25,.40),(0,.36,.24,.40),(0,.35,.24,.43),(0,.35,.24,.43),(0,.28,.34,.47),(0,.26,.36,.52),(.05,.25,.35,.55),(.08,.24,.36,.56)])
c={"mediaId":6969,"level":"B","keyWord":"come through","defaultVoice":"female",
"taps":[{"phrase":"to hug a border collie","target":"the runner","voice":"female","keys":run},
{"phrase":"to kneel on wet cobbles","target":"the runner","voice":"female","keys":run},
{"phrase":"to drape a foil blanket","target":"the steward","voice":"male","keys":stw}],
"stillS":2.2,
"nouns":[{"word":"a mountain","x":0.45,"y":0.18,"voice":"female"},{"word":"a foil blanket","x":0.17,"y":0.53,"voice":"female"},
{"word":"a border collie","x":0.68,"y":0.62,"voice":"female"},{"word":"a cup","x":0.33,"y":0.91,"voice":"female"}],
"question":"What is the runner doing?","answer":["She","is","hugging","a","border","collie."],"answerVoice":"female",
"notes":"The steward is a man (orange vest, cap), at the left edge 0.2-1.7 holding the gold blanket, then he drapes it over the runner (2.7-3.7). At 2.7-3.7 his head/arms come over the runner's head: boxes split vertically between his body and her head, so his hands and the blanket on her shoulders fall in her box. The runner stands at 0.2-1.2 and kneels from 1.7. A second crumpled foil blanket lies on the ground right; the 'a foil blanket' pill is on the one the steward holds."}
json.dump(c,open('content/6969.json','w'),indent=1)
