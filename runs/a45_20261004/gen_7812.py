import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes):
    out=[]
    for t,b in zip(T,boxes):
        if b is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=b; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
    return out
man=K([(0.08,0.37,0.48,0.63),(0.08,0.37,0.48,0.63),(0.08,0.37,0.47,0.63),(0.08,0.36,0.49,0.64),
       (0.07,0.35,0.50,0.65),(0.07,0.35,0.51,0.65),(0.06,0.34,0.52,0.66),(0.05,0.34,0.53,0.66)])
woman=K([(0.61,0.41,0.32,0.25),(0.60,0.41,0.33,0.26),(0.56,0.40,0.35,0.30),(0.58,0.37,0.33,0.31),
         (0.58,0.36,0.34,0.31),(0.59,0.36,0.33,0.30),(0.59,0.36,0.34,0.32),(0.59,0.36,0.37,0.33)])
d={"mediaId":7812,"level":"B","keyWord":"dreaming","defaultVoice":"male",
 "taps":[{"phrase":"to stare into space","target":"the man in green","voice":"male","keys":man},
         {"phrase":"to knock over his coffee","target":"the man in green","voice":"male","keys":man},
         {"phrase":"to hold out a paper cup","target":"the woman in yellow","voice":"female","keys":woman}],
 "stillS":3.2,
 "nouns":[{"word":"an arched window","x":0.80,"y":0.25,"voice":"male"},
          {"word":"a hanging lamp","x":0.48,"y":0.07,"voice":"male"},
          {"word":"a paper cup","x":0.63,"y":0.58,"voice":"male"},
          {"word":"a notebook","x":0.62,"y":0.70,"voice":"male"}],
 "question":"What is the man in green doing?",
 "answer":["He","is","staring","into","space."],"answerVoice":"male",
 "notes":"Only two usable targets (student with scarf behind overlaps the man's box), so the man has two phrases. 'knock over his coffee': cup tips over right beside his arm at 0.7-1.2 s, he never reacts; verifier may check it reads as his doing. Woman catches the cup at 1.2 and holds it out from 1.7."}
json.dump(d,open("content/7812.json","w"),indent=1)
