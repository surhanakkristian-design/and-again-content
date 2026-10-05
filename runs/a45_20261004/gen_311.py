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
W={0:(0,.14,.63,.97),.5:(0,.12,.67,.95),1:(0,.08,.52,.80),1.5:(0,0,.50,.74),2:(0,0,.50,.70),2.5:(0,0,.52,.66),
3:(0,0,.53,.66),3.5:(0,0,.58,.66),4:(0,0,.60,.62),4.5:(0,0,.48,.70),5:(0,0,.70,.60),5.5:(0,0,.70,.72),
6:(0,.05,.66,.72),6.5:(0,.05,.60,.76),7:(0,.12,.58,.90),7.5:(0,.12,.72,.86),8:(0,0,.66,.76),8.5:(0,0,.70,.62),
9:(0,0,.48,.86),9.5:(0,.08,.48,.90),10:(0,.12,.48,.86)}
M={0:(.64,.20,1,.58),.5:(.68,.20,1,.58),1:(.52,.18,1,.57),1.5:(.52,.14,1,.52),2:(.52,.05,1,.50),2.5:(.54,.05,1,.48),
3:(.55,0,1,.50),3.5:(.58,0,1,.48),4:(.62,0,1,.52),4.5:(.52,0,1,.52),5:(.70,0,1,.52),5.5:(.71,.02,1,.70),
6:(.67,.08,1,.68),6.5:(.62,.08,1,.72),7:(.60,.16,1,.82),7.5:(.74,.18,1,.82),8:(.68,.03,1,.62),8.5:(.71,0,1,.68),
9:(.52,.02,1,.70),9.5:(.62,.10,1,.72),10:(.60,.12,1,.72)}
C={0:(.82,.59,1,.85),.5:(.80,.59,1,.87),1:(.82,.58,1,.86)}
c={"mediaId":311,"level":"A","keyWord":"fork","defaultVoice":"female",
"taps":[
{"phrase":"to hold up a fork","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to open his eyes wide","target":"the man","voice":"male","keys":keys(M)},
{"phrase":"to burn on the table","target":"the candle","voice":"female","keys":keys(C)}],
"stillS":0.0,
"nouns":[{"word":"a fork","x":.47,"y":.47,"voice":"female"},{"word":"a candle","x":.86,"y":.73,"voice":"female"},
{"word":"salad","x":.42,"y":.68,"voice":"female"},{"word":"pasta","x":.50,"y":.84,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","eating","pasta","with","a","fork."],
"answerVoice":"female",
"notes":"The woman's hand and fork are in the foreground and reach across the picture; her box includes arm + fork and is cut where the man begins. The man also has a fork at his bowl (0-4.5 s) but never holds it up. The candle is only in the picture 0-1.0 s (then out of frame): short tap window. At 0.0 s the man's small fork and bowl of pasta are in the background; the slots sit on the big fork and the big bowl in front."}
json.dump(c,open("content/311.json","w"),indent=1,ensure_ascii=False)
