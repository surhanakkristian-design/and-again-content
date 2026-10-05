import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
blue=[(.02,.23,.42,.54),(.02,.23,.43,.55),(.01,.23,.44,.56),(.02,.23,.43,.58),(.02,.21,.41,.57),(.02,.21,.40,.59),(.01,.21,.40,.61),(.01,.21,.42,.61)]
tux=[(.44,.27,.18,.32),(.45,.27,.18,.31),(.45,.27,.18,.31),(.45,.27,.18,.31),(.435,.26,.18,.31),(.42,.26,.20,.32),(.415,.26,.20,.32),(.435,.26,.19,.32)]
dog=[(.50,.60,.50,.40),(.47,.61,.53,.39),(.50,.62,.50,.38),(.51,.63,.49,.37),(.51,.63,.49,.37),(.53,.63,.47,.37),(.53,.64,.47,.36),(.54,.64,.46,.36)]
k=lambda L:[{"t":t,"x":a,"y":b,"w":c,"h":d} for t,(a,b,c,d) in zip(T,L)]
c={"mediaId":7975,"level":"B","keyWord":"secretly","defaultVoice":"female",
"taps":[{"phrase":"to feed the dog secretly","target":"the woman in blue","voice":"female","keys":k(blue)},
{"phrase":"to lick the fork","target":"the dog","voice":"female","keys":k(dog)},
{"phrase":"to applaud enthusiastically","target":"the man in the bow tie","voice":"male","keys":k(tux)}],
"stillS":2.2,
"nouns":[{"word":"a chandelier","x":.63,"y":.05,"voice":"female"},{"word":"a waiter","x":.17,"y":.22,"voice":"male"},
{"word":"a candelabra","x":.85,"y":.44,"voice":"female"},{"word":"a dog","x":.80,"y":.78,"voice":"female"}],
"question":"What is the woman in blue doing?","answer":["She","is","feeding","meat","to","the","dog."],
"answerVoice":"female","notes":"Woman in blue and man in the bow tie overlap (he sits just behind her right shoulder): split vertically at x ~.43, so his face is partly inside her box and her fork hand (0.2-1.7 s) partly outside hers. Man-in-bow-tie box also covers the lower half of the woman in green standing behind (she is not a target). Dog licks the fork only at 0.2-1.2 s. Answer avoids 'secretly' to keep one word order."}
json.dump(c,open("content/7975.json","w"),indent=1)
