import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
man=[(.01,.32,.56,.86),(.03,.37,.60,.86),(.00,.36,.58,.86),(.00,.33,.59,.86),(.00,.33,.55,.86),(.07,.30,.61,.86),(.03,.29,.62,.80),(.02,.28,.62,.80)]
wom=[(.57,.57,.82,.79),(.61,.57,.82,.79),(.58,.56,.82,.79),(.59,.58,.94,.79),(.55,.57,.90,.78),(.61,.57,.92,.78),(.62,.56,.94,.79),(.62,.55,.96,.78)]
dog=[(.82,.47,1.0,.66),(.82,.48,1.0,.66),(.82,.46,1.0,.66),(.78,.44,1.0,.58),(.76,.43,1.0,.57),(.76,.43,1.0,.57),(.76,.42,1.0,.56),(.78,.41,1.0,.55)]
def k(b): return [dict(t=t,x=round(a[0],2),y=round(a[1],2),w=round(a[2]-a[0],2),h=round(a[3]-a[1],2)) for t,a in zip(T,b)]
d={"mediaId":7827,"level":"B","keyWord":"fine","defaultVoice":"male",
"taps":[{"phrase":"to pull off his hoodie","target":"the man","voice":"male","keys":k(man)},
{"phrase":"to wave from the icy water","target":"the woman","voice":"female","keys":k(wom)},
{"phrase":"to wander across the snow","target":"the husky","voice":"male","keys":k(dog)}],
"stillS":3.7,
"nouns":[{"word":"pine trees","x":0.62,"y":0.17,"voice":"male"},{"word":"a sauna","x":0.86,"y":0.28,"voice":"male"},
{"word":"a husky","x":0.88,"y":0.52,"voice":"male"},{"word":"boots","x":0.45,"y":0.84,"voice":"male"}],
"question":"What is the woman doing?",
"answer":["She","is","waving","from","the","icy","water."],"answerVoice":"female",
"notes":"Husky and woman are close from t=1.7: husky box keeps its head/body (upper part), woman box below y~0.57. Man's raised hand clipped at x~0.6 where it would overlap the woman's box. 'boots' = the empty pair standing in the snow in front (t>=3.2). Husky 'wander' = it walks a few steps nearer the hole; weak verb, verifier may prefer another."}
json.dump(d,open('content/7827.json','w'),indent=1)
