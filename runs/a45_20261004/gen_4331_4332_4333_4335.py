import json
def K(times, d):
    out=[]
    for t in times:
        v=d.get(t)
        if v is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
T25=[i*0.5 for i in range(25)]; T19=[i*0.5 for i in range(19)]

# ---------- 4331
W={0.0:(.38,0,.22,.22),0.5:(.40,0,.20,.25),1.0:(.38,0,.22,.33),1.5:(.39,.03,.23,.36),2.0:(.37,.07,.25,.40),2.5:(.38,.10,.26,.43),
3.0:(.36,.13,.28,.46),3.5:(.37,.12,.30,.51),4.0:(.35,.10,.33,.60),4.5:(.34,.13,.38,.68),5.0:(.32,.23,.42,.77),5.5:(.36,.30,.48,.70),
6.0:(.36,.38,.64,.62),6.5:(.78,.48,.22,.52),8.0:(.74,.45,.26,.55),8.5:(.68,.45,.32,.55),9.0:(.64,.43,.30,.57),9.5:(.61,.42,.32,.58),
10.0:(.56,.40,.32,.60),10.5:(.58,.40,.37,.60),11.0:(.60,.39,.40,.61),11.5:(.61,.40,.39,.60),12.0:(.66,.40,.34,.60)}
C={7.0:(.78,.40,.22,.14),7.5:(.76,.42,.24,.14),8.0:(.20,.38,.54,.24),8.5:(.28,.38,.40,.28),9.0:(.02,.38,.62,.24),9.5:(.02,.38,.59,.24),
10.0:(.02,.30,.54,.30),10.5:(.02,.28,.56,.36),11.0:(.02,.30,.58,.50),11.5:(.02,.28,.59,.50),12.0:(.02,.26,.64,.46)}
json.dump({"mediaId":4331,"level":"A","keyWord":"march","defaultVoice":"female",
"taps":[{"phrase":"to walk at the front","target":"the woman","voice":"female","keys":K(T25,W)},
{"phrase":"to wave small flags","target":"the crowd","voice":"female","keys":K(T25,C)},
{"phrase":"to stand behind a fence","target":"the crowd","voice":"female","keys":K(T25,C)}],
"stillS":9.0,
"nouns":[{"word":"the sky","x":.25,"y":.07,"voice":"female"},{"word":"a flag","x":.33,"y":.37,"voice":"female"},
{"word":"a drum","x":.33,"y":.60,"voice":"female"},{"word":"a road","x":.52,"y":.85,"voice":"female"}],
"question":"Who is walking at the front?","answer":["A","woman","is","walking","at","the","front."],"answerVoice":"female",
"notes":"Drummers stand on both sides of the woman in 4.0-5.5, so one box cannot hold them without crossing hers: no drummer target, the crowd carries two phrases. Woman only partly in the picture at 6.5 (arm, cap edge), not visible 7.0-7.5. From 8.0 she stands at the side (does not walk any more). Crowd box leaves out the people right of the woman. Several flags and drums are in the still; the pills sit on the big flag and on the nearest drummer's drum."},
open('content/4331.json','w'),indent=1)

# ---------- 4332
O={0.0:(0,.17,.30,.83),0.5:(0,.13,.34,.87),1.0:(0,.11,.36,.89),1.5:(0,.08,.32,.92),2.0:(0,.11,.33,.89),2.5:(.84,.15,.16,.85),
3.0:(.76,.08,.24,.92),3.5:(.82,0,.18,1.0),4.0:(.72,0,.28,.72),4.5:(.75,0,.25,.60),5.0:(.67,0,.33,.80),5.5:(.62,.03,.38,.86),
6.0:(.44,.24,.31,.50),6.5:(.50,.25,.25,.51),7.0:(.53,.32,.30,.60),7.5:(.52,.30,.30,.59),8.5:(.14,.22,.37,.55),9.0:(.02,.25,.40,.64)}
B={0.0:(.30,.10,.62,.90),0.5:(.34,.06,.64,.94),1.0:(.36,.04,.64,.96),1.5:(.32,.03,.68,.97),2.0:(.33,.06,.67,.94),2.5:(.10,.09,.74,.91),
3.0:(.03,.02,.73,.98),3.5:(.13,0,.69,1.0),4.0:(.17,0,.55,.86),4.5:(.23,0,.52,.67),5.0:(.22,0,.45,.85),5.5:(.15,0,.47,.93),
6.0:(.09,.23,.35,.54),6.5:(.12,.22,.38,.60),7.0:(.15,.22,.38,.72),7.5:(.12,.22,.40,.63),8.0:(.17,.22,.57,.62),8.5:(.51,.30,.30,.48),9.0:(.42,.42,.27,.47)}
CAR={6.0:(.76,.47,.24,.21),6.5:(.76,.44,.24,.30),7.0:(.83,.52,.17,.34),7.5:(.82,.40,.18,.46),8.0:(.74,.36,.26,.36),8.5:(.81,.34,.19,.36),9.0:(.69,.36,.31,.44)}
json.dump({"mediaId":4332,"level":"B","keyWord":"arrest","defaultVoice":"male",
"taps":[{"phrase":"to arrest a burglar","target":"the police officer","voice":"male","keys":K(T19,O)},
{"phrase":"to carry a grey sack","target":"the burglar","voice":"male","keys":K(T19,B)},
{"phrase":"to be parked nearby","target":"the police car","voice":"male","keys":K(T19,CAR)}],
"stillS":2.0,
"nouns":[{"word":"a police officer","x":.22,"y":.50,"voice":"male"},{"word":"a sack","x":.62,"y":.38,"voice":"male"},
{"word":"handcuffs","x":.50,"y":.66,"voice":"male"},{"word":"a cap","x":.78,"y":.14,"voice":"male"}],
"question":"What is the police officer doing?","answer":["He","is","arresting","a","burglar."],"answerVoice":"male",
"notes":"Officer and burglar touch in every frame: boxes split along the line between them, so the officer's reaching arm often lies in the burglar's box. Officer off at 8.0 (almost fully hidden behind the burglar). The car is partly hidden by the two men from 7.0; its box is the free part right of them. Car phrase is a state (no action fits the car). Crew members are not targets."},
open('content/4332.json','w'),indent=1)

# ---------- 4333
Wm={1.5:(.29,.35,.24,.28),2.0:(.56,.35,.36,.33),2.5:(.45,.34,.37,.33),3.0:(.40,.35,.34,.36),3.5:(.22,.37,.23,.33),4.0:(.30,.34,.36,.59),
4.5:(.13,.33,.51,.39),5.0:(.08,.47,.59,.53),5.5:(.08,.44,.64,.56),6.0:(.10,.37,.60,.63),6.5:(.10,.37,.56,.49),7.0:(.03,.40,.54,.43),
7.5:(.08,.39,.48,.39),8.0:(.03,.40,.46,.33),8.5:(0,.44,.50,.29),9.0:(.19,.42,.30,.25),9.5:(.22,.40,.20,.48),10.0:(.25,.39,.25,.33),
10.5:(.28,.40,.26,.29),11.0:(.30,.42,.32,.26),11.5:(.36,.40,.28,.33),12.0:(.35,.38,.25,.42)}
S={3.5:(.18,.70,.22,.26),4.0:(.10,.58,.20,.37),4.5:(.05,.72,.24,.28),6.5:(.44,.86,.40,.14),7.0:(.38,.83,.34,.17),7.5:(.38,.78,.30,.22),
8.0:(.33,.73,.27,.26),8.5:(.27,.73,.27,.25),9.0:(.33,.68,.27,.29),9.5:(.42,.58,.20,.35),10.0:(.50,.56,.20,.20),10.5:(.54,.58,.19,.18),
11.0:(.46,.68,.24,.14),11.5:(.43,.73,.35,.15),12.0:(.42,.80,.42,.20)}
TR={0.0:(.30,.34,.36,.24),0.5:(.12,.18,.88,.70),1.0:(0,.05,1.0,.90),1.5:(.54,0,.46,.92),2.0:(0,.02,.55,.90),2.5:(0,0,.44,.92),3.0:(0,0,.39,.95),
3.5:(.46,0,.54,.95),4.0:(.67,.03,.33,.90),4.5:(.66,.05,.34,.80),5.0:(0,.08,1.0,.38),5.5:(0,.10,.80,.33),6.0:(0,.15,.45,.22)}
json.dump({"mediaId":4333,"level":"B","keyWord":"platform","defaultVoice":"female",
"taps":[{"phrase":"to pull into the station","target":"the train","voice":"female","keys":K(T25,TR)},
{"phrase":"to step off the train","target":"the woman with the backpack","voice":"female","keys":K(T25,Wm)},
{"phrase":"to topple onto its side","target":"the silver suitcase","voice":"female","keys":K(T25,S)}],
"stillS":0.0,
"nouns":[{"word":"a train","x":.52,"y":.43,"voice":"female"},{"word":"a platform","x":.24,"y":.78,"voice":"female"},
{"word":"tracks","x":.78,"y":.64,"voice":"female"},{"word":"a roof","x":.22,"y":.10,"voice":"female"}],
"question":"Where is the silver suitcase rolling?","answer":["It","is","rolling","along","the","platform."],"answerVoice":"female",
"notes":"While the woman is in the door window / doorway (1.5-4.5) the train fills the frame: the train box is the free part of the train beside her; in 5.0-6.0 it is the part above her. Train off from 6.5 (only a blurred sliver, then gone). Suitcase off at 5.0-6.0 (only the handle or a corner in the picture). Where the suitcase is in front of her legs the woman's box is her head and upper body and the suitcase box is the case body. The suitcase tips at 11.0 and lies on its side from 11.5 (other suitcases in the background also roll, so the phrase is the fall). Train also off at 6.5 although a blurred sliver is left at the edge. 11.0-12.0: the woman is inside the group hug, her box is her own figure (back to the camera, backpack)."},
open('content/4333.json','w'),indent=1)

# ---------- 4335
Wo={0.0:(0,.21,.90,.51),0.5:(0,0,1.0,.83),1.0:(0,.02,1.0,.98),1.5:(0,0,1.0,1.0),2.0:(0,0,1.0,1.0),2.5:(0,0,1.0,1.0),3.0:(0,0,.95,.86),
3.5:(.03,.15,.82,.60),4.0:(.15,.24,.65,.48),4.5:(.25,.27,.50,.43),5.0:(.32,.42,.38,.28),5.5:(.34,.48,.28,.20),6.0:(.37,.35,.33,.30),
6.5:(.40,.38,.31,.26),7.0:(.41,.50,.29,.27),7.5:(.47,.56,.30,.24),8.0:(.53,.63,.31,.33),8.5:(.60,.72,.37,.28),9.0:(.63,.82,.29,.18)}
P={0.0:(.42,.72,.30,.14),0.5:(.40,.84,.34,.14),3.0:(.38,.86,.32,.14),3.5:(.36,.76,.30,.14),4.0:(.36,.72,.24,.14)}
wt="the woman in the orange sweater"
json.dump({"mediaId":4335,"level":"A","keyWord":"ask","defaultVoice":"female",
"taps":[{"phrase":"to raise her hand first","target":wt,"voice":"female","keys":K(T19,Wo)},
{"phrase":"to ask the first question","target":wt,"voice":"female","keys":K(T19,Wo)},
{"phrase":"to lie on a notebook","target":"the black pen","voice":"female","keys":K(T19,P)}],
"stillS":0.0,
"nouns":[{"word":"glasses","x":.50,"y":.33,"voice":"female"},{"word":"a sweater","x":.52,"y":.55,"voice":"female"},
{"word":"a notebook","x":.52,"y":.75,"voice":"female"},{"word":"a desk","x":.18,"y":.87,"voice":"female"}],
"question":"What is the woman in front doing?","answer":["She","is","asking","a","question."],"answerVoice":"female",
"notes":"Hard clip: by the end everyone has a hand up and speaks, so the woman's two phrases rest on 'first' (she alone has her hand up and speaks in 0-3 s). No other person has a feature that fits only them (a second woman behind her also wears an orange top, several people wear glasses), so the third target is the pen on her notebook (a state; visible 0.0, 0.5, 3.0-4.0). The woman is small and partly hidden by raised hands from 5.0: please check those boxes. A man behind her also wears glasses; the pill is on hers."},
open('content/4335.json','w'),indent=1)
