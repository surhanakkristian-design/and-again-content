import json
T=[i*0.5 for i in range(31)]
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
h={0.0:(.17,.1,.64,.52),0.5:(.07,0,.88,.72),1.0:(0,0,1,.8),1.5:(0,.13,1,.87),2.0:(.02,.1,.95,.68),
6.0:(.47,.06,.53,.94),6.5:(.08,.03,.92,.97),
8.5:(.18,.08,.55,.43),9.0:(.06,.13,.76,.49),9.5:(.02,.13,.9,.49),10.0:(.02,.08,.88,.42),
10.5:(0,.1,1,.8),11.0:(0,.12,1,.78),11.5:(0,.12,1,.78),12.0:(0,.12,1,.78),12.5:(0,.1,1,.8),13.0:(0,.12,1,.78)}
m={2.5:(0,.27,.66,.73),4.5:(0,.23,.68,.77),5.0:(0,.26,.76,.74),5.5:(0,.26,.8,.74),7.5:(0,.36,.6,.64),8.0:(.02,.33,.82,.67),
8.5:(0,.52,1,.48),9.0:(0,.63,1,.37),9.5:(0,.63,1,.37),10.0:(0,.51,1,.49)}
c={"mediaId":834,"level":"B","keyWord":"hostess","defaultVoice":"female",
"taps":[{"phrase":"to serve a roast turkey","target":"the hostess","voice":"female","keys":keys(h)},
{"phrase":"to pour water from a jug","target":"the hostess","voice":"female","keys":keys(h)},
{"phrase":"to tilt his head back","target":"the man in glasses","voice":"male","keys":keys(m)}],
"stillS":0.0,
"nouns":[{"word":"curtains","x":.82,"y":.12,"voice":"female"},{"word":"a hostess","x":.50,"y":.26,"voice":"female"},
{"word":"a turkey","x":.48,"y":.46,"voice":"female"},{"word":"a salad","x":.47,"y":.88,"voice":"female"}],
"question":"What is the hostess pouring?","answer":["She","is","pouring","water","into","a","guest's","mouth."],"answerVoice":"female",
"notes":"Only two targets: the other guests do nothing that fits only one of them, so the hostess has two phrases. 'The man in glasses' = the guest in front who looks up and gets the water (2.5, 4.5-5.5, 7.5-10.0); his clothes change between shots (blue shirt / teal T-shirt, AI inconsistency). He is OFF in the wide shots 3.0-4.0 and 13.5-15.0, where he cannot be told apart from other guests with glasses - verifier please check. 8.5-10.0: hostess and man overlap; boxes split on a horizontal line above his face (the bottom of her skirt falls in his box). Hostess OFF at 7.0 (empty pan). 'jug' is British (AmE pitcher). Pill 'curtains' sits on the right-hand curtain; the curtains fill the whole background."}
json.dump(c,open('content/834.json','w'),indent=1)
