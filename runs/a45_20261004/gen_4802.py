import json
T=[x/2 for x in range(19)]
G={0.0:(.36,.23,.58,.77),0.5:(.30,.20,.66,.80),1.0:(.31,.19,.69,.81),1.5:(.41,.18,.59,.82),2.0:(.14,.16,.86,.84),2.5:(0,.19,1,.81),
3.0:(0,.11,1,.89),3.5:(.02,.12,.96,.88),4.0:(0,.12,.76,.88),4.5:(0,.13,.95,.87),5.0:(0,.14,.93,.86),5.5:(.50,.21,.50,.79),
6.0:(.52,.22,.48,.78),6.5:(.53,.22,.47,.78),7.0:(.48,.22,.52,.78),7.5:(.31,.22,.60,.78),8.0:(.27,.21,.49,.75),8.5:(.26,.21,.46,.76),9.0:(.28,.22,.44,.76)}
B={5.5:(.05,.49,.44,.51),6.0:(.02,.46,.45,.54),6.5:(.02,.46,.50,.54),7.0:(0,.55,.26,.45)}
def ks(d): return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
gk=ks(G); bk=ks(B)
c={"mediaId":4802,"level":"A","keyWord":"museum","defaultVoice":"male",
"taps":[{"phrase":"to open the door","target":"the guard","voice":"male","keys":gk},
{"phrase":"to fold his arms","target":"the guard","voice":"male","keys":gk},
{"phrase":"to wear a white T-shirt","target":"the little boy","voice":"male","keys":bk}],
"stillS":8.0,
"nouns":[{"word":"a guard","x":.50,"y":.55,"voice":"male"},{"word":"a girl","x":.14,"y":.47,"voice":"female"},
{"word":"the floor","x":.78,"y":.80,"voice":"male"}],
"question":"What is the guard opening?","answer":["He","is","opening","the","door."],"answerVoice":"male",
"notes":"Little boy (white T-shirt, blond) visible only 5.5-7.0 s; no short action fits only him (the guard also holds the map at 5.5 s), so a state phrase is used. The girl in the denim dress at 2.0 s is not a target (on screen ~1 s). Door opening = guard grips the handle at 4.5-5.0 s. Still at 8.0 s: 'a girl' = the small girl in pink at the back left."}
json.dump(c,open('content/4802.json','w'),indent=1)
