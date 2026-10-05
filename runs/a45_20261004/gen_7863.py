import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
blue=[(.12,.26,.54,.54),(.28,.25,.40,.56),(.35,.28,.35,.58),(.48,.25,.25,.38),(.42,.26,.22,.46),(.44,.26,.30,.47),(.38,.26,.33,.56),(.38,.25,.30,.40)]
yel=[(.76,.24,.24,.26),(.72,.24,.28,.26),(.80,.25,.20,.32),(.78,.26,.22,.36),(.72,.26,.28,.46),(.80,.26,.20,.40),(.82,.26,.18,.30),None]
man=[(.66,.50,.34,.50),(.69,.50,.31,.50),(.70,.58,.30,.42),(.48,.63,.52,.37),(.12,.73,.80,.27),(.30,.73,.67,.27),(.72,.58,.28,.42),(.30,.65,.70,.35)]
def k(L): return [({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]}) for t,v in zip(T,L)]
c={"mediaId":7863,"level":"B","keyWord":"have an opportunity","defaultVoice":"female",
"taps":[{"phrase":"to climb over the barrier","target":"the woman in blue","voice":"female","keys":k(blue)},
{"phrase":"to hand over a microphone","target":"the woman in yellow","voice":"female","keys":k(yel)},
{"phrase":"to punch the air","target":"the man in white","voice":"male","keys":k(man)}],
"stillS":3.2,
"nouns":[{"word":"spotlights","x":0.75,"y":0.21,"voice":"female"},{"word":"a microphone","x":0.52,"y":0.39,"voice":"female"},
{"word":"a loudspeaker","x":0.22,"y":0.77,"voice":"female"}],
"question":"What is the woman in blue doing?","answer":["She","is","singing","into","a","microphone."],"answerVoice":"female",
"notes":"Man in white and woman in blue overlap heavily from 1.7 s on; split horizontally (woman above, man below), so the man's head is only partly in his box at 1.7-2.7 s and his left shirt is outside it at 3.2 s. Woman in yellow is only a sliver at 3.7 s -> off. 'to punch the air' = his raised fist at 3.7 s. Only 3 nouns: drum kit and guitars too cluttered / two guitars."}
json.dump(c,open('content/7863.json','w'),indent=1)
