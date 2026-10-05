import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,**dict(zip("xywh",r))) if r else {"t":t,"off":True} for t,r in zip(T,rows)]
woman=K([(0.02,0.22,0.60,0.44),(0.02,0.21,0.61,0.45),(0.0,0.21,0.64,0.45),(0.02,0.20,0.63,0.46),
         (0.0,0.18,0.65,0.45),(0.0,0.17,0.64,0.48),(0.0,0.18,0.53,0.48),(0.0,0.20,0.52,0.47)])
cat=K([(0.62,0.44,0.18,0.16),(0.63,0.44,0.18,0.17),(0.645,0.45,0.18,0.16),(0.655,0.45,0.18,0.16),
       (0.655,0.44,0.18,0.16),(0.64,0.44,0.19,0.17),(0.54,0.47,0.29,0.16),(0.52,0.47,0.38,0.15)])
d={"mediaId":6874,"level":"B","keyWord":"blogger","defaultVoice":"female",
 "taps":[{"phrase":"to chew a mouthful of cake","target":"the woman","voice":"female","keys":woman},
         {"phrase":"to type with one hand","target":"the woman","voice":"female","keys":woman},
         {"phrase":"to peer over the laptop","target":"the cat","voice":"female","keys":cat}],
 "stillS":0.2,
 "nouns":[{"word":"a blogger","x":0.30,"y":0.42,"voice":"female"},
          {"word":"fairy lights","x":0.80,"y":0.30,"voice":"female"},
          {"word":"a laptop","x":0.84,"y":0.55,"voice":"female"},
          {"word":"a mixing bowl","x":0.12,"y":0.64,"voice":"female"}],
 "question":"What is the blogger doing?",
 "answer":["She","is","chewing","a","mouthful","of","cake."],
 "answerVoice":"female",
 "notes":"Woman and cat boxes split near x 0.63-0.66 (her keyboard hand vs the cat behind the laptop); at 3.2-3.7 the cat walks behind the laptop, box widened. Cat peers over the laptop only in 0.2-2.7."}
json.dump(d,open("content/6874.json","w"),indent=1)
