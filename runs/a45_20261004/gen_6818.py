from lib_6816_6817_6818_6819 import *
man=[(.37,.28,.69,.74),(.21,.29,.71,.76),(.21,.29,.65,.80),(.14,.29,.64,.81),(.28,.29,.66,.81),(.25,.29,.62,.83),(.27,.29,.69,.84),(.20,.31,.89,.84)]
wom=[(.86,.31,1.0,.52),(.80,.30,1.0,.48),(.79,.29,.99,.44),(.78,.27,.95,.42),(.73,.25,.91,.40),(.69,.25,.87,.39),(.70,.24,.88,.38),(.70,.17,.88,.31)]
M=keys(man);W=keys(wom)
write(6818,{"mediaId":6818,"level":"B","keyWord":"administrator","defaultVoice":"male",
"taps":[{"phrase":"to skate across the office","target":"the administrator","voice":"male","keys":M},
{"phrase":"to carry heavy ring binders","target":"the administrator","voice":"male","keys":M},
{"phrase":"to wear a green jumper","target":"the woman in green","voice":"female","keys":W}],
"stillS":2.2,
"nouns":[{"word":"an administrator","x":.47,"y":.36,"voice":"male"},
{"word":"ring binders","x":.51,"y":.46,"voice":"male"},
{"word":"an old computer","x":.87,"y":.56,"voice":"male"},
{"word":"roller skates","x":.46,"y":.78,"voice":"male"}],
"question":"What is the administrator doing?",
"answer":["He","is","skating","across","the","office."],
"answerVoice":"male",
"notes":"Colleagues all wave folders, so the third target is the red-haired woman in the green jumper (state phrase; no action is unique to her). She is small and moves left as the camera pans; check her box. Two phrases share the administrator."})
