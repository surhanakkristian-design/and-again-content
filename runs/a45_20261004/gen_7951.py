import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes):
    return [{"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,boxes)]
Wo=K([(0.02,0.42,0.24,0.40),(0.02,0.41,0.23,0.42),(0.01,0.42,0.24,0.40),(0.01,0.42,0.24,0.41),
      (0.01,0.41,0.24,0.42),(0.01,0.41,0.24,0.42),(0.01,0.41,0.24,0.42),(0.01,0.41,0.24,0.42)])
Mw=K([(0.26,0.32,0.36,0.63),(0.25,0.31,0.35,0.65),(0.25,0.33,0.35,0.63),(0.25,0.31,0.35,0.65),
      (0.25,0.32,0.35,0.64),(0.25,0.31,0.35,0.65),(0.25,0.31,0.35,0.65),(0.25,0.30,0.35,0.66)])
G=K([(0.62,0.48,0.19,0.22),(0.60,0.47,0.20,0.23),(0.60,0.47,0.20,0.24),(0.60,0.46,0.20,0.25),
     (0.60,0.46,0.20,0.25),(0.60,0.46,0.20,0.25),(0.60,0.46,0.20,0.26),(0.60,0.46,0.20,0.27)])
c={"mediaId":7951,"level":"B","keyWord":"proudly","defaultVoice":"male",
 "taps":[{"phrase":"to applaud with a smile","target":"the woman","voice":"female","keys":Wo},
  {"phrase":"to flex his biceps","target":"the man in white","voice":"male","keys":Mw},
  {"phrase":"to do lunges with dumbbells","target":"the man in green","voice":"male","keys":G}],
 "stillS":0.2,
 "nouns":[{"word":"a ceiling lamp","x":0.17,"y":0.23,"voice":"male"},
  {"word":"a mirror","x":0.75,"y":0.12,"voice":"male"},
  {"word":"a vest","x":0.40,"y":0.52,"voice":"male"},
  {"word":"a barbell","x":0.75,"y":0.87,"voice":"male"}],
 "question":"What is the man in white doing?",
 "answer":["He","is","flexing","his","biceps."],
 "answerVoice":"male",
 "notes":"the man in white's reflection also flexes (box covers only the real man; his flexed right fist past x 0.60 is cut to keep clear of the man in green, who is seen in the mirror doing dumbbell lunges); 'proudly' kept out of the answer because it could stand before or after the verb; man in white's left arm and the woman's clapping hands are close, split at x 0.25."}
json.dump(c,open("content/7951.json","w"),indent=1)
