import json
T=[i*0.5 for i in range(21)]
def ks(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
woman={0.0:(0,.16,.58,.84),0.5:(0,.16,.68,.84),1.0:(0,.20,.48,.80),1.5:(0,.22,.58,.78),2.0:(0,0,.62,.66),
2.5:(.20,0,.52,.70),3.0:(.06,0,.58,.64),3.5:(0,0,.50,.75),4.0:(0,0,.33,.62),4.5:(0,0,.60,.74),5.0:(0,0,.30,.72),
5.5:(0,0,.44,.66),6.0:(.06,0,.62,.70),6.5:(0,.30,.64,.60),7.0:(0,.53,.64,.24),7.5:(0,.24,.62,.70),8.0:(0,.15,.84,.85),
8.5:(0,.15,.74,.85),9.0:(0,.18,.82,.82),9.5:(0,.24,.88,.76),10.0:(0,.36,.96,.64)}
rock={3.5:(.56,.35,.20,.14),4.0:(.48,.33,.24,.16),4.5:(.76,.33,.24,.20),5.0:(.30,.40,.54,.42),5.5:(.46,.28,.54,.72)}
c={"mediaId":5223,"level":"B","keyWord":"route","defaultVoice":"female",
"taps":[{"phrase":"to run along a dusty trail","target":"the woman","voice":"female","keys":ks(woman)},
{"phrase":"to point at the marked route","target":"the woman","voice":"female","keys":ks(woman)},
{"phrase":"to lie beside the path","target":"the boulder","voice":"female","keys":ks(rock)}],
"stillS":10.0,
"nouns":[{"word":"the sky","x":.50,"y":.12,"voice":"female"},{"word":"a valley","x":.68,"y":.37,"voice":"female"},
{"word":"a headband","x":.24,"y":.45,"voice":"female"},{"word":"a route","x":.70,"y":.80,"voice":"female"}],
"question":"What is the woman holding?",
"answer":["She","is","holding","a","map","with","a","marked","route."],"answerVoice":"female",
"notes":"Boulder only visible 3.5-5.5 s (3.5 s box is a guess on a small far rock). Woman's box at 6.5-7.5 s covers only her arm/hand at the cairn. At 0-1.5 s a second (board) map is also visible; the map was avoided as a tap target for that reason."}
json.dump(c,open('content/5223.json','w'),indent=1)
