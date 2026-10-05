import json
T=[i*0.5 for i in range(21)]
duck=[(0.31,0.42,0.46,0.24),(0.26,0.41,0.50,0.25),(0.26,0.42,0.50,0.25),(0.26,0.42,0.50,0.26),(0.26,0.18,0.52,0.46),(0.26,0.18,0.54,0.46),(0.26,0.20,0.52,0.44),(0.26,0.38,0.51,0.28),(0.26,0.33,0.52,0.35),(0,0.27,1,0.41),(0.02,0.22,0.98,0.48),(0,0.10,0.82,0.62),(0,0.14,0.81,0.62),(0.09,0.30,0.71,0.42),(0.14,0.25,0.67,0.46),(0.15,0.20,0.69,0.50),(0.14,0.21,0.68,0.50),(0.12,0.25,0.72,0.49),(0.11,0.24,0.73,0.50),(0.10,0.24,0.76,0.52),(0.09,0.22,0.79,0.56)]
def keys(b): return [{"t":t,"off":True} if k is None else {"t":t,"x":k[0],"y":k[1],"w":k[2],"h":k[3]} for t,k in zip(T,b)]
c={"mediaId":250,"level":"A","keyWord":"duck","defaultVoice":"female",
"taps":[{"phrase":p,"target":"the duck","voice":"female","keys":keys(duck)} for p in ["to put its head underwater","to open its wings","to open its beak"]],
"stillS":7.5,
"nouns":[{"word":"a duck","x":0.50,"y":0.60,"voice":"female"},{"word":"trees","x":0.50,"y":0.08,"voice":"female"},{"word":"water","x":0.78,"y":0.86,"voice":"female"}],
"question":"What is the duck doing?","answer":["The","duck","is","swimming","on","the","water."],"answerVoice":"female",
"notes":"Only one real target (the duck); a tiny dark bird far in the background in the first seconds also swims, so no 'to swim' tap phrase. 'to open its beak' happens only at 9.5-10 s. Only 3 nouns: the lily leaves are scattered, no single clear place."}
json.dump(c,open('content/250.json','w'),indent=1)
