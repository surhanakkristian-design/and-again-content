import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) for t,r in zip(T,rows)]
dog=K([(.14,.44,.34,.27),(.22,.51,.38,.27),(.35,.56,.24,.21),(.66,.57,.20,.18),(.71,.55,.19,.18),(.74,.54,.21,.18),(.74,.54,.21,.18),(.77,.50,.19,.21)])
man=K([(.53,.35,.38,.46),(.60,.35,.34,.45),(.59,.35,.30,.45),(.50,.36,.16,.44),(.50,.36,.21,.42),(.50,.35,.24,.43),(.42,.36,.32,.42),(.50,.38,.27,.39)])
old=K([(.02,.49,.12,.14),(.02,.49,.20,.15),(.02,.49,.32,.16),(.02,.48,.35,.16),(.02,.48,.35,.16),(.02,.48,.35,.16),(.02,.48,.35,.16),(.02,.48,.35,.16)])
d={"mediaId":6913,"level":"A","keyWord":"bus station","defaultVoice":"male",
"taps":[
 {"phrase":"to jump off a bench","target":"the dog","voice":"male","keys":dog},
 {"phrase":"to put on a backpack","target":"the young man","voice":"male","keys":man},
 {"phrase":"to sleep on a seat","target":"the old man","voice":"male","keys":old}],
"stillS":2.2,
"nouns":[{"word":"a bus","x":0.80,"y":0.25,"voice":"male"},{"word":"a bench","x":0.13,"y":0.66,"voice":"male"},
 {"word":"flowers","x":0.25,"y":0.46,"voice":"male"},{"word":"a dog","x":0.82,"y":0.62,"voice":"male"}],
"question":"What is the old man doing?",
"answer":["He","is","sleeping","on","a","seat."],
"answerVoice":"male",
"notes":"Dog and young man overlap from 1.2 s (dog walks behind his legs): boxes split along a vertical line, so the man's box cuts part of his backpack at 1.7-2.7 s and the dog's box cuts its rear. Old man is partly hidden behind the dog at 0.2 s (narrow box). Key word 'bus station' = whole scene, not placed as a noun."}
json.dump(d,open('content/6913.json','w'),indent=1)
