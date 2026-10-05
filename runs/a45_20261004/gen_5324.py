import json
T=[i*0.5 for i in range(25)]
def K(rows):
    return [{"t":t,"off":True} if r is None else dict(zip("txywh",(t,)+tuple(r))) for t,r in zip(T,rows)]
w=[(0,0.08,0.48,0.92),(0,0.08,0.48,0.92),(0,0.09,0.46,0.91),(0,0,0.70,0.62),(0,0.25,0.86,0.40),(0,0.25,0.86,0.40),(0,0.40,0.68,0.37),(0,0.42,0.75,0.38),
(0,0.36,0.58,0.36),(0,0.32,0.90,0.38),(0,0.38,0.97,0.38),(0,0.38,1.0,0.46),(0,0.10,0.84,0.42),(0,0.27,0.55,0.40),(0,0.37,0.57,0.44),(0,0.26,0.94,0.38),
(0,0,1.0,0.90),(0,0,0.95,0.86),(0,0,0.72,1.0),(0,0,0.72,0.92),(0,0,0.95,0.86),(0,0,0.99,0.86),(0,0,0.65,0.95),(0,0,0.85,0.95),(0,0,0.80,0.95)]
c={"mediaId":5324,"level":"A","keyWord":"sponge","defaultVoice":"female",
"taps":[{"phrase":"to wash a dirty pan","target":"the woman","voice":"female","keys":K(w)},
{"phrase":"to squeeze a sponge","target":"the woman","voice":"female","keys":K(w)},
{"phrase":"to wear a colourful T-shirt","target":"the woman","voice":"female","keys":K(w)}],
"stillS":9.5,
"nouns":[{"word":"a woman","x":0.25,"y":0.22,"voice":"female"},{"word":"a pan","x":0.62,"y":0.45,"voice":"female"},
{"word":"a sponge","x":0.28,"y":0.77,"voice":"female"},{"word":"a sink","x":0.75,"y":0.92,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","washing","a","pan","with","a","sponge."],"answerVoice":"female",
"notes":"Only one person (the woman); the pan and sponge do nothing by themselves and always overlap her hand, so all three phrases use her. In the close-ups (1.5-7.5 s) only her hand/arm is visible and the box covers hand + sponge. 'to squeeze a sponge' = 11.5-12.0 s (also squeezes soap onto it at 1.5 s). T-shirt visible 0-1.0 s and 8.0-12.0 s."}
json.dump(c,open('content/5324.json','w'),indent=1)
