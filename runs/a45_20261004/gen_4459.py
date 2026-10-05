from gen_4457 import write
W={0.0:(0.0,0.15,0.18,0.78),0.5:(0.0,0.15,0.18,0.78),1.0:(0.0,0.0,0.24,0.88),1.5:(0.0,0.0,0.45,0.97),
2.0:(0.0,0.03,0.50,1.0),2.5:(0.0,0.03,0.52,1.0),3.0:(0.0,0.05,0.52,1.0),3.5:(0.0,0.06,0.55,1.0),
4.0:(0.0,0.06,0.50,0.90),4.5:(0.0,0.06,0.48,0.80),5.0:(0.0,0.08,0.44,0.92),5.5:(0.0,0.10,0.44,0.95),
6.0:(0.0,0.10,0.42,0.75),6.5:(0.0,0.12,0.44,0.75),7.0:(0.0,0.14,0.39,0.92),7.5:(0.0,0.36,0.32,1.0),
8.0:(0.0,0.60,0.42,1.0),8.5:(0.0,0.74,0.36,1.0),9.0:(0.0,0.84,0.40,1.0)}
F={4.0:(0.55,0.62,1.0,1.0),4.5:(0.52,0.48,1.0,1.0),5.0:(0.46,0.44,1.0,1.0),5.5:(0.46,0.44,1.0,1.0),
6.0:(0.44,0.38,1.0,0.88),6.5:(0.46,0.36,1.0,0.90),7.0:(0.40,0.02,1.0,1.0),7.5:(0.33,0.0,1.0,1.0),
8.0:(0.43,0.05,1.0,1.0),8.5:(0.38,0.13,0.95,1.0),9.0:(0.42,0.42,0.90,1.0)}
c={"mediaId":4459,"level":"B","keyWord":"burning","defaultVoice":"female",
 "taps":[
  {"phrase":"to gasp in surprise","target":"the woman","voice":"female","k":"W"},
  {"phrase":"to hold wooden skewers","target":"the woman","voice":"female","k":"W"},
  {"phrase":"to send up sparks","target":"the fire","voice":"female","k":"F"}],
 "stillS":3.5,
 "nouns":[{"word":"the sky","x":0.60,"y":0.07,"voice":"female"},
          {"word":"a checked shirt","x":0.24,"y":0.58,"voice":"female"},
          {"word":"marshmallows","x":0.82,"y":0.66,"voice":"female"},
          {"word":"a fire pit","x":0.66,"y":0.90,"voice":"female"}],
 "question":"What is burning on the skewer?",
 "answer":["A","marshmallow","is","burning","on","the","skewer."],
 "answerVoice":"female",
 "notes":"Only two targets (woman twice, fire once): the marshmallows sit inside the flames from 4.5 s, a separate box for them could not be kept apart from the fire's box. 'The fire' = the fire in the pit, first really visible at 4.0 s (off before; only a glint at the frame edge at 1.5-3.5 s). The single marshmallow that burns at 0.5-1.5 s has its own flame and no box: a tap there counts for nothing. At 0-0.5 s only the woman's shoulder and hand are in the picture at the left edge. From 7.5 s she is small in the bottom-left corner. Dark figures sit in the background (not used). The question is about the first seconds (0.5-1.5 s), when one marshmallow burns."}
write(4459,c,{"W":W,"F":F})
