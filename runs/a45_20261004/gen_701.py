import json
T=[i*0.5 for i in range(21)]
S={0:(.30,.22,.34,.27),.5:(.29,.21,.41,.31),1:(.22,.22,.42,.44),1.5:(.14,.21,.56,.49),2:(.05,.18,.66,.47),2.5:(0,.22,.75,.40),
3:(0,.24,.66,.38),3.5:(0,.26,.66,.36),4:(0,.25,.75,.36),4.5:(0,.25,.78,.35),5:(0,.25,.76,.47),5.5:(0,.23,.85,.64),6:(0,.22,.93,.42),
6.5:(0,.28,1,.31),7:(0,.38,1,.25),7.5:(0,.38,.90,.29),8:(0,.35,.90,.28),8.5:(0,.33,.90,.28),9:(0,.32,.87,.28),9.5:(0,.34,.89,.28),10:(0,.34,.87,.28)}
R={6:(.76,.65,.24,.25),6.5:(.48,.60,.52,.27),7:(.12,.64,.88,.20),7.5:(.02,.68,.98,.17),8:(.05,.64,.95,.15),8.5:(.04,.62,.96,.15),
9:(0,.61,1,.22),9.5:(0,.63,1,.22),10:(0,.63,1,.14)}
def keys(D): return [({"t":t,"x":D[t][0],"y":D[t][1],"w":D[t][2],"h":D[t][3]} if t in D else {"t":t,"off":True}) for t in T]
sk=keys(S)
d={"mediaId":701,"level":"A","keyWord":"snake","defaultVoice":"male","taps":[
{"phrase":"to move across the sand","target":"the snake","voice":"male","keys":sk},
{"phrase":"to stick its tongue out","target":"the snake","voice":"male","keys":sk},
{"phrase":"to lie under the snake","target":"the rock","voice":"male","keys":keys(R)}],
"stillS":10.0,"nouns":[{"word":"a snake","x":.42,"y":.52,"voice":"male"},{"word":"a rock","x":.45,"y":.67,"voice":"male"},
{"word":"sand","x":.50,"y":.90,"voice":"male"},{"word":"the sky","x":.72,"y":.05,"voice":"male"}],
"question":"Where is the snake lying?","answer":["It","is","lying","on","a","black","rock."],"answerVoice":"male",
"notes":"Only two targets (snake, rock); the rock phrase is a state. The snake lies on the rock from 6.5 s, so the rock box is only the visible dark part below the coils. The tongue is out at 1.0, 4.0-4.5, 7.5 and 9.5 s. The sky is a narrow bright strip at the very top of the still (pill at y 0.05). A blurred grass blade crosses the foreground from 7 s (not used)."}
json.dump(d,open("content/701.json","w"),indent=1,ensure_ascii=False)
