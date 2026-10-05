import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
TOP={0.2:(0.17,0.12,0.54,0.33),0.7:(0.17,0.10,0.60,0.35),1.2:(0.10,0.07,0.74,0.38),1.7:(0.10,0.04,0.76,0.41),
     2.2:(0.12,0.01,0.72,0.46),2.7:(0.17,0.01,0.64,0.47),3.2:(0.25,0.02,0.50,0.47),3.7:(0.32,0.05,0.38,0.44)}
LEFT={0.2:(0.10,0.45,0.42,0.34),0.7:(0.10,0.45,0.42,0.34),1.2:(0.10,0.45,0.42,0.34),1.7:(0.10,0.45,0.42,0.34),
     2.2:(0.17,0.47,0.36,0.33),2.7:(0.18,0.48,0.35,0.33),3.2:(0.18,0.49,0.35,0.33),3.7:(0.19,0.49,0.35,0.33)}
RIGHT={0.2:(0.52,0.45,0.40,0.34),0.7:(0.52,0.45,0.40,0.34),1.2:(0.52,0.45,0.40,0.34),1.7:(0.52,0.45,0.40,0.34),
     2.2:(0.53,0.47,0.38,0.34),2.7:(0.53,0.48,0.40,0.34),3.2:(0.53,0.49,0.38,0.34),3.7:(0.54,0.49,0.38,0.34)}
keys=lambda D:[dict(t=t,**dict(zip("xywh",D[t]))) for t in T]
d={"mediaId":5605,"level":"A","keyWord":"basic","defaultVoice":"female",
"taps":[
 {"phrase":"to stand on their backs","target":"the woman on top","voice":"female","keys":keys(TOP)},
 {"phrase":"to wear a yellow swimsuit","target":"the woman in yellow","voice":"female","keys":keys(LEFT)},
 {"phrase":"to have blonde hair","target":"the woman in green","voice":"female","keys":keys(RIGHT)}],
"stillS":2.7,
"nouns":[{"word":"an umbrella","x":0.20,"y":0.41,"voice":"female"},
 {"word":"a net","x":0.80,"y":0.45,"voice":"female"},
 {"word":"a towel","x":0.88,"y":0.67,"voice":"female"},
 {"word":"sand","x":0.50,"y":0.88,"voice":"female"}],
"question":"What is the woman on top doing?",
"answer":["She","is","standing","on","their","backs."],
"answerVoice":"female",
"notes":"Three women overlap: top woman's box ends where the kneeling women's heads start (her lower legs excluded); kneeling pair split at x~0.52-0.54. Two phrases are states (yellow swimsuit, blonde hair) because both kneeling women do the same things (kneel, laugh). Is 'to have blonde hair' acceptable as a phrase?"}
json.dump(d,open("content/5605.json","w"),indent=1)
