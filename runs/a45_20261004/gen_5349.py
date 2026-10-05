import json
def K(d, times):
    out=[]
    for t in times:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=b; out.append({"t":t,"x":round(x,2),"y":round(y,2),"w":round(min(w,1-x),2),"h":round(min(h,1-y),2)})
    return out
T=[i*0.5 for i in range(19)]
woman={0.0:(0,0.06,0.66,0.94),0.5:(0,0.06,0.69,0.94),1.0:(0,0.07,0.66,0.93),1.5:(0,0.08,0.58,0.92),
 2.0:(0,0.07,0.58,0.93),2.5:(0,0.07,0.87,0.93),3.0:(0,0.08,0.72,0.92),3.5:(0,0.08,0.70,0.92),
 4.0:(0,0.10,0.52,0.90),4.5:(0,0.17,0.30,0.83),5.0:(0,0.17,0.25,0.83),5.5:(0,0.17,0.25,0.83),
 6.0:(0,0.15,0.21,0.85),6.5:(0,0.15,0.21,0.85)}
young={0.0:(0.68,0.08,0.32,0.92),0.5:(0.71,0.08,0.29,0.92),1.0:(0.68,0.08,0.32,0.92),1.5:(0.60,0.09,0.40,0.91),
 2.0:(0.59,0.16,0.16,0.45)}
big={3.5:(0.72,0.0,0.28,1.0),4.0:(0.53,0.01,0.47,0.99),4.5:(0.31,0.03,0.69,0.97),5.0:(0.26,0.05,0.74,0.95),
 5.5:(0.26,0.05,0.74,0.95),6.0:(0.22,0.03,0.78,0.97),6.5:(0.22,0.03,0.78,0.97),7.0:(0.04,0.03,0.96,0.97),
 7.5:(0.03,0.03,0.97,0.97),8.0:(0.0,0.02,1.0,0.98),8.5:(0.0,0.02,1.0,0.98),9.0:(0.0,0.03,1.0,0.97)}
c={"mediaId":5349,"level":"B","keyWord":"award","defaultVoice":"female",
 "taps":[
  {"phrase":"to pin on a medal","target":"the grey-haired woman","voice":"female","keys":K(woman,T)},
  {"phrase":"to shake the woman's hand","target":"the young man","voice":"male","keys":K(young,T)},
  {"phrase":"to grin at the camera","target":"the man with many medals","voice":"male","keys":K(big,T)}],
 "stillS":0.0,
 "nouns":[{"word":"flags","x":0.46,"y":0.24,"voice":"female"},
          {"word":"a bow tie","x":0.84,"y":0.38,"voice":"female"},
          {"word":"white gloves","x":0.70,"y":0.53,"voice":"female"},
          {"word":"a velvet cushion","x":0.24,"y":0.88,"voice":"female"}],
 "question":"What is the grey-haired woman doing?",
 "answer":["She","is","pinning","a","medal","on","his","jacket."],
 "answerVoice":"female",
 "notes":"Several cuts: young man in black tie 0.0-2.0 (2.0 small, behind), a different bald man at 2.5-3.0 (no target), the man with many medals from 3.5. Key word 'award' is a verb, not used as a noun. At 1.5 the woman and young man shake hands; box split at x 0.59."}
json.dump(c,open('content/5349.json','w'),indent=1)
