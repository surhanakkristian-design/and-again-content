import json
T=[i*0.5 for i in range(19)]
W={0.0:(0,0.07,1,0.93),0.5:(0,0.05,1,0.95),1.0:(0,0.03,1,0.97),1.5:(0,0,1,1),2.0:(0,0,1,1),
   2.5:(0,0,0.66,1),3.0:(0.02,0.27,0.58,0.73),3.5:(0.08,0.18,0.72,0.62),4.0:(0.22,0.13,0.46,0.62),
   4.5:(0.27,0.31,0.57,0.42),5.0:(0.27,0.19,0.36,0.52),5.5:(0.32,0.36,0.58,0.34),
   7.0:(0.34,0.66,0.3,0.34),7.5:(0.4,0.65,0.2,0.3),8.0:(0.4,0.63,0.2,0.28),8.5:(0.41,0.63,0.2,0.27),9.0:(0.4,0.64,0.2,0.26)}
D={2.5:(0.68,0.38,0.32,0.56),3.0:(0.62,0.36,0.3,0.3),4.0:(0,0.39,0.2,0.36),4.5:(0,0.38,0.26,0.36)}
def keys(m):
    return [({"t":t,"off":True} if t not in m else dict(t=t,x=m[t][0],y=m[t][1],w=m[t][2],h=m[t][3])) for t in T]
c={"mediaId":5235,"level":"B","keyWord":"cargo","defaultVoice":"female",
 "taps":[
  {"phrase":"to stamp the shipping documents","target":"the woman","voice":"female","keys":keys(W)},
  {"phrase":"to lift a stamp overhead","target":"the woman","voice":"female","keys":keys(W)},
  {"phrase":"to watch the officer closely","target":"the dockworkers","voice":"male","keys":keys(D)}],
 "stillS":8.0,
 "nouns":[{"word":"a crane","x":0.5,"y":0.2,"voice":"female"},
          {"word":"containers","x":0.85,"y":0.42,"voice":"female"},
          {"word":"crates","x":0.3,"y":0.69,"voice":"female"},
          {"word":"an officer","x":0.5,"y":0.8,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","stamping","the","wooden","cargo","crates."],
 "answerVoice":"female",
 "notes":"Two phrases share the woman (papers 0.0-2.0, stamp raised overhead at 2.5, 3.5, 4.0, 5.0). Woman off at 6.0-6.5 (empty aisle shot). Dockworkers only at 2.5-4.5; off at 3.5 (hidden behind her arm and the stamp). At 3.0 the woman box stops at x 0.60 so the big red stamp on the right is outside it (dockworker box above it). Still 8.0: two forklifts in the picture, so no forklift noun; 'an officer' pill sits on her skirt below the 'crates' pill."}
json.dump(c,open('content/5235.json','w'),indent=1)
