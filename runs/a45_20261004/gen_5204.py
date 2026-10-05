import json
T=[i*0.5 for i in range(25)]
def K(d):
    out=[]
    for t in T:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True})
        else:
            x0,y0,x1,y1=b; x0=max(0,x0);y0=max(0,y0);x1=min(1,x1);y1=min(1,y1)
            out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
W={0.0:(.25,.20,.84,1),0.5:(.50,.38,1,1),1.0:(.76,.40,1,1),1.5:(.28,.36,1,1),2.0:(.15,.35,.85,1),2.5:(.08,.27,.80,1),
3.0:(.02,.21,.76,1),3.5:(.06,.32,.50,1),4.0:(.04,.31,.60,1),4.5:(.04,.26,.50,1),5.0:(.02,.33,.62,1),5.5:(.05,.33,.62,1),
8.0:(0,.2,.26,1),8.5:(0,.27,.46,1),9.0:(.13,.35,.45,1),9.5:(.19,.36,.47,.97),10.0:(.22,.36,.46,.86),10.5:(.22,.36,.50,.82),
11.0:(.15,.37,.48,.86),11.5:(.24,.37,.50,.85),12.0:(.23,.37,.44,.85)}
M={0.0:(.84,.34,.99,.84),1.0:(.48,.27,.76,.76),3.5:(.52,.21,1,1),4.0:(.61,.18,1,1),4.5:(.60,.19,1,1),5.0:(.67,.21,.96,.68),
5.5:(.66,.38,.96,.70),8.5:(.56,.27,1,1),9.0:(.46,.34,.81,.96),9.5:(.48,.35,.82,.95),10.0:(.47,.35,.80,.83),10.5:(.51,.35,.78,.82),
11.0:(.49,.36,.77,.84),11.5:(.51,.35,.79,.83),12.0:(.45,.35,.78,.82)}
c={"mediaId":5204,"level":"A","keyWord":"improve","defaultVoice":"female",
"taps":[{"phrase":"to pull paper off the wall","target":"the woman","voice":"female","keys":K(W)},
{"phrase":"to use a hammer","target":"the man","voice":"male","keys":K(M)},
{"phrase":"to paint the wall","target":"the woman","voice":"female","keys":K(W)}],
"stillS":10.0,
"nouns":[{"word":"a plant","x":.80,"y":.46,"voice":"female"},{"word":"a tool belt","x":.63,"y":.57,"voice":"female"},
{"word":"a paint roller","x":.44,"y":.66,"voice":"female"},{"word":"tiles","x":.55,"y":.88,"voice":"female"}],
"question":"What is the woman holding?","answer":["She","is","holding","a","paint","roller."],"answerVoice":"female",
"notes":"Key word improve is a verb, not placed as a noun. The man is behind the woman at 0.5 and 1.5-3.0 (only bits of head/arm) -> off; at 0.0 and 1.0 he is in the background, boxes split from the woman (woman box at 1.0 covers only her right part, her left arm is in the man's column). He hammers the shelf only at about 0.5-1.0 (hammer clearly visible at 1.0). 6.0-7.5 painted wall, no people. At 3.5-5.5 the man is a close-up (face/arm with the smoothing float) on the right. At 8.0 the woman is only a sliver at the left edge with the roller. Woman 'paint the wall': roller on the wall at 3.5-5.5."}
json.dump(c,open('content/5204.json','w'),indent=1)
