import json
def b(x,y,w,h): return {"x":x,"y":y,"w":w,"h":h}
def keys(d,times): return [dict(t=t,**(d if "x" in d else d[t])) for t in times]
def T(n): return [i*0.5 for i in range(n)]
def save(c): json.dump(c,open(f'content/{c["mediaId"]}.json','w'),indent=1)

# 4153
t=T(9)
save({"mediaId":4153,"level":"A","keyWord":"highway","defaultVoice":"male",
"taps":[{"phrase":"to drive on the highway","target":"the blue car","voice":"male","keys":keys(b(0.24,0.57,0.57,0.28),t)},
{"phrase":"to have snow on top","target":"the mountains","voice":"male","keys":keys(b(0,0.08,1.0,0.35),t)},
{"phrase":"to hang over the fields","target":"the cloud","voice":"male","keys":keys(b(0,0.44,1.0,0.11),t)}],
"stillS":2.0,
"nouns":[{"word":"mountains","x":0.50,"y":0.25,"voice":"male"},{"word":"a cloud","x":0.30,"y":0.48,"voice":"male"},
{"word":"a car","x":0.52,"y":0.70,"voice":"male"},{"word":"a highway","x":0.50,"y":0.88,"voice":"male"}],
"question":"What is the blue car doing?","answer":["It","is","driving","on","the","highway."],"answerVoice":"male",
"notes":"Only one moving thing (the blue car); mountains and cloud are states. Our own car also drives on the highway but only a sliver of its bonnet is visible at the bottom edge. Cloud box is a thin full-width band (0.44-0.55) between the mountain box and the car box."})

# 4154
t=T(10)
W={0.0:b(0.33,0.39,0.43,0.56),0.5:b(0.33,0.39,0.50,0.56),1.0:b(0.42,0.56,0.49,0.40),1.5:b(0.33,0.50,0.53,0.40),2.0:b(0.44,0.48,0.32,0.40),
2.5:b(0.33,0.49,0.45,0.42),3.0:b(0.42,0.50,0.48,0.48),3.5:b(0.36,0.50,0.60,0.48),4.0:b(0.52,0.44,0.39,0.50),4.5:b(0.32,0.46,0.59,0.47)}
P=b(0.42,0.24,0.24,0.14)
save({"mediaId":4154,"level":"A","keyWord":"sport","defaultVoice":"female",
"taps":[{"phrase":"to hit a tennis ball","target":"the woman","voice":"female","keys":keys(W,t)},
{"phrase":"to hold a racket","target":"the woman","voice":"female","keys":keys(W,t)},
{"phrase":"to watch from a balcony","target":"the people on the balcony","voice":"female","keys":keys(P,t)}],
"stillS":3.5,
"nouns":[{"word":"a building","x":0.40,"y":0.14,"voice":"female"},{"word":"palm trees","x":0.25,"y":0.44,"voice":"female"},
{"word":"a racket","x":0.46,"y":0.59,"voice":"female"},{"word":"a woman","x":0.78,"y":0.70,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","hitting","a","tennis","ball."],"answerVoice":"female",
"notes":"Two phrases share the woman (the only other actors are the two small people on the lower balcony). The balcony people are small and dark; box is the minimum size. Key word 'sport' is not a visible noun and not used. The ball itself is tiny and not a target."})

# 4155
t=T(19)
K={0.0:b(0.15,0.14,0.66,0.58),0.5:b(0.16,0.17,0.68,0.61),1.0:b(0.13,0.20,0.70,0.68),1.5:b(0.07,0.13,0.80,0.58),2.0:b(0.11,0.18,0.60,0.48),
2.5:b(0.0,0.40,0.50,0.28),3.0:b(0.06,0.12,0.90,0.84),3.5:b(0.05,0.07,0.95,0.89),4.0:b(0.05,0.07,0.95,0.85),4.5:b(0.05,0.20,0.68,0.38),
5.0:b(0.22,0.15,0.72,0.43),5.5:b(0.21,0.13,0.62,0.45),6.0:b(0.10,0.03,0.88,0.87),6.5:b(0.0,0.0,0.86,0.80),7.0:b(0.0,0.0,0.88,0.85),
7.5:b(0.0,0.0,0.95,0.78),8.0:b(0.08,0.05,0.87,0.63),8.5:b(0.0,0.09,0.88,0.65),9.0:b(0.02,0.04,0.90,0.68)}
save({"mediaId":4155,"level":"A","keyWord":"clean","defaultVoice":"male",
"taps":[{"phrase":"to wash a dirty plate","target":"the kitten","voice":"male","keys":keys(K,t)},
{"phrase":"to look into the toilet","target":"the kitten","voice":"male","keys":keys(K,t)},
{"phrase":"to hold a clean plate","target":"the kitten","voice":"male","keys":keys(K,t)}],
"stillS":0.0,
"nouns":[{"word":"a kitten","x":0.40,"y":0.30,"voice":"male"},{"word":"a plant","x":0.85,"y":0.22,"voice":"male"},
{"word":"a plate","x":0.50,"y":0.56,"voice":"male"},{"word":"a toilet","x":0.45,"y":0.84,"voice":"male"}],
"question":"What is the kitten doing?","answer":["It","is","washing","a","plate","in","the","toilet."],"answerVoice":"male",
"notes":"The kitten is the only actor, so all three phrases share it; the clip has many cuts and the kitten is in every shot (at 2.5 s only its paw on the flush handle). The box includes the plate it holds. Key word 'clean' is in phrase 3 (clean plate at 6.5-8.5 s)."})

# 4157
save({"mediaId":4157,"level":"B","keyWord":"race","defaultVoice":"female",
"taps":[{"phrase":"to hold up a cardboard sign","target":"the elderly woman","voice":"female","keys":keys(b(0.25,0.27,0.50,0.50),t)},
{"phrase":"to line the wet avenue","target":"the trees","voice":"female","keys":keys(b(0,0,1.0,0.27),t)},
{"phrase":"to lie scattered on the road","target":"the fallen leaves","voice":"female","keys":keys(b(0,0.78,1.0,0.22),t)}],
"stillS":1.5,
"nouns":[{"word":"an arch","x":0.52,"y":0.28,"voice":"female"},{"word":"a scarf","x":0.50,"y":0.39,"voice":"female"},
{"word":"a cardboard sign","x":0.50,"y":0.52,"voice":"female"},{"word":"leaves","x":0.50,"y":0.86,"voice":"female"}],
"question":"What are the runners doing?","answer":["They","are","racing","past","an","elderly","woman."],"answerVoice":"female",
"notes":"The runners pass on both sides of the woman, so one box cannot hold them without overlapping hers: they are not a tap target; the key word 'race' is in the model answer instead. Tree box = top band (trunks reach a little lower at the edges, behind the runners). A few leaves also lie between y 0.60 and 0.78 around the woman's feet, outside the leaves box. The arch is small and partly behind the woman's head line."})
