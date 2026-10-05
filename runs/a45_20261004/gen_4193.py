import json
T=[i*0.5 for i in range(24)]
car={0.0:(.08,.45,.35,.10),1.0:(.08,.50,.33,.13),1.5:(.08,.51,.34,.13),2.0:(.07,.50,.35,.14),2.5:(.07,.50,.35,.14),
3.0:(.02,.38,.96,.54),3.5:(.03,.39,.95,.52),4.0:(.06,.41,.9,.35),4.5:(.1,.42,.86,.31),5.0:(.12,.45,.78,.26),5.5:(.13,.46,.75,.27),
6.0:(.16,.47,.69,.26),6.5:(.17,.47,.66,.26),7.0:(.18,.48,.62,.24),7.5:(.19,.48,.59,.23),8.0:(.2,.46,.57,.24),8.5:(.14,.46,.73,.31),
9.0:(.09,.46,.82,.37),9.5:(.06,.45,.88,.39),10.0:(.06,.44,.88,.40),10.5:(.06,.44,.88,.40),11.0:(.06,.45,.88,.39),11.5:(.06,.45,.88,.39)}
lid={0.0:(0,.55,1,.15),0.5:(0,.38,1,.32),1.0:(.42,.40,.58,.30),1.5:(0,.22,1,.29),2.0:(.1,.15,.9,.35),2.5:(.17,.11,.83,.39),
3.0:(.1,.07,.45,.31),3.5:(.12,.07,.45,.32),4.0:(0,.07,.56,.34),4.5:(0,.06,.57,.36),5.0:(0,.03,.57,.42),5.5:(0,0,.56,.46),
6.0:(0,0,.58,.47),6.5:(0,0,.55,.47),7.0:(0,0,.56,.48),7.5:(0,0,.56,.48),8.0:(0,0,.58,.46),9.5:(0,0,.8,.14),10.0:(0,0,1,.19),
10.5:(0,0,1,.21),11.0:(0,0,1,.28),11.5:(0,0,1,.30)}
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
v="male"
o={"mediaId":4193,"level":"B","keyWord":"underground","defaultVoice":v,
"taps":[{"phrase":"to enter an underground garage","target":"the car","voice":v,"keys":keys(car)},
{"phrase":"to tilt up on hinges","target":"the trapdoor","voice":v,"keys":keys(lid)},
{"phrase":"to gleam under orange lights","target":"the car","voice":v,"keys":keys(car)}],
"stillS":6.5,
"nouns":[{"word":"trees","x":.75,"y":.13,"voice":v},{"word":"a trapdoor","x":.25,"y":.22,"voice":v},
{"word":"a sports car","x":.5,"y":.58,"voice":v},{"word":"paving","x":.5,"y":.90,"voice":v}],
"question":"Where is the car going?","answer":["It","is","entering","an","underground","garage."],"answerVoice":v,
"notes":"Two targets only (car, tilting brick lid = 'the trapdoor'); the house (0-2.5 only, behind the lid) is not used, so the car has two phrases. Car and lid overlap in most frames: boxes are split, the lid box is the part above the car (so the lid's lower end is cut off at 1.5-8.0; at 1.0 the lid box is only its right half because the car sits under its left half). Car off at 0.5 (hidden behind the rising lid); at 0.0 only its roof shows above the lid. Lid off at 8.5-9.0 (only a sliver in the top corner); 9.5-11.5 the lid box is its concrete underside closing from the top (at 11.5 it is shut = the ceiling). 'to gleam under orange lights' fits the last shots (8.5-11.5). 'paving' is also visible behind the opening at 6.5; the pill is on the foreground bricks."}
json.dump(o,open("content/4193.json","w"),indent=1)
