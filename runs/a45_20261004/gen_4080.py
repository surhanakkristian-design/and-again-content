import json
T=[i*0.5 for i in range(31)]
def mk(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
M={0.0:(0,.03,1,.40),0.5:(.05,.03,.95,.40),1.0:(.05,.01,.95,.42),1.5:(0,0,1,1),2.5:(0,.08,1,.39),3.0:(.12,.08,.88,.36),
3.5:(.60,.20,.40,.58),4.0:(.32,.18,.68,.57),4.5:(.30,.15,.68,.62),5.0:(.17,.15,.70,.85),5.5:(.30,.18,.70,.70),
6.0:(.27,.20,.73,.62),6.5:(.29,.24,.71,.70),7.0:(.20,.23,.78,.75),7.5:(.21,.18,.72,.82),8.0:(.16,.14,.84,.86),
8.5:(.16,.22,.74,.78),9.0:(.33,0,.67,.27),9.5:(.33,0,.67,.27),10.0:(.33,0,.67,.22),10.5:(.33,0,.67,.22)}
for t in [11.0,11.5,12.0,12.5,13.0,13.5,14.0,14.5,15.0]: M[t]=(0,0,1,1)
G={0.0:(.08,.43,.77,.57),0.5:(.12,.43,.76,.57),1.0:(.15,.43,.60,.57),2.5:(0,.47,1,.53),3.0:(0,.44,.78,.56),
3.5:(0,.40,.60,.60),4.0:(0,.34,.32,.66),4.5:(0,.34,.30,.66),5.0:(0,.38,.17,.62),5.5:(0,.38,.30,.62),
6.0:(0,.36,.27,.64),6.5:(0,.36,.29,.64),7.0:(0,.38,.20,.62),7.5:(0,.38,.21,.62),8.0:(0,.38,.16,.62),
8.5:(0,.38,.16,.62),9.0:(0,.27,1,.73),9.5:(0,.27,1,.73),10.0:(0,.22,1,.78),10.5:(0,.22,1,.78)}
d={"mediaId":4080,"level":"B","keyWord":"wrist","defaultVoice":"female",
"taps":[{"phrase":"to rummage through a drawer","target":"the mother","voice":"female","keys":mk(M)},
{"phrase":"to pull off a hair tie","target":"the mother","voice":"female","keys":mk(M)},
{"phrase":"to sulk in a pink hoodie","target":"the girl","voice":"female","keys":mk(G)}],
"stillS":12.0,
"nouns":[{"word":"eyebrows","x":.48,"y":.17,"voice":"female"},{"word":"lips","x":.50,"y":.49,"voice":"female"},
{"word":"a wrist","x":.40,"y":.69,"voice":"female"},{"word":"a jumper","x":.17,"y":.82,"voice":"female"}],
"question":"Where are the hair ties?","answer":["They","are","on","the","mother's","wrist."],"answerVoice":"female",
"notes":"Two targets only (mother, girl); two phrases share the mother. The two overlap in most shots, so the boxes are split along the line between them: the mother's box leaves out the parts of her body behind the girl, and at 3.5 s her fist holding the hair (above the girl's head) is in neither box. 9.0-10.5 s (girl close-up): the mother's box is only her hand and sleeve at the top. 11.0-15.0 s: mother close-up, girl off (only the top of her hair shows at the bottom edge). 2.0 s is a motion blur, both off. 'a wrist' pill sits on the grey hair ties around the wrist, so 'hair ties' is not a noun. 'a jumper' = the purple sleeve/body at the lower left."}
json.dump(d,open("content/4080.json","w"),indent=1)
