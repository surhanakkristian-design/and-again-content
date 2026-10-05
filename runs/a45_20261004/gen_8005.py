from gen_7998_8002_8003_8005_lib import write
MN = [(0.60,0.17,0.25,0.23),(0.61,0.16,0.26,0.23),(0.53,0.16,0.30,0.24),(0.63,0.16,0.31,0.24),
      (0.62,0.16,0.30,0.23),(0.52,0.16,0.33,0.23),(0.49,0.17,0.33,0.24),(0.46,0.17,0.33,0.24)]
YW = [(0.00,0.40,0.24,0.24),(0.00,0.40,0.24,0.25),(0.00,0.41,0.24,0.25),(0.01,0.41,0.30,0.26),
      (0.00,0.41,0.29,0.27),(0.00,0.42,0.25,0.27),(0.00,0.44,0.18,0.25),None]
GW = [None,None,None,(0.62,0.42,0.18,0.22),
      (0.63,0.42,0.27,0.26),(0.67,0.45,0.32,0.25),(0.67,0.45,0.31,0.26),(0.66,0.45,0.32,0.27)]
write(8005, {"level":"B","keyWord":"stop over","defaultVoice":"male",
 "taps":[
  {"phrase":"to toss down a duffel bag","target":"the man on the roof","voice":"male","boxes":MN},
  {"phrase":"to carry a sleeping bag","target":"the woman at the motel door","voice":"female","boxes":YW},
  {"phrase":"to open a cool box","target":"the woman in the grey T-shirt","voice":"female","boxes":GW}],
 "stillS":2.2,
 "nouns":[{"word":"a neon star","x":0.34,"y":0.20,"voice":"male"},
          {"word":"a camper van","x":0.45,"y":0.56,"voice":"male"},
          {"word":"a pillow","x":0.63,"y":0.69,"voice":"male"},
          {"word":"a cool box","x":0.90,"y":0.60,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","kneeling","on","the","camper","van","roof."],
 "answerVoice":"male",
 "notes":"POV clip: the catcher's hands/bag fill the foreground (not a target). The man tosses the first bag at 0.2 and handles a second bag from 1.2 on. The woman in the grey T-shirt is set off at 0.2-1.2: a blonde figure by the van at 0.2/0.7 is probably her but small and half hidden, and at 1.2 the caught bag hides the van; she lifts the cool box lid at 3.2-3.7. The woman at the motel door goes inside and is gone at 3.7."})
