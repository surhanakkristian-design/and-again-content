from lib_6816_6817_6818_6819 import *
act=[(.17,.50,.70,.88),(.17,.49,.74,.89),(.15,.47,.76,.99),(.19,.45,.98,1.0),(.29,.41,1.0,1.0),(.28,.38,1.0,1.0),(.24,.35,1.0,1.0),(.24,.31,1.0,1.0)]
off=[(.03,.38,.30,.50),(.03,.38,.28,.49),(.02,.36,.30,.47),(.02,.33,.31,.45),(.01,.32,.29,.60),(.0,.29,.28,.56),(.0,.28,.24,.56),(.0,.27,.24,.56)]
flg=[(.43,.13,.69,.31),(.45,.11,.72,.29),(.48,.08,.79,.27),(.46,.05,.77,.25),(.50,.01,.84,.22),(.56,.0,.90,.19),(.59,.0,.97,.16),(.60,.0,.98,.15)]
A=keys(act);O=keys(off);F=keys(flg)
write(6817,{"mediaId":6817,"level":"B","keyWord":"activist","defaultVoice":"female",
"taps":[{"phrase":"to shout into a megaphone","target":"the activist","voice":"female","keys":A},
{"phrase":"to crouch on the road","target":"the police officer","voice":"male","keys":O},
{"phrase":"to show a burning globe","target":"the flag","voice":"female","keys":F}],
"stillS":0.2,
"nouns":[{"word":"a police officer","x":.18,"y":.50,"voice":"female"},
{"word":"an activist","x":.38,"y":.72,"voice":"female"},
{"word":"a flag","x":.56,"y":.22,"voice":"female"},
{"word":"a lorry","x":.86,"y":.32,"voice":"female"}],
"question":"What is the activist doing?",
"answer":["She","is","shouting","into","a","megaphone."],
"answerVoice":"female",
"notes":"Officer kneels right behind the activist: boxes split on a vertical line at her head, so her megaphone/left knee fall outside her box in the early frames and the officer box keeps only his upper body. 'police officer' and 'activist' nouns use defaultVoice (not gendered nouns)."})
