import json
T=[i*0.5 for i in range(19)]
man=[(0,.25,.97,.75),(.02,.39,.81,.61),(.02,.39,.81,.61),(.05,.33,.80,.67),(.05,.34,.90,.66),(0,.32,.31,.68),(0,.34,.28,.66),(0,.34,.30,.66),(0,.31,.28,.69),(.09,.35,.62,.65),(.17,.39,.61,.61),(.17,.37,.83,.63),(.45,.19,.55,.81),(.42,.19,.58,.81),(.45,.18,.55,.82),(.47,.17,.53,.83),(.49,.17,.51,.83),(.47,.17,.53,.83),(.57,.19,.43,.81)]
keys=[{"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,man)]
d={"mediaId":4472,"level":"B","keyWord":"altitude","defaultVoice":"male",
"taps":[{"phrase":p,"target":"the man","voice":"male","keys":keys} for p in ["to stick his head out","to board a cable car","to stare at the cliff"]],
"stillS":3.5,
"nouns":[{"word":"the sky","x":.60,"y":.08,"voice":"male"},{"word":"a fur hat","x":.13,"y":.40,"voice":"male"},{"word":"a cable car","x":.86,"y":.53,"voice":"male"},{"word":"a forest","x":.50,"y":.82,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","gaining","altitude","in","a","cable","car."],
"answerVoice":"male",
"notes":"Only the man is a unique target (the skiers are a seated group, the other cabins come and go), so all three phrases use him. He leans his head out of the cabin window at 2.5-4.0 s, steps into the cabin at the station at 4.5-5.5 s, stares open-mouthed at the rock face at 6-9 s. Key word 'altitude' is abstract: used only in the answer ('to gain altitude'), not placed as a noun; the answer sums up the whole clip (forest, then cloud level, then the high rock face). Still 3.5 s shows one other cabin only ('a cable car'); 'a fur hat' pill sits on his hat. Doubt: 'cable car' is used for the single cabin (also called a gondola)."}
json.dump(d,open("content/4472.json","w"),indent=1,ensure_ascii=False)
