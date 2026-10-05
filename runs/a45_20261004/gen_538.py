import json
T=[i*0.5 for i in range(31)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)})
    return out
M={0.0:(.18,.20,1,.86),0.5:(.33,.20,1,.86),1.0:(.41,.16,1,.86),1.5:(.41,.15,1,.86),2.0:(.42,.14,1,.85),2.5:(.41,.14,1,.85),
   3.0:(.40,.15,1,.86),3.5:(.39,.15,1,.86),4.0:(.39,.13,1,.85),4.5:(.40,.13,1,.85),14.5:(.46,.25,1,1),15.0:(.44,.26,1,1)}
P={0.0:(0,.82,.18,1),0.5:(.09,.40,.33,.75),1.0:(.19,.37,.41,.70),1.5:(.18,.36,.41,.69),2.0:(.17,.37,.42,.71),2.5:(.13,.40,.41,.76),
   3.0:(.13,.32,.40,.69),3.5:(.07,.39,.39,.76),4.0:(.08,.40,.39,.79),4.5:(.09,.40,.40,.78),
   5.0:(.26,.36,.94,1),5.5:(.21,.36,.96,1),6.0:(.23,.24,.96,1),6.5:(.18,.26,.62,.56),7.0:(.17,.23,.64,.57),7.5:(.35,.19,.78,.47),
   8.0:(.74,.14,1,.38),8.5:(.35,.08,1,.50),9.0:(.30,.16,.88,.54),9.5:(.30,.19,.88,.55),10.0:(.44,.09,1,.47),10.5:(.39,.15,.98,.52),
   11.0:(.58,.08,1,.42),11.5:(.52,.10,1,.39),12.0:(.48,.13,1,.47),12.5:(.62,.24,1,.48),13.0:(.68,.31,1,.49),13.5:(.77,.28,1,.44),
   14.0:(.82,.24,1,.38),14.5:(.15,.34,.46,.58),15.0:(.14,.34,.44,.60)}
N={0.0:(.42,.86,1,1),0.5:(.42,.86,1,1),1.0:(.42,.86,1,1),1.5:(.42,.86,1,1),2.0:(.42,.85,1,1),2.5:(.42,.85,1,1),3.0:(.42,.86,1,1),
   3.5:(.42,.86,1,1),4.0:(.42,.85,1,1),4.5:(.42,.85,1,1),
   6.5:(0,.56,1,1),7.0:(0,.57,1,1),7.5:(0,.47,1,1),8.0:(0,.38,1,1),8.5:(0,.50,1,1),9.0:(0,.54,1,1),9.5:(0,.55,1,1),10.0:(0,.47,1,1),
   10.5:(0,.52,1,1),11.0:(0,.42,1,1),11.5:(0,.17,.52,1),12.0:(0,.15,.48,1),12.5:(0,.15,.62,1),13.0:(0,.14,.68,1),13.5:(0,.14,.77,1),14.0:(0,.14,.82,1)}
c={"mediaId":538,"level":"A","keyWord":"pen","defaultVoice":"male",
 "taps":[{"phrase":"to smile at the camera","target":"the man","voice":"male","keys":keys(M)},
         {"phrase":"to leave a blue line","target":"the pen","voice":"male","keys":keys(P)},
         {"phrase":"to lie on the table","target":"the notebook","voice":"male","keys":keys(N)}],
 "stillS":14.5,
 "nouns":[{"word":"a pen","x":.31,"y":.46,"voice":"male"},{"word":"a hat","x":.72,"y":.31,"voice":"male"},
          {"word":"a shirt","x":.70,"y":.80,"voice":"male"}],
 "question":"What is the man holding?",
 "answer":["He","is","holding","a","green","pen."],"answerVoice":"male",
 "notes":"Clip cuts between the man's face (0-4.5 s, 14.5-15 s) and close-ups of the pen and the paper (5-14 s). 'the man' is OFF in the close-ups: only his fingers are in the picture there, and they are not boxed in the face shots either (the hand holding the pen lies inside the pen box). In the face shots the notebook is only the blurry open book at the bottom right. In the close-ups pen and paper overlap, so the notebook box is the paper below / left of the pen and misses the paper behind it. At 0.0 s the pen is half out of frame bottom left; at 14.0 s only its tip is at the right edge. Pen phrase: the man writes too, so 'to leave a blue line' was chosen to fit the pen only. Only 3 nouns: nothing else is clear at the still."}
json.dump(c,open('content/538.json','w'),indent=1)
