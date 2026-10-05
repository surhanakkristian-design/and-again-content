import json
T=[i*0.5 for i in range(21)]
F=(0,.05,1,.95)
player={0:F,.5:F,1:F,1.5:F,2:(0,0,.56,1),6.5:(0,.1,.48,.9),7:F,7.5:F,8:F,8.5:F,9:F,9.5:F,10:F}
flag={4.5:(.74,0,.26,.22),5:(.64,.09,.26,.32),5.5:(.68,.15,.26,.31)}
fans={3:(0,0,1,.3),3.5:(.52,0,.48,.45),4:(.2,.08,.8,.36),4.5:(0,.23,1,.34),5:(0,.42,1,.38),5.5:(0,.47,1,.41),6:(0,.28,1,.33)}
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
d={"mediaId":4310,"level":"B","keyWord":"emotional","defaultVoice":"female",
"taps":[{"phrase":"to sob with emotion","target":"the crying player","voice":"female","keys":keys(player)},
{"phrase":"to flutter above the stand","target":"the flag","voice":"female","keys":keys(flag)},
{"phrase":"to hold up green scarves","target":"the fans","voice":"female","keys":keys(fans)}],
"stillS":5.0,
"nouns":[{"word":"a flag","x":.77,"y":.18,"voice":"female"},{"word":"spectators","x":.45,"y":.58,"voice":"female"},
{"word":"footballers","x":.4,"y":.9,"voice":"female"},{"word":"the sky","x":.3,"y":.12,"voice":"female"}],
"question":"What is the footballer in close-up doing?","answer":["She","is","sobbing","with","emotion."],"answerVoice":"female",
"notes":"Key word 'emotional' is an adjective: carried by 'emotion' in phrase 1 and the answer. 'the crying player' = the blonde player of the close-ups (0-2.0, 6.5 left edge, 7.0-10.0); the other player in close-up at 2.5 has wet eyes but sings, she is not boxed. All team-mates sing with a hand on the chest, so no phrase uses that. The fans' scarves are small in the picture (stands 3.0-6.0; 3.0 and 6.0 are blurred). Flag box includes the pole and is cut where the stand begins. At 10.0 the player laughs through her tears."}
json.dump(d,open("content/4310.json","w"),indent=1)
