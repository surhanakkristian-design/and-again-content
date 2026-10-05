import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2]
def K(boxes):
    out=[]
    for t,b in zip(T,boxes):
        if b is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=b; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
    return out
man=K([(0.17,0.37,0.31,0.47),(0.15,0.34,0.35,0.50),(0.15,0.27,0.37,0.59),(0.07,0.23,0.44,0.71),
       (0.08,0.26,0.48,0.69),(0.18,0.33,0.41,0.58),(0.20,0.40,0.37,0.49)])
woman=K([(0.60,0.46,0.30,0.37),(0.60,0.46,0.37,0.37),(0.57,0.47,0.30,0.37),(0.58,0.51,0.30,0.35),
         (0.57,0.50,0.26,0.37),(0.60,0.51,0.20,0.37),(0.58,0.51,0.22,0.38)])
d={"mediaId":7814,"level":"A","keyWord":"early","defaultVoice":"male",
 "taps":[{"phrase":"to go for a run","target":"the man","voice":"male","keys":man},
         {"phrase":"to wave to the woman","target":"the man","voice":"male","keys":man},
         {"phrase":"to move a chair","target":"the woman","voice":"female","keys":woman}],
 "stillS":0.2,
 "nouns":[{"word":"the sky","x":0.50,"y":0.15,"voice":"male"},
          {"word":"a lamp","x":0.69,"y":0.34,"voice":"male"},
          {"word":"a man","x":0.33,"y":0.50,"voice":"male"},
          {"word":"a cat","x":0.83,"y":0.77,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","going","for","an","early","run."],"answerVoice":"male",
 "notes":"Man waves only at 2.7-3.2 s (seen from behind, hand raised). Woman handles a folding chair 0.2-1.7, then stands and watches; cat too small/static for a phrase. 'a man' noun is the only man in the frame."}
json.dump(d,open("content/7814.json","w"),indent=1)
