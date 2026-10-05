import json
T=[i*0.5 for i in range(19)]
B={0.0:(.05,.06,.95,.94),0.5:(.09,0,.91,1),1.0:(.06,0,.60,.86),1.5:(.06,0,.56,.76),2.0:(.12,0,.50,.72),2.5:(0,0,.62,.74),
3.0:(.03,0,.53,.80),3.5:(.26,.02,.56,.58),4.0:(.34,.06,.48,.58),4.5:(.30,.06,.52,.62),5.0:(.30,.14,.58,.48),5.5:(.30,.16,.40,.43),
6.0:(.43,.24,.24,.48),6.5:(.41,.36,.20,.30),7.0:(.38,.40,.18,.22),7.5:(.37,.40,.18,.24),8.0:(.44,.41,.18,.21),9.0:(.38,.41,.18,.23)}
P={1.0:(.66,.58,.29,.20),1.5:(.62,.50,.22,.18),2.0:(.62,.49,.20,.16),2.5:(.62,.52,.24,.17),3.0:(.56,.57,.20,.15),3.5:(.55,.60,.23,.15),
4.0:(.50,.64,.26,.16),4.5:(.52,.68,.22,.14),5.0:(.50,.62,.20,.14),5.5:(.50,.59,.20,.14)}
def keys(D): return [dict(t=t,x=D[t][0],y=D[t][1],w=D[t][2],h=D[t][3]) if t in D else dict(t=t,off=True) for t in T]
kb=keys(B); kp=keys(P)
d={"mediaId":4890,"level":"B","keyWord":"circle","defaultVoice":"male",
"taps":[{"phrase":"to hop on one leg","target":"the boy","voice":"male","keys":kb},
{"phrase":"to kick out his leg","target":"the boy","voice":"male","keys":kb},
{"phrase":"to spin on the paving","target":"the spinning top","voice":"male","keys":kp}],
"stillS":4.0,
"nouns":[{"word":"a skyscraper","x":0.72,"y":0.06,"voice":"male"},{"word":"a lamp post","x":0.28,"y":0.21,"voice":"male"},
{"word":"a spinning top","x":0.65,"y":0.72,"voice":"male"},{"word":"paving stones","x":0.30,"y":0.88,"voice":"male"}],
"question":"What is the boy circling?",
"answer":["He","is","circling","a","spinning","top."],"answerVoice":"male",
"notes":"The boy's foot passes right over the top at 1.0-5.5 s: boxes split (vertically at 1.0-3.0 s, horizontally at 3.5-5.5 s, so his feet are partly outside his box there). The top is off from 6.0 s: it becomes tiny and a second small top appears (5.5 s far right, 8.0 s), so 'the spinning top' would be ambiguous. From 6.0 s many people circle in a ring; the boy (white T-shirt, grey sweatpants) is followed as a small figure, off at 8.5 s where he is hidden. Everyone circles at the end, so 'circle' is used only in the question about the boy, not as a tap phrase."}
json.dump(d,open("content/4890.json","w"),indent=1)
