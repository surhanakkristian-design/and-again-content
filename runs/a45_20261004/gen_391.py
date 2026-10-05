import json
OFF=None
def keys(times, boxes):
    assert len(times)==len(boxes), (len(times),len(boxes))
    out=[]
    for t,b in zip(times,boxes):
        if b is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":b[0],"y":b[1],"w":round(b[2],2),"h":round(b[3],2)})
    return out
t=[round(i*0.5,2) for i in range(21)]
W=[(0,0.19,1,0.81),(0,0.21,1,0.79),(0,0.20,1,0.80),(0.03,0.23,0.97,0.77),(0.08,0.21,0.92,0.79),(0.06,0.21,0.73,0.79),
   (0.08,0.31,0.42,0.69),(0.13,0.25,0.70,0.72),(0.12,0.19,0.58,0.65),(0.09,0.24,0.62,0.63),
   (0.02,0.29,0.62,0.23),(0.02,0.29,0.65,0.23),(0.02,0.27,0.60,0.24),
   (0,0.16,0.75,0.84),(0,0.17,0.77,0.83),(0,0.16,0.80,0.84),(0,0.17,0.78,0.83),
   (0.08,0.17,0.56,0.83),(0.02,0.25,0.77,0.75),(0.04,0.26,0.90,0.74),(0,0.05,1,0.95)]
B=[OFF]*6+[(0.50,0.41,0.26,0.14),OFF,OFF,OFF,(0.31,0.52,0.30,0.13),(0.31,0.52,0.36,0.13),(0.38,0.51,0.38,0.13)]+[OFF]*8
kw=keys(t,W)
json.dump({"mediaId":391,"level":"A","keyWord":"hope","defaultVoice":"female",
 "taps":[
  {"phrase":"to climb onto the wall","target":"the woman","voice":"female","keys":kw},
  {"phrase":"to raise her arms","target":"the woman","voice":"female","keys":kw},
  {"phrase":"to sail on the sea","target":"the boat","voice":"female","keys":keys(t,B)}],
 "stillS":6.0,
 "nouns":[{"word":"a woman","x":0.22,"y":0.45,"voice":"female"},{"word":"a boat","x":0.57,"y":0.56,"voice":"female"},
          {"word":"the sea","x":0.72,"y":0.70,"voice":"female"},{"word":"a wall","x":0.55,"y":0.90,"voice":"female"}],
 "question":"What is the woman looking at?",
 "answer":["She","is","looking","at","a","boat."],"answerVoice":"female",
 "notes":"Key word 'hope' is abstract, not used as a noun. The boat is visible only at 3.0 and 5.0-6.0 (at 4.0/4.5 it is almost hidden behind her legs: off). At 5.0-6.0 the boat lies inside the woman's outline (between her legs and her hands), so her box there is only the upper body (head, back, hands) down to the boat's top, her legs are in no box; at 3.0 split at x=0.50. She climbs the wall at 3.0-3.5, raises her arms at 9.5-10.0. Tiny man in white far back at 0-2.5 s ignored."},
 open("content/391.json","w"),indent=1,ensure_ascii=False)
