from gen_7297 import K, write
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2]
woman=[(0.27,0.34,0.39,0.52),(0.34,0.35,0.36,0.53),(0.19,0.35,0.48,0.58),(0.12,0.35,0.53,0.57),
       (0.23,0.35,0.47,0.57),(0.18,0.36,0.57,0.63),(0.18,0.37,0.56,0.63)]
man=[(0.79,0.28,0.19,0.19),(0.80,0.28,0.18,0.19),(0.80,0.28,0.18,0.18),(0.79,0.28,0.18,0.18),
     (0.77,0.29,0.18,0.17),(0.76,0.29,0.18,0.18),(0.75,0.29,0.18,0.18)]
write({"mediaId":7299,"level":"B","keyWord":"livestock","defaultVoice":"female",
 "taps":[{"phrase":"to swing a metal bucket","target":"the woman","voice":"female","keys":K(T,woman)},
         {"phrase":"to lead the livestock","target":"the woman","voice":"female","keys":K(T,woman)},
         {"phrase":"to wave a tea towel","target":"the man in the doorway","voice":"male","keys":K(T,man)}],
 "stillS":0.2,
 "nouns":[{"word":"a milk van","x":0.53,"y":0.30,"voice":"female"},
          {"word":"pigs","x":0.80,"y":0.55,"voice":"female"},
          {"word":"a bucket","x":0.36,"y":0.62,"voice":"female"},
          {"word":"a hen","x":0.89,"y":0.73,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","leading","the","livestock","down","the","street."],
 "answerVoice":"female",
 "notes":"Man in the dressing gown (doorway, right) waves a tea towel only at 0.2-0.7, then sips from a mug; a second man near the van also holds a mug, so 'sip from a mug' was avoided. Man target is small (min box). 'down the street' = woman walks towards the camera along the street."})
