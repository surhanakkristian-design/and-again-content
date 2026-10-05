import json
M=[(.07,.24,.31,.26),(.05,.22,.36,.28),(.21,.32,.31,.36),(.27,.37,.31,.38),(.24,.33,.34,.58),(.25,.31,.33,.62),(.27,.29,.37,.56),(.33,.18,.33,.68),(.30,.17,.33,.54),(.27,.20,.33,.52),(.22,.25,.30,.60),(.20,.25,.27,.58),(.15,.19,.32,.56),(0,.20,.45,.54),(0,.24,.43,.60),(0,.17,.40,.65),(0,.07,.43,.65),(0,0,.36,.70),(0,0,.25,.78),(0,0,.22,.78),(0,0,.22,.66)]
W=[(.56,.26,.28,.23),(.53,.24,.28,.24),(.53,.23,.27,.21),(.48,.17,.32,.20),(.58,.09,.25,.28),(.64,.07,.29,.28),(.67,.08,.28,.24),(.68,.12,.27,.25),(.63,.16,.28,.25),(.60,.16,.26,.27),(.52,.16,.28,.26),(.47,.16,.48,.25),(.47,.15,.27,.24),(.45,.15,.30,.30),(.43,.16,.35,.36),(.40,.07,.45,.35),(.44,0,.44,.36),(.36,0,.48,.34),(.25,0,.55,.22),(.22,0,.20,.32),(.22,0,.18,.22)]
def K(L): return [{"t":i*0.5,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for i,b in enumerate(L)]
c={"mediaId":4275,"level":"A","keyWord":"complain","defaultVoice":"female",
"taps":[{"phrase":"to point at the car","target":"the woman","voice":"female","keys":K(W)},
{"phrase":"to pick up a red piece","target":"the man","voice":"male","keys":K(M)},
{"phrase":"to write with a pen","target":"the man","voice":"male","keys":K(M)}],
"stillS":0.0,
"nouns":[{"word":"a van","x":.20,"y":.20,"voice":"female"},{"word":"a woman","x":.70,"y":.37,"voice":"female"},{"word":"a wheel","x":.88,"y":.80,"voice":"female"},{"word":"the sky","x":.55,"y":.07,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","complaining","about","the","car."],"answerVoice":"female",
"notes":"Two targets only (woman, young man); man used twice (picks up the red light piece 2.0-3.5, writes on the form 6.5-7.5). Woman points at 4.5-7.0. 'Complaining' is read from her shouting face and pointing. From 9.0 only bodies without heads are visible (woman = blue shirt strip at the top, t=10 very little). Woman stands partly behind the man at 5.0-6.0: boxes split on a vertical line. defaultVoice female = the woman is the main (complaining) person."}
json.dump(c,open('content/4275.json','w'),indent=1)
