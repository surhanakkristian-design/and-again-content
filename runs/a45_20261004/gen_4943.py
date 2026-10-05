import json
T=[i*0.5 for i in range(19)]
def keys(d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in T]
act={0.0:(0.05,0.04,0.85,0.96),0.5:(0.05,0.03,0.85,0.97),1.0:(0.03,0.04,0.87,0.96),1.5:(0.38,0.28,0.42,0.60),
     2.0:(0.20,0.30,0.75,0.68),2.5:(0.42,0.27,0.58,0.73),3.5:(0,0.26,1,0.74),4.0:(0,0.25,0.80,0.75),
     4.5:(0,0.21,1,0.79),5.0:(0,0.22,1,0.78),5.5:(0,0.21,1,0.79),7.0:(0,0.14,1,0.86),7.5:(0.08,0.55,0.80,0.45),
     8.0:(0.08,0.55,0.82,0.45),8.5:(0,0.12,1,0.88),9.0:(0,0.16,1,0.84)}
old={6.0:(0,0.10,1,0.90),6.5:(0.22,0.30,0.24,0.48)}
c={"mediaId":4943,"level":"B","keyWord":"praise","defaultVoice":"male",
 "taps":[
  {"phrase":"to pull a shocked face","target":"the young man","voice":"male","keys":keys(act)},
  {"phrase":"to take a bow","target":"the young man","voice":"male","keys":keys(act)},
  {"phrase":"to punch the air","target":"the older man","voice":"male","keys":keys(old)}],
 "stillS":8.0,
 "nouns":[{"word":"a spotlight","x":0.30,"y":0.37,"voice":"male"},
          {"word":"crew members","x":0.65,"y":0.47,"voice":"male"},
          {"word":"a sweater","x":0.22,"y":0.75,"voice":"male"}],
 "question":"What is the crew doing?",
 "answer":["They","are","cheering","for","the","young","actor."],
 "answerVoice":"male",
 "notes":"Older man punches the air only at 6.0 s (close-up); at 6.5 s the box is on the man second from left in the clapping line, assumed to be the same man (glasses, black shirt) - verify. Clapperboard shot 3.0 s: young man off. 'actor' in the answer is inferred from the film set."}
json.dump(c,open('content/4943.json','w'),indent=1)
