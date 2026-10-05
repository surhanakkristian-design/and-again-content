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
W={1.0:(0,.86,.20,1),1.5:(0,.51,.57,1),2.0:(0,0,.58,1),2.5:(0,0,.56,1),3.0:(0,0,.49,1),3.5:(0,0,.43,1),4.0:(0,0,.44,1),4.5:(0,0,.45,1),5.0:(0,0,.43,1),5.5:(0,0,.55,1),6.0:(0,.10,.41,1)}
M={0.0:(.70,.33,1,.63),2.0:(.80,0,1,.20),2.5:(.57,0,1,.30),3.0:(.50,0,1,.53),3.5:(.44,0,1,1),4.0:(.45,0,1,1),4.5:(.46,0,1,1),5.0:(.44,0,1,1),5.5:(.56,0,1,1),6.0:(.80,0,1,1),6.5:(.82,0,1,1)}
C={0.5:(.74,.37,.96,.51),1.0:(.74,.38,.96,.52),1.5:(.74,.38,.96,.52),2.0:(.72,.38,.96,.52),2.5:(.74,.40,.98,.54),3.0:(.74,.54,.94,.68),6.0:(.42,.49,.79,.65),6.5:(.28,.51,.76,.70),7.0:(.15,.56,.66,.76),7.5:(.01,.60,.57,.80),8.0:(.01,.63,.57,.82),8.5:(.14,.59,.68,.78),9.0:(.26,.50,.79,.70),9.5:(.70,.47,.94,.62),10.0:(.76,.42,1,.58)}
c={"mediaId":254,"level":"A","keyWord":"earth","defaultVoice":"female",
"taps":[
 {"phrase":"to stop the turning globe","target":"the woman","voice":"female","keys":mk(W)},
 {"phrase":"to have dark curly hair","target":"the man","voice":"male","keys":mk(M)},
 {"phrase":"to sleep by the window","target":"the cat","voice":"female","keys":mk(C)}],
"stillS":8.0,
"nouns":[{"word":"the sun","x":0.78,"y":0.22,"voice":"female"},{"word":"the sea","x":0.36,"y":0.48,"voice":"female"},{"word":"a cat","x":0.25,"y":0.73,"voice":"female"},{"word":"a globe","x":0.32,"y":0.90,"voice":"female"}],
"question":"What is the cat doing?",
"answer":["The","cat","is","sleeping","by","the","window."],
"answerVoice":"female",
"notes":"Close two-shot: woman (left, yellow-brown sleeve) and man (right, curly hair) are split along a vertical line between the heads, so the woman's pointing hand is partly cut in 3.0-5.5 where it reaches under the man's head. At 0.0 only the man's hand (teal sleeve) is visible, at 1.0-1.5 only the woman's hand. The man's phrase is a state (he also points at 4.5, so pointing is not unique). Cat set off 3.5-5.5 (hidden behind globe/heads, only a sliver at 3.5 and 5.5). Key word 'earth' is not a separate visible noun; 'a globe' used."}
json.dump(c,open('content/254.json','w'),indent=1,ensure_ascii=False)
