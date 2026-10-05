import json
T=[i*0.5 for i in range(21)]
def sp(s,wy,my,wx=0.0): return ((wx,wy,round(s-wx,2),round(1-wy,2)),(s,my,round(1-s,2),round(1-my,2)))
B=[sp(.60,.20,.14)]*5+[sp(.60,.20,.14)]*3+[sp(.61,.20,.14),sp(.62,.20,.14),sp(.57,.26,.28),sp(.60,.23,.18),sp(.58,.22,.17),sp(.58,.22,.17),sp(.57,.22,.15),sp(.53,.22,.28),sp(.57,.23,.18),sp(.61,.26,.26),sp(.52,.26,.26),
 ((0,.25,.40,.75),(.60,.21,.40,.79)),((0,.23,.35,.77),(.70,.20,.30,.80))]
def keys(i): return [{"t":t,"x":b[i][0],"y":b[i][1],"w":b[i][2],"h":b[i][3]} for t,b in zip(T,B)]
c={"mediaId":705,"level":"A","keyWord":"sneezing","defaultVoice":"female",
"taps":[{"phrase":"to smell the flowers","target":"the woman","voice":"female","keys":keys(0)},
{"phrase":"to touch her nose","target":"the woman","voice":"female","keys":keys(0)},
{"phrase":"to wear a grey hoodie","target":"the man","voice":"male","keys":keys(1)}],
"stillS":3.5,
"nouns":[{"word":"flowers","x":.58,"y":.57,"voice":"female"},{"word":"a jacket","x":.20,"y":.68,"voice":"female"},{"word":"a man","x":.83,"y":.45,"voice":"male"},{"word":"jeans","x":.30,"y":.91,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","smelling","the","flowers."],"answerVoice":"female",
"notes":"Both people sneeze into an arm, laugh and open their mouths, so no sneezing phrase (it would fit both); the man gets a state phrase because no action is his alone. Key word 'sneezing' is not a placeable noun and is not in the answer. She smells the flowers only at 0.0 s and touches her nose 1.0-2.0 s and 6.0-6.5 s. The bunch of flowers she holds reaches over the split line into the man's box by up to 0.1. 'flowers' sits on the bunch in her hands; more flowers are blurred in the background."}
json.dump(c,open('content/705.json','w'),indent=1)
