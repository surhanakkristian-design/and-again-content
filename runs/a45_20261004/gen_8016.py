import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2]
def K(boxes):
    return [{"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,boxes)]
woman=[(0.43,0.26,0.36,0.74),(0.32,0.27,0.45,0.73),(0.29,0.26,0.52,0.74),(0.13,0.22,0.77,0.78),(0.16,0.22,0.78,0.78),(0.12,0.21,0.78,0.79),(0.13,0.22,0.75,0.78)]
jumper=[(0.0,0.42,0.42,0.58),(0.0,0.33,0.31,0.67),(0.0,0.52,0.28,0.48),None,None,None,None]
lantern=[(0.23,0.04,0.18,0.18),(0.25,0.04,0.18,0.18),(0.24,0.05,0.18,0.18),(0.25,0.04,0.18,0.17),(0.27,0.04,0.18,0.17),(0.30,0.04,0.18,0.17),(0.31,0.06,0.18,0.16)]
c={"mediaId":8016,"level":"B","keyWord":"take in","defaultVoice":"female",
"taps":[
 {"phrase":"to cradle a ginger kitten","target":"the woman in the raincoat","voice":"female","keys":K(woman)},
 {"phrase":"to hold out a towel","target":"the person in the white jumper","voice":"female","keys":K(jumper)},
 {"phrase":"to glow above the doorway","target":"the lantern","voice":"female","keys":K(lantern)}],
"stillS":2.7,
"nouns":[{"word":"a lantern","x":0.39,"y":0.16,"voice":"female"},
 {"word":"a kitten","x":0.60,"y":0.48,"voice":"female"},
 {"word":"a bath towel","x":0.27,"y":0.62,"voice":"female"},
 {"word":"leggings","x":0.62,"y":0.86,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","cradling","a","ginger","kitten."],
"answerVoice":"female",
"notes":"The person in the white jumper is only seen as arms/back from the left edge at 0.2-1.2 (gender unclear, so 'person'); off from 1.7. At 0.2-1.2 the towel and arms are in front of the woman, boxes split at the left edge of the woman. The kitten sits inside the woman's box but is not a target. 'to hold out a towel': the person holds the towel out and throws it over her."}
json.dump(c,open('content/8016.json','w'),indent=1)
