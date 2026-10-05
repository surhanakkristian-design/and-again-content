from gen_5405_5406_5407_5408_lib import *
T=[i*0.5 for i in range(25)]
seq={0.0:(0.38,0.27,0.62,0.73),0.5:(0.31,0.27,0.69,0.73),1.0:(0.32,0.28,0.68,0.72),1.5:(0.43,0.28,0.57,0.72),
 2.0:(0.49,0.30,0.51,0.70),2.5:(0.49,0.29,0.51,0.71),3.0:(0.47,0.30,0.53,0.70),3.5:(0.20,0.33,0.58,0.67),
 4.0:(0.08,0.35,0.54,0.65),4.5:(0.02,0.35,0.56,0.65),5.0:(0,0.36,0.50,0.64),5.5:(0,0.36,0.48,0.64),
 6.0:(0,0.35,0.47,0.65),6.5:(0,0.36,0.46,0.64),7.0:(0,0.37,0.47,0.63),7.5:(0,0.37,0.49,0.63),
 8.0:(0.54,0.34,0.46,0.66),8.5:(0.53,0.34,0.47,0.66),9.0:(0.54,0.34,0.46,0.66),9.5:(0.55,0.34,0.45,0.66),
 10.0:(0.46,0.34,0.54,0.66),10.5:(0.13,0.39,0.60,0.61),11.0:(0,0.48,0.30,0.52)}
man={9.0:(0,0.36,0.22,0.64),9.5:(0.12,0.30,0.33,0.70)}
dress={5.0:(0.70,0.36,0.18,0.40),5.5:(0.68,0.35,0.18,0.42),6.0:(0.62,0.36,0.22,0.50),6.5:(0.68,0.35,0.24,0.57),
 7.0:(0.66,0.34,0.28,0.66),7.5:(0.64,0.34,0.32,0.66),10.5:(0.80,0.31,0.20,0.69),11.0:(0.75,0.31,0.25,0.69),
 11.5:(0.64,0.31,0.36,0.69),12.0:(0.48,0.31,0.40,0.69)}
write(5407,{"mediaId":5407,"level":"A","keyWord":"toilet","defaultVoice":"female",
 "taps":[
  {"phrase":"to knock on a door","target":"the woman in sequins","voice":"female","keys":K(T,seq)},
  {"phrase":"to leave the bathroom","target":"the man in the bathroom","voice":"male","keys":K(T,man)},
  {"phrase":"to wear a colourful dress","target":"the woman in the dress","voice":"female","keys":K(T,dress)}],
 "stillS":10.0,
 "nouns":[{"word":"a toilet","x":0.27,"y":0.82,"voice":"female"},
          {"word":"a phone","x":0.48,"y":0.63,"voice":"female"},
          {"word":"a jacket","x":0.84,"y":0.76,"voice":"female"},
          {"word":"a wall","x":0.24,"y":0.28,"voice":"female"}],
 "question":"What are the guests waiting for?",
 "answer":["They","are","waiting","for","the","toilet."],
 "answerVoice":"female",
 "notes":"The man is only a sliver at the left edge at 9.0 s and fully visible at 9.5 s (a blue sleeve at the left edge at 10.0 s may be him, marked off). Woman in the dress marked off at 10.0 s (only part of her face at the right edge, behind the sequin woman's box). In the end it is the woman in sequins who walks into the bathroom (10.5-11.0 s), not the next guest as the description says."})
