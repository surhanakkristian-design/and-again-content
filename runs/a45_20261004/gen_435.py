import json
T=[i*0.5 for i in range(21)]
woman={0.0:(.05,.17,.42,.44),0.5:(0,.16,.48,.51),1.0:(0,.19,.50,.52),1.5:(0,.21,.49,.48),2.0:(0,.15,.49,.52),2.5:(0,.16,.49,.52),
3.0:(0,0,1,.67),3.5:(0,0,1,.65),4.0:(0,0,1,.60),4.5:(0,0,.92,.34),5.0:(0,0,.90,.50),
5.5:(.08,.27,.30,.49),6.0:(0,.26,.31,.40),6.5:(0,.26,.36,.41),7.0:(0,.26,.36,.42),7.5:(0,.26,.32,.42),8.0:(0,.24,.34,.43),
8.5:(0,.21,.34,.46),9.0:(0,.15,.23,.47),9.5:(0,0,.22,.48),10.0:(0,0,.20,.37)}
man={0.0:(.47,.11,.43,.50),0.5:(.48,.10,.46,.54),1.0:(.50,.13,.50,.59),1.5:(.49,.16,.51,.53),2.0:(.49,.08,.51,.60),2.5:(.49,.09,.51,.60),
5.5:(.38,.17,.59,.59),6.0:(.31,.19,.66,.47),6.5:(.36,.20,.60,.47),7.0:(.36,.21,.62,.47),7.5:(.32,.20,.60,.48),8.0:(.34,.18,.64,.49),
8.5:(.34,.14,.56,.61),9.0:(.23,.08,.62,.54),9.5:(.22,0,.62,.48),10.0:(.20,0,.72,.37)}
dog={5.5:(.30,.86,.60,.14),6.0:(.28,.86,.55,.14),6.5:(.33,.86,.50,.14),7.0:(.28,.86,.45,.14),7.5:(.30,.86,.45,.14),8.0:(.25,.86,.45,.14),
8.5:(.28,.86,.42,.14),9.0:(.25,.84,.55,.16),9.5:(.20,.65,.78,.31),10.0:(.15,.62,.75,.28)}
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
c={"mediaId":435,"level":"A","keyWord":"leather","defaultVoice":"male",
"taps":[
 {"phrase":"to brush a leather belt","target":"the woman","voice":"female","keys":keys(woman)},
 {"phrase":"to put on a jacket","target":"the man","voice":"male","keys":keys(man)},
 {"phrase":"to lie under the table","target":"the dog","voice":"male","keys":keys(dog)}],
"stillS":6.5,
"nouns":[{"word":"a woman","x":.20,"y":.50,"voice":"female"},{"word":"a jacket","x":.70,"y":.42,"voice":"male"},
 {"word":"a belt","x":.30,"y":.69,"voice":"male"},{"word":"a table","x":.62,"y":.81,"voice":"male"}],
"question":"What is the man wearing?",
"answer":["He","is","wearing","a","leather","jacket."],
"answerVoice":"male",
"notes":"Woman and man are both main persons -> defaultVoice by evenId (male). The woman brushes the belt only in the close-ups 3.0-4.0 s where just her hands, apron and shirt are visible; the man is off in 3.0-5.0 s. At 5.5 s the man's right arm overlaps the woman: split at x 0.38, his arm falls in her box. The dog is identifiable only from 5.5 s (under the table); earlier a blurred shape at the bottom, set off. 'a jacket' pill stands on the man (no 'a man' noun)."}
json.dump(c,open("content/435.json","w"),indent=1)
