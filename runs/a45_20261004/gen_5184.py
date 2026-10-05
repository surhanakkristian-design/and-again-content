import json
T=[i*0.5 for i in range(25)]
M={0.0:(0,.20,.36,.80),0.5:(0,.33,.52,.67),1.0:(0,.38,.58,.62),1.5:(0,.34,.60,.66),2.0:(0,.32,.57,.68),
 4.5:(0,.24,.92,.76),5.0:(0,.30,.80,.70),5.5:(0,.30,.80,.70),
 6.0:(0,.30,.57,.70),6.5:(0,.31,.58,.69),7.0:(0,.31,.57,.69),7.5:(0,.32,.58,.68),8.0:(0,.32,.57,.68),8.5:(0,.31,.56,.69),
 9.0:(0,.16,.64,.84),9.5:(0,.13,.58,.87),10.0:(.08,.16,.47,.84),10.5:(.03,.20,.59,.80),11.0:(.03,.18,.52,.82),
 11.5:(.03,.18,.57,.82),12.0:(.02,.20,.53,.80)}
W={0.0:(.64,.22,.36,.78),0.5:(.64,.22,.36,.78),1.0:(.65,.19,.35,.81),1.5:(.66,.17,.34,.83),2.0:(.67,.19,.33,.81),
 2.5:(0,.08,1,.92),3.0:(0,.08,1,.92),3.5:(0,.10,1,.90),4.0:(0,.08,1,.92),
 6.0:(.65,.16,.35,.84),6.5:(.65,.16,.35,.84),7.0:(.65,.16,.35,.84),7.5:(.65,.17,.35,.83),8.0:(.57,.22,.43,.78),
 8.5:(.58,.18,.42,.82),9.0:(.64,.22,.36,.78),9.5:(.58,.21,.40,.79),10.0:(.55,.21,.27,.79),10.5:(.62,.24,.28,.76),
 11.0:(.55,.22,.32,.78),11.5:(.60,.22,.30,.78),12.0:(.55,.25,.30,.75)}
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":round(min(w,1-x),2),"h":round(min(h,1-y),2)})
        else: out.append({"t":t,"off":True})
    return out
mk=keys(M); wk=keys(W)
c={"mediaId":5184,"level":"B","keyWord":"romantic","defaultVoice":"female",
 "taps":[{"phrase":"to kneel on one knee","target":"the man","voice":"male","keys":mk},
         {"phrase":"to hold out an engagement ring","target":"the man","voice":"male","keys":mk},
         {"phrase":"to burst into tears","target":"the woman","voice":"female","keys":wk}],
 "stillS":7.0,
 "nouns":[{"word":"a tower","x":.49,"y":.18,"voice":"female"},{"word":"an accordion","x":.53,"y":.36,"voice":"female"},
          {"word":"a ring box","x":.47,"y":.51,"voice":"female"},{"word":"a dress","x":.84,"y":.66,"voice":"female"}],
 "question":"What is the man holding out?","answer":["He","is","holding","out","an","engagement","ring."],"answerVoice":"male",
 "notes":"Cuts: wide proposal shot, close-up of the crying woman (2.5-4.0, man off), close-up of his hands with the ring box (4.5-5.5, woman off), wide again, then the hug (9.5-12.0) where man and woman overlap: boxes split along a vertical line between his head/back and her face/dress. defaultVoice female (couple, evenId true). Accordion player not used as a tap target because his small figure sits right between the couple's boxes."}
json.dump(c,open('content/5184.json','w'),indent=1)
