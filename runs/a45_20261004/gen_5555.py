import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
wom=[(0.32,0.25,0.53,0.75),(0.37,0.29,0.48,0.71),(0.36,0.30,0.46,0.70),(0.35,0.31,0.44,0.68),(0.31,0.32,0.40,0.61),(0.29,0.33,0.39,0.57),(0.28,0.34,0.36,0.55),(0.28,0.35,0.35,0.54)]
man=[None,None,None,(0.82,0.39,0.18,0.30),(0.76,0.37,0.24,0.39),(0.69,0.37,0.31,0.40),(0.65,0.38,0.27,0.38),(0.64,0.39,0.26,0.37)]
def k(L):
  out=[]
  for t,b in zip(T,L):
    out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
  return out
c={"mediaId":5555,"level":"B","keyWord":"anxiety","defaultVoice":"female",
"taps":[
 {"phrase":"to clutch a clothes iron","target":"the woman","voice":"female","keys":k(wom)},
 {"phrase":"to glance back nervously","target":"the woman","voice":"female","keys":k(wom)},
 {"phrase":"to scratch his head","target":"the man","voice":"male","keys":k(man)}],
"stillS":1.2,
"nouns":[{"word":"a front door","x":0.12,"y":0.40,"voice":"female"},
 {"word":"flowers","x":0.78,"y":0.18,"voice":"female"},
 {"word":"a backpack","x":0.73,"y":0.55,"voice":"female"},
 {"word":"a potted plant","x":0.36,"y":0.72,"voice":"female"}],
"question":"What is the woman holding?",
"answer":["She","is","clutching","a","clothes","iron."],
"answerVoice":"female",
"notes":"Man enters only at 1.7 s (partly, right edge) and has his hand on his head at 2.2-2.7 s, then looks at his watch; off before 1.7 s. Woman also holds a silver box-shaped object with the iron. She glances back at the house at 2.7-3.2 s."}
json.dump(c,open("content/5555.json","w"),indent=1)
