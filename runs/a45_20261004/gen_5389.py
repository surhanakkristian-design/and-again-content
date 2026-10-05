import json
T=[i*0.5 for i in range(21)]
def K(lst):
    out=[]
    for t,v in zip(T,lst):
        if v is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=v; out.append({"t":t,"x":x,"y":y,"w":round(w,2),"h":round(h,2)})
    return out
man=[(0.10,0.13,0.38,0.85),(0.13,0.2,0.37,0.8),(0.20,0.17,0.38,0.82),(0.10,0.33,0.45,0.52),
     (0.55,0.30,0.43,0.47),(0.42,0.26,0.55,0.52),(0.12,0.27,0.82,0.73),(0.0,0.27,0.44,0.73),
     (0.22,0.23,0.30,0.55),(0.20,0.26,0.34,0.46),(0.06,0.23,0.36,0.57),(0.05,0.23,0.44,0.62),
     (0.0,0.19,0.47,0.73),(0.05,0.33,0.67,0.64),(0.0,0.41,0.52,0.59),(0.0,0.17,0.30,0.30),
     None,(0.0,0.35,0.18,0.62),(0.0,0.32,0.48,0.68),(0.0,0.27,0.52,0.73),(0.0,0.24,0.52,0.76)]
wom=[(0.50,0.18,0.46,0.74),(0.57,0.4,0.40,0.58),(0.60,0.38,0.36,0.62),(0.55,0.37,0.40,0.58),
     (0.08,0.42,0.44,0.50),(0.0,0.34,0.41,0.40),None,(0.60,0.35,0.40,0.65),
     (0.52,0.38,0.48,0.58),(0.0,0.35,0.20,0.38),(0.42,0.33,0.32,0.55),(0.65,0.31,0.33,0.63),
     (0.67,0.30,0.32,0.70),(0.72,0.32,0.28,0.60),(0.58,0.30,0.40,0.67),(0.52,0.35,0.38,0.62),
     (0.37,0.31,0.50,0.67),(0.32,0.32,0.64,0.68),(0.49,0.32,0.48,0.68),(0.52,0.29,0.46,0.71),(0.52,0.26,0.46,0.74)]
c={"mediaId":5389,"level":"B","keyWord":"dodge","defaultVoice":"male",
 "taps":[
  {"phrase":"to dodge her outstretched hands","target":"the man","voice":"male","keys":K(man)},
  {"phrase":"to fold her arms","target":"the woman","voice":"female","keys":K(wom)},
  {"phrase":"to help himself to crisps","target":"the man","voice":"male","keys":K(man)}],
 "stillS":8.0,
 "nouns":[{"word":"a packet","x":0.63,"y":0.56,"voice":"male"},
          {"word":"a cushion","x":0.20,"y":0.60,"voice":"male"},
          {"word":"a sofa","x":0.20,"y":0.80,"voice":"male"},
          {"word":"curtains","x":0.50,"y":0.15,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","dodging","her","outstretched","hands."],
 "answerVoice":"male",
 "notes":"Description says she corners him; in the frames he bows and hands her the packet at ~6.5 s. Woman hidden behind the man at 3.0 s (off). 'to help himself to crisps' = 9.5-10 s, he takes a crisp from her packet. Boxes split at 1.5, 4.0, 6.5, 10.0 where the two overlap."}
json.dump(c,open("content/5389.json","w"),indent=1)
