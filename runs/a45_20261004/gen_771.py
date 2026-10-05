import json
T=[i*0.5 for i in range(17)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} if b else {"t":t,"off":True})
    return out
W={0.0:(.29,.33,.44,.63),0.5:(.27,.3,.48,.7),1.0:(.24,.28,.47,.72),1.5:(.17,.34,.48,.66),2.0:(.22,.42,.48,.5),2.5:(.22,.43,.4,.48),
 3.0:(.24,.45,.38,.52),3.5:(.24,.45,.45,.55),4.0:(.27,.45,.45,.53),4.5:(.3,.38,.47,.6),5.0:(.17,.33,.6,.67),5.5:(.36,.28,.44,.72),
 6.0:(.22,.24,.6,.76),6.5:(.08,.2,.67,.8),7.0:(.06,.2,.67,.8),7.5:(.08,.2,.58,.8),8.0:(.06,.2,.56,.8)}
P={5.5:(0,.38,.36,.14),6.0:(.83,.38,.17,.2),6.5:(.76,.48,.24,.17),7.0:(.74,.5,.26,.17),7.5:(.66,.49,.34,.17),8.0:(.62,.49,.38,.17)}
c={"mediaId":771,"level":"B","keyWord":"terminal","defaultVoice":"female",
"taps":[{"phrase":"to ride up the escalator","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to gaze at the runway","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to wait on the tarmac","target":"the plane","voice":"female","keys":keys(P)}],
"stillS":3.0,
"nouns":[{"word":"an escalator","x":.82,"y":.78,"voice":"female"},{"word":"a palm tree","x":.75,"y":.45,"voice":"female"},
{"word":"a suitcase","x":.57,"y":.88,"voice":"female"},{"word":"a cardigan","x":.42,"y":.66,"voice":"female"}],
"question":"What is the woman pulling?","answer":["She","is","pulling","a","suitcase","through","the","terminal."],"answerVoice":"female",
"notes":"Only one clear moving target (the woman), so two phrases share her; the third is the plane, visible only from 5.5 s. At 5.5 s the plane is partly behind her (her box is cut at x 0.36, the plane box is the part left of her); at 6.0 s a second small plane with a red tail sits inside her box left of her head, the plane box there is only the right part of the big plane. Key word 'terminal' is the whole place, so it is not a noun slot; it is in the answer. Still 3.0 s has a second small suitcase far left (0.15, 0.72); the slot is on hers."}
json.dump(c,open('content/771.json','w'),indent=1,ensure_ascii=False)
