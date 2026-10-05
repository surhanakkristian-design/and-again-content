import json
VID=5371
T=[i*0.5 for i in range(25)]
def K(d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in T]
G={0.0:(0,0.27,0.47,0.73),0.5:(0,0.28,0.53,0.72),1.0:(0,0.28,0.5,0.72),1.5:(0,0.28,0.55,0.72),2.0:(0,0.29,0.5,0.71),
   2.5:(0,0.42,1,0.58),3.0:(0,0.42,1,0.58),3.5:(0,0.42,1,0.58),4.0:(0.03,0.43,0.95,0.57),4.5:(0.05,0.47,0.93,0.53),
   5.0:(0.1,0.56,0.8,0.44),5.5:(0.1,0.7,0.85,0.3),6.0:(0.15,0.82,0.75,0.18),
   8.5:(0,0.32,1,0.68),9.0:(0,0.32,1,0.68),9.5:(0,0.3,1,0.7),10.0:(0,0.3,1,0.7),10.5:(0,0.32,1,0.68),11.0:(0,0.33,1,0.67),11.5:(0,0.33,1,0.67),12.0:(0,0.35,1,0.65)}
P={0.0:(0.47,0,0.48,1),0.5:(0.53,0,0.45,1),1.0:(0.5,0,0.5,1),1.5:(0.55,0,0.45,1),2.0:(0.5,0,0.5,1),
   2.5:(0.38,0,0.36,0.42),3.0:(0.38,0,0.3,0.42),3.5:(0.38,0,0.36,0.42),4.0:(0.38,0,0.34,0.43),4.5:(0.38,0,0.32,0.47),
   5.0:(0.38,0,0.3,0.56),5.5:(0.35,0,0.33,0.7),6.0:(0.36,0,0.28,0.82),
   6.5:(0.35,0,0.3,1),7.0:(0.37,0,0.28,1),7.5:(0.35,0,0.3,1),8.0:(0.38,0,0.3,1),
   8.5:(0.6,0,0.3,0.32),9.0:(0.45,0,0.32,0.32),9.5:(0.4,0,0.28,0.3),10.0:(0.33,0,0.27,0.3),10.5:(0.3,0,0.28,0.32),
   11.0:(0.33,0,0.25,0.33),11.5:(0.35,0,0.25,0.33),12.0:(0.33,0,0.27,0.35)}
c={"mediaId":VID,"level":"B","keyWord":"a garland","defaultVoice":"female",
 "taps":[
  {"phrase":"to push the pole upright","target":"the young women","voice":"female","keys":K(G)},
  {"phrase":"to dance in a circle","target":"the young women","voice":"female","keys":K(G)},
  {"phrase":"to be wrapped in leaves","target":"the pole","voice":"female","keys":K(P)}],
 "stillS":2.0,
 "nouns":[{"word":"a garland","x":0.15,"y":0.36,"voice":"female"},
          {"word":"a ribbon","x":0.62,"y":0.45,"voice":"female"},
          {"word":"a lake","x":0.9,"y":0.56,"voice":"female"},
          {"word":"a birch pole","x":0.65,"y":0.9,"voice":"female"}],
 "question":"What are the young women doing?",
 "answer":["They","are","dancing","around","the","decorated","pole."],
 "answerVoice":"female",
 "notes":"The woman who ties the ribbon (0-2.0) is also among the pushers/dancers and hard to track, so the people are one group target ('the young women'); at 0-2.0 the group box is just her. The pole box is split from the group at the women's head line (pole above, women below), so the lower pole between the women falls in the group box at 2.5-6.0 and 8.5-12.0; at 0-2.0 split vertically at her hands. Group off at 6.5-8.0 (pole only; a tiny head at the bottom edge at 8.0 ignored). 'a garland' pill sits on her flower crown (a wreath worn on the head); the leaves on the pole could also be called a garland - check whether the key word was meant for the crown or the pole wrapping."}
json.dump(c,open(f'content/{VID}.json','w'),indent=1)
