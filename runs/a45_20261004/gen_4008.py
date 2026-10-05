import json
T=[i*0.5 for i in range(21)]
man={0.0:(.58,.11,.42,.32),0.5:(.52,.13,.43,.54),1.0:(.40,.37,.33,.54),1.5:(.43,.30,.30,.60),2.0:(.33,.32,.39,.24),2.5:(.37,.37,.34,.20),3.0:(.37,.33,.36,.27),3.5:(.30,.29,.33,.31),4.0:(.10,.25,.45,.33),4.5:(.05,.24,.40,.33),5.0:(.12,.27,.36,.41),5.5:(.10,.31,.40,.39),6.0:(.14,.30,.35,.30),6.5:(.17,.29,.42,.31),7.0:(.23,.30,.42,.34),7.5:(.34,.27,.37,.36),8.0:(.42,.16,.37,.46),8.5:(.47,.17,.51,.45),9.0:(.50,.14,.50,.53),9.5:(.72,.14,.28,.27)}
dog={0.0:(.30,.47,.28,.28),0.5:(.21,.49,.29,.27),1.0:(.20,.62,.20,.29),1.5:(.20,.62,.23,.30),2.0:(.19,.56,.33,.27),2.5:(.19,.57,.33,.26),3.0:(.17,.60,.38,.33),3.5:(.08,.60,.47,.34),4.0:(.17,.58,.40,.25),4.5:(.09,.57,.51,.26),5.0:(.05,.68,.56,.26),5.5:(.12,.70,.60,.24),6.0:(.17,.60,.65,.23),6.5:(.27,.60,.58,.23),7.0:(.32,.64,.51,.28),7.5:(.28,.63,.55,.29),8.0:(.29,.62,.54,.21),8.5:(.29,.62,.56,.21),9.0:(.34,.68,.49,.24),9.5:(.29,.62,.54,.30),10.0:(.25,.54,.58,.29)}
tree={t:(0.0,0.0,.42,.23) for t in T}
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
c={"mediaId":4008,"level":"B","keyWord":"shake","defaultVoice":"male",
"taps":[
 {"phrase":"to shake a low branch","target":"the man","voice":"male","keys":keys(man)},
 {"phrase":"to sniff the ground","target":"the dog","voice":"male","keys":keys(dog)},
 {"phrase":"to bear yellow fruit","target":"the apple tree","voice":"male","keys":keys(tree)}],
"stillS":10.0,
"nouns":[{"word":"a trunk","x":.15,"y":.47,"voice":"male"},{"word":"a fence","x":.80,"y":.55,"voice":"male"},{"word":"a dog","x":.50,"y":.66,"voice":"male"},{"word":"apples","x":.15,"y":.82,"voice":"male"}],
"question":"What is the man shaking?",
"answer":["He","is","shaking","apples","off","the","tree."],
"answerVoice":"male",
"notes":"Man and dog overlap in the picture from 1.0 to 9.0 s: boxes are split (vertical at 1.0-1.5 s, horizontal elsewhere), so the man's lower legs often lie in the dog's box or in no box. Tree box is only the upper-left crown, kept clear of the man's box. The tree phrase is a state (bear fruit). The shaking itself is short (about 4.0-4.5 s). 'apples' pill is on the fallen apples; apples also hang in the tree. Man off at 10.0 s (only a red corner left)."}
json.dump(c,open("content/4008.json","w"),indent=1)
