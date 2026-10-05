import json
O={"off":True}
def b(x,y,w,h): return {"x":x,"y":y,"w":w,"h":h}
def keys(times,d): return [dict(t=t,**d[t]) for t in times]
T21=[i*0.5 for i in range(21)]
def dump(c): json.dump(c,open('content/%d.json'%c["mediaId"],'w'),indent=1)
M={0.0:b(0.27,0.38,0.18,0.35),0.5:b(0.23,0.36,0.18,0.36),1.0:b(0.22,0.38,0.18,0.45),1.5:b(0.23,0.37,0.18,0.49),2.0:b(0.24,0.33,0.18,0.44),
2.5:b(0.21,0.30,0.19,0.50),3.0:b(0.15,0.29,0.19,0.65),3.5:b(0.15,0.30,0.23,0.68),4.0:b(0.08,0.33,0.34,0.61),4.5:b(0.12,0.32,0.46,0.68),
5.0:b(0.53,0.31,0.33,0.69),5.5:b(0.59,0.31,0.33,0.68),6.0:b(0.61,0.30,0.34,0.59),6.5:b(0.58,0.31,0.34,0.54),7.0:b(0.53,0.34,0.27,0.59),
7.5:b(0.48,0.36,0.24,0.56),8.0:b(0.48,0.38,0.22,0.40),8.5:b(0.46,0.30,0.29,0.47),9.0:b(0.48,0.31,0.29,0.59),9.5:b(0.46,0.32,0.28,0.57),10.0:b(0.47,0.34,0.24,0.43)}
W={0.0:b(0.46,0.40,0.18,0.36),0.5:b(0.42,0.40,0.18,0.37),1.0:b(0.41,0.40,0.18,0.48),1.5:b(0.42,0.40,0.18,0.50),2.0:b(0.43,0.39,0.18,0.43),
2.5:b(0.41,0.38,0.18,0.48),3.0:b(0.35,0.38,0.19,0.62),3.5:b(0.39,0.37,0.22,0.63),4.0:b(0.43,0.36,0.27,0.64),4.5:b(0.59,0.37,0.41,0.63),
5.0:b(0.26,0.38,0.26,0.57),5.5:b(0.30,0.37,0.28,0.59),6.0:b(0.30,0.37,0.30,0.49),6.5:b(0.30,0.37,0.27,0.47),7.0:b(0.27,0.38,0.25,0.54),
7.5:b(0.25,0.40,0.22,0.51),8.0:b(0.26,0.41,0.21,0.37),8.5:b(0.25,0.40,0.20,0.37),9.0:b(0.22,0.36,0.25,0.53),9.5:b(0.22,0.37,0.23,0.52),10.0:b(0.21,0.39,0.25,0.38)}
F={0.0:b(0.56,0.15,0.32,0.24),0.5:b(0.55,0.16,0.32,0.24),1.0:b(0.59,0.13,0.26,0.29),1.5:b(0.62,0.11,0.22,0.33),2.0:b(0.58,0.05,0.33,0.33),
2.5:b(0.67,0.04,0.26,0.32),3.0:b(0.61,0,0.26,0.40),3.5:b(0.64,0,0.27,0.41),4.0:b(0.60,0,0.40,0.35),4.5:b(0.80,0.01,0.20,0.26),
5.0:b(0.80,0.06,0.20,0.24),5.5:b(0.65,0.08,0.35,0.22),6.0:b(0.56,0.11,0.18,0.18),6.5:b(0.44,0.15,0.18,0.15),7.0:b(0.37,0.19,0.18,0.14),
7.5:b(0.30,0.21,0.18,0.14),8.0:b(0.33,0.23,0.18,0.14),8.5:O,9.0:O,9.5:O,10.0:O}
dump({"mediaId":581,"level":"B","keyWord":"protesting","defaultVoice":"male",
"taps":[{"phrase":"to clutch a sunflower","target":"the man in the grey T-shirt","voice":"male","keys":keys(T21,M)},
{"phrase":"to carry a tree placard","target":"the woman in the green headscarf","voice":"female","keys":keys(T21,W)},
{"phrase":"to flutter in the breeze","target":"the green flag","voice":"male","keys":keys(T21,F)}],
"stillS":6.5,
"nouns":[{"word":"a sunflower","x":0.84,"y":0.50,"voice":"male"},{"word":"a palm tree","x":0.85,"y":0.14,"voice":"male"},
{"word":"the sky","x":0.35,"y":0.06,"voice":"male"},{"word":"a crowd","x":0.30,"y":0.66,"voice":"male"}],
"question":"What are the people doing?","answer":["They","are","protesting","with","painted","placards."],"answerVoice":"male",
"notes":"Crowd clip, camera swings from behind (0.0-4.5) to the front (5.0+). Man in the grey T-shirt = the one with the sunflower throughout (from behind he also carries a white sign). The woman in the green headscarf walks next to him from behind (0.0-4.5) and carries the tree placard from 5.0 on; at 5.0 the picture shows TWO green headscarves for a moment (one front left with the tree, one back view at the right edge) - the box is on the front one with the placard. Her placard is not visible while she is seen from behind. From 6.0 the flag is only a small folded green shape behind the placards; off from 8.5 (hidden). In the back view the boxes of man and woman are narrow and split between them. Mixed group -> defaultVoice male (odd id)."})
