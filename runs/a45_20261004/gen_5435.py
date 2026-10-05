import json
T=[i*0.5 for i in range(19)]
L={0.0:(.10,.30,.37,.62),0.5:(.12,.27,.38,.70),1.0:(.07,.27,.43,.73),1.5:(.06,.27,.42,.73),2.0:(.02,.24,.48,.76),2.5:(0,.22,.47,.78),3.0:(0,.22,.50,.78),
3.5:(0,.21,.52,.79),4.0:(0,.21,.56,.79),4.5:(0,.21,.52,.79),5.0:(0,.22,.50,.78),5.5:(0,.22,.50,.78),6.0:(0,.23,.50,.77),6.5:(0,.23,.50,.77),
7.0:(0,.30,.50,.70),7.5:(0,.27,.52,.73),8.0:(0,.22,.50,.78),8.5:(0,.22,.48,.78),9.0:(.02,.24,.48,.76)}
R={0.0:(.47,.32,.36,.58),0.5:(.50,.29,.37,.66),1.0:(.50,.30,.46,.70),1.5:(.48,.29,.32,.71),2.0:(.50,.28,.50,.72),2.5:(.47,.25,.50,.75),3.0:(.50,.24,.50,.76),
3.5:(.52,.23,.48,.77),4.0:(.56,.22,.44,.78),4.5:(.52,.22,.48,.78),5.0:(.50,.24,.50,.76),5.5:(.50,.24,.50,.76),6.0:(.50,.26,.50,.74),6.5:(.50,.25,.50,.75),
7.0:(.50,.25,.50,.75),7.5:(.52,.28,.48,.72),8.0:(.50,.23,.50,.77),8.5:(.48,.24,.52,.76),9.0:(.50,.25,.26,.75)}
B={0.0:None,0.5:None,1.0:None,1.5:(.80,.07,.20,.22),2.0:(.60,.06,.40,.22),2.5:(.60,.06,.40,.19),3.0:(.58,.06,.42,.18),3.5:(.58,.06,.42,.17),
4.0:(.58,.04,.42,.18),4.5:(.58,.04,.42,.18),5.0:(.58,.06,.42,.18),5.5:(.58,.06,.42,.18),6.0:(.58,.06,.42,.20),6.5:(.58,.06,.42,.19),
7.0:(.58,.06,.42,.19),7.5:(.58,.06,.42,.22),8.0:(.58,.04,.42,.19),8.5:(.58,.04,.42,.20),9.0:(.76,.16,.24,.36)}
def keys(d): return [({"t":t,"off":True} if d[t] is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]}) for t in T]
c={"mediaId":5435,"level":"B","keyWord":"alike","defaultVoice":"female",
"taps":[{"phrase":"to pull out a blue packet","target":"the woman on the left","voice":"female","keys":keys(L)},
{"phrase":"to pull out a red packet","target":"the woman on the right","voice":"female","keys":keys(R)},
{"phrase":"to overlook the lawn","target":"the building","voice":"female","keys":keys(B)}],
"stillS":0.0,
"nouns":[{"word":"the sky","x":.80,"y":.05,"voice":"female"},{"word":"trees","x":.35,"y":.20,"voice":"female"},
{"word":"a lawn","x":.86,"y":.56,"voice":"female"},{"word":"a pavement","x":.76,"y":.91,"voice":"female"}],
"question":"How do the two women look?","answer":["The","two","women","look","exactly","alike."],"answerVoice":"female",
"notes":"Hard clip for 'tap who does it': the two women look and act the same by design. The only thing that differs is the packet each pulls out of her belt bag at 3.0-3.5 s (left: blue/yellow crisps, right: red) - but they then swap packets (5.0 s the left one holds the red, the right one the blue), so the two phrases rest on 'pull out' at 3.0-3.5 s; verifier please judge. Third target is the grey building behind the trees (upper right from 1.5 s; off before, where only other buildings/trees show); its box sits above the right woman's head, at 9.0 s it takes the right edge and the right woman's box is cut at x .76 (her backpack sticks out beyond). Everything on the women is doubled (backpacks, ponytails), so the nouns are scenery at 0.0 s. Question is a state -> present simple; key word in the answer."}
json.dump(c,open('content/5435.json','w'),indent=1)
