import json
T=[i*0.5 for i in range(21)]
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":round(d[t][2],2),"h":round(d[t][3],2)} if d.get(t) else {"t":t,"off":True}) for t in T]
M={0.0:(0,0.40,0.57,0.60),0.5:(0,0.41,0.56,0.59),1.0:(0,0.44,0.55,0.56),1.5:(0,0.41,0.53,0.59),2.0:(0,0.38,0.56,0.62),2.5:(0,0.37,0.61,0.63),
3.0:(0,0.38,0.56,0.62),3.5:(0,0.37,0.53,0.63),4.0:(0,0.36,0.42,0.64),4.5:(0,0.39,0.38,0.61),5.0:(0,0.39,0.50,0.61),5.5:(0,0.38,0.52,0.62),
6.0:(0,0.44,0.56,0.56),6.5:(0,0.52,0.55,0.48),7.0:(0,0.57,0.56,0.43),7.5:(0,0.55,0.52,0.45),8.0:(0,0.55,0.55,0.45),8.5:(0,0.57,0.53,0.43),
9.0:(0,0.40,0.49,0.60),9.5:(0,0.35,0.55,0.65),10.0:(0,0.41,0.60,0.59)}
B={0.0:(0.57,0.55,0.43,0.45),0.5:(0.57,0.54,0.43,0.46),1.0:(0.56,0.55,0.44,0.45),1.5:(0.54,0.52,0.44,0.48),2.0:(0.57,0.53,0.43,0.47),2.5:(0.62,0.57,0.36,0.43),
3.0:(0.57,0.69,0.43,0.31),3.5:(0.54,0.57,0.38,0.43),4.0:(0.42,0.54,0.47,0.46),4.5:(0.42,0.54,0.58,0.46),5.0:(0.53,0.57,0.47,0.43),5.5:(0.53,0.56,0.47,0.44),
6.0:(0.57,0.52,0.43,0.48),6.5:(0.55,0.54,0.45,0.46),7.0:(0.57,0.58,0.43,0.42),7.5:(0.56,0.60,0.44,0.40),8.0:(0.56,0.62,0.44,0.38),8.5:(0.55,0.63,0.45,0.37),
9.0:(0.50,0.43,0.50,0.57),9.5:(0.56,0.45,0.44,0.55),10.0:(0.60,0.56,0.40,0.44)}
S={5.0:(0.14,0.21,0.35,0.16),5.5:(0.40,0.20,0.34,0.17),6.0:(0.39,0.26,0.33,0.16),6.5:(0.36,0.25,0.34,0.16),7.0:(0.36,0.20,0.34,0.16),7.5:(0.36,0.16,0.34,0.16),
8.0:(0.34,0.16,0.36,0.16),8.5:(0.34,0.19,0.36,0.17),9.0:(0.34,0.25,0.34,0.15),9.5:(0.38,0.21,0.34,0.14),10.0:(0.38,0.20,0.36,0.17)}
c={"mediaId":47,"level":"B","keyWord":"arena","defaultVoice":"male",
"taps":[{"phrase":"to pump his fist","target":"the man","voice":"male","keys":keys(M)},
{"phrase":"to toss popcorn into the air","target":"the boy","voice":"male","keys":keys(B)},
{"phrase":"to hang above the court","target":"the scoreboard","voice":"male","keys":keys(S)}],
"stillS":8.0,
"nouns":[{"word":"a scoreboard","x":0.52,"y":0.24,"voice":"male"},{"word":"spectators","x":0.80,"y":0.44,"voice":"male"},
{"word":"a court","x":0.45,"y":0.53,"voice":"male"},{"word":"popcorn","x":0.67,"y":0.79,"voice":"male"}],
"question":"Where are the man and the boy?",
"answer":["They","are","inside","a","packed","arena."],"answerVoice":"male",
"notes":"The man and the boy stand shoulder to shoulder, so their boxes are split along the line between them. The man pumps his fist only at 9.0-10.0 (at 10.0 he raises both fists; the boy raises open arms). The popcorn flies at 9.5-10.0 (bucket in the air at 10.0, inside the boy's box). The scoreboard = the grey video cube under the roof, visible from 5.0. 'spectators' pill sits on the stands on the right; spectators are of course all around. The key word 'arena' cannot be one label place, so it is in the model answer; the answer's subject is 'They' -> default voice. Other spectators (a man in black at 2.0-2.5 beside the boy) fall inside the boy's box."}
json.dump(c,open('content/47.json','w'),indent=1)
