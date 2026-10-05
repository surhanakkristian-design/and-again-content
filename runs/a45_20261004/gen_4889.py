import json
T=[i*0.5 for i in range(19)]
W={0.0:(0,.27,.90,.73),0.5:(.02,.25,.92,.75),1.0:(0,.35,1,.65),1.5:(0,.19,1,.81),2.0:(0,.17,1,.83),2.5:(0,.16,1,.84),
3.0:(.20,.28,.80,.72),3.5:(.07,.35,.66,.63),4.0:(.30,.39,.32,.35),4.5:(.32,.40,.35,.30),5.0:(.27,.34,.31,.24),6.0:(.35,.36,.18,.17)}
M={4.0:(.62,.18,.38,.82),4.5:(.67,.26,.33,.56),5.0:(.60,.30,.36,.52),5.5:(.58,.30,.27,.40),6.0:(.53,.38,.18,.23),6.5:(.46,.37,.18,.18)}
def keys(D): return [dict(t=t,x=D[t][0],y=D[t][1],w=D[t][2],h=D[t][3]) if t in D else dict(t=t,off=True) for t in T]
kw=keys(W); km=keys(M)
d={"mediaId":4889,"level":"B","keyWord":"circular","defaultVoice":"female",
"taps":[{"phrase":"to spin on a stool","target":"the woman on the stool","voice":"female","keys":kw},
{"phrase":"to toss her long hair","target":"the woman on the stool","voice":"female","keys":kw},
{"phrase":"to wear a beige T-shirt","target":"the man in beige","voice":"male","keys":km}],
"stillS":7.0,
"nouns":[{"word":"lights","x":0.50,"y":0.06,"voice":"female"},{"word":"a crowd","x":0.40,"y":0.47,"voice":"female"},
{"word":"a sofa","x":0.51,"y":0.75,"voice":"female"},{"word":"the floor","x":0.50,"y":0.91,"voice":"female"}],
"question":"What is the woman in white doing?",
"answer":["She","is","spinning","on","a","stool."],"answerVoice":"female",
"notes":"From 7.0 s the shot is a wide overhead view of dozens of tiny dancers: the woman on the stool is off from 5.5 s (except a tiny figure at 6.0 s) and the man in beige off from 7.0 s, both too small to tap. At 3.5 s only pointing hands, man off. At 4.0-6.0 s the man's pointing arm reaches over the woman: his box covers his body only, split from hers. The woman in brown also points and laughs, so the man got a state phrase (beige T-shirt) rather than an action. 'circular' is an adjective: the circular white platform is covered by the crowd, so no noun for it; 'a crowd' labels the dancers on it."}
json.dump(d,open("content/4889.json","w"),indent=1)
