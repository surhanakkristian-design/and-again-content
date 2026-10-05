import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes): return [dict(t=t,**dict(zip('xywh',b))) if b else {"t":t,"off":True} for t,b in zip(T,boxes)]
woman=K([(.43,.20,.34,.54),(.43,.20,.38,.54),(.43,.21,.34,.57),(.35,.25,.38,.49),(.41,.27,.32,.55),(.43,.29,.29,.53),(.46,.26,.27,.56),(.38,.23,.36,.50)])
man=K([(.05,.46,.20,.28),(.05,.47,.20,.26),(.06,.50,.32,.17),(.05,.52,.29,.19),(.08,.53,.32,.18),(.08,.53,.32,.19),(.0,.53,.38,.19),(.08,.52,.27,.21)])
pup=K([(.25,.58,.18,.20),(.25,.58,.18,.20),(.24,.68,.18,.22),(.26,.75,.18,.24),(.23,.72,.18,.25),(.23,.73,.19,.26),(.27,.73,.18,.26),(.28,.74,.18,.26)])
c={"mediaId":7161,"level":"B","keyWord":"get out","defaultVoice":"female",
"taps":[{"phrase":"to lift a puppy up high","target":"the barefoot woman","voice":"female","keys":woman},
{"phrase":"to reach across the table","target":"the young man","voice":"male","keys":man},
{"phrase":"to sniff the half-eaten cake","target":"the puppy by the cake","voice":"female","keys":pup}],
"stillS":0.2,
"nouns":[{"word":"string lights","x":.20,"y":.26,"voice":"female"},{"word":"a wicker hamper","x":.73,"y":.69,"voice":"female"},{"word":"a cake","x":.48,"y":.78,"voice":"female"},{"word":"paw prints","x":.30,"y":.88,"voice":"female"}],
"question":"What is the barefoot woman doing?","answer":["She","is","lifting","a","puppy","out","of","the","hamper."],"answerVoice":"female","notes":"Three puppies: the one the woman lifts, the one by the cake at the front (target 3: nose in the cake 0.2-1.7, walks towards the camera 2.2-3.7), and one the young man grabs from 1.2. Boxes are tight splits: woman/puppy column split at 0.2-1.2 cuts the left edge of her dress; at 1.7 her box ends at y .74 (feet cut) and the man's box ends at .71 because his puppy and the front puppy are stacked there. Sniffing is only clear at 0.2-1.7."}
json.dump(c,open('content/7161.json','w'),indent=1)
