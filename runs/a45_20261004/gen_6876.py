import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,**dict(zip("xywh",r))) if r else {"t":t,"off":True} for t,r in zip(T,rows)]
woman=K([(0.41,0.18,0.39,0.52),(0.52,0.21,0.25,0.53),(0.48,0.20,0.23,0.58),(0.465,0.22,0.265,0.57),
         (0.42,0.22,0.32,0.59),(0.38,0.25,0.39,0.61),(0.36,0.22,0.33,0.61),(0.41,0.22,0.31,0.57)])
pilot=K([(0.80,0.0,0.20,0.46),(0.77,0.04,0.23,0.49),(0.71,0.11,0.23,0.47),(0.73,0.13,0.20,0.45),
         (0.74,0.16,0.18,0.45),(0.77,0.18,0.18,0.44),(0.69,0.22,0.19,0.27),(0.72,0.23,0.18,0.26)])
worker=K([None,(0.36,0.43,0.16,0.23),(0.32,0.48,0.16,0.24),(0.29,0.50,0.175,0.23),
          (0.22,0.52,0.20,0.23),(0.12,0.54,0.23,0.24),(0.05,0.56,0.22,0.28),(0.0,0.58,0.22,0.28)])
d={"mediaId":6876,"level":"B","keyWord":"board a plane","defaultVoice":"female",
 "taps":[{"phrase":"to board a small plane","target":"the woman","voice":"female","keys":woman},
         {"phrase":"to help her aboard","target":"the pilot","voice":"male","keys":pilot},
         {"phrase":"to load the luggage","target":"the ground worker","voice":"male","keys":worker}],
 "stillS":1.2,
 "nouns":[{"word":"a propeller","x":0.27,"y":0.38,"voice":"female"},
          {"word":"a windsock","x":0.14,"y":0.47,"voice":"female"},
          {"word":"palm trees","x":0.15,"y":0.56,"voice":"female"},
          {"word":"a luggage cart","x":0.20,"y":0.68,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","boarding","a","small","plane."],
 "answerVoice":"female",
 "notes":"Ground worker hidden at 0.2 (off) and stands right behind the woman's legs at 0.7-2.2: boxes split on x, the worker box is narrower than 0.18 there and the woman's hair tip is cut. Pilot's hands on the surfboard fall in the woman's box; at 3.2-3.7 only his head shows behind her."}
json.dump(d,open("content/6876.json","w"),indent=1)
