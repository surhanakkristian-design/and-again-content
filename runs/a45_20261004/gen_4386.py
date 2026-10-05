import json
def k(t,b): return {"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}
T=[i*0.5 for i in range(25)]
young={0.0:(0.38,0.13,0.62,0.87),0.5:(0.25,0.45,0.75,0.36),1.0:(0.20,0.39,0.80,0.37),1.5:(0.15,0.37,0.85,0.53),2.0:(0.05,0.38,0.95,0.44),2.5:(0.13,0.38,0.87,0.44),3.0:(0.13,0.33,0.87,0.60)}
woman={3.5:(0.0,0.23,1.0,0.42),4.0:(0.27,0.21,0.46,0.47),4.5:(0.19,0.18,0.60,0.44),5.0:(0.24,0.20,0.51,0.42),5.5:(0.24,0.19,0.48,0.42),6.0:(0.29,0.20,0.40,0.40),6.5:(0.31,0.21,0.38,0.38),7.0:(0.31,0.22,0.36,0.37),7.5:(0.31,0.22,0.36,0.37)}
old={8.0:(0.38,0.36,0.22,0.22),8.5:(0.38,0.37,0.24,0.20),9.0:(0.27,0.36,0.44,0.21),9.5:(0.27,0.36,0.42,0.22),10.0:(0.36,0.36,0.22,0.22),10.5:(0.30,0.35,0.34,0.23),11.0:(0.22,0.34,0.53,0.24),11.5:(0.19,0.34,0.59,0.24),12.0:(0.17,0.33,0.64,0.27)}
keys=lambda d:[k(t,d.get(t)) for t in T]
c={"mediaId":4386,"level":"A","keyWord":"poster","defaultVoice":"female",
"taps":[
{"phrase":"to hold a guitar","target":"the young man","voice":"male","keys":keys(young)},
{"phrase":"to make her bed","target":"the woman","voice":"female","keys":keys(woman)},
{"phrase":"to open the curtains","target":"the old man","voice":"male","keys":keys(old)}],
"stillS":2.5,
"nouns":[{"word":"posters","x":0.72,"y":0.22,"voice":"female"},{"word":"a hat","x":0.44,"y":0.44,"voice":"female"},{"word":"a guitar","x":0.21,"y":0.78,"voice":"female"},{"word":"jeans","x":0.76,"y":0.68,"voice":"female"}],
"question":"What is on the young man's walls?",
"answer":["There","are","many","posters","on","his","walls."],
"answerVoice":"female",
"notes":"Three shots, one person each (young man 0-3.0, woman 3.5-7.5, old man 8.0-12.0). defaultVoice female: mixed group, evenId true. The young man holds the guitar only from 1.5 on (it leans on the bed before). 'to make her bed': the woman smooths out a futon on the floor. The old man is small in the picture (back to the camera at 8.0-9.5); his box does not include the curtains. 'a hat' = his dark beanie."}
json.dump(c,open("content/4386.json","w"),indent=1,ensure_ascii=False)
