import json
T=[i*0.5 for i in range(24)]
man=[(.58,.17,.42,.75),(.57,.2,.43,.75),(.58,.15,.42,.8),(.58,.1,.42,.75),(.59,.14,.41,.8),(.58,.16,.42,.78),(.58,.17,.42,.8),(.56,.19,.44,.78),
(.54,.18,.46,.75),(.51,.18,.49,.75),(.48,.2,.52,.78),(.49,.17,.51,.8),(.5,.2,.5,.7),(.5,.23,.5,.67),(.5,.25,.5,.73),(.56,.27,.44,.7),
(.58,.12,.42,.86),None,None,None,(.32,.28,.5,.72),(.29,.4,.53,.6),(.56,.84,.44,.16),(.5,.85,.5,.15)]
dol=[(0,.53,.54,.47),(0,.47,.56,.53),(0,.43,.57,.57),(0,.42,.57,.58),(0,.42,.58,.58),(0,.43,.57,.57),(0,.43,.57,.57),(0,.43,.55,.57),
(0,.43,.53,.57),(0,.41,.5,.59),(0,.46,.47,.54),(0,.43,.47,.57),(0,.43,.48,.57),(0,.45,.46,.55),(0,.44,.46,.56),(0,.47,.46,.53),
(0,.49,.53,.51),(.07,.43,.55,.57),(.13,.3,.74,.36),(.18,.3,.52,.44),None,None,None,None]
def keys(b):
    return [({"t":t,"off":True} if k is None else {"t":t,"x":k[0],"y":k[1],"w":k[2],"h":k[3]}) for t,k in zip(T,b)]
d={"mediaId":4232,"level":"A","keyWord":"show","defaultVoice":"male",
"taps":[{"phrase":"to hold a big ball","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to jump very high","target":"the dolphin","voice":"male","keys":keys(dol)},
{"phrase":"to hold his head","target":"the man","voice":"male","keys":keys(man)}],
"stillS":0.0,
"nouns":[{"word":"a dolphin","x":.2,"y":.75,"voice":"male"},{"word":"a ball","x":.8,"y":.5,"voice":"male"},
{"word":"trees","x":.22,"y":.34,"voice":"male"},{"word":"the sky","x":.3,"y":.12,"voice":"male"}],
"question":"What is the man holding?","answer":["He","is","holding","a","big","ball."],"answerVoice":"male",
"notes":"Key word 'show' (noun) is not a visible thing, so it is not among the nouns. The ball is not a tap target; the man's box includes the ball he holds. From 8.5 to 9.5 s the man is out of frame, from 10.0 s the dolphin is. Man's box is cut at the left where the dolphin's box is close (hair slightly clipped around 2-4.5 s)."}
json.dump(d,open("content/4232.json","w"),indent=1)
