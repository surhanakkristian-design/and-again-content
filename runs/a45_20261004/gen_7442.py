import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":round(r[0],2),"y":round(r[1],2),"w":round(r[2]-r[0],2),"h":round(r[3]-r[1],2)}) for t,r in zip(T,rows)]
# x0,y0,x1,y1 ; rider top part down to the pony's ears, pony from ears to hooves
ears=[0.43,0.43,0.43,0.41,0.41,0.40,0.37,0.37]
rider=[(0.32,0.30,0.64),(0.32,0.30,0.66),(0.29,0.30,0.63),(0.29,0.28,0.64),(0.28,0.28,0.67),(0.30,0.25,0.67),(0.31,0.26,0.72),(0.31,0.24,0.74)]
pony=[(0.27,0.85,0.69),(0.26,0.86,0.69),(0.25,0.86,0.68),(0.26,0.85,0.70),(0.23,0.91,0.73),(0.24,0.94,0.75),(0.25,0.92,0.77),(0.27,0.97,0.83)]
R=[(a,b,c,e) for (a,b,c),e in zip(rider,ears)]
P=[(a,e,c,b) for (a,b,c),e in zip(pony,ears)]
c={"mediaId":7442,"level":"B","keyWord":"pony","defaultVoice":"female",
 "taps":[{"phrase":"to ride bareback","target":"the young woman","voice":"female","keys":K(R)},
         {"phrase":"to carry a barefoot rider","target":"the pony","voice":"female","keys":K(P)},
         {"phrase":"to grin broadly","target":"the young woman","voice":"female","keys":K(R)}],
 "stillS":2.2,
 "nouns":[{"word":"a cliff","x":0.62,"y":0.08,"voice":"female"},{"word":"a fence","x":0.30,"y":0.27,"voice":"female"},
          {"word":"a pony","x":0.47,"y":0.68,"voice":"female"},{"word":"a river","x":0.82,"y":0.80,"voice":"female"}],
 "question":"What is the young woman doing?",
 "answer":["She","is","riding","a","pony","through","the","river."],"answerVoice":"female",
 "notes":"Only two clear targets (rider + her buckskin); the herd and the tiny people at the fence are not single targets, so the rider takes two phrases. Rider and pony overlap: split at the pony's ears; the rider's legs/feet hang inside the pony box. The animal is called a pony (key word) though the packet says buckskin horse."}
json.dump(c,open('content/7442.json','w'),indent=1)
