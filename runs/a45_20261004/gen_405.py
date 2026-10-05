import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
Y={0.5:(0.17,0.36,0.50,0.64),1.0:(0.02,0.33,0.86,0.67),1.5:(0.02,0.25,0.98,0.75),2.0:(0.04,0.21,0.94,0.79),2.5:(0.09,0.15,0.84,0.85),
   6.5:(0.29,0.32,0.21,0.16),7.0:(0.24,0.31,0.27,0.20),7.5:(0.30,0.32,0.24,0.14),8.0:(0.38,0.30,0.18,0.14),
   8.5:(0.33,0.33,0.12,0.14),9.0:(0.33,0.35,0.11,0.14),9.5:(0.34,0.35,0.11,0.14),10.0:(0.35,0.36,0.11,0.14)}
B={5.5:(0.17,0.40,0.19,0.52),6.0:(0.22,0.39,0.40,0.61),6.5:(0.40,0.48,0.52,0.52),7.0:(0.40,0.51,0.52,0.49),7.5:(0.37,0.46,0.37,0.54),
   8.0:(0.36,0.44,0.33,0.48),8.5:(0.46,0.37,0.19,0.48),9.0:(0.45,0.38,0.18,0.52),9.5:(0.46,0.38,0.18,0.50),10.0:(0.47,0.38,0.14,0.40)}
C={3.0:(0.39,0.37,0.45,0.63),3.5:(0.58,0.39,0.42,0.61),4.0:(0.63,0.37,0.37,0.63),4.5:(0.66,0.37,0.34,0.63),
   5.5:(0.37,0.39,0.25,0.61),6.0:(0.63,0.37,0.37,0.63),7.5:(0.75,0.37,0.25,0.63),8.0:(0.70,0.36,0.30,0.58),
   8.5:(0.66,0.36,0.24,0.50),9.0:(0.64,0.38,0.24,0.52),9.5:(0.65,0.38,0.22,0.52),10.0:(0.62,0.38,0.22,0.40)}
c={"mediaId":405,"level":"A","keyWord":"inside","defaultVoice":"male",
 "taps":[
  {"phrase":"to come inside first","target":"the woman in the yellow coat","voice":"female","keys":keys(Y)},
  {"phrase":"to carry a hot pot","target":"the woman with the pot","voice":"female","keys":keys(B)},
  {"phrase":"to have very short hair","target":"the woman with short hair","voice":"female","keys":keys(C)}],
 "stillS":10.0,
 "nouns":[{"word":"a lamp","x":0.58,"y":0.22,"voice":"male"},{"word":"a window","x":0.82,"y":0.42,"voice":"male"},
          {"word":"a fire","x":0.17,"y":0.60,"voice":"male"},{"word":"a table","x":0.82,"y":0.71,"voice":"male"}],
 "question":"What are the people doing?",
 "answer":["They","are","coming","inside","from","the","snow."],
 "answerVoice":"male",
 "notes":"Six or seven people, many cuts, the group stands close together at the end. Mixed group -> default voice by evenId (male). The woman in the yellow coat (red hair) comes in first at 0.5-2.5; from 6.5 she is behind the others and from 8.5 only her face shows, so her box there is kept small (about 0.11 x 0.14, under the usual minimum) to stay on her face and off the two women in grey hats beside her. 'to carry a hot pot' = the blond woman with the steaming pot (5.5: she is in the door, pot not yet in view); weak spot: at 6.5-7.0 the woman in the yellow coat also holds a pot (no steam). 'to have very short hair' is a state: her wood is not unique (the woman in the grey hat carries a piece of wood too). 5.0 = another person in a black hat shuts the door -> all off. At 5.5 the short-haired woman's wood reaches into the blond woman's box (split between their heads). 6.5-7.0 the short-haired woman is almost out of the picture on the right -> off. The key word is an adverb: it is in phrase 1 and the answer."}
json.dump(c,open('content/405.json','w'),indent=1)
