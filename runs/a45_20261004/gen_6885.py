import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) if r else {"t":t,"off":True} for t,r in zip(T,rows)]
woman=K([(.26,.19,.27,.68),(.29,.19,.27,.68),(.21,.19,.30,.70),(.20,.19,.34,.70),(.20,.18,.31,.78),(.20,.17,.33,.80),(.19,.17,.33,.83),(.20,.17,.33,.83)])
man=K([(.53,.37,.34,.42),(.56,.37,.32,.40),(.51,.37,.38,.42),(.54,.37,.38,.42),(.51,.38,.38,.42),(.53,.39,.40,.43),(.52,.38,.41,.47),(.53,.38,.41,.47)])
d={"mediaId":6885,"level":"A","keyWord":"bottom","defaultVoice":"female",
"taps":[{"phrase":"to touch her bottom","target":"the woman","voice":"female","keys":woman},
{"phrase":"to drop her ice cream","target":"the woman","voice":"female","keys":woman},
{"phrase":"to point at the bench","target":"the man","voice":"male","keys":man}],
"stillS":0.2,
"nouns":[{"word":"a tree","x":.72,"y":.18,"voice":"female"},{"word":"a bottom","x":.42,"y":.55,"voice":"female"},
{"word":"a bench","x":.78,"y":.68,"voice":"female"},{"word":"a sign","x":.82,"y":.87,"voice":"female"}],
"question":"What is the man doing?","answer":["He","is","pointing","at","the","bench."],"answerVoice":"male",
"notes":"Woman and man overlap (her hand on his back, his legs behind her); boxes split at x~0.52. Woman drops the ice cream at ~2.2 s. 'a bottom' pill sits on the green paint on her jeans."}
json.dump(d,open("content/6885.json","w"),indent=1)
