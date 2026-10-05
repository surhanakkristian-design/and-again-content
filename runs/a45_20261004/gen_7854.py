import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes):
    return [{"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,boxes)]
wom=K([(0.20,0.19,0.42,0.58),(0.49,0.28,0.45,0.54),(0.66,0.21,0.34,0.56),(0.71,0.24,0.29,0.64),
       (0.67,0.22,0.33,0.63),(0.64,0.22,0.34,0.65),(0.63,0.25,0.37,0.61),(0.69,0.23,0.31,0.63)])
man=K([(0.62,0.32,0.18,0.30),None,(0.52,0.38,0.14,0.28),(0.49,0.32,0.21,0.34),(0.47,0.33,0.20,0.33),
       (0.45,0.33,0.19,0.33),(0.44,0.34,0.19,0.32),(0.43,0.35,0.20,0.31)])
bird=K([None,None,None,(0.80,0.06,0.20,0.17),(0.72,0.08,0.20,0.14),(0.66,0.09,0.22,0.13),(0.68,0.11,0.19,0.14),None])
d={"mediaId":7854,"level":"B","keyWord":"growing","defaultVoice":"female",
"taps":[{"phrase":"to leap over a pumpkin","target":"the young woman","voice":"female","keys":wom},
{"phrase":"to wear denim dungarees","target":"the young man","voice":"male","keys":man},
{"phrase":"to perch on a leaf","target":"the bird","voice":"female","keys":bird}],
"stillS":2.7,
"nouns":[{"word":"a sunflower","x":0.76,"y":0.07,"voice":"female"},{"word":"tomatoes","x":0.88,"y":0.62,"voice":"female"},
{"word":"a pumpkin","x":0.39,"y":0.67,"voice":"female"},{"word":"a puddle","x":0.36,"y":0.80,"voice":"female"}],
"question":"What is the woman jumping over?",
"answer":["She","is","leaping","over","a","huge","pumpkin."],
"answerVoice":"female",
"notes":"'growing' is an adjective, not a placeable noun. The leap is only in the first ~0.7 s (she lands past the pumpkin). Man is behind the woman at 0.2 s and hidden at 0.7 s; at 0.2/1.2 s his box is cut to avoid her arms. Bird flies in at 1.2 s (off: in flight, overlaps her box) and is gone/leaving at 3.7 s. Man phrase is a state (no clear action of his own)."}
json.dump(d,open("content/7854.json","w"),indent=1)
