import json
T=[i*0.5 for i in range(10)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
man={0.0:(.22,.35,.58,.55),0.5:(.22,.35,.58,.55),1.0:(.22,.35,.58,.55),1.5:(.22,.35,.58,.55),2.0:(.22,.35,.58,.55),2.5:(.16,.35,.62,.55),
3.0:(0,.38,.75,.52),3.5:(0,.43,.76,.48),4.0:(0,.50,.74,.46),4.5:(0,.53,.80,.28)}
kite={0.0:(.48,.12,.20,.15),0.5:(.53,.12,.20,.15),1.0:(.58,.14,.22,.16),1.5:(.59,.14,.22,.16),2.0:(.60,.12,.22,.15),2.5:(.64,.12,.20,.16),
3.0:(.65,.15,.19,.16),3.5:(.63,.16,.20,.16),4.0:(.62,.15,.20,.16),4.5:(.63,.15,.20,.15)}
sun={t:(.22,.15,.20,.15) for t in T}
c={"mediaId":4102,"level":"A","keyWord":"sunshine","defaultVoice":"male",
"taps":[{"phrase":"to type on a laptop","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to fly on a string","target":"the kite","voice":"male","keys":keys(kite)},
{"phrase":"to shine in the sky","target":"the sun","voice":"male","keys":keys(sun)}],
"stillS":2.5,
"nouns":[{"word":"the sun","x":.32,"y":.22,"voice":"male"},{"word":"a kite","x":.74,"y":.20,"voice":"male"},
{"word":"a table","x":.72,"y":.66,"voice":"male"},{"word":"grass","x":.50,"y":.93,"voice":"male"}],
"question":"What is the weather like?",
"answer":["The","sun","is","shining","in","the","sky."],"answerVoice":"male",
"notes":"Key word 'sunshine' has no single place in the picture; 'the sun' is placed and the answer says the sun is shining. In the frames the man slides back out of his chair to the left (hands stay on the laptop), not toward the window as the description says - not used in the texts. The man's box includes the laptop and chair seat (no other target there). Illustrated clip; grass grows on the floor."}
json.dump(c,open('content/4102.json','w'),indent=1)
