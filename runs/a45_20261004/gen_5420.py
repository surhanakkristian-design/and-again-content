import json
T=[i*0.5 for i in range(21)]
man={0.0:(.41,.38,.19,.44),0.5:(.34,.34,.37,.60),1.0:(.30,.32,.41,.68),1.5:(.08,.24,.75,.76),2.0:(.10,.30,.58,.70),
2.5:(.20,.26,.47,.65),3.0:(.26,.37,.36,.47),3.5:(.34,.36,.34,.45),4.0:(.32,.39,.32,.40),4.5:(.27,.37,.30,.48),
5.0:(.43,.31,.32,.54),5.5:(.40,.34,.33,.45),6.0:(.33,.42,.36,.48),6.5:(.35,.39,.30,.36),7.0:(.34,.38,.30,.37),
7.5:(.32,.39,.30,.38),8.0:(.32,.40,.28,.35),8.5:(.30,.40,.32,.34),9.0:(.29,.40,.34,.36),9.5:(.31,.38,.34,.42),10.0:(.35,.37,.34,.45)}
boat={6.0:(.43,.28,.34,.14),6.5:(.37,.25,.37,.14),7.0:(.33,.24,.41,.14),7.5:(.30,.25,.48,.14),8.0:(.24,.23,.56,.17),
8.5:(.02,.17,.96,.22),9.0:(0,.12,1,.27),9.5:(0,.12,1,.25),10.0:(0,.12,1,.24)}
def keys(d):
    return [{"t":t,"off":True} if d.get(t) is None else dict(zip("t x y w h".split(),(t,)+d[t])) for t in T]
c={"mediaId":5420,"level":"B","keyWord":"vessel","defaultVoice":"male",
"taps":[{"phrase":"to climb aboard a tram","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to dash along the quay","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to float beside the quay","target":"the boat","voice":"male","keys":keys(boat)}],
"stillS":8.0,
"nouns":[{"word":"a vessel","x":.53,"y":.33,"voice":"male"},{"word":"a backpack","x":.45,"y":.53,"voice":"male"},
{"word":"a gangway","x":.46,"y":.71,"voice":"male"},{"word":"the sea","x":.85,"y":.45,"voice":"male"},
{"word":"the sky","x":.30,"y":.10,"voice":"male"}][:4],
"question":"What is he doing at the harbour?",
"answer":["He","is","boarding","a","passenger","vessel."],
"answerVoice":"male",
"notes":"Only one clear person target (other passengers are background), so two phrases on the man + the boat. The man stands in front of the boat from 6.0 on; the boat box is cut to the part above his head (mast/wheelhouse) to avoid overlap, so it is thin at 6.0-7.5 (h 0.14-0.16). Seagulls skipped (many, moving). Other boats far in the background at 8.0+ are tiny."}
json.dump(c,open('content/5420.json','w'),indent=1)
