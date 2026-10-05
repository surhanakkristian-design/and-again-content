import json
T=[i*0.5 for i in range(25)]
O=None
Ma=[(0,.02,.84,.62),(0,0,.88,.70),(0,0,.94,.72),(0,0,1.0,.72),(0,0,.97,.80),(0,0,1.0,.78),(0,0,1.0,.75),(0,0,.48,.58),
(0,0,.24,.46),(0,0,.24,.44),(0,0,.30,.43),(0,0,.27,.42),(0,0,.33,.40),(0,0,.36,.41),(0,0,.31,.43),O,O,O,O,
(.82,.14,.18,.86),(.54,.20,.46,.80),(.51,.24,.49,.76),(.44,.28,.56,.72),(.51,.30,.49,.70),(.53,.32,.47,.68)]
Ca=[O,O,O,O,O,O,O,(0,.58,.46,.37),(0,.46,.55,.30),(0,.44,.54,.28),(0,.43,.56,.28),(0,.42,.56,.27),(0,.40,.56,.28),(0,.41,.61,.28),(0,.43,.56,.28)]+[O]*10
def k(L): return [dict(t=t,off=True) if v is None else dict(t=t,x=v[0],y=v[1],w=v[2],h=v[3]) for t,v in zip(T,L)]
c={"mediaId":5154,"level":"B","keyWord":"houseplant","defaultVoice":"male",
"taps":[{"phrase":"to plant a tiny seedling","target":"the man","voice":"male","keys":k(Ma)},
 {"phrase":"to gaze at the ferns","target":"the man","voice":"male","keys":k(Ma)},
 {"phrase":"to have a long spout","target":"the watering can","voice":"male","keys":k(Ca)}],
"stillS":12.0,
"nouns":[{"word":"the ceiling","x":0.35,"y":0.07,"voice":"male"},{"word":"a fern","x":0.72,"y":0.24,"voice":"male"},
 {"word":"a man","x":0.80,"y":0.56,"voice":"male"},{"word":"houseplants","x":0.22,"y":0.66,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","watering","a","tiny","seedling."],"answerVoice":"male",
"notes":"Only one person; two phrases on the man, one state on the watering can (no action fits only the can: he pours, not the can). 0-3.5 only his hands/forearm are visible (close-up), 7.5-9.0 he is out of frame, 9.5 only a sliver at the right edge. 3.5-7.0 his hands grip the can's handle: man box = arm/hands above the handle line, can box below it (split horizontally), his free hand near the pot at 4.0 is outside both boxes. 'to gaze at the ferns': at 10-12 s he looks up at the hanging plants, several are ferns. Still 12.0: 'a fern' on the big hanging fern; a smaller fern also stands at the bottom left inside the 'houseplants' area."}
json.dump(c,open('content/5154.json','w'),indent=1)
