import json
def keys(T,b):
    return [({"t":t,"off":True} if k is None else {"t":t,"x":k[0],"y":k[1],"w":k[2],"h":k[3]}) for t,k in zip(T,b)]
T24=[i*0.5 for i in range(24)]; T25=[i*0.5 for i in range(25)]
N=None
# 4245
man=[(.45,.32,.22,.2),(.45,.31,.24,.21),(.42,.39,.3,.15),(.38,.3,.42,.26),(.31,.29,.63,.3),(.04,.26,.96,.43),(0,.28,1,.66)]+[N]*17
fall=[N]*7+[(0,0,.82,.66),(0,0,.8,.62),(0,0,.82,.62),(0,0,.82,.62),(0,0,.82,.62),(0,0,.78,.62)]+[(0,0,1,1)]*7+[(.28,.34,.38,.42),(.28,.34,.42,.4),(.26,.36,.42,.5),(.28,.38,.42,.47)]
d={"mediaId":4245,"level":"B","keyWord":"slide","defaultVoice":"male",
"taps":[{"phrase":"to slide on his stomach","target":"the man in turquoise","voice":"male","keys":keys(T24,man)},
{"phrase":"to pour over the wall","target":"the waterfall","voice":"male","keys":keys(T24,fall)},
{"phrase":"to sprint through shallow water","target":"the man in turquoise","voice":"male","keys":keys(T24,man)}],
"stillS":10.0,
"nouns":[{"word":"a waterfall","x":.48,"y":.57,"voice":"male"},{"word":"a palm tree","x":.78,"y":.2,"voice":"male"},
{"word":"moss","x":.2,"y":.85,"voice":"male"},{"word":"the sky","x":.4,"y":.07,"voice":"male"}],
"question":"What is the man in turquoise doing?","answer":["He","is","sliding","on","his","stomach."],"answerVoice":"male",
"notes":"The packet description says the men slide on their backs; in the frames the man in the turquoise T-shirt runs (0-0.5 s) and then slides on his stomach (1.0-3.0 s). He is not identifiable after 3.0 s (off). The waterfall is the second target (3.5-11.5 s); in the close shot 6.5-9.5 s falling water fills the whole frame, so its box is the whole frame (the two men under it are not targets). Several palm trees are visible at 10.0 s; the pill sits on the big one at the right."}
json.dump(d,open("content/4245.json","w"),indent=1)
# 4246
W=[(.28,.23,.29,.3),(.3,.23,.28,.3),(.28,.24,.28,.3),(.27,.24,.29,.3),(.25,.22,.26,.3),(.24,.22,.27,.3),(.26,.22,.29,.3),(.27,.22,.3,.3),
(.28,.21,.31,.3),(.28,.21,.31,.3),(.28,.23,.29,.3),(.28,.24,.28,.3),(.25,.23,.25,.27),(.28,.22,.26,.28),(.25,.24,.25,.3),(.28,.25,.26,.3),
(.22,.24,.25,.28),(.67,.22,.33,.78),(.65,.3,.35,.7),(.7,.3,.3,.7),(.68,.3,.32,.7),(.79,.3,.21,.7),(.02,.4,.27,.38),(.02,.42,.28,.36)]
B=[(.57,.03,.27,.9),(.58,.03,.27,.9),(.56,.04,.24,.92),(.56,.03,.22,.93),(.51,.02,.24,.92),(.51,.03,.28,.9),(.55,.03,.27,.93),(.57,.04,.3,.93),
(.59,.03,.28,.9),(.59,.05,.28,.9),(.57,.06,.29,.94),(.56,.07,.27,.93),(.5,.07,.31,.85),(.54,.06,.27,.85),(.5,.07,.28,.8),(.54,.09,.24,.8),
(.47,.07,.22,.75),(.03,.02,.64,.9),(.03,.05,.62,.95),(.05,.07,.65,.93),(0,.03,.68,.97),(0,.03,.79,.97),(.29,0,.6,1),(.3,0,.62,1)]
d={"mediaId":4246,"level":"A","keyWord":"blue","defaultVoice":"female",
"taps":[{"phrase":"to hold a big bird","target":"the woman","voice":"female","keys":keys(T24,W)},
{"phrase":"to have a blue neck","target":"the bird","voice":"female","keys":keys(T24,B)},
{"phrase":"to laugh a lot","target":"the woman","voice":"female","keys":keys(T24,W)}],
"stillS":2.5,
"nouns":[{"word":"a bird","x":.62,"y":.42,"voice":"female"},{"word":"a cap","x":.42,"y":.28,"voice":"female"},
{"word":"a T-shirt","x":.8,"y":.62,"voice":"female"},{"word":"trees","x":.4,"y":.15,"voice":"female"}],
"question":"What is the woman holding?","answer":["She","is","holding","a","big","blue","bird."],"answerVoice":"female",
"notes":"The bird (a peacock; 'bird' used for level A) is held in front of the woman, so the two overlap all the time. Split: 0-8.0 s the woman's box is her head (cap, face, hair) left of the bird's neck and the bird's box is the column with head, neck, chest and feet; 8.5-10.5 s her face is hidden, so her box is her hair/shoulder/T-shirt at the right; 11.0-11.5 s her box is the cap and face at the left. Her arms and the right part of her T-shirt are outside her box before 8.5 s; the bird's wing at the far left is outside its box. 'to have a blue neck' is a state (the bird does no clear action of its own). Key word 'blue' is used in the model answer, not as a noun label."}
json.dump(d,open("content/4246.json","w"),indent=1)
# 4247
boys=[(.54,.33,.34,.3),(.54,.33,.36,.3),(.5,.34,.4,.3),(.46,.34,.45,.3),(.58,.32,.36,.31),(.44,.32,.56,.4),(.57,.32,.43,.43),(.47,.33,.53,.42),
(.4,.32,.6,.41),(.52,.33,.48,.4),(.4,.33,.6,.4),(.47,.34,.53,.39),(.45,.34,.55,.38),(.39,.34,.61,.35),(.47,.37,.53,.33),(.42,.36,.58,.3),
(.78,.35,.22,.3),(.78,.35,.22,.28),(.24,.39,.49,.26),(.24,.4,.48,.25),(.26,.39,.45,.24),(.28,.39,.43,.23),(.29,.4,.41,.21),(.3,.4,.4,.21),(.31,.4,.38,.2)]
path=[(.38,.64,.22,.36),(.38,.64,.22,.36),(.38,.66,.22,.34),(.38,.66,.22,.34),(.38,.66,.22,.34),(.34,.79,.26,.21),(.32,.84,.24,.16),(.33,.84,.24,.16),
(.3,.8,.26,.2),(.3,.8,.24,.2),(.28,.82,.25,.18),(.27,.84,.25,.16),(.27,.82,.26,.18),(.27,.82,.26,.18),(.27,.85,.25,.15),(.27,.86,.25,.14),
(.3,.82,.26,.18),(.3,.83,.25,.17),(.39,.69,.2,.31),(.4,.69,.2,.31),(.39,.66,.2,.34),(.4,.66,.2,.34),(.4,.66,.2,.34),(.4,.66,.2,.34),(.4,.63,.2,.37)]
d={"mediaId":4247,"level":"A","keyWord":"well","defaultVoice":"male",
"taps":[{"phrase":"to jump into the water","target":"the boys","voice":"male","keys":keys(T25,boys)},
{"phrase":"to end at the well","target":"the path","voice":"male","keys":keys(T25,path)},
{"phrase":"to stand in a line","target":"the boys","voice":"male","keys":keys(T25,boys)}],
"stillS":0.5,
"nouns":[{"word":"a well","x":.3,"y":.55,"voice":"male"},{"word":"boys","x":.74,"y":.42,"voice":"male"},
{"word":"a path","x":.48,"y":.8,"voice":"male"},{"word":"the sky","x":.5,"y":.07,"voice":"male"}],
"question":"What are the boys doing?","answer":["They","are","jumping","into","the","well."],"answerVoice":"male",
"notes":"The boys act as one group (a line on the rim, jumping in one after another, floating together at the end), so 'the boys' is one target with one box around all visible boys (standing group plus the boy in the air; boys under water are not visible). The well is not a tap target because the boys stand on it and float in it (boxes would overlap); the second target is the footpath. 'to end at the well' is a state, the path does no action. From 9.0 s (top view) the boys float, they no longer stand or jump."}
json.dump(d,open("content/4247.json","w"),indent=1)
# 4248
sw=[(.46,.44,.22,.15),(.43,.43,.22,.15),(.46,.45,.22,.15),(.42,.45,.22,.15),(.43,.44,.22,.15),(.39,.43,.22,.15),(.4,.44,.22,.16),(.4,.45,.28,.15),
(.36,.42,.23,.15),(.33,.41,.22,.16),(.33,.41,.24,.17),N,N,N,(.44,.37,.22,.15),(.49,.37,.22,.15),
(.44,.38,.24,.15),(.34,.38,.28,.15),(.38,.39,.25,.15),(.36,.39,.27,.15),(.34,.39,.22,.15),(.33,.41,.22,.15),(.32,.43,.22,.15),(.3,.43,.22,.15)]
pp=[(.74,.2,.2,.14),(.74,.19,.2,.14),(.75,.18,.2,.14),(.75,.18,.2,.14),(.74,.16,.2,.14),(.73,.16,.2,.14),(.7,.16,.2,.14),(.66,.15,.2,.14),
(.59,.11,.2,.14),(.5,.08,.2,.14),(.36,.04,.2,.14),(.19,.02,.2,.14),(.01,0,.2,.14),(0,0,.18,.14),N,N,
(0,0,.2,.14),(.17,0,.2,.14),(.35,.03,.2,.14),(.51,.08,.2,.14),(.63,.12,.2,.14),(.72,.16,.2,.14),(.8,.2,.2,.14),(.8,.22,.2,.14)]
d={"mediaId":4248,"level":"A","keyWord":"indoor","defaultVoice":"male",
"taps":[{"phrase":"to swim in big waves","target":"the swimmer","voice":"male","keys":keys(T24,sw)},
{"phrase":"to stand next to the pool","target":"the people in red","voice":"male","keys":keys(T24,pp)},
{"phrase":"to wear a white cap","target":"the swimmer","voice":"male","keys":keys(T24,sw)}],
"stillS":10.0,
"nouns":[{"word":"a swimmer","x":.43,"y":.46,"voice":"male"},{"word":"lights","x":.5,"y":.08,"voice":"male"},
{"word":"people","x":.73,"y":.19,"voice":"male"},{"word":"water","x":.35,"y":.8,"voice":"male"}],
"question":"Where is the man swimming?","answer":["He","is","swimming","in","an","indoor","pool."],"answerVoice":"male",
"notes":"The packet description speaks of a person on an orange board; the frames show a swimmer with a white cap and bare shoulders (clear at 7.5-9.5 s), no board, so the texts say 'swimmer' / 'swimming'. Gender taken as male from the bare torso. The swimmer is hidden in the foam 5.5-6.5 s (off); the people in red are out of frame 7.0-7.5 s and only a sliver at 6.5 s. Both targets are small, boxes are at the minimum size. The white cap is small and only clear from 2.0 s on."}
json.dump(d,open("content/4248.json","w"),indent=1)
