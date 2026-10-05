import json
T=[i*0.5 for i in range(21)]
def keys(lst):
    return [{"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,lst)]
W=[(.30,.16,.55,.84),(.33,.21,.60,.70),(.28,.09,.66,.76),(.32,.09,.55,.66),(.18,.14,.56,.64),(.32,.20,.40,.58),
   (.35,.12,.33,.60),(.34,.17,.45,.53),(.34,.31,.48,.45),(.38,.19,.46,.48),(.24,.45,.62,.28),(.24,.37,.66,.36),
   (.30,.24,.62,.42),(.34,.10,.47,.60),(.36,.23,.46,.49),(.28,.26,.46,.50),(.24,.12,.50,.62),(.28,.13,.44,.62),
   (.35,.30,.36,.42),(.38,.32,.32,.36),(.36,.29,.36,.42)]
c={"mediaId":5051,"level":"B","keyWord":"lose","defaultVoice":"female",
 "taps":[
  {"phrase":"to tip out her backpack","target":"the young woman","voice":"female","keys":keys(W)},
  {"phrase":"to search under the bunk","target":"the young woman","voice":"female","keys":keys(W)},
  {"phrase":"to rummage through her clothes","target":"the young woman","voice":"female","keys":keys(W)}],
 "stillS":3.0,
 "nouns":[{"word":"a bunk bed","x":0.16,"y":0.20,"voice":"female"},
          {"word":"a window","x":0.69,"y":0.20,"voice":"female"},
          {"word":"a backpack","x":0.68,"y":0.75,"voice":"female"},
          {"word":"a heap of clothes","x":0.28,"y":0.88,"voice":"female"}],
 "question":"What is the young woman doing?",
 "answer":["She","is","rummaging","through","her","clothes."],
 "answerVoice":"female",
 "notes":"Only one person, so all three phrases target the young woman (the backpack only moves in her hands). Her box includes the backpack when she holds it. 'to tip out her backpack' 0.0-0.5, 'to rummage through her clothes' 1.0 and 4.0-4.5, 'to search under the bunk' 5.0-5.5 (lifts the mattress edge of the lower bunk). Window pill sits on the right window pane next to her head."}
json.dump(c,open('content/5051.json','w'),indent=1)
