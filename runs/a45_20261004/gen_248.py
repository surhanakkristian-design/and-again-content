import json
T=[i*0.5 for i in range(19)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
W=(0,.27,.35,.45)
woman={0.0:(.13,.22,.87,.62),0.5:(.13,.22,.87,.62),1.0:(.13,.05,.87,.60),1.5:(.13,0,.87,.67),2.0:(.13,0,.87,.50),
2.5:(0,0,1,1),3.0:(0,0,1,1),3.5:(0,0,1,1),4.0:(0,0,1,1),4.5:(0,0,1,1),5.0:(0,0,1,1),5.5:(0,.05,1,.95),6.0:(0,.12,1,.88),
6.5:W,7.0:W,7.5:W,8.0:W,8.5:W,9.0:W}
M=(.57,.33,.43,.67)
man={t:M for t in (6.5,7.0,7.5,8.0,8.5,9.0)}
K=(.36,.43,.20,.18)
kettle={t:K for t in (6.5,7.0,7.5,8.0,8.5,9.0)}
c={"mediaId":248,"level":"B","keyWord":"dropper","defaultVoice":"female",
"taps":[{"phrase":"to measure out the drops","target":"the woman","voice":"female","keys":keys(woman)},
{"phrase":"to swallow the medicine","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to give off steam","target":"the copper kettle","voice":"female","keys":keys(kettle)}],
"stillS":6.0,
"nouns":[{"word":"a dropper","x":.18,"y":.66,"voice":"female"},{"word":"a wooden spoon","x":.52,"y":.81,"voice":"female"},
{"word":"an apron","x":.42,"y":.93,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","measuring","out","drops","with","a","dropper."],"answerVoice":"female",
"notes":"Animated clip. 0.0-5.0 s shows only the woman's hand(s) and torso with the dropper; her box covers the hand (0-2 s) or the whole frame (2.5-5 s). In the wide shot (6.5-9 s) her arm reaches across the kettle to the man; her box stops at x .36 so the reaching arm is outside. Kettle: steam is faint (thin wisp above the spout) - check 'to give off steam'. The man swallows from the spoon only around 6.5-7.0 s. The scoop is called 'a wooden spoon' as in the description (it is deep, ladle-like)."}
json.dump(c,open("content/248.json","w"),indent=1)
