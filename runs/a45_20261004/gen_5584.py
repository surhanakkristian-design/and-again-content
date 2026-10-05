from gen_5581_5582_5583_5584_w import write
Y=[(0.18,0,0.70,0.92),(0.18,0,0.69,0.88),(0.29,0,0.52,0.83),(0.31,0,0.50,0.80),(0.34,0.04,0.42,0.74),(0.35,0.12,0.36,0.68),(0.32,0.19,0.32,0.63),(0.35,0.24,0.28,0.58)]
F=[(0,0.06,0.18,0.22),(0,0.08,0.18,0.22),(0,0.10,0.16,0.22),(0,0.13,0.14,0.21),(0,0.19,0.15,0.18),(0,0.21,0.15,0.18),(0,0.24,0.15,0.20),(0,0.26,0.18,0.20)]
O=[None,None,(0.16,0.12,0.13,0.43),(0.14,0.15,0.17,0.44),(0.15,0.20,0.19,0.43),(0.15,0.23,0.20,0.43),(0.15,0.26,0.17,0.43),(0.18,0.29,0.17,0.42)]
write({"mediaId":5584,"level":"A","keyWord":"attractive","defaultVoice":"female",
"taps":[
 {"phrase":"to walk through the market","target":"the young woman","voice":"female","boxes":Y},
 {"phrase":"to hold a knife","target":"the man in the apron","voice":"male","boxes":F},
 {"phrase":"to carry a brown bag","target":"the older woman","voice":"female","boxes":O}],
"stillS":3.2,
"nouns":[{"word":"sunglasses","x":0.48,"y":0.24,"voice":"female"},
 {"word":"a handbag","x":0.24,"y":0.46,"voice":"female"},
 {"word":"fruit","x":0.86,"y":0.45,"voice":"female"},
 {"word":"an apple","x":0.29,"y":0.75,"voice":"female"}],
"question":"What is the young woman doing?",
"answer":["She","is","walking","through","the","market."],
"answerVoice":"female",
"notes":"Fishmonger and older woman sit at the left edge, narrow; their boxes are split against each other and the young woman's coat, so some are under the 0.18 minimum width. Older woman hidden by the coat at 0.2-0.7 s (off). 'attractive' is an adjective, not used as a noun."})
