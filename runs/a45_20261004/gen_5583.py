from gen_5581_5582_5583_5584_w import write
S=[(0.19,0.07,0.51,0.47),(0.18,0.12,0.53,0.39),(0.14,0.13,0.56,0.41),(0.13,0.03,0.59,0.59),(0.12,0.39,0.50,0.33),(0.25,0.26,0.37,0.40),(0.36,0.33,0.27,0.31),(0.13,0.19,0.47,0.29)]
B=[(0.70,0.06,0.22,0.26),(0.71,0.09,0.21,0.24),(0.70,0.11,0.24,0.25),(0.72,0.08,0.28,0.26),None,None,None,(0.71,0.01,0.29,0.46)]
write({"mediaId":5583,"level":"A","keyWord":"attempt","defaultVoice":"male",
"taps":[
 {"phrase":"to jump into the pool","target":"the man in white","voice":"male","boxes":S},
 {"phrase":"to ride up the wall","target":"the man in white","voice":"male","boxes":S},
 {"phrase":"to watch from the edge","target":"the man in blue","voice":"male","boxes":B}],
"stillS":3.2,
"nouns":[{"word":"trees","x":0.60,"y":0.06,"voice":"male"},
 {"word":"a fence","x":0.30,"y":0.15,"voice":"male"},
 {"word":"a man","x":0.50,"y":0.45,"voice":"male"},
 {"word":"a pool","x":0.20,"y":0.62,"voice":"male"}],
"question":"What is the man in white doing?",
"answer":["He","is","jumping","into","the","pool."],
"answerVoice":"male",
"notes":"0.2-1.7 s: white-shirt skater's raised hand/board tip reaches into the blue-shirt man's area; skater box stops at x~0.70-0.72 so boxes do not overlap. Blue man off 2.2-3.2 (other shot). Skateboards skipped as noun (three visible)."})
