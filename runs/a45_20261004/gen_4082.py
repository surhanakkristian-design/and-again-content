import json
T=[i*0.5 for i in range(31)]
def mk(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
W={0.5:(.10,.35,.48,.48),1.0:(.30,.41,.45,.59),1.5:(.30,.40,.56,.59),2.0:(.26,.36,.44,.54),2.5:(.29,.36,.71,.55),
3.0:(.24,.27,.56,.38),3.5:(.23,.28,.51,.37),4.0:(.23,.30,.51,.41),4.5:(.36,.32,.41,.43),5.0:(.42,.31,.35,.42),
5.5:(.42,.31,.35,.42),6.0:(.42,.29,.33,.45),6.5:(.42,.29,.34,.42),7.0:(.42,.30,.34,.45),7.5:(.42,.30,.34,.45),
8.0:(.43,.28,.33,.45),8.5:(.43,.28,.33,.45),9.0:(.42,.29,.33,.45),9.5:(.42,.29,.33,.45),10.0:(.40,.28,.34,.42),
10.5:(.40,.28,.34,.42),11.0:(.39,.29,.37,.43),11.5:(.39,.29,.37,.43),12.0:(.38,.27,.38,.40),12.5:(.52,.41,.43,.24),
13.0:(.61,.59,.29,.19),13.5:(.67,.70,.18,.14),14.0:(.68,.73,.18,.14),14.5:(.69,.74,.18,.14),15.0:(.71,.74,.18,.14)}
k=mk(W)
d={"mediaId":4082,"level":"B","keyWord":"upside down","defaultVoice":"female",
"taps":[{"phrase":"to hang upside down","target":"the woman","voice":"female","keys":k},
{"phrase":"to grip the wing strut","target":"the woman","voice":"female","keys":k},
{"phrase":"to drop towards the reef","target":"the woman","voice":"female","keys":k}],
"stillS":8.0,
"nouns":[{"word":"a wing","x":.60,"y":.17,"voice":"female"},{"word":"clouds","x":.24,"y":.40,"voice":"female"},
{"word":"a strut","x":.31,"y":.58,"voice":"female"},{"word":"a reef","x":.70,"y":.78,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","hanging","upside","down."],"answerVoice":"female",
"notes":"Only one possible target (the woman), used for all three phrases. Off at 0.0 s (only her hand shows at the door edge). From 13.5 s she is a tiny falling figure (minimum box); at 15.0 s only a white dot. 'a strut' pill is on the lower part of the wing strut, left of the woman; 'a wing' on the underside of the wing at the top; 'a reef' on the turquoise reef at the lower right. 'strut' is technical vocabulary (B2+)."}
json.dump(d,open("content/4082.json","w"),indent=1)
