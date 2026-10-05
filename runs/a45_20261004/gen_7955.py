import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(l): return [ ({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2],2),"h":round(b[3],2)}) for t,b in zip(T,l)]
wom=K([(0.17,0.25,0.52,0.46),(0.22,0.32,0.50,0.38),(0.19,0.46,0.56,0.38),(0.07,0.59,0.86,0.26),(0.01,0.60,0.96,0.26),(0.10,0.58,0.90,0.27),(0.19,0.41,0.63,0.43),(0.18,0.40,0.63,0.46)])
man=K([(0.76,0.39,0.20,0.29),(0.79,0.40,0.21,0.28),(0.80,0.38,0.20,0.30),(0.80,0.32,0.20,0.27),(0.79,0.27,0.21,0.33),(0.80,0.23,0.20,0.35),(0.82,0.20,0.18,0.40),(0.81,0.17,0.19,0.43)])
c={"mediaId":7955,"level":"B","keyWord":"quick","defaultVoice":"female",
"taps":[{"phrase":"to dive for the ball","target":"the goalkeeper","voice":"female","keys":wom},
{"phrase":"to land on the turf","target":"the goalkeeper","voice":"female","keys":wom},
{"phrase":"to clutch his head","target":"the man","voice":"male","keys":man}],
"stillS":2.7,
"nouns":[{"word":"a goalpost","x":0.16,"y":0.25,"voice":"female"},{"word":"tower blocks","x":0.62,"y":0.36,"voice":"female"},{"word":"a goalkeeper","x":0.45,"y":0.70,"voice":"female"},{"word":"turf","x":0.45,"y":0.90,"voice":"female"}],
"question":"What is the goalkeeper doing?",
"answer":["She","is","diving","for","the","ball."],"answerVoice":"female",
"notes":"whether the ball is saved is unclear (it ends up beside/behind the post), so no 'save' wording. 1.7-2.7 the man stands right above her feet: boxes split horizontally (man's shoes / her foot tip slightly cut); 3.2-3.7 split vertically at x ~0.82 (her foot right of it excluded). Man clutches his head at 1.7-2.7 only."}
json.dump(c,open('content/7955.json','w'),indent=1)
