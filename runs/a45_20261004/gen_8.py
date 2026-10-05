import json
def b(t,x,y,w,h): return {"t":t,"x":x,"y":y,"w":w,"h":h}
def off(t): return {"t":t,"off":True}
T=[i*0.5 for i in range(17)]
W={0.0:(.18,.23,.54,.65),0.5:(.18,.23,.54,.65),1.0:(.03,.52,.84,.48),2.0:(0,.44,.34,.37),2.5:(0,.04,1,.96),3.0:(0,.06,1,.94),
   3.5:(0,.50,.62,.24),4.0:(0,.49,.57,.25),4.5:(0,.61,.30,.18),5.0:(0,.04,.72,.96),6.5:(.53,.47,.22,.28),7.0:(.28,.38,.47,.40),7.5:(.28,.32,.47,.42)}
R={1.5:(.32,.12,.62,.80),2.0:(.34,.12,.60,.82)}
for t in T:
    if t>=3.5: R[t]=(.76,.38,.22,.42)
D={3.5:(.12,0,.64,.50),4.0:(.20,0,.56,.49),4.5:(.18,0,.58,.61),5.5:(.20,0,.56,1),6.0:(.20,0,.56,1),6.5:(.18,0,.35,1),7.0:(.15,0,.60,.38),7.5:(.15,0,.60,.32),8.0:(.20,0,.56,1)}
k=lambda M:[b(t,*M[t]) if t in M else off(t) for t in T]
c={"mediaId":8,"level":"B","keyWord":"keycard","defaultVoice":"female",
"taps":[{"phrase":"to wheel a suitcase","target":"the woman","voice":"female","keys":k(W)},
 {"phrase":"to light up green","target":"the card reader","voice":"female","keys":k(R)},
 {"phrase":"to swing open","target":"the door","voice":"female","keys":k(D)}],
"stillS":6.0,
"nouns":[{"word":"a door","x":0.40,"y":0.28,"voice":"female"},{"word":"a card reader","x":0.84,"y":0.50,"voice":"female"},
 {"word":"a keycard","x":0.69,"y":0.61,"voice":"female"},{"word":"a handle","x":0.47,"y":0.69,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","unlocking","the","door","with","a","keycard."],
"answerVoice":"female",
"notes":"Anime clip with many cuts and continuity glitches (card floats on the reader without a hand at 5.5/6.0, door open/closed alternates). 'to swing open' needs 3 words only (to + verb + particle) - check the 3-5 word rule. In close-ups only her hand/arm is visible: I boxed the hand as 'the woman' (1.0, 2.0, 3.5-4.5, 6.5-7.5); where the arm lies over the door, the door box is only the part above the arm. Door is 'off' at 5.0 (she stands in the doorway) and in the corridor shots (many doors). The reader is red at 2.0 and green from 3.5. Still 6.0: keycard and handle pills are close (0.08 in y)."}
json.dump(c,open('content/8.json','w'),indent=1)
