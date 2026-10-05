from gen_7297 import K, write, T
woman=[(0.12,0.32,0.54,0.68),(0.09,0.31,0.58,0.69),(0.06,0.30,0.60,0.70),(0.08,0.30,0.59,0.70),
       (0.02,0.29,0.64,0.71),(0.02,0.28,0.64,0.72),(0.01,0.28,0.66,0.72),(0.00,0.25,0.74,0.75)]
man=[(0.66,0.43,0.34,0.27),(0.67,0.43,0.33,0.27),(0.66,0.42,0.34,0.28),(0.67,0.45,0.33,0.27),
     (0.66,0.41,0.34,0.29),(0.66,0.42,0.34,0.28),(0.67,0.43,0.33,0.27),(0.76,0.50,0.24,0.18)]
write({"mediaId":7298,"level":"B","keyWord":"liver","defaultVoice":"female",
 "taps":[{"phrase":"to clutch a model liver","target":"the woman","voice":"female","keys":K(T,woman)},
         {"phrase":"to grimace in pain","target":"the woman","voice":"female","keys":K(T,woman)},
         {"phrase":"to point with a pen","target":"the man","voice":"male","keys":K(T,man)}],
 "stillS":0.2,
 "nouns":[{"word":"a blackboard","x":0.84,"y":0.29,"voice":"female"},
          {"word":"a skeleton","x":0.62,"y":0.47,"voice":"female"},
          {"word":"a liver","x":0.48,"y":0.64,"voice":"female"},
          {"word":"a lab coat","x":0.24,"y":0.82,"voice":"female"}],
 "question":"What is the woman with braids holding?",
 "answer":["She","is","clutching","a","model","of","a","liver."],
 "answerVoice":"female",
 "notes":"Woman box stops at x .66-.74 (her knees reach further right) so it never overlaps the man. Man is mostly out of frame at 3.7: box covers only his hand and sleeve at the right edge. Grimace only from ~1.7 on; at 0.2-1.2 she smiles. Other students (incl. women) sit at desks in the background, hence 'woman with braids'."})
