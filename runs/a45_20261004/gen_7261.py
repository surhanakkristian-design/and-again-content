import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
man=[(0.44,0.12,0.32,0.86),(0.31,0.14,0.50,0.83),(0.24,0.21,0.56,0.78),(0.31,0.20,0.50,0.80),(0.20,0.17,0.61,0.82),(0.19,0.13,0.64,0.86),(0.33,0.09,0.53,0.91),(0.35,0.08,0.53,0.92)]
wo=[(0.77,0.42,0.23,0.31),(0.82,0.43,0.18,0.31),(0.81,0.46,0.19,0.27),(0.82,0.42,0.18,0.31),(0.82,0.41,0.18,0.31),(0.84,0.40,0.16,0.32),(0.87,0.38,0.13,0.30),(0.89,0.37,0.11,0.30)]
k=lambda b:[{"t":t,"x":x,"y":y,"w":w,"h":h} for t,(x,y,w,h) in zip(T,b)]
d={"mediaId":7261,"level":"B","keyWord":"jean","defaultVoice":"male",
"taps":[{"phrase":"to unroll heavy denim","target":"the man","voice":"male","keys":k(man)},
{"phrase":"to smooth the denim flat","target":"the man","voice":"male","keys":k(man)},
{"phrase":"to sit at a sewing machine","target":"the woman","voice":"female","keys":k(wo)}],
"stillS":2.7,
"nouns":[{"word":"denim","x":0.20,"y":0.72,"voice":"male"},{"word":"a cat","x":0.31,"y":0.47,"voice":"male"},
{"word":"scissors","x":0.38,"y":0.84,"voice":"male"},{"word":"jeans","x":0.70,"y":0.93,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","smoothing","the","denim","flat."],"answerVoice":"male",
"notes":"The man's raised right hand (0.2-0.7 s) and his shoulder (3.2-3.7 s) reach into the woman's area; the boxes split at her left edge, so his raised hand is partly cut and her box is narrow (0.11-0.16 wide) at 2.7-3.7 s where he covers most of her. Phrase 3 has 6 words. Key word 'jean' shown as 'jeans' on the man's legs; 'denim' labels the fabric on the table."}
json.dump(d,open("content/7261.json","w"),indent=1)
