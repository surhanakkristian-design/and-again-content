import json
girl={0.0:(0,.10,1.0,.90),0.5:(0,.10,1.0,.90),1.0:(0,.12,.60,.88),1.5:(0,.11,.76,.89),2.0:(0,.12,.78,.88),
2.5:(0,.11,.50,.89),3.0:(0,.17,.54,.83),3.5:(0,.18,.72,.82),4.0:(0,.21,.68,.79),4.5:(0,.21,.72,.79),5.0:(0,.21,.68,.79),
5.5:(0,.31,.90,.69),6.0:(0,.25,.68,.75),6.5:(.15,.20,.60,.80),7.0:(.25,.42,.70,.58),7.5:(.18,.46,.72,.54),
8.0:(.17,.48,.68,.52),8.5:(.15,.53,.72,.47),9.0:(.15,.53,.74,.47),9.5:(.03,.52,.75,.48),10.0:(0,.49,1.0,.51)}
lh={5.5:(.51,0,.31,.31),6.0:(.38,0,.30,.24),6.5:(.36,0,.34,.19),7.0:(.36,0,.33,.30),7.5:(.35,0,.30,.33),
8.0:(.34,.02,.28,.45),8.5:(.34,.03,.29,.50),9.0:(.34,.03,.29,.50),9.5:(.34,.02,.29,.50),10.0:(.36,.01,.28,.47)}
sun={6.0:(.68,.20,.20,.16),6.5:(.76,.14,.24,.20),7.0:(.70,.24,.25,.17),7.5:(.66,.28,.24,.17),
8.0:(.63,.32,.27,.16),8.5:(.64,.33,.26,.17),9.0:(.64,.33,.26,.17),9.5:(.64,.33,.27,.17),10.0:(.65,.29,.27,.17)}
times=[i*0.5 for i in range(21)]
def keys(d):
    return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in times]
c={"mediaId":4636,"level":"B","keyWord":"lighthouse","defaultVoice":"female",
"taps":[
 {"phrase":"to spread her arms wide","target":"the girl","voice":"female","keys":keys(girl)},
 {"phrase":"to rise against the sunset","target":"the lighthouse","voice":"female","keys":keys(lh)},
 {"phrase":"to set over the sea","target":"the sun","voice":"female","keys":keys(sun)}],
"stillS":9.0,
"nouns":[{"word":"a lighthouse","x":.50,"y":.22,"voice":"female"},{"word":"the sun","x":.76,"y":.42,"voice":"female"},
 {"word":"the sea","x":.14,"y":.62,"voice":"female"},{"word":"a denim jacket","x":.50,"y":.86,"voice":"female"}],
"question":"What is the girl admiring?",
"answer":["She","is","admiring","a","lighthouse","at sunset."],
"answerVoice":"female",
"notes":"'the lighthouse' = the real tower (5.5-10 s); the printed lighthouse on the poster (0-5 s, and the small poster she holds up 6.5-8 s) is not boxed - the phrase 'against the sunset' fits only the real one. Girl, tower and sun are close in the clifftop shots: boxes split between them, so the girl's box loses her raised hands (7.0-7.5) and the top of her head at 5.5; the sun is only a glare at 5.5 (off). 'at sunset.' is one chip."}
json.dump(c,open('content/4636.json','w'),indent=1)
