import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,**dict(zip('xywh',r))) if r else {"t":t,"off":True} for t,r in zip(T,rows)]
dog=K([(.52,.50,.31,.23),(.52,.39,.33,.34),(.50,.20,.33,.54),(.48,.27,.35,.47),(.51,.31,.32,.45),(.52,.42,.40,.33),(.52,.51,.36,.25),(.53,.49,.36,.27)])
mix=K([(0,.25,.51,.56),(0,.27,.51,.54),(0,.26,.49,.54),(0,.25,.47,.54),(0,.23,.50,.59),(0,.22,.51,.60),(0,.20,.51,.62),(0,.18,.52,.64)])
c={"mediaId":7362,"level":"B","keyWord":"mixing bowl","defaultVoice":"female",
"taps":[{"phrase":"to catch cream in its mouth","target":"the beagle","voice":"female","keys":dog},
{"phrase":"to lick its lips","target":"the beagle","voice":"female","keys":dog},
{"phrase":"to whip chocolate batter","target":"the stand mixer","voice":"female","keys":mix}],
"stillS":0.2,
"nouns":[{"word":"a mixing bowl","x":.25,"y":.62,"voice":"female"},{"word":"a beagle","x":.66,"y":.60,"voice":"female"},
{"word":"a kitchen timer","x":.88,"y":.76,"voice":"female"},{"word":"an egg yolk","x":.45,"y":.84,"voice":"female"}],
"question":"What is the beagle doing?","answer":["It","is","catching","cream","in","its","mouth."],"answerVoice":"female",
"notes":"Two targets: the beagle and the stand mixer (whole machine incl. bowl). Boxes split around x 0.50 where the dog's paws/ear touch the bowl, so a paw or ear edge is cut at 1.2-2.2 s. The beagle catches the cream about 1.2-2.2 s and licks its lips at 3.2 s. stillS 0.2 has some splashing, but all four nouns are clear and apart."}
json.dump(c,open('content/7362.json','w'),indent=1)
