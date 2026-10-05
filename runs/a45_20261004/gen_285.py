import json
T=[i*0.5 for i in range(21)]
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
gp={2.0:(0,.27,.36,.40),2.5:(0,.25,.90,.75),3.0:(0,.27,.88,.73),3.5:(.22,.24,.78,.76),4.0:(.08,.26,.90,.74),4.5:(.10,.15,.90,.83),
5.0:(0,.36,.60,.62),5.5:(.05,.28,.41,.56),6.0:(.07,.36,.32,.37),6.5:(.07,.36,.31,.37),7.0:(.07,.36,.31,.37),7.5:(.07,.36,.31,.37),
8.0:(.07,.36,.31,.37),8.5:(.07,.36,.31,.37),9.0:(.09,.37,.29,.36),9.5:(.19,.43,.21,.29),10.0:(.24,.48,.19,.23)}
dog={5.5:(.72,.70,.28,.30),6.0:(.52,.59,.36,.25),6.5:(.42,.45,.22,.16),7.0:(.42,.45,.22,.16),7.5:(.42,.45,.22,.16),8.0:(.42,.46,.22,.16),
8.5:(.42,.46,.22,.16),9.0:(.42,.47,.22,.16),9.5:(.43,.50,.18,.14),10.0:(.44,.54,.18,.14)}
c={"mediaId":285,"level":"A","keyWord":"family","defaultVoice":"male",
"taps":[
 {"phrase":"to take a family photo","target":"the man with the camera","voice":"male","keys":keys(gp)},
 {"phrase":"to wave both hands","target":"the man with the camera","voice":"male","keys":keys(gp)},
 {"phrase":"to run up the steps","target":"the dog","voice":"male","keys":keys(dog)}],
"stillS":10.0,
"nouns":[{"word":"a window","x":.50,"y":.17,"voice":"male"},{"word":"a family","x":.50,"y":.50,"voice":"male"},
 {"word":"stairs","x":.60,"y":.74,"voice":"male"},{"word":"grass","x":.22,"y":.86,"voice":"male"}],
"question":"What is the man taking?",
"answer":["He","is","taking","a","family","photo."],
"answerVoice":"male",
"notes":"Two old men in the clip: the bald one with the white moustache and braces sets up the camera (2.0-4.5) and then joins the group at the front left; the grey-haired one in the checked shirt (1.0-1.5, back row) is someone else and is never in the box. The man's box in the group shots (5.5-10.0) is tight because the family stands close. He waves both hands only at 4.5 (one hand at 5.0-5.5). The dog runs up the steps at 5.5-6.0, then sits on the grandmother's lap. The group is small at 9.5-10.0 (camera pulls back). 'a window' pill is on the upper window; there are two more windows on the porch, no other pill is on them."}
json.dump(c,open('content/285.json','w'),indent=1)
