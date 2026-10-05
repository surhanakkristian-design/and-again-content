import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(L): return [{"t":t,"off":True} if b is None else {"t":t,"x":round(b[0],2),"y":round(b[1],2),"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)} for t,b in zip(T,L)]
WO=[(0,.35,.69,1.0),(0,.35,.69,1.0),(0,.40,.70,1.0),(0,.38,.72,1.0),(0,.40,.70,1.0),(0,.42,.69,1.0),(0,.42,.72,1.0),(0,.42,.71,1.0)]
MA=[(.69,.53,.94,.70),(.69,.56,.97,.71),(.70,.57,.99,.74),(.72,.57,1.0,.74),(.70,.57,.99,.72),(.69,.58,.99,.73),(.72,.59,.99,.74),(.71,.60,.99,.74)]
SN=[(.40,.08,.90,.27),(.40,.08,.86,.26),(.40,.07,.90,.26),(.41,.07,.90,.26),(.42,.06,.92,.27),(.42,.06,.94,.27),(.48,.06,.94,.27),(.56,.06,1.0,.26)]
c={"mediaId":5541,"level":"A","keyWord":"alarm","defaultVoice":"female",
"taps":[
{"phrase":"to look up in fear","target":"the woman","voice":"female","keys":K(WO)},
{"phrase":"to hang over her head","target":"the snake","voice":"female","keys":K(SN)},
{"phrase":"to lie on a green leaf","target":"the mango","voice":"female","keys":K(MA)}],
"stillS":2.2,
"nouns":[{"word":"a snake","x":.70,"y":.20,"voice":"female"},
{"word":"a branch","x":.18,"y":.22,"voice":"female"},
{"word":"a mango","x":.82,"y":.65,"voice":"female"},
{"word":"a hammock","x":.48,"y":.74,"voice":"female"}],
"question":"What is the woman looking at?",
"answer":["She","is","looking","up","at","the","snake."],
"answerVoice":"female",
"notes":"The woman's box is split from the mango box along x ~0.70, so her knees on the far right (x 0.70-0.98, y 0.72-1.0) lie outside her tap box. Her hand rests on the mango at 0.2-1.7 s. Key word 'alarm' is abstract: not a noun slot; 'in alarm' left out of the answer to keep one word order. 'a hammock' pill sits on the visible net between her arm and her trousers."}
json.dump(c,open("content/5541.json","w"),indent=1,ensure_ascii=False)
