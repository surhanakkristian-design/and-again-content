import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
wom=[(.08,.55,.75,.20),(.01,.56,.82,.26),(0,.48,.73,.30),(0,.44,.76,.35),(0,.52,.76,.29),(0,.53,.79,.29),(0,.53,.75,.31),(0,.54,.76,.31)]
car=[(.19,.37,.18,.17),(.17,.34,.18,.21),(.19,.30,.28,.18),(.22,.23,.31,.21),(.30,.21,.26,.31),(.30,.21,.42,.32),(.28,.24,.44,.29),(.22,.25,.48,.29)]
k=lambda L:[{"t":t,"x":a,"y":b,"w":c,"h":d} for t,(a,b,c,d) in zip(T,L)]
c={"mediaId":7974,"level":"B","keyWord":"season","defaultVoice":"female",
"taps":[{"phrase":"to dive onto a lounger","target":"the woman in orange","voice":"female","keys":k(wom)},
{"phrase":"to punch the air","target":"the woman in orange","voice":"female","keys":k(wom)},
{"phrase":"to carry a cool box","target":"the man with the cool box","voice":"male","keys":k(car)}],
"stillS":0.7,
"nouns":[{"word":"a lifeguard tower","x":.59,"y":.33,"voice":"female"},{"word":"a cool box","x":.24,"y":.49,"voice":"female"},
{"word":"a beach towel","x":.80,"y":.80,"voice":"female"},{"word":"a flip-flop","x":.30,"y":.91,"voice":"female"}],
"question":"What is the woman in orange doing?","answer":["She","is","diving","onto","a","sun","lounger."],
"answerVoice":"female","notes":"From 1.2 s the woman's raised arm lies in front of the man with the cool box; boxes split horizontally, so her raised fist (punch the air) partly falls outside her box / into his. Woman dives at 0.2-0.7 s only, then lies and punches the air. Other women carry towels in the background. 'season' abstract, not a noun slot."}
json.dump(c,open("content/7974.json","w"),indent=1)
