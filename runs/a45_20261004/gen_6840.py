import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes):
    out=[]
    for t,b in zip(T,boxes):
        if b is None: out.append({"t":t,"off":True}); continue
        x0,y0,x1,y1=b
        x0=max(0,x0);y0=max(0,y0);x1=min(1,x1);y1=min(1,y1)
        out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
woman=K([(0.17,0.29,0.52,0.93),(0.16,0.28,0.51,0.93),(0.16,0.28,0.52,0.97),(0.15,0.27,0.52,0.97),
         (0.14,0.26,0.53,1.0),(0.12,0.25,0.55,1.0),(0.10,0.25,0.55,1.0),(0.08,0.24,0.56,1.0)])
man=K([(0.52,0.40,0.70,0.65),(0.52,0.39,0.70,0.65),(0.52,0.40,0.70,0.66),(0.52,0.39,0.72,0.67),
       (0.53,0.38,0.76,0.68),(0.55,0.38,0.75,0.67),(0.55,0.39,0.76,0.68),(0.56,0.38,0.76,0.67)])
d={"mediaId":6840,"level":"B","keyWord":"arrival","defaultVoice":"female",
 "taps":[
  {"phrase":"to set down a parcel","target":"the young woman","voice":"female","keys":woman},
  {"phrase":"to clutch a ferry ticket","target":"the young woman","voice":"female","keys":woman},
  {"phrase":"to push a loaded trolley","target":"the man with the trolley","voice":"male","keys":man}],
 "stillS":1.2,
 "nouns":[{"word":"a ferry","x":0.82,"y":0.18,"voice":"female"},
          {"word":"a cottage","x":0.80,"y":0.40,"voice":"female"},
          {"word":"a backpack","x":0.48,"y":0.76,"voice":"female"},
          {"word":"a parcel","x":0.59,"y":0.89,"voice":"female"}],
 "question":"What is the woman in red holding?",
 "answer":["She","is","clutching","a","ferry","ticket."],
 "answerVoice":"female",
 "notes":"Parcel is set down only at the very start (t=0.2, still falling). Woman's pointing arm at 3.2/3.7 reaches into the trolley man's box; boxes split at x=0.55. Arrival itself is not a placeable noun."}
json.dump(d,open("content/6840.json","w"),indent=1)
