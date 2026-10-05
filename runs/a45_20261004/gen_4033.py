import json
T=[i*0.5 for i in range(21)]
def K(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
P={0.0:(.44,.12,.30,.31),0.5:(.50,.12,.24,.35),1.0:(.52,.12,.22,.35),1.5:(.45,.12,.29,.33),2.0:(.45,.12,.29,.32),
2.5:(.45,.12,.29,.34),3.0:(.45,.12,.29,.34),3.5:(.45,.12,.29,.34),4.0:(.47,.10,.27,.36),4.5:(.42,.03,.35,.43),
5.0:(.44,.04,.30,.42),5.5:(.30,.09,.43,.37),6.0:(0,.05,.39,.41),6.5:(.50,.07,.34,.39),7.0:(.47,.10,.33,.36),
7.5:(.20,.14,.38,.32),8.0:(0,.16,.18,.26),8.5:(0,.17,.22,.25),9.0:(.10,.16,.26,.30),9.5:(.40,.14,.27,.28),10.0:(.70,.12,.30,.18)}
W={t:(.74,.23,.25,.23) for t in T if t<=4.0}
W.update({4.5:(.77,.20,.23,.26),5.0:(.74,.22,.26,.24),5.5:(.73,.22,.27,.24),6.0:(.60,.20,.40,.26),6.5:(.84,.20,.16,.26),
7.0:(.80,.18,.20,.28),7.5:(.75,.17,.25,.29),8.0:(.64,.19,.36,.27),8.5:(.60,.24,.40,.22),9.0:(.58,.23,.42,.23),9.5:(.67,.24,.33,.22),10.0:(.56,.30,.44,.16)})
B={0.0:(.35,.43,.20,.14),0.5:(.30,.30,.20,.14),1.0:(.33,.24,.19,.14),1.5:(.40,.45,.18,.14),2.0:(.40,.44,.20,.14)}
B.update({t:(.37,.47,.28,.17) for t in T if t>=2.5})
d={"mediaId":4033,"level":"A","keyWord":"club","defaultVoice":"male",
"taps":[{"phrase":"to hit a ball","target":"the man in purple","voice":"male","keys":K(P)},
{"phrase":"to sit on the floor","target":"the man in white","voice":"male","keys":K(W)},
{"phrase":"to land on a stick","target":"the pink ball","voice":"male","keys":K(B)}],
"stillS":3.0,
"nouns":[{"word":"a ball","x":.51,"y":.55,"voice":"male"},{"word":"a club","x":.56,"y":.41,"voice":"male"},
{"word":"a sofa","x":.36,"y":.33,"voice":"male"},{"word":"a carpet","x":.80,"y":.90,"voice":"male"}],
"question":"What is the man in purple holding?",
"answer":["He","is","holding","a","golf","club."],"answerVoice":"male",
"notes":"Two men overlap/stand close: boxes split at x=0.74 (frames 0-4 s), so the white man's knees and the purple man's head edge are cut slightly in a few frames. Ball is tiny at 0.0-1.0 s and next to the purple man's club; its box sits left of / below the man's box. From 6.5 s the purple man runs in front of the white man: split boxes are approximate. Club is small on the still (thin shaft at the man's feet). 'a stick' = the wooden tee."}
json.dump(d,open("content/4033.json","w"),indent=1)
