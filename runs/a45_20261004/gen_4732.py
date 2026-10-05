import json
T=[i*0.5 for i in range(25)]
def keys(d):
    return [{"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in T]
M={0.0:(0,0.03,0.90,0.97),0.5:(0,0.09,0.78,0.91),1.0:(0,0.10,0.58,0.90),1.5:(0,0.06,1.0,0.94),
2.0:(0,0.04,1.0,0.96),2.5:(0,0.06,0.95,0.94),3.0:(0,0.07,0.93,0.93),3.5:(0,0.06,0.93,0.94),4.0:(0,0.05,0.93,0.95),
4.5:(0,0.18,0.42,0.80),5.0:(0,0.19,0.38,0.81),5.5:(0,0.21,0.38,0.74),6.0:(0,0.14,0.38,0.82),6.5:(0,0.23,0.38,0.73),
7.0:(0,0.20,0.20,0.78),7.5:(0,0.20,0.38,0.78),8.0:(0,0.20,0.36,0.76),8.5:(0,0.20,0.28,0.78),9.0:(0,0.21,0.18,0.77),
9.5:(0.62,0.34,0.20,0.14),10.0:(0.68,0.33,0.20,0.14),10.5:(0.67,0.32,0.22,0.14),11.0:(0.58,0.33,0.24,0.14),
11.5:(0.50,0.33,0.31,0.14),12.0:(0.49,0.32,0.30,0.14)}
k=keys(M)
d={"mediaId":4732,"level":"A","keyWord":"build","defaultVoice":"male",
"taps":[
 {"phrase":"to build a wooden fence","target":"the man","voice":"male","keys":k},
 {"phrase":"to use a yellow hammer","target":"the man","voice":"male","keys":k},
 {"phrase":"to look over the fence","target":"the man","voice":"male","keys":k}],
"stillS":12.0,
"nouns":[{"word":"the sky","x":0.70,"y":0.10,"voice":"male"},{"word":"a tree","x":0.22,"y":0.20,"voice":"male"},
 {"word":"a fence","x":0.55,"y":0.52,"voice":"male"},{"word":"grass","x":0.30,"y":0.85,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","building","a","wooden","fence."],
"answerVoice":"male",
"notes":"Only one living target (the man), so all three phrases use him with the same keys. He uses the yellow rubber mallet at 5.5-6.5 s ('hammer' for level A) and looks over the finished fence at 10-12 s. In the close shots (0-4 s) his box covers nearly the whole picture, including the post he holds; at 7.0 and 9.0 s only a strip of him is left at the left edge; from 9.5 s he is a small figure behind the fence (minimum-size box). Still 12.0 s: 'a tree' is the big tree on the left (smaller trees stand far right); the man is too small there for a noun of his own."}
json.dump(d,open("content/4732.json","w"),ensure_ascii=False,indent=1)
