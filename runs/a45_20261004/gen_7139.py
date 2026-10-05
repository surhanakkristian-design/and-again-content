from gen_7139_7140_7141_7142_lib import write
W=[(0,0.26,0.65,0.55),(0,0.26,0.65,0.56),(0,0.25,0.64,0.58),(0,0.24,0.62,0.61),(0,0.23,0.60,0.64),(0,0.21,0.58,0.67),(0,0.19,0.55,0.79),(0,0.17,0.50,0.83)]
M=[(0.66,0.35,0.22,0.20),(0.66,0.35,0.24,0.20),(0.65,0.35,0.24,0.20),(0.63,0.33,0.25,0.22),(0.61,0.32,0.27,0.22),(0.59,0.31,0.28,0.23),(0.56,0.33,0.28,0.25),(0.52,0.33,0.26,0.26)]
B=[(0.22,0.04,0.38,0.21),(0.28,0.0,0.36,0.25),(0.30,0.0,0.38,0.25),(0.24,0.0,0.50,0.24),(0.19,0.09,0.57,0.14),(0.17,0.05,0.59,0.16),(0.11,0.0,0.60,0.19),(0.02,0.05,0.36,0.11)]
write(7139, {"mediaId":7139,"level":"A","keyWord":"fortune","defaultVoice":"female",
 "taps":[{"phrase":"to open her arms wide","target":"the woman","voice":"female","keys":W},
         {"phrase":"to hold up a fish","target":"the man with the fish","voice":"male","keys":M},
         {"phrase":"to fly over the boat","target":"the birds","voice":"female","keys":B}],
 "stillS":1.7,
 "nouns":[{"word":"a net","x":0.15,"y":0.15,"voice":"female"},{"word":"the sky","x":0.70,"y":0.12,"voice":"female"},
          {"word":"a boat","x":0.82,"y":0.55,"voice":"female"},{"word":"fish","x":0.45,"y":0.80,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","standing","in","a","lot","of","fish."],"answerVoice":"female",
 "notes":"Key word 'fortune' is abstract, not placed as a noun. 'the birds' = the group of seagulls above; their box is cut at the woman's head line to avoid overlap. A second man (green cap) appears bottom-left from 3.2 s, not a target."})
