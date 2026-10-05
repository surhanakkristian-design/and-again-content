import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) for t,r in zip(T,rows)]
man=K([(0.00,0.00,0.64,0.54),(0.06,0.00,0.58,0.56),(0.00,0.00,0.64,0.67),(0.00,0.00,0.64,0.76),
       (0.09,0.10,0.52,0.74),(0.14,0.21,0.48,0.64),(0.18,0.28,0.43,0.57),(0.20,0.31,0.41,0.54)])
wom=K([(0.75,0.00,0.25,0.54),(0.73,0.00,0.27,0.56),(0.70,0.00,0.30,0.66),(0.66,0.02,0.34,0.74),
       (0.63,0.18,0.33,0.66),(0.63,0.28,0.30,0.57),(0.62,0.34,0.28,0.51),(0.62,0.36,0.27,0.49)])
pan=K([(0.31,0.55,0.69,0.23),(0.32,0.57,0.68,0.23),(0.36,0.68,0.55,0.18),(0.39,0.77,0.43,0.15),
       (0.40,0.85,0.36,0.14),(0.40,0.86,0.33,0.14),(0.40,0.86,0.30,0.14),(0.40,0.86,0.32,0.14)])
d={"mediaId":7283,"level":"B","keyWord":"landlord","defaultVoice":"male",
 "taps":[{"phrase":"to scratch his neck","target":"the man","voice":"male","keys":man},
         {"phrase":"to fold her arms","target":"the woman","voice":"female","keys":wom},
         {"phrase":"to catch the dripping water","target":"the saucepan","voice":"male","keys":pan}],
 "stillS":3.7,
 "nouns":[{"word":"a water stain","x":0.42,"y":0.11,"voice":"male"},
          {"word":"a calendar","x":0.86,"y":0.40,"voice":"male"},
          {"word":"a landlord","x":0.40,"y":0.52,"voice":"male"},
          {"word":"a saucepan","x":0.56,"y":0.93,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","wincing","at","the","water","stain."],
 "answerVoice":"male",
 "notes":"Camera tilts up from the feet: 0.2-1.2 s only legs show (boxes on legs/torso). He scratches his neck and winces at the stain only from 2.2 s. 'a landlord' is inferred from the keys and clipboard, not shown explicitly. Man/woman boxes cut at the top of the saucepan box where their shoes reach down beside the pan."}
json.dump(d,open("content/7283.json","w"),indent=1)
