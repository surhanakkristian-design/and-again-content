import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]}) for t,r in zip(T,rows)]
young=[(0.04,0.36,0.52,0.44),(0.07,0.36,0.51,0.44),(0.06,0.36,0.52,0.45),(0.08,0.36,0.49,0.45),
       (0.02,0.27,0.52,0.58),(0.0,0.15,0.45,0.71),(0.0,0.12,0.37,0.75),(0.0,0.12,0.38,0.75)]
cush=[(0.57,0.42,0.30,0.24),(0.59,0.42,0.30,0.22),(0.58,0.42,0.29,0.22),(0.58,0.42,0.28,0.22),
      (0.55,0.42,0.33,0.28),(0.57,0.43,0.36,0.28),(0.62,0.45,0.37,0.28),(0.66,0.45,0.34,0.29)]
tray=[(0.74,0.28,0.20,0.14),(0.75,0.28,0.20,0.14),(0.77,0.28,0.19,0.14),(0.77,0.28,0.20,0.14),
      (0.78,0.28,0.19,0.14),(0.80,0.28,0.19,0.14),(0.82,0.28,0.18,0.17),(0.82,0.28,0.18,0.17)]
c={"mediaId":7439,"level":"B","keyWord":"poker","defaultVoice":"male",
 "taps":[{"phrase":"to stoke the fire","target":"the young man","voice":"male","keys":K(young)},
         {"phrase":"to hide behind a cushion","target":"the man with the cushion","voice":"male","keys":K(cush)},
         {"phrase":"to hold a silver tray","target":"the man with the tray","voice":"male","keys":K(tray)}],
 "stillS":3.7,
 "nouns":[{"word":"a mantelpiece","x":0.42,"y":0.34,"voice":"male"},{"word":"a poker","x":0.45,"y":0.50,"voice":"male"},
          {"word":"logs","x":0.76,"y":0.76,"voice":"male"},{"word":"tongs","x":0.40,"y":0.93,"voice":"male"}],
 "question":"What is the young man doing?",
 "answer":["He","is","stoking","the","fire","with","a","poker."],"answerVoice":"male",
 "notes":"Young man crouches and stokes the fire 0.2-1.7, stands up and walks away 2.2-3.7. Man with the cushion holds it in front of his face 0.2-1.7, later just sits with it. Tray man is small at the right edge, partly behind flames/sparks at 1.7; split from the cushion man along y ~0.42-0.45."}
json.dump(c,open('content/7439.json','w'),indent=1)
