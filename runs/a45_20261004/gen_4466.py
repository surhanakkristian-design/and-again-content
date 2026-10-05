import json
T=[i*0.5 for i in range(21)]
man=[(0,.37,.72,.63),(.08,.30,.74,.70),(.10,.34,.66,.66),(.05,.27,.70,.73),(.08,.24,.80,.76),(.28,.34,.45,.66),(.15,.29,.56,.71),(.07,.25,.73,.75),(0,.22,.68,.78),(0,.22,.98,.78),(0,.55,1,.45),(0,.57,.98,.43),(.17,.19,.58,.76),(.22,.22,.53,.63),(.36,.24,.42,.75),(.26,.19,.68,.81),(0,.37,1,.63),(.05,.41,.95,.59),(0,.41,1,.59),(0,.41,1,.59),(0,.42,1,.58)]
keys=[{"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,man)]
d={"mediaId":4466,"level":"B","keyWord":"aboard","defaultVoice":"male",
"taps":[{"phrase":p,"target":"the man","voice":"male","keys":keys} for p in ["to climb aboard a bus","to tap his travel card","to spread his arms wide"]],
"stillS":6.0,
"nouns":[{"word":"a skyscraper","x":.58,"y":.07,"voice":"male"},{"word":"a backpack","x":.62,"y":.42,"voice":"male"},{"word":"a handrail","x":.14,"y":.55,"voice":"male"},{"word":"a staircase","x":.50,"y":.80,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","climbing","aboard","a","red","bus."],
"answerVoice":"male",
"notes":"Only the man is a unique target (passengers are crowds doing the same things), so all three phrases use him. He climbs aboard three vehicles (minibus 0-2 s, city bus 2.5-4 s, red tour bus 6-7.5 s), holds his card to the reader at 3-3.5 s, arms wide 8-10 s. At 5.0/5.5 only his arm and shoulder are in the picture. Key word 'aboard' is an adverb: used in phrase 1 and the answer, not as a noun. The answer describes the tour bus shot (6-7.5 s)."}
json.dump(d,open("content/4466.json","w"),indent=1,ensure_ascii=False)
