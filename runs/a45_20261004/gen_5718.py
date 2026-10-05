import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(lst): return [dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) if b else {"t":t,"off":True} for t,b in zip(T,lst)]
woman=K([(0,.13,.51,.39),(0,.13,.49,.39),(0,.13,.52,.40),(0,.13,.57,.40),(0,.12,.57,.41),(0,.12,.57,.41),(0,.13,.58,.40),(0,.13,.58,.40)])
green=K([(.02,.53,.64,.40)]*8)
blue=K([(.66,.14,.34,.76)]*8)
c={"mediaId":5718,"level":"B","keyWord":"central","defaultVoice":"male",
"taps":[
 {"phrase":"to remove a wooden block","target":"the man in blue","voice":"male","keys":blue},
 {"phrase":"to hold the base steady","target":"the man in green","voice":"male","keys":green},
 {"phrase":"to raise both hands in alarm","target":"the woman","voice":"female","keys":woman}],
"stillS":2.2,
"nouns":[{"word":"a light bulb","x":0.51,"y":0.30,"voice":"male"},{"word":"a tower","x":0.52,"y":0.55,"voice":"male"},
 {"word":"a book","x":0.60,"y":0.83,"voice":"male"},{"word":"a mug","x":0.88,"y":0.93,"voice":"male"}],
"question":"What is the woman doing?",
"answer":["She","is","raising","both","hands","in","alarm."],
"answerVoice":"female",
"notes":"Key word 'central' (adjective) not used as a noun. Woman box cut at y~0.53 above the green man's head; her lower body at the left edge falls in the green man's box. Blue man's hand with the block reaches left of x 0.66 at 0.2-0.7 (kept out to avoid overlap). Mug at the right edge is partly cut off."}
json.dump(c,open('content/5718.json','w'),indent=1)
