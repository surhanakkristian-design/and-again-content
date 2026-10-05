from gen_7891_7892_7893_7894_lib import *
man=keys([(.22,.42,.38,.68),(.20,.39,.38,.70),(.18,.41,.385,.74),(.15,.45,.385,.77),(.05,.47,.36,.82),(0,.50,.31,.90),(0,.58,.33,1),(0,.53,.31,.97)])
wom=keys([(.38,.34,.68,.73),(.385,.28,.71,.75),(.39,.29,.80,.83),(.39,.23,.84,.87),(.38,.19,.84,.91),(.33,.15,1,1),(.34,.20,1,1),(.31,.20,.86,1)])
write({"mediaId":7892,"level":"B","keyWord":"live on","defaultVoice":"female",
"taps":[{"phrase":"to lead the way","target":"the woman","voice":"female","keys":wom},
{"phrase":"to wear frosted goggles","target":"the woman","voice":"female","keys":wom},
{"phrase":"to trail behind the woman","target":"the man","voice":"male","keys":man}],
"stillS":2.2,
"nouns":[{"word":"goggles","x":0.76,"y":0.27,"voice":"female"},{"word":"clouds","x":0.20,"y":0.43,"voice":"female"},
{"word":"a beanie","x":0.17,"y":0.52,"voice":"female"},{"word":"snow","x":0.45,"y":0.93,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","climbing","up","a","snowy","ridge."],"answerVoice":"female",
"notes":"Two climbers only; woman used for two phrases (lead the way / frosted goggles), man for 'trail behind'. Man and woman boxes split at x~0.38 at 0.2-1.7 where he stands just behind her shoulder. Woman's rope hand/rope partly outside her box. 'goggles' as bare plural (a pair)."})
