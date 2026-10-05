import json
T=[i/2 for i in range(19)]
M={0.0:(0,.37,.86,.63),0.5:(0,.34,.97,.66),1.0:(0,.36,.75,.64),1.5:(0,.25,.64,.75),2.0:(0,.22,.67,.78),2.5:(0,.25,.52,.75),
3.0:(0,.30,.47,.70),3.5:(0,.30,.42,.70),4.0:(0,.30,.42,.70),4.5:(0,.30,.42,.70),5.0:(0,.28,.52,.72),5.5:(0,.22,.60,.78),
6.0:(0,.18,.57,.82),6.5:(0,.18,.50,.82),7.0:(0,.26,.52,.74),7.5:(0,.30,.68,.70),8.0:(0,.20,.58,.80),8.5:(0,.32,.50,.68),9.0:(0,.37,.90,.63)}
O={1.5:(.64,.24,.36,.40),2.0:(.67,.37,.33,.24),8.0:(.82,.33,.18,.14),8.5:(.73,.32,.20,.14)}
def keys(d): return [({"t":t,"off":True} if t not in d else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3])) for t in T]
c={"mediaId":4424,"level":"B","keyWord":"border","defaultVoice":"male",
"taps":[{"phrase":"to step over a painted stripe","target":"the man in the beanie","voice":"male","keys":keys(M)},
{"phrase":"to grin at the camera","target":"the man in the beanie","voice":"male","keys":keys(M)},
{"phrase":"to sit inside the booth","target":"the officer","voice":"male","keys":keys(O)}],
"stillS":8.5,
"nouns":[{"word":"a passport","x":.33,"y":.655,"voice":"male"},{"word":"a booth","x":.83,"y":.37,"voice":"male"},
{"word":"a railing","x":.58,"y":.52,"voice":"male"},{"word":"a beanie","x":.18,"y":.41,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","crossing","the","border","on foot."],"answerVoice":"male",
"notes":"Only two targets: flags, cars and the boom bar overlap the selfie man in most frames. The officer is visible only at 1.5 s (in the booth window), 2.0 s (only his arm with the passport), and tiny in the booth at 8.0 / 8.5 s; whether he sits or stands is not certain. Key word 'border' is not a noun slot (the painted stripe is the border only by inference); it is used in the answer. 'on foot.' is one chip."}
json.dump(c,open('content/4424.json','w'),indent=1)
