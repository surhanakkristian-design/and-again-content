import json
def K(d,times):
    out=[]
    for t in times:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
times=[i*0.5 for i in range(25)]
S={0.0:(.38,.42,.30,.44),0.5:(.38,.42,.30,.44),1.0:(.40,.42,.30,.42),1.5:(.38,.41,.36,.42),2.0:(.08,.42,.92,.38),2.5:(.20,.37,.64,.28),
3.0:(.18,.37,.78,.26),3.5:(.04,.41,.96,.25),4.0:(.03,.43,.94,.25),4.5:(.02,.43,.95,.26),5.0:(.10,.46,.80,.23),5.5:(.04,.41,.90,.38),
6.0:(.14,.47,.62,.26),6.5:(0,.39,.88,.28),7.0:(0,.40,1.0,.28),7.5:(0,.44,.92,.25),8.0:(.02,.44,.46,.30),8.5:(0,.33,.60,.30),
9.0:(0,.40,.60,.30),9.5:(0,.385,.92,.34),10.0:(0,.42,.95,.33),10.5:(0,.48,.97,.28),11.0:(0,.49,.93,.26),11.5:(0,.49,.91,.26),12.0:(.03,.48,.87,.26)}
W={7.0:(.36,.26,.28,.14),7.5:(.15,.17,.68,.27),8.0:(.48,.02,.52,.80)}
L={8.0:(.30,.21,.18,.14),9.0:(.40,.24,.18,.14),9.5:(.41,.24,.18,.14),10.0:(.41,.27,.19,.14),10.5:(.42,.28,.19,.15),
11.0:(.41,.28,.20,.15),11.5:(.40,.27,.21,.16),12.0:(.38,.25,.27,.19)}
c={"mediaId":4239,"level":"B","keyWord":"port","defaultVoice":"male",
"taps":[
{"phrase":"to glide between cargo ships","target":"the seagull","voice":"male","keys":K(S,times)},
{"phrase":"to leap from the water","target":"the whale","voice":"male","keys":K(W,times)},
{"phrase":"to overlook the harbour","target":"the lighthouse","voice":"male","keys":K(L,times)}],
"stillS":12.0,
"nouns":[{"word":"the sky","x":.50,"y":.12,"voice":"male"},{"word":"a lighthouse","x":.51,"y":.36,"voice":"male"},
{"word":"a seagull","x":.43,"y":.61,"voice":"male"},{"word":"reins","x":.64,"y":.76,"voice":"male"}],
"question":"What is the seagull doing?",
"answer":["It","is","gliding","over","the","port."],
"answerVoice":"male",
"notes":"First-person clip: only gloved hands of the rider are visible, so no person target. The whale is in the picture only 7.0-8.0 s (8.5 s: a sliver at the right edge, set off). The lighthouse is tiny at 8.0 s and clear from 9.0 s. Key word 'port' has no single place on the still (it is the whole harbour), so it is used in the answer, not as a noun pill. 'reins' are two straps; the pill sits on the right one. 'to overlook the harbour' is a state of a thing."}
json.dump(c,open("content/4239.json","w"),indent=1)
