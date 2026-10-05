import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) for t,r in zip(T,rows)]
wom=K([(.20,.30,.45,.62),(.22,.31,.44,.61),(.18,.32,.47,.61),(.13,.32,.54,.61),(.08,.31,.60,.62),(.08,.30,.62,.64),(.08,.29,.63,.69),(.08,.29,.65,.69)])
rod=K([(.55,.14,.43,.15),(.57,.15,.41,.15),(.58,.19,.41,.13),(.58,.18,.41,.13),(.60,.16,.39,.14),(.71,.13,.28,.21),(.72,.15,.27,.21),(.74,.13,.25,.24)])
d={"mediaId":6915,"level":"B","keyWord":"butt","defaultVoice":"female",
"taps":[
 {"phrase":"to grip the rod tightly","target":"the woman","voice":"female","keys":wom},
 {"phrase":"to brace herself against the side","target":"the woman","voice":"female","keys":wom},
 {"phrase":"to bend under the strain","target":"the fishing rod","voice":"female","keys":rod}],
"stillS":0.7,
"nouns":[{"word":"a fishing rod","x":0.78,"y":0.23,"voice":"female"},{"word":"a headland","x":0.88,"y":0.36,"voice":"female"},
 {"word":"waves","x":0.84,"y":0.52,"voice":"female"},{"word":"a bucket","x":0.17,"y":0.80,"voice":"female"}],
"question":"What is the woman holding?",
"answer":["She","is","gripping","a","bent","fishing","rod."],
"answerVoice":"female",
"notes":"The man with the landing net is NOT a target: from 2.2 s he stands right behind the woman and inside her box, so no non-overlapping box exists. The fishing rod's box covers only its upper bent part (above the woman's box). Key word 'butt' (rod end in the hip holder) is hidden/unclear and would read as 'bottom' on her hip, so it is not placed as a noun."}
json.dump(d,open('content/6915.json','w'),indent=1)
