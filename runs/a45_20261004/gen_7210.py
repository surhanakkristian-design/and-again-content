import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def keys(boxes):
    return [{"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,boxes)]
woman=keys([(0.41,0.39,0.23,0.40),(0.39,0.38,0.25,0.44),(0.39,0.38,0.25,0.44),(0.38,0.37,0.26,0.48),
            (0.37,0.37,0.26,0.50),(0.38,0.37,0.27,0.51),(0.38,0.36,0.29,0.53),(0.38,0.36,0.30,0.55)])
old=keys([(0.65,0.53,0.17,0.17),(0.65,0.53,0.17,0.18),(0.65,0.53,0.15,0.18),(0.65,0.53,0.15,0.18),
          (0.64,0.53,0.16,0.18),(0.65,0.53,0.16,0.18),(0.67,0.53,0.11,0.17),(0.68,0.53,0.11,0.17)])
crouch=keys([(0.82,0.54,0.18,0.20),(0.82,0.54,0.18,0.20),(0.80,0.53,0.19,0.21),(0.80,0.53,0.20,0.21),
             (0.80,0.53,0.20,0.22),(0.81,0.54,0.19,0.21),(0.78,0.53,0.20,0.21),(0.79,0.53,0.20,0.22)])
c={"mediaId":7210,"level":"A","keyWord":"have a look around","defaultVoice":"female",
"taps":[
 {"phrase":"to walk past old furniture","target":"the woman","voice":"female","keys":woman},
 {"phrase":"to read a newspaper","target":"the old man","voice":"male","keys":old},
 {"phrase":"to reach into a box","target":"the crouching man","voice":"male","keys":crouch}],
"stillS":0.2,
"nouns":[{"word":"a window","x":0.84,"y":0.14,"voice":"female"},
 {"word":"a toy horse","x":0.24,"y":0.33,"voice":"female"},
 {"word":"a bucket","x":0.28,"y":0.83,"voice":"female"},
 {"word":"a box","x":0.86,"y":0.80,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","walking","past","old","furniture."],
"answerVoice":"female",
"notes":"The two men sit close together at the right (old man in the armchair reading, the crouching man by the crate); their boxes are split along the line between them, the old man's box is narrower than 0.18 at 3.2-3.7 s because they get closer. The crouching man reaches into the crate about 2.2-2.7 s and holds a brass candlestick from it at 3.2-3.7 s. 'a window' = the skylight in the roof; 'a toy horse' = the wooden rocking horse on the shelf (could also be 'a rocking horse' but that is above A level). Key word 'have a look around' is a phrase, not placed."}
json.dump(c,open('content/7210.json','w'),indent=1)
