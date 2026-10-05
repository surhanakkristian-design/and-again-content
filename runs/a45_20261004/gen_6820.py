import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def keys(bs): return [{"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)} for t,b in zip(T,bs)]
adult=[(0,.18,1.0,.63),(0,.18,1.0,.64),(0,.16,1.0,.67),(0,.16,1.0,.67),(0,.11,1.0,.69),(0,.12,1.0,.70),(0,.10,1.0,.69),(0,.08,1.0,.68)]
baby=[(.15,.63,.67,.92),(.19,.64,.71,.93),(.14,.67,.73,.93),(.40,.67,.86,.93),(.37,.69,.76,.94),(.33,.70,.86,.95),(.44,.69,.92,.95),(.41,.68,.87,.95)]
c={"mediaId":6820,"level":"B","keyWord":"adult","defaultVoice":"female",
"taps":[
{"phrase":"to stroke the calf's back","target":"the adult elephant","voice":"female","keys":keys(adult)},
{"phrase":"to trot beside the adult","target":"the baby elephant","voice":"female","keys":keys(baby)},
{"phrase":"to raise its short trunk","target":"the baby elephant","voice":"female","keys":keys(baby)}],
"stillS":0.2,
"nouns":[{"word":"an adult","x":0.28,"y":0.34,"voice":"female"},{"word":"an acacia tree","x":0.86,"y":0.27,"voice":"female"},{"word":"tusks","x":0.80,"y":0.54,"voice":"female"},{"word":"a calf","x":0.35,"y":0.76,"voice":"female"}],
"question":"What is the adult elephant doing?",
"answer":["It","is","stroking","the","calf's","back."],
"answerVoice":"female",
"notes":"The calf walks under / in front of the adult, so the two overlap in the picture: boxes split along the calf's top line (the adult's legs below that line fall into no box or the calf's). The adult also swings and lifts its own (long) trunk at 0.7-1.7; phrase 3 says 'short trunk' to keep it on the calf. The stroking happens at 2.2-2.7."}
json.dump(c,open('content/6820.json','w'),indent=1)
