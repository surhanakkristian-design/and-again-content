from gen_7162_7163_7164_7166_lib import write
W=[(0.38,0.33,0.31,0.56),(0.33,0.31,0.37,0.65),(0.31,0.25,0.44,0.75),(0.35,0.28,0.47,0.72),(0.26,0.26,0.56,0.74),(0.27,0.27,0.55,0.73),(0.27,0.21,0.73,0.79),(0.33,0.12,0.67,0.88)]
S=[(0.17,0.49,0.21,0.19),(0.14,0.51,0.19,0.21),(0.12,0.52,0.19,0.25),(0.09,0.52,0.26,0.28),(0.02,0.53,0.24,0.30),(0.00,0.52,0.27,0.33),(0.00,0.53,0.27,0.36),(0.02,0.54,0.31,0.40)]
D=[(0.69,0.60,0.18,0.19),(0.70,0.61,0.20,0.21),(0.75,0.63,0.25,0.24),(0.82,0.68,0.18,0.25),(0.82,0.68,0.18,0.27),(0.82,0.71,0.18,0.27),None,None]
write(7164, {"mediaId":7164,"level":"A","keyWord":"get tired","defaultVoice":"female",
 "taps":[{"phrase":"to pull a sled","target":"the woman","voice":"female","keys":W},
         {"phrase":"to ride in the sled","target":"the dogs in the sled","voice":"female","keys":S},
         {"phrase":"to walk on a lead","target":"the dog on the lead","voice":"female","keys":D}],
 "stillS":0.2,
 "nouns":[{"word":"a house","x":0.22,"y":0.24,"voice":"female"},{"word":"trees","x":0.76,"y":0.20,"voice":"female"},
          {"word":"a sled","x":0.31,"y":0.64,"voice":"female"},{"word":"a glove","x":0.10,"y":0.74,"voice":"female"}],
 "question":"What is the woman pulling?",
 "answer":["She","is","pulling","a","sled","with","dogs."],"answerVoice":"female",
 "notes":"'get tired' is a phrase, not placed. Woman's box is cut on the right where the dog on the lead walks behind her (her right glove partly outside at 0.2-1.2 s). Dog on the lead is hidden behind her / out of frame from 3.2 s (off). She pulls the sled only in the first second, then stops and bends over; 'a glove' = the dropped red mitten in the snow; 'a house' = the cabin far behind."})
