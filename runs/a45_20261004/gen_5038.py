import json
T=[i*0.5 for i in range(19)]
W={0.0:(0.16,0.23,0.62,0.77),0.5:(0.18,0.22,0.66,0.78),1.0:(0.16,0.19,0.66,0.81),1.5:(0.13,0.21,0.67,0.79),
2.0:(0.18,0.19,0.62,0.81),2.5:(0.20,0.19,0.64,0.81),3.0:(0.21,0.29,0.55,0.71),3.5:(0.25,0.29,0.52,0.71),
4.0:(0.27,0.25,0.46,0.75),4.5:(0.24,0.37,0.44,0.56),5.0:(0.27,0.36,0.44,0.57),5.5:(0.27,0.29,0.46,0.66),
6.0:(0.31,0.22,0.45,0.68),6.5:(0.29,0.20,0.48,0.73),7.0:(0.27,0.14,0.50,0.81),7.5:(0.24,0.14,0.54,0.84),
8.0:(0.27,0.09,0.51,0.80),8.5:(0.25,0.15,0.56,0.85),9.0:(0.24,0.23,0.55,0.77)}
def keys(d):
    return [{"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True} for t in T]
c={"mediaId":5038,"level":"B","keyWord":"pace","defaultVoice":"female",
"taps":[{"phrase":"to stretch her hamstring","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to run up the staircase","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to keep a steady pace","target":"the woman","voice":"female","keys":keys(W)}],
"stillS":2.0,
"nouns":[{"word":"a watchtower","x":0.55,"y":0.07,"voice":"female"},{"word":"a cap","x":0.47,"y":0.29,"voice":"female"},
{"word":"a running shoe","x":0.38,"y":0.70,"voice":"female"},{"word":"a railing","x":0.80,"y":0.88,"voice":"female"}],
"question":"What is the runner doing?","answer":["She","is","running","at","a","steady","pace."],"answerVoice":"female",
"notes":"Only one real target (the runner); tiny walkers in the background are not tappable, so all three phrases use the woman. 0-2.5 s she stretches with one foot on the railing, 3-9 s she runs up the steps. 'pace' is not a visible noun, used in phrase 3 and the answer. The railing looks like a log/stone rail (description: wooden)."}
json.dump(c,open('content/5038.json','w'),indent=1)
