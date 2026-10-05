from gen_5405_5406_5407_5408_lib import *
T=[i*0.5 for i in range(25)]
w={0.0:(0.19,0.10,0.70,0.90),0.5:(0.19,0.10,0.71,0.90),1.0:(0.19,0.10,0.70,0.90),1.5:(0.19,0.10,0.70,0.90),2.0:(0.19,0.09,0.70,0.91),
 2.5:(0.15,0,0.85,0.26),3.0:(0,0,1,0.24),3.5:(0.64,0,0.36,0.30),4.0:(0.54,0,0.46,0.28),4.5:(0.54,0,0.46,0.28),
 5.0:(0.50,0,0.50,0.37),5.5:(0.50,0,0.50,0.37),6.0:(0.40,0,0.60,0.42),
 6.5:(0,0,0.32,0.68),7.0:(0,0,0.32,0.80),7.5:(0,0,0.32,0.68),8.0:(0,0,0.32,0.72),
 8.5:(0.42,0.16,0.58,0.81),9.0:(0.43,0.17,0.55,0.83),9.5:(0.42,0,0.58,0.98),10.0:(0.25,0.12,0.75,0.54),
 10.5:(0.24,0.06,0.76,0.60),11.0:(0.22,0.08,0.78,0.58),11.5:(0.04,0.08,0.96,0.58),12.0:(0,0.07,1,0.61)}
c={2.5:(0,0.28,1,0.70),3.0:(0,0.26,1,0.72),3.5:(0,0.32,1,0.66),4.0:(0,0.30,1,0.66),4.5:(0,0.30,1,0.66),
 5.0:(0,0.39,1,0.57),5.5:(0,0.39,1,0.57),6.0:(0,0.44,1,0.52),
 8.5:(0,0.68,0.40,0.28),9.0:(0,0.68,0.42,0.28),9.5:(0,0.68,0.41,0.28),10.0:(0,0.68,0.44,0.28),10.5:(0,0.68,0.44,0.28),
 11.0:(0,0.68,0.44,0.28),11.5:(0,0.68,0.43,0.28),12.0:(0,0.70,0.44,0.26)}
kw=K(T,w)
write(5408,{"mediaId":5408,"level":"A","keyWord":"kit","defaultVoice":"female",
 "taps":[
  {"phrase":"to take out a screwdriver","target":"the woman","voice":"female","keys":kw},
  {"phrase":"to sit on a chair","target":"the woman","voice":"female","keys":kw},
  {"phrase":"to hold lots of tools","target":"the red case","voice":"female","keys":K(T,c)}],
 "stillS":12.0,
 "nouns":[{"word":"a kit","x":0.20,"y":0.83,"voice":"female"},
          {"word":"a chair","x":0.66,"y":0.90,"voice":"female"},
          {"word":"a ladder","x":0.85,"y":0.40,"voice":"female"},
          {"word":"a shirt","x":0.52,"y":0.52,"voice":"female"}],
 "question":"What is the woman fixing?",
 "answer":["She","is","fixing","a","chair."],
 "answerVoice":"female",
 "notes":"Woman and red case overlap in the close shots 2.5-6.0 s: split horizontally (woman = hands/shirt at the top, case = the tray below), so her hand reaching into the case is partly in the case box. 6.5-8.0 s close-up under the seat: only her hands at the left edge. 10.0-12.0 s her box stops above the case (split at y 0.67), cutting off her lower legs. 'a kit' = the red tool case."})
