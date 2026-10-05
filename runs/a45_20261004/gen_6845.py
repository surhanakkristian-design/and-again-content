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
man=K([(0.13,0.19,0.79,0.88),(0.13,0.16,0.80,0.89),(0.12,0.14,0.78,0.94),(0.11,0.13,0.79,0.98),
       (0.10,0.13,0.85,0.98),(0.09,0.12,0.87,1),(0.09,0.12,0.91,1),(0.08,0.11,0.93,1)])
cap=K([(0.82,0.29,1,0.62),(0.82,0.29,1,0.63),(0.82,0.30,1,0.64),(0.82,0.29,1,0.64),None,None,None,None])
d={"mediaId":6845,"level":"B","keyWord":"attempt","defaultVoice":"male",
 "taps":[
  {"phrase":"to lift a huge boulder","target":"the young man","voice":"male","keys":man},
  {"phrase":"to grit his teeth","target":"the young man","voice":"male","keys":man},
  {"phrase":"to wear a flat cap","target":"the old man in the cap","voice":"male","keys":cap}],
 "stillS":2.2,
 "nouns":[{"word":"bunting","x":0.70,"y":0.18,"voice":"male"},
          {"word":"a barrel","x":0.15,"y":0.37,"voice":"male"},
          {"word":"a dog","x":0.12,"y":0.50,"voice":"male"},
          {"word":"a boulder","x":0.52,"y":0.68,"voice":"male"}],
 "question":"What is the young man doing?",
 "answer":["He","is","attempting","to","lift","a","huge","boulder."],
 "answerVoice":"male",
 "notes":"Old man in the flat cap sits at the right edge, visible 0.2-1.7 only, then out of frame (off). The bald old man also holds a walking stick, so no stick phrase. 'to grit his teeth' clearest at 0.7-1.7."}
json.dump(d,open("content/6845.json","w"),indent=1)
