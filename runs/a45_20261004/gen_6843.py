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
lad=K([(0.18,0.20,0.80,0.65),(0.18,0.18,0.83,0.65),(0.18,0.21,0.84,0.69),(0.14,0.20,0.85,0.70),
       (0.14,0.19,0.85,0.69),(0.12,0.18,0.82,0.71),(0.11,0.18,0.88,0.72),(0.11,0.17,0.89,0.73)])
hat=K([(0.13,0.73,0.48,1),(0.12,0.75,0.50,1),(0.11,0.77,0.44,1),(0.12,0.79,0.46,1),
       (0.11,0.80,0.44,1),(0.10,0.82,0.44,1),(0.08,0.83,0.43,1),(0.07,0.84,0.43,1)])
d={"mediaId":6843,"level":"B","keyWord":"asshole","defaultVoice":"male",
 "taps":[
  {"phrase":"to sip a drink","target":"the man on the ladder","voice":"male","keys":lad},
  {"phrase":"to fan himself","target":"the man on the ladder","voice":"male","keys":lad},
  {"phrase":"to wear a straw hat","target":"the man in the straw hat","voice":"male","keys":hat}],
 "stillS":2.2,
 "nouns":[{"word":"a parasol","x":0.45,"y":0.12,"voice":"male"},
          {"word":"a handheld fan","x":0.51,"y":0.30,"voice":"male"},
          {"word":"a stepladder","x":0.36,"y":0.66,"voice":"male"},
          {"word":"a straw hat","x":0.27,"y":0.87,"voice":"male"}],
 "question":"What is the man up there doing?",
 "answer":["He","is","sipping","a","drink."],
 "answerVoice":"male",
 "notes":"Key word 'asshole' is not a visible noun and not used. Straw-hat man is a front-row crowd member, cut at the bottom edge; check no other straw hat is prominent. Phrase 'to sip a drink' kept to 4 words (no straw)."}
json.dump(d,open("content/6843.json","w"),indent=1)
