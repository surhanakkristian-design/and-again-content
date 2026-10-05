import json
T=[i*0.5 for i in range(25)]
def keys(lst):
    return [{"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,lst)]
M=[None,(0,.50,.76,.50),(0,.52,.64,.48),(0,0,.64,1.0),(0,.06,.72,.94),(0,.10,.74,.90),
   (0,.10,.66,.90),(0,.10,.68,.90),(0,.03,.62,.97),(0,0,.62,1.0),(0,0,.66,1.0),(0,.28,.88,.72),
   (0,.24,.86,.76),(0,.26,.86,.50),(0,.36,.46,.56),(0,.40,.44,.42),(0,.56,.18,.16),(0,.50,.56,.50),
   (0,0,.66,1.0),(0,.03,.72,.97),(.18,.10,.55,.90),(.22,.12,.48,.88),(.22,.14,.48,.86),(.23,.13,.49,.87),(.24,.13,.48,.87)]
L=[None]*20+[(0,.20,.18,.14),(.04,.21,.18,.14),(.04,.23,.18,.14),(.05,.23,.18,.14),(.06,.23,.18,.14)]
c={"mediaId":5049,"level":"A","keyWord":"close","defaultVoice":"male",
 "taps":[
  {"phrase":"to lock his bike","target":"the man","voice":"male","keys":keys(M)},
  {"phrase":"to close the door","target":"the man","voice":"male","keys":keys(M)},
  {"phrase":"to shine near the door","target":"the lamp","voice":"male","keys":keys(L)}],
 "stillS":2.5,
 "nouns":[{"word":"a man","x":0.22,"y":0.25,"voice":"male"},
          {"word":"trees","x":0.58,"y":0.08,"voice":"male"},
          {"word":"a lock","x":0.68,"y":0.53,"voice":"male"},
          {"word":"a gate","x":0.84,"y":0.80,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","locking","his","bike."],
 "answerVoice":"male",
 "notes":"Montage: gate padlock (0.0-2.5), bike rack (3.0-6.5), front door at dusk (7.0-12.0). Man off at 0.0 (only the padlock), only hands at 0.5-1.0 and 5.5-8.5. 'to close the door' is weakest: he turns the key and holds the handle at 9.0-12.0, the door pull itself is not very visible. Lamp only at 10.0-12.0; man box starts right of the lamp there, so his left shoulder is cut out."}
json.dump(c,open('content/5049.json','w'),indent=1)
