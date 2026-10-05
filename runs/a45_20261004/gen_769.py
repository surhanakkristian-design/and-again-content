import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} if b else {"t":t,"off":True})
    return out
cat={0.0:(.2,.03,.8,.2),0.5:(.2,.03,.8,.2),4.0:(.22,.23,.45,.15),4.5:(.27,.2,.2,.19),5.0:(.35,.24,.31,.16),5.5:(.35,.24,.31,.16),
 6.0:(.33,.23,.32,.17),6.5:(.33,.27,.27,.17),7.0:(.33,.36,.22,.16),7.5:(.34,.40,.18,.14),8.0:(.34,.45,.2,.15),8.5:(.33,.47,.2,.14),
 9.0:(.33,.47,.2,.14),9.5:(.34,.46,.2,.14),10.0:(.33,.45,.19,.14)}
man={1.0:(.28,0,.72,.26),1.5:(.18,0,.82,.46),2.0:(.15,0,.85,.37),2.5:(.2,0,.8,.4),3.0:(.2,0,.8,.57),3.5:(.26,0,.74,.42),
 4.0:(.33,0,.67,.22),4.5:(.48,.15,.52,.37),5.0:(.67,.17,.33,.4),5.5:(.67,.2,.33,.42),6.0:(.66,.25,.34,.32),6.5:(.61,.32,.39,.27),
 7.0:(.56,.36,.44,.32),7.5:(.53,.03,.47,.7),8.0:(.54,0,.46,.78),8.5:(.54,.02,.46,.72),9.0:(.54,0,.46,.9),9.5:(.55,0,.45,.9),10.0:(.53,0,.47,.74)}
wom={4.5:(0,.18,.16,.34),5.0:(0,.08,.3,.48),5.5:(0,.06,.3,.53),6.0:(0,0,.31,.57),6.5:(0,0,.31,.6),7.0:(0,0,.25,.72),7.5:(0,0,.34,.86),
 8.0:(0,.03,.33,.8),8.5:(0,.05,.32,.75),9.0:(0,.08,.32,.84),9.5:(0,.08,.33,.84),10.0:(0,.08,.31,.72)}
c={"mediaId":769,"level":"A","keyWord":"teaspoon","defaultVoice":"male",
"taps":[{"phrase":"to sleep by the window","target":"the cat","voice":"male","keys":keys(cat)},
{"phrase":"to have a beard","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to have long hair","target":"the woman","voice":"female","keys":keys(wom)}],
"stillS":4.0,
"nouns":[{"word":"a teaspoon","x":.52,"y":.45,"voice":"male"},{"word":"a cat","x":.38,"y":.31,"voice":"male"},
{"word":"sugar","x":.2,"y":.68,"voice":"male"},{"word":"tea","x":.55,"y":.82,"voice":"male"}],
"question":"What is the man holding?","answer":["He","is","holding","a","teaspoon."],"answerVoice":"male",
"notes":"Both people stir and taste, so the people phrases are states (beard / long hair). Before 7.0 s only hands are visible: the single big hand 1.0-4.5 s and the right hand 5.0-7.0 s are boxed as the man, the left arm from 4.5 s as the woman. Cat is off 1.0-3.5 s (hidden behind the hand). Boxes split between cat and the man's hand from 7.5 s."}
json.dump(c,open('content/769.json','w'),indent=1,ensure_ascii=False)
