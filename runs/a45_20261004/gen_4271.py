import json
T=[0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8]
B=[(0,.14,.70,.66),(.05,0,.95,.80),(0,.05,1,.93),(.08,.11,.90,.82),(.28,.19,.60,.59),(.23,.19,.66,.55),(.05,.17,.85,.62),(.21,.16,.58,.67),(.10,.16,.80,.53),(.29,.16,.47,.57),(.06,.16,.73,.63),(.21,.17,.57,.64),(.11,.17,.63,.52),(.26,.17,.52,.52),(.16,.18,.66,.65),(.26,.19,.55,.63),(.21,.17,.48,.54)]
keys=[{"t":float(t),"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,B)]
c={"mediaId":4271,"level":"A","keyWord":"athlete","defaultVoice":"male",
"taps":[{"phrase":p,"target":"the athlete","voice":"male","keys":keys} for p in ["to start a race","to run very fast","to take big steps"]],
"stillS":7.0,
"nouns":[{"word":"an athlete","x":.55,"y":.36,"voice":"male"},{"word":"the sky","x":.65,"y":.10,"voice":"male"},{"word":"grass","x":.14,"y":.50,"voice":"male"},{"word":"a track","x":.50,"y":.85,"voice":"male"}],
"question":"What is the athlete doing?","answer":["He","is","running","very","fast."],"answerVoice":"male",
"notes":"Only one possible target (the sprinter), used for all three phrases. An official stands behind him at t=0-0.5 only. Grass strip is narrow; pill on its left part."}
json.dump(c,open('content/4271.json','w'),indent=1)
