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
W=[(0.10,0.72,0.90,0.28),(0.42,0.70,0.58,0.30),(0.62,0.56,0.38,0.40),OFF,(0.82,0.14,0.18,0.34),(0.80,0.17,0.20,0.20),
   (0.70,0.20,0.30,0.66),(0.50,0,0.50,0.86),(0.45,0,0.55,0.73),(0.22,0,0.58,0.53),(0.18,0.09,0.48,0.46),
   (0.24,0.21,0.36,0.29),(0.22,0.25,0.38,0.22),(0.28,0.27,0.36,0.22),(0.31,0.29,0.22,0.22),(0.34,0.29,0.22,0.20),
   (0.35,0.31,0.22,0.18),(0.34,0.32,0.22,0.17),(0.34,0.34,0.22,0.16),(0.32,0.36,0.26,0.15),(0.30,0.36,0.27,0.14)]
H=[(0.33,0,0.67,0.72),(0.15,0,0.85,0.70),(0,0.02,0.62,0.98),(0,0.04,1,0.96),(0,0,0.82,1),(0,0.02,0.80,0.98),
   (0,0.03,0.70,0.97),(0,0.09,0.50,0.91),(0,0.09,0.45,0.91),(0,0.53,1,0.44),(0,0.55,1,0.43),
   (0.22,0.50,0.60,0.44),(0.20,0.47,0.48,0.32),(0.24,0.49,0.40,0.30),(0.10,0.51,0.62,0.36),(0.02,0.49,0.80,0.37),
   (0,0.49,0.84,0.25),(0,0.49,0.86,0.23),(0,0.50,0.84,0.34),(0,0.51,0.82,0.33),(0,0.50,0.82,0.24)]
kw=keys(t,W)
json.dump({"mediaId":392,"level":"A","keyWord":"horse","defaultVoice":"female",
 "taps":[
  {"phrase":"to ride a horse","target":"the woman","voice":"female","keys":kw},
  {"phrase":"to carry the woman","target":"the horse","voice":"female","keys":keys(t,H)},
  {"phrase":"to get on the horse","target":"the woman","voice":"female","keys":kw}],
 "stillS":8.5,
 "nouns":[{"word":"the sky","x":0.50,"y":0.15,"voice":"female"},{"word":"a woman","x":0.50,"y":0.41,"voice":"female"},
          {"word":"a horse","x":0.25,"y":0.56,"voice":"female"},{"word":"grass","x":0.55,"y":0.85,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","riding","a","horse."],"answerVoice":"female",
 "notes":"Rider sits on the horse, so the two always overlap: from 4.5 s the boxes are split by a horizontal line at the horse's back (woman = upper body above the saddle; her boots and the horse's head, which rises above that line, fall in the other box or in none). 0.0-1.0 only the woman's hands / sleeves are in the picture, 1.5 s she is not visible, 2.0-3.0 only her arm and coat at the right edge. She gets on the horse at 3.0-4.0 s and rides from 4.5 s."},
 open("content/392.json","w"),indent=1,ensure_ascii=False)
