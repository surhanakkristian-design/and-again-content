import json
T=[i*0.5 for i in range(21)]
W={0.0:(0,.28,.93,.72),0.5:(.02,.33,.90,.67),1.0:(.03,.31,.60,.69),1.5:(.06,.30,.64,.70),2.0:(0,.33,.70,.67),
 2.5:(0,.47,.70,.53),3.0:(.03,.46,.60,.54),3.5:(.06,.48,.82,.52),4.0:(.20,.41,.42,.59),4.5:(.28,.38,.58,.62),
 5.0:(.18,.41,.56,.59),5.5:(.31,.41,.47,.59),6.0:(.26,.43,.54,.57),6.5:(.26,.42,.52,.58),7.0:(.36,.43,.48,.57),
 7.5:(.31,.44,.44,.56),8.0:(.31,.45,.40,.50),8.5:(.36,.45,.40,.50),9.0:(.33,.48,.38,.48),9.5:(.33,.48,.38,.48),10.0:(.34,.47,.36,.47)}
def keys(d):
    out=[]
    for t in T:
        x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":round(min(w,1-x),2),"h":round(min(h,1-y),2)})
    return out
wk=keys(W)
c={"mediaId":5182,"level":"B","keyWord":"achievement","defaultVoice":"female",
 "taps":[{"phrase":"to add the final brushstrokes","target":"the woman","voice":"female","keys":wk},
         {"phrase":"to wipe her forehead","target":"the woman","voice":"female","keys":wk},
         {"phrase":"to climb down the stepladder","target":"the woman","voice":"female","keys":wk}],
 "stillS":10.0,
 "nouns":[{"word":"a mural","x":.75,"y":.28,"voice":"female"},{"word":"dungarees","x":.54,"y":.62,"voice":"female"},
          {"word":"a stepladder","x":.12,"y":.70,"voice":"female"},{"word":"the pavement","x":.78,"y":.86,"voice":"female"}],
 "question":"What is the woman looking at?","answer":["She","is","looking","up","at","her","mural."],"answerVoice":"female",
 "notes":"Only one real target (the painter); a passer-by's arm appears at the right edge at 6.5-7.5 only, so all three phrases use the woman. She climbs down the stepladder at about 2.0-3.5 s. Key word 'achievement' is abstract, not used as a noun. 'mural' pill sits on the painted waves upper right."}
json.dump(c,open('content/5182.json','w'),indent=1)
