import json
T=[i*0.5 for i in range(19)]
def keys(d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} for t in T]
man={0.0:(0.17,0.11,0.83,0.57),0.5:(0.17,0.10,0.83,0.57),1.0:(0.36,0.08,0.64,0.92),1.5:(0.24,0.27,0.76,0.73),
     2.0:(0,0,0.55,0.96),2.5:(0,0,0.48,0.92),3.0:(0.40,0.03,0.60,0.31),3.5:(0.42,0.04,0.58,0.46),
     4.0:(0.22,0.07,0.78,0.44),4.5:(0.08,0,0.92,0.49),5.0:(0,0,1,0.70),5.5:(0,0,1,0.72),6.0:(0,0,0.80,0.72),
     6.5:(0.10,0.05,0.88,0.62),7.0:(0.04,0.10,0.96,0.62),7.5:(0.04,0.10,0.96,0.65),8.0:(0.02,0.10,0.98,0.70),
     8.5:(0.02,0.08,0.98,0.76),9.0:(0,0,1,0.98)}
steak={3.0:(0.08,0.34,0.78,0.28),3.5:(0.08,0.50,0.86,0.20),4.0:(0.06,0.51,0.86,0.19),4.5:(0.26,0.49,0.54,0.15)}
c={"mediaId":4940,"level":"B","keyWord":"butcher","defaultVoice":"male",
 "taps":[
  {"phrase":"to hang sausages on hooks","target":"the butcher","voice":"male","keys":keys(man)},
  {"phrase":"to tie the parcel with string","target":"the butcher","voice":"male","keys":keys(man)},
  {"phrase":"to lie on a brass scale","target":"the steak","voice":"male","keys":keys(steak)}],
 "stillS":7.5,
 "nouns":[{"word":"a butcher","x":0.45,"y":0.40,"voice":"male"},
          {"word":"a parcel","x":0.72,"y":0.67,"voice":"male"},
          {"word":"a display counter","x":0.30,"y":0.80,"voice":"male"},
          {"word":"jars","x":0.85,"y":0.25,"voice":"male"}],
 "question":"What is the butcher doing?",
 "answer":["He","is","wrapping","the","steak","in","brown","paper."],
 "answerVoice":"male",
 "notes":"Only one main person (a customer's face/hand appears at the left/bottom edge at 6.5-8.0 s, not a target). Steak visible 3.0-4.5 s; at 3.0 s the butcher's hands hold it, box split at y 0.34. At 4.5 s steak partly covered by the paper."}
json.dump(c,open('content/4940.json','w'),indent=1)
