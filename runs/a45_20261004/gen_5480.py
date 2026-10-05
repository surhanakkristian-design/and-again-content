import json
T=[i*0.5 for i in range(25)]
def mk(d):
    return [{"t":t,"off":True} if d.get(t) is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) for t in T]
man={0.0:(0.39,0.05,0.61,0.79),0.5:(0.39,0.05,0.61,0.8),1.0:(0.39,0.06,0.61,0.78),1.5:(0.39,0.04,0.61,0.8),
 2.0:(0.33,0.06,0.67,0.84),2.5:(0.26,0.04,0.74,0.63),3.0:(0.27,0.06,0.73,0.8),3.5:(0.39,0.04,0.61,0.84),
 4.0:(0.4,0.03,0.6,0.8),4.5:(0.4,0.04,0.6,0.78),5.0:(0.4,0.05,0.6,0.8),5.5:(0.4,0.04,0.6,0.82),6.0:(0.42,0.05,0.58,0.75),
 6.5:(0.4,0.04,0.6,0.76),7.0:(0.4,0.04,0.6,0.8),7.5:(0.4,0.07,0.6,0.84),8.0:(0.4,0.07,0.6,0.75),8.5:(0.42,0.04,0.58,0.73),
 9.0:(0.42,0.05,0.58,0.9),9.5:(0.41,0.05,0.59,0.82),10.0:(0.3,0.07,0.7,0.64),10.5:(0.3,0.07,0.7,0.68),
 11.0:(0.47,0.05,0.53,0.86),11.5:(0.42,0.04,0.58,0.9),12.0:(0.43,0.06,0.57,0.88)}
water={0.0:(0.21,0.66,0.18,0.2),0.5:(0.21,0.66,0.18,0.2),1.0:(0.21,0.66,0.18,0.2),1.5:(0.21,0.66,0.18,0.2),
 2.5:(0.26,0.67,0.18,0.27),3.5:(0.2,0.68,0.19,0.3),4.0:(0.21,0.66,0.19,0.2),4.5:(0.21,0.68,0.19,0.22),5.0:(0.21,0.67,0.19,0.2),
 5.5:(0.21,0.67,0.19,0.2),6.0:(0.24,0.68,0.18,0.2),6.5:(0.21,0.62,0.19,0.16),7.0:(0.21,0.68,0.19,0.3),7.5:(0.21,0.69,0.19,0.31),
 8.0:(0.21,0.66,0.19,0.2),8.5:(0.24,0.68,0.18,0.3),9.0:(0.24,0.7,0.18,0.2),9.5:(0.22,0.7,0.19,0.28),10.0:(0.29,0.71,0.18,0.24)}
c={"mediaId":5480,"level":"A","keyWord":"task","defaultVoice":"male",
 "taps":[{"phrase":"to wash a plate","target":"the man","voice":"male","keys":mk(man)},
  {"phrase":"to wear a cap","target":"the man","voice":"male","keys":mk(man)},
  {"phrase":"to run into the sink","target":"the water","voice":"male","keys":mk(water)}],
 "stillS":12.0,
 "nouns":[{"word":"a cap","x":0.68,"y":0.1,"voice":"male"},{"word":"glasses","x":0.15,"y":0.41,"voice":"male"},
  {"word":"plates","x":0.15,"y":0.6,"voice":"male"},{"word":"a towel","x":0.65,"y":0.88,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","washing","a","plate."],"answerVoice":"male",
 "notes":"Only one person, so two phrases share the man; 'to wear a cap' is a state (no second action fits only him without sound). Water stream is thin and runs right next to his hands: water box kept left of x~0.40, man box starts there, so his hand under the tap sometimes falls in the water box (3.5, 4.0, 7.5). Water OFF at 2.0, 3.0 (hidden by plate/hands) and from 10.5 (tap off/out of view). Key word 'task' is not a visible noun."}
json.dump(c,open('content/5480.json','w'),indent=1)
