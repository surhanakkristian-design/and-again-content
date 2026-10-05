import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes): return [ {"t":t,"off":True} if b is None else {"t":t,"x":round(b[0],2),"y":round(b[1],2),"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)} for t,b in zip(T,boxes)]
wom=[(0.40,0.37,0.69,0.84),(0.40,0.36,0.71,0.85),(0.40,0.36,0.70,0.86),(0.40,0.36,0.72,0.86),(0.39,0.35,0.73,0.89),(0.39,0.35,0.77,0.89),(0.37,0.35,0.75,0.90),(0.36,0.35,0.79,0.91)]
man=[(0.19,0.34,0.40,0.62),(0.17,0.34,0.40,0.61),(0.15,0.33,0.40,0.62),(0.13,0.33,0.40,0.62),(0.07,0.33,0.39,0.62),(0.06,0.40,0.39,0.64),(0.06,0.41,0.37,0.65),(0.06,0.40,0.35,0.66)]
dog=[(0.12,0.62,0.40,0.80),(0.10,0.61,0.40,0.80),(0.10,0.62,0.40,0.81),(0.08,0.62,0.40,0.82),(0.07,0.62,0.39,0.84),(0.08,0.64,0.39,0.85),(0.0,0.65,0.27,0.90),(0.0,0.66,0.30,0.90)]
c={"mediaId":5567,"level":"B","keyWord":"arrogant","defaultVoice":"female",
"taps":[{"phrase":"to take a mirror selfie","target":"the woman","voice":"female","keys":K(wom)},
{"phrase":"to struggle with heavy boxes","target":"the man","voice":"male","keys":K(man)},
{"phrase":"to circle around the man","target":"the poodle","voice":"female","keys":K(dog)}],
"stillS":1.2,
"nouns":[{"word":"a chandelier","x":0.46,"y":0.25,"voice":"female"},{"word":"a poodle","x":0.25,"y":0.70,"voice":"female"},
{"word":"a fireplace","x":0.78,"y":0.64,"voice":"female"},{"word":"flowers","x":0.85,"y":0.50,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","taking","a","mirror","selfie."],"answerVoice":"female",
"notes":"Whole clip is a reflection in a mirror. Man's legs are behind the poodle: man/poodle boxes split horizontally at the dog's back. Poodle walks off left at 3.2-3.7 s."}
json.dump(c,open('content/5567.json','w'),indent=1)
