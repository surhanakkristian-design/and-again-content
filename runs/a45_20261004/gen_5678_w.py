import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
WO={0.2:(0,.46,.30,.42),0.7:(0,.48,.32,.40),1.2:(0,.51,.33,.36),1.7:(0,.51,.33,.36),2.2:(0,.50,.33,.36),2.7:(0,.48,.33,.38),3.2:(0,.49,.33,.38),3.7:(0,.43,.34,.45)}
CA={0.2:(.30,.58,.25,.14),0.7:(.32,.57,.22,.14),1.2:(.33,.57,.21,.14),1.7:(.33,.57,.21,.14),2.2:(.33,.57,.21,.14),2.7:(.33,.58,.21,.14),3.2:(.33,.57,.21,.14),3.7:(.34,.58,.22,.14)}
MA={t:(.56,.29,.40,.56) for t in T}; MA[3.7]=(.58,.30,.42,.55)
k=lambda t,v:{"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]}
c={"mediaId":5678,"level":"B","keyWord":"break a promise","defaultVoice":"female",
 "taps":[{"phrase":"to paint her toenails","target":"the woman","voice":"female","keys":[k(t,WO[t]) for t in T]},
  {"phrase":"to frown at his watch","target":"the man","voice":"male","keys":[k(t,MA[t]) for t in T]},
  {"phrase":"to curl up on the sofa","target":"the cat","voice":"female","keys":[k(t,CA[t]) for t in T]}],
 "stillS":0.2,
 "nouns":[{"word":"a floor lamp","x":0.37,"y":0.43,"voice":"female"},{"word":"a cat","x":0.42,"y":0.66,"voice":"female"},
  {"word":"nail polish","x":0.22,"y":0.81,"voice":"female"},{"word":"a coffee table","x":0.36,"y":0.89,"voice":"female"}],
 "question":"What is the man doing?",
 "answer":["He","is","frowning","at","his","watch."],"answerVoice":"male",
 "notes":"Woman and cat sit close: split along x ~.33 (woman left incl. head/body, cat right); the woman's painted foot and hand (x .38-.48, y .70-.78) fall outside both boxes. Man adjusts his cuff at 0.2-0.7 and looks at his watch from 1.2; frown is mild. Key word 'break a promise' is a phrase, not a visible noun."}
json.dump(c,open('content/5678.json','w'),indent=1)
