import json
T=[0.2,0.7,1.2,1.7,2.2,2.7]
def K(rows): return [dict(t=t,**dict(zip('xywh',r))) if r else {"t":t,"off":True} for t,r in zip(T,rows)]
man=K([(.63,.31,.27,.55),(.63,.31,.28,.55),(.64,.31,.28,.56),(.71,.35,.26,.52),(.70,.36,.25,.51),(.73,.37,.23,.50)])
woman=K([(.42,.65,.20,.35),(.43,.65,.19,.35),(.46,.64,.17,.36),(.50,.66,.20,.34),(.50,.67,.19,.33),(.53,.68,.19,.32)])
mob=K([(.03,0,.57,.64),(.23,0,.39,.62),(.02,0,.61,.60),(.17,0,.53,.62),(.38,0,.28,.62),(0,0,.72,.62)])
c={"mediaId":7364,"level":"A","keyWord":"mobile","defaultVoice":"male",
"taps":[{"phrase":"to stand on a ladder","target":"the man on the ladder","voice":"male","keys":man},
{"phrase":"to hold the ladder","target":"the woman in black","voice":"female","keys":woman},
{"phrase":"to turn in the air","target":"the mobile","voice":"male","keys":mob}],
"stillS":2.7,
"nouns":[{"word":"a glass roof","x":.30,"y":.10,"voice":"male"},{"word":"a mobile","x":.55,"y":.47,"voice":"male"},
{"word":"a tool bag","x":.90,"y":.72,"voice":"male"},{"word":"a ladder","x":.86,"y":.92,"voice":"male"}],
"question":"What is the mobile doing?","answer":["It","is","turning","in","the","air."],"answerVoice":"male",
"notes":"The mobile (hanging sculpture) is spread over the whole upper picture and touches the man; its box covers the main part of the sculpture and stops above the woman's head and left of the man, so the outer discs near his head (1.7 s) and the top-right discs at 0.2 s are cut. Man and woman boxes are split where her arm reaches the ladder beside his legs, so her arm and his outer hand are cut. Two visitors watch from the balcony inside the mobile box (not targets). Question asks about the mobile because two men and two women are visible."}
json.dump(c,open('content/7364.json','w'),indent=1)
