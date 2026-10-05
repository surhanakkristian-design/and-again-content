import json
T=[i*0.5 for i in range(25)]
YM={0.5:(0,.03,.30,.87),1.0:(0,.06,.52,.94),1.5:(0,.07,.68,.92),2.0:(0,.06,.62,.90),2.5:(0,.06,.64,.90),3.0:(0,.08,.65,.92),3.5:(0,.08,.66,.92)}
WO={4.0:(.70,.18,.30,.45),4.5:(.58,.14,.42,.46),5.0:(.28,.15,.72,.45),5.5:(.27,.16,.73,.44),6.0:(.58,.10,.42,.50),6.5:(.63,.12,.37,.60),7.0:(.62,.40,.38,.34),7.5:(.82,.28,.18,.48)}
SU={8.0:(.36,.23,.28,.18),8.5:(.33,.23,.35,.18),9.0:(.30,.24,.39,.19),9.5:(.30,.24,.40,.18),10.0:(.31,.25,.39,.17),10.5:(.32,.25,.37,.17),11.0:(.32,.28,.36,.17),11.5:(.32,.29,.36,.16),12.0:(.33,.31,.34,.15)}
def keys(B):
    return [{"t":t,"off":True} if t not in B else {"t":t,"x":B[t][0],"y":B[t][1],"w":B[t][2],"h":B[t][3]} for t in T]
c={"mediaId":5378,"level":"A","keyWord":"set","defaultVoice":"female",
"taps":[{"phrase":"to put down a mug","target":"the man in the T-shirt","voice":"male","keys":keys(YM)},
{"phrase":"to set the table","target":"the woman","voice":"female","keys":keys(WO)},
{"phrase":"to open his arms","target":"the man in the suit","voice":"male","keys":keys(SU)}],
"stillS":7.5,
"nouns":[{"word":"a window","x":0.42,"y":0.20,"voice":"female"},{"word":"a sink","x":0.52,"y":0.40,"voice":"female"},
{"word":"a bowl","x":0.57,"y":0.58,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","setting","the","table."],"answerVoice":"female",
"notes":"Three scenes, one target each: young man in grey T-shirt 0.5-3.5 s (puts the mug down at 1.5-2 s, then rocks the table), woman in the kitchen 4-7.5 s (puts glasses and plates on the table; at 7-7.5 s only her arm is in frame), man in the suit 8-12 s (small and far away, arms open). defaultVoice female: no single main person (mixed group), evenId true. Key word 'set' is a verb, not placed as a noun."}
json.dump(c,open('content/5378.json','w'),indent=1)
