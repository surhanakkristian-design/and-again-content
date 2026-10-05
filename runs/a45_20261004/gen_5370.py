import json
VID=5370
T=[i*0.5 for i in range(25)]
def K(d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in T]
M={0.0:(0,0.16,0.33,0.38),0.5:(0,0.29,0.37,0.31),1.0:(0,0.3,0.3,0.28),1.5:(0,0.3,0.15,0.3),
   4.5:(0.2,0.37,0.72,0.63),5.0:(0.08,0.38,0.92,0.62),5.5:(0.06,0.37,0.9,0.63),6.0:(0.02,0.38,0.97,0.62),6.5:(0.05,0.38,0.9,0.62),
   7.0:(0.08,0.1,0.85,0.72),7.5:(0.06,0.1,0.92,0.72),8.0:(0,0.08,1,0.72),8.5:(0,0.07,1,0.73),9.0:(0,0.08,1,0.72),9.5:(0,0.07,1,0.73),
   10.0:(0,0.04,1,0.76),10.5:(0,0.04,1,0.76),11.0:(0,0.04,1,0.76),11.5:(0,0.05,1,0.75),12.0:(0,0.08,1,0.73)}
H={0.0:(0.33,0.33,0.67,0.16),0.5:(0.37,0.37,0.62,0.15),1.0:(0.3,0.37,0.7,0.15),1.5:(0.15,0.37,0.85,0.14),
   2.0:(0,0.36,1,0.14),2.5:(0.15,0.37,0.8,0.14),3.0:(0.4,0.37,0.6,0.14),3.5:(0.05,0.37,0.95,0.14),4.0:(0,0.37,1,0.14)}
c={"mediaId":VID,"level":"B","keyWord":"a canoe","defaultVoice":"male",
 "taps":[
  {"phrase":"to paddle across the water","target":"the man","voice":"male","keys":K(M)},
  {"phrase":"to bite into a cinnamon bun","target":"the man","voice":"male","keys":K(M)},
  {"phrase":"to stand on a rocky island","target":"the red houses","voice":"male","keys":K(H)}],
 "stillS":0.5,
 "nouns":[{"word":"the sky","x":0.5,"y":0.15,"voice":"male"},
          {"word":"a red house","x":0.72,"y":0.44,"voice":"male"},
          {"word":"a paddle","x":0.42,"y":0.57,"voice":"male"},
          {"word":"a canoe","x":0.13,"y":0.67,"voice":"male"}],
 "question":"What is he doing at the table?",
 "answer":["He","is","biting","into","a","cinnamon","bun."],
 "answerVoice":"male",
 "notes":"Three shots: water 0.0-4.0 (man only at 0.0-1.5, off 2.0-4.0 where only his hand/paddle blade show), street 4.5-6.5, cafe table 7.0-12.0. The boat is really a sit-in kayak with a double paddle; key word given as canoe, kept as 'a canoe' noun. The red houses box covers the row of houses on the rock (water shots only); at 1.5 split from the man at x 0.15. Small cyclist in the street shot not used. Still 0.5: two red houses, pill on the bigger right one."}
json.dump(c,open(f'content/{VID}.json','w'),indent=1)
