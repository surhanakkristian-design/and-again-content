import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes): return [ ({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)}) for t,b in zip(T,boxes)]
P=[(0.39,0.22,0.59,0.84),(0.34,0.21,0.54,0.86),(0.32,0.21,0.57,0.86),(0.37,0.20,0.62,0.89),(0.02,0.19,0.56,0.88),(0.24,0.18,0.56,0.89),(0.30,0.18,0.60,0.90),(0.26,0.17,0.60,0.90)]
D=[(0.03,0.28,0.38,0.77),(0.05,0.28,0.33,0.77),(0.08,0.29,0.31,0.83),(0.08,0.27,0.36,0.87),None,None,(0.05,0.28,0.29,0.72),(0.02,0.27,0.25,0.77)]
W=[(0.60,0.50,0.88,0.88),(0.55,0.50,0.87,0.89),(0.58,0.51,0.87,0.90),(0.63,0.51,0.88,0.90),(0.57,0.47,0.88,0.91),(0.57,0.47,0.88,0.92),(0.61,0.50,0.90,0.92),(0.61,0.52,0.95,0.95)]
c={"mediaId":6939,"level":"A","keyWord":"change clothes","defaultVoice":"male",
"taps":[{"phrase":"to put on a jacket","target":"the man in front","voice":"male","keys":K(P)},
{"phrase":"to drop a gold jacket","target":"the man on the left","voice":"male","keys":K(D)},
{"phrase":"to kneel on the floor","target":"the woman on the floor","voice":"female","keys":K(W)}],
"stillS":3.2,
"nouns":[{"word":"a curtain","x":0.89,"y":0.28,"voice":"male"},{"word":"clothes","x":0.63,"y":0.40,"voice":"male"},{"word":"a gold jacket","x":0.20,"y":0.82,"voice":"male"},{"word":"shoes","x":0.23,"y":0.91,"voice":"male"}],
"question":"What is the man in front doing?","answer":["He","is","changing","his","clothes."],"answerVoice":"male",
"notes":"The man in front and the kneeling woman overlap (her hands on his trousers/waist): split vertically, his box keeps his body, hers starts right of his legs, so her hands and his outstretched right arm fall outside. The man on the left stands behind the man in front and is hidden at 2.2-2.7 s (off; at 2.7 s only his hand and a bit of hair show behind the shoulder). Gold jacket is dropped between 1.2 and 1.7 s."}
json.dump(c,open('content/6939.json','w'),ensure_ascii=False,indent=1)
