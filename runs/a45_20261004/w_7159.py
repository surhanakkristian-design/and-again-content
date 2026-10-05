import json
T=[0.2,0.7,1.2,1.7,2.2,2.7]
def K(boxes): return [dict(t=t,**dict(zip('xywh',b))) if b else {"t":t,"off":True} for t,b in zip(T,boxes)]
woman=K([(.47,.19,.46,.67),(.50,.20,.44,.64),(.53,.20,.38,.63),(.63,.20,.32,.62),(.66,.18,.29,.65),(.70,.18,.27,.64)])
dog=K([(.09,.46,.37,.41),(.09,.46,.40,.43),(.06,.46,.46,.38),(.04,.45,.58,.38),(.02,.44,.63,.41),(.02,.44,.67,.42)])
c={"mediaId":7159,"level":"A","keyWord":"get home","defaultVoice":"female",
"taps":[{"phrase":"to hold an umbrella","target":"the woman","voice":"female","keys":woman},
{"phrase":"to unlock the front door","target":"the woman","voice":"female","keys":woman},
{"phrase":"to look up at the woman","target":"the dog","voice":"female","keys":dog}],
"stillS":0.2,
"nouns":[{"word":"an umbrella","x":.25,"y":.32,"voice":"female"},{"word":"a dog","x":.22,"y":.70,"voice":"female"},
{"word":"shopping bags","x":.76,"y":.48,"voice":"female"},{"word":"a door","x":.86,"y":.12,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","unlocking","the","front","door."],"answerVoice":"female",
"notes":"Woman and dog overlap from 1.2 on (dog's head in front of her coat); split vertically, the woman's box excludes her umbrella and part of her coat at 2.2-2.7. She holds the keys at 0.2-1.7 and unlocks the door at 2.2-2.7."}
json.dump(c,open('content/7159.json','w'),indent=1)
