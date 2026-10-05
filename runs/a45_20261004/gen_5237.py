import json
T=[i*0.5 for i in range(9)]
M={0.0:(0.34,0.27,0.32,0.37),0.5:(0.32,0.27,0.3,0.36),1.0:(0.33,0.28,0.28,0.39),1.5:(0.0,0.47,0.7,0.53),2.0:(0.0,0.47,0.62,0.53),
   2.5:(0.2,0.26,0.43,0.47),3.0:(0.2,0.26,0.39,0.47),3.5:(0.15,0.25,0.65,0.49),4.0:(0.12,0.25,0.68,0.49)}
P={2.5:(0.64,0.4,0.36,0.24),3.0:(0.6,0.38,0.4,0.25)}
F={2.5:(0.28,0.74,0.72,0.26),3.0:(0.2,0.75,0.8,0.25),3.5:(0.2,0.76,0.8,0.24),4.0:(0.25,0.75,0.75,0.25)}
def keys(m):
    return [({"t":t,"off":True} if t not in m else dict(t=t,x=m[t][0],y=m[t][1],w=m[t][2],h=m[t][3])) for t in T]
c={"mediaId":5237,"level":"A","keyWord":"star","defaultVoice":"male",
 "taps":[
  {"phrase":"to touch the old wall","target":"the man","voice":"male","keys":keys(M)},
  {"phrase":"to pour hot tea","target":"the teapot","voice":"male","keys":keys(P)},
  {"phrase":"to burn in the dark","target":"the fire","voice":"male","keys":keys(F)}],
 "stillS":3.5,
 "nouns":[{"word":"stars","x":0.5,"y":0.15,"voice":"male"},
          {"word":"a cup","x":0.44,"y":0.42,"voice":"male"},
          {"word":"a man","x":0.6,"y":0.6,"voice":"male"},
          {"word":"a fire","x":0.62,"y":0.9,"voice":"male"}],
 "question":"What is the man holding?",
 "answer":["He","is","holding","a","small","cup","of","tea."],
 "answerVoice":"male",
 "notes":"Three shots: dune run 0.0-1.0, carved wall 1.5-2.0, campfire under the stars 2.5-4.0. Teapot only at 2.5-3.0 (held by someone off-screen, only a hand visible); teapot box split from the man box at x ~0.6, so the man's right shoulder/arm (x 0.6-0.75) is outside his box there. Man box ends at y ~0.73 above the fire box. The man touches the wall only at 1.5-2.0 but his box follows him in every shot."}
json.dump(c,open('content/5237.json','w'),indent=1)
