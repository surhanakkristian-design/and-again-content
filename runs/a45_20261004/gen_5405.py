from gen_5405_5406_5407_5408_lib import *
T=[i*0.5 for i in range(19)]
baby={0.0:(0.0,0.0,0.88,0.82),0.5:(0.02,0.0,0.96,0.82),1.0:(0.0,0.0,1.0,0.81),1.5:(0.14,0.0,0.86,0.80),
 2.0:(0.10,0.0,0.89,0.83),2.5:(0.10,0.0,0.89,0.83),3.0:(0.06,0.0,0.94,0.86),3.5:(0.10,0.01,0.86,0.86),4.0:(0.02,0.03,0.90,0.85)}
grey={4.5:(0.24,0.18,0.48,0.68),5.0:(0.30,0.28,0.40,0.63),5.5:(0.26,0.38,0.53,0.48),6.0:(0.32,0.44,0.56,0.39)}
kb=K(T,baby); kg=K(T,grey)
write(5405,{"mediaId":5405,"level":"B","keyWord":"toddler","defaultVoice":"male",
 "taps":[
  {"phrase":"to take wobbly first steps","target":"the baby in stripes","voice":"male","keys":kb},
  {"phrase":"to wear a striped bodysuit","target":"the baby in stripes","voice":"male","keys":kb},
  {"phrase":"to clamber onto a foam block","target":"the toddler in grey","voice":"male","keys":kg}],
 "stillS":3.0,
 "nouns":[{"word":"a toddler","x":0.52,"y":0.48,"voice":"male"},
          {"word":"a woman","x":0.12,"y":0.36,"voice":"female"},
          {"word":"a man","x":0.86,"y":0.22,"voice":"male"},
          {"word":"a rug","x":0.50,"y":0.90,"voice":"male"}],
 "question":"What is the baby in stripes doing?",
 "answer":["The","baby","is","taking","wobbly","first","steps."],
 "answerVoice":"male",
 "notes":"Baby gender unclear -> defaultVoice male (evenId false). Two phrases share the baby target (wobbly steps / striped bodysuit); the kneeling adults both clap and cheer, so no phrase fits only one of them. Toddler in grey only boxed in the close daycare shot 4.5-6.0 (climbs onto the green foam block); off in the wide shots."})
