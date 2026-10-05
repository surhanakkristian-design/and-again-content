import json
def keys(times, boxes):
    return [{"t":t,"off":True} if boxes.get(t) is None else {"t":t,"x":boxes[t][0],"y":boxes[t][1],"w":boxes[t][2],"h":boxes[t][3]} for t in times]
T=[i*0.5 for i in range(19)]
off={0.0:(0.10,0.03,0.58,0.90),0.5:(0.0,0.05,0.82,0.85),1.0:(0.24,0.05,0.48,0.88),1.5:(0.20,0.07,0.66,0.86),2.0:(0.30,0.12,0.60,0.78),2.5:(0.24,0.19,0.70,0.70),
3.0:(0.48,0.30,0.42,0.62),3.5:(0.49,0.34,0.47,0.58),4.0:(0.69,0.34,0.31,0.46),4.5:(0.73,0.38,0.27,0.38),5.0:(0.82,0.40,0.18,0.34),5.5:(0.80,0.42,0.20,0.34)}
pl={1.0:(0.0,0.10,0.22,0.80),1.5:(0.0,0.10,0.19,0.80),2.0:(0.0,0.15,0.28,0.62),2.5:(0.0,0.20,0.23,0.62),3.0:(0.0,0.30,0.45,0.58),3.5:(0.0,0.34,0.48,0.54),
4.0:(0.0,0.35,0.68,0.40),4.5:(0.0,0.38,0.72,0.35),5.0:(0.0,0.40,0.81,0.33),5.5:(0.0,0.40,0.79,0.32),6.0:(0.0,0.40,1.0,0.34),
6.5:(0.0,0.44,1.0,0.16),7.0:(0.0,0.47,1.0,0.17),7.5:(0.0,0.48,1.0,0.15),8.0:(0.0,0.49,1.0,0.13),8.5:(0.0,0.49,1.0,0.13),9.0:(0.0,0.49,1.0,0.14)}
om={6.5:(0.0,0.60,0.34,0.40),7.0:(0.0,0.65,0.38,0.35),7.5:(0.0,0.63,0.42,0.37),8.0:(0.0,0.62,0.38,0.38),8.5:(0.0,0.62,0.42,0.38),9.0:(0.0,0.63,0.40,0.37)}
c={"mediaId":5063,"level":"A","keyWord":"column","defaultVoice":"male",
"taps":[
 {"phrase":"to lead the band","target":"the officer in front","voice":"male","keys":keys(T,off)},
 {"phrase":"to play music","target":"the band players","voice":"male","keys":keys(T,pl)},
 {"phrase":"to have grey hair","target":"the old man","voice":"male","keys":keys(T,om)}],
"stillS":8.0,
"nouns":[{"word":"a flag","x":0.72,"y":0.26,"voice":"male"},
 {"word":"a tree","x":0.80,"y":0.40,"voice":"male"},
 {"word":"a column","x":0.50,"y":0.55,"voice":"male"},
 {"word":"a man","x":0.18,"y":0.80,"voice":"male"}],
"question":"What is the band doing?",
"answer":["The","band","is","marching","down","the","street."],
"answerVoice":"male",
"notes":"Officer = front man without an instrument (moustache, sword); a second officer marches right behind him at 0-2.5 and is not boxed separately. Officer box ends at 5.5 (small at the right edge); off from 6.0. Band players = the instrument players, a group target; in the long avenue shots (6.5-9.0) they are the tiny ranks of the column. The old man: the child is only a dark head in front of him, so a state phrase (grey hair) is used; no one else with grey hair is visible. Crowd not used (behind the players everywhere)."}
json.dump(c,open('content/5063.json','w'),indent=1)
