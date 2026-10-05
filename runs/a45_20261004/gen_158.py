import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
man={0.0:(0,.24,.42,.76),0.5:(0,.24,.47,.76),1.0:(0,.23,.49,.77),1.5:(0,.20,.49,.80),2.0:(0,.13,.43,.87),2.5:(0,.13,.63,.87),
3.0:(0,.10,.52,.90),3.5:(0,.10,.51,.90),4.0:(0,.10,.49,.90),4.5:(0,.10,.55,.90),5.0:(0,.13,.55,.87),5.5:(0,.20,.47,.80),
6.0:(0,.18,.52,.82),6.5:(0,.22,.55,.78),7.0:(0,.26,.53,.74),7.5:(0,.26,.50,.74),8.0:(0,.24,.49,.76),8.5:(0,.22,.53,.78),
9.0:(0,.25,.50,.75),9.5:(0,0,.27,1)}
woman={0.0:(.60,.27,.40,.73),0.5:(.49,.26,.51,.74),1.0:(.50,.25,.50,.75),1.5:(.50,.22,.50,.78),2.0:(.60,.18,.40,.82),2.5:(.63,.17,.37,.83),
3.0:(.66,.18,.34,.82),3.5:(.65,.18,.35,.82),4.0:(.62,.17,.38,.83),4.5:(.66,.17,.34,.83),5.0:(.70,.20,.30,.80),5.5:(.48,.25,.52,.75),
6.0:(.54,.22,.46,.78),6.5:(.69,.25,.31,.75),7.0:(.70,.28,.30,.72),7.5:(.69,.30,.31,.70),8.0:(.65,.27,.35,.73),8.5:(.64,.25,.36,.75),
9.0:(.52,.28,.48,.72),9.5:(.70,0,.30,1)}
sq={0.0:(.46,.41,.14,.12),2.0:(.48,.41,.12,.12),3.0:(.54,.45,.12,.13),3.5:(.53,.47,.12,.13),4.0:(.50,.48,.12,.13),4.5:(.55,.45,.11,.13),
5.0:(.58,.44,.12,.14),6.5:(.56,.44,.13,.14),7.0:(.56,.44,.14,.14),7.5:(.54,.43,.15,.14),8.0:(.50,.43,.15,.13),8.5:(.53,.43,.11,.13),
9.5:(.38,.37,.25,.19),10.0:(.34,.19,.37,.30)}
c={"mediaId":158,"level":"A","keyWord":"chewing","defaultVoice":"female",
"taps":[
 {"phrase":"to touch his neck","target":"the man","voice":"male","keys":keys(man)},
 {"phrase":"to raise one finger","target":"the woman","voice":"female","keys":keys(woman)},
 {"phrase":"to eat a nut","target":"the squirrel","voice":"female","keys":keys(sq)}],
"stillS":7.0,
"nouns":[{"word":"a squirrel","x":.64,"y":.50,"voice":"female"},{"word":"candy","x":.74,"y":.65,"voice":"female"},
 {"word":"a shirt","x":.22,"y":.70,"voice":"female"},{"word":"leaves","x":.50,"y":.12,"voice":"female"}],
"question":"What are the two people doing?",
"answer":["They","are","chewing","candy","on","a","bench."],
"answerVoice":"female",
"notes":"Squirrel sits between the two people and is small: its box is narrower than 0.18 in most frames so it does not overlap the people's boxes; the woman's box is cut at the squirrel's right edge (her candy hand sticks out a little at 3.0-5.0, 6.5). Squirrel off where it is hidden behind hands/candy (0.5-1.5, 2.5, 5.5, 6.0, 9.0). The squirrel's 'nut' is tiny; clearest at 10.0. Man touches his neck 6.5-7.5; woman raises a finger 8.0-8.5. defaultVoice female: couple, even id."}
json.dump(c,open("content/158.json","w"),indent=1)
