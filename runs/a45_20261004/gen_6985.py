import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows):
    return [{"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]} for t,r in zip(T,rows)]
cook=K([(0.05,0.22,0.92,0.48),(0.28,0.32,0.48,0.55),(0.28,0.40,0.47,0.50),(0.02,0.38,0.96,0.32),
        (0.02,0.20,0.96,0.50),(0.24,0.22,0.54,0.60),(0.24,0.20,0.56,0.62),(0.24,0.24,0.58,0.58)])
pot=K([(0.70,0.70,0.29,0.18),(0.77,0.70,0.23,0.18),(0.75,0.78,0.25,0.15),(0.76,0.70,0.24,0.18),
       (0.76,0.70,0.24,0.18),(0.80,0.70,0.20,0.17),(0.82,0.70,0.18,0.17),(0.82,0.70,0.18,0.17)])
d={"mediaId":6985,"level":"B","keyWord":"cook from scratch","defaultVoice":"male",
 "taps":[
  {"phrase":"to toss noodles into the air","target":"the cook","voice":"male","keys":cook},
  {"phrase":"to stretch the noodles apart","target":"the cook","voice":"male","keys":cook},
  {"phrase":"to steam on a camping stove","target":"the pot","voice":"male","keys":pot}],
 "stillS":2.7,
 "nouns":[{"word":"string lights","x":0.20,"y":0.24,"voice":"male"},
          {"word":"a cutting board","x":0.46,"y":0.85,"voice":"male"},
          {"word":"a camping stove","x":0.87,"y":0.86,"voice":"male"},
          {"word":"tomatoes","x":0.18,"y":0.93,"voice":"male"}],
 "question":"What is the cook doing?",
 "answer":["He","is","stretching","the","noodles","apart."],
 "answerVoice":"male",
 "notes":"Key word 'cook from scratch' is a phrase, not a placeable noun. The cook's box stops above the pot (y .70) in the wide-arm frames, so his legs are outside it. Steam from the pot is faint (clearest at 0.7 and 2.2 s). The friends and the dog all watch, so no unique phrase fit them."}
json.dump(d,open('content/6985.json','w'),indent=1)
