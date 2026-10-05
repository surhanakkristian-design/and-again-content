import json
T=[round(i*0.5,1) for i in range(19)]
def keys(d):
    return [dict(t=t,**dict(zip('xywh',d[t]))) if t in d else {'t':t,'off':True} for t in T]
woman={0.0:(.02,0,.98,1),0.5:(0,0,1,1),1.0:(0,.10,1,.90),1.5:(0,.18,1,.82),2.0:(.08,.24,.84,.71),2.5:(.17,.29,.66,.56),
 3.0:(.20,.33,.58,.52),3.5:(.27,.35,.46,.38),4.0:(.30,.37,.38,.30),4.5:(.32,.39,.34,.25),5.0:(.36,.47,.24,.16),
 5.5:(.40,.46,.18,.14),6.0:(.36,.45,.18,.14),6.5:(.39,.48,.18,.14)}
man={4.0:(.18,.72,.62,.28),4.5:(.22,.66,.51,.34),5.0:(.37,.64,.25,.22),5.5:(.40,.61,.18,.14),6.0:(.36,.60,.18,.14)}
c={"mediaId":4877,"level":"A","keyWord":"sit","defaultVoice":"female",
"taps":[
 {"phrase":"to close her eyes","target":"the woman in white","voice":"female","keys":keys(woman)},
 {"phrase":"to lean back in her seat","target":"the woman in white","voice":"female","keys":keys(woman)},
 {"phrase":"to wear a denim jacket","target":"the man in the front row","voice":"male","keys":keys(man)}],
"stillS":2.5,
"nouns":[{"word":"people","x":0.60,"y":0.08,"voice":"female"},
 {"word":"a jumper","x":0.50,"y":0.50,"voice":"female"},
 {"word":"jeans","x":0.55,"y":0.72,"voice":"female"},
 {"word":"a seat","x":0.50,"y":0.92,"voice":"female"}],
"question":"What is the woman in white doing?",
"answer":["She","is","sitting","in","her","seat."],
"answerVoice":"female",
"notes":"Woman in a cream jumper ('in white' for A level). She is off from 7.0 s: too tiny in the wide shot to tap. Man in glasses + denim jacket in the front row (4.0-6.0 s), off at 6.5 s where he is too small and too close to her. Lean back = 1.0-2.0 s; eyes closed 1.0-4.5 s, nobody else closes the eyes. Key word 'sit' is a verb, so it appears in the answer only."}
json.dump(c,open('content/4877.json','w'),indent=1)
