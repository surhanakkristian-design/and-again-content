import json
T=[i*0.5 for i in range(19)]
def keys(lst):
    return [{"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,lst)]
G=[(.14,.30,.86,.70),(.04,.26,.96,.74),(0,.21,1.0,.79),(0,.21,1.0,.79),
   (.40,.74,.34,.26),(.41,.75,.34,.25),(.40,.75,.35,.25),(.43,.76,.33,.24),(.39,.78,.32,.22),(.37,.82,.32,.18),(.38,.84,.30,.16),
   (.22,.35,.60,.65),(.18,.40,.64,.60),(.19,.39,.65,.61),(.19,.38,.64,.62),(.19,.35,.64,.65),(.18,.34,.64,.66),(.20,.34,.64,.66),(.18,.34,.64,.66)]
Y=[None]*4+[(.35,.43,.18,.27),(.34,.45,.18,.27),(.33,.45,.18,.27),(.39,.49,.18,.24),(.38,.48,.22,.27),(.41,.47,.21,.28),(.48,.47,.18,.28)]+[None]*8
c={"mediaId":5050,"level":"B","keyWord":"lose","defaultVoice":"male",
 "taps":[
  {"phrase":"to gasp in horror","target":"the grey-haired man","voice":"male","keys":keys(G)},
  {"phrase":"to bury his face","target":"the grey-haired man","voice":"male","keys":keys(G)},
  {"phrase":"to take down a banner","target":"the young man","voice":"male","keys":keys(Y)}],
 "stillS":8.0,
 "nouns":[{"word":"a bar chart","x":0.58,"y":0.20,"voice":"male"},
          {"word":"balloons","x":0.13,"y":0.60,"voice":"male"},
          {"word":"a tie","x":0.51,"y":0.74,"voice":"male"},
          {"word":"confetti","x":0.80,"y":0.95,"voice":"male"}],
 "question":"What is the grey-haired man doing?",
 "answer":["He","is","burying","his","face","in","his","hands."],
 "answerVoice":"male",
 "notes":"0.0-1.5 close-up of the grey-haired man (mouth open, horrified; the hand on the cane at the bottom is taken as his). 2.0-5.0 hall shot: the grey head seen from behind at the bottom is assumed to be him (same grey hair and dark suit). Young man in a light-blue shirt by the door pulls the banner down at 2.0-5.0; 'take down' is read from the banner sagging and disappearing. 'to bury his face' from 6.0 on. Confetti pill on the floor right of his shoe is the weakest slot."}
json.dump(c,open('content/5050.json','w'),indent=1)
