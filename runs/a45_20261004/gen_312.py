import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True})
        else:
            x0,y0,x1,y1=b
            out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
W={0:(.54,.22,.86,.70),.5:(.44,.17,.83,.74),1:(.08,.24,.74,.95),1.5:(.08,.30,.66,1),2:(0,.30,.30,.80),
5:(0,.34,.20,.93),5.5:(.02,.33,.33,1),6:(.08,.34,.56,.95),6.5:(0,.33,.38,1),7:(0,.33,.18,.96)}
D={0:(.87,.22,1,.64),.5:(.84,.15,1,.60),1:(.75,.18,1,.86),1.5:(.68,.42,1,.56),2:(.70,.24,1,.82),2.5:(.18,.27,.73,.97),
3:(.02,.30,.59,.99),3.5:(0,.40,.61,.99),4:(.08,.36,.72,1),4.5:(.40,.30,.87,.97),
6.5:(.72,.29,1,.75),7:(.52,.30,.86,.83),7.5:(.37,.31,.65,.79),8:(.21,.30,.50,.68),8.5:(.17,.30,.44,.67),
9:(.14,.31,.40,.74),9.5:(.14,.31,.39,.72),10:(.15,.32,.35,.60)}
R={2.5:(.74,.05,1,1),3:(.60,.26,1,1),3.5:(.62,.26,1,1),4:(.73,.26,1,1),4.5:(.88,.36,1,1),
5:(.76,.38,1,.52),6:(.78,.36,1,.52),7.5:(.82,.34,1,1),8:(.60,.22,1,1),8.5:(.55,.21,1,1),
9:(.50,.22,1,1),9.5:(.47,.22,1,1),10:(.48,.19,1,1)}
c={"mediaId":312,"level":"B","keyWord":"foul","defaultVoice":"female",
"taps":[
{"phrase":"to dribble the ball","target":"the player with the ball","voice":"female","keys":keys(W)},
{"phrase":"to commit a foul","target":"the defender","voice":"male","keys":keys(D)},
{"phrase":"to blow the whistle","target":"the referee","voice":"female","keys":keys(R)}],
"stillS":9.5,
"nouns":[{"word":"the ceiling","x":.40,"y":.06,"voice":"female"},{"word":"a wristband","x":.25,"y":.47,"voice":"female"},{"word":"a badge","x":.77,"y":.60,"voice":"female"}],
"question":"What is the referee doing?",
"answer":["She","is","blowing","the","whistle","for","a","foul."],
"answerVoice":"female",
"notes":"Cuts/camera jumps: the player with the ball is off 2.5-4.5 s and from 7.5 s; the defender (the big man in purple who grabs her shirt at 1.0-1.5 s and then raises his hands) is off 5.0-6.0 s (only a hand at the edge); other small purple and orange players stand in the background and are NOT in the boxes. The referee's pointing arm crosses the defender; her box is body/head only where he stands (hand-only boxes at 5.0 and 6.0 s; off at 5.5, 6.5, 7.0 s). No 'a whistle' slot: the whistle is tiny in her mouth and a second one hangs on the cord next to the badge. 'foul' is not a visible noun, it is in the answer and in phrase 2. The wristband pill lies next to the defender in the background."}
json.dump(c,open("content/312.json","w"),indent=1,ensure_ascii=False)
