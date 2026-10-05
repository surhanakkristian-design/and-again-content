import json
T=[i*0.5 for i in range(25)]
def K(d): return [{"t":t,"off":True} if d.get(t) is None else dict(t=t,**dict(zip("xywh",d[t]))) for t in T]
W={0.0:(0,0.19,0.71,0.81),0.5:(0,0.21,0.7,0.79),1.0:(0,0.24,0.18,0.76),2.0:(0,0.14,0.18,0.86),2.5:(0,0.19,0.47,0.81),3.0:(0,0.2,0.5,0.8),3.5:(0,0.2,0.5,0.8),
   9.0:(0.06,0.22,0.6,0.78),9.5:(0.07,0.22,0.56,0.78),10.0:(0.02,0.21,0.7,0.79),10.5:(0.01,0.24,0.46,0.76),11.0:(0,0.26,0.36,0.74),11.5:(0,0.26,0.38,0.74),12.0:(0,0.26,0.37,0.66)}
H={4.0:(0,0.4,0.39,0.42),4.5:(0,0.39,0.73,0.61),5.0:(0,0.42,0.7,0.58),5.5:(0,0.46,0.69,0.54),6.0:(0,0.39,0.71,0.28),6.5:(0,0.37,0.72,0.55),
   7.0:(0,0.29,0.5,0.71),7.5:(0,0.5,0.54,0.5),8.0:(0,0.4,0.74,0.56),8.5:(0,0.41,0.92,0.59)}
c={"mediaId":5202,"level":"A","keyWord":"put","defaultVoice":"female",
 "taps":[
  {"phrase":"to open the fridge","target":"the woman","voice":"female","keys":K(W)},
  {"phrase":"to smile at the camera","target":"the woman","voice":"female","keys":K(W)},
  {"phrase":"to put food on shelves","target":"the hand","voice":"female","keys":K(H)}],
 "stillS":12.0,
 "nouns":[{"word":"a woman","x":0.2,"y":0.45,"voice":"female"},{"word":"milk","x":0.38,"y":0.6,"voice":"female"},
          {"word":"juice","x":0.86,"y":0.67,"voice":"female"},{"word":"a fridge","x":0.62,"y":0.82,"voice":"female"}],
 "question":"What is the woman opening?",
 "answer":["She","is","opening","the","fridge."],
 "answerVoice":"female",
 "notes":"Woman visible only in the wide shots (0-3.5, 9-12; off at 1.5 where only a sliver shows); the hand (only arm/hand visible) is the target in the close-ups 4-8.5 and off in the wide shots so it never overlaps the woman. 'the hand' is presumably hers, but the woman as a whole is never visible while food is put in. Smile at the camera: 2.5-3.5 and 9.0."}
json.dump(c,open('content/5202.json','w'),indent=1)
