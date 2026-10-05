from gen_5592_5593_5595_5596_lib import keys, write
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
top=[0.60,0.60,0.61,0.61,0.62,0.63,0.63,0.64]
gy=[0.27,0.27,0.28,0.27,0.25,0.26,0.24,0.26]
goat=keys([(t,0,gy[i],0.30,min(0.34,top[i]-gy[i])) for i,t in enumerate(T)])
woman=keys([(t,0.30,0.15,0.58,top[i]-0.15) for i,t in enumerate(T)])
jumper=keys([(t,0,top[i],0.53,1-top[i]-0.02) for i,t in enumerate(T)])
write(5592,{"mediaId":5592,"level":"B","keyWord":"aware","defaultVoice":"female",
 "taps":[{"phrase":"to carry off a cake box","target":"the goat","voice":"female","keys":goat},
         {"phrase":"to bite into a sandwich","target":"the red-haired woman","voice":"female","keys":woman},
         {"phrase":"to wear a knitted jumper","target":"the woman in the jumper","voice":"female","keys":jumper}],
 "stillS":0.2,
 "nouns":[{"word":"a willow","x":0.25,"y":0.10,"voice":"female"},
          {"word":"a rowing boat","x":0.82,"y":0.33,"voice":"female"},
          {"word":"a goat","x":0.14,"y":0.50,"voice":"female"},
          {"word":"a jug","x":0.58,"y":0.74,"voice":"female"}],
 "question":"What is the goat doing?",
 "answer":["The","goat","is","carrying","off","a","cake","box."],
 "answerVoice":"female",
 "notes":"Key word 'aware' is an adjective, not placed. The young man is left out as a target: he and both women lie close together and his action (looking at his friend) is not unique. Tap boxes of the goat and the kneeling woman are split at x=0.30 (her elbow and the box nearly touch); the kneeling woman's box stops where the jumper woman's head begins, so her lower skirt is outside it. The cake box is partly cut off at the goat's split edge in the first frames."})
