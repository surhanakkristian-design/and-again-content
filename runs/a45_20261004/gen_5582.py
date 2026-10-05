from gen_5581_5582_5583_5584_w import write
W=[(0,0.31,0.38,0.38),(0,0.32,0.38,0.37),(0,0.32,0.38,0.37),(0,0.31,0.38,0.38),(0,0.29,0.38,0.38),(0,0.26,0.32,0.40),(0,0.25,0.22,0.45),(0,0.25,0.18,0.45)]
N=[(0.38,0.48,0.18,0.25)]*5+[(0.38,0.48,0.20,0.25),(0.37,0.48,0.25,0.26),(0.37,0.48,0.27,0.26)]
M=[(0.56,0.29,0.44,0.71),(0.56,0.28,0.44,0.72),(0.56,0.28,0.44,0.72),(0.57,0.27,0.43,0.73),(0.58,0.25,0.42,0.75),(0.60,0.23,0.40,0.77),(0.62,0.23,0.38,0.77),(0.66,0.22,0.34,0.78)]
write({"mediaId":5582,"level":"B","keyWord":"attack","defaultVoice":"female",
"taps":[
 {"phrase":"to point her finger at him","target":"the woman in the blazer","voice":"female","boxes":W},
 {"phrase":"to drop his papers","target":"the man","voice":"male","boxes":M},
 {"phrase":"to take notes at a desk","target":"the woman at the desk","voice":"female","boxes":N}],
"stillS":3.2,
"nouns":[{"word":"the ceiling","x":0.50,"y":0.13,"voice":"female"},
 {"word":"wood panelling","x":0.58,"y":0.45,"voice":"female"},
 {"word":"a desk","x":0.48,"y":0.62,"voice":"female"},
 {"word":"a parquet floor","x":0.45,"y":0.88,"voice":"female"}],
"question":"What is the standing woman doing?",
"answer":["She","is","pointing","her","finger","at","him."],
"answerVoice":"female",
"notes":"Pointing woman's outstretched hand (x 0.40-0.52) overlaps the note-taker in the picture; her box stops at x 0.38 so the boxes do not overlap. Papers fall only 0.2-1.7 s. She stops pointing at ~2.5 s. Chandeliers/portraits/lecterns skipped as nouns (more than one each)."})
