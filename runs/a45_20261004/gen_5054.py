import json
B = {0.0:(0.17,0.16,0.72,0.66),0.5:(0.10,0.17,0.88,0.65),1.0:(0.03,0.31,0.97,0.69),1.5:(0.17,0.16,0.60,0.40),
2.0:(0.15,0.21,0.52,0.26),2.5:(0.18,0.19,0.56,0.27),3.0:(0.11,0.14,0.57,0.42),3.5:(0.01,0.13,0.63,0.66),
4.0:(0.42,0.20,0.58,0.76),4.5:(0.29,0.22,0.71,0.74),5.0:(0.14,0.32,0.86,0.64),5.5:(0.42,0.23,0.58,0.74),
6.0:(0.31,0.23,0.69,0.73),6.5:(0.48,0.17,0.52,0.79),7.0:(0.62,0.17,0.38,0.83),7.5:(0.37,0.19,0.63,0.81),
8.0:(0.28,0.13,0.72,0.87),8.5:(0.13,0.14,0.86,0.86),9.0:(0.16,0.19,0.70,0.81)}
keys=[{"t":t,"x":b[0],"y":b[1],"w":b[2],"h":round(min(b[3],1-b[1]),2)} for t,b in B.items()]
ph=["to shoulder a heavy bag","to push a loaded trolley","to load suitcases into a van"]
c={"mediaId":5054,"level":"B","keyWord":"lift","defaultVoice":"male",
"taps":[{"phrase":p,"target":"the man","voice":"male","keys":keys} for p in ph],
"stillS":2.5,
"nouns":[{"word":"the sky","x":0.50,"y":0.08,"voice":"male"},{"word":"suitcases","x":0.48,"y":0.39,"voice":"male"},
{"word":"a cool box","x":0.40,"y":0.64,"voice":"male"},{"word":"a luggage trolley","x":0.55,"y":0.81,"voice":"male"}],
"question":"What is the man lifting?",
"answer":["He","is","lifting","suitcases","into","the","boot."],"answerVoice":"male",
"notes":"Only one person, so all three phrases use the man. He swings the duffel bag onto his shoulder 0-1 s, pushes the trolley 1.5-3.5 s, loads the van 4-6.5 s. Boxes 1.5-3.0 s cover his upper body above the luggage (legs hidden behind the trolley). 'Lift' is a verb, used in the answer."}
json.dump(c,open('content/5054.json','w'),indent=1)
