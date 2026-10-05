import json
T=[i*0.5 for i in range(21)]
def mk(d):
    out=[]
    for t in T:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True})
        else:
            x0,y0,x1,y1=b
            out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
P={0.0:(0,.07,.70,.63),0.5:(0,.26,.54,.60),1.0:(0,.41,.47,.63),1.5:(0,.52,.37,.68),2.0:(0,.46,.44,.78),2.5:(0,.38,.60,.74),
   3.0:(0,.08,.26,1),3.5:(0,.56,.21,.76),
   6.5:(.36,.20,.70,.75),7.0:(.33,.21,.69,.75),7.5:(.35,.20,.69,.75),8.0:(.33,.17,.70,.76),8.5:(.32,.16,.70,.78),9.0:(.33,.16,.73,.80),9.5:(.28,.28,.66,.86),10.0:(.27,.28,.66,.87)}
M={3.0:(.51,0,1,1),3.5:(.50,0,1,1),4.0:(.49,0,1,1),4.5:(.70,.62,1,.92),5.0:(.80,.68,1,.84)}
TP={3.0:(.32,.41,.50,.55),3.5:(.22,.42,.49,.73),4.0:(0,.42,.48,.76),4.5:(0,.34,.69,.82),5.0:(0,.33,1,.67),5.5:(0,.34,1,.76),6.0:(0,.39,1,.82)}
c={"mediaId":258,"level":"B","keyWord":"edge","defaultVoice":"female",
"taps":[
 {"phrase":"to balance on a plank","target":"the person with blue hair","voice":"female","keys":mk(P)},
 {"phrase":"to have a ginger beard","target":"the man","voice":"male","keys":mk(M)},
 {"phrase":"to stretch across the lawn","target":"the tarp","voice":"female","keys":mk(TP)}],
"stillS":8.0,
"nouns":[{"word":"pine trees","x":0.70,"y":0.12,"voice":"female"},{"word":"boulders","x":0.20,"y":0.45,"voice":"female"},{"word":"a lake","x":0.80,"y":0.66,"voice":"female"},{"word":"a plank","x":0.50,"y":0.86,"voice":"female"}],
"question":"What is the blue-haired person doing?",
"answer":["The","person","is","balancing","on","a","narrow","plank."],
"answerVoice":"female",
"notes":"Three shots. Shot 1 (0-2.5) shows only a hand with a red checked sleeve on the table edge: boxed as the blue-haired person (same shirt). Gender of the blue-haired person unclear: 'the person', default voice. Both people hold the rope at 3.0-3.5, so the man's phrase is a state (beard). In shot 2 man, tarp and the person's arm overlap: boxes split, the person's forearm at 3.0 and the man's lower hand at 3.5 are partly outside their boxes; the tarp box at 3.0 is only the free patch between them. Key word 'edge' is not placed as a noun (not one clear place at the still)."}
json.dump(c,open('content/258.json','w'),indent=1,ensure_ascii=False)
