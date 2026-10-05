import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) if r else {"t":t,"off":True} for t,r in zip(T,rows)]
woman=K([(.35,.24,.27,.42),(.47,.40,.35,.30),(.46,.37,.36,.32),(.50,.29,.38,.39),(.42,.20,.33,.46),(.30,.08,.38,.60),(0,0,.40,.64),(0,0,.18,.70)])
sit=K([(.17,.37,.18,.14),(.21,.36,.18,.14),(.19,.34,.18,.14),(.22,.33,.18,.14),(.23,.31,.18,.14),None,(.40,.31,.18,.14),(.41,.31,.18,.14)])
d={"mediaId":6886,"level":"B","keyWord":"bound","defaultVoice":"female",
"taps":[{"phrase":"to bound down the dune","target":"the woman","voice":"female","keys":woman},
{"phrase":"to kick up sand","target":"the woman","voice":"female","keys":woman},
{"phrase":"to sit on the steep slope","target":"the seated person","voice":"female","keys":sit}],
"stillS":2.7,
"nouns":[{"word":"a sand dune","x":.82,"y":.15,"voice":"female"},{"word":"a scarf","x":.40,"y":.30,"voice":"female"},
{"word":"camels","x":.84,"y":.36,"voice":"female"},{"word":"a skirt","x":.50,"y":.48,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","bounding","down","the","sand","dune."],"answerVoice":"female",
"notes":"Seated person on the slope is small (gender unclear; at 0.2 the woman box starts at x 0.35, cutting her outstretched arm, so 'the seated person'); hidden behind the woman at 2.7 (off). At 3.2 the woman box is cut at x 0.40 so it does not overlap the seated person (her right hand reaches ~0.52). At 3.7 only a sliver of her skirt at the left edge."}
json.dump(d,open("content/6886.json","w"),indent=1)
