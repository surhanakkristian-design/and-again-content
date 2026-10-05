import json
B = {0.0:(0.0,0.30,1.0,0.45),0.5:(0.0,0.38,1.0,0.40),1.0:(0.40,0.35,0.25,0.40),1.5:(0.0,0.0,0.56,0.96),
2.0:(0.0,0.0,0.80,0.86),2.5:(0.44,0.21,0.56,0.38),3.0:(0.64,0.02,0.36,0.42),3.5:(0.55,0.0,0.45,0.50),
4.0:(0.44,0.0,0.56,0.54),4.5:(0.74,0.41,0.26,0.23),5.0:(0.12,0.05,0.88,0.58),5.5:(0.28,0.24,0.48,0.56),
6.0:(0.38,0.27,0.41,0.47),6.5:(0.37,0.29,0.38,0.45),7.0:(0.40,0.30,0.33,0.43),7.5:(0.34,0.31,0.40,0.43),
8.0:(0.29,0.32,0.42,0.41),8.5:(0.12,0.32,0.38,0.41),9.0:(0.04,0.33,0.18,0.47)}
keys=[{"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in B.items()]
ph=["to shake out a bed sheet","to plump up the pillows","to fold towels into swans"]
c={"mediaId":5056,"level":"B","keyWord":"maid","defaultVoice":"female",
"taps":[{"phrase":p,"target":"the maid","voice":"female","keys":keys} for p in ph],
"stillS":6.0,
"nouns":[{"word":"a maid","x":0.60,"y":0.46,"voice":"female"},{"word":"a cleaning trolley","x":0.22,"y":0.60,"voice":"female"},
{"word":"a balcony","x":0.86,"y":0.58,"voice":"female"},{"word":"a flower","x":0.53,"y":0.70,"voice":"female"}],
"question":"What is the maid folding?",
"answer":["She","is","folding","the","towels","into","swans."],"answerVoice":"female",
"notes":"Only one person, so all three phrases use the maid. Close-ups: 1.5-5.0 s show only her arm/hands (and face at the top edge), boxes follow the visible arm. Sheet 0-1 s, tucks it in 1.5-2 s, punches/plumps pillows 2.5-3.5 s, shapes the towel swan 4-5 s. 'a flower' = the pink frangipani on the swans' necks."}
json.dump(c,open('content/5056.json','w'),indent=1)
