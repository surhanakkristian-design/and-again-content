from gen_5340_5342_5343_5344_lib import K, write
blonde=K([(0.0,0.00,0.28,0.18,0.20),(0.5,0.00,0.30,0.18,0.20),(1.0,0.00,0.30,0.20,0.26),(1.5,0.00,0.27,0.22,0.27),
 (2.0,0.00,0.35,0.49,0.27),(2.5,0.00,0.27,0.44,0.63),(3.0,0.00,0.25,0.50,0.50),(3.5,0.00,0.25,0.47,0.55),
 (4.0,0.00,0.18,0.48,0.60),(4.5,0.00,0.20,0.48,0.58),(5.0,0.00,0.20,0.48,0.60),(5.5,0.00,0.20,0.48,0.62),
 (6.0,0.00,0.27,0.44,0.48),(6.5,0.00,0.29,0.46,0.66),(7.0,0.00,0.19,0.36,0.81),(7.5,0.00,0.25,0.34,0.75),
 (8.0,0.00,0.29,0.50,0.69),(8.5,0.00,0.26,0.47,0.70),(9.0,0.00,0.28,0.46,0.70)])
curly=K([(0.0,0.80,0.28,0.20,0.22),(0.5,0.78,0.30,0.22,0.20),(1.0,0.72,0.32,0.28,0.29),(1.5,0.76,0.27,0.24,0.30),
 (2.0,0.51,0.40,0.49,0.35),(2.5,0.52,0.31,0.48,0.69),(3.0,0.51,0.25,0.49,0.70),(3.5,0.48,0.25,0.52,0.57),
 (4.0,0.49,0.18,0.51,0.62),(4.5,0.49,0.20,0.51,0.62),(5.0,0.49,0.21,0.51,0.62),(5.5,0.49,0.20,0.51,0.62),
 (6.0,0.45,0.21,0.55,0.55),(6.5,0.47,0.03,0.53,0.82),(7.0,0.37,0.18,0.63,0.82),(7.5,0.50,0.26,0.47,0.74),
 (8.0,0.51,0.30,0.49,0.70),(8.5,0.53,0.24,0.47,0.75),(9.0,0.58,0.26,0.42,0.74)])
write(5343,{"mediaId":5343,"level":"B","keyWord":"twin","defaultVoice":"female",
 "taps":[
  {"phrase":"to put on a navy jacket","target":"the curly-haired girl","voice":"female","keys":curly},
  {"phrase":"to wear a tie-dye hoodie","target":"the curly-haired girl","voice":"female","keys":curly},
  {"phrase":"to wear a graphic T-shirt","target":"the blonde girl","voice":"female","keys":blonde}],
 "stillS":4.0,
 "nouns":[{"word":"a power socket","x":0.18,"y":0.16,"voice":"female"},{"word":"a tie-dye hoodie","x":0.75,"y":0.45,"voice":"female"},
  {"word":"beads","x":0.48,"y":0.76,"voice":"female"},{"word":"twin beds","x":0.50,"y":0.91,"voice":"female"}],
 "question":"What are the girls sitting on?",
 "answer":["They","are","sitting","on","twin","beds."],
 "answerVoice":"female",
 "notes":"Almost every action is shared by both girls (peeking, flopping back, threading and tying bracelets - both tie at 4.0-5.5 -, dancing, swinging jackets), so two phrases are clothing states; the only unique action is the navy jacket (7.0-9.0; the blonde puts on an orange one). From 7.5 a mirror shows a reflection of the curly-haired girl between the two; it is not boxed. 'twin beds' pill sits on the join of the two beds."})
