import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
man={0.0:(.50,.30,.50,.70),0.5:(.44,.28,.56,.72),1.0:(.56,.43,.44,.57),1.5:(.80,.37,.20,.45),2.0:(.70,.14,.30,.72),
2.5:(.80,0,.20,.68),3.0:(.82,0,.18,.48),4.5:(.05,0,.95,.88),5.0:(.10,0,.90,1),5.5:(0,.03,1,.97),6.0:(0,.20,1,.80),
6.5:(0,.14,1,.86),7.0:(0,.14,1,.86),7.5:(0,.24,1,.76),8.0:(.13,.25,.87,.75),8.5:(.40,.21,.60,.79),9.0:(.61,.08,.39,.92),
9.5:(.54,.28,.46,.72),10.0:(.50,.27,.50,.73)}
woman={1.0:(0,.15,.42,.42),1.5:(0,.12,.77,.48),2.0:(0,0,.70,.50),2.5:(0,.05,.80,.36),3.0:(0,0,.80,.34),3.5:(.15,0,.55,.24),
4.0:(0,.08,.42,.22),8.5:(0,.38,.20,.24),9.0:(0,.23,.39,.44),9.5:(0,.26,.37,.44),10.0:(0,.26,.43,.32)}
parrot={0.0:(0,0,.20,.38),0.5:(.28,0,.24,.28),1.0:(.62,0,.30,.42),1.5:(.77,0,.23,.36),6.0:(.15,0,.31,.20),6.5:(.08,0,.38,.14),
7.0:(.12,0,.36,.14),7.5:(.12,.03,.36,.21),8.0:(.25,.03,.30,.22),8.5:(.30,.02,.28,.19),9.0:(.40,.04,.20,.42),9.5:(.40,.07,.25,.21),
10.0:(.44,.10,.19,.17)}
c={"mediaId":244,"level":"A","keyWord":"drink","defaultVoice":"male",
"taps":[{"phrase":"to drink orange juice","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to make orange juice","target":"the woman","voice":"female","keys":keys(woman)},
{"phrase":"to sit on a stick","target":"the parrot","voice":"male","keys":keys(parrot)}],
"stillS":9.0,
"nouns":[{"word":"a parrot","x":.50,"y":.18,"voice":"male"},{"word":"a man","x":.78,"y":.45,"voice":"male"},
{"word":"juice","x":.15,"y":.50,"voice":"male"},{"word":"oranges","x":.14,"y":.66,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","drinking","a","glass","of","orange","juice."],"answerVoice":"male",
"notes":"Fast camera moves; in close-ups (6.0-7.5 s) the man's box is cut below the parrot, so the top of his hair is outside. Woman is only hands at 2.5-4.0 s and only an arm with the jug at 8.5 s. Parrot off while hidden behind the man. Key word 'drink' (noun) is not used as a noun label; the answer uses the verb."}
json.dump(c,open("content/244.json","w"),indent=1)
