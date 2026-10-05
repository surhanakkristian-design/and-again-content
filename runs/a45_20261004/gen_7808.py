import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes):
    out=[]
    for t,b in zip(T,boxes):
        if b is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=b; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
    return out
man=K([(0.35,0.59,0.28,0.26),(0.33,0.60,0.29,0.26),(0.33,0.53,0.26,0.36),(0.33,0.52,0.30,0.38),
       (0.32,0.53,0.29,0.40),(0.31,0.53,0.30,0.42),(0.31,0.52,0.31,0.43),(0.30,0.52,0.32,0.47)])
plant=K([(0.20,0.32,0.37,0.27),(0.24,0.32,0.39,0.28),(0.60,0.29,0.135,0.41),(0.66,0.28,0.34,0.48),
         None,None,None,None])
lilac=K([(0.635,0.34,0.27,0.37),(0.66,0.33,0.30,0.38),(0.74,0.32,0.20,0.38),None,
         (0.62,0.31,0.30,0.40),(0.62,0.31,0.30,0.40),(0.74,0.29,0.26,0.43),(0.72,0.29,0.28,0.43)])
d={"mediaId":7808,"level":"A","keyWord":"do nothing","defaultVoice":"male",
 "taps":[{"phrase":"to do nothing","target":"the man on the bed","voice":"male","keys":man},
         {"phrase":"to carry a plant","target":"the woman with the plant","voice":"female","keys":plant},
         {"phrase":"to drop a pillow","target":"the woman in lilac","voice":"female","keys":lilac}],
 "stillS":3.7,
 "nouns":[{"word":"a window","x":0.16,"y":0.33,"voice":"male"},
          {"word":"a sofa","x":0.36,"y":0.51,"voice":"male"},
          {"word":"a pillow","x":0.47,"y":0.62,"voice":"male"},
          {"word":"the floor","x":0.22,"y":0.92,"voice":"male"}],
 "question":"What is the lying man doing?",
 "answer":["He","is","doing","nothing."],"answerVoice":"male",
 "notes":"Man lies on a bare mattress, called 'the bed' for level A. Plant woman's legs overlap the lying man at 0.2/0.7: boxes split horizontally at y~0.6. At 1.2 plant woman and lilac woman split at x~0.74; lilac woman hidden behind plant woman at 1.7 (off). Lilac woman's pillow lands on his face ~3.0 s."}
json.dump(d,open("content/7808.json","w"),indent=1)
