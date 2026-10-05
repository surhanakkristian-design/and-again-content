import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) for t,r in zip(T,rows)]
pian=K([(0.25,0.37,0.25,0.31),(0.25,0.38,0.24,0.30),(0.25,0.41,0.25,0.30),(0.25,0.42,0.25,0.31),
        (0.25,0.46,0.25,0.30),(0.25,0.48,0.25,0.30),(0.25,0.51,0.25,0.29),(0.21,0.45,0.29,0.35)])
cat=K([(0.51,0.35,0.18,0.15),(0.51,0.36,0.18,0.15),(0.51,0.38,0.18,0.16),(0.51,0.44,0.19,0.14),
       (0.51,0.48,0.18,0.14),(0.51,0.49,0.18,0.14),(0.51,0.50,0.18,0.14),(0.51,0.51,0.18,0.14)])
bag=K([(0.56,0.13,0.18,0.15),(0.56,0.15,0.18,0.15),(0.56,0.17,0.18,0.15),(0.56,0.20,0.18,0.15),
       (0.55,0.23,0.18,0.15),(0.55,0.25,0.18,0.15),(0.55,0.27,0.18,0.15),(0.55,0.27,0.18,0.15)])
d={"mediaId":7282,"level":"B","keyWord":"landing","defaultVoice":"male",
 "taps":[{"phrase":"to play a grand piano","target":"the man at the piano","voice":"male","keys":pian},
         {"phrase":"to stroll along the piano","target":"the cat","voice":"male","keys":cat},
         {"phrase":"to hold up a baguette","target":"the man with the baguette","voice":"male","keys":bag}],
 "stillS":2.2,
 "nouns":[{"word":"a window","x":0.12,"y":0.35,"voice":"male"},
          {"word":"a grand piano","x":0.76,"y":0.44,"voice":"male"},
          {"word":"a cat","x":0.58,"y":0.54,"voice":"male"},
          {"word":"a landing","x":0.47,"y":0.76,"voice":"male"}],
 "question":"Where is the grand piano?",
 "answer":["It","is","standing","on","the","wooden","landing."],
 "answerVoice":"male",
 "notes":"Pianist and cat are close: split at x 0.51 (pianist's hands on the keys are partly outside his box). Clapping and dozing were avoided because two men on the left both do it. The baguette man leans over the upper banister; neighbours with coffee cups are nearby but hold no baguette."}
json.dump(d,open("content/7282.json","w"),indent=1)
