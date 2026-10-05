import json
T=[i*0.5 for i in range(21)]
def ks(d):
    return [{"t":t,"off":True} if d.get(t) is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) for t in T]
man={0.0:(.36,.43,.26,.30),0.5:(.38,.41,.26,.33),1.0:(.39,.42,.28,.33),1.5:(.41,.42,.28,.36),2.0:(.41,.44,.26,.33),
2.5:(.39,.44,.28,.33),3.0:(.39,.44,.27,.36),3.5:(.31,.41,.31,.47),4.0:(.29,.39,.37,.54),4.5:(.25,.37,.40,.62),
5.0:(.20,.39,.53,.61),5.5:(.38,.42,.42,.52),6.0:(.42,.41,.32,.34),6.5:(.44,.43,.36,.38),7.0:(.39,.40,.30,.46),
7.5:(.29,.41,.39,.42),8.0:(.29,.39,.37,.52),8.5:(.30,.34,.42,.66),9.0:(.27,.32,.43,.68),9.5:(.27,.34,.40,.66),10.0:(.35,.35,.27,.65)}
clock={3.0:(.82,.04,.18,.20),3.5:(.70,.25,.20,.15),4.0:(.70,.31,.18,.14),4.5:(.74,.34,.18,.14),5.0:(.78,.35,.18,.14)}
c={"mediaId":5226,"level":"B","keyWord":"carriage","defaultVoice":"male",
"taps":[{"phrase":"to dash along the platform","target":"the man","voice":"male","keys":ks(man)},
{"phrase":"to clutch a duffel bag","target":"the man","voice":"male","keys":ks(man)},
{"phrase":"to hang above the platform","target":"the clock","voice":"male","keys":ks(clock)}],
"stillS":4.0,
"nouns":[{"word":"a glass roof","x":.50,"y":.12,"voice":"male"},{"word":"a clock","x":.79,"y":.38,"voice":"male"},
{"word":"a carriage","x":.16,"y":.45,"voice":"male"},{"word":"a duffel bag","x":.45,"y":.56,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","dashing","along","the","platform."],"answerVoice":"male",
"notes":"Clock only visible 3.0-5.0 s (small, top right). Man runs toward camera 0-5 s, away 5.5-6.5 s, boards 7-7.5 s, stands in the doorway 8-10 s; the answer describes the running part. Other travellers pull suitcases, so no suitcase phrase."}
json.dump(c,open('content/5226.json','w'),indent=1)
