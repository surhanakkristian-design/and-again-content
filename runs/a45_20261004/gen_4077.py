import json
T=[i*0.5 for i in range(31)]
def mk(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
blue={0.0:(0,.25,.63,.41),0.5:(0,.23,.64,.43),1.0:(0,.23,.64,.43),1.5:(0,.23,.64,.43),2.0:(0,.25,.63,.41),2.5:(0,.18,.57,.46),
6.5:(0,.02,.43,.60),7.0:(.05,.20,.44,.50),7.5:(0,.26,.57,.44),8.0:(0,.25,.47,.44),8.5:(0,.28,.50,.41),9.0:(0,.27,.48,.43),
9.5:(0,.14,1,.60),10.0:(0,0,1,.66),10.5:(0,0,1,.66),11.0:(0,0,1,.66),11.5:(0,0,1,.66),
12.0:(0,0,.82,1),12.5:(0,0,.82,1),13.0:(0,0,.82,1),13.5:(0,0,.82,1),14.0:(0,.22,.49,.48),14.5:(0,.22,.50,.48),15.0:(0,.22,.48,.48)}
white={0.0:(.63,.29,.37,.37),0.5:(.64,.29,.36,.37),1.0:(.64,.29,.36,.37),1.5:(.64,.29,.36,.37),2.0:(.63,.29,.37,.37),2.5:(.57,.28,.43,.36),
3.0:(.43,.27,.57,.39),3.5:(.43,.27,.57,.39),4.0:(0,.10,1,.80),4.5:(0,.02,1,.86),5.0:(0,.04,1,.88),5.5:(0,.06,1,.86),6.0:(.41,.29,.59,.42),
6.5:(.47,.30,.53,.40),7.0:(.49,.33,.51,.37),7.5:(.57,.29,.43,.41),8.0:(.47,.30,.53,.39),8.5:(.50,.32,.50,.37),9.0:(.48,.33,.52,.37),
9.5:(.70,.74,.30,.26),10.0:(.70,.66,.30,.34),10.5:(.70,.66,.30,.34),11.0:(.70,.66,.30,.34),11.5:(.70,.66,.30,.34),
12.0:(.82,.28,.18,.72),12.5:(.82,.28,.18,.72),13.0:(.82,.28,.18,.72),13.5:(.82,.28,.18,.72),14.0:(.49,.32,.51,.38),14.5:(.50,.32,.50,.38),15.0:(.48,.34,.52,.36)}
moon={}
for t in [0.0,0.5,1.0,1.5,2.0,3.0,3.5]: moon[t]=(.37,0,.36,.14)
for t in [6.0,7.0,7.5,8.0,8.5,9.0,14.0,14.5,15.0]: moon[t]=(.34,0,.37,.20)
moon[6.5]=(.43,0,.27,.20)
d={"mediaId":4077,"level":"A","keyWord":"asleep","defaultVoice":"male",
"taps":[{"phrase":"to fly out of the nest","target":"the blue bird","voice":"male","keys":mk(blue)},
{"phrase":"to fall asleep again","target":"the white bird","voice":"male","keys":mk(white)},
{"phrase":"to shine in the sky","target":"the moon","voice":"male","keys":mk(moon)}],
"stillS":14.5,
"nouns":[{"word":"the moon","x":.52,"y":.08,"voice":"male"},{"word":"the sky","x":.22,"y":.19,"voice":"male"},{"word":"a bird","x":.74,"y":.55,"voice":"male"},{"word":"a nest","x":.50,"y":.74,"voice":"male"}],
"question":"What is the white bird doing?","answer":["It","is","sleeping","in","the","nest."],"answerVoice":"male",
"notes":"Several shots. Blue bird: off at 3.0-6.0 s (flown out of the picture / close-up of the white bird). At the start the blue bird's head lies on the white bird, the boxes are split at about x .63, so a strip of his face falls outside his box. 6.5 s: the hovering blue bird's head is in front of the moon; moon box narrowed to the right part, his box ends at x .43. Close-ups 9.5-13.5 s: the white bird is only a blurred body / part of her face at the right edge. 'to fall asleep again': the white bird opens her eyes at 5-7 s and closes them from 7.5 s, the blue bird stays awake; both sleep at 0-2 s, so 'to sleep' alone would fit both. 'a bird' pill is on the white bird; no other noun names the blue bird. Key word 'asleep' is in a phrase, the answer uses 'sleeping'."}
json.dump(d,open("content/4077.json","w"),indent=1)
