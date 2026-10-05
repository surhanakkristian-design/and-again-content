import json
def K(d, times):
    out=[]
    for t in times:
        v=d.get(t)
        if v is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=v; out.append({"t":t,"x":x,"y":y,"w":round(min(w,1-x),2),"h":round(min(h,1-y),2)})
    return out
times=[i*0.5 for i in range(19)]
man={0.0:(0.09,0,0.71,1),0.5:(0.12,0,0.66,1),1.0:(0.08,0,0.62,1),1.5:(0.10,0.04,0.56,0.96),2.0:(0.18,0,0.66,1),
 2.5:(0.22,0,0.65,0.90),3.0:(0.10,0,0.62,0.86),3.5:(0.17,0,0.57,0.81),4.0:(0.23,0.04,0.54,0.84),4.5:(0.28,0.01,0.42,0.86),
 5.0:(0.22,0.05,0.45,0.88),5.5:(0.28,0.05,0.38,0.86),6.0:(0.23,0.08,0.34,0.80),6.5:(0.26,0.11,0.36,0.75),
 7.0:(0.27,0.14,0.40,0.74),7.5:(0.24,0.16,0.41,0.70),8.0:(0.22,0.16,0.43,0.72),8.5:(0.25,0.16,0.39,0.70),9.0:(0.22,0.12,0.43,0.75)}
cyc={1.0:(0.70,0.22,0.30,0.34)}
c={"mediaId":5278,"level":"B","keyWord":"corner","defaultVoice":"male","taps":[
 {"phrase":"to stroll past chalk drawings","target":"the young man","voice":"male","keys":K(man,times)},
 {"phrase":"to wear headphones round his neck","target":"the young man","voice":"male","keys":K(man,times)},
 {"phrase":"to cycle along the road","target":"the cyclist","voice":"male","keys":K(cyc,times)}],
 "stillS":5.0,
 "nouns":[{"word":"a denim jacket","x":0.38,"y":0.32,"voice":"male"},
  {"word":"a zebra crossing","x":0.78,"y":0.42,"voice":"male"},
  {"word":"a fire hydrant","x":0.17,"y":0.58,"voice":"male"},
  {"word":"a litter bin","x":0.72,"y":0.62,"voice":"male"}],
 "question":"What is the young man doing?",
 "answer":["He","is","strolling","past","chalk","drawings."],
 "answerVoice":"male",
 "notes":"One main person; the only other clear single target is the cyclist, who is visible at 1.0 only (box split from the man at x 0.70, so the man's right hand is cut there). Two phrases share the young man. Chalk drawings visible 3.0-4.5. Still 5.0: one hydrant (at 4.5 there are two), bin, zebra crossing with pedestrians; 'corner' not placed as a pill because the corner itself has no single clear spot."}
json.dump(c,open('content/5278.json','w'),indent=1)
