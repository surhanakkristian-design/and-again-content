import json
T=[i*0.5 for i in range(25)]
man={0.0:(0,.38,.83,.62),0.5:(0,.37,.66,.63),1.0:(0,.37,.86,.63),1.5:(0,.38,.64,.62),2.0:(0,.38,.84,.62),2.5:(0,.38,.66,.62),
3.0:(0,.39,.84,.61),3.5:(0,.39,1,.61),4.0:(0,.40,1,.60),4.5:(0,.42,1,.58),5.0:(0,.45,.97,.55),5.5:(0,.42,.62,.58),
6.0:(0,.43,.81,.57),6.5:(0,.42,.75,.58),7.0:(0,.41,.71,.59),7.5:(0,.40,.74,.60),8.0:(0,.41,.60,.59),8.5:(0,.39,.64,.61),
9.0:(.31,.41,.33,.53),9.5:(.31,.42,.31,.46),10.0:(.34,.42,.32,.45),10.5:(.33,.42,.32,.45),11.0:(.31,.43,.45,.48),
11.5:(.31,.45,.55,.46),12.0:(.31,.45,.52,.45)}
peng={t:(.12,.42,.18,.14) for t in (9.5,10.0,10.5,11.0,11.5)}
peng[9.0]=(.12,.43,.18,.14); peng[12.0]=(.12,.40,.18,.14)
def keys(d):
    return [{"t":t,"off":True} if d.get(t) is None else dict(zip("t x y w h".split(),(t,)+d[t])) for t in T]
M="male"
c={"mediaId":5423,"level":"B","keyWord":"worldwide","defaultVoice":M,
"taps":[{"phrase":"to reach for some vegetables","target":"the traveller","voice":M,"keys":keys(man)},
{"phrase":"to spread his arms wide","target":"the traveller","voice":M,"keys":keys(man)},
{"phrase":"to stand side by side","target":"the two penguins","voice":M,"keys":keys(peng)}],
"stillS":11.0,
"nouns":[{"word":"a sun hat","x":.50,"y":.48,"voice":M},{"word":"a rucksack","x":.40,"y":.58,"voice":M},
{"word":"snow","x":.70,"y":.85,"voice":M},{"word":"the sky","x":.50,"y":.15,"voice":M}],
"question":"What is he doing in the snow?",
"answer":["He","is","spreading","his","arms","wide."],
"answerVoice":M,
"notes":"The traveller is the only clear person target until 5.0; the market sellers wear the same conical hats, so none is used as a target. 'the two penguins' = the pair on the left (x 0.23-0.28) in the snow shot 9.0-12.0; a third penguin stands alone on the right. Their box is a minimum 0.18x0.14 box at x 0.12-0.30, so the traveller's box starts at x 0.31 and cuts his outstretched left arm at 11.0-12.0. Selfie arm at bottom-left in Paris/boat shots is included in his box."}
json.dump(c,open('content/5423.json','w'),indent=1)
