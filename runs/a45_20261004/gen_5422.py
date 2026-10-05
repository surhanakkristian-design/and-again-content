import json
T=[i*0.5 for i in range(19)]
man={0.0:(.14,.04,.86,.96),0.5:(0,0,1,.85),1.0:(.22,0,.78,1),1.5:(.34,0,.66,1),2.0:(.63,0,.37,1),2.5:(.73,0,.27,1),
3.0:(0,.29,.62,.71),3.5:(0,.32,.55,.68),4.0:(0,.28,.45,.72),4.5:(.07,.24,.46,.76),5.0:(.17,.26,.47,.74),
5.5:(.78,.44,.18,.24),6.0:(.80,.44,.18,.24),6.5:(.77,.44,.20,.24),7.0:(.80,.44,.18,.25),7.5:(.80,.45,.18,.24),
8.0:(.80,.44,.18,.24),8.5:(.79,.45,.18,.23),9.0:(.79,.44,.18,.25)}
sbin={0.5:(0,.86,.20,.14),1.0:(0,.76,.22,.24),1.5:(0,.62,.33,.38),2.0:(.22,.34,.40,.58),2.5:(.22,.42,.50,.47)}
rbins={5.5:(.02,.49,.75,.20),6.0:(.02,.49,.77,.19),6.5:(.03,.49,.73,.19),7.0:(.03,.49,.76,.19),7.5:(.03,.49,.76,.19),
8.0:(.03,.50,.76,.20),8.5:(.03,.50,.75,.20),9.0:(.01,.50,.76,.20)}
def keys(d):
    return [{"t":t,"off":True} if d.get(t) is None else dict(zip("t x y w h".split(),(t,)+d[t])) for t in T]
M="male"
c={"mediaId":5422,"level":"B","keyWord":"recycling","defaultVoice":M,
"taps":[{"phrase":"to crumple up a wrapper","target":"the young man","voice":M,"keys":keys(man)},
{"phrase":"to stand beside a park bench","target":"the steel bin","voice":M,"keys":keys(sbin)},
{"phrase":"to form a colourful row","target":"the recycling bins","voice":M,"keys":keys(rbins)}],
"stillS":6.0,
"nouns":[{"word":"recycling bins","x":.40,"y":.58,"voice":M},{"word":"a street lamp","x":.86,"y":.13,"voice":M},
{"word":"the sky","x":.35,"y":.10,"voice":M},{"word":"a young man","x":.85,"y":.47,"voice":M}],
"question":"What is he doing in the square?",
"answer":["He","is","tossing","litter","into","the","recycling","bins."],
"answerVoice":M,
"notes":"Steel bin only in the park shot 0.5-2.5 (a sliver at 0.0 -> off); its box is split from the young man where his hand touches the lid (2.0-2.5) and where his hands are over it (1.0-1.5). The recycling bins are one group target (a row) 5.5-9.0; the man stands just right of the row, boxes split at x ~0.78. 'to stand beside a park bench' is a state (no action fits only the bin). Green dumpster at 3.5-5.0 not used."}
json.dump(c,open('content/5422.json','w'),indent=1)
