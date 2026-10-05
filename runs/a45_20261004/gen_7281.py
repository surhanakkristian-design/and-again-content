import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) for t,r in zip(T,rows)]
worker=K([(0.13,0.25,0.46,0.60),(0.10,0.25,0.48,0.60),(0.01,0.24,0.50,0.61),(0.02,0.23,0.50,0.62),
          (0.07,0.22,0.48,0.64),(0.07,0.22,0.49,0.64),(0.05,0.22,0.50,0.64),(0.05,0.21,0.51,0.65)])
metal=K([(0.60,0.66,0.33,0.20),(0.59,0.66,0.35,0.22),(0.52,0.66,0.42,0.22),(0.53,0.66,0.42,0.22),
         (0.56,0.66,0.39,0.24),(0.57,0.66,0.38,0.24),(0.56,0.66,0.39,0.26),(0.58,0.66,0.38,0.28)])
furn=K([(0.75,0.21,0.25,0.44)]*8)
d={"mediaId":7281,"level":"B","keyWord":"lance","defaultVoice":"male",
 "taps":[{"phrase":"to grip a long lance","target":"the worker in front","voice":"male","keys":worker},
         {"phrase":"to spit out sparks","target":"the furnace","voice":"male","keys":furn},
         {"phrase":"to pour into a channel","target":"the molten metal","voice":"male","keys":metal}],
 "stillS":2.2,
 "nouns":[{"word":"a face shield","x":0.42,"y":0.29,"voice":"male"},
          {"word":"a furnace","x":0.88,"y":0.42,"voice":"male"},
          {"word":"a lance","x":0.62,"y":0.64,"voice":"male"},
          {"word":"molten metal","x":0.62,"y":0.81,"voice":"male"}],
 "question":"What is the worker in front gripping?",
 "answer":["He","is","gripping","a","long","metal","lance."],
 "answerVoice":"male",
 "notes":"Sparks burst from the furnace top only in 0.2-1.2 s; the furnace box stays on it all clip. Molten-metal box covers the tap stream and the right part of the channel; the left end of the channel runs under the worker's feet and is left to the worker box (split at the worker's right edge). A second worker stands far left in the background (not a target)."}
json.dump(d,open("content/7281.json","w"),indent=1)
