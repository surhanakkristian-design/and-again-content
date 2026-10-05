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
B={0:(0,.14,.60,1),.5:(0,.14,.59,1),1:(0,.17,.56,1),1.5:(0,.17,.54,1),2:(0,.17,.51,1),2.5:(0,.16,.45,1),
3:(0,.14,.46,1),3.5:(0,.13,.40,1),4:(0,.13,.50,1),4.5:(0,.10,.46,1),5:(0,.10,.47,1),5.5:(0,.16,.51,1),6:(0,.16,.47,1),
6.5:(0,.08,1,1),7:(0,.08,1,1),7.5:(0,.08,1,1),8:(0,.08,1,1),8.5:(0,.08,1,1),
9:(0,.25,.35,1),9.5:(0,.26,.29,1),10:(0,.25,.26,1)}
F={0:(.61,.27,1,.86),.5:(.60,.28,1,.87),1:(.57,.28,1,.90),1.5:(.56,.29,1,.93),2:(.52,.25,1,.80),2.5:(.46,.27,1,1),
3:(.47,.20,1,.90),3.5:(.41,.20,1,.92),4:(.51,.22,1,.84),4.5:(.47,.26,1,.88),5:(.48,.28,1,.95),5.5:(.52,.28,1,.95),6:(.48,.22,1,.88)}
M={9:(.36,.25,1,.95),9.5:(.30,.24,1,.94),10:(.27,.24,1,.86)}
c={"mediaId":313,"level":"B","keyWord":"foundation","defaultVoice":"female",
"taps":[
{"phrase":"to blend in the foundation","target":"the woman in white","voice":"female","keys":keys(F)},
{"phrase":"to turn her head sideways","target":"the woman with braids","voice":"female","keys":keys(B)},
{"phrase":"to reflect both women","target":"the mirror","voice":"female","keys":keys(M)}],
"stillS":10.0,
"nouns":[{"word":"parrots","x":.42,"y":.17,"voice":"female"},{"word":"braids","x":.14,"y":.36,"voice":"female"},
{"word":"a mirror","x":.68,"y":.32,"voice":"female"},{"word":"foundation","x":.48,"y":.87,"voice":"female"}],
"question":"What is the woman in white doing?",
"answer":["She","is","blending","foundation","with","a","sponge."],
"answerVoice":"female",
"notes":"0-6.0 s the two women overlap (the woman in white leans in behind the other one's face, her hand with the sponge is on the cheek): boxes split by a vertical line near the profile, the helping hand belongs to the woman in white. 6.5-8.5 s only the woman with braids (she turns her head from side to side). 9.0-10.0 s the woman in white is only a reflection, so she is off and the mirror (with both reflections) is the third target; the real woman with braids is the back view on the left. 'foundation' sits on the three bottles of foundation (no other clear place at 10.0 s). 'braids' is on the real woman's head; her reflection in the mirror also shows braids. 'parrots' = the two lovebirds above the mirror (one flying, one perched)."}
json.dump(c,open("content/313.json","w"),indent=1,ensure_ascii=False)
