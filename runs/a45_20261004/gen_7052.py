import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(lst):
    return [{"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,lst)]
wom=K([(0.0,0.27,0.82,0.70),(0.0,0.27,0.87,0.70),(0.0,0.26,0.92,0.74),(0.0,0.25,1.0,0.75),
       (0.0,0.23,1.0,0.77),(0.0,0.23,1.0,0.77),(0.0,0.21,1.0,0.79),(0.0,0.21,1.0,0.79)])
cat=K([(0.38,0.13,0.20,0.14),(0.38,0.12,0.20,0.15),(0.38,0.12,0.20,0.14),(0.38,0.11,0.20,0.14),
       (0.38,0.09,0.20,0.14),(0.39,0.09,0.21,0.14),(0.40,0.07,0.20,0.14),(0.40,0.07,0.20,0.14)])
c={"mediaId":7052,"level":"A","keyWord":"do the cooking","defaultVoice":"female",
 "taps":[{"phrase":"to taste the food","target":"the young woman","voice":"female","keys":wom},
         {"phrase":"to cook on the stove","target":"the young woman","voice":"female","keys":wom},
         {"phrase":"to sit on the fridge","target":"the cat","voice":"female","keys":cat}],
 "stillS":2.2,
 "nouns":[{"word":"a cat","x":0.48,"y":0.18,"voice":"female"},{"word":"a fridge","x":0.70,"y":0.27,"voice":"female"},
          {"word":"carrots","x":0.58,"y":0.63,"voice":"female"}],
 "question":"What is the young woman doing?",
 "answer":["She","is","doing","the","cooking."],"answerVoice":"female",
 "notes":"Family at the door not used as a target: the young woman's outstretched arm crosses them, so boxes could not be split cleanly. Her box spans the full width from 1.7 s (arm + spoon)."}
json.dump(c,open('content/7052.json','w'),indent=1)
