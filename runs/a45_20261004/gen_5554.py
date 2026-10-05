import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
man=[(0.0,0.33,0.19,0.42),(0.0,0.33,0.20,0.42),(0.0,0.33,0.20,0.42),(0.0,0.33,0.20,0.42),(0.0,0.32,0.20,0.42),(0.0,0.32,0.20,0.42),(0.0,0.32,0.21,0.42),(0.0,0.32,0.21,0.42)]
lil=[(0.20,0.48,0.35,0.48),(0.21,0.48,0.36,0.48),(0.21,0.49,0.36,0.48),(0.21,0.50,0.37,0.49),(0.21,0.50,0.41,0.50),(0.21,0.50,0.40,0.50),(0.22,0.51,0.41,0.49),(0.22,0.52,0.38,0.48)]
yel=[(0.56,0.37,0.38,0.48),(0.58,0.37,0.37,0.48),(0.58,0.38,0.37,0.49),(0.59,0.37,0.38,0.52),(0.63,0.37,0.37,0.53),(0.62,0.37,0.38,0.54),(0.64,0.37,0.36,0.54),(0.61,0.37,0.39,0.54)]
k=lambda L:[{"t":t,"x":a,"y":b,"w":c,"h":d} for t,(a,b,c,d) in zip(T,L)]
c={"mediaId":5554,"level":"A","keyWord":"answer","defaultVoice":"female",
"taps":[
 {"phrase":"to answer his question","target":"the woman by the window","voice":"female","keys":k(yel)},
 {"phrase":"to write in a notebook","target":"the woman in purple","voice":"female","keys":k(lil)},
 {"phrase":"to stand next to the shelves","target":"the man","voice":"male","keys":k(man)}],
"stillS":0.2,
"nouns":[{"word":"a window","x":0.75,"y":0.20,"voice":"female"},
 {"word":"a plant","x":0.28,"y":0.34,"voice":"female"},
 {"word":"a table","x":0.86,"y":0.69,"voice":"female"},
 {"word":"a backpack","x":0.55,"y":0.90,"voice":"female"}],
"question":"What is the woman in purple doing?",
"answer":["She","is","writing","in","a","notebook."],
"answerVoice":"female",
"notes":"'to answer his question' rests on her speaking to the listening man with an open-hand gesture (transcript confirms a reply); check it reads without sound. Man's pen hand sits above the purple woman's head; box split at x 0.20."}
json.dump(c,open("content/5554.json","w"),indent=1)
