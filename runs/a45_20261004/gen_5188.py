import json
T=[i*0.5 for i in range(21)]
M={0.0:(.30,.27,.70,.73),0.5:(.28,.27,.72,.73),1.0:(.32,.29,.68,.71),1.5:(.28,.29,.72,.71),2.0:(.30,.28,.70,.72),2.5:(.28,.26,.72,.74),
3.0:(.33,.28,.67,.72),3.5:(.48,.28,.52,.72),4.0:(.50,.24,.50,.76),4.5:(.50,.24,.50,.76),5.0:(.60,.22,.40,.78),5.5:(.58,.17,.42,.75),
6.0:(.58,.20,.38,.54),6.5:(.62,.18,.38,.62),7.0:(.60,.18,.40,.62),7.5:(.56,.18,.44,.62),8.0:(.58,.19,.40,.62),8.5:(.58,.19,.40,.62),
9.0:(.58,.20,.36,.64),9.5:(.64,.18,.32,.70),10.0:(.64,.17,.33,.70)}
F={3.5:(0,.35,.48,.52),4.0:(0,.31,.50,.53),4.5:(.08,.31,.42,.46),5.0:(.16,.27,.43,.48),5.5:(.08,.25,.44,.38),6.0:(.11,.25,.37,.37),
6.5:(.06,.25,.44,.41),7.0:(.03,.24,.45,.43),7.5:(.06,.24,.43,.42),8.0:(.07,.24,.38,.42),8.5:(.08,.24,.40,.40),9.0:(.12,.24,.26,.48),
9.5:(.13,.24,.31,.50),10.0:(.12,.24,.28,.52)}
B={5.5:(.10,.64,.35,.30),6.0:(.38,.62,.20,.16),6.5:(.40,.72,.22,.18),7.0:(.36,.71,.24,.16),7.5:(.36,.66,.19,.18),8.0:(.32,.66,.25,.18),
8.5:(.33,.64,.25,.20),9.0:(.38,.50,.20,.22),9.5:(.44,.36,.20,.24),10.0:(.40,.29,.24,.31)}
def keys(d):
    return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else {"t":t,"off":True} for t in T]
c={"mediaId":5188,"level":"B","keyWord":"disappointment","defaultVoice":"male",
"taps":[{"phrase":"to struggle with a fishing rod","target":"the man in the hat","voice":"male","keys":keys(M)},
{"phrase":"to carry a landing net","target":"the man in the fleece","voice":"male","keys":keys(F)},
{"phrase":"to land on the jetty","target":"the boot","voice":"male","keys":keys(B)}],
"stillS":8.0,
"nouns":[{"word":"the sky","x":0.55,"y":0.08,"voice":"male"},{"word":"a landing net","x":0.20,"y":0.59,"voice":"male"},
{"word":"a rubber boot","x":0.45,"y":0.75,"voice":"male"},{"word":"a jetty","x":0.55,"y":0.91,"voice":"male"}],
"question":"What has the bearded man caught?","answer":["He","has","caught","a","green","rubber","boot."],"answerVoice":"male",
"notes":"Key word 'disappointment' is abstract, so it is not a noun and not in the answer. The man in the fleece is hidden behind the man in the hat 0.0-3.0 (marked off; at 2.0-3.0 only his net/arm shows). Boot flies in at 5.5 (blurred), lands 6.0, is lifted 9.0-10.0; boxes split from the man's box where he holds it. 'to land on the jetty': the boot lands at 5.5-6.5."}
json.dump(c,open('content/5188.json','w'),indent=1)
