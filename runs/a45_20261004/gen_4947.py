import json
T=[i*0.5 for i in range(19)]
H=[(0.15,0,0.85,0.47),(0.15,0,0.85,0.45),(0.18,0,0.82,0.45)]+[None]*16
W=[None,None,None,(0.52,0.20,0.48,0.80),(0.22,0.21,0.78,0.79),(0.35,0.21,0.65,0.79),(0.33,0.22,0.67,0.78),(0.35,0.20,0.65,0.80),
(0.62,0.21,0.38,0.79),(0.66,0.22,0.34,0.78),(0.60,0.20,0.40,0.80),(0.60,0.23,0.40,0.77),(0.40,0.27,0.60,0.73),(0.03,0.24,0.97,0.76),
(0.66,0.26,0.34,0.74),None,(0.77,0.22,0.23,0.78),(0.71,0.07,0.29,0.93),(0.69,0.08,0.31,0.92)]
P=[None]*15+[(0,0.08,0.97,0.74),(0,0.16,0.76,0.63),(0,0.19,0.70,0.55),(0,0.19,0.68,0.50)]
def ks(L): return [{"t":t,"off":True} if k is None else {"t":t,"x":k[0],"y":k[1],"w":k[2],"h":k[3]} for t,k in zip(T,L)]
taps=[{"phrase":"to squeeze a paint tube","target":"the hands","voice":"female","keys":ks(H)},
{"phrase":"to dab at the canvas","target":"the woman","voice":"female","keys":ks(W)},
{"phrase":"to have bright green eyes","target":"the portrait","voice":"female","keys":ks(P)}]
c={"mediaId":4947,"level":"B","keyWord":"portrait","defaultVoice":"female","taps":taps,"stillS":8.5,
"nouns":[{"word":"a portrait","x":0.32,"y":0.30,"voice":"female"},{"word":"dungarees","x":0.85,"y":0.62,"voice":"female"},{"word":"brushes","x":0.18,"y":0.84,"voice":"female"},{"word":"a palette","x":0.70,"y":0.87,"voice":"female"}],
"question":"What is the woman painting?","answer":["She","is","painting","a","colourful","portrait."],"answerVoice":"female",
"notes":"'the hands' (0-1 s, squeezing the tube) are probably the artist's, shown before she appears; woman off then. Portrait target only once finished and seen from the front (7.5-9.0 s); woman off at 7.5 s (hidden behind the canvas, only an edge visible). At 8.5/9.0 s her raised arm crosses above the canvas corner; boxes split at x 0.70."}
json.dump(c,open('content/4947.json','w'),indent=1)
