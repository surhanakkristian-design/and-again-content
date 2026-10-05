import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def k(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]}) for t,r in zip(T,rows)]
woman=k([(.27,.22,.43,.56),(.42,.15,.40,.63),(.51,.20,.38,.66),(.60,.23,.32,.61),(.63,.24,.31,.58),(.64,.26,.31,.56),(.64,.27,.31,.57),(.63,.28,.31,.52)])
grey=k([None,None,(0,.16,.23,.70),(.01,.22,.33,.60),(.05,.24,.33,.58),(.05,.27,.32,.53),(.08,.28,.31,.62),(.10,.29,.29,.52)])
yellow=k([(0,.04,.20,.70),(.02,.14,.40,.65),(.23,.23,.28,.57),(.34,.28,.26,.50),(.38,.31,.25,.45),(.38,.31,.25,.43),(.39,.31,.24,.46),(.39,.32,.23,.44)])
d={"mediaId":6931,"level":"B","keyWord":"catch up","defaultVoice":"female",
 "taps":[
  {"phrase":"to glance at her companions","target":"the woman","voice":"female","keys":woman},
  {"phrase":"to wear a grey cycling jersey","target":"the man in grey","voice":"male","keys":grey},
  {"phrase":"to cycle in the middle","target":"the man in yellow","voice":"male","keys":yellow}],
 "stillS":2.2,
 "nouns":[{"word":"mountains","x":0.45,"y":0.31,"voice":"female"},{"word":"a braid","x":0.80,"y":0.40,"voice":"female"},{"word":"the road","x":0.50,"y":0.88,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","glancing","at","her","companions."],
 "answerVoice":"female",
 "notes":"Man in grey enters only at 1.2 s; man in yellow is at the left edge at 0.2 s and only in the middle from 1.2 s on. Grey-jersey phrase is a state because all three just ride. The key word 'catch up' is not visible as an action (they ride level), so it is not used."}
json.dump(d,open("content/6931.json","w"),indent=1)
