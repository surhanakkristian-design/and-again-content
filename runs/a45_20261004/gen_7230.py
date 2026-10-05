import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,**dict(zip("xywh",r))) if r else {"t":t,"off":True} for t,r in zip(T,rows)]
man=K([(.28,.21,.25,.42),(.28,.21,.25,.42),(.26,.21,.27,.42),(.26,.21,.27,.42),(.22,.19,.31,.42),(.20,.19,.33,.42),(.18,.18,.35,.44),(.17,.18,.36,.44)])
wom=K([(.53,.21,.46,.78)]*4+[(.53,.19,.46,.80)]*4)
d={"mediaId":7230,"level":"B","keyWord":"horror","defaultVoice":"female",
"taps":[{"phrase":"to hold up a china poodle","target":"the woman with braids","voice":"female","keys":wom},
{"phrase":"to grimace in disgust","target":"the woman with braids","voice":"female","keys":wom},
{"phrase":"to grin behind the stall","target":"the man in the flat cap","voice":"male","keys":man}],
"stillS":1.7,
"nouns":[{"word":"a flat cap","x":.44,"y":.26,"voice":"female"},{"word":"a lampshade","x":.14,"y":.36,"voice":"female"},
{"word":"a china poodle","x":.62,"y":.62,"voice":"female"},{"word":"teacups","x":.32,"y":.72,"voice":"female"}],
"question":"What is the woman with braids doing?",
"answer":["She","is","grimacing","at","a","china","poodle."],"answerVoice":"female",
"notes":"Lamp held by an outstretched arm whose owner is ambiguous (braided woman vs red-haired woman at left edge), so no lamp phrase. Red-haired woman mostly off-frame, not used. Woman box covers body only; her outstretched arm crosses in front of the man."}
json.dump(d,open("content/7230.json","w"),indent=1)
