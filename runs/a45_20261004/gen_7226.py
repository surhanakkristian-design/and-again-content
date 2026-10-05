from gen_7225_7226_7228_7229_lib import *
man=keys([(0.12,0.33,0.39,0.40),(0.12,0.33,0.38,0.40),(0.10,0.33,0.40,0.40),(0.10,0.32,0.42,0.42),
          (0.06,0.30,0.43,0.42),(0.05,0.28,0.49,0.45),(0.02,0.27,0.52,0.47),(0.02,0.26,0.52,0.48)])
wom=keys([(0.52,0.32,0.48,0.48),(0.51,0.32,0.49,0.49),(0.55,0.31,0.45,0.52),(0.62,0.30,0.38,0.58),
          (0.64,0.27,0.36,0.62),(0.66,0.26,0.34,0.68),(0.56,0.26,0.44,0.70),(0.55,0.26,0.45,0.72)])
write(7226,dict(level="B",keyWord="homeless",defaultVoice="male",
 taps=[dict(phrase="to sip a steaming coffee",target="the bearded man",voice="male",keys=man),
       dict(phrase="to crouch on the pavement",target="the young woman",voice="female",keys=wom),
       dict(phrase="to offer a paper bag",target="the young woman",voice="female",keys=wom)],
 stillS=2.2,
 nouns=[dict(word="a beanie",x=0.32,y=0.34,voice="male"),
        dict(word="a paper bag",x=0.74,y=0.62,voice="male"),
        dict(word="a sleeping bag",x=0.40,y=0.72,voice="male"),
        dict(word="cardboard",x=0.25,y=0.92,voice="male")],
 question="What is the bearded man doing?",
 answer=["He","is","sipping","a","steaming","coffee."],
 answerVoice="male",
 notes="keyword 'homeless' is not a placeable noun. Woman's reaching hand at 3.7 s crosses under the man's hands; box split at x 0.55. Dog not used as target (small, half hidden)."))
