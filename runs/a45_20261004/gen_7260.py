import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
wo=[(0.10,0.22,0.59,0.68),(0.10,0.22,0.60,0.68),(0.09,0.20,0.61,0.72),(0.09,0.20,0.62,0.72),(0.08,0.18,0.66,0.74),(0.08,0.18,0.68,0.74),(0.13,0.17,0.64,0.77),(0.08,0.16,0.69,0.77)]
ba=[(0.70,0.20,0.30,0.50),(0.71,0.20,0.29,0.50),(0.71,0.20,0.29,0.50),(0.72,0.20,0.28,0.50),(0.75,0.22,0.25,0.48),(0.77,0.22,0.23,0.48),(0.78,0.24,0.22,0.46),(0.79,0.24,0.21,0.46)]
dr=[(0.74,0.70,0.26,0.29),(0.74,0.70,0.26,0.29),(0.74,0.70,0.26,0.29),(0.74,0.70,0.26,0.29),(0.76,0.70,0.24,0.29),(0.77,0.70,0.23,0.29),(0.78,0.70,0.22,0.29),(0.79,0.70,0.21,0.29)]
k=lambda b:[{"t":t,"x":x,"y":y,"w":w,"h":h} for t,(x,y,w,h) in zip(T,b)]
d={"mediaId":7260,"level":"B","keyWord":"jazz","defaultVoice":"female",
"taps":[{"phrase":"to lower her brass trumpet","target":"the woman","voice":"female","keys":k(wo)},
{"phrase":"to pluck a double bass","target":"the bass player","voice":"male","keys":k(ba)},
{"phrase":"to brush a snare drum","target":"the drummer","voice":"male","keys":k(dr)}],
"stillS":1.7,
"nouns":[{"word":"a trumpet","x":0.30,"y":0.36,"voice":"female"},{"word":"a music stand","x":0.18,"y":0.55,"voice":"female"},
{"word":"a double bass","x":0.86,"y":0.62,"voice":"female"},{"word":"a snare drum","x":0.62,"y":0.83,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","playing","a","brass","trumpet","under","a","spotlight."],"answerVoice":"female",
"notes":"Drummer is only partly visible (hands, arm, knee at the right edge); his box is the lower right corner below the bass player's box. The woman lowers the trumpet only at 3.2 s. Her bun overlaps the bass player's box line at 2.2-3.7 s; split at the shirt edge."}
json.dump(d,open("content/7260.json","w"),indent=1)
