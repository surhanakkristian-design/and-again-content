from gen_7162_7163_7164_7166_lib import write
W=[(0.04,0.31,0.38,0.61),(0.05,0.29,0.41,0.65),(0.17,0.27,0.33,0.70),(0.16,0.41,0.33,0.58),(0.16,0.46,0.36,0.54),(0.20,0.54,0.52,0.46),(0.19,0.50,0.56,0.50),(0.18,0.48,0.63,0.52)]
M=[(0.42,0.35,0.20,0.27),(0.46,0.34,0.18,0.27),(0.50,0.38,0.18,0.28),(0.50,0.37,0.21,0.30),(0.52,0.36,0.17,0.29),(0.55,0.33,0.21,0.21),(0.58,0.27,0.20,0.23),(0.60,0.19,0.22,0.29)]
S=[(0.50,0.62,0.45,0.20),(0.59,0.61,0.41,0.21),(0.71,0.62,0.29,0.22),(0.82,0.62,0.18,0.22),None,None,None,None]
write(7162, {"mediaId":7162,"level":"B","keyWord":"get over","defaultVoice":"female",
 "taps":[{"phrase":"to hug a bundle of wool","target":"the woman","voice":"female","keys":W},
         {"phrase":"to brandish a broom","target":"the man with the broom","voice":"male","keys":M},
         {"phrase":"to trot towards the pens","target":"the sheep","voice":"female","keys":S}],
 "stillS":0.2,
 "nouns":[{"word":"wool","x":0.50,"y":0.14,"voice":"female"},{"word":"a broom","x":0.56,"y":0.39,"voice":"female"},
          {"word":"a sheep","x":0.72,"y":0.70,"voice":"female"},{"word":"floorboards","x":0.62,"y":0.90,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","hugging","a","bundle","of","wool."],"answerVoice":"female",
 "notes":"Key word 'get over' is a phrasal verb, not placed. Woman hugs wool from 1.7 s (throws it up before). Woman/man boxes split where her raised arm or knees approach the man; from 2.7 s the man's box is cut above his feet so the kneeling woman's head stays in hers. Sheep leaves frame after 1.7 s. Seated men are not targets."})
