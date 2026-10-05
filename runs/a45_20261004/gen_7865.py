import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
man=[(.41,.25,.36,.27),(.41,.25,.36,.27),(.41,.25,.37,.28),(.44,.27,.37,.26),(.41,.25,.40,.27),(.44,.25,.37,.27),(.46,.25,.36,.28),(.48,.25,.37,.28)]
wom=[(.07,.24,.33,.28),(.06,.24,.34,.28),(.06,.24,.34,.28),(.06,.23,.35,.29),(.06,.24,.34,.28),(.07,.24,.34,.28),(.13,.24,.31,.28),(.18,.24,.29,.28)]
fire=[(.32,.52,.36,.22),(.31,.52,.38,.22),(.30,.53,.38,.22),(.31,.54,.38,.21),(.30,.53,.38,.22),(.31,.53,.39,.22),(.30,.53,.39,.22),(.31,.53,.40,.22)]
k=lambda L:[{"t":t,"x":a,"y":b,"w":c,"h":d} for t,(a,b,c,d) in zip(T,L)]
c={"mediaId":7865,"level":"A","keyWord":"heating","defaultVoice":"male",
"taps":[{"phrase":"to hold some wood","target":"the man in brown","voice":"male","keys":k(man)},
{"phrase":"to hold her hat","target":"the woman in blue","voice":"female","keys":k(wom)},
{"phrase":"to burn brightly","target":"the fire","voice":"male","keys":k(fire)}],
"stillS":3.2,
"nouns":[{"word":"the sky","x":0.50,"y":0.08,"voice":"male"},{"word":"trees","x":0.88,"y":0.40,"voice":"male"},
{"word":"a fire","x":0.50,"y":0.70,"voice":"male"},{"word":"shoes","x":0.40,"y":0.93,"voice":"male"}],
"question":"What is the woman in blue doing?","answer":["She","is","holding","her","hat."],"answerVoice":"female",
"notes":"Man in brown holds the log only 0.2-1.7 s (puts it on the fire at 1.7 s). Fire box partly covered by the viewer's mittens. Woman in blue keeps both hands on her woolly hat the whole clip. 'shoes' = the viewer's trainers at the bottom (pill on the left one). Key word 'heating' not a visible noun, so not used."}
json.dump(c,open('content/7865.json','w'),indent=1)
