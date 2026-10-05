import json
T=[i*0.5 for i in range(19)]
def K(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
W={0.0:(0,0.21,1,0.79),0.5:(0,0.22,1,0.78),1.0:(0,0.18,1,0.82),1.5:(0,0.24,1,0.76),2.0:(0,0,1,1),
   7.0:(0.57,0.26,0.39,0.74),7.5:(0.6,0.15,0.4,0.85),8.0:(0.82,0.27,0.18,0.73),8.5:(0.75,0.18,0.25,0.65),9.0:(0.43,0.12,0.52,0.82)}
M={2.5:(0.08,0.32,0.74,0.66),3.0:(0.1,0.21,0.72,0.79),3.5:(0.27,0.14,0.56,0.86),6.0:(0.01,0.34,0.3,0.48),
   7.5:(0.34,0.37,0.18,0.42),8.0:(0.45,0.35,0.21,0.36),8.5:(0.41,0.3,0.19,0.36)}
H={4.0:(0.05,0.26,0.92,0.49),4.5:(0.1,0.25,0.9,0.52),5.0:(0.01,0.24,0.99,0.55),5.5:(0.73,0,0.27,1),6.0:(0.73,0.14,0.27,0.86),
   6.5:(0.27,0.19,0.6,0.81),7.0:(0,0.24,0.46,0.76),7.5:(0,0.17,0.33,0.83),8.0:(0,0.26,0.44,0.74),8.5:(0,0.19,0.4,0.81),9.0:(0,0.19,0.4,0.81)}
c={"mediaId":5200,"level":"A","keyWord":"lively","defaultVoice":"female",
 "taps":[
  {"phrase":"to sit under a blanket","target":"the woman in the striped sweater","voice":"female","keys":K(W)},
  {"phrase":"to jump out of a chair","target":"the man in the T-shirt","voice":"male","keys":K(M)},
  {"phrase":"to do push-ups","target":"the man in the hoodie","voice":"male","keys":K(H)}],
 "stillS":2.5,
 "nouns":[{"word":"a plant","x":0.55,"y":0.22,"voice":"female"},{"word":"a door","x":0.15,"y":0.35,"voice":"female"},
          {"word":"a chair","x":0.17,"y":0.66,"voice":"female"},{"word":"a cup","x":0.37,"y":0.92,"voice":"female"}],
 "question":"What are the young people doing?",
 "answer":["They","are","giving","high","fives."],
 "answerVoice":"female",
 "notes":"Multi-shot clip. Striped-sweater woman marked off at 5.5-6.5 (uncertain/blurred in the group shot). T-shirt man off at 5.5 (unclear which person) and 6.5 (hidden behind hoodie man), 7.0 and 9.0. Key word 'lively' is an adjective, not used as a noun."}
json.dump(c,open('content/5200.json','w'),indent=1)
