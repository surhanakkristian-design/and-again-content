import json
T=[i*0.5 for i in range(21)]
def K(lst):
    out=[]
    for t,v in zip(T,lst):
        if v is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=v; out.append({"t":t,"x":x,"y":y,"w":round(w,2),"h":round(h,2)})
    return out
man=[(0.04,0.0,0.56,1.0),(0.0,0.0,0.66,1.0),(0.0,0.2,0.56,0.8),(0.0,0.2,0.58,0.8),
     (0.40,0.18,0.45,0.82),(0.40,0.17,0.60,0.83),(0.50,0.18,0.50,0.82),(0.42,0.2,0.58,0.8),
     (0.0,0.2,0.52,0.8),(0.0,0.18,0.60,0.82),(0.0,0.08,0.20,0.92),None,
     (0.0,0.0,0.27,1.0),(0.0,0.0,0.15,0.65),None,None,None,None,None,(0.0,0.0,0.20,0.48),(0.0,0.0,0.22,1.0)]
wom=[(0.60,0.35,0.40,0.65),(0.66,0.33,0.34,0.67),(0.56,0.4,0.44,0.6),(0.58,0.38,0.42,0.62),
     (0.02,0.36,0.38,0.64),(0.0,0.35,0.38,0.65),(0.0,0.33,0.48,0.67),(0.0,0.42,0.42,0.58),
     (0.52,0.40,0.48,0.6),(0.60,0.28,0.40,0.72),(0.24,0.33,0.66,0.67),(0.33,0.3,0.64,0.7),
     (0.37,0.16,0.63,0.84),(0.16,0.25,0.81,0.75),(0.08,0.15,0.78,0.85),(0.04,0.22,0.90,0.78),
     (0.28,0.25,0.70,0.75),(0.08,0.2,0.92,0.8),(0.17,0.25,0.83,0.75),(0.25,0.3,0.75,0.7),(0.23,0.32,0.77,0.68)]
c={"mediaId":5388,"level":"B","keyWord":"packet","defaultVoice":"female",
 "taps":[
  {"phrase":"to hold crisps out of reach","target":"the man","voice":"male","keys":K(man)},
  {"phrase":"to reach for the crisps","target":"the woman","voice":"female","keys":K(wom)},
  {"phrase":"to settle on the sofa","target":"the woman","voice":"female","keys":K(wom)}],
 "stillS":8.5,
 "nouns":[{"word":"a packet","x":0.46,"y":0.68,"voice":"female"},
          {"word":"a football shirt","x":0.80,"y":0.56,"voice":"female"},
          {"word":"a cushion","x":0.19,"y":0.56,"voice":"female"},
          {"word":"a poster","x":0.17,"y":0.09,"voice":"female"}],
 "question":"What is the man doing?",
 "answer":["He","is","holding","the","packet","out","of","reach."],
 "answerVoice":"male",
 "notes":"Two crisp packets appear: from ~6 s the woman takes a second packet off the sofa while the man keeps his; description says she takes his. Man mostly off-frame 7.0-9.0 s (only a hand/packet edge), marked off. Several frames split boxes where the two overlap (2.0, 3.5, 4.0, 4.5)."}
json.dump(c,open("content/5388.json","w"),indent=1)
