import json
def keys(times, boxes):
    return [{"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(times,boxes)]
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
cat=[(0.19,0.10,0.36,0.15)]*6+[(0.19,0.11,0.38,0.15),(0.19,0.11,0.30,0.15)]
hens=[(0.82,0.48,0.18,0.17),(0.82,0.50,0.18,0.19),(0.69,0.53,0.31,0.30),(0.53,0.52,0.47,0.30),
      (0.50,0.53,0.48,0.29),(0.52,0.56,0.48,0.31),(0.48,0.30,0.52,0.65),(0.50,0.18,0.50,0.81)]
beans=[(0.13,0.26,0.42,0.53),(0.10,0.26,0.68,0.58),(0.03,0.26,0.65,0.62),(0.03,0.26,0.49,0.62),
       (0.0,0.26,0.49,0.70),(0.0,0.50,0.51,0.50),(0.0,0.76,0.47,0.24),(0.0,0.78,0.49,0.22)]
c={"mediaId":6863,"level":"A","keyWord":"bean","defaultVoice":"male",
 "taps":[
  {"phrase":"to sleep on the bags","target":"the cat","voice":"male","keys":keys(T,cat)},
  {"phrase":"to eat the beans","target":"the hens","voice":"male","keys":keys(T,hens)},
  {"phrase":"to fall onto the floor","target":"the beans","voice":"male","keys":keys(T,beans)}],
 "stillS":1.2,
 "nouns":[{"word":"a cat","x":0.37,"y":0.16,"voice":"male"},
          {"word":"a wheel","x":0.56,"y":0.52,"voice":"male"},
          {"word":"hens","x":0.85,"y":0.68,"voice":"male"},
          {"word":"beans","x":0.30,"y":0.81,"voice":"male"}],
 "question":"What are the hens eating?",
 "answer":["They","are","eating","the","beans."],
 "answerVoice":"male",
 "notes":"No person: defaultVoice male (evenId false). 'the hens' is a group target (two hens; at 3.2-3.7 s one flaps up onto the cart, box covers both). 'the beans' box = falling stream + pile, cut at the hens' box where the hens stand in the pile (left part only from 1.7 s). At 3.7 s the hen's head touches the cat; boxes split at x 0.49/0.50. Beans stop falling after about 2.5 s."}
json.dump(c,open('content/6863.json','w'),indent=1)
