import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes): return [ ({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)}) for t,b in zip(T,boxes)]
RF=[(0.0,0.19,0.45,0.57),(0.0,0.19,0.47,0.57),(0.0,0.20,0.49,0.57),(0.0,0.19,0.48,0.57),(0.0,0.17,0.49,0.57),(0.0,0.15,0.49,0.56),(0.0,0.12,0.49,0.57),(0.0,0.09,0.48,0.57)]
PL=[(0.58,0.21,1.0,0.64),(0.57,0.20,1.0,0.64),(0.55,0.20,1.0,0.66),(0.54,0.19,1.0,0.65),(0.57,0.16,1.0,0.67),(0.56,0.16,1.0,0.67),(0.57,0.13,1.0,0.69),(0.57,0.09,1.0,0.69)]
CO=[(0.39,0.58,0.57,0.74),(0.38,0.58,0.56,0.75),(0.37,0.58,0.55,0.75),(0.35,0.58,0.53,0.75),(0.38,0.58,0.56,0.76),(0.37,0.58,0.55,0.77),(0.38,0.59,0.56,0.77),(0.37,0.59,0.56,0.78)]
c={"mediaId":6938,"level":"B","keyWord":"chance","defaultVoice":"female",
"taps":[{"phrase":"to clench a whistle","target":"the referee","voice":"female","keys":K(RF)},
{"phrase":"to gasp in disbelief","target":"the player","voice":"female","keys":K(PL)},
{"phrase":"to balance on its edge","target":"the coin","voice":"female","keys":K(CO)}],
"stillS":2.7,
"nouns":[{"word":"floodlights","x":0.75,"y":0.10,"voice":"female"},{"word":"a whistle","x":0.28,"y":0.41,"voice":"female"},{"word":"a coin","x":0.48,"y":0.65,"voice":"female"},{"word":"mud","x":0.50,"y":0.88,"voice":"female"}],
"question":"What is the player doing?","answer":["She","is","gasping","in","disbelief."],"answerVoice":"female",
"notes":"Key word 'chance' is abstract, not placed. Player's gasp is clearest from 1.2 s (hand over mouth before). Referee also looks surprised but her mouth holds the whistle; the open-mouthed gasp is only the player's. Player box left edge trimmed to 0.56-0.57 at 2.2-3.7 s so it does not overlap the coin box; edge of her hair falls just outside."}
json.dump(c,open('content/6938.json','w'),ensure_ascii=False,indent=1)
