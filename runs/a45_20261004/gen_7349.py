import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def k(t,b): return {"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}
M={0.2:(0.53,0.34,0.32,0.53),0.7:(0.53,0.34,0.30,0.52),1.2:(0.51,0.35,0.31,0.57),1.7:(0.50,0.37,0.35,0.56),
   2.2:(0.45,0.34,0.42,0.64),2.7:(0.43,0.35,0.40,0.65),3.2:(0.34,0.34,0.46,0.66),3.7:(0.25,0.35,0.47,0.65)}
D={0.2:(0.29,0.37,0.23,0.37),0.7:(0.30,0.37,0.22,0.39),1.2:(0.30,0.36,0.21,0.39),1.7:(0.32,0.36,0.18,0.40),
   2.2:None,2.7:None,3.2:None,3.7:(0.72,0.36,0.20,0.45)}
c={"mediaId":7349,"level":"B","keyWord":"a millionaire","defaultVoice":"male",
 "taps":[
  {"phrase":"to stride across a white towel","target":"the man","voice":"male","keys":[k(t,M[t]) for t in T]},
  {"phrase":"to carry a dachshund","target":"the woman with the dog","voice":"female","keys":[k(t,D[t]) for t in T]},
  {"phrase":"to wear heavy gold chains","target":"the man","voice":"male","keys":[k(t,M[t]) for t in T]}],
 "stillS":0.7,
 "nouns":[{"word":"a villa","x":0.72,"y":0.15,"voice":"male"},
          {"word":"a dachshund","x":0.40,"y":0.50,"voice":"male"},
          {"word":"a millionaire","x":0.70,"y":0.62,"voice":"male"},
          {"word":"a towel","x":0.35,"y":0.75,"voice":"male"}],
 "question":"What is the millionaire doing?",
 "answer":["He","is","striding","across","a","white","towel."],
 "answerVoice":"male",
 "notes":"Single shot, camera tracks back. The man steps off the towel early (0.2-0.7). The woman with the dog walks behind the man from 2.2 to 3.2 (off; at 3.2 she may be the half-hidden woman right of him, dog not visible) and reappears to his right at 3.7 holding the dachshund; her box at 3.7 is cut at x 0.72 next to the man's hand. Two phrases share the man (the other women all do the same thing). 'a millionaire' pill on the man is the key word, an interpretation of the rich look."}
json.dump(c,open('content/7349.json','w'),indent=1)
