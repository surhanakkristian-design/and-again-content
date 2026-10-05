import json
T=[i*0.5 for i in range(19)]
young={0:(.3,.3,.7,.7),.5:(.22,.3,.78,.7),1:(.27,.32,.58,.68),1.5:(.26,.3,.52,.7),2:(0,.29,.88,.71),2.5:(.82,.44,.18,.5),
4:(.62,.52,.38,.48),4.5:(.78,.37,.22,.6),5:(.79,.33,.21,.6),5.5:(.82,.4,.18,.55),7:(.83,.43,.17,.57),8.5:(.87,.56,.13,.44),9:(.78,.44,.22,.56)}
old={2.5:(.17,.57,.28,.4),4:(.31,.68,.3,.3),4.5:(.47,.48,.3,.47),5:(.42,.45,.32,.53),5.5:(.41,.47,.34,.53),6:(.42,.68,.44,.32),6.5:(.41,.67,.48,.33)}
bike={7:(.18,.47,.64,.53),7.5:(.25,.5,.7,.5),8:(.3,.65,.7,.35),8.5:(.28,.6,.58,.4),9:(.15,.5,.62,.46)}
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
d={"mediaId":4311,"level":"A","keyWord":"young","defaultVoice":"male",
"taps":[{"phrase":"to wear a grey vest","target":"the young man","voice":"male","keys":keys(young)},
{"phrase":"to carry a brown bag","target":"the old woman","voice":"female","keys":keys(old)},
{"phrase":"to ride a bike","target":"the man on the bike","voice":"male","keys":keys(bike)}],
"stillS":9.0,
"nouns":[{"word":"a ball","x":.31,"y":.71,"voice":"male"},{"word":"a bike","x":.33,"y":.87,"voice":"male"},
{"word":"trees","x":.35,"y":.42,"voice":"male"},{"word":"the sky","x":.7,"y":.12,"voice":"male"}],
"question":"What is the young man doing?","answer":["He","is","playing","with","a","ball."],"answerVoice":"male",
"notes":"Key word 'young' is in the target name and the question. Phrase 1 is a state: every action of the young man (throwing, catching, laughing) is also done by others; 'vest' = sleeveless top (British use, as in the clip description). The woman in the dark red top also carries a WHITE bag from 4.5 s, so the old woman's phrase names the brown paper bag. The ball is not a tap target (it lies on whoever holds it). The man in the suit who jumps (2.5-3.5) is not used: two other men in suits stand at 0-2.0. Still 9.0 is the last frame: the ball is in the air next to the bike. The answer describes the first shot (0-2.0)."}
json.dump(d,open("content/4311.json","w"),indent=1)
