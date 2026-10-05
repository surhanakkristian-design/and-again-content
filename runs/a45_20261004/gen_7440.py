import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]}) for t,r in zip(T,rows)]
bear=[(0.18,0.29,0.47,0.69),(0.17,0.37,0.50,0.61),(0.01,0.54,0.72,0.46),(0.04,0.54,0.72,0.46),
      (0.05,0.53,0.67,0.45),(0.11,0.53,0.63,0.41),(0.15,0.52,0.74,0.44),(0.16,0.52,0.78,0.47)]
woman=[(0.65,0.13,0.31,0.24),(0.61,0.12,0.33,0.24),(0.58,0.12,0.37,0.27),(0.58,0.12,0.34,0.27),
       (0.53,0.12,0.34,0.27),(0.52,0.12,0.29,0.25),(0.50,0.14,0.26,0.24),(0.50,0.15,0.22,0.23)]
far=[(0.0,0.42,0.17,0.15),(0.0,0.42,0.16,0.15),(0.03,0.39,0.18,0.14),(0.03,0.39,0.18,0.14),
     (0.03,0.38,0.18,0.14),(0.03,0.38,0.18,0.14),(0.03,0.37,0.18,0.14),(0.03,0.37,0.18,0.14)]
c={"mediaId":7440,"level":"B","keyWord":"polar bear","defaultVoice":"female",
 "taps":[{"phrase":"to paw at the bus","target":"the big polar bear","voice":"female","keys":K(bear)},
         {"phrase":"to wave through the window","target":"the woman in the cream hat","voice":"female","keys":K(woman)},
         {"phrase":"to watch from a distance","target":"the bear in the distance","voice":"female","keys":K(far)}],
 "stillS":3.7,
 "nouns":[{"word":"the sky","x":0.20,"y":0.10,"voice":"female"},{"word":"a knitted hat","x":0.60,"y":0.23,"voice":"female"},
          {"word":"a polar bear","x":0.55,"y":0.70,"voice":"female"},{"word":"snow","x":0.18,"y":0.88,"voice":"female"}],
 "question":"What is the big polar bear doing?",
 "answer":["It","is","walking","alongside","the","bus."],"answerVoice":"female",
 "notes":"Big bear paws at the bus 0.2-0.7, then walks along it on all fours. Woman in the cream hat waves/presses hands at the glass; at 3.2-3.7 she also covers her mouth (man in black hat does too, so no mouth phrase). Distant bear is small at the left; at 0.2-0.7 the big bear's box starts at x .17-.18 to avoid the distant bear's box, cropping a thin slice of its left legs/back. 'a polar bear' pill is on the big bear; the distant bear carries no noun."}
json.dump(c,open('content/7440.json','w'),indent=1)
