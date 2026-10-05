import json
T=[0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0]
def k(t,b): return {"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}
mo={1.0:(0,.28,.45,.72),1.5:(0,.28,.50,.72),2.0:(0,.29,.48,.71),2.5:(.08,.30,.26,.55),3.0:(.12,.31,.22,.38),3.5:(.20,.31,.22,.30)}
gp={2.5:(.80,.42,.20,.36),3.0:(.70,.40,.30,.60),3.5:(.70,.42,.30,.58),4.0:(.74,.43,.26,.57),4.5:(.72,.40,.28,.60),5.0:(.74,.37,.26,.63),
5.5:(.80,.36,.20,.64),6.0:(.82,.34,.18,.66),6.5:(.80,.35,.20,.65),7.0:(.78,.36,.22,.64),7.5:(.74,.38,.26,.62),8.0:(.82,.44,.18,.56)}
net={0.0:(0,.38,1.0,.21),0.5:(.12,.39,.70,.19),1.0:(.46,.36,.54,.16),1.5:(.51,.33,.34,.18),2.0:(.49,.30,.30,.16),2.5:(.35,.28,.45,.13),
3.0:(.35,.25,.65,.14),3.5:(.43,.25,.52,.16),4.0:(0,.22,.95,.16),4.5:(0,.20,.97,.14),5.0:(0,.21,1.0,.15),5.5:(0,.20,1.0,.15),
6.0:(0,.18,1.0,.15),6.5:(0,.18,1.0,.15),7.0:(0,.19,1.0,.16),7.5:(0,.18,1.0,.18),8.0:(0,.31,.95,.12),8.5:(0,.66,1.0,.16)}
K=lambda m:[k(t,m.get(t)) for t in T]
d={"mediaId":4811,"level":"B","keyWord":"teammate","defaultVoice":"male",
"taps":[{"phrase":"to wear a bright orange vest","target":"the man in orange","voice":"male","keys":K(mo)},
{"phrase":"to wear a pink sports top","target":"the girl in pink","voice":"female","keys":K(gp)},
{"phrase":"to stretch across the court","target":"the net","voice":"male","keys":K(net)}],
"stillS":6.0,
"nouns":[{"word":"a volleyball net","x":0.30,"y":0.24,"voice":"male"},
{"word":"the sea","x":0.28,"y":0.33,"voice":"male"},
{"word":"hands","x":0.55,"y":0.59,"voice":"male"},
{"word":"sand","x":0.55,"y":0.90,"voice":"male"}],
"question":"What are the players doing?",
"answer":["They","are","stacking","their","hands","in","the","middle."],
"answerVoice":"male",
"notes":"Group clip: every action (high fives, stacking hands, arms up) is shared by several players, so two phrases are states (orange vest, pink top) and one is the net. Man in orange visible 1.0-3.5 s (hidden behind others from 4.0). Girl in pink identified from 2.5 s (right edge) to 8.0 s. Girl-in-pink boxes cover her body only, not her outstretched arms (they reach over other players). Net boxes are cut to stay clear of the person boxes. 9.0 s is the sky/sun only. Answer subject 'They' (mixed group) -> defaultVoice male (evenId false)."}
json.dump(d,open("content/4811.json","w"),indent=1)
