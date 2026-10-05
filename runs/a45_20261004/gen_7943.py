from gen_7943_7944_7945_7947_lib import *
W=[(.18,.33,.70,.89),(.18,.33,.70,.89),(.18,.33,.70,.95),(.18,.33,.70,.95),(.18,.30,.71,.94),(.18,.30,.73,.95),(.17,.30,.56,.97),(.16,.29,.52,.97)]
M=[(0,.39,.18,.68)]*6+[(0,.39,.17,.70),(0,.39,.16,.70)]
w=keys(W); m=keys(M)
write(7943,{"mediaId":7943,"level":"A","keyWord":"point","defaultVoice":"female",
"taps":[{"phrase":"to hold the chalk","target":"the woman","voice":"female","keys":w},
 {"phrase":"to rub her hands","target":"the woman","voice":"female","keys":w},
 {"phrase":"to hold a long stick","target":"the man","voice":"male","keys":m}],
"stillS":3.7,
"nouns":[{"word":"a point","x":0.72,"y":0.40,"voice":"female"},{"word":"a board","x":0.80,"y":0.22,"voice":"female"},{"word":"a woman","x":0.34,"y":0.62,"voice":"female"}],
"question":"What is the woman holding?","answer":["She","is","holding","a","piece","of","chalk."],"answerVoice":"female",
"notes":"Woman presses chalk into one point on the board (0.2-2.7), then steps back and rubs/brushes her hands (3.2-3.7). Man at far left edge holds the long wooden pointer; his box is split from the woman's at x=0.18 so her back leg/jacket edge is cut slightly. Girl next to him not used. 'to hold the chalk' is weaker at 3.2-3.7 (chalk not clearly in hand). Key word 'a point' = the spot where the chalk lines meet."})
