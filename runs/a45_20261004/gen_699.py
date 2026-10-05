import json
T=[i*0.5 for i in range(21)]
F={0:(0,.20,.33,.68),.5:(0,.22,.44,.78),1:(0,.20,.34,.80),1.5:(0,0,.72,.78),2:(0,0,.92,.50),2.5:(0,.08,.85,.72),3:(0,.08,.90,.77),
3.5:(0,.33,.88,.44),4:(0,.33,.88,.46),6.5:(0,.29,.42,.19),7:(0,.25,.60,.33),7.5:(0,.28,.56,.30),8:(.03,.27,.66,.55),8.5:(0,.18,.60,.82),
9:(0,.16,1,.69),9.5:(0,.06,1,.94),10:(0,.06,1,.94)}
G={4:(.68,0,.32,.24),4.5:(.30,.13,.68,.34),5:(.24,.15,.68,.42),5.5:(.30,.12,.64,.46),6:(.10,.10,.82,.36),6.5:(0,.14,.21,.14)}
C={0:(.34,.47,.66,.53),.5:(.45,.50,.55,.50),1:(.35,.58,.65,.42),1.5:(0,.79,1,.21),2:(0,.72,1,.28),2.5:(0,.81,1,.19),3:(0,.86,1,.14),
3.5:(.22,.78,.78,.22),4:(.20,.80,.80,.20),4.5:(0,.48,.86,.52),5:(0,.58,.86,.42),5.5:(0,.59,.86,.41),6:(0,.47,.86,.53),6.5:(.12,.49,.73,.33),
7:(.25,.59,.75,.32),7.5:(.26,.59,.73,.32),8:(.70,.46,.30,.30),8.5:(.61,.56,.39,.28),9:(0,.86,1,.14)}
def keys(D): return [({"t":t,"x":D[t][0],"y":D[t][1],"w":D[t][2],"h":D[t][3]} if t in D else {"t":t,"off":True}) for t in T]
d={"mediaId":699,"level":"B","keyWord":"smuggle","defaultVoice":"male","taps":[
{"phrase":"to smuggle some cheese","target":"the farmer","voice":"male","keys":keys(F)},
{"phrase":"to raise the barrier","target":"the guard","voice":"male","keys":keys(G)},
{"phrase":"to carry a load of hay","target":"the cart","voice":"male","keys":keys(C)}],
"stillS":4.5,"nouns":[{"word":"a guard","x":.60,"y":.36,"voice":"male"},{"word":"hay","x":.22,"y":.47,"voice":"male"},
{"word":"a barrier","x":.82,"y":.56,"voice":"male"},{"word":"a cart","x":.30,"y":.68,"voice":"male"}],
"question":"What is the farmer smuggling?","answer":["He","is","smuggling","cheese","under","the","hay."],"answerVoice":"male",
"notes":"Farmer, guard and cart overlap in almost every shot, so the boxes are split and are partial: in the close-ups (1.5-4.0 s) the farmer box is his hands/arms and the cart box is only the wooden strip below; at 8.0-8.5 s the cart box is only the right part of the cart. At 4.0 s only the guard's torso is visible (top right). At 6.5 s the guard box is his head only (the farmer stands in front of him). Cart set off at 9.5-10 s (only a wisp of hay left). 'the farmer' is identified by the cart and work clothes against the uniformed guard."}
json.dump(d,open("content/699.json","w"),indent=1,ensure_ascii=False)
