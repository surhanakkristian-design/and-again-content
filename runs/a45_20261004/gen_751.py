import json
def K(times, d):
    out=[]
    for t in times:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
T21=[i*0.5 for i in range(21)]; T15=[i*0.5 for i in range(15)]
def save(o): json.dump(o,open(f"content/{o['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# 751
girl={0.0:(.33,.18,.37,.82),0.5:(.33,.17,.33,.28),1.0:(0,.03,1,.97),1.5:(0,.03,1,.97),2.0:(0,.03,1,.97),2.5:(.05,.10,.78,.90),
3.0:(0,.10,1,.90),3.5:(0,.10,1,.90),4.0:(0,.08,1,.92),4.5:(0,0,1,1),5.0:(.05,0,.85,1),5.5:(0,0,1,1),6.0:(.15,.02,.72,.96),
6.5:(.12,.02,.76,.96),7.0:(.13,.02,.74,.96),7.5:(.41,.26,.18,.74),8.0:(.38,.25,.22,.72),8.5:(.39,.24,.18,.73),9.0:(.29,.26,.33,.72),
9.5:(.33,.25,.32,.73),10.0:(.31,.26,.34,.70)}
wom={0.0:(.70,.18,.30,.82),0.5:(.68,.17,.32,.83),7.5:(.59,.18,.41,.82),8.0:(.60,.25,.40,.75),8.5:(.57,.20,.43,.80),
9.0:(.62,.27,.30,.70),9.5:(.66,.28,.28,.70),10.0:(.65,.27,.28,.68)}
g=K(T21,girl); w=K(T21,wom)
save({"mediaId":751,"level":"B","keyWord":"style","defaultVoice":"female","taps":[
{"phrase":"to strike a confident pose","target":"the girl with blue hair","voice":"female","keys":g},
{"phrase":"to reject the beige jacket","target":"the girl with blue hair","voice":"female","keys":g},
{"phrase":"to have a long ponytail","target":"the woman in beige","voice":"female","keys":w}],
"stillS":6.0,"nouns":[{"word":"a scarf","x":.50,"y":.22,"voice":"female"},{"word":"a checkered jacket","x":.32,"y":.33,"voice":"female"},
{"word":"platform boots","x":.50,"y":.82,"voice":"female"},{"word":"a mirror","x":.78,"y":.66,"voice":"female"}],
"question":"What is the blue-haired girl doing?",
"answer":["She","is","striking","a","confident","pose."],"answerVoice":"female",
"notes":"Only two targets: every action of the two friends is shared by both (both hold the jacket, both stare, both get scarves), so the woman gets a state phrase (ponytail visible at 0-0.5 and 7.5; the man has none). The rejection is visible as the wagging finger with closed eyes at 1.5-2.0 and her choosing another jacket. At 5.0 only her leg and boot are in the picture (boxed). Woman is 'off' at 6-7 where only her blurred mirror reflection shows. Mirror pill sits on the glass right of the girl (blurred reflection there). Key word 'style' is abstract, not used as a noun."})

# 752
wo={0.0:(0,.02,.72,.70),0.5:(0,.02,.74,.72),1.0:(0,.02,.68,.84),1.5:(0,0,.70,.86),2.0:(0,0,.80,.45),2.5:(0,0,.84,.24),3.0:(0,0,.90,.20),
3.5:(0,0,.70,.28),4.0:(0,0,1,.30),4.5:(0,0,1,.28),5.0:(0,0,1,.38),5.5:(0,0,1,.38),6.0:(0,0,1,.34),6.5:(0,0,.82,.68),7.0:(0,0,.74,.78),
7.5:(0,.02,.72,.62),8.0:(0,.04,.64,.58),8.5:(0,.04,.60,.58),9.0:(0,.06,.58,.55),9.5:(0,.06,.63,.57),10.0:(0,.08,.62,.54)}
man={0.0:(.80,.47,.20,.20),0.5:(.82,.47,.18,.20),1.0:(.82,.49,.18,.18),1.5:(.82,.52,.18,.18),2.0:(.82,.26,.18,.20),7.0:(.80,.42,.20,.20),
7.5:(.80,.40,.20,.42),8.0:(.74,.28,.26,.72),8.5:(.68,.05,.32,.95),9.0:(.66,.02,.34,.98),9.5:(.64,.04,.36,.96),10.0:(.63,.04,.37,.96)}
bowl={0.0:(.36,.78,.54,.21),0.5:(.38,.80,.55,.20),1.0:(.40,.86,.52,.14),1.5:(.52,.86,.40,.14),2.0:(.50,.58,.42,.21),2.5:(.25,.47,.63,.30),
3.0:(.17,.47,.80,.37),6.5:(.52,.76,.48,.24),7.0:(.30,.81,.58,.18),7.5:(.36,.65,.44,.18),8.0:(.34,.64,.38,.16),8.5:(.31,.63,.35,.15),
9.0:(.31,.62,.33,.14),9.5:(.32,.63,.32,.14),10.0:(.32,.62,.30,.14)}
save({"mediaId":752,"level":"A","keyWord":"sugar","defaultVoice":"female","taps":[
{"phrase":"to drink black coffee","target":"the woman","voice":"female","keys":K(T21,wo)},
{"phrase":"to wear a white T-shirt","target":"the man","voice":"male","keys":K(T21,man)},
{"phrase":"to be full of sugar","target":"the small bowl","voice":"female","keys":K(T21,bowl)}],
"stillS":0.0,"nouns":[{"word":"a cup","x":.48,"y":.45,"voice":"female"},{"word":"sugar","x":.70,"y":.89,"voice":"female"},
{"word":"a table","x":.42,"y":.77,"voice":"female"},{"word":"a window","x":.82,"y":.18,"voice":"female"}],
"question":"What is the woman drinking?","answer":["She","is","drinking","a","cup","of","black","coffee."],"answerVoice":"female",
"notes":"No phrase about spooning or stirring the sugar: the hand with the spoon (2.0-6.0) comes from the lower left and looks like the woman's own, while the description says the partner does it - not decidable from the picture. The man is only an elbow at the right edge until 8.0 (boxed at 0-2.0 and 7.0-7.5, 'off' at 2.5-6.5 where only a blurred forearm crosses the background); his white T-shirt shows from 8.0. In the close-ups 3.0-6.0 the woman is only her torso with the necklace at the top of the picture (boxed there). The bowl looks almost empty in the last shot (8-10) but is full at 0-3.0. The man also holds a cup of coffee but never drinks."})

# 753
man={0.0:(0,.17,.50,.24),0.5:(0,.28,.40,.65),1.5:(0,.08,.22,.92),2.0:(0,.08,.30,.92),2.5:(.20,.08,.18,.92),
3.0:(0,.07,1,.93),3.5:(0,.07,1,.93),4.0:(0,.06,1,.94),4.5:(0,.06,1,.94),5.0:(0,.06,1,.94),5.5:(0,.06,1,.94),6.0:(0,.06,1,.94),6.5:(0,.06,1,.94),
7.0:(.27,.10,.68,.87),7.5:(.29,.10,.66,.87),8.0:(.18,.10,.75,.87),8.5:(.18,.10,.77,.87),9.0:(.20,.10,.74,.88),9.5:(.22,.10,.72,.88),10.0:(.21,.10,.72,.86)}
wom={2.5:(0,.38,.20,.60),7.0:(0,.10,.27,.88),7.5:(0,.11,.29,.87),8.0:(0,.11,.18,.87),8.5:(0,.11,.18,.87),9.0:(0,.15,.19,.83),9.5:(0,.13,.20,.85),10.0:(0,.11,.19,.87)}
m=K(T21,man)
save({"mediaId":753,"level":"A","keyWord":"suit","defaultVoice":"male","taps":[
{"phrase":"to put on a blue jacket","target":"the man","voice":"male","keys":m},
{"phrase":"to look in the mirror","target":"the man","voice":"male","keys":m},
{"phrase":"to touch the man's arm","target":"the woman","voice":"female","keys":K(T21,wom)}],
"stillS":10.0,"nouns":[{"word":"a suit","x":.38,"y":.42,"voice":"male"},{"word":"a mirror","x":.80,"y":.13,"voice":"male"},
{"word":"a dress","x":.10,"y":.62,"voice":"male"},{"word":"shoes","x":.42,"y":.90,"voice":"male"}],
"question":"What is the man wearing?","answer":["He","is","wearing","a","blue","suit."],"answerVoice":"male",
"notes":"From 7.0 the man's box also takes in his reflection in the right mirror (a learner may tap it for 'to look in the mirror'); his reflection in the left mirror lies behind the woman and stays in her box. At 0-2.5 the man is only a hand / a strip at the left edge beside the hanging suit ('off' at 1.0, where just a sliver of his shirt shows) (the man at 1.5-2.5 has a beard and looks different from the man from 3.0 on, treated as the same person). At 2.5 the woman's head overlaps the man's, split at x=.20. The woman touches his arm only at 7.0. The suit is also visible as a reflection in the mirror, so 'a suit' could be put on the mirror slot; mirror pill placed at the top of the right mirror above the reflection."})

# 754
wo={0.0:(.08,.15,.84,.85),0.5:(.18,.08,.72,.92),1.0:(.10,0,.82,.70),1.5:(.17,0,.66,.68),2.0:(.17,0,.66,.60),2.5:(.17,0,.66,.44),
3.0:(0,.02,1,.84),3.5:(0,.02,1,.84),4.0:(0,.02,1,.84),4.5:(0,.15,1,.71),5.0:(0,.02,1,.66),5.5:(.03,.18,.97,.68),
6.0:(.40,.44,.53,.56),6.5:(.50,.40,.47,.60),7.0:(.47,.40,.46,.60)}
fr={0.5:(0,.76,.18,.24),1.0:(.10,.70,.25,.30),1.5:(.05,.68,.92,.32),2.0:(0,.60,.95,.40),2.5:(.05,.44,.88,.56),
3.0:(.18,.86,.66,.14),3.5:(.18,.86,.66,.14),4.0:(.18,.86,.66,.14),4.5:(.20,.86,.66,.14),5.0:(.20,.68,.64,.32),5.5:(.20,.86,.66,.14),
6.0:(0,.57,.40,.43),6.5:(.03,.50,.47,.50),7.0:(.08,.52,.39,.48)}
w=K(T15,wo)
save({"mediaId":754,"level":"B","keyWord":"support","defaultVoice":"female","taps":[
{"phrase":"to grip the metal bar","target":"the woman in the red top","voice":"female","keys":w},
{"phrase":"to struggle with a pull-up","target":"the woman in the red top","voice":"female","keys":w},
{"phrase":"to support her friend's feet","target":"the woman in the hoodie","voice":"female","keys":K(T15,fr)}],
"stillS":7.0,"nouns":[{"word":"a pull-up bar","x":.50,"y":.18,"voice":"female"},{"word":"a hoodie","x":.24,"y":.77,"voice":"female"},
{"word":"a tank top","x":.66,"y":.84,"voice":"female"},{"word":"a bun","x":.74,"y":.47,"voice":"female"}],
"question":"What is the woman in grey doing?","answer":["She","is","supporting","her","friend's","feet."],"answerVoice":"female",
"notes":"The friend in the grey hoodie has short hair and an undercut; taken as a woman as the description says ('her friend'), voice female. At 3.0-5.5 only her hands (and at 5.0 sleeves and the top of her head) are visible at the bottom; boxed as a strip under the woman's box. At 1.5-2.5 the hands hold the shoes, boxes split along the line between shoes and hands. The question is asked in the present continuous although the support happens at 1.5-5.5 and the last shot shows the handshake. 'a bun' = the hair bun of the woman in the red top."})
