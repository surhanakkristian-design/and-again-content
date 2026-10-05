from gen_5340_5342_5343_5344_lib import K, write
girl=K([(0.0,0.00,0.20,0.50,0.62),(0.5,0.00,0.20,0.50,0.62),(1.0,0.00,0.20,0.50,0.62),(1.5,0.00,0.20,0.51,0.60),
 (2.0,0.00,0.18,0.48,0.64),(2.5,0.00,0.19,0.45,0.60),(3.0,0.00,0.20,0.45,0.60),(3.5,0.00,0.20,0.50,0.60),
 (4.0,0.00,0.37,0.52,0.63),(4.5,0.00,0.37,0.55,0.63),(5.0,0.00,0.37,0.50,0.63),(5.5,0.00,0.36,0.54,0.64),
 (6.0,0.00,0.18,0.76,0.82),(6.5,0.00,0.18,0.78,0.82),(7.0,0.00,0.22,0.50,0.78),(7.5,0.00,0.22,0.53,0.78),
 (8.0,0.00,0.22,0.47,0.78),(8.5,0.05,0.22,0.51,0.78),(9.0,0.18,0.23,0.32,0.77),(9.5,0.15,0.25,0.29,0.75),
 (10.0,0.10,0.26,0.27,0.74)])
woman=K([(0.0,0.51,0.10,0.49,0.70),(0.5,0.51,0.10,0.49,0.70),(1.0,0.51,0.12,0.49,0.68),(1.5,0.52,0.07,0.48,0.73),
 (2.0,0.50,0.05,0.50,0.75),(2.5,0.47,0.05,0.53,0.75),(3.0,0.47,0.06,0.53,0.74),(3.5,0.52,0.07,0.48,0.73),
 (4.0,0.53,0.19,0.47,0.81),(4.5,0.56,0.18,0.44,0.82),(5.0,0.51,0.18,0.49,0.82),(5.5,0.55,0.18,0.45,0.82),
 (6.0,0.77,0.00,0.23,1.00),(6.5,0.80,0.00,0.20,1.00),(7.0,0.51,0.16,0.49,0.84),(7.5,0.54,0.16,0.46,0.84),
 (8.0,0.48,0.16,0.52,0.84),(8.5,0.57,0.15,0.43,0.85),(9.0,0.51,0.16,0.49,0.84),(9.5,0.45,0.16,0.55,0.84),
 (10.0,0.38,0.17,0.62,0.83)])
write(5342,{"mediaId":5342,"level":"B","keyWord":"tongue","defaultVoice":"female",
 "taps":[
  {"phrase":"to taste the pink frosting","target":"the girl","voice":"female","keys":girl},
  {"phrase":"to hold up a crayon drawing","target":"the girl","voice":"female","keys":girl},
  {"phrase":"to braid the girl's hair","target":"the woman","voice":"female","keys":woman}],
 "stillS":2.5,
 "nouns":[{"word":"a tongue","x":0.30,"y":0.37,"voice":"female"},{"word":"a piping bag","x":0.26,"y":0.60,"voice":"female"},
  {"word":"an apron","x":0.76,"y":0.55,"voice":"female"},{"word":"cupcakes","x":0.50,"y":0.87,"voice":"female"}],
 "question":"What is the girl tasting?",
 "answer":["She","is","tasting","the","pink","frosting."],
 "answerVoice":"female",
 "notes":"Girl and woman overlap a lot (piping, braiding, hug); boxes split along the line between them, so the woman's reaching hands / arms partly fall in the girl's box. The man in the background (4.0-5.5) is deliberately not a target. 'a tongue' pill sits on the girl's open mouth next to the woman's finger at 2.5."})
