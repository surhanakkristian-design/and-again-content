from gen_7943_7944_7945_7947_lib import *
R=[(.06,.29,.32,.58),(.04,.29,.31,.58),(0,.29,.31,.61),(0,.30,.31,.62),(0,.31,.35,.63),(0,.31,.34,.63),(0,.33,.52,.69),(0,.36,.64,.69)]
W=[(.53,.29,.92,.90),(.54,.27,.95,.93),(.56,.28,.99,.99),(.58,.26,1.0,1.0),(.62,.24,1.0,1.0),(.58,.26,1.0,1.0),(.62,.27,1.0,1.0),(.66,.24,1.0,1.0)]
r=keys(R)
write(7947,{"mediaId":7947,"level":"B","keyWord":"pound","defaultVoice":"female",
"taps":[{"phrase":"to lean across the scale","target":"the raccoon","voice":"female","keys":r},
 {"phrase":"to carry a wicker basket","target":"the woman","voice":"female","keys":keys(W)},
 {"phrase":"to snatch the butter","target":"the raccoon","voice":"female","keys":r}],
"stillS":0.7,
"nouns":[{"word":"a wall lamp","x":0.15,"y":0.11,"voice":"female"},{"word":"a raccoon","x":0.16,"y":0.40,"voice":"female"},{"word":"a brass scale","x":0.40,"y":0.31,"voice":"female"},{"word":"butter","x":0.52,"y":0.49,"voice":"female"},{"word":"a wicker basket","x":0.79,"y":0.61,"voice":"female"}][1:],
"question":"What is the woman carrying?","answer":["She","is","carrying","a","wicker","basket."],"answerVoice":"female",
"notes":"Raccoon only leans across the scale from ~2.2 and grabs the butter at 3.2-3.7 (paw on the block at 3.7); earlier it stands beside the scale. Two raccoon phrases share its keys. Woman leans on the counter and laughs, covers her mouth at 3.2-3.7; basket on her arm throughout (partly cut at the right edge late). Key word 'pound' (unit of weight) is not a visible object; the brass weight is on the left pan."})
