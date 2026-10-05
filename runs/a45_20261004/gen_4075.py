import json
T=[i*0.5 for i in range(23)]
def box(t):
    if t<6: return (.35,.45,.23,.21)
    if t<8: return (.37,.45,.23,.21)
    if t<10: return (.38,.44,.24,.22)
    return (.39,.43,.25,.22)
keys=[dict(t=t,x=box(t)[0],y=box(t)[1],w=box(t)[2],h=box(t)[3]) for t in T]
d={"mediaId":4075,"level":"A","keyWord":"danger","defaultVoice":"female",
"taps":[{"phrase":"to float in the sea","target":"the woman","voice":"female","keys":keys},
{"phrase":"to hold her arms out","target":"the woman","voice":"female","keys":keys},
{"phrase":"to wear a black swimsuit","target":"the woman","voice":"female","keys":keys}],
"stillS":7.0,
"nouns":[{"word":"sharks","x":.40,"y":.30,"voice":"female"},{"word":"a woman","x":.48,"y":.54,"voice":"female"},{"word":"the sea","x":.76,"y":.88,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","floating","in","the","sea","with","sharks."],"answerVoice":"female",
"notes":"Only one possible tap target: the sharks fill the whole picture around and under the woman, so all three phrases are about the woman (same keys). Key word 'danger' is abstract and not shown as a thing, so it is not a noun and not in the answer. 'sharks' pill sits on a group above her, 'the sea' on the shark-free water bottom right; sharks are everywhere, so the sharks slot is only one of many possible places. She floats with her face up in the frames (packet says face down); no text depends on it."}
json.dump(d,open("content/4075.json","w"),indent=1)
