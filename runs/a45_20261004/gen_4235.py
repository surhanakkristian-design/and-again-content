import json
T=[i*0.5 for i in range(20)]
B={0:(.38,.42,.38,.48),.5:(.36,.41,.36,.49),1:(.27,.41,.34,.59),1.5:(.18,.44,.36,.52),2:(.16,.4,.36,.45),2.5:(.18,.38,.34,.42),3:(.23,.36,.3,.45),3.5:(.24,.36,.3,.45)}
R={4:(0,.27,1,.6),4.5:(0,.27,1,.58),5:(0,.3,1,.68),5.5:(.05,.33,.95,.56),6:(.05,.3,.95,.62),6.5:(.05,.3,.95,.6),7:(0,.3,1,.7),7.5:(.05,.32,.95,.58),
8:(.1,.28,.9,.6),8.5:(.05,.28,.95,.55),9:(0,.3,1,.64),9.5:(.08,.3,.92,.66)}
def keys(b):
    return [({"t":t,"off":True} if t not in b else {"t":t,"x":b[t][0],"y":b[t][1],"w":b[t][2],"h":b[t][3]}) for t in T]
d={"mediaId":4235,"level":"B","keyWord":"cast","defaultVoice":"male",
"taps":[{"phrase":"to cast a fishing line","target":"the boy","voice":"male","keys":keys(B)},
{"phrase":"to stand barefoot on grass","target":"the boy","voice":"male","keys":keys(B)},
{"phrase":"to hold turquoise fishing line","target":"the reel","voice":"male","keys":keys(R)}],
"stillS":0.0,
"nouns":[{"word":"a fishing rod","x":.26,"y":.24,"voice":"male"},{"word":"a boy","x":.58,"y":.54,"voice":"male"},
{"word":"a lake","x":.16,"y":.63,"voice":"male"},{"word":"grass","x":.6,"y":.92,"voice":"male"}],
"question":"What is the boy doing?","answer":["He","is","casting","a","fishing","line","into","the","lake."],"answerVoice":"male",
"notes":"Two shots: the boy casting (0-3.5 s), then a close-up of the reel in his hands (4.0-9.5 s). Only two targets exist: the boy (phrases 1 and 2, same keys; off in the close-up, only fingers are seen) and the reel (off in the wide shot, where it is a speck at his hands inside his box). Phrase 2 and 3 are states: no second distinct action is shown for the boy, and the reel only sits in the hand (its handle turns a little). The boy's box holds his body, not the full length of the rod. Key word 'cast' is a verb: in phrase 1 and the answer."}
json.dump(d,open("content/4235.json","w"),indent=1)
