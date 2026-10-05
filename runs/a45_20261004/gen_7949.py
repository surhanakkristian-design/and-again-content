import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes):
    out=[]
    for t,b in zip(T,boxes):
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
woman=K([(0.60,0.19,0.39,0.65),(0.62,0.15,0.38,0.70),(0.71,0.10,0.29,0.79),(0.83,0.04,0.17,0.88),None,None,None,None])
kitten=K([(0.42,0.49,0.17,0.14),(0.42,0.49,0.18,0.14),(0.43,0.47,0.18,0.14),(0.42,0.46,0.18,0.14),
          (0.44,0.43,0.18,0.14),(0.44,0.41,0.18,0.14),(0.43,0.38,0.19,0.15),(0.44,0.36,0.22,0.15)])
man=K([(0.19,0.25,0.23,0.40),(0.22,0.23,0.20,0.42),(0.20,0.20,0.23,0.44),(0.20,0.18,0.22,0.46),
       (0.19,0.13,0.25,0.49),(0.21,0.09,0.23,0.52),(0.19,0.04,0.24,0.58),(0.19,0.01,0.25,0.59)])
c={"mediaId":7949,"level":"B","keyWord":"prejudice","defaultVoice":"female",
 "taps":[{"phrase":"to clutch a tiny dog","target":"the woman in lilac","voice":"female","keys":woman},
  {"phrase":"to perch on a dog's head","target":"the kitten","voice":"female","keys":kitten},
  {"phrase":"to grip a dog's lead","target":"the man","voice":"male","keys":man}],
 "stillS":2.7,
 "nouns":[{"word":"blossom","x":0.15,"y":0.12,"voice":"female"},
  {"word":"a block of flats","x":0.78,"y":0.25,"voice":"female"},
  {"word":"a kitten","x":0.52,"y":0.47,"voice":"female"},
  {"word":"a rottweiler","x":0.30,"y":0.68,"voice":"female"}],
 "question":"What is the kitten standing on?",
 "answer":["It","is","standing","on","the","rottweiler's","head."],
 "answerVoice":"female",
 "notes":"key word 'prejudice' is abstract, not used as a noun; lilac woman leaves at 2.2 (only a sleeve sliver at the right edge, marked off); kitten box squeezed between man and lilac woman at 0.2."}
json.dump(c,open("content/7949.json","w"),indent=1)
