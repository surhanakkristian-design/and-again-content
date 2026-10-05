import json
T=[i*0.5 for i in range(21)]
w={0.0:(0,.41,.84,.59),0.5:(.02,.42,.86,.58),1.0:(.08,.45,.78,.55),1.5:(.10,.42,.78,.58),2.0:(0,.45,.84,.55),2.5:(.44,.40,.56,.60),
3.0:(.42,.30,.58,.70),3.5:(.42,.24,.54,.76),4.0:(.18,0,.50,.65),4.5:(.26,0,.48,.50),5.0:(.26,0,.48,.54),5.5:(.24,0,.48,.50),
6.0:(.36,0,.38,.43),6.5:(.41,0,.35,.42),7.0:(.36,0,.33,.41),7.5:(.34,.33,.27,.31),8.0:(.35,.37,.32,.49),8.5:(.26,.26,.50,.71),
9.0:(.26,.17,.58,.83),9.5:(.24,.17,.56,.83),10.0:(.22,.23,.60,.77)}
tw={0.0:(.40,.05,.28,.16),0.5:(.40,.06,.28,.16),1.0:(.40,.07,.28,.16),1.5:(.42,.07,.28,.16),2.0:(.40,.08,.28,.16),2.5:(.42,.08,.28,.16),
3.0:(.38,.07,.28,.16),3.5:(.38,.03,.28,.16)}
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
c={"mediaId":437,"level":"A","keyWord":"leg","defaultVoice":"female",
"taps":[
 {"phrase":"to put her leg up","target":"the woman","voice":"female","keys":keys(w)},
 {"phrase":"to run up the stairs","target":"the woman","voice":"female","keys":keys(w)},
 {"phrase":"to stand on the hill","target":"the tower on the hill","voice":"female","keys":keys(tw)}],
"stillS":0.5,
"nouns":[{"word":"the sky","x":.25,"y":.08,"voice":"female"},{"word":"stairs","x":.60,"y":.35,"voice":"female"},
 {"word":"a shoe","x":.22,"y":.57,"voice":"female"},{"word":"a leg","x":.52,"y":.77,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","running","up","the","stairs."],
"answerVoice":"female",
"notes":"Only one person; two phrases share her. Third target is the watchtower on the hilltop in the first shot (0-3.5 s); in the close-ups it is out of frame or an unreadable blur, and the building behind her in the last shot (7.5-10 s) is a different tower that does not stand on a hill, so the target is off there - verifier please check this choice. 'to put her leg up' is used instead of 'to stretch her leg' to stay at level A. In 4.0-7.0 s only her legs are in frame (box = the legs). 'a leg' pill is on the raised leg (dark leggings) at 0.5 s."}
json.dump(c,open("content/437.json","w"),indent=1)
