import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
W={0.2:(.70,.17,.30,.76),0.7:(.70,.17,.30,.72),1.2:(.70,.17,.30,.74),1.7:(.70,.18,.30,.74),
   2.2:(.55,.25,.45,.60),2.7:(.58,.25,.42,.70),3.2:(.60,.25,.40,.74),3.7:(.60,.24,.40,.76)}
A={0.2:(.44,.58,.26,.42),0.7:(.44,.59,.26,.41),1.2:(.44,.60,.26,.40),1.7:(.44,.62,.26,.38),2.2:(.44,.85,.28,.15)}
k=lambda t,v:{"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]} if v else {"t":t,"off":True}
wk=[k(t,W[t]) for t in T]; ak=[k(t,A.get(t)) for t in T]
c={"mediaId":5677,"level":"B","keyWord":"bowling","defaultVoice":"female",
 "taps":[{"phrase":"to raise both arms in triumph","target":"the woman","voice":"female","keys":wk},
  {"phrase":"to point down the lane","target":"the hand","voice":"female","keys":ak},
  {"phrase":"to turn around in surprise","target":"the woman","voice":"female","keys":wk}],
 "stillS":3.2,
 "nouns":[{"word":"a neon sign","x":0.65,"y":0.22,"voice":"female"},{"word":"pins","x":0.71,"y":0.34,"voice":"female"},
  {"word":"a gutter","x":0.14,"y":0.62,"voice":"female"},{"word":"a bowling lane","x":0.42,"y":0.70,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","raising","both","arms","in","triumph."],"answerVoice":"female",
 "notes":"Only one person plus a foreground pointing hand (no body), so woman is used for phrases 1 and 3 (raising arms 0.2-1.7, turning around 2.2-3.7). Woman box starts at x .70 in 0.2-1.7 to stay clear of the hand box, so her raised left hand (~.64) is cut slightly. At 2.2 hand box below y .85, woman's shoes cut. The answer describes the first half of the clip; she lowers her arms later. The pins fly at 0.2-0.7 (too small to tap)."}
json.dump(c,open('content/5677.json','w'),indent=1)
