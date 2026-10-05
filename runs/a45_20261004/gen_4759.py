import json
T=[i*0.5 for i in range(25)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
baker={2.0:(.76,.02,.24,.60),2.5:(.78,0,.22,.62),3.0:(.80,.04,.20,.70),3.5:(.66,.56,.34,.18),4.0:(.64,.47,.36,.15),
4.5:(.82,.38,.18,.18),5.0:(.70,.49,.30,.14),5.5:(.76,.49,.24,.14),6.5:(0,0,1.0,1.0),7.0:(.18,.02,.82,.98),
7.5:(.26,.05,.74,.95),8.0:(.24,.04,.76,.96),8.5:(.24,.06,.76,.94),9.0:(.21,.06,.79,.94),9.5:(.18,.04,.82,.96),
10.0:(.14,.04,.86,.96),10.5:(.14,.04,.86,.96),11.0:(.14,.14,.86,.86),11.5:(.24,.24,.76,.76),12.0:(.58,.16,.42,.84)}
crowd={2.0:(0,.14,.76,.37),2.5:(0,.14,.78,.36),3.0:(0,.16,.80,.44),3.5:(0,.14,.97,.42),4.0:(0,.13,.90,.34),
4.5:(0,.11,.82,.39),5.0:(0,.13,.92,.36),5.5:(0,.13,.97,.36),6.0:(0,.11,.98,.40),12.0:(.12,.29,.46,.31)}
c={"mediaId":4759,"level":"B","keyWord":"baker","defaultVoice":"male",
"taps":[
 {"phrase":"to listen to a baguette","target":"the baker","voice":"male","keys":keys(baker)},
 {"phrase":"to arrange trays of croissants","target":"the baker","voice":"male","keys":keys(baker)},
 {"phrase":"to gather outside the window","target":"the crowd","voice":"male","keys":keys(crowd)}],
"stillS":11.0,
"nouns":[{"word":"a baker","x":.58,"y":.30,"voice":"male"},{"word":"a baguette","x":.24,"y":.60,"voice":"male"},
 {"word":"an apron","x":.62,"y":.76,"voice":"male"},{"word":"croissants","x":.18,"y":.93,"voice":"male"}],
"question":"What is the man doing?",
"answer":["The","baker","is","holding","a","baguette","to","his","ear."],
"answerVoice":"male",
"notes":"0.0-1.5 s (oven shot) shows no target, only a hand at 0.5 s. In the window shot (2.0-5.5 s) only the baker's head, arm or hand is in the picture at the right edge; his box is the right column / the arm and is cut where the crowd stands behind him, so at 2.5 and 3.0 s his outstretched hand lies outside his box. At 12.0 s the clapping men outside the door are boxed as the crowd and the baker box is cut at x .58 (his forearms and the baguette cross in front of them). Dim figures behind the door glass at 6.5-11.5 s are not boxed. Nouns 'a baker' (head) and 'an apron' are both on the same large figure, pills 0.46 apart in y."}
json.dump(c,open("content/4759.json","w"),indent=1)
