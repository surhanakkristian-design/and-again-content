import json
times=[i*0.5 for i in range(21)]
def keys(d): return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in times]
bird={0.5:(.66,.52,.22,.22),1.0:(.18,.24,.24,.32),1.5:(0,0,.20,.22),2.0:(.13,0,.28,.32),2.5:(.08,.05,.22,.27),5.5:(.24,.39,.24,.22),6.0:(.24,.59,.74,.19),6.5:(.45,.36,.30,.14),7.0:(.42,.33,.20,.14),7.5:(.42,.33,.20,.14)}
leaves={0.0:(.50,.47,.38,.16),0.5:(.20,.35,.44,.62),1.0:(0,.57,.45,.38),1.5:(.08,.26,.56,.52),2.0:(.38,.38,.45,.37),2.5:(.45,.39,.28,.25),3.0:(.47,.44,.48,.22),3.5:(.43,.41,.38,.17),
4.0:(.36,.39,.30,.18),4.5:(.33,.47,.30,.21),5.0:(.29,.45,.36,.21),5.5:(.49,.44,.21,.21),6.0:(.48,.45,.18,.14),6.5:(.48,.51,.18,.14),7.0:(.47,.48,.18,.14),7.5:(.44,.48,.18,.14),
8.0:(.40,.45,.18,.14),8.5:(.37,.45,.18,.14),9.0:(.35,.46,.18,.14),9.5:(.34,.46,.18,.14),10.0:(.33,.455,.18,.14)}
trees={0.0:(.32,0,.68,.30),0.5:(0,0,1,.16),6.0:(0,0,1,.20),6.5:(0,0,1,.27),7.0:(0,0,1,.30),7.5:(0,0,1,.31),8.0:(0,0,1,.37),8.5:(0,0,1,.38),9.0:(0,0,1,.44),9.5:(0,0,1,.44),10.0:(0,0,1,.45)}
c={"mediaId":615,"level":"A","keyWord":"river","defaultVoice":"male",
"taps":[{"phrase":"to fly over the water","target":"the bird","voice":"male","keys":keys(bird)},
{"phrase":"to move down the river","target":"the leaves","voice":"male","keys":keys(leaves)},
{"phrase":"to grow by the river","target":"the trees","voice":"male","keys":keys(trees)}],
"stillS":5.5,
"nouns":[{"word":"a river","x":.55,"y":.25,"voice":"male"},{"word":"a bird","x":.30,"y":.46,"voice":"male"},{"word":"leaves","x":.63,"y":.57,"voice":"male"},{"word":"stones","x":.68,"y":.86,"voice":"male"}],
"question":"What is moving down the river?","answer":["Two","leaves","are","moving","down","the","river."],"answerVoice":"male",
"notes":"People are only partly in the picture (a face, arms, a leg) and both do the same, so no person target. 'the leaves' = the orange and the yellow leaf as one target: 0.0-2.5 they are still held in hands (box includes the hands); at 1.0 the box holds only the yellow leaf because the orange one lies next to the bird; from 8.0 the leaves are a very small orange dot (minimum box). Bird: stands on a stone at 0.5-2.5 and 5.5, flies off 6.0-7.5; from 8.0 it is only a speck and set off. At 6.0 the leaves lie between the bird's wings: leaves box above, bird box below, the wing tips are outside. Trees box = the upper band (both banks). defaultVoice male: no main person, evenId false."}
json.dump(c,open('content/615.json','w'),indent=1,ensure_ascii=False)
