import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) if r else dict(t=t,off=True) for t,r in zip(T,rows)]
woman=K([(0.36,0.20,0.58,0.66),(0.36,0.20,0.58,0.66),(0.37,0.20,0.57,0.66),(0.36,0.20,0.58,0.66),
         (0.39,0.18,0.59,0.70),(0.40,0.18,0.60,0.70),(0.45,0.29,0.55,0.67),(0.48,0.29,0.52,0.67)])
paint=K([(0.0,0.17,0.35,0.65),(0.0,0.17,0.35,0.65),(0.0,0.15,0.36,0.70),(0.0,0.15,0.35,0.68),
         (0.0,0.14,0.38,0.70),(0.0,0.17,0.39,0.68),(0.0,0.13,0.44,0.72),(0.0,0.13,0.47,0.72)])
d={"mediaId":6903,"level":"B","keyWord":"bring out","defaultVoice":"female",
 "taps":[{"phrase":"to wipe grime off a canvas","target":"the woman","voice":"female","keys":woman},
         {"phrase":"to grip a small glass jar","target":"the woman","voice":"female","keys":woman},
         {"phrase":"to rest on a wooden easel","target":"the painting","voice":"female","keys":paint}],
 "stillS":0.7,
 "nouns":[{"word":"a painting","x":0.20,"y":0.55,"voice":"female"},
          {"word":"an easel","x":0.20,"y":0.10,"voice":"female"},
          {"word":"cotton swabs","x":0.45,"y":0.90,"voice":"female"},
          {"word":"a colour chart","x":0.88,"y":0.90,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","wiping","grime","off","the","painting."],
 "answerVoice":"female",
 "notes":"Woman's working hand reaches over the painting; split the boxes at the painting's right edge, so taps on her hand count for the painting. Painting phrase is a state (no action fits it alone). Background restorers too small/hidden to use."}
json.dump(d,open("content/6903.json","w"),indent=1)
