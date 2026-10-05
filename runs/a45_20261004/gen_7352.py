import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def k(t,b): return {"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}
M={0.2:(0.38,0.28,0.52,0.64),0.7:(0.45,0.26,0.37,0.65),1.2:(0.41,0.27,0.51,0.65),1.7:(0.36,0.28,0.48,0.64),
   2.2:(0.41,0.28,0.41,0.64),2.7:(0.37,0.26,0.48,0.64),3.2:(0.31,0.27,0.50,0.63),3.7:(0.26,0.26,0.51,0.64)}
W={0.2:(0.90,0.43,0.10,0.19),0.7:(0.82,0.42,0.18,0.17),1.2:(0.92,0.42,0.08,0.18),1.7:(0.84,0.43,0.16,0.17),
   2.2:(0.82,0.42,0.18,0.18),2.7:(0.85,0.42,0.15,0.17),3.2:(0.81,0.41,0.18,0.17),3.7:(0.79,0.41,0.19,0.17)}
c={"mediaId":7352,"level":"B","keyWord":"a mini","defaultVoice":"female",
 "taps":[
  {"phrase":"to stride down a wet runway","target":"the model","voice":"female","keys":[k(t,M[t]) for t in T]},
  {"phrase":"to wear a high-visibility jacket","target":"the worker","voice":"male","keys":[k(t,W[t]) for t in T]},
  {"phrase":"to wear an orange miniskirt","target":"the model","voice":"female","keys":[k(t,M[t]) for t in T]}],
 "stillS":2.2,
 "nouns":[{"word":"floodlights","x":0.88,"y":0.32,"voice":"female"},
          {"word":"a plane","x":0.20,"y":0.40,"voice":"female"},
          {"word":"a mini","x":0.56,"y":0.57,"voice":"female"},
          {"word":"guests","x":0.15,"y":0.60,"voice":"female"}],
 "question":"What is the model doing?",
 "answer":["She","is","striding","down","a","wet","runway."],
 "answerVoice":"female",
 "notes":"Single shot. The worker in the yellow high-vis jacket is small and at the right edge (half cut off at 0.2-1.2); his box is narrow at 0.2 and 1.2 because the model's swinging coat reaches x 0.90-0.96 there (split along the line). The model's coat tip is cut at 2.7. Two phrases share the model; the second uses 'miniskirt' to carry the key word 'mini' (noun pill 'a mini' on the orange skirt). 'runway' here = catwalk on an airport apron. 'guests' pill on the seated audience at the left."}
json.dump(c,open('content/7352.json','w'),indent=1)
