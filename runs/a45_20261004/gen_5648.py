from gen_5648_5649_5650_5651_lib import *
top=K([(0.11,0.08,0.84,0.60),(0.11,0.10,0.84,0.58),(0.11,0.04,0.84,0.64),(0.11,0.15,0.84,0.55),
       (0.11,0.07,0.83,0.63),(0.14,0.08,0.82,0.65),(0.22,0.16,0.70,0.61),(0.21,0.16,0.73,0.61)])
low=K([(0.27,0.69,0.28,0.30),(0.28,0.70,0.26,0.29),(0.28,0.72,0.26,0.28),(0.29,0.73,0.26,0.27),
       (0.28,0.75,0.27,0.25),(0.29,0.75,0.26,0.25),(0.28,0.78,0.23,0.22),(0.27,0.78,0.23,0.22)])
wom=K([(0.64,0.70,0.26,0.29),(0.65,0.71,0.25,0.28),(0.68,0.73,0.24,0.27),(0.67,0.73,0.25,0.27),
       (0.66,0.76,0.26,0.24),(0.67,0.76,0.27,0.24),(0.71,0.78,0.25,0.22),(0.71,0.78,0.26,0.22)])
write(5648,{"mediaId":5648,"level":"A","keyWord":"best","defaultVoice":"male",
 "taps":[{"phrase":"to climb near the ceiling","target":"the man up high","voice":"male","keys":top},
         {"phrase":"to wear a black T-shirt","target":"the man below","voice":"male","keys":low},
         {"phrase":"to wear black leggings","target":"the woman","voice":"female","keys":wom}],
 "stillS":0.2,
 "nouns":[{"word":"windows","x":0.72,"y":0.27,"voice":"male"},{"word":"boxes","x":0.12,"y":0.77,"voice":"male"},
          {"word":"a bowl","x":0.12,"y":0.86,"voice":"male"},{"word":"a woman","x":0.80,"y":0.80,"voice":"female"}],
 "question":"What is the man up high doing?",
 "answer":["He","is","climbing","near","the","ceiling."],"answerVoice":"male",
 "notes":"Key word 'best' (noun) not a visible thing, not in nouns. Other two also hold ropes and start to climb, so the top man's phrase uses 'near the ceiling'; the other two get clothing states (no unique action). Top man's feet come close to the man below's head at 3.2-3.7; boxes split at y 0.77/0.78."})
