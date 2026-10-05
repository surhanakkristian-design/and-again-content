import json
M=[(0.0,.41,.30,.59,.70),(0.5,.42,.30,.58,.70),(1.0,.58,.32,.42,.68),(1.5,.47,.33,.53,.67),(2.0,.52,.34,.48,.66),(2.5,.50,.35,.50,.65),
(3.0,.50,.36,.50,.64),(3.5,.50,.36,.50,.64),(4.0,.50,.35,.50,.65),(4.5,.49,.35,.51,.65),(5.0,.49,.34,.51,.66),(5.5,.48,.38,.52,.62),
(6.0,.48,.38,.52,.62),(6.5,.38,.40,.58,.60),(7.0,.38,.48,.62,.52),(7.5,.39,.51,.61,.49),(8.0,.36,.59,.60,.41),(8.5,.38,.65,.56,.35),
(9.0,.35,.70,.55,.30),(9.5,.48,.73,.48,.27),(10.0,.50,.76,.40,.24)]
B={0.0:(.00,.49,.37,.17),0.5:(.00,.49,.40,.17),1.0:(.00,.50,.48,.18),1.5:(.08,.50,.38,.18),2.0:(.33,.52,.18,.14)}
mk=[dict(t=t,x=x,y=y,w=w,h=h) for t,x,y,w,h in M]
bk=[dict(t=t,x=B[t][0],y=B[t][1],w=B[t][2],h=B[t][3]) if t in B else dict(t=t,off=True) for t,*_ in M]
d={"mediaId":5265,"level":"A","keyWord":"container","defaultVoice":"male",
"taps":[{"phrase":"to look through binoculars","target":"the young man","voice":"male","keys":mk},
{"phrase":"to drive a small boat","target":"the man in the boat","voice":"male","keys":bk},
{"phrase":"to look up at the ship","target":"the young man","voice":"male","keys":mk}],
"stillS":3.0,
"nouns":[{"word":"the sky","x":.40,"y":.15,"voice":"male"},{"word":"containers","x":.16,"y":.43,"voice":"male"},
{"word":"binoculars","x":.70,"y":.43,"voice":"male"},{"word":"water","x":.22,"y":.72,"voice":"male"}],
"question":"What is the young man doing?",
"answer":["He","is","looking","through","his","binoculars."],
"answerVoice":"male",
"notes":"Both men wave at 0.0-0.5, so no waving phrase. Boat man only visible 0.0-2.0 (tiny at 2.0). Answer is one of several things he does (binoculars 1.5-4.0)."}
json.dump(d,open('content/5265.json','w'),indent=1)
