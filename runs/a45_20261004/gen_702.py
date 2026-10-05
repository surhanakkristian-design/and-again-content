import json
T=[i*0.5 for i in range(17)]
W=[(0,0,.38,.44),(0,0,.38,.44),(0,0,.65,.70),(0,0,.95,.82),(0,0,.97,.82),(0,0,1,.82),(.08,0,.86,.93),(.08,0,.88,.93),(0,0,1,.83),(.13,0,.87,.82),(0,0,1,.92),(.14,0,.80,.96),(.18,0,.68,.64),(.33,.21,.46,.60),(.24,.24,.50,.76),(0,.22,1,.78),(.07,.05,.86,.95)]
keys=[{"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,W)]
c={"mediaId":702,"level":"A","keyWord":"sneakers","defaultVoice":"female",
"taps":[{"phrase":p,"target":"the woman","voice":"female","keys":keys} for p in ["to put on her sneakers","to tie her shoes","to jump up the stairs"]],
"stillS":3.0,
"nouns":[{"word":"sneakers","x":.45,"y":.68,"voice":"female"},{"word":"socks","x":.47,"y":.47,"voice":"female"},{"word":"legs","x":.50,"y":.20,"voice":"female"},{"word":"the sky","x":.82,"y":.10,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","putting","on","her","sneakers."],"answerVoice":"female",
"notes":"Only one target (the woman); 0.0-0.5 s show only her leg and sock, 1.5-5.5 s mostly legs/hands. She puts the sneakers on 1.0-1.5 s, ties them 2.0-2.5 s, jumps on the stairs 5.5-7.0 s. 'socks' pill is small and sits just above the sneakers pill (0.21 apart in y)."}
json.dump(c,open('content/702.json','w'),indent=1)
