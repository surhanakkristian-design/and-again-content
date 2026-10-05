import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) for t,r in zip(T,rows)]
man=K([(0.00,0.22,0.56,0.78),(0.02,0.20,0.58,0.80),(0.00,0.22,0.58,0.78),(0.00,0.22,0.56,0.78),
       (0.02,0.26,0.56,0.74),(0.08,0.29,0.48,0.70),(0.07,0.33,0.44,0.62),(0.10,0.32,0.37,0.58)])
wom=K([(0.56,0.37,0.44,0.63),(0.60,0.37,0.40,0.63),(0.58,0.36,0.41,0.64),(0.56,0.35,0.42,0.65),
       (0.58,0.38,0.33,0.60),(0.57,0.39,0.29,0.58),(0.51,0.38,0.27,0.58),(0.47,0.38,0.24,0.56)])
d={"mediaId":7308,"level":"B","keyWord":"love","defaultVoice":"female",
 "taps":[
  {"phrase":"to shield her from the rain","target":"the man in the white T-shirt","voice":"male","keys":man},
  {"phrase":"to clutch a paper bag","target":"the woman in the camel coat","voice":"female","keys":wom},
  {"phrase":"to touch her wet hair","target":"the woman in the camel coat","voice":"female","keys":wom}],
 "stillS":3.2,
 "nouns":[{"word":"an awning","x":0.50,"y":0.15,"voice":"female"},
  {"word":"a phone box","x":0.78,"y":0.37,"voice":"female"},
  {"word":"a paper bag","x":0.55,"y":0.54,"voice":"female"},
  {"word":"a bicycle","x":0.90,"y":0.62,"voice":"female"}],
 "question":"What is the man in white doing?",
 "answer":["He","is","shielding","her","from","the","rain."],
 "answerVoice":"male",
 "notes":"Man and woman stand shoulder to shoulder under one jacket: boxes split vertically between them; the jacket part over the woman lies in her box. She touches her hair at about 1.7 s and 3.7 s. defaultVoice female = mixed couple, evenId true. Key word 'love' is abstract, not placed."}
json.dump(d,open('content/7308.json','w'),indent=1)
