import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes): return [dict(t=t,**dict(zip('xywh',b))) if b else {"t":t,"off":True} for t,b in zip(T,boxes)]
woman=K([(.31,.28,.31,.61),(.29,.28,.35,.62),(.25,.28,.32,.63),(.25,.28,.32,.62),(.25,.26,.31,.65),(.25,.26,.32,.66),(.25,.26,.34,.66),(.25,.26,.35,.66)])
man=K([(.64,.43,.29,.30),(.64,.43,.31,.30),(.68,.43,.27,.31),(.65,.43,.30,.31),(.74,.43,.22,.31),(.75,.43,.22,.31),(.72,.43,.25,.31),(.64,.43,.33,.31)])
cat=K([(.0,.71,.29,.22),(.0,.72,.28,.21),(.0,.73,.24,.22),(.0,.74,.24,.21),(.0,.72,.24,.22),(.0,.73,.24,.22),(.0,.75,.24,.21),(.0,.75,.24,.21)])
c={"mediaId":7160,"level":"A","keyWord":"get lost on the way","defaultVoice":"female",
"taps":[{"phrase":"to look at a map","target":"the woman in the hat","voice":"female","keys":woman},
{"phrase":"to point down the street","target":"the old man","voice":"male","keys":man},
{"phrase":"to sit on the ground","target":"the cat","voice":"female","keys":cat}],
"stillS":0.2,
"nouns":[{"word":"a hat","x":.45,"y":.32,"voice":"female"},{"word":"a door","x":.10,"y":.56,"voice":"female"},
{"word":"a suitcase","x":.47,"y":.73,"voice":"female"},{"word":"a cat","x":.14,"y":.84,"voice":"female"}],
"question":"What is the tourist doing?","answer":["She","is","looking","at","a","map."],"answerVoice":"female",
"notes":"Static camera. She holds the folded map from the start and opens/reads it at 2.7-3.7 (before that she looks around). The man points at 0.2-1.7 and 3.7, waves at 2.2-3.2. Cat box and woman box split around x .24-.25 (her suitcase handle/arm near the cat). Woman on the balcony is not a target; 'the tourist' in the question to avoid an 8-word question."}
json.dump(c,open('content/7160.json','w'),indent=1)
