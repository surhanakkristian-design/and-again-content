import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
woman={0.0:(0.42,0.02,0.58,0.34),0.5:(0.48,0.20,0.52,0.20),1.0:(0.40,0.0,0.60,1.0),1.5:(0.33,0.17,0.67,0.80),2.0:(0.33,0.50,0.67,0.47),
 2.5:(0.25,0.74,0.75,0.26),3.0:(0.20,0.82,0.80,0.18),3.5:(0.20,0.82,0.80,0.18),4.0:(0.22,0.44,0.78,0.46),4.5:(0.40,0.0,0.60,0.26),
 5.0:(0.66,0.48,0.34,0.50),5.5:(0.24,0.28,0.76,0.72),6.0:(0.20,0.25,0.80,0.75),6.5:(0.42,0.24,0.58,0.76),7.0:(0.50,0.23,0.50,0.77),
 7.5:(0.55,0.23,0.45,0.77),8.0:(0.68,0.25,0.32,0.75),8.5:(0.58,0.26,0.42,0.74),9.0:(0.0,0.02,0.80,0.98),9.5:(0.0,0.25,0.54,0.75),
 10.0:(0.07,0.33,0.42,0.67)}
man={8.0:(0.0,0.20,0.48,0.80),8.5:(0.0,0.25,0.56,0.75),9.5:(0.54,0.35,0.20,0.55),10.0:(0.49,0.36,0.27,0.44)}
cow={0.0:(0.60,0.36,0.22,0.14),0.5:(0.60,0.40,0.20,0.14),4.5:(0.78,0.36,0.22,0.14),6.5:(0.24,0.43,0.18,0.14),7.0:(0.32,0.39,0.18,0.14),
 7.5:(0.37,0.37,0.18,0.14),8.0:(0.48,0.36,0.20,0.14),9.0:(0.80,0.37,0.20,0.14),9.5:(0.74,0.37,0.26,0.20),10.0:(0.78,0.37,0.22,0.22)}
c={"mediaId":863,"level":"A","keyWord":"water bottle","defaultVoice":"female",
"taps":[
 {"phrase":"to drink from a bottle","target":"the woman","voice":"female","keys":keys(woman)},
 {"phrase":"to wear a grey T-shirt","target":"the man","voice":"male","keys":keys(man)},
 {"phrase":"to stand on the grass","target":"the cow","voice":"female","keys":keys(cow)}],
"stillS":7.0,
"nouns":[{"word":"the sky","x":0.72,"y":0.12,"voice":"female"},{"word":"mountains","x":0.40,"y":0.30,"voice":"female"},
 {"word":"flowers","x":0.24,"y":0.53,"voice":"female"},{"word":"a water bottle","x":0.47,"y":0.62,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","drinking","from","a","water","bottle."],
"answerVoice":"female",
"notes":"Many shots are POV close-ups where only the woman's hand / pink sleeve is in the picture; her box sits on the hand and arm there. The man appears only from 8.0 (left edge, high five) and from behind at 9.5-10.0, so his phrase is a state (grey T-shirt). The cow is tiny in the background until 9.0; boxes at minimum size, off where it is hidden behind the woman's arm or not identifiable (1.0-4.0, 5.0-6.0, 8.5). At 9.0 a hand with a pink sleeve at the top right is outside the woman's box (cannot be attributed safely). The description does not mention the man."}
json.dump(c,open("content/863.json","w"),indent=1)
