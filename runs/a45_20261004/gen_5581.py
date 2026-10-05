from gen_5581_5582_5583_5584_w import write
M=[(0.04,0.43,0.56,0.52)]*8
W=[(0.60,0.26,0.34,0.72)]*8
write({"mediaId":5581,"level":"B","keyWord":"assure","defaultVoice":"male",
"taps":[
 {"phrase":"to kneel on a mat","target":"the man","voice":"male","boxes":M},
 {"phrase":"to check the knot","target":"the man","voice":"male","boxes":M},
 {"phrase":"to rub her hands together","target":"the woman","voice":"female","boxes":W}],
"stillS":0.2,
"nouns":[{"word":"a cliff","x":0.25,"y":0.25,"voice":"male"},
 {"word":"the sky","x":0.75,"y":0.12,"voice":"male"},
 {"word":"a water bottle","x":0.64,"y":0.82,"voice":"male"},
 {"word":"a coil of rope","x":0.17,"y":0.91,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","checking","the","knot","on","her","harness."],
"answerVoice":"male",
"notes":"Man and woman boxes split at x=0.60; woman's clasped hands (x~0.53-0.60, above the man's head) fall in neither box. Key word 'assure' (verb) not a visible noun."})
