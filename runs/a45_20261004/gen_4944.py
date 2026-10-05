import json
T=[i*0.5 for i in range(19)]
K=[(0.02,0.20,0.96,0.80),(0.02,0.20,0.96,0.80),(0.02,0.20,0.96,0.80),(0.02,0.20,0.96,0.80),(0.02,0.18,0.96,0.82),None,
(0.02,0.10,0.96,0.90),(0.08,0.20,0.86,0.79),(0.10,0.22,0.78,0.70),(0.40,0.50,0.20,0.16),(0.38,0.50,0.21,0.18),(0.41,0.50,0.20,0.18),(0.38,0.50,0.20,0.16),None,
(0.18,0.23,0.67,0.77),(0.13,0.16,0.77,0.84),(0.10,0.15,0.82,0.85),(0.06,0.50,0.87,0.50),(0.04,0.48,0.92,0.52)]
keys=[{"t":t,"off":True} if k is None else {"t":t,"x":k[0],"y":k[1],"w":k[2],"h":k[3]} for t,k in zip(T,K)]
taps=[{"phrase":p,"target":"the woman","voice":"female","keys":keys} for p in ["to touch up her make-up","to twirl in a gown","to bow over the roses"]]
c={"mediaId":4944,"level":"B","keyWord":"gown","defaultVoice":"female","taps":taps,"stillS":8.0,
"nouns":[{"word":"a curtain","x":0.80,"y":0.10,"voice":"female"},{"word":"a bouquet","x":0.50,"y":0.57,"voice":"female"},{"word":"a gown","x":0.50,"y":0.88,"voice":"female"}],
"question":"What is the woman holding?","answer":["She","is","holding","a","bouquet","of","red","roses."],"answerVoice":"female",
"notes":"Only one person in the clip (a hand gives roses at 6.5 s, woman off then); all three phrases target the woman. 0-2 s she is seen mostly in the mirror plus her real shoulder at the right edge; box covers both. 2.5 s is a motion blur -> off."}
json.dump(c,open('content/4944.json','w'),indent=1)
