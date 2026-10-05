from gen_7943_7944_7945_7947_lib import *
W=[(.22,.28,.70,.62),(.22,.28,.72,.62),(.22,.28,.72,.64),(.22,.27,.73,.64),(.20,.24,.72,.62),(.20,.22,.72,.61),(.20,.24,.68,.62),(.20,.24,.70,.62)]
M=[(.70,.34,1.0,.63),(.74,.35,1.0,.63),(.73,.36,1.0,.66),(.75,.35,1.0,.66),(.73,.30,1.0,.62),(.73,.28,1.0,.64),(.69,.26,1.0,.66),(.70,.32,1.0,.74)]
C=[(.53,.63,.87,.91),(.56,.63,.89,.91),(.60,.66,.88,.99),(.62,.66,.90,.98),(.68,.63,.93,.98),(.68,.65,.94,1.0),None,None]
write(7945,{"mediaId":7945,"level":"B","keyWord":"poorly","defaultVoice":"female",
"taps":[{"phrase":"to spill the milk","target":"the woman with the jug","voice":"female","keys":keys(W)},
 {"phrase":"to wipe up the mess","target":"the man in brown","voice":"male","keys":keys(M)},
 {"phrase":"to leap off the counter","target":"the cat","voice":"female","keys":keys(C)}],
"stillS":3.7,
"nouns":[{"word":"a paper lamp","x":0.58,"y":0.06,"voice":"female"},{"word":"an apron","x":0.45,"y":0.52,"voice":"female"},{"word":"a cloth","x":0.60,"y":0.69,"voice":"female"},{"word":"spilt milk","x":0.40,"y":0.77,"voice":"female"}],
"question":"What is the man in brown doing?","answer":["He","is","wiping","up","the","spilt","milk."],"answerVoice":"male",
"notes":"Man's arm and the cloth reach left under the woman's waving hand; boxes split at x~0.70 and his box stops at the counter line in most frames so the cloth/hand is partly outside his box (at 3.7 his box goes down to 0.74 to the right of x 0.70). Cat is in front of the man's lower body, man's box ends where the cat's begins; cat gone at 3.2-3.7. Man also wears an apron (brown), so the woman is named by the jug, not the apron; the 'an apron' pill sits on her black apron. Key word 'poorly' is an adverb, not used as a noun."})
