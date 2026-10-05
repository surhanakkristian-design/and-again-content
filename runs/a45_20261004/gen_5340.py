from gen_5340_5342_5343_5344_lib import K, write
N=None
blue=K([(0.0,0.00,0.25,0.36,0.75),(0.5,0.00,0.24,0.42,0.76),(1.0,0.00,0.22,0.40,0.78),(1.5,0.00,0.35,0.46,0.65),
 (2.0,0.00,0.21,0.48,0.52),(2.5,0.00,0.06,0.62,0.84),(3.0,0.05,0.22,0.60,0.72),(3.5,0.00,0.26,0.18,0.70),
 (4.0,N),(4.5,0.00,0.27,0.46,0.63),(5.0,N),(5.5,0.00,0.15,0.55,0.85),(6.0,0.00,0.08,0.42,0.32),
 (6.5,0.00,0.24,0.37,0.76),(7.0,0.00,0.26,0.31,0.74),(7.5,0.00,0.26,0.47,0.74),(8.0,0.00,0.26,0.50,0.70),
 (8.5,0.00,0.25,0.51,0.71),(9.0,0.00,0.25,0.50,0.71)])
red=K([(0.0,0.64,0.28,0.36,0.72),(0.5,0.66,0.28,0.34,0.72),(1.0,0.78,0.35,0.22,0.65),(1.5,0.70,0.40,0.30,0.55),
 (2.0,0.67,0.33,0.33,0.34),(2.5,0.82,0.00,0.18,0.58),(3.0,0.82,0.45,0.18,0.45),(3.5,0.68,0.38,0.32,0.62),
 (4.0,0.48,0.29,0.52,0.71),(4.5,N),(5.0,0.62,0.26,0.38,0.70),(5.5,N),(6.0,0.55,0.08,0.45,0.75),
 (6.5,0.50,0.26,0.50,0.74),(7.0,0.60,0.28,0.40,0.72),(7.5,0.48,0.28,0.52,0.72),(8.0,0.51,0.27,0.49,0.73),
 (8.5,0.52,0.26,0.48,0.74),(9.0,0.51,0.25,0.49,0.75)])
write(5340,{"mediaId":5340,"level":"A","keyWord":"garage","defaultVoice":"male",
 "taps":[
  {"phrase":"to take a ball out","target":"the boy in blue","voice":"male","keys":blue},
  {"phrase":"to use a screwdriver","target":"the boy in blue","voice":"male","keys":blue},
  {"phrase":"to wear a red hoodie","target":"the boy in red","voice":"male","keys":red}],
 "stillS":3.5,
 "nouns":[{"word":"a garage","x":0.45,"y":0.08,"voice":"male"},{"word":"grass","x":0.22,"y":0.44,"voice":"male"},
  {"word":"a bed","x":0.62,"y":0.34,"voice":"male"},{"word":"a fence","x":0.17,"y":0.31,"voice":"male"}],
 "question":"What are the boys carrying?",
 "answer":["They","are","carrying","a","box","into","the","garage."],
 "answerVoice":"male",
 "notes":"'to use a screwdriver': at 5.5 the close-up face is the blue boy (blue sleeve); at 6.0 both faces under the frame and the screwdriver hand is not clearly his. 'a garage' pill sits on the raised garage door / ceiling. 'a bed' = unfinished bunk-bed frame. Two balls and several boxes at 3.5, so no ball or box noun."})
