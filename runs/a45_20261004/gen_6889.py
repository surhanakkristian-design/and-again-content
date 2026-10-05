import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) if r else {"t":t,"off":True} for t,r in zip(T,rows)]
woman=K([(.28,.19,.37,.63),(.35,.19,.29,.62),(.33,.19,.30,.62),(.35,.19,.29,.62),(.37,.19,.29,.66),(.44,.18,.34,.66),(.44,.18,.38,.70),(.49,.18,.34,.75)])
man=K([(.65,.34,.25,.28),(.64,.34,.25,.28),(.63,.35,.24,.26),(.64,.35,.24,.26),(.66,.36,.21,.26),(.78,.38,.18,.22),None,None])
d={"mediaId":6889,"level":"B","keyWord":"brain","defaultVoice":"female",
"taps":[{"phrase":"to stride along the table","target":"the woman","voice":"female","keys":woman},
{"phrase":"to point at the chessboards","target":"the woman","voice":"female","keys":woman},
{"phrase":"to clutch his head","target":"the standing man","voice":"male","keys":man}],
"stillS":0.7,
"nouns":[{"word":"a chandelier","x":.12,"y":.14,"voice":"female"},{"word":"a blindfold","x":.50,"y":.23,"voice":"female"},
{"word":"a curtain","x":.85,"y":.15,"voice":"female"},{"word":"a chess clock","x":.63,"y":.86,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","striding","along","the","long","table."],"answerVoice":"female",
"notes":"Key word 'brain' is not a visible noun, so not among the nouns. Standing man clutches his head 0.2-1.2, hands drop to his chest from 1.7; mostly hidden behind the woman at 2.7 (box on the visible part to her right), off at 3.2-3.7. Woman/man boxes split at her right hand (x ~0.64). 'to stride' is a slow walk here - 'to walk along the table' would be the safer fallback."}
json.dump(d,open("content/6889.json","w"),indent=1)
