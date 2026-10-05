import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows):
    out=[]
    for t,r in zip(T,rows):
        if r is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=r; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
    return out
def save(d):
    json.dump(d,open(f"content/{d['mediaId']}.json","w"),indent=1)

# 5623
woman=K([(0.05,0.32,0.47,0.68)]*8)
bald=K([(0.53,0.26,0.24,0.30)]*8)
save({"mediaId":5623,"level":"B","keyWord":"be into","defaultVoice":"female",
 "taps":[{"phrase":"to clutch a stack of records","target":"the woman","voice":"female","keys":woman},
         {"phrase":"to kneel beside wooden crates","target":"the woman","voice":"female","keys":woman},
         {"phrase":"to rummage in a cardboard box","target":"the bald man","voice":"male","keys":bald}],
 "stillS":2.2,
 "nouns":[{"word":"headphones","x":0.17,"y":0.29,"voice":"female"},
          {"word":"a wall lamp","x":0.56,"y":0.11,"voice":"female"},
          {"word":"a cardboard box","x":0.68,"y":0.48,"voice":"female"},
          {"word":"wooden crates","x":0.80,"y":0.85,"voice":"female"}],
 "question":"What is the woman holding?",
 "answer":["She","is","clutching","a","stack","of","records."],"answerVoice":"female",
 "notes":"Woman box stops at x 0.52 so it does not overlap the bald man; her reaching arm/hand at the crates (x 0.55-0.87) lies outside it. Bald man handles something in a box - 'rummage' is a mild reading of his hand movement. Records also lie in the crates, so the answer names the stack she holds."})

# 5624
parrot=K([(0.45,0.26,0.18,0.14),(0.46,0.26,0.18,0.14),(0.46,0.25,0.18,0.14),(0.47,0.23,0.22,0.15),
          (0.47,0.22,0.30,0.15),(0.47,0.23,0.19,0.14),(0.48,0.22,0.18,0.14),(0.51,0.24,0.19,0.14)])
white=K([(0.06,0.41,0.42,0.45),(0.06,0.40,0.42,0.46),(0.04,0.40,0.44,0.50),(0.03,0.39,0.43,0.51),
         (0.0,0.39,0.46,0.53),(0.0,0.39,0.46,0.55),(0.0,0.40,0.46,0.58),(0.0,0.39,0.46,0.61)])
navy=K([(0.66,0.40,0.34,0.48),(0.66,0.40,0.34,0.50),(0.64,0.40,0.36,0.52),(0.64,0.39,0.36,0.56),
        (0.66,0.39,0.34,0.55),(0.68,0.39,0.32,0.58),(0.68,0.41,0.32,0.59),(0.68,0.41,0.32,0.59)])
save({"mediaId":5624,"level":"B","keyWord":"be known as","defaultVoice":"male",
 "taps":[{"phrase":"to spread its wings","target":"the parrot","voice":"male","keys":parrot},
         {"phrase":"to hold a tea glass","target":"the man in the white shirt","voice":"male","keys":white},
         {"phrase":"to point at the standing man","target":"the man in the dark jumper","voice":"male","keys":navy}],
 "stillS":0.2,
 "nouns":[{"word":"a ceiling fan","x":0.14,"y":0.08,"voice":"male"},
          {"word":"a lantern","x":0.55,"y":0.14,"voice":"male"},
          {"word":"a parrot","x":0.55,"y":0.33,"voice":"male"},
          {"word":"mint tea","x":0.22,"y":0.89,"voice":"male"}],
 "question":"Where is the parrot perching?",
 "answer":["It","is","perching","on","the","man's","shoulder."],"answerVoice":"male",
 "notes":"Parrot spreads its wings only around 1.7-2.2 s. A half-visible man at the far left edge also has a tea glass; the man in the white shirt holds his up clearly. Standing young man is not a tap target (parrot sits on him)."})

# 5625
man=K([(0.10,0.36,0.68,0.43)]*8)
dog=K([(0.37,0.80,0.50,0.13)]*8)
save({"mediaId":5625,"level":"A","keyWord":"be on holiday","defaultVoice":"male",
 "taps":[{"phrase":"to drink from a coconut","target":"the man","voice":"male","keys":man},
         {"phrase":"to lie in a hammock","target":"the man","voice":"male","keys":man},
         {"phrase":"to sleep on the sand","target":"the dog","voice":"male","keys":dog}],
 "stillS":2.2,
 "nouns":[{"word":"a hammock","x":0.13,"y":0.57,"voice":"male"},
          {"word":"a dog","x":0.60,"y":0.85,"voice":"male"},
          {"word":"a suitcase","x":0.90,"y":0.70,"voice":"male"},
          {"word":"a beach bar","x":0.25,"y":0.32,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","lying","in","a","hammock."],"answerVoice":"male",
 "notes":"Man box ends at y 0.80 so it does not overlap the dog; his bare foot (x 0.12-0.30, y 0.82-0.89) lies outside it. He drinks from the coconut only in the first half, later just holds it."})

# 5627
cat=K([(0.27,0.44,0.46,0.14),(0.27,0.44,0.46,0.14),(0.25,0.425,0.51,0.16),(0.24,0.425,0.54,0.16),
       (0.26,0.41,0.55,0.185),(0.28,0.41,0.53,0.19),(0.28,0.42,0.53,0.19),(0.27,0.45,0.52,0.17)])
hand=K([(0.38,0.585,0.62,0.415),(0.38,0.585,0.62,0.415),(0.36,0.59,0.64,0.41),(0.36,0.59,0.64,0.41),
        (0.38,0.60,0.62,0.40),(0.40,0.605,0.60,0.395),(0.43,0.67,0.57,0.33),None])
save({"mediaId":5627,"level":"B","keyWord":"be out of stock","defaultVoice":"male",
 "taps":[{"phrase":"to curl up on a shelf","target":"the cat","voice":"male","keys":cat},
         {"phrase":"to yawn widely","target":"the cat","voice":"male","keys":cat},
         {"phrase":"to reach up towards the cat","target":"the hand","voice":"male","keys":hand}],
 "stillS":3.7,
 "nouns":[{"word":"a brass lamp","x":0.20,"y":0.10,"voice":"male"},
          {"word":"a cat","x":0.55,"y":0.52,"voice":"male"},
          {"word":"mosaic tiles","x":0.35,"y":0.93,"voice":"male"}],
 "question":"Where is the cat lying?",
 "answer":["It","is","lying","in","a","gap","between","the","jars."],"answerVoice":"male",
 "notes":"No visible person, only a hand (bracelet, rust sleeve) - defaultVoice male by the evenId rule. The fingertips nearly touch the cat's underside at 1.2-2.7 s; boxes split along the shelf line. Hand leaves the picture by 3.7 s. Only 3 nouns: jars/tins sit on every shelf, so no unambiguous 4th slot."})
