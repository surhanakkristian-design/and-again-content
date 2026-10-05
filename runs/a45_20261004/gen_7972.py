import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
man=[(0,.26,.42,.42),(0,.25,.40,.44),(0,.23,.48,.57),(0,.23,.45,.55),(0,.21,.40,.54),(0,.21,.40,.53),(0,.24,.40,.56),(0,.24,.40,.57)]
per=[(0,.69,1,.31),(0,.69,1,.31),(0,.81,1,.19),(0,.79,1,.21),(0,.76,1,.24),(0,.75,1,.25),(0,.80,1,.20),(0,.81,1,.19)]
k=lambda L:[{"t":t,"x":a,"y":b,"w":c,"h":d} for t,(a,b,c,d) in zip(T,L)]
c={"mediaId":7972,"level":"B","keyWord":"scene","defaultVoice":"male",
"taps":[{"phrase":"to point at the view","target":"the man","voice":"male","keys":k(man)},
{"phrase":"to laugh with delight","target":"the man","voice":"male","keys":k(man)},
{"phrase":"to wear a gold bracelet","target":"the second person","voice":"male","keys":k(per)}],
"stillS":2.2,
"nouns":[{"word":"the sky","x":.55,"y":.12,"voice":"male"},{"word":"hills","x":.65,"y":.34,"voice":"male"},
{"word":"a stone bridge","x":.70,"y":.55,"voice":"male"},{"word":"rooftops","x":.72,"y":.70,"voice":"male"}],
"question":"What is the young man doing?","answer":["He","is","admiring","the","view","from","the","tower."],
"answerVoice":"male","notes":"Second person shown only as forearms in the foreground (gender unclear), target named 'the second person'; the man wears a watch, not a bracelet. 'scene' not used as a noun (abstract)."}
json.dump(c,open("content/7972.json","w"),indent=1)
