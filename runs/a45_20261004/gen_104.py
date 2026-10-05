import json
T=[i*0.5 for i in range(21)]
B=[(.33,0,.37,.52),(.36,0,.36,.61),(.31,.20,.40,.54),(.30,0,.42,.72),(.28,0,.43,.78),(.26,0,.46,.87),(.26,0,.48,1.0),(.23,0,.51,1.0),
(.22,0,.52,.88),(.20,0,.54,.84),(.18,0,.54,.94),(.19,0,.55,.93),(.20,0,.52,.81),(.23,0,.63,.74),(.24,.18,.56,.58),(.23,.01,.61,.75),
(.18,0,.66,.94),(.20,.14,.64,.86),(.16,.33,.73,.65),(.14,.34,.84,.62),(.06,.28,.94,.64)]
keys=[{"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,B)]
d={"mediaId":104,"level":"A","keyWord":"bottom","defaultVoice":"female",
"taps":[{"phrase":p,"target":"the woman","voice":"female","keys":keys} for p in ["to swim to the bottom","to pick up a stone","to hold up a stone"]],
"stillS":7.0,
"nouns":[{"word":"a mask","x":0.50,"y":0.31,"voice":"female"},{"word":"a stone","x":0.50,"y":0.56,"voice":"female"},{"word":"the bottom","x":0.50,"y":0.86,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","taking","a","stone","from","the","bottom."],
"answerVoice":"female",
"notes":"Only one possible target (the woman) for all three phrases; the stone is in her hand most of the clip. 'the bottom' = the sandy sea floor (key word) instead of 'sand'. A second person is faintly visible far behind her at 9.0-10.0 s (does none of the actions)."}
json.dump(d,open("content/104.json","w"),indent=1)
