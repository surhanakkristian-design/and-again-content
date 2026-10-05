import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def k(t,b): return {"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}
W=[(0.27,0.28,0.47,0.56),(0.27,0.28,0.47,0.56),(0.25,0.28,0.48,0.56),(0.25,0.28,0.48,0.56),(0.29,0.28,0.48,0.60),(0.29,0.28,0.48,0.60),(0.27,0.28,0.50,0.62),(0.26,0.28,0.53,0.64)]
M=[(0.01,0.35,0.20,0.38),(0.01,0.35,0.20,0.38),(0.0,0.35,0.20,0.50),(0.0,0.35,0.20,0.50),(0.0,0.35,0.19,0.38),(0.0,0.35,0.19,0.38),(0.0,0.36,0.18,0.50),(0.0,0.36,0.18,0.50)]
wk=[k(t,b) for t,b in zip(T,W)]; mk=[k(t,b) for t,b in zip(T,M)]
d={"mediaId":7342,"level":"B","keyWord":"membrane","defaultVoice":"female",
"taps":[{"phrase":"to press against the membrane","target":"the woman","voice":"female","keys":wk},
{"phrase":"to keep her eyes closed","target":"the woman","voice":"female","keys":wk},
{"phrase":"to cover his mouth in shock","target":"the man","voice":"male","keys":mk}],
"stillS":0.7,
"nouns":[{"word":"a wooden frame","x":0.36,"y":0.10,"voice":"female"},{"word":"a membrane","x":0.60,"y":0.22,"voice":"female"},
{"word":"a man","x":0.12,"y":0.50,"voice":"male"},{"word":"a floor light","x":0.82,"y":0.87,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","pushing","her","face","into","the","membrane."],"answerVoice":"female",
"notes":"Woman is seen through the milky sheet; her lower body fades into the glow, box down to the hem. Man stands at the far left edge in shadow; box clipped at x=0. Membrane pill placed on the empty upper sheet, away from the woman."}
json.dump(d,open('content/7342.json','w'),indent=1)
