import json
T=[i*0.5 for i in range(21)]
man={0.0:(.26,.21,.36,.44),0.5:(.31,.15,.40,.40),1.0:(.30,.11,.38,.55),1.5:(.26,.13,.44,.52),2.0:(.20,.23,.45,.31),2.5:(.25,.09,.56,.38),3.0:(.32,.23,.43,.50),3.5:(.39,.54,.44,.38),4.0:(.37,.21,.36,.32),4.5:(.30,.46,.45,.40),5.0:(.15,.23,.58,.42),5.5:(.15,.19,.46,.34),6.0:(.10,.27,.40,.40),6.5:(.08,.20,.33,.46)}
an={6.0:(.74,.33,.25,.17),6.5:(.69,.34,.27,.16),7.0:(.61,.34,.26,.16),7.5:(.55,.34,.28,.16),8.0:(.53,.35,.27,.17),8.5:(.54,.35,.27,.17),9.0:(.55,.35,.27,.17),9.5:(.58,.36,.28,.17),10.0:(.59,.35,.28,.17)}
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
c={"mediaId":4007,"level":"A","keyWord":"dark","defaultVoice":"male",
"taps":[
 {"phrase":"to jump off a wall","target":"the man with no shoes","voice":"male","keys":keys(man)},
 {"phrase":"to turn in the air","target":"the man with no shoes","voice":"male","keys":keys(man)},
 {"phrase":"to stand far away","target":"the two animals","voice":"male","keys":keys(an)}],
"stillS":8.5,
"nouns":[{"word":"a trampoline","x":.78,"y":.92,"voice":"male"},{"word":"animals","x":.68,"y":.43,"voice":"male"},{"word":"stones","x":.62,"y":.63,"voice":"male"},{"word":"a wall","x":.17,"y":.60,"voice":"male"}],
"question":"What is the man jumping onto?",
"answer":["He","is","jumping","onto","a","trampoline."],
"answerVoice":"male",
"notes":"Key word 'dark' is not a placeable noun, so it is not among the nouns. The jumper (white T-shirt, striped trousers, bare feet) is marked off from 7.0 s: he stands in a tight group at the left edge and cannot be told apart safely. The two animals look like lionesses; named 'animals' to stay safe. At 6.0 s only their eyes glow. Clip seems to replay the jump (5.0-5.5 s)."}
json.dump(c,open("content/4007.json","w"),indent=1)
