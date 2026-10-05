import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) for t,r in zip(T,rows)]
cow=K([(0.00,0.21,0.46,0.33),(0.00,0.21,0.41,0.32),(0.00,0.21,0.40,0.33),(0.00,0.21,0.41,0.32),
       (0.00,0.21,0.43,0.33),(0.00,0.20,0.48,0.34),(0.00,0.23,0.47,0.31),(0.00,0.24,0.52,0.30)])
wom=K([(0.47,0.28,0.52,0.58),(0.42,0.29,0.54,0.53),(0.40,0.30,0.52,0.54),(0.41,0.29,0.53,0.55),
       (0.43,0.30,0.47,0.56),(0.49,0.34,0.47,0.52),(0.47,0.35,0.44,0.52),(0.52,0.36,0.42,0.50)])
d={"mediaId":7304,"level":"B","keyWord":"look away","defaultVoice":"female",
 "taps":[
  {"phrase":"to screw up her eyes","target":"the woman","voice":"female","keys":wom},
  {"phrase":"to stick out its tongue","target":"the cow","voice":"female","keys":cow},
  {"phrase":"to lean over the stable door","target":"the cow","voice":"female","keys":cow}],
 "stillS":0.2,
 "nouns":[{"word":"a cow","x":0.15,"y":0.35,"voice":"female"},
  {"word":"a stable door","x":0.40,"y":0.15,"voice":"female"},
  {"word":"a jumper","x":0.70,"y":0.62,"voice":"female"},
  {"word":"oats","x":0.45,"y":0.89,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","looking","away","from","the","cow's","tongue."],
 "answerVoice":"female",
 "notes":"Cow and woman touch (tongue near her raised hand): boxes split vertically between snout and hand; the woman's left arm reaching across the table lies outside her box. Cow sticks out its tongue from about 1.7 s on. 'to lean over the stable door': the cow's head hangs over the lower half of the door."}
json.dump(d,open('content/7304.json','w'),indent=1)
