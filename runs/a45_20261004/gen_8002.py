from gen_7998_8002_8003_8005_lib import write
WP = [(0.03,0.19,0.47,0.79),(0.03,0.18,0.49,0.80),(0.03,0.17,0.48,0.82),(0.02,0.17,0.51,0.82),
      (0.01,0.15,0.54,0.84),(0.01,0.13,0.53,0.86),(0.00,0.12,0.56,0.88),(0.00,0.12,0.55,0.88)]
BL = [(0.50,0.25,0.29,0.34),(0.56,0.44,0.43,0.26),(0.54,0.44,0.26,0.27),(0.57,0.41,0.36,0.28),
      (0.57,0.40,0.33,0.29),(0.58,0.39,0.32,0.30),(0.59,0.38,0.33,0.31),(0.62,0.36,0.32,0.33)]
DG = [(0.50,0.67,0.20,0.18),(0.53,0.71,0.24,0.17),(0.52,0.71,0.20,0.18),(0.54,0.70,0.24,0.18),
      (0.56,0.70,0.24,0.18),(0.56,0.70,0.27,0.18),(0.58,0.70,0.26,0.19),(0.60,0.70,0.28,0.19)]
write(8002, {"level":"B","keyWord":"stay over","defaultVoice":"female",
 "taps":[
  {"phrase":"to take a mirror selfie","target":"the woman with the phone","voice":"female","boxes":WP},
  {"phrase":"to tug at the bag handles","target":"the woman on the bed","voice":"female","boxes":BL},
  {"phrase":"to sniff an overnight bag","target":"the dachshund","voice":"female","boxes":DG}],
 "stillS":2.2,
 "nouns":[{"word":"a ceiling lamp","x":0.37,"y":0.12,"voice":"female"},
          {"word":"a bookshelf","x":0.56,"y":0.38,"voice":"female"},
          {"word":"a dachshund","x":0.50,"y":0.77,"voice":"female"},
          {"word":"a toothbrush","x":0.75,"y":0.91,"voice":"female"}],
 "question":"What is the dachshund doing?",
 "answer":["It","is","sniffing","an","overnight","bag."],
 "answerVoice":"female",
 "notes":"The dachshund's body is partly behind the selfie woman's shirt line; its box covers only the head and the bag (x from ~0.5) so it does not overlap her box. The woman on the bed jumps on the bed at 0.2, then kneels and pulls the bag handles from 0.7 on. Pill 'a dachshund' sits on the dog body right next to the selfie woman's leg."})
