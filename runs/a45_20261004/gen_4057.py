import json
T=[i*0.5 for i in range(31)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
man={0.0:(0,0.02,0.95,0.82),0.5:(0,0.04,0.95,0.81),1.0:(0,0.06,0.97,0.81),1.5:(0,0.07,0.95,0.80),2.0:(0,0.08,0.96,0.77),2.5:(0,0.08,1.0,0.77),
3.5:(0.03,0.23,0.27,0.52),4.0:(0.03,0.31,0.54,0.43),4.5:(0.03,0.31,0.54,0.43),5.0:(0.02,0.31,0.52,0.56),5.5:(0.0,0.22,0.18,0.16)}
woman={7.0:(0.03,0.13,0.38,0.77),7.5:(0.05,0.27,0.55,0.55),8.0:(0.15,0.25,0.55,0.57),8.5:(0.17,0.25,0.55,0.57),9.0:(0.15,0.26,0.54,0.66),
9.5:(0.15,0.26,0.55,0.64),10.0:(0.12,0.25,0.56,0.57),10.5:(0.12,0.25,0.56,0.57),11.0:(0.15,0.27,0.53,0.68),11.5:(0.17,0.27,0.48,0.68),
12.0:(0.15,0.26,0.50,0.58),12.5:(0.19,0.26,0.49,0.58),13.0:(0.19,0.25,0.50,0.66),13.5:(0.22,0.25,0.52,0.66),14.0:(0.22,0.24,0.55,0.58),
14.5:(0.19,0.23,0.58,0.59),15.0:(0.15,0.26,0.57,0.68)}
wk=keys(woman)
d={"mediaId":4057,"level":"A","keyWord":"cola","defaultVoice":"male",
"taps":[
{"phrase":"to shake a bottle","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to open the bottle","target":"the woman","voice":"female","keys":wk},
{"phrase":"to get very wet","target":"the woman","voice":"female","keys":wk}],
"stillS":6.0,
"nouns":[{"word":"a roof","x":0.50,"y":0.13,"voice":"male"},{"word":"a door","x":0.30,"y":0.26,"voice":"male"},
{"word":"grass","x":0.22,"y":0.52,"voice":"male"},{"word":"cola","x":0.54,"y":0.61,"voice":"male"}],
"question":"What is the woman opening?",
"answer":["She","is","opening","a","bottle","of","cola."],
"answerVoice":"female",
"notes":"Two people, never in the picture together (man 0-5.5 s, woman from 7.0 s); the bottle is not a tap target because it is held in front of the man / touches the woman. Man is OFF at 3.0, 6.0, 6.5 s (out of frame; only a fingertip at 6.5); at 5.5 s only a slice of his head at the left edge. defaultVoice male: mixed pair, odd id. 'cola' labels the bottle at 6.0 s; 'a roof' is the thin dark roof of the shed."}
json.dump(d,open("content/4057.json","w"),indent=1,ensure_ascii=False)
