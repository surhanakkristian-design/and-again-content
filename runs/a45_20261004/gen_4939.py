import json
T=[i*0.5 for i in range(19)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
man={0.0:(0,0,1,0.48),0.5:(0,0,1,0.45),1.0:(0,0,0.9,0.62),1.5:(0,0,1,0.62),2.0:(0,0,0.92,0.62),
     4.5:(0,0.05,1,0.95),5.0:(0,0.05,1,0.95),5.5:(0,0.05,1,0.95),6.0:(0,0,1,0.29),6.5:(0.2,0,0.8,0.25),
     7.0:(0,0,1,1),7.5:(0,0,1,1),8.0:(0,0.05,1,0.95),8.5:(0,0.05,1,0.95),9.0:(0,0.05,1,0.95)}
cro={6.0:(0,0.31,1,0.57),6.5:(0,0.26,1,0.56)}
c={"mediaId":4939,"level":"A","keyWord":"golden","defaultVoice":"male",
 "taps":[
  {"phrase":"to press the dough","target":"the man","voice":"male","keys":keys(man)},
  {"phrase":"to wipe his forehead","target":"the man","voice":"male","keys":keys(man)},
  {"phrase":"to lie on a tray","target":"the croissants","voice":"male","keys":keys(cro)}],
 "stillS":6.0,
 "nouns":[{"word":"croissants","x":0.45,"y":0.52,"voice":"male"},
          {"word":"a tray","x":0.30,"y":0.89,"voice":"male"},
          {"word":"an apron","x":0.72,"y":0.12,"voice":"male"}],
 "question":"What is the man holding?",
 "answer":["He","is","holding","a","loaf","of","golden","bread."],
 "answerVoice":"male",
 "notes":"Single person; two man phrases. Croissants visible only 6.0-6.5 s (one shot). Man body partly hidden behind bread at 8-9 s, box includes bread."}
json.dump(c,open('content/4939.json','w'),indent=1)
