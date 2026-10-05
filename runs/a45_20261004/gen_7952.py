import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes):
    return [{"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,boxes)]
mx=[0.40,0.40,0.40,0.40,0.39,0.38,0.37,0.35]; mt=[0.44,0.44,0.44,0.43,0.43,0.42,0.42,0.42]
M=K([(x,y,round(1-x,2),round(1-y,2)) for x,y in zip(mx,mt)])
wl=[0.09,0.09,0.08,0.08,0.05,0.03,0.02,0.01]; wt=[0.27,0.27,0.26,0.25,0.24,0.24,0.24,0.23]; wb=[0.80,0.81,0.81,0.81,0.83,0.83,0.85,0.85]
Wm=K([(l,t,round(r-l,2),round(b-t,2)) for l,t,r,b in zip(wl,wt,mx,wb)])
c={"mediaId":7952,"level":"B","keyWord":"psychology","defaultVoice":"male",
 "taps":[{"phrase":"to gesture with both hands","target":"the man","voice":"male","keys":M},
  {"phrase":"to listen attentively","target":"the woman","voice":"female","keys":Wm},
  {"phrase":"to recline on a sofa","target":"the man","voice":"male","keys":M}],
 "stillS":2.2,
 "nouns":[{"word":"a floor lamp","x":0.56,"y":0.19,"voice":"male"},
  {"word":"a curtain","x":0.78,"y":0.08,"voice":"male"},
  {"word":"a notebook","x":0.20,"y":0.52,"voice":"male"},
  {"word":"a velvet sofa","x":0.50,"y":0.93,"voice":"male"}],
 "question":"Where is the man lying?",
 "answer":["He","is","lying","on","a","velvet","sofa."],
 "answerVoice":"male",
 "notes":"key word 'psychology' is abstract, not placed; the woman's elbow on the chair back reaches over the man's head, her box is cut at the man's left edge; notebook = the book on her lap; man rests his hands on his chest at 3.7 (gesturing before)."}
json.dump(c,open("content/7952.json","w"),indent=1)
