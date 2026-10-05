from gen_7075_7076_7077_7079_w import write
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
W=[(0.18,0.00,0.49,0.95),(0.00,0.00,0.64,0.88),(0.00,0.00,0.62,0.92),(0.00,0.00,0.62,0.86),(0.00,0.04,0.62,0.78),(0.00,0.08,0.63,0.70),(0.00,0.13,0.63,0.72),(0.00,0.13,0.63,0.72)]
M=[(0.67,0.35,0.20,0.19),(0.64,0.35,0.20,0.20),(0.62,0.36,0.20,0.22),(0.62,0.36,0.20,0.22),(0.62,0.36,0.20,0.20),(0.63,0.36,0.20,0.20),(0.63,0.37,0.20,0.20),(0.63,0.37,0.20,0.20)]
d={"mediaId":7076,"level":"B","keyWord":"edge","defaultVoice":"female",
"taps":[
 {"phrase":"to walk along the edge","target":"the woman","voice":"female","boxes":W},
 {"phrase":"to stretch out her arms","target":"the woman","voice":"female","boxes":W},
 {"phrase":"to gesture towards the woman","target":"the man in the hat","voice":"male","boxes":M}],
"stillS":2.2,
"nouns":[{"word":"a canvas tent","x":0.76,"y":0.43,"voice":"female"},
 {"word":"flamingos","x":0.16,"y":0.47,"voice":"female"},
 {"word":"gravel","x":0.78,"y":0.74,"voice":"female"},
 {"word":"an edge","x":0.50,"y":0.90,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","walking","along","the","edge."],
"answerVoice":"female",
"notes":"The woman's box is cut at x~0.63 so it does not overlap the small man in the hat behind her: her right arm (out to x~0.98) lies outside her box. Man in the hat points at her from 1.2 on (at 0.2/0.7 he just stands). The second man by the car is not used. 'an edge' pill sits on the salt/gravel line."}
write(d,T)
