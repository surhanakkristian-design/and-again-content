import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
man=[(.04,.12,.60,.63),(.02,.50,.62,1.0),(.00,.63,.68,.97),(.00,.58,.64,.91),(.00,.56,.60,.86),(.00,.55,.58,.84),(.00,.54,.56,.82),(.00,.53,.56,.82)]
pur=[(.60,.43,.74,.62),(.62,.41,.72,.60),(.60,.41,.70,.60),(.59,.40,.68,.58),(.57,.39,.65,.56),(.58,.39,.65,.55),(.56,.38,.64,.54),(.57,.38,.64,.53)]
blo=[(.74,.35,.93,.66),(.72,.32,.90,.65),(.70,.32,.88,.63),(.68,.31,.85,.65),(.65,.31,.81,.62),(.65,.31,.80,.62),(.64,.32,.78,.61),(.64,.31,.78,.61)]
def k(b): return [dict(t=t,x=round(a[0],2),y=round(a[1],2),w=round(a[2]-a[0],2),h=round(a[3]-a[1],2)) for t,a in zip(T,b)]
d={"mediaId":7828,"level":"A","keyWord":"finish","defaultVoice":"male",
"taps":[{"phrase":"to fall into the sand","target":"the man","voice":"male","keys":k(man)},
{"phrase":"to carry a surfboard","target":"the woman in purple","voice":"female","keys":k(pur)},
{"phrase":"to cover her mouth","target":"the blonde woman","voice":"female","keys":k(blo)}],
"stillS":3.7,
"nouns":[{"word":"the sky","x":0.40,"y":0.15,"voice":"male"},{"word":"grass","x":0.15,"y":0.52,"voice":"male"},
{"word":"a man","x":0.22,"y":0.69,"voice":"male"},{"word":"sand","x":0.55,"y":0.90,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","sitting","in","the","sand."],"answerVoice":"male",
"notes":"The woman in purple and the blonde woman are small and walk side by side in the background: their boxes are narrow and split on the line between them (purple box under the 0.18 minimum). At t=0.2 the man's raised right arm is clipped at x=0.60 so his box does not overlap theirs. The blonde woman covers her mouth from about t=1.2 (before that she just rides her skateboard). Key word 'finish' is a verb, not a noun."}
json.dump(d,open('content/7828.json','w'),indent=1)
