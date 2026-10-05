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
worker=K([(0.82,0,1,0.53),(0.60,0,1,0.57),(0.47,0.03,1,0.63),(0.41,0.13,1,0.69),
          (0.41,0.20,1,0.73),(0.49,0.26,1,0.74),(0.47,0.27,0.97,0.77),(0.71,0.29,1,0.77)])
woman=K([(0.16,0,0.36,0.14),(0.17,0,0.38,0.20),(0.17,0.01,0.37,0.23),(0.18,0.05,0.39,0.28),
         (0.19,0.09,0.39,0.32),(0.19,0.12,0.39,0.35),(0.19,0.15,0.39,0.38),(0.19,0.15,0.39,0.38)])
d={"mediaId":6842,"level":"B","keyWord":"assembly","defaultVoice":"male",
 "taps":[
  {"phrase":"to guide a hub into place","target":"the young worker","voice":"male","keys":worker},
  {"phrase":"to step back from the hub","target":"the young worker","voice":"male","keys":worker},
  {"phrase":"to look on from the truck","target":"the woman on the truck","voice":"female","keys":woman}],
 "stillS":3.7,
 "nouns":[{"word":"a crane","x":0.84,"y":0.20,"voice":"male"},
          {"word":"an assembly","x":0.50,"y":0.56,"voice":"male"},
          {"word":"a tyre","x":0.30,"y":0.74,"voice":"male"},
          {"word":"a pallet","x":0.27,"y":0.93,"voice":"male"}],
 "question":"What is the young worker doing?",
 "answer":["He","is","guiding","a","hub","into","place."],
 "answerVoice":"male",
 "notes":"'an assembly' labels the wheel-hub assembly (key word) - verify it reads naturally. 'to step back from the hub' only at the last frame (3.7). The woman is small at the top left, partly cut at t=0.2."}
json.dump(d,open("content/6842.json","w"),indent=1)
