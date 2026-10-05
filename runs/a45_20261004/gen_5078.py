import json,os
H=os.path.dirname(os.path.abspath(__file__))
def keys(times,d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in times]
T=[i*0.5 for i in range(25)]
cook={0.0:(0.02,0.20,0.62,0.62),0.5:(0.0,0.19,0.68,0.64),1.0:(0.0,0.19,0.66,0.65),1.5:(0.0,0.19,0.65,0.65),2.0:(0.0,0.19,0.64,0.66),2.5:(0.0,0.05,0.70,0.80),
 3.0:(0.0,0.0,0.48,0.48),3.5:(0.0,0.0,1.0,0.50),4.0:(0.0,0.0,1.0,0.63),4.5:(0.0,0.0,0.51,0.62),5.0:(0.0,0.17,1.0,0.46),5.5:(0.0,0.0,0.44,0.68),
 6.0:(0.0,0.0,0.80,0.45),6.5:(0.0,0.0,0.86,0.40),7.0:(0.44,0.0,0.40,0.18),7.5:(0.0,0.0,0.92,0.80),8.0:(0.0,0.04,1.0,0.93),8.5:(0.08,0.12,0.70,0.50),
 9.0:(0.13,0.15,0.55,0.53),9.5:(0.08,0.05,0.65,0.56),10.0:(0.10,0.09,0.63,0.52),10.5:(0.14,0.23,0.58,0.37),11.0:(0.0,0.20,0.86,0.42),11.5:(0.08,0.23,0.92,0.37),12.0:(0.0,0.25,1.0,0.31)}
beard={3.0:(0.49,0.0,0.29,0.30),4.5:(0.52,0.0,0.25,0.29),5.0:(0.40,0.0,0.30,0.16),5.5:(0.45,0.0,0.19,0.27)}
ck=keys(T,cook)
c={"mediaId":5078,"level":"B","keyWord":"pork","defaultVoice":"male",
"taps":[
 {"phrase":"to carve the roast pork","target":"the cook","voice":"male","keys":ck},
 {"phrase":"to squeeze a lime","target":"the cook","voice":"male","keys":ck},
 {"phrase":"to have a bushy beard","target":"the bearded man","voice":"male","keys":keys(T,beard)}],
"stillS":9.0,
"nouns":[{"word":"pork","x":0.90,"y":0.41,"voice":"male"},{"word":"an apron","x":0.42,"y":0.50,"voice":"male"},
 {"word":"a lime","x":0.10,"y":0.66,"voice":"male"},{"word":"tacos","x":0.50,"y":0.80,"voice":"male"}],
"question":"What is the cook doing?","answer":["He","is","carving","slices","of","roast","pork."],"answerVoice":"male",
"notes":"Cook carves the spit 0.0-2.5, then close-ups (3.0-7.0) show only his arm/hands/cleaver; at 7.0 only his hand dropping onion at the top. Squeezes a lime 9.5-11.0. The bearded man (customer in black shirt, glasses) is only in the background of the close-ups 3.0, 4.5-5.5, partly hidden by the cook's arm; boxes split there, so the cook's box loses the cleaver's right part at 4.5/5.5 and his upper arm at 5.0. A similar bearded figure at the left edge at 7.0 is marked off (unclear). Bearded phrase is a state (no action fits only him). 11.5-12.0: customers' hands grab tacos at the bottom, kept out of the cook box."}
json.dump(c,open(f"{H}/content/5078.json","w"),indent=1)
