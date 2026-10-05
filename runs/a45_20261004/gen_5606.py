import json
T=[0.2,0.7,1.2,1.7,2.2]
BAT={0.2:(0.60,0.18,0.40,0.73),0.7:(0.82,0.17,0.18,0.75),1.2:(0.82,0.16,0.18,0.76),1.7:(0.82,0.16,0.18,0.76),2.2:None}
PIT={0.2:(0.32,0.47,0.28,0.19),0.7:(0.32,0.46,0.30,0.20),1.2:(0.46,0.44,0.18,0.22),1.7:(0.48,0.43,0.20,0.23),2.2:(0.50,0.42,0.21,0.24)}
BALL={0.2:(0.26,0.33,0.18,0.14),0.7:(0.20,0.30,0.18,0.14),1.2:(0.18,0.30,0.18,0.14),1.7:(0.16,0.32,0.18,0.14),2.2:(0.14,0.35,0.18,0.14)}
keys=lambda D:[({"t":t,"off":True} if D[t] is None else dict(t=t,**dict(zip("xywh",D[t])))) for t in T]
d={"mediaId":5606,"level":"B","keyWord":"batting","defaultVoice":"male",
"taps":[
 {"phrase":"to swing a wooden bat","target":"the batter","voice":"male","keys":keys(BAT)},
 {"phrase":"to turn round on the mound","target":"the pitcher","voice":"male","keys":keys(PIT)},
 {"phrase":"to soar into the night sky","target":"the ball","voice":"male","keys":keys(BALL)}],
"stillS":1.2,
"nouns":[{"word":"the sky","x":0.40,"y":0.12,"voice":"male"},
 {"word":"palm trees","x":0.15,"y":0.47,"voice":"male"},
 {"word":"a grandstand","x":0.78,"y":0.50,"voice":"male"},
 {"word":"home plate","x":0.50,"y":0.94,"voice":"male"}],
"question":"What is the ball doing?",
"answer":["The","ball","is","soaring","into","the","night","sky."],
"answerVoice":"male",
"notes":"Swing visible only at 0.2 s (ball already hit); batter is a sliver at the right edge after that and off at 2.2 s. Ball is tiny: minimum boxes kept above the pitcher's box (ball box bottom = pitcher box top at 0.2 s). Ball rises then drifts down among the palms in the image as it flies away (perspective) - 'soar into the night sky' follows the description. 'home plate' without article (fixed term)."}
json.dump(d,open("content/5606.json","w"),indent=1)
