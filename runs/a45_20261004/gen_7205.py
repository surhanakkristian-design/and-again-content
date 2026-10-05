import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def keys(boxes):
    return [{"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,boxes)]
woman=keys([(0.23,0.22,0.57,0.58),(0.23,0.21,0.57,0.61),(0.23,0.21,0.58,0.63),(0.23,0.21,0.58,0.64),
            (0.23,0.20,0.62,0.72),(0.33,0.20,0.59,0.76),(0.45,0.15,0.55,0.85),(0.15,0.14,0.85,0.86)])
man=keys([(0.0,0.24,0.18,0.18)]*4+[(0.0,0.15,0.22,0.36),(0.02,0.14,0.30,0.26),(0.17,0.13,0.27,0.24),None])
c={"mediaId":7205,"level":"A","keyWord":"harm","defaultVoice":"female",
"taps":[
 {"phrase":"to hold a dirty bird","target":"the woman","voice":"female","keys":woman},
 {"phrase":"to kneel in the water","target":"the woman","voice":"female","keys":woman},
 {"phrase":"to carry a black box","target":"the man with the box","voice":"male","keys":man}],
"stillS":0.2,
"nouns":[{"word":"a ship","x":0.78,"y":0.305,"voice":"female"},
 {"word":"a mask","x":0.48,"y":0.385,"voice":"female"},
 {"word":"a bird","x":0.47,"y":0.55,"voice":"female"},
 {"word":"a crab","x":0.18,"y":0.87,"voice":"female"}],
"question":"What is the woman holding?",
"answer":["She","is","holding","a","dirty","bird."],
"answerVoice":"female",
"notes":"Key word 'harm' is a verb, not placed. The man with the box: 0.2-1.7 s a worker at the far left edge holding a black crate (likely the same man, small and partly cut off; box may also touch the man with a shovel next to him); 2.2-3.2 s the man in a cap carrying the crate. At 2.7 and 3.2 s his crate reaches the woman, so her box starts right of it (her left arm and the bird's head are left outside her box). At 3.7 s off (camera turned). 'to kneel in the water': she kneels until ~3.2 s, then starts to stand."}
json.dump(c,open('content/7205.json','w'),indent=1)
