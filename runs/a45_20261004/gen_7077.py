from gen_7075_7076_7077_7079_w import write
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
D=[(0.60,0.33,0.40,0.37),(0.45,0.33,0.55,0.38),(0.45,0.33,0.55,0.38),(0.46,0.33,0.54,0.38),(0.46,0.31,0.54,0.40),(0.45,0.31,0.55,0.40),(0.57,0.31,0.43,0.42),(0.58,0.31,0.42,0.42)]
P=[(0.00,0.35,0.42,0.37),(0.00,0.35,0.42,0.37),(0.00,0.35,0.42,0.37),(0.00,0.35,0.45,0.37),(0.00,0.35,0.46,0.38),(0.00,0.35,0.45,0.38),(0.00,0.37,0.48,0.37),(0.00,0.37,0.48,0.37)]
C=[(0.37,0.75,0.24,0.17),(0.37,0.75,0.24,0.17),(0.37,0.76,0.24,0.18),(0.37,0.76,0.24,0.18),(0.37,0.77,0.24,0.19),(0.37,0.77,0.24,0.19),(0.37,0.79,0.24,0.20),(0.37,0.80,0.24,0.20)]
d={"mediaId":7077,"level":"B","keyWord":"elder","defaultVoice":"female",
"taps":[
 {"phrase":"to point at the dashboard","target":"the driver","voice":"female","boxes":D},
 {"phrase":"to raise her hand in protest","target":"the passenger","voice":"female","boxes":P},
 {"phrase":"to fill the cup holders","target":"the iced coffees","voice":"female","boxes":C}],
"stillS":0.2,
"nouns":[{"word":"a rear-view mirror","x":0.47,"y":0.32,"voice":"female"},
 {"word":"an air freshener","x":0.47,"y":0.41,"voice":"female"},
 {"word":"a steering wheel","x":0.68,"y":0.56,"voice":"female"},
 {"word":"iced coffees","x":0.49,"y":0.86,"voice":"female"}],
"question":"What is the driver doing?",
"answer":["She","is","pointing","at","the","dashboard."],
"answerVoice":"female",
"notes":"Right-hand-drive car: the driver (older woman, long dark hair) sits on the RIGHT, the passenger in the hoodie on the LEFT. Driver points at the centre console from 0.7 to 2.7 ('dashboard' = console area). Key word 'elder' not used as a noun (needs guessing). Boxes of driver and passenger split at x~0.45 where her pointing hand and the passenger's raised hand are close. The air freshener was not used as a tap target: its minimum box would overlap both women."}
write(d,T)
