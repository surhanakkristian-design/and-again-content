import json
T=[i*0.5 for i in range(25)]
D=[(.20,.09,.57,.48),(.20,.10,.40,.47),(.20,.14,.21,.44),(.20,.14,.19,.44),(.18,.15,.18,.44)]+[None]*20
H=[None,(.61,.27,.19,.30),(.42,.29,.32,.28),(.40,.28,.34,.30),(.37,.23,.35,.36),
(.43,.17,.57,.83),(.45,.20,.55,.80),(.44,.20,.56,.80),(.55,.21,.45,.79),(.51,.23,.49,.77),(.62,.28,.38,.72),(.69,.35,.31,.65),(.76,.31,.24,.69),(.62,.28,.38,.72),(.58,.39,.42,.61),
(0,.25,.46,.75),(0,.27,.49,.73),(0,.29,.54,.71),(0,.33,.50,.67),(0,.33,.50,.67),(0,.33,.50,.67),(0,.34,.50,.66),(0,.36,.50,.64),(0,.37,.51,.63),(0,.37,.50,.63)]
F=[None]*5+[(.10,.15,.32,.27),(.04,.18,.40,.36),(.06,.26,.37,.42),(.13,.27,.41,.39),(.08,.28,.42,.41),(.16,.27,.45,.38),(.18,.28,.50,.41),(.26,.31,.49,.32),(.08,.28,.52,.38),(.06,.28,.51,.37),
(.47,.33,.30,.65),(.50,.35,.27,.62),(.55,.33,.25,.57),(.52,.35,.32,.61),(.55,.36,.34,.62),(.55,.37,.37,.61),(.56,.38,.39,.62),(.58,.40,.41,.60),(.63,.41,.37,.59),(.57,.41,.43,.59)]
def keys(B):
    return [{"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,B)]
c={"mediaId":4377,"level":"B","keyWord":"basement","defaultVoice":"male",
"taps":[{"phrase":"to grin at the camera","target":"the man in the hoodie","voice":"male","keys":keys(H)},
{"phrase":"to hug himself and shiver","target":"the man in the T-shirt","voice":"male","keys":keys(F)},
{"phrase":"to swing open slowly","target":"the door","voice":"male","keys":keys(D)}],
"stillS":12.0,
"nouns":[{"word":"a projector","x":.66,"y":.29,"voice":"male"},{"word":"a screen","x":.27,"y":.37,"voice":"male"},{"word":"a popcorn machine","x":.68,"y":.41,"voice":"male"},{"word":"armchairs","x":.52,"y":.54,"voice":"male"}],
"question":"What is the grinning man doing?","answer":["He","is","showing","his","friend","the","basement."],"answerVoice":"male",
"notes":"In the storeroom shots the two men overlap in the picture: the hoodie man's box starts at his head/hood, his near shoulder and arm (below the friend's crossed arms) are left out so the boxes do not overlap. From 7.5 s both are seen from behind; at 8.0-9.0 the hoodie man's stretched arm crosses the friend's box. The door is only in the first shot (0-2 s). 'his friend' in the answer is an assumption from the description. Pills 'a screen' and 'a popcorn machine' are close (dx 0.41, dy 0.04)."}
json.dump(c,open('content/4377.json','w'),indent=1)
