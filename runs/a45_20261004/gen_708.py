import json
T=[i*0.5 for i in range(15)]
M=[(.38,0,.62,.66),(.26,0,.74,.69),(.24,0,.76,.77),(.23,0,.77,.78),(.18,0,.82,.71),(.18,0,.82,.84),(.11,0,.89,.85),(.18,0,.82,.87),(.11,0,.89,.76),(.14,0,.86,.84),(0,0,1,1),(.08,0,.92,.95),(0,0,1,1),(0,0,1,1),(0,0,1,1)]
keys=[{"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,M)]
c={"mediaId":708,"level":"A","keyWord":"soap","defaultVoice":"male",
"taps":[{"phrase":p,"target":"the man","voice":"male","keys":keys} for p in ["to pick up the soap","to wash his hands","to look at his hands"]],
"stillS":3.0,
"nouns":[{"word":"soap","x":.60,"y":.84,"voice":"male"},{"word":"a tap","x":.14,"y":.34,"voice":"male"},{"word":"a bubble","x":.34,"y":.12,"voice":"male"},{"word":"hands","x":.42,"y":.58,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","washing","his","hands","with","soap."],"answerVoice":"male",
"notes":"One target only (the man) for all three phrases: the soap is inside his hands at 0.5-1.0 s and the bubble floats in front of his shirt at 3.5-6.5 s, so neither can have a box that does not overlap his; the tap is crossed by his arm at 5.0 s. Until 5.5 s only his arms, hands and shirt are visible, the face from 6.0 s. He picks up the soap 0.0-0.5 s, washes 1.0-5.5 s, looks at his clean hands 6.0-7.0 s. 'hands' pill sits on the foam-covered hands; a second, tiny bubble is at (0.35, 0.33), the 'a bubble' pill is on the big one."}
json.dump(c,open('content/708.json','w'),indent=1)
