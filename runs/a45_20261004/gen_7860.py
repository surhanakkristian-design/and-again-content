import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
man=[(.44,.36,.37,.46),(.40,.32,.41,.50),(.45,.33,.36,.50),(.46,.28,.36,.54),(.45,.25,.37,.60),(.41,.26,.34,.62),(.35,.20,.40,.68),(.30,.32,.47,.58)]
wom=[(.82,.40,.18,.34),(.82,.40,.18,.34),(.82,.39,.18,.37),(.82,.39,.18,.37),(.82,.38,.18,.39),(.76,.37,.21,.40),(.76,.37,.20,.42),(.78,.37,.20,.42)]
k=lambda L:[{"t":t,"x":a,"y":b,"w":c,"h":d} for t,(a,b,c,d) in zip(T,L)]
c={"mediaId":7860,"level":"A","keyWord":"hard","defaultVoice":"male",
"taps":[{"phrase":"to hit the tyre hard","target":"the man","voice":"male","keys":k(man)},
{"phrase":"to lift a heavy hammer","target":"the man","voice":"male","keys":k(man)},
{"phrase":"to stand and watch","target":"the woman","voice":"female","keys":k(wom)}],
"stillS":2.2,
"nouns":[{"word":"the sky","x":0.30,"y":0.12,"voice":"male"},{"word":"a hammer","x":0.30,"y":0.41,"voice":"male"},
{"word":"a woman","x":0.88,"y":0.55,"voice":"female"},{"word":"a tyre","x":0.40,"y":0.86,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","hitting","the","tyre","hard."],"answerVoice":"male",
"notes":"Only two people; man used for two phrases (hit / lift hammer). Man's right foot cut from his box where it is under the woman."}
json.dump(c,open('content/7860.json','w'),indent=1)
