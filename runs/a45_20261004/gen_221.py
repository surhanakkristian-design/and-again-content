import json
T=[i*0.5 for i in range(31)]
W={0.0:(0,.12,.80,.88),0.5:(.03,.10,.85,.90),1.0:(.05,.10,.88,.90),1.5:(.10,.11,.75,.46),2.0:(.08,.10,.75,.46),2.5:(.10,.07,.82,.51),
3.0:(.10,.03,.80,.47),3.5:(.12,.03,.78,.45),4.0:(.10,.01,.78,.45),4.5:(.12,.03,.80,.48),5.0:(.33,.34,.67,.66),5.5:(.30,.34,.66,.66),
6.0:(.22,.27,.78,.73),6.5:(.20,.22,.78,.78),7.0:(.40,.34,.28,.21),7.5:(.37,.35,.38,.23),8.0:(.32,.31,.43,.31),8.5:(.30,.32,.53,.32),
9.0:(.03,.24,.80,.42),9.5:(.05,.23,.82,.46),10.0:(0,.27,1.0,.73),10.5:(0,.19,1.0,.81),11.0:(0,.33,1.0,.67),11.5:(0,.16,1.0,.84),
12.0:(0,.42,1.0,.58),12.5:(.15,.46,.85,.54),13.0:(.05,.52,.85,.48),13.5:(.15,.48,.85,.52),14.0:(.10,.45,.90,.55),14.5:(.10,.36,.90,.64),15.0:(.05,.30,.90,.70)}
C={1.5:(.15,.58,.70,.42),2.0:(0,.57,.70,.43),2.5:(0,.59,.90,.41),3.0:(0,.51,1.0,.49),3.5:(.02,.49,.96,.51),4.0:(0,.47,.98,.53),4.5:(0,.52,1.0,.48)}
F={12.0:.40,12.5:.44,13.0:.50,13.5:.46,14.0:.43,14.5:.34,15.0:.28}
def k(D,f=None):
    out=[]
    for t in T:
        if t in D:
            v=D[t]
            if f: v=(0,0,1.0,v)
            out.append({"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
        else: out.append({"t":t,"off":True})
    return out
d={"mediaId":221,"level":"B","keyWord":"degree","defaultVoice":"female",
"taps":[{"phrase":"to celebrate her graduation","target":"the woman","voice":"female","keys":k(W)},
{"phrase":"to bear a gold seal","target":"the certificate","voice":"female","keys":k(C)},
{"phrase":"to flutter through the air","target":"the confetti","voice":"female","keys":k(F,True)}],
"stillS":4.5,
"nouns":[{"word":"a certificate","x":.55,"y":.72,"voice":"female"},{"word":"a graduation cap","x":.50,"y":.20,"voice":"female"},{"word":"a tassel","x":.80,"y":.40,"voice":"female"}],
"question":"What is the woman celebrating?","answer":["She","is","celebrating","her","graduation."],"answerVoice":"female",
"notes":"Certificate box is off at 0.0-1.0 (only the closed cover is visible) and from 5.0 on. Woman is boxed on the stadium screen at 7.0-9.5 (her picture on the screen; the screen itself is not a target). Confetti fills the whole frame at 12.0-15.0: its box is the area above her head, her box the area below, split at the top of her head. Key word 'degree' is not in the answer (the degree is shown as 'a certificate' noun). 'a tassel' is a hard word; only 3 nouns."}
json.dump(d,open("content/221.json","w"),indent=1)
