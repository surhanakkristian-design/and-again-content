import json
W={2.0:(0,0,1,1),2.5:(0,.06,1,.94),3.0:(.50,.15,.50,.85),5.5:(.05,.10,.95,.90),9.0:(0,.06,1,.94),9.5:(0,.02,1,.98),
11.0:(.02,.15,.80,.55),11.5:(.05,.09,.90,.61),12.0:(.03,0,.92,.69),12.5:(.05,0,.93,.69),13.0:(.03,0,.90,.67),13.5:(.03,0,.92,.67),
14.0:(.03,0,.92,.68),14.5:(.03,0,.95,.68),15.0:(.02,0,.96,.65)}
B={11.0:(.10,.71,.76,.27),11.5:(.12,.71,.72,.28),12.0:(.10,.70,.76,.28),12.5:(.08,.70,.80,.29),13.0:(.06,.68,.82,.32),13.5:(.06,.68,.82,.32),
14.0:(.05,.69,.84,.31),14.5:(.05,.69,.85,.31),15.0:(.03,.66,.87,.34)}
H={6.5:(.10,.32,.90,.36),7.0:(.03,.34,.97,.56)}
T=[i/2 for i in range(31)]
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
o={"mediaId":28,"level":"A","keyWord":"subject","defaultVoice":"female",
"taps":[{"phrase":"to smile at the camera","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to lie on the table","target":"the books","voice":"female","keys":keys(B)},
{"phrase":"to play the piano","target":"the hands on the piano","voice":"female","keys":keys(H)}],
"stillS":12.0,
"nouns":[{"word":"hair","x":.55,"y":.10,"voice":"female"},{"word":"a jacket","x":.24,"y":.56,"voice":"female"},
{"word":"books","x":.47,"y":.83,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","smiling","at","the","camera."],"answerVoice":"female",
"notes":"Quick-cut clip. 'the hands on the piano' are only on screen at 6.5-7.0 s (about 1 s); the hand turning the sheet music at 7.5-8.0 and the hands on the calculator at 1.0-1.5 are NOT this target. Woman boxed in the blurred frames 2.0 and 3.0 as well. Key word 'subject' is abstract, so it is not a noun slot; only 3 nouns."}
json.dump(o,open("content/28.json","w"),indent=1)
